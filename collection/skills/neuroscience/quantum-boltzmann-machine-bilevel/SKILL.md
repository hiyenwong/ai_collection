---
name: quantum-boltzmann-machine-bilevel
description: >
  Quantum Boltzmann Machine via Bilevel Optimization methodology. Extends QAOA
  circuit to bilevel optimization for fully connected QBMs, overcoming the
  fixed target Hamiltonian barrier. Use when building quantum generative models,
  training quantum Boltzmann machines, or extending QAOA for ML applications.
  arXiv:2605.07473
---

# Quantum Boltzmann Machine via Bilevel Optimization

## Description

Breaks QAOA's fixed target Hamiltonian barrier by enabling flexible Hamiltonian
construction through bilevel optimization. Creates fully connected Quantum
Boltzmann Machines that capture complex energy landscapes for optimization
and machine learning.

## Activation Keywords
- quantum boltzmann machine
- QBM bilevel optimization
- QAOA extension
- quantum generative model
- quantum energy-based model
- bilevel quantum optimization
- fully connected QBM
- quantum approximate optimization extension

## Core Architecture

### Bilevel Optimization Framework

```
Upper level:  Optimize QBM parameters (weights, biases)
  → Minimize KL divergence between model and data distributions
Lower level:  Optimize QAOA circuit parameters
  → Prepare thermal state of current Hamiltonian
```

### Algorithm

```python
def train_qbm_bilevel(data_samples, p_layers=3, n_qubits=None, max_iter=100):
    """Train fully connected QBM via bilevel optimization.
    
    Args:
        data_samples: Binary data vectors
        p_layers: Number of QAOA layers
        n_qubits: Number of qubits (defaults to data dimension)
    """
    n = n_qubits or len(data_samples[0])
    
    # Initialize Hamiltonian parameters
    # Fully connected: h_i (biases) + J_ij (couplings)
    biases = np.random.randn(n) * 0.1
    couplings = np.random.randn(n, n) * 0.1
    couplings = (couplings + couplings.T) / 2  # Symmetric
    
    for iteration in range(max_iter):
        # LOWER LEVEL: Optimize QAOA circuit for current H
        gamma, beta = optimize_qaoa_circuit(biases, couplings, p_layers)
        
        # UPPER LEVEL: Update Hamiltonian to match data
        model_expectation = compute_expectations(gamma, beta, biases, couplings)
        data_expectation = compute_data_expectations(data_samples)
        
        # Gradient update (contrastive divergence style)
        grad_biases = data_expectation['local_z'] - model_expectation['local_z']
        grad_couplings = data_expectation['ZZ'] - model_expectation['ZZ']
        
        biases += learning_rate * grad_biases
        couplings += learning_rate * grad_couplings
    
    return biases, couplings
```

## Key Innovations

1. **Flexible Hamiltonian**: Unlike standard QAOA with fixed mixing/problem
   Hamiltonians, this approach learns the Hamiltonian itself
2. **Full Connectivity**: All-to-all couplings (J_ij for all i,j) vs
   QAOA's limited connectivity
3. **Bilevel Structure**: Inner loop prepares states, outer loop learns model
4. **Generative Capability**: Can sample from learned distribution

## Comparison

| Method | Connectivity | Hamiltonian | Training |
|--------|-------------|-------------|----------|
| Classical BM | Full | Fixed | CD/k-CD |
| Standard QBM | Limited | Fixed | Gradient-based |
| QAOA | Problem-specific | Fixed | Variational |
| **QBM-Bilevel** | **Full** | **Learned** | **Bilevel** |

## Use Cases

- **Generative Modeling**: Learn and sample from complex distributions
- **Optimization**: Find low-energy states of learned Hamiltonians
- **Feature Learning**: Extract hidden representations from data
- **Quantum-Classical Hybrid**: Bridge classical ML with quantum circuits

## Pitfalls

- Bilevel optimization is computationally expensive
- Inner loop convergence affects outer loop quality
- Requires careful balancing of learning rates at both levels
- Near-term hardware limitations on qubit count and connectivity

## References
- arXiv:2605.07473 - "Breaking QAOA's Fixed Target Hamiltonian Barrier"
