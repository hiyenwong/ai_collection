---
name: bayesian-sparsity-shared-neural-response
description: "Bayesian sparsity modeling framework for detecting shared neural responses across individuals in fMRI data using intersubject correlation (ISC) analysis. Activation: Naturalistic fMRI analysis, Movie-watching studies."
---

# Bayesian Sparsity Modeling of Shared Neural Response in fMRI

> Bayesian sparsity modeling framework for detecting shared neural responses across individuals in fMRI data using intersubject correlation (ISC) analysis.

## Metadata
- **Source**: arXiv:2604.21676v1
- **Authors**: Spencer Wadsworth, Nabin Koirala, Nicole Landi et al.
- **Published**: 2026-04-23
- **Categories**: stat.AP

## Core Methodology

### Key Innovation
### Core Method
The Bayesian Sparsity Modeling (BSM) framework addresses key limitations of traditional Intersubject Correlation (ISC) analysis:

1. **Sparsity Prior**: Introduces Bayesian sparsity modeling to identify shared neural responses while handling noise and individual differences
2. **Group-Level Inference**: Enables principled statistical inference at the group level rather than pairwise comparisons
3. **Robustness**: More robust to outliers and heterogeneous responses across subjects

### Technical Framework
- **Prior**: Sparse prior (spike-and-slab or horseshoe) on shared response components
- **Likelihood**: Gaussian observation model for fMRI time series
- **Inference**: Variational Bayes or MCMC for posterior estimation
- **Output**: Posterior probability maps of shared neural responses

## Implementation Guide

### Prerequisites
### Prerequisites
- Python 3.8+
- NumPy, SciPy for numerical computation
- PyMC or NumPyro for Bayesian inference
- Nilearn for fMRI data handling

### Step-by-Step
1. **Preprocess fMRI**: Motion correction, normalization, smoothing
2. **Extract Time Series**: From regions of interest or whole brain
3. **Apply BSM**: Fit Bayesian sparsity model to group data
4. **Posterior Analysis**: Identify regions with high probability of shared response
5. **Statistical Testing**: Compare against null models

### Applications
- Naturalistic fMRI analysis
- Movie-watching studies
- Social cognition research
- Clinical biomarker discovery

## Pitfalls
- Requires sufficient subjects (>20 recommended)
- Computationally intensive for whole-brain analysis
- Prior sensitivity in sparse regions

## Related Skills
- neuroscience-research-method
- brain-connectivity-analysis
- eeg-decoding-brain-computer-interface

## References
- arXiv: https://arxiv.org/abs/2604.21676v1
