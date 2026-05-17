---
name: wavelet-variance-equipartition-quantum
description: >
  Wavelet variance equipartition methodology for assessing world model quality and
  determining classical simulability of amplitude-encoded quantum kernels. Uses wavelet
  scaling exponent α as a physics-grounded diagnostic: optimal representations satisfy
  variance equipartition (α ≈ 1/2) mirroring Kolmogorov's inertial range. Establishes
  α = 1/2 as a sharp transition boundary for classical simulability of quantum kernels
  using tensor networks. Use when: evaluating learned representations in world models,
  analyzing quantum kernel simulability, studying wavelet scaling in machine learning,
  or assessing tensor network efficiency for quantum simulation.
  Activation: wavelet variance equipartition, quantum kernel simulability, tensor network
  simulation, wavelet scaling exponent, world model quality, Kolmogorov inertial range.
---

# Wavelet Variance Equipartition for Quantum Kernel Analysis

Methodology from arXiv:2605.11557 — "Wavelet Variance Equipartition as a Threshold for World-Model Quality and Quantum Kernel TN-Simulability" (Kam, Cadet, Bessafi, 2026).

## Core Insight

The wavelet scaling exponent α serves as a universal diagnostic connecting:
1. **World model representation quality**: Optimal representations satisfy α ≈ 1/2
2. **Quantum kernel classical simulability**: α = 1/2 marks sharp transition boundary

## Wavelet Scaling Exponent α

For a signal or representation, the wavelet variance scales as:

    Var(W_j) ∝ 2^(-2αj)

where W_j are wavelet coefficients at scale j.

- **α < 1/2**: Persistent/long-range correlations — hard to simulate classically
- **α = 1/2**: Variance equipartition (Kolmogorov inertial range) — critical boundary
- **α > 1/2**: Anti-persistent/smooth — easy to simulate classically

## Connection to Quantum Kernel Simulability

For amplitude-encoded quantum kernels:

- When α < 1/2: Tensor network simulation requires exponentially large bond dimension
- When α = 1/2: Sharp transition in tensor network simulability
- When α > 1/2: Efficient classical simulation via tensor networks possible

## Application to World Models

World models learn compact latent representations of complex environments. The wavelet
scaling exponent provides a physics-grounded metric (not just empirical) for assessing
structural fidelity:

1. Compute wavelet transform of latent representations
2. Estimate scaling exponent α from wavelet variance across scales
3. Compare to α = 1/2 equipartition benchmark
4. Deviations indicate structural deficiencies in the learned representation

## Tensor Network Simulation Protocol

```python
# 1. Compute wavelet decomposition of data/representation
# 2. Estimate α from log-log plot of wavelet variance vs. scale
# 3. If α ≥ 1/2: tensor network simulation feasible
# 4. If α < 1/2: exponential bond dimension required
# 5. Use α to predict required TN bond dimension for given accuracy
```

## Key Findings

- α = 1/2 is a sharp phase transition, not a gradual boundary
- Tensor network efficiency directly correlated with wavelet scaling properties
- Provides quantitative criterion for when quantum advantage is achievable
- Connects statistical physics (Kolmogorov turbulence) to ML representation quality

## When to Apply

- Evaluating whether a quantum kernel offers genuine advantage over classical TN methods
- Assessing quality of learned representations in world models or autoencoders
- Determining bond dimension requirements for tensor network simulation
- Analyzing structural properties of high-dimensional data through wavelet lens
