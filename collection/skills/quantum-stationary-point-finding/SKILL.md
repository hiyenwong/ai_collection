---
name: quantum-stationary-point-finding
description: Quantum comparison oracle methodology for finding stationary points of non-convex functions with quadratic speedup — O~(n/epsilon^1.5) quantum vs O~(n^2/epsilon^1.5) classical queries. ICML 2026 paper by Wang et al.
category: quantum
tags:
  - quantum-optimization
  - non-convex-optimization
  - quantum-algorithms
  - stationary-points
  - comparison-oracle
  - icml
arxiv: "2606.27082"
date: "2026-06-26"
---

# Quantum Stationary Point Finding by Comparisons

## Trigger Conditions
Use this skill when:
- Optimizing non-convex functions with only comparison oracle access (no gradient information)
- Need to find epsilon-stationary points efficiently
- Classical comparison-based optimization is too slow (O~(n^2) queries)
- Quantum access to comparison oracle is available (superposition queries)
- Working with black-box optimization where function values can be compared but not differentiated

## Methodology

### Core Result
**First quantum algorithm** for finding stationary points using only comparison queries:
- **Quantum**: O~(n/epsilon^1.5) queries — quadratic speedup
- **Classical**: O~(n^2/epsilon^1.5) queries
- **Assumption**: Function is twice differentiable with Lipschitz gradient and Hessian

### Key Subroutine: Normalized Hessian Estimation
- Estimates the normalized Hessian to accuracy delta
- Uses O~(n^2 * log(1/delta)) comparison queries
- This subroutine is the core technical contribution

### Algorithm Structure
1. **Hessian estimation** via quantum comparison oracle in superposition
2. **Normalized gradient computation** using estimated Hessian
3. **Iterative refinement** toward epsilon-stationary point
4. **Quantum speedup** comes from superposition queries to comparison oracle

### Comparison Oracle Model
- Given two points x, y: outputs sign(f(x) - f(y))
- Quantum version: queries can be made in superposition
- This is weaker than gradient oracle but stronger than zeroth-order oracle

## Implementation Considerations

### Requirements
- Function f: R^n → R twice differentiable
- Lipschitz gradient: ||∇f(x) - ∇f(y)|| ≤ L||x - y||
- Lipschitz Hessian: ||∇²f(x) - ∇²f(y)|| ≤ M||x - y||
- Quantum comparison oracle access

### Complexity Breakdown
| Component | Query Complexity |
|-----------|-----------------|
| Hessian estimation | O~(n^2 * log(1/delta)) |
| Full algorithm | O~(n / epsilon^1.5) |
| Classical baseline | O~(n^2 / epsilon^1.5) |

### Practical Applicability
- **Near-term**: Theoretical result; requires fault-tolerant quantum computer
- **Comparison oracle**: More realistic than gradient oracle for some applications
- **ICML 2026**: Peer-reviewed, accepted to top ML conference

## Pitfalls
- **Oracle assumption**: Requires quantum comparison oracle, not yet available on NISQ devices
- **Smoothness assumptions**: Requires twice differentiable with Lipschitz conditions
- **Dimension scaling**: Still linear in n (though quadratically better than classical)
- **Constant factors**: Big-O hides potentially large constants

## Related Papers
- arXiv:2606.27082 — Finding Stationary Points by Comparisons (ICML 2026)
- Authors: Helin Wang, Chenyi Zhang, Xiwen Tao, Yexin Zhang, Tongyang Li

## Activation
quantum stationary points, comparison oracle optimization, non-convex quantum optimization, quadratic speedup optimization, quantum gradient-free, hessian estimation quantum, epsilon-stationary point, ICML quantum algorithm