---
name: loewner-order-algorithm
description: "Iterative algorithm to compute minimal upper bounds in the Loewner order on Hermitian matrices. Use for quantum information, convex optimization, operator theory, and numerical linear algebra tasks involving matrix inequalities."
metadata:
  arxiv_id: "2606.18173"
  published: "2026-06-16"
  authors: "Adam Humeniuk, Gabriel Jarry-Bolduc, Patrick Pascua"
  tags: [quantum-information, matrix-analysis, optimization, linear-algebra, loewner-order]
---

# Loewner Order Minimal Upper Bound Algorithm

## Description

An iterative method to exactly compute a minimal upper bound (MUB) for any finite collection of n×n Hermitian matrices under the Loewner order (positive semidefiniteness). The algorithm terminates in at most n iterations and applies to quantum information, control theory, numerical linear algebra, and operator theory.

## Activation Keywords
- loewner order, loewner upper bound
- hermitian matrix bound, matrix partial order
- quantum information matrix, matrix inequality
- positive semidefinite bound, minimal upper bound
- 算子理论, 半正定矩阵
- 量子信息矩阵不等式

## Core Mathematical Framework

### Loewner Order

For Hermitian matrices A, B: A ≤ B iff B - A is positive semidefinite (PSD).

Key property: Unlike scalar ordering, the Loewner order is a **partial order** — two Hermitian matrices may have multiple incomparable minimal upper bounds.

### Minimal Upper Bound (MUB)

A matrix M is a MUB of {A₁, ..., Aₖ} if:
1. M ≥ Aᵢ for all i (upper bound)
2. No M' < M satisfies M' ≥ Aᵢ for all i (minimal)

### Algorithm (at most n iterations)

```
Input: Hermitian matrices {A₁, ..., Aₖ} ∈ ℂⁿˣⁿ
Initialize: M₀ = max(λ_max(Aᵢ)) · I  (spectral upper bound)
For t = 0, 1, ..., n-1:
  1. Compute Dₜ = Mₜ - A_j for the "tightest" constraint j
  2. Find the smallest eigenvalue λ_min(Dₜ) and eigenvector v
  3. If λ_min(Dₜ) ≥ 0: Mₜ is already PSD for all constraints → done
  4. Update: Mₜ₊₁ = Mₜ - α·vv† where α minimizes the update
Output: Minimal upper bound M
```

### Key Theoretical Result

- Algorithm terminates in at most n iterations
- The MUB is characterized algebraically by Stott's conditions
- Self-contained proof provided in the paper

## Usage Patterns

### Pattern 1: Quantum State Comparison
Compare quantum states via density matrix ordering — find minimal states that dominate a set of given density matrices.

### Pattern 2: Convex Optimization
Use MUB computation as a subroutine in semidefinite programming where constraints are defined by Loewner ordering.

### Pattern 3: Control Theory
Compute minimal Lyapunov function bounds for stability analysis of linear systems.

## Error Handling

### Numerical Instability
If eigenvalue computations become unstable near termination:
- Use high-precision arithmetic for final iterations
- Apply small regularization ε·I to ensure strict PSD

### Non-uniqueness
MUBs are not unique in general — the algorithm finds ONE minimal bound. For comprehensive analysis, iterate with different initializations.

## References
- arXiv: 2606.18173 — "An algorithm to exactly compute minimal upper bounds in the Loewner order"
