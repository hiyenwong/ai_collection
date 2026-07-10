---
name: quantum-linear-solver-beyond-condition
version: 1.0.0
description: Quantum linear system solving methodology that overcomes the condition number barrier. Uses truncation-based and filtering-based solvers with complexity independent of worst-case condition number kappa. Introduces effective condition number bounds and affine dilation input model.
category: quantum
tags:
  - quantum
  - linear-systems
  - algorithms
  - numerical-analysis
  - condition-number
  - quantum-algorithms
trigger_words:
  - quantum linear system solver
  - quantum HHL algorithm
  - quantum linear equations
  - condition number quantum
  - quantum algorithm linear system
  - block encoding linear system
  - effective condition number
source_paper: "arXiv:2607.07691 - Faster quantum linear system solver beyond the condition number (2026)"
---

# Quantum Linear System Solver Beyond the Condition Number

## Overview

Two quantum algorithms for solving linear systems `Ax = b` with query complexity independent of the worst-case spectral condition number `κ = ||A^{-1}||`. Both solvers produce the normalized quantum state `|x⟩` to accuracy `ε`, dramatically improving upon the standard `O(κ)` dependence.

## Core Methodology

### Input Models

1. **Standard Block Encoding Model**: `A` accessed via block encoding, `|b⟩` prepared by unitary
2. **Affine Dilation Model** (novel): Encodes `A` and `|b⟩` jointly, enabling further query complexity refinements

### Solver 1: Truncation-Based

Query complexity to `A`:
```
O(κ_eff · polylog(κ_eff / ε))
```

Query complexity to `|b⟩`: **Optimal**

#### Effective Condition Number Bounds

For positive even integer `t`:
```
κ_eff ≤ ||(A†A)^{-t/2} |x⟩||^{1/t} / ε^{1/t}
```

For positive odd integer `t`:
```
κ_eff ≤ ||A^{-1†} (A†A)^{-(t-1)/2} |x⟩||^{1/t} / ε^{1/t}
```

### Solver 2: Filtering-Based

When solution norm is known:
```
Query complexity = 6 · ||A^{-1†} |x⟩|| / ε · ln(1/ε)
```

Extremely simple implementation with favorable runtime prefactor.

## Key Innovation: The κ-Barrier Breakthrough

Traditional quantum linear system solvers (e.g., HHL) have complexity scaling as `O(κ)`. This is a worst-case measure that can significantly overestimate runtime for typical instances. The new solvers achieve complexity dependent on `κ_eff`, which can be much smaller than `κ` for well-conditioned solution states.

## Solution Norm Estimator

A similarly simple estimator with the same asymptotic cost (up to logarithmic factors) for cases where `||x||` is unknown.

## Activation

This skill activates when designing quantum linear system algorithms, analyzing quantum algorithm complexity, implementing HHL-type solvers, or studying quantum numerical linear algebra.

## Related Concepts

- Block encoding techniques
- Quantum singular value transformation (QSVT)
- Effective vs spectral condition numbers
- Quantum state preparation
- Quantum algorithm complexity analysis
