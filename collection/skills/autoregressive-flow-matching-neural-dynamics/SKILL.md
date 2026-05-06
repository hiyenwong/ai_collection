---
name: autoregressive-flow-matching-neural-dynamics
description: "Autoregressive Flow Matching (AFM) for probabilistic prediction of neural dynamics. Generative framework combining autoregressive models with flow matching for forecasting neural population activity under naturalistic stimuli. Activation: AFM, autoregressive flow matching, neural dynamics prediction, neural population forecasting."
---

# Autoregressive Flow Matching (AFM) for Probabilistic Prediction of Neural Dynamics

> Generative framework combining autoregressive sequence modeling with flow matching for probabilistic forecasting of neural population activity in response to naturalistic stimuli.

## Metadata
- **Source**: arXiv:2604.11178v1
- **Authors**: Camille Gontier, Youssuf Saleh, Jonathan Arreguit, Pamela Villagrán, Denis Rivière, Bertrand Thirion, Alain Destexhe
- **Published**: 2026-04-13
- **Categories**: q-bio.NC, cs.LG, stat.ML

## Core Methodology

### Problem Statement
Forecasting neural activity in response to naturalistic stimuli remains challenging due to:
- **Stochastic Nature**: Neural responses are inherently probabilistic
- **Temporal Dependencies**: Long-range temporal correlations in neural dynamics
- **High Dimensionality**: Large neural populations with complex interactions
- **Stimulus-Response Variability**: Same stimulus can evoke different responses

### Key Innovation
Autoregressive Flow Matching (AFM) combines:
1. **Flow Matching**: Continuous normalizing flows for flexible density estimation
2. **Autoregressive Modeling**: Sequential prediction with temporal dependencies
3. **Conditional Generation**: Stimulus-conditioned neural response prediction
4. **Multi-Scale Dynamics**: Capturing both fast and slow neural dynamics

### Technical Framework

#### 1. Flow Matching Fundamentals

Flow matching learns a continuous-time transformation between simple and complex distributions:

```
Given: Source distribution p₀ (e.g., Gaussian)
       Target distribution p₁ (neural population activity)

Learn: Velocity field v(x, t) such that:
       dx/dt = v(x, t)
       Flow φ_t transforms p₀ → p₁

Conditional Flow Matching objective:
L = E_{t,x₁,x₀} ||v(x_t, t) - u_t(x_t|x₁)||²

Where x_t = α_t x₁ + σ_t x₀ is the interpolation
      u_t is the conditional vector field
```

#### 2. Autoregressive Extension

For time series, predict autoregressively:

```
Given neural history: N_{<t} = {N_{t-T}, ..., N_{t-1}}
Given stimulus context: S_t

Predict: p(N_t | N_{<t}, S_t) using flow matching

Autoregressive generation:
For t = 1 to T:
    N_t ~ FlowMatch(N_{<t}, S_t)
    Append N_t to history
```

#### 3. Model Architecture

```
┌─────────────────────────────────────────────────────────┐
│        Autoregressive Flow Matching (AFM)                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Input: Neural history N_{<t}, Stimulus S_t              │
│                     ↓                                    │
│  History Encoder (Temporal Conv / LSTM / Transformer)    │
│                     ↓                                    │
│  Stimulus Encoder (Visual/audio/text → latent)           │
│                     ↓                                    │
│  Conditioning Vector c_t = [History; Stimulus]           │
│                     ↓                                    │
│  Velocity Network v(N, t, c_t)                           │
│  ├── MLP backbone                                        │
│  ├── FiLM conditioning (c_t modulates hidden layers)     │
│  └── Output: velocity field in neural activity space     │
│                     ↓                                    │
│  Flow Integration (Euler / RK4 solver)                   │
│                     ↓                                    │
│  Predicted Neural Activity N_t                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Implementation Guide

### Prerequisites
- PyTorch >= 2.0
- torchdyn (for neural ODE/flow matching)
- NumPy, SciPy
- CUDA-capable GPU

### Step-by-Step Implementation

#### 1. Flow Matching Core

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class FlowMatching(nn.Module):
    """
    Core flow matching implementation
    """
    def __init__(self, dim, hidden_dim=256, n_layers=4):
        super().__init__()
        self.dim = dim
        
        # Velocity network
        layers = []
        in_dim = dim + 1  # +1 for time
        for _ in range(n_layers):
            layers.extend([
                nn.Linear(in_dim, hidden_dim),
                nn.SiLU(),
            ])
            in_dim = hidden_dim
        layers.append(nn.Linear(hidden_dim, dim))
        
        self.velocity_net = nn.Sequential(*layers)
        
    def forward(self, x, t):
        """
        Compute velocity field
        
        Args:
            x: [batch, dim] current state
            t: [batch, 1] time (0 to 1)
        
        Returns:
            v: [batch, dim] velocity
        """
        xt = torch.cat([x, t], dim=-1)
        return self.velocity_net(xt)
    
    def sample(self, n_samples, n_steps=100):
        """
        Sample from learned distribution via ODE integration
        """
        # Start from noise
        x = torch.randn(n_samples, self.dim)
        
        # Euler integration
        dt = 1.0 / n_steps
        for i in range(n_steps):
            t = torch.ones(n_samples, 1) * i / n_steps
            v = self.forward(x, t)
            x = x + dt * v
        
        return x

class ConditionalFlowMatching(FlowMatching):
    """
    Flow matching with conditioning
    """
    def __init__(self, dim, cond_dim, hidden_dim=256, n_layers=4):
        super().__init__(dim, hidden_dim, n_layers)
        
        # FiLM conditioning
        self.cond_proj = nn.Sequential(
            nn.Linear(cond_dim, hidden_dim * 2 * n_layers),  # Scale and shift per layer
            nn.SiLU()
        )
        
    def forward(self, x, t, cond):
        """
        Args:
            x: [batch, dim] current state
            t: [batch, 1] time
            cond: [batch, cond_dim] conditioning
        
        Returns:
            v: [batch, dim] velocity
        """
        # Get FiLM params
        film_params = self.cond_proj(cond)
        # (Apply FiLM in velocity network - see implementation below)
        
        xt = torch.cat([x, t], dim=-1)
        return self.velocity_net_with_film(xt, film_params)
```

#### 2. Autoregressive Neural Dynamics Model

```python
class AutoregressiveFlowMatching(nn.Module):
    """
    AFM for neural dynamics prediction
    """
    def __init__(self, n_neurons, stimulus_dim, history_len=10, 
                 hidden_dim=256, flow_steps=50):
        super().__init__()
        
        self.n_neurons = n_neurons
        self.history_len = history_len
        self.flow_steps = flow_steps
        
        # History encoder (temporal CNN)
        self.history_encoder = nn.Sequential(
            nn.Conv1d(n_neurons, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1)
        )
        
        # Stimulus encoder
        self.stimulus_encoder = nn.Sequential(
            nn.Linear(stimulus_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )
        
        # Flow matching network
        cond_dim = 256 + 128  # History + Stimulus
        self.flow = ConditionalFlowMatching(
            dim=n_neurons,
            cond_dim=cond_dim,
            hidden_dim=hidden_dim
        )
        
    def encode_history(self, history):
        """
        Encode neural history
        
        Args:
            history: [batch, history_len, n_neurons]
        Returns:
            h: [batch, 256] history embedding
        """
        # Transpose for conv: [batch, n_neurons, history_len]
        h = history.transpose(1, 2)
        h = self.history_encoder(h)  # [batch, 256, 1]
        return h.squeeze(-1)
    
    def forward(self, history, stimulus, target=None, train=True):
        """
        Forward pass
        
        Args:
            history: [batch, history_len, n_neurons]
            stimulus: [batch, stimulus_dim]
            target: [batch, n_neurons] (for training)
        
        Returns:
            loss or prediction
        """
        batch_size = history.shape[0]
        
        # Encode history and stimulus
        h_hist = self.encode_history(history)
        h_stim = self.stimulus_encoder(stimulus)
        
        # Combine conditioning
        cond = torch.cat([h_hist, h_stim], dim=-1)
        
        if train and target is not None:
            # Training: flow matching loss
            loss = self.flow_matching_loss(target, cond)
            return loss
        else:
            # Inference: sample next neural state
            pred = self.sample_next(cond)
            return pred
    
    def flow_matching_loss(self, target, cond):
        """
        Compute conditional flow matching loss
        """
        batch_size = target.shape[0]
        
        # Sample time
        t = torch.rand(batch_size, 1, device=target.device)
        
        # Sample noise
        x0 = torch.randn_like(target)
        
        # Linear interpolation (can use other schedulers)
        alpha_t = 1 - t
        sigma_t = t
        xt = alpha_t * target + sigma_t * x0
        
        # Target velocity (for optimal transport)
        ut = target - x0  # Simple conditional vector field
        
        # Predict velocity
        vt = self.flow(xt, t, cond)
        
        # MSE loss
        loss = F.mse_loss(vt, ut)
        
        return loss
    
    def sample_next(self, cond, n_samples=1):
        """
        Sample next neural state via ODE integration
        """
        # Start from noise
        x = torch.randn(n_samples, self.n_neurons, device=cond.device)
        
        # Euler integration
        dt = 1.0 / self.flow_steps
        for i in range(self.flow_steps):
            t = torch.ones(n_samples, 1, device=cond.device) * i / self.flow_steps
            v = self.flow(x, t, cond)
            x = x + dt * v
        
        return x
    
    @torch.no_grad()
    def generate_trajectory(self, history, stimulus_sequence):
        """
        Generate full neural trajectory autoregressively
        
        Args:
            history: [1, history_len, n_neurons] initial history
            stimulus_sequence: [seq_len, stimulus_dim]
        
        Returns:
            trajectory: [seq_len, n_neurons]
        """
        trajectory = []
        current_history = history.clone()
        
        for stim in stimulus_sequence:
            stim_batch = stim.unsqueeze(0)
            
            # Predict next step
            next_neural = self.forward(current_history, stim_batch, train=False)
            trajectory.append(next_neural.squeeze(0))
            
            # Update history (slide window)
            current_history = torch.cat([
                current_history[:, 1:, :],
                next_neural.unsqueeze(1)
            ], dim=1)
        
        return torch.stack(trajectory, dim=0)
```

#### 3. Multi-Scale Dynamics

```python
class MultiScaleAFM(nn.Module):
    """
    AFM with multi-scale temporal dynamics
    """
    def __init__(self, n_neurons, stimulus_dim, scales=[1, 5, 20]):
        super().__init__()
        
        self.scales = scales
        self.scale_models = nn.ModuleList([
            AutoregressiveFlowMatching(n_neurons, stimulus_dim, history_len=s)
            for s in scales
        ])
        
        # Fusion network
        self.fusion = nn.Sequential(
            nn.Linear(n_neurons * len(scales), 256),
            nn.ReLU(),
            nn.Linear(256, n_neurons)
        )
        
    def forward(self, history, stimulus):
        """
        Multi-scale prediction
        """
        predictions = []
        
        for scale, model in zip(self.scales, self.scale_models):
            # Downsample or use appropriate window
            if scale > 1:
                hist_scaled = history[:, ::scale, :]
            else:
                hist_scaled = history
            
            pred = model(hist_scaled, stimulus, train=False)
            predictions.append(pred)
        
        # Fuse predictions
        combined = torch.cat(predictions, dim=-1)
        output = self.fusion(combined)
        
        return output
```

#### 4. Training Pipeline

```python
class AFMTrainer:
    """
    Training pipeline for AFM
    """
    def __init__(self, model, lr=1e-3, device='cuda'):
        self.model = model.to(device)
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        self.device = device
        
    def train_epoch(self, dataloader):
        """
        Train for one epoch
        
        Args:
            dataloader: Yields (history, stimulus, target) tuples
        """
        self.model.train()
        total_loss = 0
        
        for history, stimulus, target in dataloader:
            history = history.to(self.device)
            stimulus = stimulus.to(self.device)
            target = target.to(self.device)
            
            # Forward
            loss = self.model(history, stimulus, target, train=True)
            
            # Backward
            self.optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def evaluate(self, dataloader):
        """Evaluate model"""
        self.model.eval()
        
        metrics = {'mse': 0, 'correlation': 0}
        
        with torch.no_grad():
            for history, stimulus, target in dataloader:
                history = history.to(self.device)
                stimulus = stimulus.to(self.device)
                target = target.to(self.device)
                
                # Generate predictions
                pred = self.model(history, stimulus, train=False)
                
                # MSE
                metrics['mse'] += F.mse_loss(pred, target).item()
                
                # Correlation
                corr = torch.corrcoef(
                    torch.stack([pred.flatten(), target.flatten()])
                )[0, 1]
                metrics['correlation'] += corr.item()
        
        for k in metrics:
            metrics[k] /= len(dataloader)
        
        return metrics
```

## Applications

1. **Neural Prosthetics**: Predict intended movements from neural activity
2. **Brain-Computer Interfaces**: Real-time neural decoding
3. **Closed-Loop Neuroscience**: Stimulus design based on predicted responses
4. **Neural Data Imputation**: Fill missing neural recordings
5. **Computational Psychiatry**: Predict abnormal neural dynamics

## Key Features

- **Probabilistic**: Captures uncertainty in neural responses
- **Autoregressive**: Models temporal dependencies
- **Stimulus-Conditioned**: Naturalistic stimulus response prediction
- **Flexible**: Can handle varying neural population sizes
- **Scalable**: Efficient sampling via ODE solvers

## Pitfalls

1. **Training Stability**: Flow matching can be unstable with poor initialization
2. **Computational Cost**: ODE integration is slower than direct prediction
3. **Autoregressive Error Accumulation**: Errors compound over long trajectories
4. **Distribution Shift**: Performance degrades for out-of-distribution stimuli
5. **Hyperparameter Sensitivity**: Sensitive to flow schedule and architecture

## Related Skills
- neural-dynamics-decision-making
- neural-population-decoding
- neural-population-dynamics
- autoregressive-flow-matching-neural-dynamics

## References
```
Gontier, C., et al. (2026). Probabilistic Prediction of Neural Dynamics via 
Autoregressive Flow Matching. 
arXiv preprint arXiv:2604.11178v1.
```
