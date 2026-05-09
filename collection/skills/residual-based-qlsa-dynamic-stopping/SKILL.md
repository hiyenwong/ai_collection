---
name: residual-based-qlsa-dynamic-stopping
description: >
  Residual-based Quantum Linear System Algorithm (QLSA) with a posteriori dynamic stopping.
  Provides verifiable convergence guarantees for solving Ax = b on quantum computers by
  computing residual norms ||b - Ax|| without full state tomography.
  Use when: (1) designing QLSA convergence checks, (2) implementing HHL-type algorithms
  with practical stopping criteria, (3) comparing quantum vs classical linear solvers,
  (4) analyzing QLSA runtime dependence on condition number kappa, (5) building
  quantum numerical linear algebra pipelines.
  Trigger: QLSA, quantum linear system, HHL stopping, residual norm, quantum convergence
---

# Residual-Based QLSA with Dynamic Stopping

## Problem

Standard QLSAs (HHL and variants) output a quantum state |x> proportional to A⁻¹|b>,
but offer no way to check solution quality without destroying the state. Classical
iterative solvers use residuals ||b - Ax|| to adaptively stop; this skill port that
pattern to the quantum setting.

## Core Algorithm

### Residual State Preparation

Given |ψ_b> = |b>/||b||, prepare the normalized residual state:

```
|ψ_r> = (|0> ⊗ |b> - |1> ⊗ |Ax>) / ||r||
```

where ||r|| = ||b - Ax|| is the residual norm.

### a Posteriori Estimation

1. **Prepare** |ψ_r> using controlled application of A
2. **Estimate** ||r||/||b|| via amplitude estimation on |0> register
3. **Compare** to tolerance ε: if ||r||/||b|| < ε, accept solution
4. **Iterate** otherwise: increase QLSA precision and retry

### Key Complexity Result

The a posteriori verification step runs in:
- **O(κ · polylog(N) / ε)** queries to A and |b>
- where κ = condition number, N = matrix dimension

This is asymptotically equivalent to one QLSA run, making verification "free."

## Implementation Pattern

```python
def residual_check(qlsa_state, b_state, A_operator, epsilon):
    """
    Verify QLSA solution without destroying |x>.
    
    Args:
        qlsa_state: quantum register holding |x>
        b_state: quantum register holding |b>
        A_operator: block-encoding of matrix A
        epsilon: relative tolerance ||r||/||b|| < eps
    
    Returns:
        (accepted, residual_estimate)
    """
    # 1. Prepare residual superposition
    controlled_apply_A(qlsa_state, b_state, A_operator)
    
    # 2. Estimate amplitude of |0> register
    residual_norm = amplitude_estimate(control_qubit)
    
    # 3. Decision
    accepted = residual_norm < epsilon
    return accepted, residual_norm
```

## Design Guidelines

### When to Use A Posteriori vs A Priori

| Criterion | A Priori | A Posteriori |
|-----------|----------|-------------|
| Condition number known | Yes | Either |
| κ is loose bound | Wasteful | Tight |
| Solution quality critical | Insufficient | Recommended |
| Runtime budget fixed | Preferred | Risk of overrun |

### Parameter Selection

- **Tolerance ε**: Set based on downstream task sensitivity
- **Condition number κ**: Use power iteration or classical precomputation
- **Block-encoding precision**: Match ε to avoid over-refinement

### Classical Comparison

Always benchmark against classical iterative solvers (CG, GMRES):
- QLSA advantage: O(κ · log(N)/ε) vs O(κ · N/ε) classically
- But: state preparation + readoverhead can negate speedup for small N
- Crossover typically at N > 10⁶ for sparse, well-conditioned systems

## Pitfalls

1. **State preparation cost**: Loading |b> can dominate total runtime
2. **Block-encoding overhead**: Sparse matrix encoding adds log(N) factors
3. **Readout cost**: Extracting classical x from |x> requires O(N) measurements
4. **κ dependence**: Runtime scales linearly with condition number
5. **Noise sensitivity**: NISQ devices degrade residual estimation accuracy

## Related Skills

- `quantum-ml-data-loading` — state preparation techniques
- `quantum-neural-network-designer` — QNN architecture design
- `quantum-algorithm-framework-designer` — general quantum algo patterns

## Paper

arXiv:2605.06414 — "A Residual-Based Quantum Linear System Algorithm with
Dynamic Stopping" (2026)
