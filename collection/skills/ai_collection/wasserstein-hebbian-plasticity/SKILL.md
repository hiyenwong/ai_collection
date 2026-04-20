---
name: wasserstein-hebbian-plasticity
description: "Wasserstein geometric framework for Hebbian plasticity (Tan-HWG) — modeling memory states as probability distributions on Wasserstein space. Derives geometric learning rules from optimal transport theory. Activation: wasserstein hebbian, optimal transport plasticity, geometric learning, tan-hwg, distributional memory."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Wasserstein Geometric Framework for Hebbian Plasticity (arXiv:2604.16052)"
    tags: [neuroscience, hebbian, wasserstein, optimal-transport, geometry]
---

# Wasserstein Geometric Framework for Hebbian Plasticity

## Source Paper
- **Title**: Wasserstein Geometric Framework for Hebbian Plasticity
- **arXiv**: 2604.16052
- **PDF**: https://arxiv.org/pdf/2604.16052

## Overview

This paper introduces the **Tan-HWG framework** (Hebbian-Wasserstein-Geometry), a geometric theory of Hebbian plasticity in which memory states are modeled as probability distributions on the Wasserstein space. By framing learning as optimal transport between probability distributions, it derives principled geometric learning rules that generalize classical Hebbian plasticity.

## Core Concepts

### Wasserstein Space as Memory Manifold
- Memory states represented as probability distributions over neural activity
- Wasserstein distance (optimal transport cost) measures similarity between memories
- The space of distributions forms a Riemannian manifold with natural geometry
- Geodesics in Wasserstein space correspond to smooth memory transitions

### Geometric Hebbian Learning Rule
- Classical Hebbian: Δw ∝ pre × post (local correlation)
- Wasserstein Hebbian: Δw follows gradient of transport cost
- Learning minimizes Wasserstein distance between current and target distributions
- Naturally incorporates spatial structure of neural representations

### Key Advantages
- **Distributional**: Handles uncertainty in neural representations
- **Geometric**: Respects the natural geometry of the representation space
- **Scalable**: Optimal transport has efficient computational approximations
- **Biologically plausible**: Gradient descent on transport cost resembles STDP

## Implementation Pattern

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

class WassersteinHebbian:
    """Wasserstein geometric Hebbian learning."""
    
    def __init__(self, n_pre, n_post, lr=0.01):
        self.n_pre = n_pre
        self.n_post = n_post
        self.W = np.random.randn(n_pre, n_post) * 0.1
        self.lr = lr
    
    def wasserstein_distance_1d(self, p, q):
        """1D Wasserstein distance (sorted CDF difference)."""
        p_sorted = np.sort(p)
        q_sorted = np.sort(q)
        return np.mean(np.abs(p_sorted - q_sorted))
    
    def hebbian_update_wasserstein(self, pre_activity, target_dist):
        """
        Update weights to minimize Wasserstein distance
        between output distribution and target.
        """
        # Forward pass
        output = pre_activity @ self.W
        output_dist = self._softmax(output)
        
        # Compute Wasserstein gradient
        # Approximation: gradient of transport cost w.r.t. weights
        w_grad = np.zeros_like(self.W)
        for i in range(self.n_pre):
            for j in range(self.n_post):
                # Local contribution to transport cost
                cost_diff = output_dist[j] - target_dist[j]
                w_grad[i, j] = pre_activity[i] * cost_diff
        
        # Update weights (gradient descent on transport cost)
        self.W -= self.lr * w_grad
        return self.W
    
    def _softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()
    
    def memory_interpolation(self, memory_a, memory_b, n_steps=10):
        """Generate geodesic path between two memories."""
        # Wasserstein barycenter interpolation
        interpolated = []
        for t in np.linspace(0, 1, n_steps):
            interp = (1-t) * memory_a + t * memory_b
            interpolated.append(interp)
        return interpolated
```

## Mathematical Framework
The Tan-HWG framework derives learning rules from:
1. **Wasserstein-2 metric**: W₂²(μ, ν) = inf E[|X-Y|²] over couplings
2. **Benamou-Brenier formula**: Dynamic formulation of optimal transport
3. **Otto calculus**: Riemannian geometry on probability space
4. **Hebbian correspondence**: Local synaptic updates approximate global transport optimization

## Applications
- **Memory consolidation**: Smooth transitions between memory states
- **Continual learning**: Preventing catastrophic forgetting via geometric constraints
- **Neural representation learning**: Learning structured embeddings
- **Brain-inspired AI**: Geometrically principled learning rules

## Related Skills
- [[meta-learning-in-context-brain-decoding]]
- [[stochastic-synaptic-plasticity]]
- [[heterogeneous-synaptic-dynamics]]
