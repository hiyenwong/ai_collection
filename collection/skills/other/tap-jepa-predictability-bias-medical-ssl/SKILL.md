---
name: tap-jepa-predictability-bias-medical-ssl
description: Predictability-bias audit of JEPA medical SSL. Use when analyzing masked predictive pretraining.
category: ai_collection
---

# TAP-JEPA Predictability Bias in Medical SSL

**Paper**: "The Predictability Bias of Joint-Embedding Predictive Learning in Medical Imaging" (arXiv:2610.13237, Drexel et al., TUM/Imperial, Oct 2026)

## Core Insight

Joint-embedding predictive architectures (JEPA/I-JEPA/V-JEPA family) learn by predicting teacher representations of **masked targets from visible context**. Point prediction collapses the conditional target distribution to its mean — it **cannot reproduce variation that context does not resolve**. This is the **predictability bias**: the objective preferentially preserves context-constrained (predictable) information and loses context-independent information.

In medical imaging this is clinically dangerous: **recurrent anatomy is predictable from context; sporadic localized pathology often is not**. A lesion can be evident in its own voxels yet unpredictable when those voxels are hidden. The encoder organizes around "what anatomy makes predictable" while clinically decisive deviations are less reliably retained.

## Reusable Methodology: Tracing the Training Objective (Audit Protocol)

The transferable contribution is not the encoder but the **audit pipeline** — replaying the exact masking, teacher, and predictor computations at a fixed checkpoint (no parameter updates) to measure what survives prediction:

1. **Masking-exposure audit**: replay production masks (1,600/scan); classify each pathology event as fully visible / partially visible / fully hidden+targeted. Found 61.5–81.4% of pathology events fully hidden; pathology tokens are rare (0.41–7.04 per 1,000 target tokens).
2. **Teacher-to-prediction retention (Skill shortfall)**: fit identical linear probes on (a) geometry-only baseline B (mask mode, grid position, occupancy, nearest-context distance), (b) predicted features Ẑ, (c) normalized teacher targets Z, at the same tokens. Normalized shortfall Q_short = [Skill(Z) − Skill(Ẑ)] / [Skill(Z) − Skill(B)] = fraction of teacher-accessible discrimination lost. Pathology shortfall 31.8–36.7% vs anatomy 6.2–11.2%.
3. **Pathology–control displacement (Actr metric)**: hide pathology + shape/voxel-matched control translated within the same organ; project teacher and predicted features on cross-fitted teacher pathology–control axes. Actr = x²-weighted mean signed fractional reduction in teacher separation, decomposed D+ (pathology→control) vs D− (control→pathology). Prediction attenuates separation 17.9–72.4%, pathology-side dominant in 5/6 categories; attenuation grows with distance from visible context (liver: 67.4%→83.4% beyond 96mm). Calibrate against 4,096 random axes to separate pathology-directed attenuation from generic contraction.
4. **Visible-context intervention**: replace visible pathology vs matched-control final-layer activations with same-organ mean; re-evaluate predictor on shared clean targets. Control replacement costs MORE than pathology replacement (+12.6% to +27.3% in 4 categories) — visible pathology contributes less than normal tissue to predicting surroundings.
5. **Downstream token-deletion**: delete all final-layer pathology tokens from attentive-MIL scan probes, renormalize attention without refitting; decision margin drops ≤0.45% for 4/7 probes (but 10.5% for atelectasis) — decisions may route around local findings.

## Key Metrics & Prevalence-Normalized Skill

Use **Skill = (AP − π)/(1 − π)** (prevalence-normalized average precision) for rare-class regional probes: 0 when AP = prevalence, 1 for perfect. Essential when positives are 0.4–7 per 1,000 tokens — raw AP is uninterpretable.

## Design Implications (when building medical SSL)

- **Contextual predictability ≠ clinical relevance.** Never assume a strong transfer benchmark certifies that local findings are represented.
- Training objectives should **retain diagnostic features regardless of predictability from surrounding anatomy**: complement JEPA losses with objectives that preserve context-independent variation (e.g., contrastive/instance terms on pathology-candidate regions, report-supervised or anomaly-conditional signals).
- Small/low-contrast findings remain hard across ALL current CT foundation models — probe them explicitly.
- Audit BEFORE deploying: the masking-exposure audit alone tells you whether your target task's evidence is typically hidden during pretraining.
- Caveat from paper: alternative scan-level cues (acquisition metadata, co-occurring labels) are themselves predictive (0.68–1.24× encoder Skill) — leakage-prone benchmarks can mask missing pathology representations.

## Training Details (for replication)

ViT-B/3D student + EMA teacher + 6-layer predictor; 113,611 thoraco-abdomino-pelvic CT volumes (NLST+CT-RATE+Merlin+AbdomenAtlas); 240 epochs, 32×H200, 1,622 GPU-hours; 24mm isotropic tokens; multi-block targets + cropped context + multi-scale blocks; ~16% in-body tokens visible / 84% hidden; occupancy-weighted feature-wise L1. Frozen features competitive with COLIPRI/Merlin/VoxelFM on RAD-ChestCT and Merlin benchmarks (highest AUPRC 0.5268 external thorax; highest AUROC 0.8714 abdomen) — bias exists even in SOTA-competitive encoders.

## Related Skills

- `neurolens-jepa-chronic-recordings` — JEPA latent-space prediction for electrode drift
- `stock-jepa-prior-anchored-revision` — prior-anchored JEPA for finance
- `matched-input-eeg-fm-audit` — auditing methodology in adjacent modality

## Activation

predictability bias, JEPA audit, masked predictive pretraining, medical SSL failure modes, pathology representation loss, Skill prevalence normalization, teacher-prediction replay, CT foundation model critique
