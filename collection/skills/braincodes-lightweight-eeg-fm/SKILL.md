---
name: braincodes-lightweight-eeg-fm
description: Compact EEG foundation model over discrete neural codes.
trigger: lightweight EEG foundation model, BioCodec RVQ tokenizer, mixed-axis 3D RoPE electrodes, oscillation-injection auxiliary objective, wearable EEG transfer, Muse ear-EEG sparse montage, masked code prediction
version: 1.0
author: neuro-cron 2026-10-23
license: MIT
category: ai_collection
metadata:
  hermes:
    tags: [eeg-foundation-model, vector-quantization, rope, self-supervised, edge-ai]
    related_skills: [eeg-fm-grounding-probes, use-fm-lightweight-semantic-eeg, eeg-fm-audit-systematic-evaluation]
---

# BrainCodes: Lightweight EEG Foundation Model over Discrete Neural Codes

Source: Avramidis, Tashev, Emmanouilidou (arXiv:2610.29320, USC + Microsoft Research, Oct 2026). 1.9M-parameter backbone beats 69M REVE on 14-benchmark mean.

## When to Use
- Building/choosing an EEG foundation model under parameter or device constraints (wearables, ear-EEG, Muse 4-channel headbands)
- Designing pretraining objectives that resist the 1/f-aperiodic power domination of squared-error reconstruction
- Transferring pretrained EEG representations across ARBITRARY electrode montages

## Core Problem Solved
EEG-FMs pretrain on masked reconstruction (waveform or spectral). Under squared error, high-power broadband 1/f content dominates the loss while narrowband oscillations contribute little — the model fits the aperiodic background and drops rhythmic structure. Spatially, neighboring electrodes hold redundant lead-field mixtures, so masked-channel reconstruction is solvable by interpolation without encoding real spatial dynamics. BrainCodes replaces both with (1) CATEGORICAL prediction of discrete code indices (loss weight decoupled from signal power) and (2) an explicit oscillation-injection auxiliary at the bottleneck.

## Architecture

**1. Frozen BioCodec tokenizer** (per channel, independent): RVQ with K=6 stages, shared vocabulary V=256, codebook dim d_c=16, aggregate embedding D=128 by summing dequantized residuals z_{c,t} = Σ_k W_k e_k(q_{c,t,k}). Code-frame rate 21 Hz (30 s window → T=625 frames). Tokenizer pretrained once (arXiv:2510.09095), held frozen — re-tokenize only affected channels when injecting perturbations.

**2. Factorized transformer U-Net** (1.9M trainable): 3 blocks × 3 layers — first two layers do TIME-mixing attention (within channel, RoPE positions), third does CHANNEL-mixing attention (across channels at fixed t). Hourglass: pool time by factors p_i (total ×4) → bottleneck T_b = T/4, symmetric decoder with skip connections + SKIP DROPOUT (prevents decoder from bypassing the bottleneck, forcing the compressed path to retain information).

**3. Mixed-axis 3D RoPE for electrodes** — the montage-transfer key. Resolve each channel label to standard 10-05 coordinate p_c ∈ R³, mean-center, divide by largest centered norm → p̃_c in unit ball (absolute placement removed, relative distances kept). Per head h and rotary pair r: learnable 3D frequency vector ω_{h,r} with log-spaced magnitude base^{−r/R} and random unit direction (both optimized). Rotation angle θ_{h,c,r} = ω_{h,r}ᵀp̃_c; positional attention logit reduces to Δθ_{h,i,j,r} = ω_{h,r}ᵀ(p̃_j − p̃_i) — attention depends ONLY on relative electrode displacement (the quantity volume conduction depends on). During pretraining add Gaussian coordinate jitter capped at half the mean nearest-neighbor spacing.

## Pretraining Objectives

**Primary — masked code prediction (L_tok):** contiguous temporal block mask covering 20–80% of a channel's code frames; per RVQ stage k a linear head predicts discrete index q_{c,t,k}; loss = mean cross-entropy over masked positions averaged over the 6 stages. Categorical CE, not waveform MSE → band contributions decoupled from their residual power.

**Auxiliary — region oscillation injection (L_osc):** inject a Hann-windowed narrowband burst (center f_c, duration δ_c, amplitude a_c) into a contiguous electrode region (seed electrode + ⌈ρC⌉ nearest neighbors), re-tokenize affected channels, then read the TIME-AVERAGED bottleneck b_c with linear heads: regress min-max-normalized frequency (L_f) and duration (L_δ) under squared error; predict per-channel injected-or-not under BCE (L_ℓ). Total: L = λ_tok L_tok + λ_aux(L_f + L_δ + L_ℓ). This supervises frequency, duration, AND spatial extent of oscillatory structure directly at the bottleneck.

**Corpus:** Healthy Brain Network EEG (HBN, releases R3/R4/R7/R8) — 820 h, 1,131 participants, dense 128-channel montage (allows arbitrary channel-subset training). Preprocess: 0.5–75 Hz band-pass, 60 Hz notch, 250 Hz resample, robust z-score per channel, 30 s windows, randomized window length (2–30 s) + channel sets during training, 20% participant-disjoint validation.

## Downstream Readouts
- b_c = time-averaged bottleneck (D dims/channel) — best for SUSTAINED states (seizure, cognitive load; linear probe even beat fine-tuning on Siena due to positive-class scarcity regularization)
- b̄_c = flattened bottleneck (T_b·D dims) — best for TRANSIENT events at specific latencies (motor imagery, TUEV events: 0.563 vs 0.502 on BCI IV-2a)

## Key Results
- **14 benchmarks, best mean** among BIOT/LaBraM/CBraMod/CSBrain/REVE: fine-tune mean nBAC 0.609 (vs REVE 0.581 with 36× more params); linear-probe mean nBAC 0.498; efficiency 0.32 nBAC per M-param vs REVE 0.01.
- **Wearable SOTA** (first systematic consumer-hardware eval of EEG-FMs): ear-EEG sleep EESM23 0.5254 vs 0.4176 (REVE); Muse-Motor 0.5889 vs 0.5083; frozen linear probe on ear-EEG keeps 91% of fine-tune performance.
- **Sparse-montage retention:** farthest-point-sampling montages 32→16→8→4→1 electrodes keep ~91% of full-montage BAC at 4 electrodes (PhysioNet-MI 83%, OpenBMI-ERP 87%, Siena ≥ full).
- **Grounding (companion probe paper):** shortest influence decay length λ=0.73 head-widths (LaBraM 0.90, REVE 0.96, CBraMod 4.05, CSBrain 4.53); only model with positive rhythm-vs-noise-color preference index at ALL SNRs (weakest on white/pink noise color while strongest on δ/μ/β/spindle rhythm ID).

## Ablations (mean BAC across 3 datasets)
| Variant | Mean BAC | Δ |
|---|---|---|
| Official | 0.645 | — |
| − oscillation auxiliary L_osc | 0.574 | −0.071 (largest) |
| random codebook init | 0.592 | −0.053 |
| MLP positional encoding (no RoPE) | 0.613 | −0.032 |
| random-token masking (no blocks) | 0.623 | −0.022 (least stable) |

Backbone pretraining dominates: full 0.498 mean nBAC vs 0.270 (random backbone + BioCodec) vs 0.121 (random quantizer). Pretrained tokenizer adds most on motor imagery (+0.212 BCI IV-2a).

## Implementation Recipe
1. Freeze a pretrained single-channel RVQ tokenizer (BioCodec); never retrain it.
2. Encode each channel independently → tokens + aggregate embeddings.
3. Factorize attention (temporal RoPE / channel 3D-mixed-RoPE); hourglass-pool time ×4 with skip dropout.
4. Pretrain on block-masked code-index CE + oscillation-injection auxiliary heads at the bottleneck; jitter coordinates.
5. Train on randomized channel subsets of a dense-montage corpus for montage-agnostic transfer.
6. Expose both readouts (b_c, b̄_c); pick by task type (sustained vs transient).

## References
- arXiv:2610.29320 (main); BioCodec tokenizer arXiv:2510.09095; NeuroRVQ benchmark arXiv:2510.13068; RoPE (Su et al.); mixed-axis rotary for ViT (Heo et al. ECCV 2024); aperiodic spectral bias (Kommineni et al. arXiv:2605.26434); HBN corpus (Alexander et al. 2017).
- Evaluation probes: see skill [[eeg-fm-grounding-probes]] (companion paper arXiv:2610.29367).