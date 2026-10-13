---
name: broken-scale-symmetries-undercomplete-autoencoders
description: "欠完备线性自编码器：SGD破缺GL(k)标度对称，定向漂移到decoder-heavy权重直至稳定性边缘。"
category: ai_collection
---

# Broken Scale Symmetries in Undercomplete Linear Autoencoders

**Paper**: "Broken scale symmetries in undercomplete linear autoencoders" (arXiv: 2610.03640, Farhad Pashakhanloo & Jacob A. Zavatone-Veth, Harvard Center for Brain Science, Oct 2026). Note: authors used OpenAI Codex for simulation code generation (checked by hand).

## Core Finding (one sentence)

On the PCA solution manifold of undercomplete linear autoencoders, finite-stepsize SGD **breaks the GL(k) scale symmetry in a preferred direction** — it does not balance scales (as in noise-balancing accounts) but drifts **toward large decoder weights**, until curvature grows to the finite-stepsize stability boundary (edge of stability), so progressive sharpening occurs *without any learning of the function*.

## Setup and Symmetry

- Linear autoencoder f(x) = U(W x), W ∈ ℝ^{k×d} encoder, U ∈ ℝ^{d×k} decoder, k < d (undercomplete).
- **GL(k) symmetry**: (W, U) ↦ (W A, A⁻¹U) for any A ∈ GL(k) leaves the function invariant.
- Gradient flow **preserves** this symmetry: the Noether charge **Q = WᵀW − UUᵀ ∈ ℝ^{k×k} is conserved** (∂_t Q = 0 under gradient flow).
- Finite-stepsize **minibatch SGD breaks it**: Q accumulates changes slowly.

## Why Undercompleteness Selects a Direction (the geometry)

- **Contractive (undercomplete, k<d)**: perfect reconstruction is impossible. The reconstruction-anticorrelation term in the SGD noise does not vanish, and **no noise-balanced equilibrium exists** where drift terms cancel on average (contrast: Ziyin et al. 2025 balancing mechanism). Solution geometry selects a **preferred sign of scale drift**: decoder weights grow, encoder weights shrink (product fixed on the manifold).
- **Expansive (overcomplete)**: perfect reconstruction is possible — there is no fundamental geometric reason for directed drift.
- This is a *geometric* selection, not a statistical/noise-balancing equilibrium: the loss landscape converts **residual gradient noise into directed motion along a manifold of functionally-equivalent solutions**.

## Effective Scale Dynamics (analytically tractable)

Two-timescale separation under minibatch SGD (stepsize η, batch size B):
- Fast: T_fast ~ 1/η steps — relaxation back to the PCA manifold.
- Slow: T_slow ~ B/η² steps — accumulation of Q drift (T_fast/T_slow ~ η/B ≪ 1).

Leveraging this separation, the **scale degrees of freedom S = AᵀA** (A = balancing transformation) obey an effective flow in the η→0 limit:

**∂_τ S + S⁻¹(∂_τ S)S⁻¹ = S^(−1/2) C S^(−1/2)**  (Eq. 5)

where C = E[‖x_⊥‖² x_∥ x_∥ᵀ] involves the parallel/perpendicular decomposition of the data relative to the top-k PCA subspace. This predicts **anisotropic growth**: scale modes s_i = (WᵀW)_ii grow at *different* rates (dominant mode s₁ first), with excellent agreement to simulation at small finite stepsize. For co-diagonalizable cases the solution is explicit.

## Edge of Stability Endpoint

- Naively the effective dynamics would grow scale forever; but discrete-SGD stability fails when Hessian eigenvalues μ satisfy **η·μ ≳ κ (κ=2 for full-batch GD; edge-of-stability literature)**.
- The dangerous modes are μ₁₁^∥ > μ₁₂^∥ > … — curvature **increases with scale**, so drift self-terminates at the stability boundary: **progressive sharpening via pure manifold drift, after the function has already converged**.
- Sequential saturation: eigenvalues saturate one at a time near η·μ ≈ 2, matching edge-of-stability phenomenology — but here it reflects *zero ongoing learning*.

## Sharpness Measures Disagree (important caveat)

- **Population-Hessian sharpness** (max eigenvalue λ_max): increases with scale → endpoints are *sharper* than balanced baseline.
- **Batch sharpness** BS (Andreyev & Beneventano 2025, E[∇L_B ᵀ H_B ∇L_B]/E[‖∇L_B‖²]): on the PCA manifold **strictly decreasing in global scale — homogeneous of degree −1** (BS ∝ 1/s). The "modified batch sharpness" MBS (separately averaged numerator/denominator) is provably strictly decreasing under the effective dynamics for Gaussian data with balanced initialization.
- So "the network sharpens" is measure-dependent: λ_max↑ while BS/MBS↓ simultaneously. Any sharpness-based stability criterion must specify which object it tracks.

## Nonlinear Extension (preliminary)

- Homogeneous activations (ReLU) break GL(k) down to **per-neuron positive-diagonal scaling** (A diagonal, A_ij > 0).
- Undercomplete ReLU autoencoders show similar **directed drift toward decoder-heavy weights** (Fig. S2) — the bias is not a linear-only artifact; in-depth geometric basis left to future work.

## When to Use This Skill

- Analyzing SGD symmetry breaking / scale (balanced vs feature-learning) regimes in autoencoders and homogeneous networks — the *direction* of drift is geometry-selected in undercomplete nets, not noise-balanced.
- Interpreting edge-of-stability / progressive-sharpening phenomena: sharpening can be pure parameter-space drift along a function-invariant manifold (no functional learning) — caution when reading "sharpness = learning progress".
- Choosing sharpness measures: population λ_max vs batch sharpness move in **opposite** directions here — an explicit counterexample to treating sharpness as a scalar.
- Theoretical work on SGD-induced implicit bias in linear models with non-unimodal solution manifolds; Noether-charge analyses of training dynamics.

## Key Formulas

| Object | Expression |
|---|---|
| Conserved charge (gradient flow) | Q = WᵀW − UUᵀ, ∂_t Q = 0 |
| Effective scale flow | ∂_τ S + S⁻¹(∂_τ S)S⁻¹ = S^(−1/2) C S^(−1/2) |
| Slow/fast timescales | T_slow ~ B/η², T_fast ~ 1/η |
| Stability condition | η·λ_max(Hessian) ≲ κ (κ=2 full-batch) |
| Batch sharpness scaling | BS ∝ 1/s (homogeneous degree −1) |

## Related Skills

- [[weight-geometry-functional-memory]] — weight geometry governing function in recurrent networks
- [[hessian-null-space-continuation]] — mode-connectivity through Hessian null-space traversals
- [[lyapunov-spectrum-random-neural-networks]] — complementary random-network curvature analysis
