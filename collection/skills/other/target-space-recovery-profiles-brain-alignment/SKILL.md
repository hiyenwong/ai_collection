---
name: target-space-recovery-profiles-brain-alignment
description: "Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment — a framework for identifying which reproducible brain response dimensions are recovered by model predictions, going beyond simple prediction accuracy. (arXiv:2605.20127)"
tags: [brain-alignment, model-evaluation, fmri, visual-cortex, prediction-accuracy, encoding-models, reproducible-dimensions]
---

# Target-Space Recovery Profiles for Model-Brain Alignment

**Paper**: [arXiv:2605.20127](https://arxiv.org/abs/2605.20127) — Submitted 19 May 2026
**Authors**: Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, Ayumu Yamashita, Kaoru Amano
**Categories**: q-bio.NC, cs.AI, cs.LG

## Summary

Artificial vision models are often evaluated against the human visual cortex by measuring how accurately their internal representations predict brain responses. However, **prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered**. This paper introduces a unified framework for evaluating both model-brain and brain-brain alignment by identifying the **response dimensions recovered by prediction**.

## Key Findings

1. **Reproducible response dimensions**: Using repeated fMRI measurements, the framework identifies target-brain response dimensions that can be reproducibly predicted across independent trial splits.

2. **Early-to-intermediate visual cortex is low-dimensional**: The early-to-intermediate visual-cortex responses contain a **low-dimensional set of reproducible dimensions**.

3. **Brain-to-brain diagnostic reference**: Brain-to-brain comparisons identify which dimensions are consistently recoverable from other subjects' brains, providing a **diagnostic human reference** rather than only a scalar benchmark.

4. **Prediction accuracy can mask mismatches**: In some cases, **pretrained and randomly initialized models achieve similar prediction accuracy** while showing distinct recovery profiles across these response dimensions.

## Methodology

- **Data**: Natural Scenes Dataset (fMRI, 8 subjects viewing same natural images)
- **Step 1**: Identify reproducible brain response dimensions via repeated trial splits
- **Step 2**: Predict target-brain responses from another subject's brain or a vision model's representations
- **Step 3**: Quantify recovery strength for each reproducible dimension
- **Evaluation**: Compare recovery profiles across models and across subjects

## Implications

- Provides a **more diagnostic evaluation** of alignment between artificial vision models and the human visual cortex
- Reveals that **prediction accuracy alone is insufficient** — two models can have the same accuracy but recover different brain dimensions
- Enables **targeted model improvement** by identifying which response dimensions need better alignment
- Serves as a **bridge between encoding model evaluation and representational similarity analysis**

## Activation

**Keywords**: brain alignment, model evaluation, fMRI, encoding models, prediction accuracy, response dimensions, representational similarity, Natural Scenes Dataset, visual cortex, reproducible dimensions, target-space recovery

## Related Skills

- `platonic-representations-brain-universal-geometry` — Cross-subject geometric alignment
- `geometric-brain-dynamics-mapping` — Geometry-aware brain dynamics mapping
- `neuroscience-of-transformers` — Transformer architectures for brain data modeling
- `decoding-encoding-alignment-critique` — Critical analysis of brain-model alignment
