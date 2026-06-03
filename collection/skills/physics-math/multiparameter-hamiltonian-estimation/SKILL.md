---
name: multiparameter-hamiltonian-estimation
description: >
  Optimal multiparameter estimation for quantum systems using the unified
  Cramér-Rao bound framework. Use when: (1) estimating functions of multiple
  parameters in quantum Hamiltonians, (2) designing quantum sensing protocols,
  (3) analyzing precision limits for non-commuting generators, (4) optimizing
  quantum metrology with multiple parameters. Based on arXiv:2605.04136.
---

# Multiparameter Hamiltonian Estimation

Ultimate quantum limit and estimation protocol for functions of multiple
parameters in general Hamiltonians (arXiv:2605.04136).

## Core Result

The multiparameter estimation problem reduces to an optimized single-parameter
quantum Cramér-Rao bound, even for arbitrary (possibly non-commuting) generators.

## Key Insight

Although estimating a function f(theta_1, ..., theta_k) of k parameters is
fundamentally multiparameter, the tight bound equals:

    Var(f_hat) >= (nabla f)^T * F_Q^{-1} * (nabla f) / N

where F_Q is the quantum Fisher information matrix and N is the number of probes.

## Protocol Design

1. **Identify generators**: Express Hamiltonian as H = sum(theta_i * G_i)
2. **Compute QFI matrix**: F_Q[ij] = 4 * Cov(G_i, G_j) in optimal probe state
3. **Gradient projection**: Project gradient of target function onto QFI-inverse
4. **Optimal measurement**: Choose measurement saturating the single-parameter bound

## Application to Quantum Sensing

For sensing applications:
- Multiple field components (magnetic, electric, gravitational)
- Non-commuting observables (different spin directions)
- Function estimation (field magnitude, direction, gradients)

## Advantages Over Prior Work

- Unifies single-parameter and multiparameter bounds
- Handles arbitrary generator sets (commuting and non-commuting)
- Provides constructive estimation protocol
- Tight bound achievable with appropriate measurement strategy

## Pitfalls

- Non-commuting generators introduce fundamental trade-offs
- Optimal probe state may be entangled across multiple probes
- Saturation requires collective measurements on all probes
- Finite-N corrections may be significant for small sample sizes
