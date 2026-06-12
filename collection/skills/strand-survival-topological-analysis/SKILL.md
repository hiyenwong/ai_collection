---
name: strand-survival-topological-analysis
description: STRAND (Survival Topological Representation ANalysis of Diagrams) treats persistence diagrams as survival data for hypothesis testing, effect sizes, and vectorisation in neuroscience applications.
tags:
  - neuroscience
  - topological-data-analysis
  - persistence-diagrams
  - survival-analysis
  - brain-connectivity
  - fMRI
activation_keywords:
  - STRAND
  - persistence diagrams
  - topological data analysis
  - survival analysis
  - brain connectivity
  - fMRI topology
version: 1.0.0
---

# STRAND: From Persistence to Survival - Topological Features Analysis

## Overview
This methodology from arXiv:2606.11911 (June 10, 2026) introduces **STRAND** (Survival Topological Representation ANalysis of Diagrams), which treats persistence diagrams as survival data, enabling hypothesis testing, interpretable effect sizes, and vectorisation from a single coherent representation.

**Authors**: Juliette Murris, Bernadette Stolz, Karsten Borgwardt

## Core Innovation

### Problem Addressed
Persistence diagrams (PDs) are standard in topological data analysis but:
1. **Do not naturally live in a vector space**
2. Statistical tools for comparing them evolved **separately** from downstream prediction methods
3. No unified framework linking hypothesis testing and machine learning

### Key Breakthrough
**STRAND treats (collections of) PDs as survival data**:
- Each topological feature with persistence $p = d - b$ is a **fully observed time-to-event**
- Persistence survival function $S(t) = \mathbb{P}(p > t)$ is central for comparing diagrams

## Three Capabilities from One Representation

### 1. Non-Parametric Two-Sample Test
- **Calibrated Type I error**
- **High power** from small number of diagrams
- Applicable to manifold topology comparisons

### 2. Interpretable Effect Sizes
- Quantifies topological feature differences
- Enables statistical inference beyond p-values

### 3. 1-Wasserstein-Stable Feature Vector
- **Wasserstein-stable** vectorisation
- For downstream machine learning tasks
- First unified framework for PD analysis

## Methodology

### Persistence as Survival Data
```python
# Each feature: time-to-event interpretation
persistence = death_time - birth_time  # time-to-event
survival_function = P(persistence > threshold)
```

### Survival Function Analysis
- Non-parametric estimation from PD collections
- Survival curves capture topological feature persistence
- Enables distribution comparison without parametric assumptions

### Vectorisation Strategy
- 1-Wasserstein distance preserved
- Embedding stable to geometric perturbations
- Suitable for ML classifier/regressor inputs

## Validation & Performance

### Synthetic Validation
- Manifold topology with **controlled structure**
- Calibration: **Type I error matches theoretical**
- Power: **High detection** of topological differences

### Benchmark Performance
- **14 graph datasets**
- **3D point cloud benchmarks**
- Competitive with specialized vectorisation methods

### Neuroscience Application
- **Functional brain connectivity** in fMRI data
- Network topology comparison across conditions
- Detect connectivity pattern differences

## Applications

### 1. Brain Network Analysis
- Compare connectivity topology between groups
- Test cognitive state effects on brain structure
- Detect disease-related topological changes

### 2. Neuroscience Hypothesis Testing
- Formal statistical tests for topological features
- Effect sizes quantify clinical significance
- Beyond mere classification accuracy

### 3. Topological ML Pipeline
- Unified framework: test → interpret → predict
- Single representation for all analysis stages
- Reproducible statistical inference

## Implementation Guide

### Key Concepts
```python
from strand import STRANDAnalyzer

# Initialize with persistence diagrams
analyzer = STRANDAnalyzer(pd_collection)

# Two-sample test
test_result = analyzer.two_sample_test(group1_pds, group2_pds)

# Effect size
effect = analyzer.effect_size(group1_pds, group2_pds)

# Feature vector for ML
features = analyzer.vectorise(pd_collection)
```

### Calibration Guarantee
- Type I error under null hypothesis matches significance level
- No ad-hoc threshold selection
- Proper statistical inference

## Technical Details

### Survival Function Properties
- Non-parametric Kaplan-Meier style estimation
- Captures persistence distribution structure
- Robust to outlier features

### Wasserstein Stability
- 1-Wasserstein metric preserved in embedding
- Geometric perturbations bounded
- Suitable for downstream learning

### Statistical Framework
- Hypothesis testing with calibrated p-values
- Effect sizes with confidence intervals
- Vectorisation for prediction tasks

## Cross-References

- [[higher-order-brain-networks]] - Higher-order topological analysis
- [[brain-connectivity-analysis]] - Connectivity methods
- [[fmri-foundation-model-batch-effects]] - Batch effects in fMRI
- [[topological-effective-connectivity-hodge]] - Hodge decomposition

## Key Insight

> **STRAND is the first method to provide hypothesis testing, effect sizes, and vectorisation for persistence diagrams from a single coherent and interpretable representation, enabling proper statistical inference in topological neuroscience.**

## Activation Keywords

Use when working on:
- Persistence diagram analysis
- Topological brain connectivity
- Statistical testing of topological features
- Vectorisation of persistence diagrams
- fMRI network topology comparison