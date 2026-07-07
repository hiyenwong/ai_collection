---
name: "quantum-ergodicity-semiclassical"
description: "Mathematical framework for quantum ergodicity and semiclassical measures. Covers high-frequency eigenmodes of the Laplacian on chaotic manifolds, the Quantum Ergodicity theorem (Schnirelman), Quantum Unique Ergodicity conjecture, and Kolmogorov-Sinai entropy constraints on semiclassical measures. Use for quantum chaos, semiclassical analysis, eigenmode distribution, or mathematical physics research."
metadata:
  arxiv_id: "2606.12098"
  published: "2026-06-10"
  tags: [quantum, ergodicity, semiclassical, chaos, mathematical-physics, eigenmodes, laplacian]
---

# Quantum Ergodicity & Semiclassical Measures

## Core Concept

Studies the macroscopic distribution of high-frequency eigenmodes of the Laplacian on compact manifolds where the geodesic flow is chaotic. The distribution is characterized by **semiclassical measures** — probability measures on phase space describing where quantum mass concentrates in the classical limit.

## Mathematical Framework

### Quantum Ergodicity Theorem (Schnirelman)

For a compact manifold M with chaotic geodesic flow:

```
If {φ_j} are Laplacian eigenfunctions with eigenvalues λ_j → ∞,
then there exists a density-one subsequence {φ_{j_k}} such that
the semiclassical measures converge to Liouville measure.
```

This means "most" high-frequency eigenmodes equidistribute in phase space.

### Quantum Unique Ergodicity (QUE) Conjecture

**Conjecture**: For manifolds with negative curvature (strongly chaotic/Anosov systems), the FULL sequence of eigenmodes equidistributes — not just a density-one subsequence.

**Partial results**: Proven for specific cases including arithmetic surfaces (Lindenstrauss, Soundararajan).

### Kolmogorov-Sinai Entropy Constraints

For Anosov systems, admissible semiclassical measures μ must satisfy:

```
h_KS(μ) ≥ (1/2) h_KS(Liouville)
```

This lower bound rules out measures concentrated on periodic orbits.

## Usage Patterns

### Pattern 1: Eigenmode Analysis on Chaotic Manifolds

When analyzing high-frequency eigenmodes on manifolds with chaotic geodesic flow:

1. Verify the geodesic flow is ergodic (mixing, Anosov, etc.)
2. Apply Quantum Ergodicity theorem for density-one subsequence results
3. For negative curvature: check QUE conjecture applicability
4. Compute semiclassical measures to characterize eigenmode concentration

### Pattern 2: Semiclassical Measure Construction

To construct or verify semiclassical measures:

1. Take eigenfunction sequence φ_j with λ_j → ∞
2. Compute Wigner distributions W_j on phase space T*M
3. Extract weak-* limit points → these are semiclassical measures
4. Verify invariance under geodesic flow

### Pattern 3: Manifolds with Boundary

For domains with boundary:

1. Apply Schnirelman's theorem with boundary condition adjustments
2. Dirichlet/Neumann conditions affect the measure class
3. Billiard dynamics replace geodesic flow

## Key Results Summary

| System | Result | Status |
|--------|--------|--------|
| General chaotic | Quantum Ergodicity (density-1) | ✅ Proven |
| Negative curvature | QUE (full sequence) | Partial results |
| Arithmetic surfaces | QUE | ✅ Proven |
| Anosov flows | KS entropy lower bound | ✅ Proven |
| Manifolds w/ boundary | QE with adjustments | ✅ Proven |

## Pitfalls

### Density-One vs Full Sequence

- Quantum Ergodicity guarantees equidistribution for a density-one **subsequence**, NOT the full sequence
- QUE conjecture is strictly stronger and remains open in general
- Don't claim full equidistribution without verifying QUE conditions

### Manifolds with Boundary

- Boundary conditions (Dirichlet/Neumann) significantly affect results
- Bouncing ball modes can concentrate on specific trajectories
- Geodesic flow must be replaced by billiard dynamics

### Semiclassical Limit

- Results apply as ℏ → 0 (or equivalently λ → ∞)
- Finite-frequency eigenmodes may show significant deviations
- Numerical verification requires very high eigenvalues

## Activation

- quantum ergodicity, semiclassical measures, quantum chaos, eigenmodes, laplacian, schnirelman theorem, QUE conjecture, kolmogorov-sinai entropy, anisov flow, mathematical physics, 量子遍历性, 半经典测度
