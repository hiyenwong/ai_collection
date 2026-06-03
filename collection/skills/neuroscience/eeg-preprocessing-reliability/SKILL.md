---
name: eeg-preprocessing-reliability
description: >
  EEG preprocessing reliability methodology for quantifying and mitigating
  preprocessing-induced prediction instability in EEG deep learning. Based on
  arXiv:2605.07212 (Hou et al., 2026). Use when: (1) evaluating EEG model
  robustness to preprocessing pipeline choices, (2) designing preprocessing-stable
  BCI/decoding systems, (3) analyzing counterfactory prediction flip rates (CFR),
  (4) implementing Preprocessing Uncertainty (PU) diagnostics, (5) applying
  NA-PGI regularization for graph-structured preprocessing consistency, (6)
  performing Walsh-Hadamard decomposition of preprocessing intervention space.
  Activation: eeg preprocessing reliability, preprocessing sensitivity, CFR,
  preprocessing uncertainty, PU, NA-PGI, EEG pipeline stability, counterfactual
  intervention, preprocessing flip rate, EEG deep learning reliability,
  预处理可靠性, 脑电预处理敏感性.
---

# EEG Preprocessing Reliability

Based on: *"Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability"* (Hou et al., arXiv:2605.07212, May 2026).

## Core Problem

EEG deep learning predictions are unstable under preprocessing choices. Across 6 datasets, up to **42% of trial-level predictions flip** when only preprocessing changes (same raw data, same model, same labels). Standard uncertainty methods (softmax entropy, MC Dropout, ensembles) hold preprocessing fixed and do not capture this.

## Seven Atomic Preprocessing Interventions

| # | Intervention | Option A (0) | Option B (1) | Impact |
|---|---|---|---|---|
| 1 | Reference | Common avg ref | Original | Medium |
| 2 | High-pass filter | 0.1 Hz | 0.5 Hz | High |
| 3 | Low-pass filter | 45 Hz | 30 Hz | High |
| 4 | Baseline correction | None | 200ms subtractive | High |
| 5 | Artifact attenuation | Off | ASR | High |
| 6 | Epoch rejection | Off | Autoreject | Med-High |
| 7 | Bad-channel repair | Off | RANSAC+interp | Medium |

These form a 7D Boolean lattice (128 pipelines, 448 edges).

## Key Findings

### Sensitivity Varies by Task

| Dataset | Task | Channels | Mean Acc (%) | CFR (%) |
|---------|------|----------|-------------|---------|
| BCI-IV-2a | MI (4-cls) | 22 | 37.6 | 42.4 |
| SEED-IV | Emotion (4-cls) | 62 | 31.9 | 35.8 |
| PhysionetMI | MI (2-cls) | 64 | 57.7 | 21.7 |
| Sleep-EDF | Sleep (5-cls) | 2 | 85.6 | 9.6 |
| Lee2019-ERP | P300 (2-cls) | 62 | 84.1 | 4.1 |
| P300 | ERP (2-cls) | 16 | 83.4 | 2.6 |

**CFR inversely correlates with accuracy**: preprocessing matters most when model is least confident.

### Sensitivity is Near-Additive

Walsh-Hadamard decomposition: interactions contribute 0.2% of total variance. Greedy step-by-step optimization achieves within 2.5% of oracle best-of-128 on all datasets. However, additivity may not extend to continuous preprocessing parameters.

### Dominant Interventions are Task-Specific

- BCI-IV-2a: epoch rejection dominates (20.9%)
- Sleep-EDF: high-pass filtering dominates
- P300: high-pass filtering dominates
- Spearman rank correlations of intervention importance: mean 0.32 (non-transferable across tasks)

## Diagnostic Metrics

### Counterfactual Flip Rate (CFR)

Fraction of test trials whose prediction changes across all 128 pipelines:
```
CFR = (1/|P|-1) * sum_{p != p_ref} I[f_p(x) != f_{p_ref}(x)]
```

### Preprocessing Uncertainty (PU)

Per-trial measure of pipeline disagreement, complementary to softmax entropy. Correlates only moderately with entropy (rho=0.42) and MC Dropout (rho=0.31).

### Per-Intervention Effect

Average accuracy change when toggling one intervention across 64 pipeline pairs.

## Mitigation: NA-PGI

**Normalized Adaptive Preprocessing-guided Intervention (NA-PGI)**: graph-structured regularizer exploiting the compositional lattice of preprocessing interventions.

- Reduces CFR by up to 35%
- Single transferable hyperparameter (lambda)
- Edge-level logit consistency with logit-variance normalization
- Most effective on high-density EEG settings

## Protocol for Evaluating Preprocessing Sensitivity

1. Select anchor pipeline (p0)
2. Train model on p0 only
3. Evaluate on all 128 counterfactual pipelines
4. Compute CFR and per-intervention effects
5. Identify dominant interventions for the task
6. (Optional) Apply NA-PGI for mitigation

## Implementation Notes

- All preprocessing via MNE-Python
- 128 variants: ~min/subject (CPU)
- ERM training: ~GPU-hour/dataset on A100
- EEGNet-v4 with 3-fold subject-wise CV
- Generate 128 counterfactual views per raw recording

## When to Apply

- Before reporting EEG decoding results: quantify preprocessing sensitivity
- When deploying BCI systems across sites: verify pipeline stability
- When comparing EEG studies: account for preprocessing-induced variability
- When training EEG foundation models: evaluate preprocessing robustness

## Code Reference

Original implementation: https://github.com/dengzhe-hou/EEG-Preprocessing-Sensitivity

## Related

- vlm-visual-cortex-alignment-robustness: complementary robustness analysis
- eeg-preprocessing-reliability: EEG decoding reliability assessment
- same-brain-different-prediction: methodological concern for all EEG studies
