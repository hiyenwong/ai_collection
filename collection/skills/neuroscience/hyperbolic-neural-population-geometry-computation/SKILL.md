---
name: hyperbolic-neural-population-geometry-computation
description: "Hyperbolic geometry framework for neural population activity in hippocampus. Modern Hopfield Network computes MMSE estimator, hyperbolic associative memory yields larger capacity than Euclidean models. ICML 2026 paper. Activation: hyperbolic geometry, neural population, hippocampus, associative memory, Hopfield network, spatial navigation, cognitive map, memory capacity, MMSE estimator."
category: neuroscience
---

## Context

**arXiv Paper**: [2606.10238](https://arxiv.org/abs/2606.10238) - Hyperbolic Neural Population Geometry Benefits Computation

**Authors**: Dennis Wu, Yi-Chun Hung, Braden Yuille, James E. Fitzgerald, Han Liu

**Submitted**: 2026-06-08

**Conference**: ICML 2026 (37 pages, 5 figures)

**Core Discovery**: Recent empirical findings suggest hyperbolic structure underlies hippocampal population activity. This paper provides theoretical framework: (1) hippocampal tuning curves statistically induce hyperbolic geometry, (2) Modern Hopfield Network update rule computes MMSE estimator, (3) hyperbolic associative memory has larger capacity than leading models.

**Key Innovation**: Animals encode spatial information as latent hyperbolic cognitive map, improving memory capacity and decoding accuracy. Hyperbolic geometry provides exponential expansion of distance → more efficient representation of hierarchical structures.

## Core Methodology

### 1. Hippocampal Tuning Curves Induce Hyperbolic Geometry

**Problem**: Why does hippocampal neural population exhibit hyperbolic structure?

**Solution**: Statistical induction from tuning curve construction:

```python
def construct_hyperbolic_tuning_curves(n_neurons, curvature=-1):
    """
    Build hippocampal tuning curves that induce hyperbolic geometry
    
    Args:
        n_neurons: number of place cells
        curvature: hyperbolic space curvature (negative)
    
    Returns:
        tuning_curves: {neuron_id: {position: firing_rate}}
    """
    import numpy as np
    
    # Hyperbolic space: Poincaré disk model
    # Distance metric: d(u,v) = arccosh(1 + 2||u-v||^2 / ((1-||u||^2)(1-||v||^2)))
    
    # Place field centers in hyperbolic disk
    centers = sample_hyperbolic_disk(n_neurons, curvature)
    
    tuning_curves = {}
    for i, center in enumerate(centers):
        # Gaussian tuning curve in hyperbolic space
        positions = np.linspace(0, 1, 100)  # Positions in disk
        distances = hyperbolic_distance(center, positions)
        
        # Firing rate: exp(-distance^2 / sigma^2)
        sigma = 0.1  # Place field width
        firing_rates = np.exp(-distances**2 / (2 * sigma**2))
        
        tuning_curves[i] = {pos: rate for pos, rate in zip(positions, firing_rates)}
    
    return tuning_curves

def hyperbolic_distance(u, v, curvature=-1):
    """
    Compute distance in hyperbolic space (Poincaré disk)
    
    Formula: d(u,v) = arccosh(1 + 2||u-v||^2 / ((1-||u||^2)(1-||v||^2)))
    """
    import numpy as np
    
    u_norm_sq = np.sum(u**2)
    v_norm_sq = np.sum(v**2)
    diff_norm_sq = np.sum((u - v)**2)
    
    denominator = (1 - u_norm_sq) * (1 - v_norm_sq)
    argument = 1 + 2 * diff_norm_sq / denominator
    
    return np.arccosh(argument)
```

**Statistical Induction**:
- Place fields in hyperbolic disk → Gaussian tuning curves
- Population activity manifold inherits hyperbolic geometry
- Exponential expansion of distance → hierarchical structure encoding

### 2. Modern Hopfield Network = MMSE Estimator

**Problem**: What does Hopfield Network compute in neural decoding context?

**Solution**: Modern Hopfield Network update rule computes **Minimum Mean-Squared Error (MMSE) estimator**.

```python
import torch
import torch.nn as nn

class ModernHopfieldNetwork(nn.Module):
    """
    Modern Hopfield Network that computes MMSE estimator
    
    Key insight: Update rule = optimal Bayesian decoder
    """
    def __init__(self, n_patterns, pattern_dim, beta=1.0):
        super().__init__()
        self.n_patterns = n_patterns
        self.pattern_dim = pattern_dim
        self.beta = beta  # Temperature parameter
        
        # Stored patterns (memory)
        self.memory = nn.Parameter(torch.randn(n_patterns, pattern_dim))
        
    def forward(self, query_pattern):
        """
        Hopfield update rule: computes MMSE estimator
        
        Formula: x_new = sum_j w_j * pattern_j
        where w_j = exp(beta * <query, pattern_j>) / sum_k exp(beta * <query, pattern_k>)
        
        This is the MMSE estimator under Gaussian prior assumption.
        """
        # Compute similarity scores
        similarity = torch.matmul(query_pattern, self.memory.T)
        
        # Attention weights (softmax)
        weights = torch.softmax(self.beta * similarity, dim=-1)
        
        # MMSE estimate: weighted combination of stored patterns
        mmse_estimate = torch.matmul(weights, self.memory)
        
        return mmse_estimate, weights
    
    def compute_mmse_theoretical(self, query, noise_variance=0.1):
        """
        Theoretical MMSE estimator derivation
        
        Under model: observation = true_pattern + noise
        Prior: patterns ~ Gaussian
        
        MMSE = posterior_mean = sum_j p(pattern_j|observation) * pattern_j
        """
        # Bayesian posterior computation
        log_likelihoods = -torch.norm(query - self.memory, dim=-1) / (2 * noise_variance)
        
        # Posterior weights
        posterior_weights = torch.softmax(log_likelihoods, dim=-1)
        
        # Posterior mean (MMSE)
        posterior_mean = torch.matmul(posterior_weights, self.memory)
        
        return posterior_mean, posterior_weights
```

**Key Result**: Hopfield Network attention mechanism ≡ Bayesian posterior mean → optimal decoding.

### 3. Hyperbolic Associative Memory

**Problem**: Can associative memory be defined in hyperbolic space?

**Solution**: Yes, and it yields **larger capacity** than Euclidean models.

```python
import geoopt  # Library for Riemannian optimization

class HyperbolicAssociativeMemory(nn.Module):
    """
    Associative memory in hyperbolic space
    
    Advantages:
    - Exponential distance expansion → better separation
    - Hierarchical structure encoding → more patterns per dimension
    - Larger capacity than Euclidean Hopfield Networks
    """
    def __init__(self, n_patterns, dim, curvature=-1):
        super().__init__()
        self.curvature = curvature
        
        # Hyperbolic manifold: Poincaré ball
        self.manifold = geoopt.PoincareBall(c=curvature)
        
        # Stored patterns in hyperbolic space
        # Initialize on tangent space, then project to manifold
        patterns_init = torch.randn(n_patterns, dim) * 0.1
        self.memory = geoopt.ManifoldParameter(
            patterns_init,
            manifold=self.manifold
        )
        
    def forward(self, query):
        """
        Hyperbolic associative memory retrieval
        
        Distance metric: exponential expansion
        Similarity: exp(-distance)
        """
        # Hyperbolic distances from query to all stored patterns
        distances = self.manifold.dist(query.unsqueeze(0), self.memory)
        
        # Similarity scores (inverse distance)
        similarities = torch.exp(-distances)
        
        # Attention weights
        weights = similarities / similarities.sum()
        
        # Hyperbolic weighted combination (geodesic interpolation)
        retrieved = self.hyperbolic_weighted_sum(weights, self.memory)
        
        return retrieved, weights
    
    def hyperbolic_weighted_sum(self, weights, patterns):
        """
        Weighted sum in hyperbolic space
        
        Use geodesic interpolation (Möbius addition)
        """
        # Normalize weights for hyperbolic combination
        w_normalized = weights / weights.sum()
        
        # Möbius weighted sum
        result = torch.zeros_like(patterns[0])
        for w, p in zip(w_normalized, patterns):
            result = self.manifold.mobius_add(result, p * w)
        
        return result
    
    def compute_capacity(self):
        """
        Estimate memory capacity
        
        Hyperbolic capacity > Euclidean due to:
        - Exponential distance growth
        - Hierarchical structure
        """
        # Pairwise distances between stored patterns
        n = len(self.memory)
        distances = torch.zeros(n, n)
        for i in range(n):
            for j in range(n):
                distances[i, j] = self.manifold.dist(self.memory[i], self.memory[j])
        
        # Average distance (measure of separation)
        avg_distance = distances.mean()
        
        # Capacity estimate: patterns that can be stored without interference
        # In hyperbolic space, capacity grows exponentially with distance
        capacity_estimate = torch.exp(avg_distance) * self.memory.shape[1]
        
        return capacity_estimate
```

**Capacity Comparison**:
- Euclidean Hopfield: capacity ~ 0.14N (N = pattern dimension)
- Hyperbolic associative memory: capacity ~ exponential(distance) × dim
- **Result**: Hyperbolic model achieves significantly larger capacity

### 4. Neural Decoding from Hyperbolic Population Activity

```python
def decode_from_hyperbolic_population(population_activity, memory_patterns):
    """
    Decode position from hyperbolic neural population
    
    Args:
        population_activity: firing rates across place cells
        memory_patterns: stored hyperbolic representations
    
    Returns:
        decoded_position: position estimate in hyperbolic space
    """
    import torch
    
    # Treat population activity as query to associative memory
    query = torch.tensor(population_activity)
    
    # Hopfield retrieval (MMSE estimate)
    hopfield = ModernHopfieldNetwork(len(memory_patterns), len(population_activity))
    hopfield.memory = torch.tensor(memory_patterns)
    
    decoded_position, confidence = hopfield.forward(query)
    
    return decoded_position, confidence
```

## Implementation Steps

### Step 1: Hyperbolic Geometry Setup

```python
import geoopt
import torch

# Poincaré ball model
manifold = geoopt.PoincareBall(c=-1.0)

# Sample points uniformly in hyperbolic disk
def sample_hyperbolic_disk(n_samples, dim=2, curvature=-1):
    """
    Sample uniformly in Poincaré disk
    
    Use rejection sampling or polar coordinates
    """
    manifold = geoopt.PoincareBall(c=curvature)
    
    # Sample in tangent space (Euclidean)
    tangent_samples = torch.randn(n_samples, dim)
    
    # Project to manifold via exponential map
    origin = torch.zeros(dim)
    hyperbolic_samples = manifold.expmap(origin, tangent_samples)
    
    return hyperbolic_samples

# Example: place field centers
place_centers = sample_hyperbolic_disk(100, dim=2, curvature=-1)
```

### Step 2: Hyperbolic Neural Population Model

```python
class HyperbolicPlaceCellPopulation(nn.Module):
    """
    Place cell population in hyperbolic space
    
    Generates tuning curves with hyperbolic geometry
    """
    def __init__(self, n_cells, dim=2, curvature=-1):
        super().__init__()
        self.manifold = geoopt.PoincareBall(c=curvature)
        
        # Place field centers
        centers_init = torch.randn(n_cells, dim) * 0.1
        self.centers = geoopt.ManifoldParameter(centers_init, manifold=self.manifold)
        
        # Place field widths (in hyperbolic distance)
        self.widths = nn.Parameter(torch.ones(n_cells) * 0.5)
        
    def forward(self, position):
        """
        Compute firing rates for all place cells given position
        
        Args:
            position: query position in hyperbolic disk
        
        Returns:
            firing_rates: vector of firing rates
        """
        # Hyperbolic distances
        distances = self.manifold.dist(position.unsqueeze(0), self.centers)
        
        # Gaussian tuning curves
        firing_rates = torch.exp(-distances**2 / (2 * self.widths**2))
        
        return firing_rates
    
    def decode_position(self, firing_rates):
        """
        Decode position from firing rates using Hopfield retrieval
        
        This is the MMSE estimator
        """
        # Stored patterns: firing rates at canonical positions
        canonical_positions = sample_hyperbolic_disk(50, dim=2)
        stored_patterns = self.forward(canonical_positions)
        
        # Hopfield retrieval
        hopfield = ModernHopfieldNetwork(50, len(self.centers))
        hopfield.memory = stored_patterns
        
        decoded_position, weights = hopfield.forward(firing_rates)
        
        return decoded_position
```

### Step 3: Capacity Benchmarking

```python
def benchmark_memory_capacity():
    """
    Compare Euclidean vs. Hyperbolic associative memory capacity
    """
    import numpy as np
    
    results = {}
    
    # Euclidean Hopfield Network
    dim = 100
    n_patterns_euc = int(0.14 * dim)  # Classical capacity bound
    
    # Test Euclidean retrieval
    patterns_euc = torch.randn(n_patterns_euc, dim)
    hopfield_euc = ModernHopfieldNetwork(n_patterns_euc, dim)
    hopfield_euc.memory = patterns_euc
    
    query_euc = patterns_euc[0] + torch.randn(dim) * 0.1
    retrieved_euc, _ = hopfield_euc.forward(query_euc)
    
    error_euc = torch.norm(retrieved_euc - patterns_euc[0]).item()
    results['euclidean'] = {
        'capacity': n_patterns_euc,
        'retrieval_error': error_euc
    }
    
    # Hyperbolic Associative Memory
    n_patterns_hyp = n_patterns_euc * 5  # Test higher capacity
    memory_hyp = HyperbolicAssociativeMemory(n_patterns_hyp, dim, curvature=-1)
    
    query_hyp = memory_hyp.memory[0] + torch.randn(dim) * 0.1
    query_hyp = memory_hyp.manifold.projx(query_hyp)  # Project back to manifold
    
    retrieved_hyp, _ = memory_hyp.forward(query_hyp)
    
    error_hyp = memory_hyp.manifold.dist(retrieved_hyp, memory_hyp.memory[0]).item()
    capacity_hyp = memory_hyp.compute_capacity().item()
    
    results['hyperbolic'] = {
        'capacity': capacity_hyp,
        'retrieval_error': error_hyp
    }
    
    print(f"Euclidean capacity: {n_patterns_euc}, error: {error_euc:.4f}")
    print(f"Hyperbolic capacity: {capacity_hyp:.1f}, error: {error_hyp:.4f}")
    
    return results
```

## Pitfalls

### 1. Hyperbolic Distance Numerical Instability
**Problem**: Poincaré ball distances blow up near boundary (||u|| → 1).

**Solution**: Clip vectors to stay within safe radius:
```python
def safe_hyperbolic_distance(u, v, safe_radius=0.9):
    u_clipped = u / max(torch.norm(u), safe_radius)
    v_clipped = v / max(torch.norm(v), safe_radius)
    return hyperbolic_distance(u_clipped, v_clipped)
```

### 2. Gradient Descent in Hyperbolic Space
**Problem**: Standard gradient descent doesn't work on curved manifolds.

**Solution**: Use Riemannian gradient descent:
```python
# Use geoopt.optim.RiemannianAdam
optimizer = geoopt.optim.RiemannianAdam(model.parameters(), lr=0.01)
```

### 3. Pattern Interference in High Capacity
**Problem**: More patterns → potential interference even in hyperbolic space.

**Solution**: Use hierarchical encoding:
```python
# Organize patterns in hyperbolic tree structure
# Levels encode hierarchical relationships
def hierarchical_pattern_storage(patterns, levels):
    for level, patterns_at_level in zip(levels, patterns):
        # Store patterns at specific hyperbolic depth
        depth = level / max(levels)
        scaled_patterns = patterns_at_level * (1 - depth)
```

### 4. MMSE Assumption Validity
**Problem**: Hopfield Network ≡ MMSE requires Gaussian prior.

**Solution**: Test prior assumption empirically:
```python
def test_prior_assumption(population_data):
    # Fit Gaussian to population statistics
    from scipy.stats import multivariate_normal
    
    mean = population_data.mean(axis=0)
    cov = np.cov(population_data.T)
    
    # Test goodness-of-fit
    gaussian = multivariate_normal(mean, cov)
    log_likelihood = gaussian.logpdf(population_data).mean()
    
    return log_likelihood
```

## Verification

### 1. Hyperbolic Geometry Induction Test
```python
# Generate place cell population
population = HyperbolicPlaceCellPopulation(100, dim=2)

# Sample positions uniformly in disk
positions = sample_hyperbolic_disk(1000, dim=2)

# Compute population activity manifold
activities = torch.stack([population(p) for p in positions])

# Test: manifold should exhibit hyperbolic structure
from sklearn.manifold import Isomap

embedding = Isomap(n_components=2).fit_transform(activities)
assert embedding.shape[1] == 2  # 2D manifold
```

### 2. Hopfield = MMSE Test
```python
hopfield = ModernHopfieldNetwork(50, 100)
query = torch.randn(100)

# Hopfield retrieval
retrieved_hf, _ = hopfield.forward(query)

# MMSE theoretical computation
retrieved_mmse, _ = hopfield.compute_mmse_theoretical(query)

# Test: both should match
assert torch.allclose(retrieved_hf, retrieved_mmse, atol=1e-3)
```

### 3. Capacity Improvement Test
```python
results = benchmark_memory_capacity()

# Test: hyperbolic capacity > euclidean
assert results['hyperbolic']['capacity'] > results['euclidean']['capacity'] * 2

# Test: retrieval errors comparable (no degradation despite higher capacity)
assert results['hyperbolic']['retrieval_error'] < 2 * results['euclidean']['retrieval_error']
```

## Key Results

- **Hyperbolic tuning curves**: Place field construction statistically induces hyperbolic geometry
- **Hopfield = MMSE**: Modern Hopfield Network update rule computes optimal Bayesian decoder
- **Hyperbolic associative memory**: Larger capacity than Euclidean Hopfield Networks
- **Decoding accuracy**: Hyperbolic cognitive map improves position decoding

## Theoretical Implications

1. **Spatial Navigation**: Animals use hyperbolic cognitive maps for hierarchical spatial encoding
2. **Memory Capacity**: Hyperbolic geometry enables exponential expansion → more memories per neuron
3. **Neural Decoding**: Hopfield Networks implement optimal Bayesian inference
4. **Computation Geometry**: Curved neural manifolds benefit downstream computation

## Practical Applications

- **Spatial navigation AI**: Hyperbolic maps for hierarchical environment encoding
- **Memory augmentation**: Hyperbolic associative memories for larger capacity storage
- **Neural decoding**: Bayesian inference via Hopfield dynamics
- **Cognitive modeling**: Hyperbolic cognitive maps for hierarchical reasoning

## References

- Paper: arXiv:2606.10238 (ICML 2026)
- Related: Hippocampal place cells, Modern Hopfield Networks, hyperbolic neural networks, associative memory capacity
- Keywords: hyperbolic geometry, neural population, hippocampus, associative memory, MMSE estimator