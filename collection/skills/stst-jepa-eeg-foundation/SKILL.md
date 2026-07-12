---
name: stst-jepa-eeg-foundation
description: "STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Predictive Architecture for EEG self-supervised learning. Largest EEG foundation model (47,703 sessions, ages 5-81) using JEPA-style latent prediction with EMA tokenizer + auxiliary signal reconstruction. Rank 1 on NeuralBench for sex, age, psychopathology. Brain age gap correlates with cognitive efficiency. Activation: stst-jepa, eeg foundation model, brain age, self-supervised eeg, eeg self-supervised learning, JEPA eeg, EEG2Rep, brain space, neuralbench, brain age gap, cognitive efficiency"
tags: [eeg, self-supervised-learning, foundation-model, brain-age, transformer, JEPA]
---

# STST-JEPA — Shallow-Target Spatio-Temporal JEPA for EEG

**Paper**: STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning
**arXiv**: 2607.06629v2
**Authors**: Roy Segal, Yoni Svechinsky, Tomer Fekete (brain.space)
**Published**: 2026-07-07 (updated 2026-07-09)
**Categories**: cs.LG, q-bio.NC

## Core Contribution

Largest EEG foundation model pretraining to date: 47,703 sessions spanning ages 5-81 from brain.space and Healthy Brain Network (HBN) corpora. Uses a JEPA-style joint embedding predictive architecture with shallow (tokenizer-level) EMA targets plus auxiliary signal reconstruction, achieving rank-1 on NeuralBench across 3 downstream tasks from a single shared backbone.

## Key Innovations

### 1. Joint Latent-Prediction + Reconstruction Objective
- **Latent prediction** (λ=1.0): Predict masked token representations against EMA-of-tokenizer targets (MSE)
- **Auxiliary reconstruction** (λ=0.35): Smooth-L1 loss reconstructing each masked patch back to raw 16-sample waveform
- Maps loosely to **predictive processing** accounts of cortex (Rao & Ballard 1999; Friston 2010): latent generative model disciplined by signal-level consequences
- Reconstruction deliberately down-weighted — acts as soft floor preventing representation collapse, not co-equal supervision

### 2. PMA (Pooled Multihead Attention) Channel Pooling
- Collapses C=128 channels into single token per temporal index via Set Transformer PMA
- 16 learned inducing queries attend over channel dimension via 16-head cross-attention
- **Coordinate-aware**: each patch embedding combined with learned projection of 3D electrode coordinates
- **Mask-aware**: invalid/missing channels suppressed — handles montage heterogeneity (115-channel brain.space vs 128-channel HBN)
- Gated coordinate learning: gate initialized to zero, trained at 5× LR

### 3. Shallow-Target Architecture
- EMA target stream is **tokenizer-level** (not encoder-level) — unlike canonical JEPA
- Context encoder: 24-layer transformer (d=768, 16 heads, FFN=3072) — no EMA twin
- Predictor: 2-layer transformer with cross-attention, sinusoidal position queries at masked positions
- Closest published analogue: multilayered MAE with EMA-targeted tokens

### 4. Spatiotemporal Block Masking
- 4 rectangular blocks sampled per example
- Each block: random channels [0.2, 0.5] × random time patches [0.1, 0.3]
- Average mask ratio: ~24% of grid positions

### 5. Lightweight Attentive Probe Protocol
- Self-attention (CLS token) + single query cross-attention + linear head
- Single-query design: O(d_p) params vs O(T · d_p) for standard attention
- Length-agnostic — reusable across window lengths

## Architecture

```
Input: 30s × 256Hz × 128 channels = 7,680 samples/channel
  ↓
Tokenization: 1D temporal conv (P=16, stride=16) → 480 temporal patches × 128 channels
  ↓
PMA Channel Pooling: 128 channel patches → 1 token (d=768) per temporal index
  ↓
Token Sequence: T=480 tokens, d=768 (with RoPE positional encoding)
  ↓
[SPATIOTEMPORAL BLOCK MASKING — ~24% masked]
  ↓
Context Encoder (24-layer transformer, visible tokens only)
  ↓
Predictor (2-layer cross-attention, predicts at masked positions)
  ↓
┌─────────────────────┬──────────────────────┐
│  L_lat (MSE)        │  L_rec (Smooth-L1)    │
│  vs EMA tokenizer   │  vs raw 16-sample     │
│  target tokens      │  patch waveform       │
│  λ=1.0              │  λ=0.35               │
└─────────────────────┴──────────────────────┘
```

## Hyperparameters

| Component | Parameter | Value |
|-----------|-----------|-------|
| Input | Window | 30s @ 256Hz (7,680 samples/ch) |
| Input | Channels | 128 (unified budget, mask handles missing) |
| Tokenizer | Patch length | 16 samples (480 patches/ch) |
| PMA | Inducing queries | 16 |
| Encoder | Layers / width / heads | 24 / 768 / 16 |
| Encoder | FFN dim | 3,072 |
| Encoder | Dropout | 0.1 |
| Positional | Encoding | RoPE (base 10,000) |
| Predictor | Layers | 2 (cross-attention) |
| EMA | Momentum | 0.9996 → 0.9999 (warmup 12,000 steps) |
| Masking | Blocks per example | 4 rectangular |
| Loss | λ_lat / λ_rec | 1.0 / 0.35 |
| Optimizer | AdamW peak LR | 5e-5 |
| Optimizer | Weight decay | 0.05 |
| Training | Devices | 7 GPUs (DDP, 16-mixed) |
| Training | Global batch | 245 windows (35/device) |
| Training | Epochs | 15 (~155,500 steps) |

## EEG Preprocessing Pipeline

1. **Upstream conditioning** (done before SSL pipeline):
   - High-pass 1Hz + transient spike interpolation
   - Notch filter at line frequency + harmonics
   - Bad channel removal (spectral quality model or RMS threshold)
   - ASR (κ=20 robust SD threshold)
   - ICA (Picard, extended) — remove ocular + cardiac components, protect alpha
2. **Resample** to 256Hz via polyphase resampling
3. **Window extraction**: 30s with 6s stride (train) / 2s stride (val)
4. **Robust normalization**: channel-wise median/IQR z-scoring
5. **Validity mask**: missing channels + nonfinite stats + amplitude > 150

## Results

### Age Regression (held-out validation, N=3,367 sessions)
| Method | MAE (yr) | RMSE (yr) | R² |
|--------|----------|-----------|-----|
| STST-JEPA + probe (combined) | **3.06** | 5.11 | 0.85 |
| STST-JEPA + probe (brain.space only) | 4.82 | 7.06 | 0.654 |
| Predict training mean (17.7yr) | ~10.09 | 13.27 | ~0 |

### NeuralBench Leaderboard (single shared backbone)
| Task | Metric | Ours (30s) | Prior Best | Rank |
|------|--------|------------|------------|------|
| Sex | bal. acc. | 0.911 | 0.910 (ShallowFBCSPNet) | 1/18 |
| Age | Pearson r | 0.749 | 0.721 (REVE) | 1/17 |
| Psychopathology | Pearson r | 0.215 | 0.137 (CBraMod) | 1/15 |

### Brain Age Gap × Behavioural Capacity
- 7 of 21 targets survive BH-FDR correction (q=0.05)
- All significant targets show **negative** correlation: older-looking brain → worse cognitive efficiency
- Strongest: Stroop efficiency (r=-0.089), n-back (r=-0.057)
- Effects small (|r|<0.10) but directionally consistent

## Loss Dynamics
- L_lat: drops ~4 orders of magnitude (0.0575 → 1.93e-4, 99.7% reduction)
- L_rec: modest decrease (0.317 → 0.169, -47%), acts as soft floor
- Late training plateau: L_lat ∈ [1.5e-2, 2.2e-2], L_rec ∈ [0.13, 0.18]

## Brain-Inspired Framing
Joint objective maps to **predictive processing** theory:
- Latent prediction ≈ cortex's generative model predicting hidden causes
- Reconstruction ≈ sensory prediction error disciplining the model
- Not a claim about cortical fidelity — architectural intuition only

## Limitations & Caveats
- No controlled ablation of joint objective (beyond compute budget)
- No fixed-protocol test on internal brain.space partition
- No clinical biomarker claim
- Pediatric-heavy corpus (HBN) — MAE not directly comparable to adult benchmarks
- 30s windows give advantage over 2s standard NeuralBench protocol
- Mixed resting/task paradigms in pretraining — BAG may carry task state information

## Projected Improvements (from paper)
1. **3× corpus scaling** (~143K sessions): projected MAE 2.6-2.9yr
2. **Auxiliary losses**: age regression head (λ≈0.05), cohort token, contrastive-by-age-band
3. **Fine-tuning**: end-to-end fine-tuning projected 0.2-0.5yr MAE reduction; LoRA adapters (rank 8-16)

## Related Work
- JEPA family: I-JEPA (Assran et al. 2023), V-JEPA (Bardes et al. 2024), data2vec (Baevski et al. 2022)
- EEG foundation models: BENDR, BrainBERT, BIOT, LaBraM, Neuro-GPT, EEG2Rep, REVE
- Self-supervised SSL: BYOL, MAE, VICReg, LeJEPA

## Related Skills
- [[reve-eeg-foundation]] - REVE EEG foundation model
- [[laya-eeg-foundation]] - Laya LeJEPA approach to EEG
- [[eeg-fm-audit-systematic-evaluation]] - EEG foundation model evaluation framework
- [[identity-trap-eeg-foundation-models]] - EEG foundation model identity trap
