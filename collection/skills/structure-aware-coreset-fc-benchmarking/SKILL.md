---
name: structure-aware-coreset-fc-benchmarking
description: "Accelerating benchmarking of functional connectivity (FC) modeling via structure-aware coreset selection for large-scale fMRI datasets. Reduces combinatorial explosion in model-data evaluation pairs. Activation: functional connectivity, fMRI benchmarking, coreset selection, FC modeling, brain network analysis, connectomics benchmarking."
---

# Structure-aware Core-set Selection for FC Benchmarking

> Methodology for accelerating functional connectivity (FC) modeling benchmarking on large-scale fMRI datasets by selecting representative subject subsets (coresets) that preserve structural brain properties.

## Metadata
- **Source**: arXiv:2602.05667
- **Authors**: Ling Zhan, Zhen Li, Junjie Huang, et al.
- **Published**: 2026-02-05
- **Categories**: cs.LG

## Core Methodology

### Key Innovation
Addresses the combinatorial explosion problem in FC benchmarking: with hundreds of FC methods × thousands of subjects × multiple datasets, exhaustive evaluation is computationally prohibitive. The proposed structure-aware coreset selection identifies a small representative subset of subjects that preserves key brain network properties, enabling efficient yet reliable benchmarking.

### Technical Framework
1. **Coreset Selection**: Identify a representative subset of subjects from large fMRI datasets
2. **Structure-Awareness**: Preserve spatial brain structure (anatomical regions) and functional topology (network patterns) in the selection
3. **Evaluation Proxy**: Demonstrate that benchmarking on the coreset yields rankings consistent with full-dataset evaluation
4. **Scalability**: Reduce computational cost by orders of magnitude while maintaining benchmark validity

### Implementation Guide

#### Prerequisites
- Large-scale fMRI datasets (e.g., HCP, UK Biobank)
- FC estimation pipeline (partial correlation, regularized inverse covariance, etc.)
- Scikit-learn or similar for clustering/selection

#### Step-by-Step
1. Compute FC matrices for all subjects
2. Extract structural features (region-wise connectivity patterns, network topology metrics)
3. Apply structure-aware coreset selection (clustering + representative sampling)
4. Validate coreset by comparing FC method rankings against full-dataset rankings
5. Use coreset for rapid benchmarking of new FC methods

### Code Example
```python
import numpy as np
from sklearn.cluster import KMeans

def structure_aware_coreset(fc_matrices, n_select=50, n_clusters=10):
    """Select representative subjects preserving brain network structure."""
    n_subjects = fc_matrices.shape[0]
    # Flatten upper triangular FC values
    feats = np.array([mat[np.triu_indices_from(mat, k=1)] for mat in fc_matrices])
    # Cluster subjects by FC patterns
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(feats)
    # Proportionally sample from each cluster
    selected = []
    for c in range(n_clusters):
        idx = np.where(labels == c)[0]
        n_c = max(1, int(n_select * len(idx) / n_subjects))
        # Pick closest to cluster center
        dists = np.linalg.norm(feats[idx] - kmeans.cluster_centers_[c], axis=1)
        selected.extend(idx[np.argsort(dists)[:n_c]])
    return selected[:n_select]
```

## Applications
- **FC Method Comparison**: Rapid benchmarking of new FC estimation methods
- **Large-scale Studies**: Efficient analysis of biobank-scale datasets
- **Reproducibility**: Standardized benchmarking subsets for community comparison
- **Pipeline Optimization**: Quick evaluation of preprocessing choices

## Pitfalls
- Coreset may miss rare but important subject phenotypes
- Validation needed for each new dataset
- Trade-off between coreset size and ranking fidelity
- May not generalize across all FC metrics

## Related Skills
- brain-network-topology
- gaussian-graphical-connectivity-analysis
- functional-connectome-fingerprint
