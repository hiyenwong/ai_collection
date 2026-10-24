---
name: neuromotor-hierarchy-network-semg
description: Use when decoding sEMG across users/sessions. Physiology-guided hierarchy builds a compact latent neuromotor state.
category: ai_collection
trigger: sEMG decoding, hand pose estimation, emg2pose, emg2qwerty, motor primitives, muscle synergy, cross-user generalization, Henneman size principle, neuromotor latent state
---

# Neuromotor Hierarchy Network (NHN): Physiology-Guided sEMG Decoding

**Source**: Neuromotor Hierarchy Network: Physiological Inductive Biases for Robust Generalization in sEMG Decoding — Wang, Qi, Zhang, Luo, He, Motani, Wu (NUS), arXiv:2610.07713 (Oct 2026, cs.LG)

## Core Idea

sEMG↔kinematics relationships vary across users/sessions because tissue filtering, electrode placement, and volume conduction corrupt the waveform AFTER the neuromotor signal is generated. Instead of learning a direct waveform→output mapping (which entangles recording variability with true coordination), NHN infers a **compact latent neuromotor state** (N=32 primitives) that represents task-relevant neuromuscular coordination, with recording effects factored out by design. Physiology guides the *structure*; task supervision shapes the *content*.

## Architecture Pipeline (all causal, wearable-safe)

`x ∈ R^{C×T0}` (16 wrist channels @2kHz) → A (measurement adapter) → E (spatiotemporal encoder) → B (state construction) → H_κ (task head)

**1. Measurement adaptation with intensity preservation (A)**
- Intensity path: per-channel log-std over causal window, centered against cumulative mean → q (relative intensity retained for task fusion).
- Partial whitening: W(x) = [(1−α)Diag(Σ_b) + αΣ_b + λ_b·I]^(−1/2)(x−µ_b) per block b, α∈[0,1] interpolates channel-wise normalization ↔ joint whitening WITHOUT PCA rotation (no sensor-layout destruction). λ_b from mean channel variance.
- Waveform path: learned residual blend x̃ = (1−η_w)x + η_d·s₀·(D(x)−x) + η_w·s₀·(W(x)−x) — once-calibrated fixed scale s₀ keeps both candidates on input amplitude scale.

**2. Spatiotemporal encoder (E) — time-depth separable (TDS) blocks**
- Temporal conv + local-global mixing: local = shared width-k circular convs over G feature groups on a ring (parameter-efficient channel interaction); global = low-rank bottleneck W_down→GELU→W_up with learned gate γ_r (distant muscle-group coordination).
- **Multi-timescale adaptive gain**: M context states per feature, each accumulating input with a different learned timescale τ_m via s_t^(m) = (1−e^(−Δt/τ_m))u_t + e^(−Δt/τ_m)s_(t−1)^(m) (common-drive motivation); concatenated states → learned map g_a → residual gain: f_t = u_t ⊙ (1 + tanh(g_a([s_t^(1);...;s_t^(M)]))). Gain reweights encoder features; NOT the same as integration below.

**3. Latent state construction (B) — three physiological stages**
- **Non-negative candidate drives**: d_t = Softplus(LN(g_d(f_t))) ∈ R^N_≥0 — non-negativity prevents cancellation during integration (low-dim coordination = muscle synergy prior).
- **Temporal integration**: causal FIR paths with per-primitive non-negative geometric kernels (heterogeneous motor-unit contraction times): d̄_t = ω₀⊙d_t + Σ_m ω_m⊙(k_m *_c d)_t, ω softmax-normalized per primitive. Synaptic-integration analogue.
- **Henneman-inspired graded allocation**: p_t = N·d̄_t ⊙ softmax((d̄_t + β)/θ_t), with learned recruitment priorities β ∈ R^N (size principle) and drive-dependent temperature θ_t = max(1e−4, mean TopK(d̄_t)). Softmax weights all primitives; multiplication by d̄_t preserves continuous magnitudes.

**4. Task heads**: autoregressive LSTM (pose, 50Hz rollout) or TDS+CTC head on concatenated two-wrist state sequences (typing, 100Hz state).

## Results

| Task | Result |
|---|---|
| emg2pose (Regression+Tracking, 3 splits) | AE −0.52% to −2.84% vs Hadidi et al. best variants, **48.4% fewer params**, 35.6% less compute; gains largest on unseen Stage splits |
| emg2qwerty (typing) | beam CER −19.4% zero-shot, −30.4% fine-tuned vs SplashNet-Upscale, **65.9% fewer params**, 75% less compute |
| Params | 0.88M (typing) vs SplashNet-Upscale 5.06M |

## What the Latent State Learns (mechanistic findings)

- **Pose**: primitives have distributed, overlapping joint-angle associations (multi-primitive composites represent posture; not one primitive per finger). Training LENGTHENS adaptive-gain timescales but SHORTENS integration lags → long context for feature reweighting, recent drives for state construction.
- **Typing**: same-key primitive-activation patterns have higher cross-window cosine similarity than different keys → keystrokes reuse primitive combinations. Training SHORTENS S/L gain timescales, LENGTHENS M — task-dependent temporal preferences within one architecture.
- **Allocation ablation**: uniform allocation (equal weights) raises pose AE +3.94° and typing CER +42.12 pts at unchanged total activation → decoding uses the RELATIVE distribution across primitives, not overall strength. Top-12 of 32 primitives ≈ 49% of allocation weight.

## Reusable Patterns

1. **Factor measurement from message**: partial whitening (interpolated diagonal↔full covariance, no rotation) + preserved relative-intensity side path — reusable for ANY cross-session biosignal (EEG, fNIRS, cardiac).
2. **Non-negativity before temporal integration** — prevents drive cancellation; applies to any primitive/synergy bottleneck.
3. **Henneman allocation (softmax((d+β)/θ) ⊙ d)** — continuous, order-sensitive soft recruitment; drop-in replacement for uniform primitive weighting; the temperature calibrates to current drive level via TopK mean.
4. **Two-timescale separation**: multi-timescale exponential context for *feature gain* vs geometric-kernel FIR for *drive integration* — train them separately, read learned timescales as diagnostics.
5. Allocation-spread + Neff (effective primitives) as interpretability readout for any latent-factor model.

## Limitations (stated)

Primitives are task representations, NOT genuine physiological sources. Wrist sEMG only; device deployment and other sensor layouts untested. Longer tracking horizons degrade (though still below vemg2pose).

## Connections

- SplashNet / emg2pose / emg2qwerty line (Hadidi, Salter, Sivakumar, Kaifosh).
- Muscle-synergy low-rank control (d'Avella, Bizzi); common drive (Negro); size principle (Henneman, Milner-Brown).
- Same "physiological inductive bias + task supervision" philosophy as [[connectome-informed-flyvision-general-vision]] (fruit fly) and [[physiologically-constrained-musculoskeletal-neural-network]] (sEMG→joint kinematics).
