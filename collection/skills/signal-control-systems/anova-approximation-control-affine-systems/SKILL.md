---
name: anova-approximation-control-affine-systems
description: Use when learning control-affine surrogates from state-control data. ANOVA index-set encoding.
category: research
---

# ANOVA Approximation for Control-Affine Systems (Coupled Least Squares)

Source: arXiv:2610.19858 — Kircheis (Mittweida), Potts, Schaller (Chemnitz), Worthmann (Ilmenau); DFG Project-ID 519323897. Julia code: gitlab.hrz.tu-chemnitz.de/manuels-at-tu-chemnitz.de/anova-for-control.

## Problem
Learn a surrogate of a control-affine discrete-time system x⁺ = F(x) + G(x)u from given samples (x_i, u_i, H(x_i,u_i)) where H = F(x)+G(x)u, in high state dimension d (e.g. discretized PDEs). Two blockers for standard ANOVA:
1. F and G cannot be sampled separately (one measurement gives only their combination).
2. Naive joint ANOVA over (x,u) wastes effort on control–control interactions u_ℓ·u_k that are excluded a priori by control affinity.

## Core Method — encode control affinity into the ansatz
Dictionary = state-basis functions AUGMENTED by the same functions times control components:

```
A_N(x,u) = Σ_μ a_μ φ_μ(x)  +  Σ_ℓ Σ_μ b_{μ,ℓ} φ_μ(x)·u_ℓ
```

- Affine linear in u **by construction** — no spurious control interactions ever arise.
- Works with arbitrary given state–control samples (no forced control values / experiment design needed).
- Implementation = pure PREPROCESSING of ANOVA index sets (Algorithm A.1): take the (d+m)-dim joint ANOVA index set and keep only terms with |u-index| ≤ 1; each kept term keeps its state part. Runs inside existing ANOVA software.
- Coupled least squares: solve one joint LSQ over the augmented dictionary; sensitivity-based term selection still applies (sparsity threshold on global sensitivity/Sobol indices).

## Theory (with explicit constants)
- **Prop 3.4**: limit M→∞ is the L²(Ω,ω)-orthogonal projection onto span{φ_μ, φ_μ·u_ℓ}.
- **Prop 3.7**: Marcinkiewicz–Zygmund inequality for the coupled ansatz space — norm equivalence discrete↔continuous L², uniform over the space, with high probability.
- **Thm 3.8**: probabilistic L² error bound with explicit constants, based on M–Z inequality; error splits into truncation (superposition dimension q), bandwidth (per-variable polynomial degree N), and estimation (sample count M) terms.
- **Rem 3.10 / Cor 3.13**: separate error control on drift F and input map G; extension to multivariate control u ∈ ℝ^m.
- Basis: Chebyshev (Ω=[−1,1], arcsine weight), tensor products; low-dimensional structure = few active ANOVA terms of low order.

## Numerical results
| Example | Outcome |
|---|---|
| Academic test function | Error >0.6 up to M=100; <10⁻⁶ at M=200; reaches LSQ solver accuracy 10⁻⁹–10⁻⁸ beyond. Truncation vanishes for q ≥ true order |
| Nonlinear advection–diffusion, shallow water equations, viscous Burgers | Dominant ANOVA couplings of F and G correctly identified via global sensitivity indices; for polynomial dynamics error hits solver accuracy (unless threshold discards relevant terms) |

## Reuse patterns
1. **Structure-encoding dictionaries**: when the physical model excludes whole interaction families (control affinity, positivity, conservation laws), delete those basis terms from the dictionary a priori instead of regularizing them away — the LSQ solution then cannot violate the structure.
2. **Index-set preprocessing**: impose structural constraints on an existing sparse-grid/ANOVA approximation framework by filtering multi-indices, not by writing a new solver.
3. **Sensitivity-driven identification**: global sensitivity (Sobol) indices of the learned surrogate double as a coupling-structure detector for PDE discretizations — each component couples mainly to spatial neighbors, so the index set is small.
4. **Separate drift/input error budgets** keep the surrogate valid when parameters change (re-identify G only, keep F, etc.).

## Pitfalls
- Sparsity threshold set too aggressively discards relevant terms and the error stalls above solver accuracy (observed).
- M must exceed ~(m+1)·O(active terms) — below that, error stays near 1 (underdetermined).
- q (superposition dimension) must be ≥ true interaction order for zero truncation error; verify by plateau of error vs q.
- Control-affinity is assumed exact; bilinear or control-quadratic terms are out of scope (use Koopman/bilinear EDMD instead).
