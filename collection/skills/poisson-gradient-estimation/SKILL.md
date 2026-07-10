---
name: poisson-gradient-estimation
description: "Systematic comparison of Poisson gradient estimation methods (EAT vs GSM) for latent variable models in computational neuroscience. Activation: poisson gradient, EAT method, Gumbel-SoftMax, spike train inference."
---

# Poisson Gradient Estimation for Latent Variable Models

> First systematic comparison of Exponential Arrival Time (EAT) and Gumbel-SoftMax (GSM) methods for differentiating through Poisson-distributed latent variables in computational neuroscience.

## Metadata
- **Source**: arXiv:2602.03896
- **Authors**: Michael Ibrahim, Hanqi Zhao, Eli Sennesh, Zhi Li, Anqi Wu
- **Published**: 2026-02-03
- **Category**: stat.ML

## Core Methodology

### Problem Statement
Poisson-distributed latent variable models are widely used in computational neuroscience, but differentiating through discrete stochastic samples remains challenging. This work addresses gradient estimation for:
- Variational autoencoders with Poisson latents
- Partially observable generalized linear models (inferring latent neural connectivity from spike trains)

### Key Methods Compared

#### 1. Exponential Arrival Time (EAT) Simulation
- Simulates Poisson process via exponential inter-arrival times
- **Modified EAT contribution**: Unbiased first moment (exactly matching firing rate), reduced second-moment bias
- **Advantages**: Better distributional fidelity, higher robustness to hyperparameters

#### 2. Gumbel-SoftMax (GSM) Relaxation
- Continuous relaxation of discrete sampling
- Differentiable approximation to Poisson sampling
- **Trade-offs**: Simpler implementation but may introduce bias

## Implementation Guide

### Prerequisites
```python
import torch
import numpy as np
```

### Modified EAT Method
```python
def modified_eat_sample(rate, shape):
    """
    Modified Exponential Arrival Time sampling for Poisson variables.
    Provides unbiased first moment (exact firing rate matching).
    
    Args:
        rate: Poisson rate parameter (lambda)
        shape: Output shape
    
    Returns:
        Poisson samples with unbiased first moment
    """
    # Standard Poisson sampling with moment correction
    return torch.poisson(rate)  # Simplified - see paper for full

def compute_poisson_gradient_eat(model, data, rate_param):
    """Compute gradients using EAT method."""
    # Enable gradient computation through stochastic nodes
    # Implementation depends on specific model architecture
    pass
```

### GSM Alternative
```python
def gumbel_softmax_poisson(logits, temperature=1.0, hard=False):
    """
    Gumbel-SoftMax relaxation for Poisson-like discrete sampling.
    
    Args:
        logits: Log probabilities
        temperature: Softmax temperature (lower = more discrete)
        hard: If True, returns hard samples with soft gradients
    """
    gumbel_noise = -torch.log(-torch.log(torch.rand_like(logits) + 1e-10) + 1e-10)
    y_soft = torch.softmax((logits + gumbel_noise) / temperature, dim=-1)
    
    if hard:
        # Straight-through estimator
        index = y_soft.max(dim=-1, keepdim=True)[1]
        y_hard = torch.zeros_like(logits).scatter_(-1, index, 1.0)
        return (y_hard - y_soft).detach() + y_soft
    return y_soft
```

### Evaluation Framework
```python
def evaluate_gradient_method(model, data_loader, method='eat'):
    """
    Evaluate gradient estimation method on downstream tasks.
    
    Metrics:
    1. Distributional fidelity: KL divergence from true Poisson
    2. Gradient quality: Gradient variance, bias
    3. Task performance: ELBO, prediction accuracy
    """
    results = {
        'kl_divergence': [],
        'gradient_variance': [],
        'task_performance': []
    }
    
    for batch in data_loader:
        if method == 'eat':
            gradient = compute_poisson_gradient_eat(model, batch)
        elif method == 'gsm':
            gradient = compute_poisson_gradient_gsm(model, batch)
        
        # Evaluate metrics
        # ...
    
    return results
```

## Applications

### 1. Variational Autoencoders with Poisson Latents
```python
class PoissonVAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * 2)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, input_dim),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        params = self.encoder(x)
        rate = torch.exp(params[:, :latent_dim])
        z = modified_eat_sample(rate, rate.shape)
        x_recon = self.decoder(z)
        return x_recon, rate, z
```

### 2. Latent Neural Connectivity Inference
Infer latent connectivity from observed spike trains in partially observable GLMs.

## Recommendations for Practitioners

| Method | Best For | Avoid When |
|--------|----------|------------|
| Modified EAT | High fidelity, robust gradients | Simple/quick implementation |
| GSM | Quick prototyping, simple models | High precision required |

**Key Findings**:
1. Modified EAT exhibits better overall performance (often comparable to exact gradients)
2. Substantially higher robustness to hyperparameter choices
3. Preferred for production systems requiring stable training

## Pitfalls
- **Hyperparameter sensitivity**: GSM can be sensitive to temperature scheduling
- **Numerical stability**: EAT requires careful handling of near-zero rates
- **Computational cost**: EAT may be slower than GSM in some implementations

## Related Skills
- spiking-neural-network-analysis
- computational-neuroscience-in-llm-era
- neural-population-dynamics

## References
- arXiv:2602.03896 - A Hitchhiker's Guide to Poisson Gradient Estimation
