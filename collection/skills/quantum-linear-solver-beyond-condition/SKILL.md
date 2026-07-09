---
name: quantum-linear-solver-beyond-condition
category: quantum
description: Quantum linear system algorithms with complexity independent of condition number - truncation-based and filtering-based solvers beyond the HHL kappa-barrier
trigger_words: quantum linear solver, condition number independence, HHL improvement, block encoding, filtering-based solver, truncation solver, quantum Ax=b
---

# Quantum Linear Solver Beyond Condition Number (Q-QLS)

## Overview

Two quantum algorithms for solving normalized linear systems Ax = |b⟩ with query complexity independent of the spectral condition number κ = ‖A⁻¹‖, overcoming the traditional κ-barrier in quantum linear system solvers. Based on Dalzell, Li, and Su (arXiv:2607.07691, 2026).

## Problem Setting

Given:
- Matrix A accessed via block encoding
- State |b⟩ prepared by unitary
- Goal: produce normalized solution |x⟩ = A⁻¹|b⟩ / ‖A⁻¹|b⟩‖ to accuracy ε

**Traditional HHL**: O(κ · polylog(κ/ε)) — scales linearly with condition number

**This work**: O(κ_eff · polylog(κ_eff/ε)) where κ_eff ≪ κ for typical instances

## Algorithm 1: Truncation-Based Solver

### Core Idea
Truncate the matrix inversion polynomial expansion based on effective condition number rather than worst-case κ.

### Complexity
- Queries to |b⟩: Optimal (minimal possible)
- Queries to A: O(κ_eff · polylog(κ_eff/ε))
- κ_eff bounds:
  - κ_eff ≤ ‖(A†A)^(-t/2)|x⟩‖^(1/t) / ε^(1/t) for even t
  - κ_eff ≤ ‖A^(-1†)(A†A)^(-(t-1)/2)|x⟩‖^(1/t) / ε^(1/t) for odd t

### Implementation Pattern
```python
def truncation_qls(block_encoding_A, state_b, epsilon, t=2):
    """
    Truncation-based quantum linear system solver.
    
    Args:
        block_encoding_A: Block encoding of matrix A
        state_b: Prepared state |b⟩
        epsilon: Target accuracy
        t: Polynomial degree parameter (even integer)
    """
    # 1. Estimate effective condition number
    kappa_eff = estimate_effective_condition(block_encoding_A, state_b, t)
    
    # 2. Truncate polynomial expansion at optimal degree
    poly_degree = optimal_truncation_degree(kappa_eff, epsilon)
    
    # 3. Apply truncated polynomial via block encoding
    solution_state = apply_truncated_polynomial(
        block_encoding_A, state_b, poly_degree
    )
    
    return solution_state
```

## Algorithm 2: Filtering-Based Solver

### Core Idea
Extremely simple filtering approach with favorable runtime prefactor.

### Complexity
- Leading order: 6 · ‖A^(-1†)|x⟩‖/ε · ln(1/ε) queries to A
- Same asymptotic cost for solution norm estimation (up to log factors)

### Implementation Pattern
```python
def filtering_qls(block_encoding_A, state_b, epsilon, known_norm=False):
    """
    Filtering-based quantum linear system solver.
    
    Args:
        block_encoding_A: Block encoding of matrix A
        state_b: Prepared state |b⟩
        epsilon: Target accuracy
        known_norm: Whether ‖A⁻¹|b⟩‖ is known a priori
    """
    if known_norm:
        # Optimal: 6 * ||A^{-1†}|x⟩||/ε * ln(1/ε)
        return filter_with_known_norm(block_encoding_A, state_b, epsilon)
    else:
        # First estimate norm, then filter
        norm_est = estimate_solution_norm(block_encoding_A, state_b, epsilon)
        return filter_with_estimated_norm(block_encoding_A, state_b, epsilon, norm_est)
```

## When to Use

### Prefer Truncation-Based:
- When effective condition number is significantly smaller than κ
- When higher precision is needed (polylog scaling in 1/ε)
- When matrix structure allows tight κ_eff bounds

### Prefer Filtering-Based:
- When simplicity is preferred
- When solution norm is known or easy to estimate
- When favorable constant factors matter more than asymptotic scaling

## Key Insights

1. **κ is a worst-case measure**: Typical problem instances have κ_eff ≪ κ
2. **Solution-dependent bounds**: κ_eff depends on |x⟩ itself, not just A
3. **Affine dilation model**: Joint encoding of A and |b⟩ allows further refinements
4. **Norm estimation**: Solution norm can be estimated with same asymptotic cost

## Pitfalls

- **Block encoding overhead**: The block encoding of A may itself be expensive
- **State preparation**: Preparing |b⟩ efficiently is non-trivial for arbitrary vectors
- **κ_eff estimation**: Requires additional quantum queries to bound
- **Normalization**: Output is normalized state |x⟩, not the unnormalized solution vector

## Activation

Use when: quantum linear systems, HHL improvement, condition number analysis, quantum algorithms, block encoding, quantum numerical linear algebra, quantum machine learning subroutines
