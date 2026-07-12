---
name: quantum-inspired-optimization
description: "Quantum-Inspired Evolutionary Optimization (QIEO) for non-convex ML optimization. Uses quantum superposition-inspired probability amplitudes, quantum rotation gates for distribution updates, and quantum interference for exploration/exploitation balance. Use when: quantum-inspired optimization, QIEO, non-convex optimization, global search evolutionary, escaping local minima, 量子启发优化, 量子进化优化."
category: optimization
---

# Quantum-Inspired Evolutionary Optimization (QIEO)

> A unified framework that treats non-convex optimization as a global search problem using quantum-inspired probability amplitudes to maintain a global view of the search space and escape local minima more effectively than traditional evolutionary algorithms.

**Source**: arXiv:2605.07947

## Core Problem

Non-convex optimization in ML (neural network training, hyperparameter search, combinatorial problems) is plagued by **local minima**. Traditional evolutionary algorithms (GA, PSO) maintain a limited view of the search space and can prematurely converge.

## QIEO Solution

### Key Innovation

QIEO leverages **three quantum-inspired mechanisms**:

1. **Quantum superposition-inspired probability amplitudes**: Each candidate solution is represented as a probability distribution (Q-bit) rather than a point estimate, maintaining a global view of the search space
2. **Quantum rotation gates for distribution updates**: Solutions are updated via rotation operations that smoothly shift probability mass toward promising regions
3. **Quantum interference for exploration/exploitation balance**: Interference patterns naturally balance exploration (broad probability distributions) and exploitation (focused distributions)

### Why It Works Better

- **Global search view**: Q-bits encode probability across the entire search space, not just sampled points
- **Smooth transitions**: Rotation gates provide continuous, gradual updates (no disruptive jumps)
- **Automatic balance**: Interference intrinsically manages exploration vs. exploitation without manual parameter tuning

## Core Concepts

### Q-Bit Representation

A Q-bit encodes a candidate solution as a pair of probability amplitudes:

```
Q-bit: |ψ⟩ = α|0⟩ + β|1⟩,  where |α|² + |β|² = 1
```

- |α|² = probability of bit = 0
- |β|² = probability of bit = 1
- The full solution is a tensor product of Q-bits across all dimensions

For multi-dimensional continuous optimization:
- Each dimension has its own Q-bit representation
- Amplitudes parameterize a probability density over the search space

### Quantum Rotation Gate Update

The Q-bit state is rotated toward better solutions:

```
[α']   [cos(Δθ)  -sin(Δθ)] [α]
[β'] = [sin(Δθ)   cos(Δθ)] [β]
```

- Δθ (rotation angle) is determined by comparing current solution to best-known solution
- Direction and magnitude of rotation guide probability mass toward better regions
- Smooth, continuous update preserves search space structure

### Quantum Interference

When multiple candidate solutions overlap in the search space:
- **Constructive interference** amplifies promising regions
- **Destructive interference** suppresses poor regions
- This naturally balances exploration and exploitation

## Key Patterns

### Pattern 1: Q-Bit Initialization

```python
import numpy as np

def initialize_qbits(n_dimensions, n_populations):
    """Initialize Q-bit population with uniform superposition."""
    # Each Q-bit: [alpha, beta] where |alpha|^2 + |beta|^2 = 1
    qbits = np.ones((n_populations, n_dimensions, 2)) / np.sqrt(2)
    # Uniform distribution: equal probability for all states
    return qbits

def observe(qbits, n_samples=1):
    """Collapse Q-bits to classical binary solutions via measurement."""
    solutions = np.zeros((qbits.shape[0], qbits.shape[1]))
    for i in range(qbits.shape[0]):
        for j in range(qbits.shape[1]):
            if np.random.random() < qbits[i, j, 1]**2:
                solutions[i, j] = 1
    return solutions
```

### Pattern 2: Quantum Rotation Gate Update

```python
def rotate_qbits(qbits, best_solution, current_solutions, rotation_base=0.01):
    """Update Q-bit amplitudes via quantum rotation gates."""
    for pop_idx in range(qbits.shape[0]):
        for dim_idx in range(qbits.shape[1]):
            # Determine rotation direction and magnitude
            if current_solutions[pop_idx, dim_idx] != best_solution[dim_idx]:
                # Rotate toward the better solution
                alpha, beta = qbits[pop_idx, dim_idx]
                delta_theta = rotation_base * np.sign(
                    best_solution[dim_idx] - 0.5
                )
                
                # Apply rotation gate
                cos_t, sin_t = np.cos(delta_theta), np.sin(delta_theta)
                qbits[pop_idx, dim_idx, 0] = cos_t * alpha - sin_t * beta
                qbits[pop_idx, dim_idx, 1] = sin_t * alpha + cos_t * beta
    
    # Renormalize
    norm = np.sqrt(qbits[:,:,0]**2 + qbits[:,:,1]**2, keepdims=True)
    qbits /= norm
    return qbits
```

### Pattern 3: Interference-Based Exploration/Exploitation

```python
def quantum_interference(qbits, diversity_threshold=0.1):
    """Apply quantum interference to balance exploration/exploitation."""
    # Measure population diversity
    mean_beta = np.mean(qbits[:,:,1]**2, axis=0)
    diversity = np.std(qbits[:,:,1]**2, axis=0)
    
    for dim_idx in range(qbits.shape[1]):
        if diversity[dim_idx] < diversity_threshold:
            # Low diversity → increase exploration (flatten distribution)
            qbits[:, dim_idx, :] = 1 / np.sqrt(2)
        else:
            # High diversity → allow exploitation (sharpen distribution)
            # Constructive interference: amplify dominant amplitudes
            qbits[:, dim_idx, 1] = np.clip(
                qbits[:, dim_idx, 1] * 1.1, 0, 1
            )
    
    # Renormalize
    norm = np.sqrt(qbits[:,:,0]**2 + qbits[:,:,1]**2, keepdims=True)
    qbits /= norm
    return qbits
```

## Workflow

### Running QIEO for Non-Convex Optimization

1. **Define the objective function**: f(x) to minimize/maximize over search space
2. **Initialize Q-bit population**: Uniform superposition across all dimensions
3. **Main loop** (for each generation):
   - **Observe**: Collapse Q-bits to classical solutions via measurement
   - **Evaluate**: Score each solution against the objective function
   - **Update best**: Track the globally best solution found
   - **Rotate**: Apply quantum rotation gates to shift probability toward best
   - **Interfere**: Apply interference to balance exploration/exploitation
   - **Check convergence**: Stop if improvement plateaus or max generations reached
4. **Return best solution**

### Comparison: Traditional GA vs QIEO

| Aspect | Genetic Algorithm | QIEO |
|--------|------------------|------|
| Representation | Point estimates (bitstrings) | Q-bits (probability amplitudes) |
| Search view | Local (population sample) | Global (entire space encoded) |
| Update mechanism | Crossover + mutation | Quantum rotation gates |
| Exploration control | Manual (mutation rate) | Automatic (quantum interference) |
| Local minima escape | Limited | Strong (global probability view) |

## When to Use

| Scenario | Why QIEO |
|----------|----------|
| Non-convex ML loss landscapes | Global search view avoids local minima |
| Hyperparameter optimization | Probabilistic representation handles discrete + continuous |
| Combinatorial optimization | Natural Q-bit binary representation |
| Multi-modal objective functions | Interference identifies multiple promising regions |
| Noisy optimization problems | Probability smoothing handles noise |

## When NOT to Use

- Convex optimization (gradient descent is more efficient)
- Real-time optimization requiring single-step solutions
- Problems with very high dimensionalities (>1000 dims without decomposition)
- When exact gradient information is available and reliable

## Best Practices

1. **Start with uniform superposition**: Initialize all Q-bits at 1/√2 for unbiased exploration
2. **Adaptive rotation angles**: Scale Δθ based on generation number (large early, small late)
3. **Monitor diversity**: Use interference to prevent premature convergence
4. **Hybrid with local search**: Combine QIEO global search with gradient-based refinement
5. **Population size tuning**: 20-100 Q-bit individuals typically sufficient; scale with problem dimensionality

## Limitations

- Computational overhead from maintaining Q-bit population
- Requires careful normalization to maintain valid probability distributions
- Convergence analysis less mature than traditional evolutionary methods
- May be overkill for simple unimodal problems

## Implementation Parameters

| Parameter | Typical Range | Effect |
|-----------|--------------|--------|
| Population size | 20-100 | Larger = better coverage, more compute |
| Rotation base Δθ | 0.005-0.05 | Larger = faster convergence, risk of overshooting |
| Diversity threshold | 0.05-0.2 | Lower = more exploitation, higher = more exploration |
| Max generations | 100-1000 | Scale with problem complexity |

## Related Skills

- **compositional-quantum-heuristics**: Quantum heuristic design patterns
- **quantum-boltzmann-bilevel**: Quantum-inspired bilevel optimization
- **quantum-framework-agnostic-design**: Framework-agnostic quantum algorithm design
