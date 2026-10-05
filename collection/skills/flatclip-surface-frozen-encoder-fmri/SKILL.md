---
name: flatclip-surface-frozen-encoder-fmri
description: Cortical flatmaps + frozen SigLIP2 for fMRI prediction.
category: ai_collection
---

# FlatClip: Geometry-Aware Surface-Level Baseline for fMRI Representation Learning

**Source**: arXiv:2609.31204 (NeurIPS 2026), Wang, Ye, Ning, Zuo, Xia, Wen, Liu (SUSTech / Warwick)
**Code**: https://github.com/OneMore1/FlatClip

## Core Idea

fMRI representation scale ladder: ROI-level (coarse, efficient) ← **surface-level flatmap (this)** → voxel-level (fine, costly). FlatClip renders cortical activity as geometry-aware 2D flatmap image sequences and encodes them with a **frozen SigLIP2** image encoder — zero fMRI-specific pretraining — then trains only a lightweight MLP probe. Result: a competitive middle-ground representation that beats most ROI-level baselines (HCP 82.06% sex classif.) while remaining below the strongest voxel models (Omni-fMRI 92.86%).

## Pipeline (3 stages)

1. **Flatmap adapter**: preprocessed volumetric fMRI → cortical vertices (fsLR 32k) → Pycortex rasterizes onto a *deterministic* flatmap layout → normalize + colormap + mask (cortex or task region) → crop → composite to RGB frames `x_{i,t} ∈ R^{H×W×3}`. Stack T frames: `X_i ∈ R^{T×H×W×3}`.
   - Resting-state: t indexes time points (T=40 frames).
   - Visual NSD: each sample = stimulus-level **GLM response map** (one per viewed image).
2. **Frozen feature extraction**: `z_{i,t} = f_θ^global(x_{i,t}) ∈ R^768` (SigLIP2 frozen, no gradients).
   - Resting-state pooling: temporal mean `h_i = (1/T)Σ_t z_{i,t}` (T=40, d=768).
   - NSD pooling: valid **patch features** (NaFlex, ≤1024 patches) → AdaptiveAvgPool to 16×16=256 tokens → token mean.
3. **Lightweight probe**: MLP 768→256→256→C (BatchNorm, GELU, dropout 0.2), class-weighted CE (resting) or class-weighted BCE multilabel (NSD COCO80, C=80). Only probe trained. Seeds 42/43/44, checkpoint by val weighted F1.

## Key Results

| Benchmark | FlatClip | Best ROI-level | Best voxel-level |
|---|---|---|---|
| HCP sex (ACC) | 82.06±2.05 | 68.24 (BrainMASS) | 92.86 (Omni-fMRI) |
| ADNI MCI/CN | 61.11 | 58.33 (Brain Harmony) | 69.78 (SwiFT) |
| ADNI AD/CN | 75.46 | 70.90 (Brain Harmony) | 84.26 (Omni-fMRI) |
| PPMI PD | 54.86 | 62.50 (Brain-LM) | 68.13 (Omni-fMRI) |

- NSD COCO80: FlatClip beats general-purpose fMRI foundation models (Omni-fMRI, NeuroSTORM, SwiFT) on visual recognition; performance improves monotonically whole-cortex < HCP-MMP visual cortex < NSD task-active region (NSDgeneral) → **task-relevant cortical coverage matters**.
- PPMI weakness is principled: PD is subcortical/brainstem — cortical flatmaps structurally omit the relevant signal.

## Geometry-Disruption Controls (the reusable methodology)

Matched-probe protocol (fixed MLP arch/training, fresh probe per condition), frozen encoder:

| Control input | HCP ACC |
|---|---|
| Real flatmap | 82.06 |
| Spatial block-shuffle | 76.14* |
| L-R hemisphere swap | 74.96* |
| Within-hemisphere shuffle | 70.90* |
| Cortical-pixel permutation | 72.93* |
| Random-init encoder | 70.56* |
| Phase-randomized + histogram-matched | 64.64* |
| FC heatmap | 57.87* |
| Random image | 48.90* |

(*Holm-corrected p<0.05 vs real.) Anatomy-linked arrangement beats permutation under **all 3 colormaps** (Inferno +7.26, Grayscale +8.24, RdBu_r +8.74 wF1). Two separable factors confirmed: (a) spatially organized input, (b) pretrained (not random) visual features.

## Reusable Design Patterns

1. **Frozen-image-encoder-as-probe-baseline**: before building a domain-specific foundation model, test how far a *frozen* general vision encoder (SigLIP2/DINOv2/MAE/CLIP) gets on rendered domain data. Separates "what pretraining buys" from "what task data buys".
2. **Geometry-aware rendering as domain adapter**: project inherently-3D scientific data onto a fixed 2D anatomical layout (Pycortex flatmap) instead of training 3D/4D architectures. The layout IS the inductive bias.
3. **Perturbation-control ladder** for claiming "spatial structure matters": block-shuffle → hemisphere-swap → pixel-permutation → phase-randomized (Fourier surrogate) → histogram-matched → random-image → random-init-encoder. Each rung isolates a distinct hypothesis.
4. **Task-relevant input support selection**: same-mask comparisons (whole cortex vs task-active cortex) show gains from *selecting geometry relevant to the target*, not just preserving geometry.
5. **Feature caching economy**: features extracted once; region choice / probe capacity / covariate adjustment evaluated without touching the encoder.
6. **Covariate adjustment protocol**: fit covariate models (age, motion, site) on training subjects, apply unchanged to val/test before probe training — HCP wF1 80.88 (age-adj) vs 82.04 raw.

## Practical Recipe

```python
# Pseudocode skeleton
for subj in subjects:
    frames = [pycortex_render(vertex_data[subj, t], cmap='inferno', mask=cortex_mask) for t in range(40)]
    feats  = [siglip2_global(frame) for frame in frames]     # frozen
    h      = mean(feats)                                      # 768-d subject feature
probe = MLP(768, 256, 256, n_classes)                          # only this trains
# NSD variant: GLM beta map → flatmap → patch features → AdaptiveAvgPool(16×16) → token mean
```

- Normalization: **global z-score** (frame z-score similar; voxel z-score hurts HCP −7.6).
- Backbone: SigLIP2 > DINOv2 > ViT-B on this protocol.
- More feature granularity helps some tasks (40 patch-mean 84.94 vs one-global 82.06 on HCP) — but one compact global token is the headline setting.

## Limitations (honest accounting)

- Flatmaps introduce cuts + metric distortion; omit subcortical/brainstem (hence PPMI failure mode).
- Temporal mean pooling discards frame order — no dynamics.
- Direct-volume slice encoding (encode each non-empty slice, average over slices+time) reaches 89.32 wF1 on HCP — *more images beat better rendering*; flatmap wins on image-count economy, not raw ceiling.
- Below strongest voxel-level models overall (Omni-fMRI 92.86 vs 82.06 on HCP).

## Related Skills

- `flexibrain-resolution-agnostic-fmri-encoding` — voxel-level resolution-agnostic counterpart
- `brain-dit-fmri-foundation-model` — fMRI-specific pretraining branch
- `infant-fmri-deep-learning-review` — representation-first design philosophy
