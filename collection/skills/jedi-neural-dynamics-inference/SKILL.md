---
name: jedi-neural-dynamics-inference
description: "JEDI: Jointly Embedded Inference of Neural Dynamics - learning shared embeddings of RNN weights to infer neural population dynamics across tasks and contexts. Triggers: neural dynamics inference, RNN embedding, meta-learning, neural population, cross-task generalization."
---

# JEDI: Jointly Embedded Inference of Neural Dynamics

> A meta-learning framework that learns shared embeddings of RNN weights to infer neural population dynamics across different tasks and contexts, enabling identification of task-specific dynamical rules from limited, noisy neural data.

## Metadata
- **Source**: arXiv:2603.10489v1
- **Authors**: Aniruddh Galgali, Saurabh Vyas, Vivek Jayaram, et al.
- **Published**: 2026-03-11
- **Institution**: Carnegie Mellon University, University of Washington, Columbia University

## Core Methodology

### Key Innovation
Animal brains flexibly achieve diverse behavioral tasks using a single neural network with shared anatomical structure. JEDI (Jointly Embedded Inference of Neural Dynamics) formalizes this biological insight by learning a shared latent space of recurrent neural network (RNN) weights. This enables: (1) identifying task-specific dynamical motifs from limited neural recordings, (2) inferring latent dynamics in novel tasks without retraining, and (3) predicting neural responses under novel stimulus conditions.

### Theoretical Framework

#### Problem Formulation
Given:
- Neural recordings {Xᵗ} from multiple tasks t ∈ {1,...,T}
- Task descriptions or context variables {cᵗ}
- Limited data per task (few trials)

Goal: Infer the underlying dynamical system for each task:
```
ẋ = f(x, u; θᵗ) + noise
where θᵗ are task-specific parameters
```

#### Joint Embedding Approach
Instead of learning each task independently, JEDI learns:
```
θᵗ = decoder(zᵗ)  where zᵗ ∈ R^d (low-dimensional embedding)
```

All tasks share the same decoder, but have unique embeddings zᵗ.

#### Neural Architecture

**Encoder Network** (weights → embedding):
```python
class WeightEncoder(nn.Module):
    """Encode RNN weights into latent embedding"""
    
    def __init__(self, weight_dim, latent_dim):
        super().__init__()
        # Weight encoder
        self.encoder = nn.Sequential(
            nn.Linear(weight_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * 2)  # μ and σ
        )
    
    def forward(self, weights):
        """
        Args:
            weights: flattened RNN parameters
        Returns:
            z_mean, z_std: latent distribution parameters
        """
        out = self.encoder(weights)
        z_mean = out[:, :latent_dim]
        z_std = F.softplus(out[:, latent_dim:]) + 1e-4
        return z_mean, z_std
```

**Decoder Network** (embedding → dynamics):
```python
class DynamicsDecoder(nn.Module):
    """Decode latent embedding into RNN dynamics"""
    
    def __init__(self, latent_dim, state_dim, input_dim, hidden_dim):
        super().__init__()
        self.latent_dim = latent_dim
        self.state_dim = state_dim
        
        # Generate RNN parameters from latent code
        self.w_hh_generator = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, state_dim * state_dim)
        )
        
        self.w_xh_generator = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, state_dim * input_dim)
        )
        
        self.b_h_generator = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, state_dim)
        )
    
    def generate_rnn_params(self, z):
        """Generate RNN weight matrices from latent code"""
        W_hh = self.w_hh_generator(z).view(-1, self.state_dim, self.state_dim)
        W_xh = self.w_xh_generator(z).view(-1, self.state_dim, self.input_dim)
        b_h = self.b_h_generator(z)
        return W_hh, W_xh, b_h
    
    def forward(self, z, x, u):
        """
        Args:
            z: latent embedding (batch, latent_dim)
            x: current state (batch, state_dim)
            u: input (batch, input_dim)
        Returns:
            dx: state update
        """
        W_hh, W_xh, b_h = self.generate_rnn_params(z)
        
        # RNN dynamics: dx/dt = -x + tanh(W_hh @ x + W_xh @ u + b_h)
        dx = -x + torch.tanh(
            torch.bmm(W_hh, x.unsqueeze(-1)).squeeze(-1) +
            torch.bmm(W_xh, u.unsqueeze(-1)).squeeze(-1) +
            b_h
        )
        return dx
```

### Training Objective

#### Evidence Lower Bound (ELBO)
```
L = E_q(z|weights)[log p(data|z)] - β * KL(q(z|weights) || p(z))
```

Where:
- First term: reconstruction accuracy (predicted vs. actual neural activity)
- Second term: KL divergence keeping embeddings close to prior
- β: regularization coefficient (β-VAE approach)

#### Contrastive Task Loss
To encourage task-discriminative embeddings:
```python
def contrastive_task_loss(embeddings, task_labels, temperature=0.1):
    """
    InfoNCE loss for task discrimination
    
    Args:
        embeddings: (batch, latent_dim)
        task_labels: (batch,) integer task identifiers
    """
    # Normalize embeddings
    embeddings = F.normalize(embeddings, dim=1)
    
    # Compute similarity matrix
    similarity = torch.matmul(embeddings, embeddings.t()) / temperature
    
    # Mask out self-similarity
    mask = torch.eye(len(embeddings), device=embeddings.device).bool()
    similarity = similarity.masked_fill(mask, -float('inf'))
    
    # Positive pairs: same task
    task_mask = task_labels.unsqueeze(0) == task_labels.unsqueeze(1)
    task_mask = task_mask & ~mask  # Exclude diagonal
    
    # Contrastive loss
    loss = 0
    for i in range(len(embeddings)):
        pos_sim = similarity[i][task_mask[i]].mean()
        neg_sim = similarity[i][~task_mask[i]].mean()
        loss -= torch.log(torch.exp(pos_sim) / 
                         (torch.exp(pos_sim) + torch.exp(neg_sim)))
    
    return loss / len(embeddings)
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch 1.10+
- NumPy, SciPy for data handling
- scikit-learn for preprocessing

### Step-by-Step: Training JEDI

1. **Data Preparation**
```python
import numpy as np
import torch
from torch.utils.data import Dataset

class NeuralDynamicsDataset(Dataset):
    """Dataset for neural population recordings across tasks"""
    
    def __init__(self, recordings, task_labels, trial_info):
        """
        Args:
            recordings: List of (time, neurons) arrays, one per trial
            task_labels: Task identifier for each trial
            trial_info: Dict with condition, stimulus, etc.
        """
        self.recordings = recordings
        self.task_labels = task_labels
        self.trial_info = trial_info
        
        # Bin data and compute firing rates
        self.binned_data = []
        for rec in recordings:
            # Bin at 20ms
            bin_size = 20
            n_bins = len(rec) // bin_size
            binned = rec[:n_bins * bin_size].reshape(n_bins, bin_size, -1)
            firing_rates = binned.mean(axis=1)  # (n_bins, neurons)
            self.binned_data.append(firing_rates)
    
    def __len__(self):
        return len(self.binned_data)
    
    def __getitem__(self, idx):
        return {
            'activity': torch.tensor(self.binned_data[idx], dtype=torch.float32),
            'task': torch.tensor(self.task_labels[idx], dtype=torch.long),
            'length': len(self.binned_data[idx])
        }
```

2. **JEDI Model Definition**
```python
import torch.nn as nn
import torch.nn.functional as F

class JEDI(nn.Module):
    """Jointly Embedded Inference of Neural Dynamics"""
    
    def __init__(self, n_neurons, latent_dim, rnn_hidden_dim, n_tasks):
        super().__init__()
        self.n_neurons = n_neurons
        self.latent_dim = latent_dim
        self.rnn_hidden_dim = rnn_hidden_dim
        
        # Weight encoder (infers dynamics from data)
        weight_dim = rnn_hidden_dim * rnn_hidden_dim + rnn_hidden_dim * n_neurons + rnn_hidden_dim
        self.encoder = WeightEncoder(weight_dim, latent_dim)
        
        # Dynamics decoder (generates RNN from latent code)
        self.decoder = DynamicsDecoder(latent_dim, rnn_hidden_dim, n_neurons, 256)
        
        # Observation model (neural firing rates)
        self.observation = nn.Linear(rnn_hidden_dim, n_neurons)
    
    def forward(self, neural_data, task_id=None):
        """
        Args:
            neural_data: (batch, time, neurons)
            task_id: (batch,) optional task labels
        Returns:
            predicted_activity, z_mean, z_std, z_sample
        """
        batch_size, time_steps, _ = neural_data.shape
        
        # Infer latent embedding from data
        # (In practice, amortized inference or variational approach)
        z_mean, z_std, z_sample = self.infer_latent(neural_data)
        
        # Generate RNN parameters
        W_hh, W_xh, b_h = self.decoder.generate_rnn_params(z_sample)
        
        # Run dynamics forward
        h = torch.zeros(batch_size, self.rnn_hidden_dim, device=neural_data.device)
        predicted_rates = []
        
        for t in range(time_steps):
            # Input at time t
            u = neural_data[:, t, :]  # (batch, neurons)
            
            # RNN update
            dh = -h + torch.tanh(
                torch.bmm(W_hh, h.unsqueeze(-1)).squeeze(-1) +
                torch.bmm(W_xh, u.unsqueeze(-1)).squeeze(-1) +
                b_h
            )
            h = h + 0.05 * dh  # Euler integration
            
            # Predict firing rates
            rates = F.softplus(self.observation(h))
            predicted_rates.append(rates)
        
        predicted_activity = torch.stack(predicted_rates, dim=1)
        
        return predicted_activity, z_mean, z_std, z_sample
    
    def infer_latent(self, neural_data):
        """Infer latent embedding from neural data"""
        # Amortized inference: encode statistics of data
        data_mean = neural_data.mean(dim=1)  # (batch, neurons)
        data_std = neural_data.std(dim=1)
        
        # Simple MLP encoder
        stats = torch.cat([data_mean, data_std], dim=1)
        h = F.relu(self.inference_mlp(stats))
        
        z_mean = self.z_mean_layer(h)
        z_std = F.softplus(self.z_std_layer(h)) + 1e-4
        
        # Reparameterization
        eps = torch.randn_like(z_std)
        z_sample = z_mean + eps * z_std
        
        return z_mean, z_std, z_sample
```

3. **Training Loop**
```python
def train_jedi(model, train_loader, n_epochs=500, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=50)
    
    for epoch in range(n_epochs):
        total_loss = 0
        total_recon = 0
        total_kl = 0
        
        for batch in train_loader:
            neural_data = batch['activity']
            task_labels = batch['task']
            
            # Forward pass
            predicted, z_mean, z_std, z_sample = model(neural_data, task_labels)
            
            # Reconstruction loss
            recon_loss = F.poisson_nll_loss(
                predicted, neural_data, log_input=False, reduction='mean'
            )
            
            # KL divergence
            kl_loss = -0.5 * torch.sum(
                1 + torch.log(z_std.pow(2)) - z_mean.pow(2) - z_std.pow(2)
            ) / len(neural_data)
            
            # Contrastive task loss
            contrastive_loss = contrastive_task_loss(z_sample, task_labels)
            
            # Total loss
            loss = recon_loss + 0.01 * kl_loss + 0.1 * contrastive_loss
            
            # Backward
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            
            total_loss += loss.item()
            total_recon += recon_loss.item()
            total_kl += kl_loss.item()
        
        scheduler.step(total_loss)
        
        if epoch % 50 == 0:
            print(f"Epoch {epoch}: Loss={total_loss/len(train_loader):.4f}, "
                  f"Recon={total_recon/len(train_loader):.4f}, "
                  f"KL={total_kl/len(train_loader):.4f}")
    
    return model
```

4. **Cross-Task Inference**
```python
def infer_new_task(model, new_task_data, n_steps=100):
    """Infer latent dynamics for a new, unseen task"""
    
    # Optimize task-specific embedding
    z = nn.Parameter(torch.randn(1, model.latent_dim))
    optimizer = torch.optim.Adam([z], lr=0.01)
    
    for step in range(n_steps):
        optimizer.zero_grad()
        
        # Generate dynamics from z
        predicted = model.generate_from_z(z, new_task_data.shape[1])
        
        # Compute reconstruction loss
        loss = F.poisson_nll_loss(predicted, new_task_data, log_input=False)
        
        loss.backward()
        optimizer.step()
    
    return z.detach()
```

## Applications

### 1. Multi-Task Brain-Computer Interfaces
- **Task identification**: Infer which task subject is performing from neural activity
- **Adaptive decoding**: Adjust decoder based on inferred task context
- **Error detection**: Identify when subject switches tasks unexpectedly

### 2. Cognitive Neuroscience
- **Task representation**: Understand how brain represents different cognitive tasks
- **Mental flexibility**: Study how brain switches between task sets
- **Working memory**: Infer maintenance dynamics across different memory tasks

### 3. Computational Psychiatry
- **Cognitive flexibility deficits**: Model reduced task-switching in disorders
- **Biomarker discovery**: Identify aberrant neural dynamics signatures
- **Treatment monitoring**: Track changes in neural flexibility with intervention

### 4. Brain-Inspired AI
- **Meta-learning**: Transfer learning strategies across related tasks
- **Continual learning**: Prevent catastrophic forgetting through shared representations
- **Few-shot adaptation**: Rapid adaptation to new tasks with limited data

## Pitfalls

### Identifiability Issues
- **Problem**: Multiple RNN parameterizations can produce similar dynamics
- **Solution**: Add regularization favoring simple solutions; use observational constraints

### Limited Data Per Task
- **Problem**: Few trials per task make inference unreliable
- **Solution**: Strong priors from other tasks; hierarchical Bayesian approach; data augmentation

### Non-Stationarity
- **Problem**: Neural dynamics drift over time (learning, fatigue)
- **Solution**: Include time as a covariate; online adaptation of embeddings

### Causal Interpretation
- **Problem**: Correlation between tasks doesn't imply shared mechanisms
- **Solution**: Validate with perturbation experiments; lesion studies in silico

## Related Skills
- meta-learning-in-context-brain-decoding: Meta-learning for brain decoding
- neural-population-dynamics: Neural population dynamics analysis
- attractor-metadynamics-neural: Attractor landscape evolution in neural networks

## References
```bibtex
@article{galgali2026jedi,
  title={JEDI: Jointly Embedded Inference of Neural Dynamics},
  author={Galgali, Aniruddh and Vyas, Saurabh and Jayaram, Vivek and others},
  journal={arXiv preprint arXiv:2603.10489},
  year={2026}
}
```
