---
name: polystep-gradient-free-training
description: "Gradient-free neural network training via Optimal Transport geometry (PolyStep optimizer). Based on arXiv:2605.01928 (Le, 2026). Use when training non-differentiable models including hard-LIF spiking neurons, quantized networks, discrete routing, or blackbox simulators. Replaces backpropagation and surrogate gradients with forward-pass-only optimization. Activation: polystep optimizer, gradient-free training, non-differentiable network, hard-LIF training, optimal transport optimizer, surrogate gradient alternative, forward-only training, spiking network training without backprop."
---

# PolyStep: Gradient-Free Training via Optimal Transport

Gradient-free optimizer that trains non-differentiable neural networks using only forward passes, based on optimal transport geometry. Achieves 93.4% on hard-LIF SNNs, closing within 4.4pp of surrogate-gradient Adam.

## Core Algorithm

PolyStep evaluates loss at structured polytope vertices in a compressed subspace, computes softmax-weighted assignments, and displaces particles toward low-cost vertices via barycentric projection.

### Mathematical Formulation

For parameters θ ∈ ℝᵈ, at step t:

1. **Sample polytope vertices**: V = {θ + σ·uᵢ} where uᵢ are structured directions in compressed subspace
2. **Evaluate losses**: Lᵢ = Loss(Vᵢ) for each vertex
3. **Softmax weighting**: wᵢ = exp(-Lᵢ/τ) / Σⱼ exp(-Lⱼ/τ)
4. **Barycentric update**: θ ← Σᵢ wᵢ·Vᵢ

This corresponds to the one-sided limit of a regularized optimal transport problem, inheriting geometric structure without Sinkhorn iterations.

### Convergence Guarantees

- O(log T / √T) convergence to conservative-stationary points on piecewise-smooth losses
- Clarke-stationary convergence on hard-LIF, quantized, and discrete architectures
- Extended to piecewise-constant regime via hitting-time bound
- Rates match zeroth-order query-complexity lower bounds

## Implementation

### Core PolyStep Optimizer

```python
import numpy as np
from typing import Callable, Tuple

class PolyStep:
    """Gradient-free optimizer using optimal transport geometry."""
    
    def __init__(self, dim: int, n_vertices: int = None, 
                 sigma: float = 0.1, tau: float = 1.0,
                 compress_ratio: float = 0.5, lr: float = 0.01):
        self.dim = dim
        self.n_vertices = n_vertices or min(2 * dim, 128)
        self.sigma = sigma  # perturbation scale
        self.tau = tau      # temperature for softmax
        self.compress_ratio = compress_ratio
        self.lr = lr
        self._compressed_dim = max(1, int(dim * compress_ratio))
    
    def _sample_directions(self, rng: np.random.RandomState) -> np.ndarray:
        """Sample structured directions in compressed subspace."""
        # Random projection to compressed subspace
        P = rng.randn(self.dim, self._compressed_dim) / np.sqrt(self._compressed_dim)
        # Sample vertices on unit sphere in compressed space
        Z = rng.randn(self.n_vertices, self._compressed_dim)
        Z /= np.linalg.norm(Z, axis=1, keepdims=True)
        # Project back to full space
        directions = Z @ P.T
        directions /= np.linalg.norm(directions, axis=1, keepdims=True)
        return directions
    
    def step(self, theta: np.ndarray, loss_fn: Callable[[np.ndarray], float],
             rng: np.random.RandomState) -> Tuple[np.ndarray, float]:
        """Single optimization step. Forward-pass only."""
        directions = self._sample_directions(rng)
        vertices = theta + self.sigma * directions
        
        # Evaluate all vertices (forward passes only)
        losses = np.array([loss_fn(v) for v in vertices])
        
        # Softmax weighting
        weights = np.exp(-losses / self.tau)
        weights /= weights.sum()
        
        # Barycentric update
        displacement = weights @ (vertices - theta)
        theta_new = theta + self.lr * displacement
        
        return theta_new, losses.min()
```

### Training Hard-LIF Spiking Networks

```python
def train_hard_lif_snn(model, train_loader, n_epochs=50, **polystep_kwargs):
    """Train a hard-LIF SNN with PolyStep (no surrogate gradients)."""
    params = model.get_parameters()  # flat array
    dim = params.size
    
    optimizer = PolyStep(dim=dim, n_vertices=64, sigma=0.05, tau=0.5, lr=0.01)
    rng = np.random.RandomState(42)
    
    for epoch in range(n_epochs):
        total_loss = 0.0
        for inputs, targets in train_loader:
            def loss_fn(p):
                model.set_parameters(p)
                outputs = model(inputs)
                return compute_loss(outputs, targets)
            
            params, loss = optimizer.step(params, loss_fn, rng)
            total_loss += loss
        
        model.set_parameters(params)
        # Evaluate...
```

## Comparison with Alternatives

| Method | Hard-LIF Acc. | Gradient Needed? | Convergence Proof |
|--------|--------------|-----------------|-------------------|
| PolyStep | 93.4% | No (forward-only) | O(log T/√T) |
| Surrogate Adam | 97.8% | Yes (approximate) | Standard |
| Evolution Strategies | ~30% | No | None |
| Random Search | ~10% | No | None |

## When to Use

- **Hard-LIF neurons**: Binary spikes with non-differentiable threshold
- **Quantized networks**: INT8/binary weights with discrete updates
- **Discrete routing**: MoE with hard expert selection (argmax)
- **Blackbox simulators**: Systems where gradients are unavailable
- **Staircase activations**: Non-smooth activation functions

## When NOT to Use

- Standard differentiable networks (use Adam/SGD)
- When surrogate gradients achieve sufficient accuracy
- Very high-dimensional models (>10M params) — vertex sampling becomes expensive
- When convergence speed is critical — PolyStep is slower than gradient methods

## Pitfalls

- Vertex count n_vertices must scale with effective dimension, not raw parameter count
- Temperature τ needs tuning: too high → random walk, too low → premature convergence
- Compression ratio trades off sample efficiency against direction diversity
- Loss evaluation count per step = n_vertices (can be parallelized)
- Not suitable for online/streaming training — requires batch loss evaluation

## References

- Le, A.T. (2026). Training Non-Differentiable Networks via Optimal Transport. arXiv:2605.01928
- Code: https://github.com/anindex/polystep
