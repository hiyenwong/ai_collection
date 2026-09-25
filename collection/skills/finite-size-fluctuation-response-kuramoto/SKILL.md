---
name: finite-size-fluctuation-response-kuramoto
description: Finite-N FRR for noisy coupled phase oscillators.
category: ai_collection
metadata:
  arxiv_id: "2609.28834"
  published: "2026-09-23"
  authors: "Mrinal Sarkar (Heidelberg), Yoshiyuki Y. Yamaguchi (Kyoto)"
  tags: [fluctuation-response, kuramoto, dean-kawasaki, finite-size, landau-poles, nonequilibrium, neural-oscillations]
---

# Finite-Size Fluctuation–Response Relation (F-FRR) for Noisy Coupled Phase Oscillators

Methodology from arXiv:2609.28834 (Sarkar & Yamaguchi, PRL-style Letter, Sep 2026). Derives TWO exact fluctuation–response relations in the incoherent phase of finite-N noisy mean-field coupled phase oscillators (Kuramoto-type): the naive infinite-size FRR (I-FRR) and a finite-size-corrected FRR (F-FRR) whose correction factor is a spectrum function Λ_n(s) whose roots are Landau poles of the linearized operator. Use when analyzing macroscopic order-parameter fluctuations in oscillator/brain-rhythm models at finite N, or when equilibrium fluctuation–dissipation reasoning fails.

## Problem

Equilibrium FDT links spontaneous fluctuations to linear response. Nonequilibrium steady states violate it, and finite systems add a second fluctuation source (finite-size noise ~ 1/√N) on top of external noise. Experiments/simulations are always finite — what is the correct FRR for macroscopic observables (order parameter Z_n) in a finite-N noisy coupled-oscillator system?

## Setup

N globally-coupled phase oscillators (general kernel Γ(θ), natural-frequency distribution g(ω), noise D):

```
θ̇_j = ω_j + (1/N)·Σ_k Γ(θ_j−θ_k) + H(θ_j,t) + √(2D)·ξ_j(t)
```

Order parameters Z_n(t) = (1/N)·Σ_k e^{inθ_k(t)}. Incoherent phase: ⟨Z_n⟩ = 0.

Two correlation functions of Z_n:
- **C_n^ini(t) = C_n(t, 0)** — initial-value correlation, reference time pinned at t=0 (this is the N→∞ stationary correlation)
- **C_n(t) = ⟨C_n(t,τ)⟩_τ** — time-averaged stationary correlation of the finite-N stationary state (the experimentally accessible one)

They DIFFER: a finite-N system starting from the infinite-size stationary state relaxes and **generates additional correlations** (macroscopic order parameter magnitude grows even below the critical coupling, then saturates).

## Main Results (Laplace domain)

Both FRRs derived from the linearized **Dean–Kawasaki equation** (exact stochastic density evolution; the DK term √(2D·F^st/∂θ·ζ)/√N captures finite-N fluctuations):

```
I-FRR:  R̂_n(s) = −inN·Ĉ_n^ini(s)·Ĥ_n(s)                 (no finite-size correction)
F-FRR:  R̂_n(s) = −inN·Λ_{−n}(−s)·Ĉ_n(s)·Ĥ_n(s)          (finite-size correction)
```

where the response R_n(t) = Z_n^h(t) (order parameter under weak external force H) and the **spectrum function**:

```
Λ_n(s) = 1 + Γ_n^/2 · ∫ i·n·g(ω)/(s + inω + D·n²) dω     (Landau contour integral)
```

- Roots of Λ_n(s) = eigenvalues/Landau poles of the linearized operator → stability of the incoherent state
- **Λ_{−n}(−s) is the finite-size correction factor**: encodes correlations generated while relaxing to the finite-N stationary state
- Λ → 1 in the weak-coupling limit (Γ_n → 0) or strong-noise limit (D → ∞) ⇒ F-FRR reduces to I-FRR
- Validity window: |H| ≪ 1 but |H| ≫ 1/√N (perturbation dominates finite-size noise)

## Time-Domain (experimentally usable) Form

For external force H(θ,t) = −h·Θ(t)·sin(θ − ω_ext·t) (n=1 mode):

```
e^{−iω_ext·t}·R_{−1}(t) = N·Λ_1(−iω_ext)·∫₀ᵗ e^{−iω_ext·t'}·C_{−1}(t') dt'
```

Measure the stationary correlation C_{−1}(t), multiply by N·Λ_1(−iω_ext), convolve with the drive — that IS the response. Ignoring Λ_1 **substantially overestimates** response amplitude at weak noise (not a small correction!).

## Numerical Verification Protocol

- Testbed: noisy Kuramoto (Γ(θ) = −K·sinθ), Gaussian g(ω), N = 10⁵, Euler–Maruyama, Δt = 0.01, 2×10³ realizations, τ-average over τ∈[0, T−t]
- Critical coupling with noise: K_c(D) = 2√2/π · e^{−D²/2}/erfc(D/√2); recovers K_c(0) = 2√2/π ≈ 1.596
- Quality metric: normalized residual Δ = ∫|R_measured − R_prediction|²dt / ∫|R_measured|²dt; Δ ≤ 0.1 good, Δ ≥ 0.2 poor
- Result: ∆_F (with Λ_1) small across the ENTIRE (D,K) non-synchronized plane; ∆_noF (naive, Λ=1) fails at weak noise — only valid in the strong-noise/weak-coupling corner
- Breakdown occurs only near the critical line K_c(D) where linear response diverges

## Neuroscience Relevance

- Brain-rhythm models (theta/alpha oscillations, resting-state networks) are Kuramoto-type oscillator systems at finite N — applying naive FDT-based reasoning to fMRI/MEG order-parameter fluctuations misses the Λ correction
- Deco et al. (PR E 108, 064410) use FDT violations to classify brain states; this paper gives the exact finite-size correction needed to separate true nonequilibrium signatures from trivial finite-N artifacts in such analyses
- Concrete next steps flagged by the authors: FRR on sparse/modular/long-range connectome topologies (finite spectral dimension), and the synchronized regime

## Usage Patterns

1. **Correct response prediction from correlations**: R_n(s) = −inN·Λ_{−n}(−s)·C_n(s)·H_n(s) — never use the raw correlation without Λ when N is finite and coupling is non-negligible
2. **Estimating effective N**: measure Λ_1(−iω_ext) from data = ratio of true response to I-FRR prediction → diagnostic of how finite the effective oscillator pool is
3. **Stability diagnosis**: compute Λ_n(s) poles directly from g(ω) and Γ_n to get Landau poles → decay modes of order-parameter fluctuations
4. **Experimental design**: probe strength must satisfy 1/√N ≪ |H| ≪ 1; observation window must let C_n(t) decay (T_obs ≈ decay time)

## Pitfalls

- The I-FRR uses C^ini (τ=0 reference); the F-FRR uses the τ-averaged stationary C(t). Mixing them up silently loses the Λ factor — the two curves are clearly distinguishable at low noise D but collapse at high noise.
- The relations hold only in the NONSYNCHRONIZED phase (K < K_c(D)); near criticality linear response diverges and both FRRs break down.
- Z_n correlations are O(1/N) while both FRR sides are O(1) — the relations connect rescaled quantities; don't interpret raw correlation magnitudes without the N prefactor.
- Assumption: initial state independent of the DK noise (f^ini·ζ = 0). For prepared/correlated initial states the I-FRR identity may fail.

## Related Skills
- `kuramoto-brain-network` — Kuramoto phase dynamics on empirical brain networks (this skill adds the finite-N FRR layer)
- `bipartite-oscillator-synchronization` — EI oscillator networks
- `neural-critical-dynamics-theory` — criticality framework for information processing

**Source**: arXiv:2609.28834 — M. Sarkar & Y.Y. Yamaguchi, "Fluctuation–Response Relation in Finite-Size Noisy Coupled Phase Oscillators", cond-mat.stat-mech, 23 Sep 2026.
