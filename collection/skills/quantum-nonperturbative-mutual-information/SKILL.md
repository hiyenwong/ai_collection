---
name: quantum-nonperturbative-mutual-information
description: "Non-perturbative closed form for typical bipartite mutual information of Haar-random states. Extends Page formula with exact single expression using special functions, valid across all system sizes without asymptotic approximation. Use when: quantum entanglement entropy, Page curve, Haar-random state statistics, bipartite mutual information, random quantum states, entanglement thermodynamics."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29725"
  published: "2026-05-29"
  tags: [quantum-foundations, random-matrix-theory, entanglement, haar-random-states, mutual-information]
---

# Non-Perturbative Bipartite Mutual Information for Haar-Random States

## Source Paper

arXiv:2605.29725 — "Non-Perturbative Closed Form for the Typical Bipartite Mutual Information of Haar-Random States" (2026-05-29)

## Abstract

The average bipartite quantum mutual information of Haar-random pure states can be expressed exactly through Page formula in terms of digamma functions. We show that this quantity admits a single non-perturbative closed form expression using special functions, valid for all system sizes without requiring asymptotic expansion.

## Core Methodology

### Page Formula Background

For a random pure state on a bipartite Hilbert space H_A ⊗ H_B with dimensions d_A ≤ d_B:

**Page's average entanglement entropy:**
```
⟨S_A⟩ = ψ(d_A d_B + 1) - ψ(d_B + 1) - (d_A - 1)/(2 d_B)
```

Where ψ is the digamma function. For d_A d_B ≫ 1:
```
⟨S_A⟩ ≈ ln(d_A) - d_A/(2 d_B)
```

### Bipartite Mutual Information

For a pure state |ψ⟩ on H_A ⊗ H_B, the mutual information is:
```
I(A:B) = S_A + S_B - S_AB = 2 S_A
```
(since S_AB = 0 for pure states and S_A = S_B)

The average mutual information over Haar measure:
```
⟨I(A:B)⟩ = 2 ⟨S_A⟩
```

### Non-Perturbative Closed Form

The key contribution is expressing ⟨I(A:B)⟩ as a single closed form using special functions, valid for **all** d_A, d_B without requiring the large-dimension asymptotic expansion. This provides:

1. **Exact finite-size corrections** to the Page formula
2. **Unified expression** bridging small and large system limits
3. **Analytic continuation** properties useful for theoretical analysis

## Usage Patterns

### Pattern 1: Computing Exact Entanglement for Finite Systems

When precise entanglement values are needed for small-to-medium quantum systems:

1. Use the non-perturbative closed form instead of asymptotic Page formula
2. Compute exact digamma function values for given dimensions
3. Account for finite-size corrections explicitly

### Pattern 2: Benchmarking Quantum Randomness

Use when verifying that a quantum circuit produces Haar-random states:

1. Compute measured mutual information from experimental data
2. Compare against the exact non-perturbative prediction
3. Deviations indicate non-randomness or experimental noise

### Pattern 3: Entanglement Thermodynamics

Use when studying thermalization in isolated quantum systems:

1. Model subsystem reduced states as effectively Haar-random
2. Apply non-perturbative formula for exact thermal entropy
3. Track approach to equilibrium via mutual information dynamics

## Mathematical Framework

### Exact Mutual Information Formula

For dimensions (d_A, d_B) with d_A ≤ d_B:

```
⟨I(A:B)⟩_Haar = 2 [ψ(d_A d_B + 1) - ψ(d_B + 1) - (d_A - 1)/(2 d_B)]
```

This is exact for all finite d_A, d_B.

### Special Function Representation

The non-perturbative form expresses this using a unified special function representation that:
- Recovers Page's formula in the large-d limit
- Provides exact values for small dimensions
- Enables analytic continuation to complex dimensions

### Asymptotic Expansion

For d_A, d_B → ∞ with d_A/d_B fixed:
```
⟨I(A:B)⟩ ≈ 2 ln(d_A) - d_A/d_B + O(1/d_B²)
```

## When to Use

- Computing entanglement entropy for finite-dimensional quantum systems
- Benchmarking quantum random circuit sampling
- Studying Page curve dynamics in black hole information paradox
- Analyzing thermalization in many-body quantum systems
- Quantum information theory with finite-size effects

## Pitfalls

1. **Dimension ordering**: The formula assumes d_A ≤ d_B; swap if needed
2. **Pure vs mixed states**: Page formula applies to pure states on the composite system
3. **Numerical stability**: Digamma function evaluation may need care for very large arguments
4. **Haar measure assumption**: Results apply only to states distributed according to Haar measure

## Related Skills

- quantum-fisher-information-duality: QFI duality framework
- rademacher-quantum-circuits: Rademacher complexity for quantum circuits
- random-matrix-quantum-statistics: RMT analysis of quantum systems

## Activation Keywords

- Page formula mutual information
- Haar random state entanglement
- non-perturbative entanglement entropy
- bipartite quantum mutual information
- digamma function entanglement
- 量子纠缠熵
- 随机量子态
- Page curve exact form
