---
name: geometric-typicality-entanglement
description: "Exact geometric typicality and bipartite entanglement methodology using projected central limit theorem on hyperspheres. Derives Beta distribution for subsystem occupation, Lubkin purity formula, and Bernoulli-factorized asymptotic expansion of mutual information for Haar-random states. Applicable to quantum information theory, random matrix theory, eigenstate thermalization."
category: quantum-mathematics
---

## Context

This skill extracts reusable methodology from arXiv:2605.29732 (Wang, Li, Braunstein — "Exact Geometric Typicality and Bipartite Entanglement from the Projected Central Limit Theorem on Hyperspheres"). The paper bridges statistical typicality on high-dimensional hyperspheres with quantum entanglement measures.

## Core Methodology

### 1. Projected Central Limit Theorem on Hyperspheres

- Start from uniform distribution on high-dimensional hypersphere S^{N-1}
- Project onto low-dimensional subspace to derive exact Beta distribution for subsystem occupation probabilities
- Quantifies finite-size "platykurtic" suppression of tails relative to Gaussian approximation
- Key insight: exact moments replace Gaussian approximation in eigenstate thermalization treatments

### 2. Lubkin Purity Formula Re-derivation

- Derive Lubkin's purity formula from elementary hyperspherical moments
- Avoids group-theoretic machinery (Schur-Weyl duality) — purely geometric approach
- Accessible to statisticians and probabilists without quantum information background

### 3. Bernoulli-Factorized Asymptotic Expansion

- For bipartite quantum mutual information ⟨I(A:B)⟩ of Haar-random pure states:
- Full asymptotic expansion in 1/N admits Bernoulli-factorized form
- Every order k ≥ 1 carries symmetric factor (d_A^{2k}-1)(d_B^{2k}-1)
- All higher odd-order corrections vanish identically
- Key structural result: symmetry between subsystems A and B at every perturbative order

### 4. Algebraic Reorganization of Page's Formula

- Exact algebraic reorganization separates leading finite-size correction into:
  - **Quantum coherence term**: (d_A² - 1)(d_B² - 1)/(2N) — dominant, su(d_A) ⊗ su(d_B) structure
  - **Classical probability term**: (d_A - 1)(d_B - 1)/(2N) — subtracted, Cartan ⊗ Cartan structure
- Trace separation to difference between diagonal and eigenvalue entropies via Schur's majorisation theorem
- Dimensional counts (d-1) and (d²-1) acquire meaning through Cartan structure of generalized Bloch decomposition

### 5. Non-perturbative Closed Form

- Exact typical mutual information: ⟨I(A:B)⟩ = (d_A²-1)(d_B²-1) · G(d_A, d_B, d_E)
- G given by explicit Bose-Einstein integral
- Asymptotic expansion reproduces full Bernoulli series

## Implementation Steps

1. **Define hyperspherical geometry**: Start with N-dimensional sphere, define projection operator onto subspace of dimension d_A × d_B
2. **Compute hyperspherical moments**: Use Beta function identities for exact moments of projected coordinates
3. **Derive occupation probabilities**: Map moments to subsystem occupation Beta distribution
4. **Compute purity**: Evaluate purity as second moment of projected distribution → Lubkin formula
5. **Mutual information expansion**: Expand mutual information in powers of 1/N, identify Bernoulli factors
6. **Separate quantum/classical terms**: Decompose using Cartan subalgebra vs full Lie algebra dimensions
7. **Closed form evaluation**: Express result as Bose-Einstein integral G(d_A, d_B, d_E)

## Pitfalls

- **Gaussian approximation trap**: Standard treatments use Gaussian CLT approximation; this methodology shows it misses platykurtic tail suppression. For finite-size systems (small N), the exact Beta distribution is essential.
- **Odd-order vanishing**: The vanishing of all higher odd-order corrections is a non-trivial symmetry result — do not assume corrections exist at every order.
- **Dimension counting**: The distinction between (d-1) and (d²-1) is subtle but critical — (d-1) counts Cartan subalgebra dimensions (classical), (d²-1) counts full Lie algebra dimensions (quantum coherence).
- **Bernoulli factors**: The Bernoulli numbers appear in the asymptotic expansion coefficients — ensure correct sign convention (B₁ = -1/2, B₂ = 1/6, etc.).

## Verification

- Reproduce Lubkin purity formula for small dimensions (d_A = d_B = 2) using hyperspherical moments
- Verify Bernoulli-factorized form matches known Page formula asymptotics
- Check that odd-order terms beyond first order vanish in the expansion
- Confirm Bose-Einstein integral G reproduces leading-order Page correction

## Activation

geometric typicality, bipartite entanglement, projected central limit theorem, hypersphere, Haar random states, Page formula, Lubkin purity, Bernoulli factorization, quantum mutual information, eigenstate thermalization, random matrix theory, 2605.29732
