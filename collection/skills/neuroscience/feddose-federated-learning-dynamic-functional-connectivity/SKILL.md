---
name: feddose-federated-learning-dynamic-functional-connectivity
description: "FedDOSE framework for federated learning that explicitly decomposes site effects for modeling brain dynamic functional connectivity. Introduces Modularity-Guided Tucker Decomposition to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns. Uses class-specific prototypes with Optimal Transport barycenter formulation and Procrustes analysis for global alignment across sites."
metadata:
  arxiv_id: "2608.07393"
  published: "2026-08-11"
  authors: "Deepank Girish, Yi Hao Chan, Yubin Zheng, Sukrit Gupta, Jagath C. Rajapakse"
  tags: [federated-learning, dynamic-functional-connectivity, multi-site-fmri, autism-spectrum-disorder, adhd, optimal-transport, tucker-decomposition, modularity-guided, procrustes-analysis]
license: Complete terms in LICENSE.txt
---

# FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity

## Overview

FedDOSE is a novel federated learning framework that explicitly decomposes site effects for analysis of dynamic functional connectivity (dFC) in multi-site fMRI datasets. While standard federated learning approaches struggle with statistical heterogeneity and site differences in multi-site data settings, FedDOSE addresses these challenges by introducing a Modularity-Guided Tucker Decomposition block to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns efficiently.

The framework generates class-specific prototypes across all sites and aligns them at the global level using a combination of Optimal Transport (OT) barycenter formulation and Procrustes analysis. Extensive experiments for diagnosing Autism Spectrum Disorder (ASD) and Attention-Deficit Hyperactivity Disorder (ADHD) on three multi-site resting-state fMRI datasets (ABIDE-I, ABIDE-II, and ADHD-200) demonstrate that FedDOSE outperforms state-of-the-art methods in ASD and ADHD detection.

## When to Use

Use FedDOSE when:
- Working with multi-site fMRI datasets requiring privacy-preserving collaborative training
- Analyzing dynamic functional connectivity (dFC) instead of static FC
- Needing to handle statistical heterogeneity and site differences in federated learning
- Diagnosing neurodevelopmental disorders like ASD and ADHD
- Requiring modular-level spatio-temporal pattern analysis
- Working with high-dimensional dFC tensors that need efficient encoding

## Core Methodology

### 1. Modularity-Guided Tucker Decomposition
- Encodes high-dimensional dFC tensors efficiently
- Captures modular-level spatio-temporal patterns
- Reduces dimensionality while preserving relevant information
- Incorporates brain network modularity as prior knowledge

### 2. Class-Specific Prototype Generation
- Generates prototypes for each diagnostic class (healthy, ASD, ADHD)
- Prototypes are created across all participating sites
- Enables consistent representation learning despite site differences
- Provides interpretable class representations

### 3. Global Alignment Strategy
- **Optimal Transport (OT) Barycenter Formulation**: Aligns prototypes across sites using optimal transport theory
- **Procrustes Analysis**: Further refines alignment through geometric transformation
- Combines both methods for robust cross-site consistency
- Preserves local site-specific characteristics while ensuring global coherence

### 4. Federated Learning Architecture
- Privacy-preserving paradigm for collaborative training
- Explicit decomposition of site effects
- Handles statistical heterogeneity across sites
- Maintains data locality while enabling model sharing

## Implementation Guidelines

### Data Preparation
1. **dFC Tensor Construction**: Compute dynamic functional connectivity matrices over sliding time windows
2. **Site Metadata**: Collect site-specific metadata for heterogeneity analysis
3. **Quality Control**: Apply consistent preprocessing across all sites
4. **Dataset Partitioning**: Ensure appropriate train/validation/test splits per site

### Model Architecture
1. **Tucker Decomposition Block**: Implement modularity-guided Tucker decomposition with appropriate ranks
2. **Prototype Layer**: Design prototype generation layer with appropriate number of prototypes per class
3. **Alignment Module**: Implement OT barycenter and Procrustes analysis components
4. **Federated Communication**: Set up secure communication protocol between sites

### Training Protocol
1. **Local Training**: Train models locally at each site with site-specific data
2. **Prototype Exchange**: Share only prototype representations, not raw data
3. **Global Alignment**: Perform OT and Procrustes alignment at central server
4. **Model Aggregation**: Aggregate aligned models using federated averaging or similar techniques

## Expected Results

- Superior performance in ASD and ADHD detection compared to state-of-the-art methods
- Robust learning from multi-site datasets with statistical heterogeneity
- Effective handling of site differences through explicit decomposition
- Preservation of privacy through federated learning paradigm
- Efficient encoding of high-dimensional dFC tensors through Tucker decomposition

## Pitfalls and Considerations

- **Computational Complexity**: Tucker decomposition and OT alignment can be computationally intensive
- **Site Heterogeneity**: Extreme site differences may still pose challenges despite decomposition
- **Prototype Quality**: Performance depends on quality and representativeness of prototypes
- **Communication Overhead**: Federated learning requires multiple communication rounds
- **Hyperparameter Tuning**: Multiple hyperparameters for decomposition ranks, OT parameters, etc.
- **Data Imbalance**: Site-specific data imbalances may affect prototype quality

## Activation Keywords

- FedDOSE federated learning
- Dynamic functional connectivity dFC
- Multi-site fMRI privacy
- Modularity-Guided Tucker Decomposition
- Optimal Transport barycenter fMRI
- Procrustes analysis federated
- ASD ADHD diagnosis multi-site
- Site effects decomposition
- Class-specific prototypes fMRI
- Brain network modularity federated

## References

- Original Paper: arXiv:2608.07393 [cs.LG]
- Related Skills:
  - `federated-brain-trajectory-gnn`
  - `dynamic-path-brain-connectivity`
  - `time-varying-brain-connectivity`
  - `functional-connectivity-graph-neural-networks`
  - `specificity-aware-federated-graph-learning`