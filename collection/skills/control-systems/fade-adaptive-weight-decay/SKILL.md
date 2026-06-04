---
name: fade-adaptive-weight-decay
description: "FADE: Forgetting through Adaptive Decay for continual learning. Adapts per-parameter weight decay rates online via meta-gradient descent. Balances acquiring new knowledge with retaining old. Activation: FADE, adaptive weight decay, continual learning forgetting, meta-gradient weight decay, controlled forgetting, Ramesh Schmidhuber."
---

# FADE: Forgetting through Adaptive Weight Decay

> Continual learning method that adapts per-parameter weight decay rates online via approximate meta-gradient descent, enabling controlled forgetting of obsolete knowledge while retaining stable representations.

## Metadata
- **Source**: arXiv:2604.27063
- **Authors**: Aditya A. Ramesh, Alex Lewandowski, Jürgen Schmidhuber
- **Published**: 2026-04-29
- **Categories**: cs.LG, cs.NE

## Core Methodology

### Key Innovation
Weight decay is reframed as a **mechanism for controlled forgetting** in continual learning. Instead of using a fixed scalar weight decay that uniformly discards information across all parameters, FADE adapts **per-parameter decay rates** online via approximate meta-gradient descent.

### Problem Statement
Continual learning agents with finite capacity must balance:
- **Acquiring new knowledge** (learning from current data)
- **Retaining old knowledge** (remembering past tasks)
- **Controlled forgetting** (discarding knowledge that is no longer needed)

Fixed weight decay fails because:
- It drives forgetting uniformly over time
- It applies uniformly across all parameters
- Some parameters encode stable knowledge (should decay slowly)
- Others track rapidly changing targets (should decay quickly)

### Technical Framework: FADE Algorithm

1. **Per-parameter decay rates**: Each weight θ_i has its own decay rate λ_i
2. **Online adaptation**: Decay rates are updated via approximate meta-gradient descent
3. **Meta-gradient derivation**: 
   - Outer objective: minimize prediction error
   - Inner update: standard gradient step + per-parameter weight decay
   - Meta-gradient: ∂Loss/∂λ_i computed through the dependency chain
4. **Application to final layer**: FADE is derived for online linear setting and applied to the final layer of neural networks

### Algorithm Structure
```
For each time step t:
    1. Forward pass: ŷ = f(x; θ)
    2. Compute loss: L = loss(ŷ, y)
    3. Update weights: θ ← θ - η·∇L - λ ⊙ θ  (per-parameter decay)
    4. Compute meta-gradient: ∂L/∂λ
    5. Update decay rates: λ ← λ - α·∂L/∂λ
```

### Key Properties
- **Automatic discovery**: FADE discovers distinct decay rates for different parameters
- **Complements step-size adaptation**: Works alongside learning rate methods
- **Consistent improvement**: Outperforms fixed weight decay on online tracking and streaming classification

## Implementation Guide

### Prerequisites
- PyTorch or similar framework with gradient computation
- Online/streaming learning setup

### Step-by-Step Implementation

1. **Initialize per-parameter decay rates** (e.g., λ_i = λ₀ for all i)
2. **During training loop**:
   - Standard forward pass and loss computation
   - Apply per-parameter weight decay: `θ.grad += λ * θ`
   - Compute meta-gradient for λ via implicit differentiation or unrolled optimization
   - Update λ with its own learning rate
3. **Monitor decay rate distribution** to verify diverse rates emerge

### Code Example
```python
import torch

class FADEOptimizer:
    """FADE: Forgetting through Adaptive Decay optimizer."""
    
    def __init__(self, params, lr=0.01, initial_decay=0.001, meta_lr=0.001):
        self.params = list(params)
        self.lr = lr
        self.meta_lr = meta_lr
        # Per-parameter decay rates
        self.decay_rates = torch.full(
            (len(self.params),), initial_decay, requires_grad=True
        )
        self.meta_optimizer = torch.optim.Adam([self.decay_rates], lr=meta_lr)
    
    def step(self, loss_fn, x, y):
        # Forward pass
        pred = self.params[-1](x)  # Assuming final layer
        loss = loss_fn(pred, y)
        
        # Standard gradient step with per-parameter decay
        loss.backward()
        for i, param in enumerate(self.params):
            param.grad += self.decay_rates[i] * param.data
        
        # Meta-gradient update for decay rates
        # (Simplified: approximate via loss sensitivity)
        self.meta_optimizer.zero_grad()
        # Compute meta-gradient (details in paper)
        meta_grad = self._compute_meta_gradient(loss)
        self.decay_rates.grad = meta_grad
        self.meta_optimizer.step()
        
        return loss
    
    def _compute_meta_gradient(self, loss):
        """Approximate meta-gradient for decay rates."""
        # Implementation follows paper derivation
        pass
```

## Applications
- **Online/streaming learning**: Classification with non-stationary data distributions
- **Online tracking**: Predicting time-varying targets
- **Continual learning**: Multi-task learning without catastrophic forgetting
- **Neural network compression**: Automatic identification of redundant parameters
- **Transfer learning**: Balancing old and new task knowledge

## Pitfalls
- **Computational overhead**: Meta-gradient computation adds cost; use approximations
- **Hyperparameter tuning**: Meta learning rate (α) needs careful selection
- **Final layer focus**: Current derivation is for linear/last-layer; extension to deep networks requires additional analysis
- **Not a silver bullet**: Complements but doesn't replace other continual learning methods (replay, regularization, architecture-based)

## Related Skills
- continual-learning-spiking-transformer
- cortex-continual-learning-ftn
- dimensionality-modularity-continual-learning
- gradient-free-continual-learning-snn
- selective-forgetting-agent-memory-biological
- mistake-gated-continual-learning
- neuromorphic-continual-nuclear-ics
