---
name: use-fm-lightweight-semantic-eeg
description: 1.46M-param EEG foundation model with frozen-encoder cross-disorder transfer.
category: ai_collection
trigger: EEG foundation model, lightweight EEG encoder, frozen-encoder transfer, cross-disorder EEG, TUAB TUEP classification, semantic EEG representations, self-supervised EEG pretraining
---

# USE-FM: Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer

Methodology from arXiv:2610.05503 (Peng & Bui, UIUC, 2026-10-04, cs.LG/q-bio.NC): a **1.46M-parameter
CNN–Transformer autoencoder** pretrained self-supervised on TUEG (~18,800 h, 2.26M 30-s segments)
transfers competitively to clinically distinct EEG tasks with the encoder **fully frozen** —
challenging the "ever-larger EEG foundation model" trend (Neuro-GPT 79.53M, Brant 500M,
LaBraM up to 369M).

## Core Claim

Effective cross-disorder EEG representation transfer does **not** require large architectures:
large-scale self-supervised reconstruction pretraining lets a compact encoder (~1/5 of baseline size)
learn semantic representations that transfer frozen across abnormal-EEG detection (TUAB) and
epileptic seizure recognition (TUEP).

## Architecture & Pretraining

- **Encoder**: 1D-CNN (19→64→128 channels, local temporal features) + LayerNorm + linear projection
  + Transformer encoder → latent z ∈ R^128
- **Decoder** (pretraining only, discarded after): Transformer decoder + CNN decoder reconstructs
  the multichannel signal
- **Loss**: MSE reconstruction, L = (1/CT)·‖x − x̂‖² — decoder sees ONLY the latent, forcing the
  encoder to preserve essential temporal+spatial information in 128 dims
- **Data pipeline**: 0.3–75 Hz band-pass, 60 Hz notch, standard 19-channel 10-20 montage,
  200 Hz resample, 30-s non-overlapping windows, amplitude normalized to ±100 µV
- **Pretraining**: TUEG 2,259,998 segments, Adam lr=1e-4, batch 64, early stopping (patience 5),
  ~100 h on 4×A100 (DDP), up to 100 epochs
- **Downstream**: encoder FROZEN; only an MLP classifier g_φ(f_θ*(x)) is trained per task

## Frozen-Encoder Results (mean ± std over runs)

| Task | Metric | USE-FM (1.46M) | LUNA-Base (7.10M) | CBraMod (5.15M) |
|---|---|---|---|---|
| TUAB (abnormal) | AUC | **85.24 ± 5.61** | 84.13 ± 3.75 | 84.09 ± 5.39 |
| | ACC | **80.25 ± 5.91** | 80.22 ± 4.21 | 80.23 ± 6.14 |
| | SEN | 81.13 ± 11.76 | **82.25 ± 12.49** | 80.99 ± 14.76 |
| | F1 | 82.52 ± 5.79 | **82.53 ± 5.00** | 82.04 ± 7.12 |
| TUEP (epilepsy) | AUC | 67.35 ± 5.91 | 67.00 ± 4.45 | **68.20 ± 8.60** |
| | ACC | 69.00 ± 3.24 | 67.50 ± 2.74 | **70.50 ± 6.78** |
| | SEN | **75.00 ± 14.14** | 62.00 ± 7.48 | 61.00 ± 13.93 |
| | F1 | **70.37 ± 4.01** | 65.46 ± 2.89 | 66.86 ± 8.23 |

**Honest reading**: on TUAB the three models are statistically indistinguishable; on TUEP, USE-FM
wins sensitivity (+13 pts) and F1 (+3.5–4.9 pts) but loses AUC/ACC to CBraMod by ~1 pt. The
clinically relevant claim is the sensitivity/F1 balance for screening (fewer missed seizures), at
~20–25% of the parameter count.

## Latent Semantic Analysis

- k-means on TUEP embeddings, k swept 3–20: **all three models show the same WCSS elbow at k=4**
  → a consistent intrinsic clustering structure emerges regardless of encoder size
- PCA + t-SNE colored by k=4 clusters: USE-FM latent space is organized comparably to the
  5–7M baselines — compactness/separability does not require scale

## Implementation Recipe (reproducible protocol)

1. Preprocess TUEG: montage → 19 ch, 200 Hz, band-pass 0.3–75 Hz, notch 60 Hz, ±100 µV, 30-s windows
2. Train CNN–Transformer autoencoder with MSE reconstruction until early stopping
3. Discard decoder; freeze encoder weights
4. Per downstream task: extract latents, train only a small MLP classifier
5. Evaluate AUC/ACC/SEN/F1 with mean±std across independent runs
6. Characterize latents: WCSS elbow sweep → k-means → PCA/t-SNE visualization

## When to Use

- Resource-constrained clinical EEG deployment (edge/low-memory) where 100M+ models are impractical
- Cross-disorder transfer studies needing a fair frozen-encoder comparison protocol
- Building a compact universal EEG representation for screening tasks where sensitivity matters most
- Baseline design: benchmark new EEG foundation models against 1.46M USE-FM before scaling

## Limitations

- Conference paper (IEEE SPMB 2025, 6 pages): limited ablations; architecture adapted from a prior
  semantic EEG framework rather than novel
- TUEP variance is large (SEN ±14.14) — small-dataset sensitivity; results should be read as
  "competitive," not dominant
- Only two downstream disorders; cross-disorder generality beyond TUAB/TUEP untested
