---
name: feddose-federated-brain-connectivity
title: FedDOSE Federated Learning Framework for Brain Dynamic Functional Connectivity
version: 1.0.0
description: FedDOSE federated brain dFC with site decomposition.
trigger: Use when implementing federated learning for multi-site fMRI dynamic functional connectivity analysis that needs to handle site heterogeneity while preserving privacy.
---

# FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity

## Overview
FedDOSE is a novel federated learning framework that explicitly decomposes site differences for analysis of dynamic functional connectivity (dFC) in multi-site fMRI datasets. It addresses two key challenges: statistical heterogeneity due to site differences and the limitation of existing FL approaches that rely on static functional connectivity, omitting dynamic information in brain networks.

## Key Innovations

### 1. Modularity-Guided Tucker Decomposition
- Encodes high-dimensional dFC tensors efficiently
- Captures modular-level spatio-temporal patterns
- Reduces dimensionality while preserving dynamic information

### 2. Class-Specific Prototype Generation
- Generates prototypes across all sites for each class (e.g., ASD, ADHD)
- Uses Optimal Transport (OT) barycenter formulation for global alignment
- Applies Procrustes analysis for fine-grained alignment

### 3. Site Effect Decomposition
- Explicitly models and separates site-specific effects from disease signatures
- Enables robust representation learning from heterogeneous multi-site data
- Maintains privacy through federated learning paradigm

## Implementation Steps

### Step 1: Data Preparation
- Collect multi-site resting-state fMRI datasets (e.g., ABIDE-I, ABIDE-II, ADHD-200)
- Preprocess data using standard pipelines (motion correction, normalization, etc.)
- Extract time series from brain regions of interest (ROIs)

### Step 2: Dynamic FC Computation
- Compute sliding-window correlation matrices for each subject
- Stack correlation matrices into 3D dFC tensors (time × ROI × ROI)
- Apply Fisher z-transformation for normality

### Step 3: Modularity-Guided Tucker Decomposition
- Identify modular structure in brain networks using community detection
- Apply Tucker decomposition guided by modular constraints
- Extract low-dimensional representations preserving spatio-temporal patterns

### Step 4: Federated Learning Setup
- Initialize global model parameters
- Distribute model to participating sites
- Ensure compliance with privacy regulations and data governance

### Step 5: Local Training and Prototype Generation
- Each site trains local model on its data
- Generate class-specific prototypes from local representations
- Apply site-specific normalization if needed

### Step 6: Global Aggregation with OT Barycenter
- Collect prototypes from all sites
- Compute OT barycenter to align prototypes globally
- Apply Procrustes analysis for additional alignment refinement
- Update global model with aligned prototypes

### Step 7: Model Evaluation
- Evaluate on held-out test sets from each site
- Assess performance on diagnostic tasks (ASD, ADHD detection)
- Compare against state-of-the-art methods

## Performance Characteristics
- **Accuracy**: Outperforms state-of-the-art methods in ASD and ADHD detection
- **Robustness**: Handles statistical heterogeneity across sites effectively
- **Privacy**: Maintains data privacy through federated learning
- **Scalability**: Supports multiple sites and large datasets

## Use Cases
- Multi-site neuroimaging consortia (ABIDE, ADHD-200, etc.)
- Privacy-preserving brain disorder diagnosis
- Federated analysis of dynamic brain networks
- Cross-site biomarker discovery for neurological disorders

## Limitations and Considerations
- Requires sufficient data at each site for meaningful local training
- Computational overhead from OT barycenter computation
- May need adaptation for non-fMRI modalities
- Assumes consistent preprocessing across sites

## References
- Girish, D., Chan, Y. H., Zheng, Y., Gupta, S., & Rajapakse, J. C. (2026). FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity. arXiv:2608.07393
- DOI: https://doi.org/10.48550/arXiv.2608.07393

## Activation Keywords
FedDOSE, federated learning, dynamic functional connectivity, fMRI, site effects, Tucker decomposition, optimal transport, brain networks, multi-site analysis