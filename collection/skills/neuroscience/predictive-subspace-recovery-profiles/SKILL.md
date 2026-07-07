---
name: predictive-subspace-recovery-profiles
description: Target-Space Recovery Profiles methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which reproducible brain response dimensions are recovered by predictions, enabling diagnostic evaluation of NeuroAI model-brain alignment. Activation: model brain alignment, predictive subspace, recovery profile, brain prediction evaluation, NeuroAI alignment, target-space recovery, NSD analysis.
---

# Predictive Subspace Recovery Profiles Methodology

Target-Space Recovery Profiles methodology for evaluating model–brain alignment beyond scalar prediction accuracy.

## Core Insight

Prediction accuracy alone cannot reveal **which dimensions** of the target brain's response space are recovered by a model. Two models with identical prediction accuracy may recover completely different response dimensions. This methodology makes the structural content of prediction explicit.

## Key Components

### 1. Reproducible Target Reference
- Use **repeated fMRI measurements** of the same stimuli to identify target-brain response dimensions that are reproducibly recoverable across independent trial splits
- Fit target-to-target predictions between split halves → extract orthonormal target basis vectors **uⱼ** ranked by reproducibility
- The first 3 dimensions typically account for ~89% of normalized reference weight; median entropy effective rank ≈ 5.12

### 2. Predictive Subspace
- For any source (another subject's brain OR a model's internal representations), fit a ridge-regularized low-rank linear mapping to target responses
- Extract the orthonormal basis **Qₛ** spanning the predictive subspace in target response space
- Prediction accuracy = held-out correlation between predicted and observed responses

### 3. Recovery Profile
- **Directional Reference Coverage**: DirCovₛ,ⱼ = ‖Qₛᵀuⱼ‖²₂ — how much the predictive subspace overlaps with each target-reference direction
- Sort target-reference dimensions by coverage strength → get ordered profile
- Profile shape reveals which dimensions are recovered and which are missed

### 4. Brain-to-Brain Human Reference
- Brain-to-brain recovery profile provides human reference: shows which dimensions are typically recoverable from another subject
- Model-to-brain profiles should be interpreted **relative to** this human reference
- Coverage declines from ~0.96 at k=1 to ~0.87 at k=10 for brain-to-brain (structured decline, not flat)

## Key Findings (Nakamura et al., 2026)

### Pretraining changes recovery profiles beyond accuracy
- ImageNet-pretrained models exceed 4-seed random mean in profile mean by 0.177 (95% CI: 0.162–0.192)
- Random models can match prediction accuracy but recover different dimensions

### Brain-to-brain as diagnostic reference
- Brain sources recover dimensions with characteristic declining profile
- Provides "human ceiling" for what is recoverable from biological systems
- Pairs of brain sources show small profile differences; model-brain pairs show larger differences

### Accuracy-matched analysis reveals structural mismatches
- Near-equal accuracy pairs (|Δaccuracy| ≤ 0.01): pretrained models consistently show higher top-k coverage
- Scalar accuracy masks directional mismatches in target response space

## When to Use

- **Requires repeated measurements** of target brain (splits define reference)
- Most appropriate for **measured response patterns** (voxel, neural population responses)
- Complementary to existing alignment methods (RSA, encoding models, alignment pattern analysis)
- Useful when goal is not only to predict but to **understand which parts** of target response space are recovered

## Experimental Protocol

### Data
- NSD-core-shared: 8 subjects, 515 shared repeated natural images
- ROIs: V1v, V1d, V2v, V2d, V3v, V3d, hV4 (both hemispheres)
- 5 synchronized outer folds for cross-validation

### Sources
- Brain sources: responses from non-target subjects in corresponding ROI
- Model sources: ResNet-18/50, VGG-16, ViT-B/16 (pretrained and randomly initialized)

### Fits
- Ridge-regularized low-rank linear fits
- Rank and regularization selected by inner CV on outer-training images
- Recovery profiles computed from source-induced predictive subspaces
- Profile plots display top-k prefixes through k=10

## Implementation Steps

1. **Estimate reproducible target reference** via split-half target-to-target prediction
2. **Fit source-to-target mapping** for each source (brain or model)
3. **Extract predictive subspace** Qₛ from fitted mapping
4. **Compute directional coverage** for each target-reference direction
5. **Build recovery profile** by sorting dimensions by coverage strength
6. **Compare** model-to-brain profile against brain-to-brain human reference

## Pitfalls

- **Not a global brain-likeness claim**: high recovery only supports conditional interpretation for the evaluated ROI, dataset, preprocessing, and readout class
- **Cannot be used as held-out prediction accuracy**: recovery profiles are diagnostics, not additional prediction scores
- **Repeated measurements required**: without repeats, reproducible reference cannot be estimated
- **Fitting/evaluation separation**: outer-test responses only define evaluation reference, never used for model selection or hyperparameter tuning

## Related Concepts

- Encoding models, Representational Similarity Analysis (RSA)
- Alignment Pattern Analysis (cross-region relational criterion)
- Spectral theory of neural prediction (model-side geometry decomposition)
- Brain-to-brain prediction as human reference benchmark
- GLMdenoise response-amplitude estimation

## Related Skills

- `decoding-encoding-alignment-critique` — Critical analysis of brain-model alignment methods
- `feature-visualization-brain-encoder` — Feature visualization for brain encoder interpretability
- `naturality-violation-score` — Category-theoretic brain-DNN alignment
- `brain-dit-fmri-foundation-model` — fMRI foundation model evaluation
- `in-context-brain-decoding` — Training-free cross-subject brain decoding

## Reference

- **Title**: Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model–Brain Alignment
- **Authors**: Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, Ayumu Yamashita, Kaoru Amano
- **arXiv**: 2605.20127 [q-bio.NC, cs.AI, cs.LG]
- **Date**: May 2026
- **Institution**: The University of Tokyo, Osnabrück University, Freie Universität Berlin, Kobe University
- **Dataset**: Natural Scenes Dataset (NSD)
- **URL**: https://arxiv.org/abs/2605.20127
