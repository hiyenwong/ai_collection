---
name: eeg-text-semantic-alignment-imagined-speech
description: "Contrastive EEG-text alignment for imagined-speech BCI"
tags: [eeg, imagined-speech, contrastive-learning, bci, semantic-alignment, reliability, brain-computer-interface]
---

# Semantic Alignment of EEG and Text: Contrastive Framework for Imagined Speech Decoding

**Source**: arXiv:2610.20766v1 (2026-10-14, q-bio.NC/cs.LG) — Namdari, Iacomi, Barbieri, Mainardi. Aligns single-trial imagined-speech EEG into a **frozen language embedding space** via semantically reweighted contrastive learning, keeping closed-set decoding parity while gaining retrieval, intrinsic reliability ranking, and semantic-structure probing.

**Activation**: imagined speech decoding, EEG-language alignment, EEG-text contrastive, open-vocabulary BCI, decoding confidence/reliability without confidence head, semantic EEG probing, Chisco dataset, BGE text encoder for neural decoding.

## When to Use
- Building imagined-speech / inner-speech BCI where outputs must go beyond a fixed label set (ranked retrieval, candidate shortlists, user-in-the-loop confirmation)
- Need an **intrinsic decoding-reliability signal** without training a separate confidence head
- Want to probe whether EEG representations carry semantic structure beyond training labels

## Core Recipe

### 1. Frozen Text Encoder as Fixed Semantic Manifold
- Embed stimulus sentences + category names with a pretrained text encoder, **L2-normalized**, weights FROZEN during EEG training (avoids moving-target + preserves pretrained semantics; fine-tuning on tiny vocab distorts space)
- Encoder selection = empirical probe benchmark (Linear/MLP/XGBoost Top-1 on the 39 categories + zero-shot): bge-small-zh-v1.5 (24M, 512-d) matched bge-base/large separability (~0.77 vs 0.80 linear probe) at ~4x less compute — model size did NOT monotonically help

### 2. EEG Encoder
EEGNet-style conv backbone (122ch × 1651 samples) → 4-layer Transformer (8 heads, key-dim 64) → attention pooling → MLP(256, GELU) → 512-d output → **L2-normalize** (shared unit hypersphere with text).

### 3. Composite Objective (the key idea)
`L = λ_align·L_SNCE + λ_cls·L_CE` with λ_align=1, λ_cls=0.5.

**L_SNCE — semantically reweighted InfoNCE** (preserves text-space topology):
```
L_SNCE = -1/N Σ W_{y_i} log[ exp(s(z_i,t_i)/τ) / Σ_j ω_ij·exp(s(z_i,t_j)/τ) ]
ω_ij = 1                        (i=j)
     = max(δ, 1 - cos(t_i,t_j)) (i≠j),  δ=0.05
W_y = freq_y^(-0.5)             (inverse-sqrt class-balanced weights)
```
Semantically CLOSE negatives are down-weighted (penalized less); distant negatives get full weight → soft contrastive that keeps the geometry of the frozen space instead of collapsing it.

**L_CE — prototype-tied classification (NO learned linear head)**:
- Class prototypes p_c = L2-normalized embeddings of category descriptions from the SAME frozen encoder
- Logits = scaled dot-products s(z_i, p_c)/τ with the SAME learnable temperature (τ init 0.07, clipped [0.01, 1.0], jointly optimized)
- Weighted CE + label smoothing ε=0.1 → class separability anchored to the frozen geometry

### 4. Evaluation Battery (rigor pattern worth copying)
- **Sentence-grouped stratified 5-fold CV** (all trials of a sentence stay in one fold); 15% of train pool = validation; test folds untouched by model selection
- **Prior-aware chance baselines**: 10,000 Monte Carlo samples per fold (class-imbalanced data → naive 1/C is wrong)
- **Balanced 2v2 pairwise accuracy** (20,000 class-balanced pairs; chance 50%; ties half-credit) — BCI-realistic two-intent discrimination; compute from EEG-prototype cosines (contrastive) or class probs (closed-set)
- **MaxCosine selective decoding**: m_i = cos(z_i, p_ŷ). Derive coverage thresholds (100/80/60/40/20%) on VALIDATION scores only, apply unchanged to test → coverage transfer + selective accuracy + validation-referenced quintiles + AUROC(correct vs incorrect)
- **Evaluation-time semantic axes**: 5 bipolar axes (e.g. Practical–Emotional) from 3 anchor phrases/pole embedded by frozen encoder; EEG-side vs sentence-side assignment agreement (balanced acc, chance 50%) — axes NEVER used in training
- **Semantic Gallery Probe (SGP)**: color unseen held-out sentences by cosine to a test EEG embedding (qualitative open-candidate inspection, PCA 2D)

## Training Hyperparameters (verified)
- Batch 64, Adam lr 3e-4, ×0.7 after 5 stale epochs (min 1e-6), early stop 16 epochs, ≤100 epochs
- Augmentation: Gaussian noise σ=0.05; channel dropout 10% w.p. 0.1; circular time-shift ±50 samples
- Model selection: validation Top-5 (retrieval-oriented) for contrastive; validation Top-1 for closed-set — criteria FIXED before test evaluation

## Key Results (Chisco, 5 subjects, 39 categories)
- Parity with task-optimized closed-set classifier: Top-1 ~0.08–0.11 (chance 0.03), Top-5 ~0.29–0.33 (chance 0.15), macro-F1 0.057–0.070, 2v2 0.69–0.73 — language-space mapping costs nothing on fixed-intent metrics
- **MaxCosine works as free reliability signal**: at 20% validation-target coverage, Top-1 8.3→17.2 (range 15.6–19.2 across subjects), Top-5 29→49 (42.9–50.5); AUROC 0.60–0.64 all folds > 0.5; coverage transfers within ~1pp
- Reliability info concentrated in TOP quintile (17.2% vs 5.4–7.2% lower quintiles — not a strict monotone gradient)
- Semantic axes: all 5 above chance — Practical–Emotional 61.3%, Goal-directed–Leisure 60.0%, Physical–Cognitive 59.2%

## Pitfalls / Scope Limits
- MaxCosine is a **raw ranking score, NOT a calibrated probability** — do not interpret as p(correct); no online abstention tested
- Comparison is **system-level** (different backbones for the two systems) — does not isolate the training objective under identical architecture
- Within-subject only, 5 healthy subjects, single dataset — no cross-session/population claims
- Frozen-encoder choice is dataset-language-dependent (Chinese → bge-zh); rerun the probe benchmark per language/corpus
- 2v2 for the contrastive system computed against category PROTOTYPES, not sentence embeddings (match the closed-set task)

## Related Skills
- [[mindalign-eeg-visual-decoding]] — tri-modal EEG/vision/language contrastive (visual decoding counterpart)
- [[imagined-speech-cross-subject-null]] — leakage-controlled cross-subject imagined-speech evaluation (same arXiv batch, 2610.20954)
- [[eeg-speech-decoding-detection-floor-audit]] — positive-control/detection-floor rigor for speech-EEG claims
