---
name: information-enthalpy-potential
description: Information enthalpy theory. Structured-information resource counterweights free-energy minimization, IEP metric quantifies it from spike rasters. Use when analyzing neural complexity drivers, dark-room problem, or quantifying structured information in spike trains.
category: ai_collection
created: 2026-10-09
source_paper: "If the brain were so simple: Information-based drivers of intelligence and their interaction through an n-body-inspired framework (arXiv:2610.11142)"
authors: "Kagan, Zhou, Habibollahi, Baccetti (Cortical Labs, Melbourne)"
---

# Information Enthalpy & the IEP Metric — Structured Information as a Neural Driver

## Core Idea

Free Energy Principle (FEP) explains why systems seek predictable states but NOT why they keep seeking **complex structured input** after prediction error is minimized (the dark-room problem). Kagan et al. (Cortical Labs — the DishBrain team) propose a complementary fundamental driver: **information enthalpy maximization** — neural systems maximize an internal pool of *structured, temporally extended, non-random* information usable for future prediction and self-regulation. Not maximal entropy (noise is useless), not minimal entropy (stasis collapses reorganization opportunity).

## Formal Framework

**Information-storage process**: interaction history `P_{-∞:t} = (O, X, A)` encoded via causal stochastic kernel ε⁽ⁿ⁾ into storage states M_t⁽ⁿ⁾ (an "information pool", not raw history). Storage state entropy bounded by capacity: `H(M_t) ≤ C_st,t`.

**Capacity dynamics** (leaky accumulation with plasticity):
```
C_st,t = (1−α_t)·C_st,t−1 + C_r,t−1          (storage capacity)
C_r,t  = u_t − v_t + (1−δ_decay)·C_r,t−1     (throughput: build − prune + retention)
T_cap,t = 1/α_t                               (retention window; predictive horizon ≤ retrospective window)
```

**Three constraints on admissible processes**:
1. Flow: `R_t ≤ C_r,t` — directed-information rate (innovation information per step, conditioned on prior stored states) bounded by throughput.
2. Storage: `H(M_t) ≤ C_st,t`.
3. Structure availability: `R_st,t ≤ Γ_t·C_r,t` — multiscale structured-information rate bounded by signal-dependent availability Γ_t ∈ [0,1].

**Scale-resolved rate**: `R_st,t = Σ_j w(τ_j)·R_t^{(n,τ_j)}` over downsampled macro-grids τ_j — structure lives at multiple concurrent scales.

**Predictive content**: kernel-weighted conditional mutual information across horizons `P(M_t) = Σ_i w(H_i)·I(M_t; F_{t+1:t+H_i} | A)`, H_N ≤ T_cap.

**Predictive-resource hypersurface**: `Φ_π(t; C_r, C_st, Γ) = sup_{admissible} P(M_t)` — non-decreasing, concave in C_r (diminishing returns).

**Information enthalpy**: `H_I = κ·Φ_π` where κ = Landauer bound `k_B·T·ln2` (theoretical) or empirical κ_bio. Realized resource `h_I(M_t) = κ·P(M_t) ≤ H_I`.

**Biological energy budget**: `E_req = E_neural + E_plastic + E_act + E_homeo ≤ E_sup` — acquisition/maintenance of enthalpy costs metabolic energy; homeostatic penalty Ψ(h_t) for exceeding tolerance.

## The IEP Metric (implementable)

Composite score quantifying structured-information potential of an input signal (channel×time binary raster):

```
IEP(X; Θ) = (1−β)·R⁽ᵅ⁾(S̃) + β·C_MS(S̃)  ∈ [0,1]
```

**Pipeline**: raster X → overlapping patches (C_p×T_p, strides s_c≠C_p, s_t≠T_p) → occupancy-threshold pooling (p_c×p_t blocks, threshold θ) → flatten to atomic symbols → symbol sequence S → PSC-weighted replication (Permutation Statistical Complexity weights w_k, replication κ_k = 1+⌊λw_k⌋) → S̃.

**Component 1 — entropy-weighted redundancy** (shuffled-LZC):
```
R(S̃) = (c_shuf − c(S̃)) / c_shuf          (LZC phrase count vs M-shuffle surrogate)
R⁽ᵅ⁾(S̃) = R(S̃)·H_sym(S̃)^α              (H_sym = normalized token entropy; α penalizes trivial runs)
```
R≈1 → high temporal structure; entropy weight prevents rewarding degenerate repeats.

**Component 2 — multiscale statistical complexity**:
```
R_B(S̃) = 1 − c(S̃)/c(S̃_B_i)              (block-permutation surrogate at block size B_i, order preserved within blocks)
C_MS(S̃) = ∫ R_B dx / (R_1·(x_max−x_min)), x = log₂B   (normalized AUC over log-scale grid, trapezoidal)
```
Large B preserves local structure but scrambles long-range order; small B the reverse — AUC across scales measures structure persistence.

**Hyperparameters Θ**: patch sizes, strides, pool sizes, θ, α, β, block set B, surrogates M, PSC (D, τ, w, λ, ν). All effects mediated through S̃.

## Validation

- **Fractal spike rasters** (Mandelbrot/Julia/Dragon): originals score above all 3 surrogates (permute-time / Bernoulli-global / permute-all) — IEP detects intrinsic multi-scale structure, not firing-rate marginals.
- **Spiking Speech Commands** (700-ch artificial-cochlea rasters): speech structure (onset bursts, spectral concentration, temporal envelopes) yields separable IEP vs randomized controls.

## The n-Body State-Space Landscape

Brain = n-body-inspired interacting drivers moving a neural system through high-dim state-space: (1) FEP/free-energy minimization (ergodic, state-sustaining), (2) information enthalpy maximization (non-ergodic, adaptation-driving), (3) criticality maintenance. Landscape states: subcriticality (deterministic entropy + depleted enthalpy → quiescent), supercriticality (random entropy + redundant enthalpy → runaway), hypersynchrony (deterministic entropy + redundant enthalpy), decoupled noise (random entropy + depleted enthalpy), and the unstable central near-critical regime. High-IEP input pushes systems toward criticality; embodied BNNs show criticality markers only with structured environmental input.

## Falsifiable Predictions

1. Neural systems should preferentially seek high-IEP over both noise and stasis (direct solution to dark-room problem without complex priors).
2. Criticality maintenance requires structured input supply — an *embodied* relation, not just internal attractor.
3. IEP should predict learning/engagement in BNN closed-loop experiments better than entropy alone.
4. n-body formulation: driver interactions across timescales, no strict hierarchy (single neurons can predict behavior).

## Use When

- Designing closed-loop stimulation/feedback for BNNs or BCI — pick high-IEP stimulus structure.
- Quantifying "interestingness" of neural signals beyond entropy (LZC alone rewards noise).
- Theorizing neural criticality as embodied information-structural relation.
- Building curiosity/intrinsic-motivation signals for agents: IEP is a computable intrinsic reward candidate for structured-environment seeking.
- Critiquing/extends FEP: ergodicity-breaking driver accounts for learning-memory transitions.
