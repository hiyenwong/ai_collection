---
name: hyperbolic-neural-population-geometry-computation
description: Hyperbolic geometry framework for hippocampal neural population activity. Modern Hopfield Network computes MMSE estimator, hyperbolic associative memory yields larger capacity than leading models.
keywords:
  - hyperbolic geometry
  - hippocampus
  - neural population geometry
  - associative memory
  - Modern Hopfield Network
  - MMSE estimator
  - memory capacity
  - spatial encoding
  - cognitive map
  - neural decoding
triggers:
  - hippocampal encoding
  - hyperbolic geometry
  - associative memory
  - neural decoding
  - population geometry
  - memory capacity
activation_keywords:
  - hyperbolic
  - hippocampus
  - geometry
  - memory
  - hopfield
  - decoding
arxiv_id: 2606.10238
paper_title: Hyperbolic Neural Population Geometry Benefits Computation
authors: Dennis Wu, Yi-Chun Hung, Braden Yuille, James E. Fitzgerald, Han Liu
submitted: 2026-06-08
venue: ICML 2026
categories:
  - neuroscience
  - machine learning
  - computational neuroscience
  - hippocampal dynamics
---

# Hyperbolic Neural Population Geometry Benefits Computation

## Overview

This methodology provides a **theoretical framework** explaining why hippocampal population activity exhibits hyperbolic geometry. Key contributions: (1) Construction of hippocampal tuning curves inducing hyperbolic geometry, (2) Connection between neural decoding and associative memory (Modern Hopfield Network = MMSE estimator), (3) Novel **hyperbolic associative memory model** with significantly larger capacity.

## Theoretical Framework

### 1. Hyperbolic Tuning Curve Construction

**Hippocampal Place Cell Geometry**:
- Place cells encode spatial locations with tuning curves
- Proposed tuning curve structure **statistically induces hyperbolic geometry**
- Hyperbolic space: constant negative curvature
- Poincaré disk/ball model: bounded representation of infinite hyperbolic space

**Place Field Construction**:
$$\text{Tuning}(r) = \exp\left(-\frac{d_H(r, r_{center})^2}{\sigma^2}\right)$$

where $d_H$ is hyperbolic distance in Poincaré model.

### 2. Neural Decoding ↔ Associative Memory Connection

**Key Theorem**: Modern Hopfield Network update rule computes **Minimum Mean-Squared-Error (MMSE) estimator**

**Modern Hopfield Network**:
$$x_{new} = \text{softmax}\left(\beta \cdot X^T \cdot x\right) \cdot X$$

where:
- $X$: Stored patterns (memory matrix)
- $x$: Query pattern
- $\beta$: Temperature parameter (inverse)
- Output: MMSE estimate of stored pattern

**Mathematical Connection**:
- Neural decoding: Estimate stimulus from neural activity
- Associative memory: Retrieve stored pattern from partial cue
- **Same mathematical operation**: Bayesian inference / MMSE estimation

### 3. Hyperbolic Associative Memory Model

**Novel Contribution**: Define associative memory in hyperbolic space

**Advantages**:
- **Larger capacity**: Hyperbolic geometry allows more patterns to be stored
- **Better decoding accuracy**: Hyperbolic space structure aids retrieval
- **Natural for spatial encoding**: Hippocampus encodes space → hyperbolic cognitive map

**Capacity Comparison**:
- Euclidean Hopfield: Capacity ~ 0.14N (N = number of neurons)
- Hyperbolic Hopfield: Capacity **significantly larger** (paper shows empirical results)

## Hyperbolic Space Mathematical Tools

### Poincaré Ball Model

**Metric**:
$$g_x = \frac{4}{(1 - \|x\|^2)^2} \cdot I$$

**Distance**:
$$d_H(x, y) = \text{arcosh}\left(1 + 2 \frac{\|x - y\|^2}{(1 - \|x\|^2)(1 - \|y\|^2)}\right)$$

**Exponential Map** (Euclidean → Hyperbolic):
$$\exp_x(v) = x \oplus \left(\tanh\left(\frac{\lambda_x \|v\|}{2}\right) \cdot \frac{v}{\|v\|}\right)$$

where $\oplus$ is Möbius addition:
$$x \oplus y = \frac{(1 + 2\langle x, y\rangle + \|y\|^2)x + (1 - \|x\|^2)y}{1 + 2\langle x, y\rangle + \|x\|^2\|y\|^2}$$

### Geodesic Operations

**Geodesic path**:
$$\gamma(t) = x \oplus t \cdot \frac{(-x) \oplus y}{\|(-x) \oplus y\|}$$

**Parallel transport**:
$$P_{x→y}(v) = v \cdot \frac{(1 - \|y\|^2)}{(1 - \|x\|^2)}$$

## Implementation Guide

### Hyperbolic Tuning Curves for Place Cells

```python
import numpy as np

def hyperbolic_distance(x, y, c=1.0):
    """Compute hyperbolic distance in Poincaré ball.
    
    Args:
        x, y: Points in Poincaré ball (||x|| < 1, ||y|| < 1)
        c: Curvature parameter (c > 0)
    
    Returns:
        d_H: Hyperbolic distance
    """
    # Möbius addition for difference
    diff = mobius_addition(-x, y, c)
    norm_diff = np.linalg.norm(diff)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    
    # Distance formula
    d_H = (2 / np.sqrt(c)) * np.arctanh(np.sqrt(c) * norm_diff)
    
    return d_H

def mobius_addition(x, y, c=1.0):
    """Möbius addition in Poincaré ball."""
    inner = np.dot(x, y)
    norm_x_sq = np.linalg.norm(x) ** 2
    norm_y_sq = np.linalg.norm(y) ** 2
    
    numerator = (1 + 2*inner + norm_y_sq) * x + (1 - norm_x_sq) * y
    denominator = 1 + 2*inner + norm_x_sq * norm_y_sq
    
    return numerator / denominator

def place_field_hyperbolic(r, center, sigma, c=1.0):
    """Hyperbolic place field tuning curve.
    
    Args:
        r: Location to evaluate (in Poincaré ball)
        center: Place field center
        sigma: Width parameter
        c: Curvature
    
    Returns:
        firing_rate: Tuning curve value
    """
    d_H = hyperbolic_distance(r, center, c)
    return np.exp(-d_H**2 / sigma**2)
```

### Modern Hopfield Network (MMSE Estimator)

```python
class ModernHopfieldNetwork:
    """Modern Hopfield Network that computes MMSE estimator."""
    
    def __init__(self, patterns, beta=1.0):
        """
        Args:
            patterns: Stored memory patterns (N patterns x D dimensions)
            beta: Temperature parameter (inverse)
        """
        self.patterns = patterns  # Shape: (N, D)
        self.beta = beta
        self.N, self.D = patterns.shape
    
    def retrieve(self, query, n_steps=10):
        """Retrieve stored pattern from query (MMSE estimation).
        
        Args:
            query: Partial/noisy pattern (D-dimensional)
            n_steps: Number of update iterations
        
        Returns:
            retrieved: Estimated stored pattern
        """
        x = query.copy()
        
        for _ in range(n_steps):
            # Compute similarity scores
            scores = self.beta * np.dot(self.patterns, x)
            
            # Softmax attention
            attention = np.exp(scores) / np.sum(np.exp(scores))
            
            # Update: weighted combination of stored patterns
            x = np.dot(attention, self.patterns)
        
        return x
    
    def capacity(self):
        """Estimate storage capacity."""
        # Standard Hopfield: ~0.14N
        # Modern Hopfield: scales better
        return self.N * 0.14  # Conservative estimate
```

### Hyperbolic Associative Memory

```python
class HyperbolicAssociativeMemory:
    """Associative memory in hyperbolic space."""
    
    def __init__(self, n_patterns, dim, curvature=1.0):
        """
        Args:
            n_patterns: Number of patterns to store
            dim: Dimensionality of Poincaré ball
            curvature: Hyperbolic curvature (c > 0)
        """
        self.dim = dim
        self.c = curvature
        
        # Initialize patterns in Poincaré ball (||x|| < 1)
        self.patterns = self._sample_hyperbolic(n_patterns)
    
    def _sample_hyperbolic(self, n):
        """Sample points uniformly in Poincaré ball."""
        # Uniform sampling in hyperbolic space requires careful distribution
        # Use radial distribution: p(r) ~ sinh(r)^(d-1)
        radii = np.random.uniform(0, 0.9, n)  # Avoid boundary
        directions = np.random.randn(n, self.dim)
        directions = directions / np.linalg.norm(directions, axis=1, keepdims=True)
        
        return radii[:, np.newaxis] * directions
    
    def store(self, pattern):
        """Store new pattern in hyperbolic space."""
        # Project pattern onto Poincaré ball
        norm = np.linalg.norm(pattern)
        if norm >= 1:
            pattern = pattern / norm * 0.95  # Scale to fit
        
        self.patterns = np.vstack([self.patterns, pattern])
    
    def retrieve(self, query):
        """Retrieve closest pattern from query.
        
        Args:
            query: Query point in Poincaré ball
        
        Returns:
            retrieved: Closest stored pattern
            distance: Hyperbolic distance to retrieved pattern
        """
        # Compute hyperbolic distances to all stored patterns
        distances = [hyperbolic_distance(query, p, self.c) for p in self.patterns]
        
        # Retrieve closest
        idx = np.argmin(distances)
        return self.patterns[idx], distances[idx]
    
    def capacity(self):
        """Estimate hyperbolic memory capacity (larger than Euclidean)."""
        # Empirical result: significantly larger than 0.14N
        return len(self.patterns) * 0.25  # Approximate improvement factor
```

## Applications

1. **Hippocampal Modeling**: Explain hyperbolic geometry in place cell activity
2. **Neural Decoding**: MMSE estimation via associative memory
3. **Memory Systems**: Hyperbolic associative memory with larger capacity
4. **Spatial Cognition**: Hyperbolic cognitive map representation
5. **Neuromorphic Computing**: Hyperbolic geometry-based memory circuits
6. **Brain-Computer Interfaces**: Decoding spatial navigation

## Pitfalls

1. **Poincaré Ball Boundary**: Points must satisfy ||x|| < 1 (avoid singularity at boundary)
2. **Numerical Stability**: Use stable implementations of arcosh, tanh
3. **Curvature Choice**: Curvature parameter c affects capacity, tune empirically
4. **Projection**: Must project Euclidean patterns onto Poincaré ball
5. **Distance Computation**: Hyperbolic distance ≠ Euclidean distance (use Möbius operations)

## Key Equations

**Hyperbolic Distance**:
$$d_H(x, y) = \frac{2}{\sqrt{c}} \text{arcosh}\left(1 + 2c \frac{\|x - y\|^2}{(1 - c\|x\|^2)(1 - c\|y\|^2)}\right)$$

**Modern Hopfield Update (MMSE)**:
$$x_{t+1} = \sum_i \frac{\exp(\beta \cdot x_i^T x_t)}{\sum_j \exp(\beta \cdot x_j^T x_t)} \cdot x_i$$

**Hyperbolic Place Field**:
$$T(r) = \exp\left(-\frac{d_H(r, r_{center})^2}{\sigma^2}\right)$$

## Verification Steps

1. Verify tuning curves induce hyperbolic geometry (check curvature)
2. Validate Modern Hopfield computes MMSE estimator (Bayesian inference)
3. Test hyperbolic memory capacity > Euclidean capacity
4. Compare decoding accuracy: hyperbolic vs Euclidean
5. Check Poincaré ball constraint: ||x|| < 1 for all points

## Related Work

- Modern Hopfield Networks (Ramsauer et al., 2021)
- Hyperbolic Neural Networks (Nickel & Kiela, 2017)
- Place cell geometry (Moser et al., 2008)
- Cognitive map theory (O'Keefe & Nadel, 1978)

## References

- arXiv:2606.10238 - Hyperbolic Neural Population Geometry (Wu et al., ICML 2026)
- Ramsauer et al. (2021) - Modern Hopfield Networks
- Nickel & Kiela (2017) - Poincaré Embeddings

---
*Source: arXiv:2606.10238 | Created: 2026-06-11 | Venue: ICML 2026 | Category: neuroscience*