---
name: quantum-tomography-retrodiction-unified
description: "Unified framework for quantum tomography and quantum retrodiction — proves Petz recovery map equals gradient update of log-likelihood in maximum-likelihood tomography, with noncommutative generalization for arbitrary quantum channels. Use when working with quantum tomography, quantum retrodiction, Petz recovery map, maximum-likelihood estimation, quantum channel inference, statistical inference in quantum systems, or gradient-based quantum state reconstruction."
metadata:
  arxiv_id: "2606.23777"
  published: "2026-06-22"
  authors: "Sebastian Murk, Ian Tan, Fabian Müller, Dominik Šafránek"
  tags: [quantum-tomography, quantum-retrodiction, petz-map, maximum-likelihood, quantum-channels, statistical-inference]
---

# Quantum Tomography-Retrodiction Unified Framework

Methodology from arXiv:2606.23777 bridging quantum tomography and quantum retrodiction.

## Core Insight

Quantum tomography and quantum retrodiction are manifestations of the same underlying principle:

**Petz recovery map = Gradient update of log-likelihood**

## Key Results

1. **Equivalence theorem**: For measurement channel E, the Petz recovery map R_E,σ is precisely the gradient update used in maximum-likelihood tomography.

2. **Monotonic likelihood**: Repeated applications of the Petz map monotonically increase the likelihood function.

3. **Noncommutative generalization**: Extends beyond measurement channels to arbitrary quantum channels via gradient of generalized likelihood.

4. **Iterative maximization**: The resulting procedure maximizes likelihood for general quantum tomography.

## Mathematical Framework

### Petz Recovery Map

For channel E and reference state σ:

```
R_E,σ(Y) = σ^(1/2) E†(E(σ)^(-1/2) Y E(σ)^(-1/2)) σ^(1/2)
```

### Connection to MLE

Given measurement data D, the log-likelihood L(ρ) = log P(D|ρ):

```
ρ_{n+1} = R_E,ρ_n (ρ_measured)
```

is equivalent to gradient ascent on L(ρ).

## Usage Patterns

### When to Apply

- Quantum state tomography with limited measurement data
- Quantum process tomography for unknown channels
- Retrodiction: inferring past states from current measurements
- Iterative reconstruction algorithms
- Statistical inference in quantum experiments

### When NOT to Apply

- Compressed sensing tomography (different regime)
- Direct fidelity estimation (single observable)
- Classical statistical problems

## Practical Implementation

```python
def petz_tomography_iteration(rho, measurement_data, measurement_channel, n_iter=100):
    """
    Iterative quantum tomography using Petz recovery map.
    
    rho: initial state estimate
    measurement_data: observed measurement outcomes
    measurement_channel: quantum channel E describing measurement
    n_iter: number of iterations
    """
    for _ in range(n_iter):
        # Compute Petz recovery update
        sigma = measurement_channel(rho)
        sigma_inv_sqrt = matrix_power(sigma, -0.5)
        rho_inv_sqrt = matrix_power(rho, 0.5)
        
        # Petz map application
        recovered = rho_inv_sqrt @ measurement_channel.adjoint(
            sigma_inv_sqrt @ measurement_data @ sigma_inv_sqrt
        ) @ rho_inv_sqrt
        
        rho = recovered / trace(recovered)  # normalize
    return rho
```

## Pitfalls

- **Singular reference state**: Petz map requires invertible σ; use regularization for near-singular states
- **Non-measurement channels**: Noncommutative generalization requires careful handling of arbitrary channel structure
- **Convergence**: Monotonic likelihood increase doesn't guarantee fast convergence; may need acceleration techniques
