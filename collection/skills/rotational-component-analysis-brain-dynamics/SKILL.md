---
name: rotational-component-analysis-brain-dynamics
description: Detect hidden rotational modes in neural dynamics via RCA.
trigger: rotational dynamics, RCA, rotational component analysis, DRCA, double rotation, angular current, asymmetry production rate, mirror symmetry breaking, nonreciprocal dynamics, spontaneous activity, low-variance latent modes, jPCA alternative, probability flux, brain-wide dynamics, early psychosis, dynamical readiness, rotational irreversibility, dimensionality reduction
category: ai_collection
---

# Rotational Component Analysis (RCA/DRCA) — Brain-Wide Rotational Dynamics

Source: arXiv:2610.25061 (Sihan Chen, Yunlong Xu, Doruk Efe Gökmen, Michel Fruchart, Brent Doiron, Vincenzo Vitelli — Leinweber Institute / James Franck Institute / Neurobiology, U Chicago + ESPCI Paris; q-bio.NC, 18 Oct 2026). A dimensionality-reduction method that optimizes **broken mirror symmetry** instead of explained variance, revealing low-variance rotational modes in spontaneous brain activity that constrain cue-evoked behavior and learning.

## Why it matters

- PCA/jPCA miss rotational modes living in LOW-variance planes: the behavior-predictive mouse rotational plane carries only **0.6%** of total variance (PCA plane: 87%). Variance is the wrong objective when the signal is a directed current.
- The phase of the resting-state rotation at random cue onset predicts trial-by-trial lever-pull responses (response probability 20%→70%+ across cue-onset states) — spontaneous dynamics are a **"dynamical readiness" coordinate**, not background noise.
- Rotational irreversibility (APR) separates early psychosis from controls (P=5.22e-07) at exactly zero PCA group difference (P=0.124).

## Core method — RCA

1. **Centered angular current** for plane coordinates x1 = w1·y, x2 = w2·y (orthonormal w1, w2; c = empirical center):
   `j = (x1−c1)·ẋ2 − (x2−c2)·ẋ1` — the planar kinematic analogue of angular momentum; its sign distinguishes clockwise/counterclockwise.
   Discrete one-step estimator (adjacent samples, spacing τ = Δt):
   `J_{Δt,k} = (x1,k−c1)(x2,k+1−x2,k) − (x2,k−c2)(x1,k+1−x1,k)`
2. **APR estimator (asymmetry production rate)** — over one-step segments:
   `σ̂b(τ) = (2·J̄τ)² / (τ·ΔJτ)` where J̄τ, ΔJτ = mean and variance of accumulated current.
   This is EXACTLY the symmetrized-KL APR for Gaussian currents (Jeffreys D[N(J̄,ΔJ) ‖ N(−J̄,ΔJ)] = (2J̄)²/ΔJ; verified numerically) — it balances persistent directed current against rotation-irrelevant fluctuation.
3. **Formal definition**: APR uses a KL divergence between the current distribution p_J(j) and its symmetry-transformed copy p_J(−j). Admissible currents C_M must be additive under concatenation J[Γ1∘Γ2]=J[Γ1]+J[Γ2] and odd under BOTH the spatial transform M and time reversal T: J[MΓ]=−J[Γ], J[TΓ]=−J[Γ]. A positive APR therefore requires simultaneous **spatial-symmetry breaking AND temporal irreversibility**. σ̂b is a current-specific lower bound on σAPR^M = sup over admissible currents; the mean/variance form parallels thermodynamic uncertainty relations, with a nonlinear lower bound B(u), u = ΔJτ/J̄τ², B(u) ≈ 2/u at weak asymmetry (leading order, verified).
4. **Optimization**: gradient descent + automatic differentiation over (w1, w2) maximizing σ̂b. Unsupervised — no trial alignment, no trial averaging, no behavioral labels; works on continuous recordings or pooled individual trials.
5. **Trial-level consistency**: normalized cumulative current `Ji(t) = (1/R²)∫ji(s)ds`; SNR = |⟨Ji(tf)⟩| / SD[Ji(tf)] across trials.

## DRCA — double-rotation modes

A pair of counter-rotating currents around two neighboring centers CAN be mirror-symmetric (reflection exchanges and reverses the pair), but it breaks **half-turn symmetry**: a 180° rotation about c exchanges the cycles while preserving chirality. Under a half-turn the ordinary current j is unchanged, but the position-weighted current `j* = (x1−c1)·j` flips sign (parity verified numerically). Detect double rotations by optimizing `σ̂b_double = (2·J̄τ*)²/(τ·ΔJτ*)` over the accumulated j* — the factor (x1−c1) changes sign across the midline so counter-rotating currents add instead of canceling.

## Key results

- **Reaching benchmark** (single-trial fits, no averaging): macaque RCA SNR 0.89 vs jPCA 0.05; human 1.90 vs 0.98.
- **Mouse BraiDyn-BC** (25 head-fixed GCaMP mice, 44 cortical regions @30 Hz, 15 training days): rest RCA plane = 0.6% variance, 6.3 s period, strong clockwise probability flux; the 87%-variance PCA plane shows only weak circulation.
- **Response model**: P_rsp(xcue) = P0(1−c0‖xcue‖) + g·xcue. RCA response gradient g=0.151 vs PCA 0.050, jPCA 0.078 — extreme upper tail of 2,000 random planes. Cue-onset RCA state beats pupil-arousal on held-out sessions (AUC 0.611 vs 0.535; 35,547 train / 12,272 held-out trials).
- **Mechanism**: post-cue drift decomposes as f_post = f_pre + f_rsp with `f_rsp(x) = f0_rsp(1+c·x·n̂⊥)·n̂∥`; the transverse gradient of f∥post = f_post·n̂∥ is inherited from the rotational flow, and response probability is a sigmoid of f∥post (empirical 20%→70%+). RNNs trained to answer randomly timed cues develop spontaneous rotation and the same state→response geometry with no rotation imposed.
- **Learning** (15 days): f_rsp amplitude grows while f_pre stays fixed; the P_rsp(f∥post) mapping is stable — learning strengthens the cue-evoked drive WITHIN the spontaneous scaffold. A reward-gated associative rule `f0_rsp ← (1−a1)f0_rsp + b1·f_s; k ← (1−a2)k + b2·x_s` (reinforce drifts/locations of rewarded samples) reproduces the learned field from sparse reward alone — no explicit cost function.
- **Human generalization**: HCP-YA fMRI rotational current (0.2% variance, 51 s period); HCP-YA MEG (2.6%, 4.4 s). **HCP-EP early psychosis**: APR markedly reduced (P=5.22e-07) while PCA leading-axis variability is not different (P=0.124); robust in split-sample projection-learning.
- **DRCA**: mouse task flux has two centers — pre-cue period circulates around the lower-right center, post-cue around the upper-left (preparatory vs response dynamics). The pre-cue DRCA state 2.7 s (80 frames) before the cue predicts response (AUC 0.612; RCA cue-onset state 0.638; combined 0.677 — complementary). Human fMRI social task: task and fixation blocks occupy different centers (2.1% variance).
- **Non-neural validation**: recovers rotational coordinates from noise-obscured simulated traveling patterns (coupled complex amplitudes) and from ciliary beating data — a general tool for hidden nonreciprocal dynamics (closest alternative: DyCA).

## Implementation notes

- Use one-step trajectory segments after all temporal binning/downsampling; c is the empirical center; mean/variance over all valid within-trajectory transitions.
- Region loadings visualization: minimum-Frobenius-norm antisymmetric matrix `A = 2·sgn(ω)·(w1w2ᵀ − w2w1ᵀ)/(‖w1‖²+‖w2‖²)` (unit rotation in region space; ω = signed rotation coefficient) — a coupling PATTERN implied by the projection, not anatomical connectivity.
- Interpretation of APR: with complete variables and stochastic-thermodynamic assumptions the path-space divergence would be the entropy production rate (EPR); neural observables are coarse-grained, so APR isolates the asymmetry expressed through the selected current — treat it as a statistical measure of dynamical symmetry breaking.
- Latent rotation ≠ physical rotating waves: RCA operates in a learned latent space (weighted combination of regions/sensors) — no dense spatial sampling, frequency band, or wave template needed. A coherent physical vortex would also appear as a latent loop.

## When to use

- Detecting directed circulation/irreversibility in spontaneous or single-trial neural recordings where PCA/jPCA fail (low-variance rotational modes).
- Linking ongoing brain state to future behavior and learning (dynamical-readiness coordinates; state→response-probability maps).
- Separating task epochs via double-rotation structure (DRCA) — preparatory vs response, task vs fixation.
- Clinical biomarkers of dynamical irreversibility (e.g., early psychosis) invisible to variance-based methods.
- Any high-dimensional trajectory data with hidden nonreciprocal dynamics (biological or physical).
