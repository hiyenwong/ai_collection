---
name: quantum-tunneling-optimization
description: "Quantum-inspired evolutionary optimization for non-convex ML landscapes using superposition-inspired probabilistic encoding and simulated tunneling to escape local optima. Use when classical optimizers (ADAM, GA, DE) get stuck in local minima on sparse signal recovery, robust regression, or any non-convex objective. Triggers: non-convex optimization, local optima escape, quantum tunneling optimizer, sparse signal recovery, robust regression, quantum evolutionary algorithm, superposition-inspired encoding"
---

# Quantum-Tunneling Optimization

## Overview

This skill provides quantum-inspired optimization techniques that overcome the fundamental limitation of classical optimizers: getting trapped in local optima of non-convex landscapes. The approach uses quantum superposition-inspired probabilistic representations and simulated quantum tunneling to traverse energy barriers.

Based on: *Exploring the non-convexity in machine learning using quantum-inspired optimization* (arxiv:2605.07947, May 2026).

## Core Problem: Local Optima Traps

Classical gradient-based and evolutionary optimizers fail on non-convex landscapes:

- **ADAM/SGD**: Gradient descent flows downhill, gets stuck in first local minimum
- **Genetic Algorithms**: Population diversity loss leads to premature convergence
- **Differential Evolution**: Mutation operator ineffective in high-dimensional narrow basins
- **Iterative Hard Thresholding**: Converges to sparse local optima

The QIEO framework beats all of these on sparse signal recovery and robust regression benchmarks.

## Technique 1: Quantum Superposition-Inspired Encoding

Represent candidate solutions as probabilistic superpositions rather than point estimates:

```python
import numpy as np

class QuantumInspiredIndividual:
    """
    Each gene is a probability amplitude pair [α, β] where
    |α|² + |β|² = 1, representing superposition of 0 and 1 states.
    """
    def __init__(self, n_genes):
        # Initialize as uniform superposition
        self.amplitudes = np.ones((n_genes, 2)) / np.sqrt(2)
    
    def observe(self):
        """Collapse superposition to classical solution via measurement."""
        probs = self.amplitudes[:, 0] ** 2  # Probability of |0⟩
        return (np.random.random(self.amplitudes.shape[0]) < probs).astype(int)
    
    def rotate(self, angles):
        """Apply quantum rotation gate to evolve superposition."""
        cos_t = np.cos(angles)
        sin_t = np.sin(angles)
        new_amps = np.zeros_like(self.amplitudes)
        new_amps[:, 0] = cos_t * self.amplitudes[:, 0] - sin_t * self.amplitudes[:, 1]
        new_amps[:, 1] = sin_t * self.amplitudes[:, 0] + cos_t * self.amplitudes[:, 1]
        # Normalize
        norms = np.linalg.norm(new_amps, axis=1, keepdims=True)
        self.amplitudes = np.where(norms > 0, new_amps / norms, new_amps)
```

**Key insight:** The superposition representation maintains exploration of the entire solution space simultaneously, unlike classical point-based representations.

## Technique 2: Quantum Tunneling Simulation

Simulate quantum tunneling to escape local optima:

```python
def quantum_tunneling_escape(current_solution, fitness, barrier_height, tunneling_rate=0.1):
    """
    Simulate quantum tunneling through energy barrier.
    Unlike classical hill-climbing, tunneling probability depends on
    barrier width, not just height.
    """
    # Tunneling probability: P ≈ exp(-2 * κ * w) where κ = √(2m(V-E))/ℏ
    barrier_width = estimate_barrier_width(current_solution, fitness)
    tunneling_prob = np.exp(-2 * tunneling_rate * barrier_width)
    
    if np.random.random() < tunneling_prob:
        # Tunnel to other side of barrier
        jump_distance = sample_from_tunneling_distribution(barrier_width)
        new_solution = current_solution + jump_distance
        return new_solution, True  # Successful tunnel
    
    return current_solution, False  # Stay put
```

**When to apply:** When fitness improvement stalls for >K generations, or when gradient magnitude falls below threshold.

## Technique 3: Hybrid Search Strategy

Combine quantum-inspired exploration with classical exploitation:

```python
def qieo_optimize(objective_fn, n_genes, n_individuals, max_generations):
    """
    Quantum-Inspired Evolutionary Optimization loop.
    """
    # Initialize population in superposition
    population = [QuantumInspiredIndividual(n_genes) for _ in range(n_individuals)]
    
    best_solution = None
    best_fitness = float('inf')
    
    for gen in range(max_generations):
        # Observation: collapse to classical solutions
        solutions = [ind.observe() for ind in population]
        fitnesses = [objective_fn(s) for s in solutions]
        
        # Update best
        gen_best_idx = np.argmin(fitnesses)
        if fitnesses[gen_best_idx] < best_fitness:
            best_fitness = fitnesses[gen_best_idx]
            best_solution = solutions[gen_best_idx]
        
        # Quantum-inspired crossover: interfere amplitudes
        for i in range(0, n_individuals, 2):
            crossover_angle = 0.1 * np.pi  # Small rotation
            population[i].rotate(np.full(n_genes, crossover_angle))
            population[i+1].rotate(np.full(n_genes, -crossover_angle))
        
        # Quantum-inspired mutation: random phase shift
        for ind in population:
            mutation_mask = np.random.random(n_genes) < 0.05
            mutation_angles = np.random.normal(0, np.pi/4, n_genes) * mutation_mask
            ind.rotate(mutation_angles)
        
        # Tunneling escape for stagnating individuals
        if gen > 10 and no_improvement(fitnesses, window=5):
            for ind in population:
                tunneling_angle = np.random.uniform(np.pi/8, np.pi/2, n_genes)
                ind.rotate(tunneling_angle)  # Large rotation = tunneling
        
        # Selection: keep best amplitudes
        ranks = np.argsort(fitnesses)
        elite_indices = ranks[:n_individuals // 2]
        for idx in ranks[n_individuals // 2:]:
            donor = np.random.choice(elite_indices)
            population[idx].amplitudes = population[donor].amplitudes.copy()
    
    return best_solution, best_fitness
```

## Activation Scenarios

Use this skill when:
- Optimizing non-convex objective functions with many local minima
- ADAM, SGD, or other gradient methods fail to converge
- GA/DE converge prematurely to suboptimal solutions
- Working on sparse signal recovery, compressed sensing
- Doing robust regression with heavy-tailed noise
- Hyperparameter tuning in complex loss landscapes
- Feature selection with combinatorial search space

## Comparison: When QIEO Outperforms Classical Methods

| Scenario | Best Classical | QIEO Advantage |
|----------|---------------|----------------|
| Sparse signal recovery | IHT | Tunnels through local sparse solutions |
| Robust regression | ADAM | Explores non-convex loss landscape better |
| Feature selection | GA | Maintains diversity via superposition |
| Hyperparameter tuning | Bayesian opt. | Parallel exploration of config space |

## Anti-Patterns to Avoid

1. **Too aggressive tunneling** — High tunneling rates prevent exploitation of found good regions
2. **Ignoring problem structure** — Custom rotation angles informed by problem structure outperform random rotations
3. **Pure quantum** — The hybrid approach (quantum exploration + classical refinement) is essential
4. **Single individual** — Population-based approach is key; single quantum-inspired optimization loses diversity
