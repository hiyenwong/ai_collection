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

## Protocol Design

1. **Identify generators**: H = sum(theta_i * G_i)
2. **Compute QFI matrix**: F_Q[ij] = 4 * Cov(G_i, G_j) in optimal probe state
3. **Gradient projection**: Project gradient of target function onto QFI-inverse
4. **Optimal measurement**: Choose measurement saturating the single-parameter bound

## Application to Quantum Sensing

- Multiple field components (magnetic, electric, gravitational)
- Non-commuting observables (different spin directions)
- Function estimation (field magnitude, direction, gradients)

## Pitfalls

- Non-commuting generators introduce fundamental trade-offs
- Optimal probe state may be entangled across multiple probes
- Saturation requires collective measurements on all probes