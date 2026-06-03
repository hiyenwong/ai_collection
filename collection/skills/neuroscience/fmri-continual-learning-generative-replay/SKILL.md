---
name: fmri-continual-learning-generative-replay
description: "Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay (FC-GR). A continual learning framework for multi-site fMRI brain disorder diagnosis using graph variational autoencoder (GVAE) to generate synthetic FC matrices. Includes curriculum-based replay strategy and consistency loss for cross-site knowledge preservation. Activation: fMRI continual learning, brain disorder diagnosis, functional connectivity generative replay, multi-site fMRI learning, catastrophic forgetting prevention in neuroimaging, GVAE brain connectivity."
version: v1.0.0
last_updated: 2026-04-17
source_paper: "Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay (arXiv:2604.14259)"
---

# fMRI Continual Learning with Generative Replay

Continual learning framework for brain disorder diagnosis using generative replay of functional connectivity matrices.

## Problem Statement

Existing fMRI diagnostic models are trained on single sites or require full multi-site access, making them unsuitable for:
- Sequential data arrival from multiple institutions
- Privacy-preserving distributed learning
- Adaptive learning with new patient populations

## FC-GR Framework

```
Task 1 → Task 2 → Task 3 → ... → Task N
   │        │        │              │
   ▼        ▼        ▼              ▼
GVAE learns FC matrix distribution + generates synthetic samples
   │
   ▼
Classifier trained on Real Data + Synthetic Replay
(Curriculum-based sampling)
```

## Core Components

### 1. Graph Variational Autoencoder (GVAE)

```python
class FC_GVAE(nn.Module):
    def __init__(self, num_rois=116, hidden_dim=256, latent_dim=64):
        super().__init__()
        self.num_rois = num_rois
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(num_rois * num_rois, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_rois * num_rois),
            nn.Tanh()
        )
    
    def encode(self, fc_matrix):
        batch_size = fc_matrix.size(0)
        x = fc_matrix.view(batch_size, -1)
        h = self.encoder(x)
        return self.fc_mu(h), self.fc_logvar(h)
    
    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z):
        batch_size = z.size(0)
        fc_flat = self.decoder(z)
        fc_matrix = fc_flat.view(batch_size, self.num_rois, self.num_rois)
        # Symmetrize
        fc_matrix = (fc_matrix + fc_matrix.transpose(-2, -1)) / 2
        # Zero diagonal
        mask = torch.eye(self.num_rois).bool()
        fc_matrix = fc_matrix.masked_fill(mask, 0)
        return fc_matrix
```

### 2. Consistency Loss

```python
class ConsistencyLoss(nn.Module):
    def forward(self, real_fc, generated_fc):
        losses = {}
        
        # Mean connectivity strength
        losses['mean'] = F.mse_loss(
            real_fc.mean(dim=[1, 2]),
            generated_fc.mean(dim=[1, 2])
        )
        
        # Connectivity variance
        losses['variance'] = F.mse_loss(
            real_fc.var(dim=[1, 2]),
            generated_fc.var(dim=[1, 2])
        )
        
        # Node strength distribution
        real_strength = real_fc.sum(dim=2)
        gen_strength = generated_fc.sum(dim=2)
        losses['node_strength'] = F.mse_loss(real_strength, gen_strength)
        
        return sum(losses.values())
```

### 3. Curriculum-Based Replay

```python
class CurriculumReplay:
    def __init__(self, buffer_size=1000, n_classes=2):
        self.buffer_size = buffer_size
        self.n_classes = n_classes
        self.replay_buffer = []
        self.class_counts = np.zeros(n_classes)
    
    def update_buffer(self, new_fc_matrices, new_labels, gvae):
        with torch.no_grad():
            mu, _ = gvae.encode(new_fc_matrices)
            latents = mu.cpu().numpy()
        
        for fc, label, latent in zip(new_fc_matrices, new_labels, latents):
            self.replay_buffer.append({
                'latent': latent,
                'label': label.item(),
                'count': self.class_counts[label.item()]
            })
            self.class_counts[label.item()] += 1
        
        if len(self.replay_buffer) > self.buffer_size:
            self.replay_buffer = self.replay_buffer[-self.buffer_size:]
    
    def sample(self, n_samples, gvae):
        if len(self.replay_buffer) == 0:
            return None, None
        
        # Inverse frequency sampling
        class_probs = 1.0 / (self.class_counts + 1)
        class_probs = class_probs / class_probs.sum()
        
        sampled_classes = np.random.choice(
            self.n_classes, size=n_samples, p=class_probs
        )
        
        sampled_data = []
        for cls in sampled_classes:
            class_samples = [s for s in self.replay_buffer if s['label'] == cls]
            if len(class_samples) > 0:
                sample = min(class_samples, key=lambda x: x['count'])
                sampled_data.append(sample)
        
        if len(sampled_data) > 0:
            latents = torch.FloatTensor([s['latent'] for s in sampled_data])
            with torch.no_grad():
                fc_matrices = gvae.decode(latents.to(gvae.fc_mu.weight.device))
            labels = torch.LongTensor([s['label'] for s in sampled_data])
            return fc_matrices, labels
        
        return None, None
```

## Training Workflow

```python
def train_fc_gr(gvae, classifier, datasets, num_epochs=50):
    gvae_optimizer = Adam(gvae.parameters(), lr=1e-3)
    clf_optimizer = Adam(classifier.parameters(), lr=1e-4)
    consistency_loss_fn = ConsistencyLoss()
    curriculum_replay = CurriculumReplay(buffer_size=1000)
    
    for task_id, (fc_data, labels) in enumerate(datasets):
        loader = DataLoader(TensorDataset(fc_data, labels), batch_size=32)
        
        for epoch in range(num_epochs):
            for batch_fc, batch_labels in loader:
                # Train GVAE
                recon, mu, logvar = gvae(batch_fc)
                gvae_loss = gvae_loss_fn(recon, batch_fc, mu, logvar)
                
                replay_fc, _ = curriculum_replay.sample(16, gvae)
                if replay_fc is not None:
                    recon_replay, mu_r, logvar_r = gvae(replay_fc)
                    gvae_loss += 0.1 * consistency_loss_fn(replay_fc, recon_replay)
                
                gvae_optimizer.zero_grad()
                gvae_loss.backward()
                gvae_optimizer.step()
                
                # Train Classifier
                real_logits = classifier(batch_fc)
                real_loss = F.cross_entropy(real_logits, batch_labels)
                
                replay_loss = 0
                if replay_fc is not None:
                    replay_logits = classifier(replay_fc)
                    replay_loss = F.cross_entropy(replay_logits, replay_labels)
                
                clf_loss = real_loss + 0.5 * replay_loss
                clf_optimizer.zero_grad()
                clf_loss.backward()
                clf_optimizer.step()
            
            curriculum_replay.update_buffer(fc_data, labels, gvae)
```

## Performance Metrics

| Method | Average Accuracy Retention |
|--------|---------------------------|
| Naive Fine-tuning | 42.1% |
| Experience Replay | 68.5% |
| **FC-GR (Ours)** | **87.3%** |

## Datasets Evaluated

- **Alzheimer's Disease**: Multi-site fMRI datasets
- **Autism Spectrum Disorder**: ABIDE I & II
- **Schizophrenia**: COBRE, UCLA datasets

## Activation Keywords

- fMRI continual learning
- Brain disorder diagnosis
- Functional connectivity generative replay
- Multi-site fMRI learning
- Catastrophic forgetting prevention in neuroimaging
- GVAE brain connectivity, FC-GR framework

## Tools Used

- `python`: PyTorch, PyTorch Geometric
- `numpy`: Matrix operations
- `nilearn`: FC matrix computation
- `scikit-learn`: Evaluation metrics

## References

- Paper: [arXiv:2604.14259](https://arxiv.org/abs/2604.14259)
