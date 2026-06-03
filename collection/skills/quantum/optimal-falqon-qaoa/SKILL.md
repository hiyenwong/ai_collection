---
name: optimal-falqon-qaoa
description: "Optimal FALQON methodology for quantum approximate optimization. Treats per-layer time step (δ_k) and scaling factor (M_k) as decision variables optimized via classical methods, replacing fixed hyperparameters. Achieves statistically significant improvement over standard FALQON and QAOA on combinatorial problems. Use when: FALQON, quantum approximate optimization, NISQ combinatorial optimization, QAOA parameter tuning, quantum optimization algorithms, feedback-based quantum optimization, layer-wise quantum parameter optimization. Activation: FALQON optimization, optimal FALQON, QAOA parameter tuning, quantum combinatorial optimization, NISQ optimization, layer-wise quantum optimization."
---

# Optimal FALQON for Quantum Approximate Optimization

Methodology for improving Feedback-based Adaptive Quantum Optimization (FALQON) by treating per-layer parameters as optimization variables rather than fixed hyperparameters.

## Problem

Standard FALQON uses fixed hyperparameters (time step δ and scaling factor M), requiring hundreds to thousands of layers for acceptable solutions on combinatorial problems.

## Solution: Optimal FALQON

Treat per-layer time step (δ_k) and scaling factor (M_k) as **decision variables** optimized via classical methods:

$$\min_{\{\delta_k, M_k\}} \langle \psi(\{\delta_k, M_k\}) | H_C | \psi(\{\delta_k, M_k\}) \rangle$$

Where $H_C$ is the cost Hamiltonian and the quantum state evolves through layers with layer-specific parameters.

## Key Advantages

1. **Fewer layers needed**: Dramatically reduces circuit depth vs. standard FALQON
2. **NISQ-compatible**: Maintains single circuit evaluation per layer
3. **Better than QAOA**: Statistically significant improvement over QAOA variants
4. **Validated**: Empirical study on all 94 non-isomorphic 3-regular graphs with 12 vertices

## Workflow

### Step 1: Problem Formulation

Encode combinatorial problem as Ising/QUBO:
$$H_C = \sum_i h_i Z_i + \sum_{i<j} J_{ij} Z_i Z_j$$

### Step 2: Initialize FALQON Circuit

- Mixer Hamiltonian: $H_M = \sum_i X_i$
- Initial state: $|+\rangle^{\otimes n}$
- Layer depth: $p$ (typically small, e.g., 5-20)

### Step 3: Classical Optimization Loop

```python
def optimal_falqon(H_C, H_M, n_qubits, n_layers, optimizer):
    """Optimal FALQON with classical parameter optimization."""
    # Decision variables: {δ_k, M_k} for k = 1, ..., n_layers
    params = initialize_params(n_layers)
    
    for iteration in range(max_iterations):
        # Quantum circuit evaluation (single shot per layer)
        energy = evaluate_circuit(params, H_C, H_M, n_qubits)
        
        # Classical optimizer updates {δ_k, M_k}
        params = optimizer.step(energy, params)
    
    return params
```

### Step 4: Parameter Constraints

Constrain parameters to physically meaningful ranges:
- $0 < \delta_k < \pi$ (time step bounds)
- $M_k > 0$ (positive scaling)
- Optional smoothness: $|\delta_{k+1} - \delta_k| < \epsilon$

### Step 5: Comparison Benchmarks

Validate against:
- Standard FALQON (fixed parameters)
- QAOA with p=1,2,3,... layers
- Classical heuristics (simulated annealing, etc.)

## Implementation Patterns

### Gradient-Based Optimization

```python
import numpy as np
from scipy.optimize import minimize

def falqon_objective(params, H_C, H_M, n_qubits, n_layers):
    """Objective function: energy expectation value."""
    # Reshape params into {δ_k, M_k} pairs
    deltas = params[:n_layers]
    Ms = params[n_layers:]
    
    # Simulate FALQON circuit
    energy = simulate_falqon(deltas, Ms, H_C, H_M, n_qubits)
    return energy

# Optimize
n_layers = 10
x0 = np.random.uniform(0.1, 1.0, 2 * n_layers)
result = minimize(falqon_objective, x0, args=(H_C, H_M, n_qubits, n_layers),
                  method='COBYLA', bounds=[(0, np.pi)] * n_layers + [(0, None)] * n_layers)
```

### Parameter Transfer Learning

- Optimal parameters from small instances transfer to larger instances
- Use warm-start from smaller graph solutions

## Empirical Results (arXiv: 2605.08332)

- Tested on all 94 non-isomorphic 3-regular graphs with 12 vertices
- Statistically significant improvement over standard FALQON
- Outperforms multiple QAOA variants at equivalent depth

## Use Cases

- MaxCut on regular graphs
- Portfolio optimization
- Scheduling problems
- Graph coloring
- Any QUBO/Ising optimization on NISQ devices

## Related Skills

- `quantum-optimization-qaoa`: QAOA guide
- `quantum-boltzmann-machine-qaoa`: QAOA with QBM
- `quantum-portfolio-optimization`: Quantum finance optimization
- `quantum-portfolio-optimizer`: QAOA for portfolio optimization

## References

- arXiv:2605.08332 — Mancini & Sodagari (2026)
- FALQON original paper: Magann et al., Phys. Rev. Lett. (2022)
