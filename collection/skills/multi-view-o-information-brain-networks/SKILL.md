---
name: multi-view-o-information-brain-networks
description: >
  Higher-order brain interaction analysis using O-information integrated with Multi-View
  Information Bottleneck (MVIB) framework for fMRI-based psychiatric diagnosis. Characterizes
  synergy vs redundancy in 3+ brain region interactions. Use when: analyzing higher-order
  brain interactions (HOIs), fMRI psychiatric diagnosis (MDD, ASD, AD), O-information computation,
  multi-view information bottleneck, synergy-redundancy decomposition, hypergraph brain networks,
  brain connectivity beyond pairwise.
  Activation: O-information, higher-order brain interactions, HOIs, multi-view information bottleneck,
  MVIB, synergy redundancy brain, fMRI diagnosis, triadic brain interactions, hypergraph fMRI.
version: 1.0.0
metadata:
  hermes:
    tags: [brain-networks, higher-order, O-information, information-bottleneck, fmri, psychiatric-diagnosis, synergy, redundancy]
    source_paper: "Modeling Higher-Order Brain Interactions via a Multi-View Information Bottleneck Framework for fMRI-based Psychiatric Diagnosis (arXiv:2604.17713)"
    date: 2026-04-20
---

# Multi-View O-Information for Higher-Order Brain Networks

## Overview

Most brain connectivity analysis stops at pairwise (functional) connectivity, missing higher-order
interactions (HOIs) among 3+ regions that are central to complex brain dynamics. This skill provides
methodology for computing and integrating O-information — a signed measure characterizing whether
multi-region interactions are synergy-dominated (information emerges only from joint observation)
or redundancy-dominated (information is shared across regions).

**Source Paper**: Zhang et al., "Modeling Higher-Order Brain Interactions via a Multi-View Information
Bottleneck Framework for fMRI-based Psychiatric Diagnosis" (arXiv:2604.17713, 2026-04-20)

## Core Concepts

### O-Information

O-information is a signed information-theoretic measure:
- **Positive O-info**: Redundancy-dominated — regions share common information
- **Negative O-info**: Synergy-dominated — joint observation reveals more than sum of parts
- Computed for 3rd-order (triadic) and 4th-order (tetradic) interactions

### Multi-View Information Bottleneck (MVIB)

Three-view architecture:
1. **Pairwise view** — standard functional connectivity matrices
2. **Triadic view** — 3rd-order O-information tensors
3. **Tetradic view** — 4th-order O-information tensors

Each view is compressed via IB principle to extract diagnosis-relevant features while
penalizing redundancy between views.

## Computational Methods

### Accelerated O-Information Estimation

Two acceleration strategies for scalable computation:

#### 1. Gaussian Analytical Approximation
For multivariate Gaussian data, O-info has closed-form expression via covariance matrix determinants:
Ω(X₁,...,Xₙ) = ΣᵢH(Xᵢ) - H(X₁,...,Xₙ) - (n-2)·I(X₁;...;Xₙ)

Where H is differential entropy computable from log-determinant of covariance.

#### 2. Randomized Matrix-based Rényi Entropy
Matrix-based Rényi entropy estimator with random projections achieves 30× speedup vs
conventional kNN-based estimators while preserving accuracy.

## Implementation Pattern

```python
import numpy as np
from itertools import combinations
from scipy.linalg import slogdet

def o_information_gaussian(cov_matrix, indices):
    """
    Compute O-information for a subset of variables assuming Gaussian distribution.
    
    Args:
        cov_matrix: Full covariance matrix (n_regions x n_regions)
        indices: Tuple of region indices for the interaction
    
    Returns:
        O-information value (positive=redundancy, negative=synergy)
    """
    sub_cov = cov_matrix[np.ix_(indices, indices)]
    n = len(indices)
    
    # Individual entropies
    individual_entropies = sum(
        0.5 * np.log(2 * np.pi * np.e * cov_matrix[i, i])
        for i in indices
    )
    
    # Joint entropy
    _, log_det = slogdet(sub_cov)
    joint_entropy = 0.5 * (n * np.log(2 * np.pi * np.e) + log_det)
    
    # Total correlation
    total_correlation = individual_entropies - joint_entropy
    
    # O-information = (n-2)·TC - sum of (n-1)-order TCs
    # Simplified for third order: Ω = ΣH(Xi) + H(X1,X2,X3) - ΣH(Xi,Xj)
    if n == 3:
        pairwise_tc = sum(
            0.5 * np.log(cov_matrix[i,i] * cov_matrix[j,j] / 
                        (cov_matrix[i,i] * cov_matrix[j,j] - cov_matrix[i,j]**2 + 1e-10))
            for i, j in combinations(indices, 2)
        )
        return total_correlation - pairwise_tc
    
    return total_correlation  # Simplified for higher orders

def compute_higher_order_features(fmri_timeseries, order=3):
    """
    Compute O-information for all combinations of given order.
    
    Args:
        fmri_timeseries: (n_regions, n_timepoints)
        order: Interaction order (3 for triadic, 4 for tetradic)
    
    Returns:
        Dictionary mapping region combinations to O-information values
    """
    n_regions = fmri_timeseries.shape[0]
    cov = np.cov(fmri_timeseries)
    
    results = {}
    for combo in combinations(range(n_regions), order):
        results[combo] = o_information_gaussian(cov, combo)
    
    return results

def tri_view_ib_encoding(pairwise_features, triadic_features, tetradic_features, 
                          diagnosis_labels, beta=0.01):
    """
    Multi-view Information Bottleneck encoding.
    
    Compresses each view to maximize mutual information with diagnosis
    while minimizing mutual information between views.
    
    Args:
        pairwise_features: Standard FC features
        triadic_features: 3rd-order O-information features
        tetradic_features: 4th-order O-information features
        diagnosis_labels: Binary/multiclass diagnosis
        beta: Trade-off parameter for redundancy penalty
    
    Returns:
        Compressed multi-view representation
    """
    # Each view is encoded through its own encoder
    # IB objective: min Σ I(X_i; Z_i) - β·I(Z_i; Y) + γ·Σ I(Z_i; Z_j)
    # Implemented via variational approximation
    pass
```

## Key Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| order | HOI order to compute | 3 (triadic), 4 (tetradic) |
| n_regions | Number of brain ROIs | 90 (AAL), 200 (Schaefer) |
| beta | IB redundancy penalty | 0.01 - 0.1 |
| speedup | Acceleration factor | ~30× vs kNN |

## Applications

- **Psychiatric diagnosis**: MDD, ASD, ADHD classification from resting-state fMRI
- **Neurodegenerative detection**: Alzheimer's disease (ADNI dataset)
- **Brain connectivity characterization**: Beyond pairwise FC to synergy-redundancy profiles
- **Feature selection**: Identify synergistic/redundant brain region groups

## Datasets Validated

- REST-meta-MDD (depression)
- ABIDE (autism)
- UCLA (ADHD)
- ADNI (Alzheimer's)

## Limitations

- Computationally expensive for large ROI counts (mitigated by acceleration strategies)
- Requires sufficient timepoints for reliable covariance estimation
- Gaussian approximation may miss non-linear dependencies

## Related Skills

- brain-graph-neural — GNN methods for brain connectivity
- task-aware-brain-connectivity — DAG-based effective connectivity
- higher-order-brain-networks — TDA-based higher-order analysis

