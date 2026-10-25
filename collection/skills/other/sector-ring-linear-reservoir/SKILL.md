---
name: sector-ring-linear-reservoir
description: "Use when tuning reservoir time-scales or ESN search cost."
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-25
license: MIT
metadata:
  hermes:
    tags: [reservoir-computing, echo-state-network, eigenvalue-design, hyperparameter-search, associative-scan, linear-reservoir]
    related_skills: [esn-empirical-boundaries-fewshot-patterns, linear-reservoir-computing-bottleneck, closed-loop-forecasting-ssm-snn]
  arxiv_id: "2610.25806"
  paper_title: "Sector-Ring Linear Reservoirs: Sector-Wise Decay-Timescale Allocation With State Reuse Across Candidate Settings"
  paper_authors: "Yudai Ebato, Sou Nobukawa, Yusuke Sakemi, Takashi Kanamaru, Nina Sviridova, Kazuyuki Aihara"
  published: "2026-10-19"
---

# Sector-Ring Linear Reservoir (SRLR)

Make the **eigenvalue distribution of a linear reservoir a design variable** with only K+2 search coordinates, and cut hyperparameter-search cost by ~99.8% with a **state bank** that precomputes per-timescale states once and assembles every candidate from them. From arXiv 2610.25806 (Ebato, Nobukawa, Sakemi, Kanamaru, Sviridova, Aihara — Chiba Inst. Tech / U. Tokyo IRCN; IEEE submission).

## When to Use

Use when: designing or tuning reservoir/ESN eigenvalue spectra, spectral radius, or decay timescales; hyperparameter search over reservoir settings is the cost bottleneck (state collection dominates); the input is colored (non-flat spectrum) and per-mode state scales must be equalized across candidates; you want interpretable timescale allocation (WHICH frequency bands need long vs short memory); building linear/diagonalizable recurrence + nonlinear readout architectures (complex-diagonal ESN, LRU family, next-generation RC).

## Problem

Reservoir performance depends on whether fixed dynamics suit the task: memory length and frequency response are task-dependent. Searching candidate settings is expensive because each candidate requires driving the reservoir over the input and collecting states. A full per-mode parameterization (M independent timescales) is both hard to search and uninterpretable; a single global timescale (SCR/linear ring, LRU-γ) leaves the allocation problem untouched.

## Core Method

### 1. Rotation–decay block form (eigenvalues as explicit parameters)

Real recurrence W_rec is block-diagonal 2x2: block j holds state x_j,t ∈ R² updated by

    x_j,t = R_j x_j,t-1 + w_j u_t,   R_j = r_j R(θ_j)

so each block realizes one complex-conjugate pair λ_j = r_j e^{±iθ_j}. N = 2M modes.

### 2. Sector-ring parameterization (K+2 coordinates)

- Angles FIXED at midpoints: θ_j = (j − 1/2)π/M, j = 1..M (evenly spaced in (0,π)). Midpoints avoid θ = 0, π where R(θ) = ±I gives a degenerate repeated real eigenvalue (both coordinates carry the same response up to scale).
- (0,π) split into K equal consecutive sectors; sector of block j: s(j) = floor(Kθ_j/π). With M a multiple of K each sector holds M/K modes.
- ONE half-life η_k per sector: radius r_j = 2^(−1/η_s(j)), i.e. amplitude halves every η updates (time constant τ_k = η_k/ln 2). The half-life PROFILE η = (η_0..η_K−1) is the decay-timescale design variable. All r_j < 1 ⇒ echo state property for any η > 0.
- K = 1 collapses to the common-radius reference (all modes share one timescale = linear Simple Cycle Reservoir).
- Paper setting: N=64, M=32, K=8 (4 modes/sector), η_k ∈ {0.25, 0.5, 1, 2, 4, 8} — the FINITE half-life set is what enables the state bank.
- Remaining coordinates: target state scale σ* and ridge β. Search space is (σ*, η, β).

### 3. PSD-scaled input weights (equalize mode state scale under colored input)

Mode j responds most strongly to input frequencies near θ_j, so state variance depends on the eigenvalue setting. White-noise normalizations (LRU-γ, complex-diagonal ESN per-mode scaling) mis-equalize scale when the input spectrum is non-flat. Fix analytically:

    w_j = g_j q(φ_j),  q(φ) = [cos φ, sin φ]^T

- Direction φ_j: chosen so the two state coordinates have EQUAL predicted variance (from the one-sided Welch PSD of the training input weighted by block-j's frequency response).
- Gain g_j = σ* / sqrt(κ_j), κ_j = predicted per-coordinate variance at unit gain = integral of the one-sided PSD weighted by the block frequency response over [0, f_s/2].

Measured effect: median P90/P10 ratio of mode-coordinate scales = 1.00 (PSD-scaled) vs 9.86–34.0 (γ-normalized / uniform random). Scale confound is removed, so timescale-profile comparisons are clean.

### 4. Fixed nonlinear feature map (mixing outside the linear recurrence)

    χ_t = [tanh(Q^T h_t)^T, 1]^T,  Q^T Q = I (Haar orthogonal, QR of a Gaussian matrix with fixed column signs, per model seed)

Block-diagonal recurrence has no cross-mode interaction; the fixed orthogonal Q supplies dense mixing and tanh supplies nonlinearity, applied ONCE outside the recurrence. Linear reservoir + expressive nonlinear readout is a universal-approximation class (next-generation RC / linear reservoir networks / complex-diagonal ESN lineage). Readout: ridge regression W_out = (Φ^T Φ + βI)^{-1} Φ^T Y, closed form.

### 5. State bank — the cost trick (99.8% fewer mode trajectories)

Candidate = (σ*, η, β). Because (a) each η_k comes from a finite set of L ≤ 6 values and (b) the recurrence is LINEAR:

1. For each distinct half-life ℓ in η: if bank B has no entry, set ALL sectors to ℓ, σ* = 1, compute states of all M modes over warmup+train+val ONCE, store under ℓ.
2. Assemble any candidate: for each sector k, copy the mode-state columns from B[η_k]; scale the whole state matrix by σ* (linearity ⇒ states scale linearly with σ*).
3. Apply feature map tanh(H Q), fit ridge at β, score. β only changes the ridge solve.

Mode trajectories computed drop from C·M (per-candidate recompute) to L·M with L ≤ 6 however large C is. Paper: 245,760 evaluations per configuration — SRLR wall time 3.29 h vs ESN 10.93 h, LI-ESN 9.96 h (common-radius reference 2.30 h but uniformly worse accuracy). Bank is complete by ~evaluation 3.

### 6. Associative-scan state generation (parallel-in-time)

Per half-life, the mode recurrence is the element-wise complex map ζ_t = a ⊙ ζ_{t−1} + b_t with a = (λ_1..λ_M) fixed. Affine maps compose associatively:

    (a2, b2) ∘ (a1, b1) = (a2 ⊙ a1, a2 ⊙ b1 + b2)

so an associative scan reproduces the serial recurrence in O(log T) sequential stages of O(TN) element-wise ops. Diagonal form makes matrix products element-wise, which is what makes composition cheap.

## Key Results (Lorenz/Rössler, x→x prediction and x→z reconstruction, horizons 0/1/12, 10 seeds, TPE/Optuna searches, NRMSE)

- Sector-wise allocation beats the common-radius reference in ALL 8 cases: mean NRMSE reduced 11.6–47.4%. The degree of freedom is real.
- vs nonlinear ESN / LI-ESN: SRLR lowest mean in 5/8 (all 4 x→x prediction cases + Rössler x→z at horizon 12); LI-ESN wins the 3 remaining reconstruction cases; ESN none. Linear recurrence + fixed nonlinearity is competitive.
- Selected half-life profiles CHANGE with prediction target and horizon (same input sequence) — direct evidence that suitable reservoir dynamics are task-dependent; profiles also varied across seeds (contributions of Q vs finite-search budget NOT separated — honest open point).

## Implementation Recipe

1. Choose M, K (M multiple of K; e.g. 32/8). Fix angles at midpoints; assign sectors by floor.
2. Restrict η_k to a small finite log-spaced set (e.g. {0.25,0.5,1,2,4,8}) — the discretization is what buys the state bank.
3. Compute one-sided Welch PSD of standardized training input; per block derive κ_j and direction φ_j; set w_j = (σ*/√κ_j) q(φ_j).
4. Build bank: for each ℓ in the allowed set (lazily, on first request), run the associative scan at σ*=1, store train/val state matrices under ℓ.
5. Search (σ*, η, β) with TPE; each evaluation = assemble from bank, tanh(HQ), ridge solve, validation NRMSE.
6. Read the selected η profile as the diagnosis: which angular sectors (frequency bands) the task wants long/short memory over.

## Generalizable Patterns

- **Discretize-then-bank**: factorize the model so per-value expensive artifacts are precomputed once per discrete hyperparameter value and assembled per candidate. Applies to any linear or diagonalizable-model search, not just reservoirs.
- **PSD input scaling**: replace white-noise per-mode normalization with training-input-PSD-weighted scaling whenever modes are frequency-selective and the input is colored.
- **K-parameter interpolation**: sector-wise allocation sits between 1 global timescale and M per-mode timescales — few enough coordinates to search, enough resolution to adapt to band structure, and interpretable as a spectrum-shaped memory profile.
- **Controlled comparisons**: the common-radius reference isolates exactly the new degree of freedom; PSD scaling isolates the scale confound. Each ablation changes one axis.

## Honest Limitations (from the paper)
- Input-weight design ordering is TASK-DEPENDENT: PSD-scaled design was the WORST in x→z reconstruction at horizon 0 for both systems (~26–28% above the best of the three designs), and best in 4/8 cases overall.
- The block-diagonal recurrence is NORMAL (commutes with its transpose): no transient amplification through non-orthogonal modes — non-normal ESN recurrences are not covered; extending sector allocation to non-normal recurrences is open.
- Evidence base: 2 chaotic systems x 4 tasks, one protocol, K = 8 fixed, N = 64. Selected profiles vary across seeds; contributors (mixing matrix Q vs finite search budget) not separated.
- State bank requires finite discrete timescale sets and linearity (σ* scaling); continuous-radius models (the common-radius reference) cannot use it.

## Related Skills

- [[esn-empirical-boundaries-fewshot-patterns]] — ESN benchmarking discipline
- [[linear-reservoir-computing-bottleneck]] — capacity analysis of linear reservoirs
- [[closed-loop-forecasting-ssm-snn]] — closed-loop forecasting pitfalls (SRLR evaluated open-loop only)
- [[hyperreservoir-context-dependent-readout]] — context-modulated reservoir readouts
- [[esn-online-training-percolation-reservoir]] — reservoir density near percolation threshold
