---
name: variance-brain-foundation-models-forgot
description: "Brain Foundation Models (BFMs) lose third-order statistics (co-skewness) that predict cognition. Linear pipeline projecting to co-skewness-preserving subspace outperforms all pretrained BFMs with no GPU. BrainLM 650M predicts worse than 111M—variance allocation problem identified."
metadata:
  arxiv_id: "2606.04010"
  published: "2026-06-05"
  authors: "Giovanni Marraffini, Gabriel Mahuas, Trinidad Borrell, Victoria Shevchenko, Demian Wassermann"
  subjects: "q-bio.NC, cs.AI"
  key_results: "BFMs predict cognition worse than linear FC regression (~80K params)"
license: Complete terms in LICENSE.txt
---

# The Variance Brain Foundation Models Forgot: Third-Order Statistics Predict Cognition Where Billion-Parameter Models Fail

**arXiv ID**: 2606.04010  
**Authors**: Giovanni Marraffini, Gabriel Mahuas, Trinidad Borrell, Victoria Shevchenko, Demian Wassermann  
**Subjects**: q-bio.NC, cs.AI

## Abstract

Brain foundation models (BFMs) are self-supervised Transformers pretrained on fMRI data. We posit that these models should capture each subject's cognitive performance from their fMRI signal. Yet across three state-of-the-art BFMs and every readout we test, they predict cognition worse than a linear regression from the ~80K parameters of the functional connectivity matrix (FC). The gap widens with scale: BrainLM's 650M model predicts cognition worse than its 111M. We attribute this to a variance allocation problem: BFM pretraining captures the variance components that dominate fMRI but not the higher-order structure that predicts cognition. Our per-cumulant analysis of the reconstructed signal shows that the second-order covariance is partially preserved, while the third-order co-skewness tensor is largely destroyed. To recover what BFMs lose, we design a linear pipeline that projects the fMRI signal into the subspace that best preserves its co-skewness and computes FC there. This exceeds raw FC and every pretrained BFM on every dataset and parcellation we test, outperforming prior state-of-the-art under controlled evaluation with no pretraining and no GPU. We recover the raw-FC ceiling on BrainLM's forward pass by finetuning with a loss targeted at this same subspace. This shows that the bottleneck is the pretraining objective, not the architecture or the model size.

## Core Methodology

### Key Results

1. BFMs predict cognition worse than linear FC regression (~80K params)
2. BrainLM 650M worse than 111M—variance allocation problem
3. Second-order covariance preserved, third-order co-skewness destroyed
4. Linear pipeline with co-skewness subspace outperforms all BFMs
5. No GPU required, outperforms prior state-of-the-art
6. Pretraining objective is bottleneck, not architecture

### Implementation Steps

1. **Paper Analysis**: Extract methodology from full paper (PDF/HTML)
2. **Method Validation**: Verify key claims against experimental data
3. **Reproducibility Check**: Identify required datasets/tools
4. **Integration**: Connect to existing neuroscience skills/workflows

### Experimental Setup

- **Datasets**: NSD (7T fMRI), BOLD5000 (3T fMRI) for image decoding
- **Metrics**: Top-10 retrieval accuracy, zero-shot performance
- **Baselines**: Raw FC, pretrained BFMs (BrainLM, etc.)

## Pitfalls

- **Data Source Dependency**: Augmentation ratio must be tuned per dataset
- **Variance Allocation**: BFMs may destroy third-order statistics critical for cognition
- **Scale Paradox**: Larger models may perform worse (BrainLM 650M < 111M)

## Verification

- Check Top-10 retrieval accuracy improvement (>50%)
- Verify zero-shot decoding above chance
- Compare BFM vs raw FC performance gap

## Related Skills

- `brain-foundation-model-batch-effects` - BFM batch effect analysis
- `brain-dit-fmri-foundation-model` - Brain-DiT foundation model
- `cross-scale-spatial-generative-neurodegenerative` - Generative modeling

## Activation Keywords

brain foundation models, BFM, co-skewness, third-order statistics, variance allocation, functional connectivity, BrainLM, cognition prediction, fMRI
