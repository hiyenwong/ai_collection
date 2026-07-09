---
name: quantum-linear-solver-beyond-condition
category: quantum-algorithms
description: Quantum linear system algorithms with complexity independent of condition number κ. Introduces truncation-based and filtering-based solvers that overcome the κ-barrier for solving Ax=b. (arXiv: 2607.07691)
activation: quantum linear system, HHL algorithm, condition number barrier, quantum linear solver, truncation solver, filtering solver, effective condition number, quantum algorithm complexity
---

# Quantum Linear System Solvers Beyond the Condition Number

## Overview

This work presents two quantum algorithms that solve linear systems Ax=b with complexity **independent of the condition number κ**, breaking the traditional κ-barrier that limits quantum linear system solvers.

**Paper**: "Faster quantum linear system solver beyond the condition number" (arXiv:2607.07691, 2026-07-08)

## Key Results

### Truncation-Based Solver
- Query complexity: O(κ_eff · polylog(κ_eff/ε)) queries to A
- Optimal number of queries to |b⟩
- Effective condition number κ_eff ≤ ||(A†A)^{-t/2}|x⟩||^{1/t} / ε^{1/t} for positive even integer t

### Filtering-Based Solver
- Query complexity: 6·||A^{-1†}|x⟩||/ε · ln(1/ε) to leading order
- Extremely simple with favorable runtime prefactor
- Includes solution norm estimator with same asymptotic cost

## Problem Setting

Standard input model:
- A accessed through block encoding
- |b⟩ prepared by a unitary
- Goal: produce normalized solution |x⟩ to accuracy ε

### Affine Dilation Model (Novel)
- Encodes A and |b⟩ jointly
- Allows further refinements of query complexity

## Mathematical Foundation

### Traditional κ-Barrier
Standard quantum linear system solvers (HHL and variants) have complexity O(κ·polylog(κ/ε)), where κ = ||A^{-1}|| is the spectral condition number. This can significantly overestimate actual runtime for typical instances.

### Effective Condition Number Bounds
For positive even integer t:
```
κ_eff ≤ ||(A†A)^{-t/2}|x⟩||^{1/t} / ε^{1/t}
```

For positive odd integer t:
```
κ_eff ≤ ||A^{-1†}(A†A)^{-(t-1)/2}|x⟩||^{1/t} / ε^{1/t}
```

These bounds overcome the κ-barrier by depending on the actual solution structure rather than worst-case conditioning.

## Algorithm Design Patterns

### Truncation Approach
1. Expand solution in eigenbasis: |x⟩ = Σᵢ αᵢ|λᵢ⟩
2. Truncate small eigenvalue contributions
3. Use quantum signal processing for eigenvalue filtering
4. Complexity depends on κ_eff, not κ

### Filtering Approach
1. Apply filter function to suppress small eigenvalues
2. Use quantum amplitude amplification
3. Solution: 6·||A^{-1†}|x⟩||/ε · ln(1/ε) queries

## Implementation Considerations

```python
# Pseudocode for truncation-based solver
def truncation_solver(A_block_encoding, b_state, epsilon, t=2):
    """
    Truncation-based quantum linear system solver
    
    Args:
        A_block_encoding: Block encoding of matrix A
        b_state: Quantum state |b⟩
        epsilon: Target accuracy
        t: Power parameter for κ_eff bound (positive even integer)
    
    Returns:
        Quantum state approximating |x⟩ = A^{-1}|b⟩ / ||A^{-1}|b⟩||
    """
    # 1. Estimate effective condition number
    kappa_eff = estimate_effective_condition(A_block_encoding, t, epsilon)
    
    # 2. Truncate small eigenvalues
    truncated_state = apply_eigenvalue_truncation(
        A_block_encoding, b_state, kappa_eff
    )
    
    # 3. Quantum signal processing for filtering
    filtered_state = apply_qsp_filter(
        truncated_state, kappa_eff, epsilon
    )
    
    return filtered_state
```

## Pitfalls

- **Block encoding requirement**: Algorithm assumes efficient block encoding of A exists
- **Solution state preparation**: Requires |b⟩ to be efficiently preparable
- **Norm estimation**: Solution norm must be estimated separately (algorithm provides estimator)
- **t parameter selection**: Higher t gives tighter bounds but may increase computational overhead
- **Practical advantage**: Theoretical improvement may not translate to near-term quantum hardware

## Comparison with Prior Work

| Algorithm | Complexity | κ-dependent |
|-----------|-----------|-------------|
| HHL (original) | O(κ²·log(1/ε)) | Yes |
| Improved HHL | O(κ·polylog(κ/ε)) | Yes |
| Li (recent) | O(κ_eff·polylog) | Partially |
| This work | O(κ_eff·polylog) | No (uses κ_eff) |

## References

- arXiv:2607.07691 — Faster quantum linear system solver
- HHL algorithm (Harrow, Hassidim, Lloyd, 2009)
- Quantum signal processing (Low, Yoder, Chuang, 2016)
