---
name: target-space-recovery-profiles
description: "Target-Space Recovery Profiles (TSRP) methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which reproducible brain response dimensions are recovered by prediction models."
---

# Target-Space Recovery Profiles (TSRP) Methodology

**Paper**: Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment
**arXiv**: [2605.20127](https://arxiv.org/abs/2605.20127)
**Authors**: Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, Ayumu Yamashita, Kaoru Amano
**Date**: May 20, 2026
**Categories**: q-bio.NC, cs.AI, cs.LG

## Core Problem

Artificial vision models are typically evaluated against the human visual cortex by measuring how accurately their internal representations predict brain responses (e.g., fMRI, EEG). However, **prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered**. Two models with identical prediction accuracy may recover fundamentally different neural response patterns, masking model-brain mismatches.

## TSRP Framework

### Step 1: Identify Reproducible Response Dimensions

Using repeated measurements of the target brain (e.g., repeated fMRI trials):

1. Split data into independent trial splits
2. Identify response dimensions that can be **reproducibly predicted** across splits
3. These reproducible dimensions form the "recovery space" for evaluation

### Step 2: Predict Target-Brain Responses

Given either:
- Another subject's brain responses (brain-to-brain prediction), or
- A model's internal representations (model-to-brain prediction)

Predict target-brain responses using the same prediction pipeline.

### Step 3: Quantify Recovery Strength

For each reproducible response dimension identified in Step 1:
- Compute how strongly that dimension is recovered by the prediction
- Build a **recovery profile**: a vector of recovery strengths across all dimensions

### Step 4: Diagnostic Evaluation

- Compare recovery profiles across different models
- Compare model recovery profiles against brain-to-brain recovery profiles (human reference)
- Identify which specific dimensions each model fails to capture

## Key Findings (from Natural Scenes Dataset)

1. **Early-to-intermediate visual cortex** responses contain a **low-dimensional set of reproducible dimensions**
2. Brain-to-brain comparisons identify which dimensions are **consistently recoverable** across subjects, providing a diagnostic human reference
3. Pretrained and randomly initialized models can achieve **similar prediction accuracy** while showing **distinct recovery profiles**
4. **Prediction accuracy alone can mask model-brain mismatches**

## Applications

- **Model-brain alignment evaluation**: Beyond scalar accuracy metrics, provide diagnostic dimension-by-dimension analysis
- **Cross-subject neural consistency**: Quantify which response dimensions are shared across individuals
- **Model development guidance**: Identify specific neural response dimensions that models fail to capture
- **Benchmark design**: Replace single-number benchmarks with diagnostic profile comparisons

## Implementation Considerations

### Data Requirements
- Repeated measurements of the same stimuli for the same subjects (to establish reproducibility)
- Multiple subjects viewing the same stimuli (for brain-to-brain reference)
- Sufficient trials per condition to enable reliable split-half analysis

### Dimensionality Reduction
- PCA or similar methods to identify dominant response dimensions
- Focus on dimensions that show high reproducibility across trial splits
- Low-dimensional structure expected in early visual cortex

### Recovery Metric
- Correlation-based or regression-based measurement of dimension recovery strength
- Normalize across dimensions for fair comparison
- Statistical testing for significance of recovery differences

## Connection to Existing Skills

This methodology extends and complements:
- **target-predictor-profiles** (existing skill): TSRP generalizes from model-to-model prediction to model-brain and brain-brain alignment
- **naturality-violation-score**: Both address model-brain alignment but TSRP focuses on dimension recovery rather than transformation naturality
- **encoding-evaluation-ground-truth**: TSRP provides a complementary evaluation framework that doesn't require ground-truth approximations

## Activation

Trigger words: target-space recovery, model-brain alignment evaluation, brain response dimensions, reproducible neural dimensions, beyond prediction accuracy, diagnostic alignment, recovery profile, brain-to-brain comparison, visual cortex alignment

## Pitfalls

- **Requires repeated measurements**: Cannot be applied to single-trial datasets without modifications
- **Dimension selection bias**: The choice of dimensionality reduction method affects which dimensions are identified
- **Cross-subject variability**: Brain-to-brain reference profiles may vary depending on subject population
- **Not a replacement for accuracy**: TSRP complements but does not replace prediction accuracy metrics
