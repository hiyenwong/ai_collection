---
name: multi-view-o-information-brain-dynamics
description: Multi-view O-Information framework for higher-order brain dynamics — synergy and redundancy analysis in neural time series. Quantifies how groups of 3+ brain regions jointly encode information beyond pairwise interactions. Use when: brain network analysis beyond pairwise connectivity, information-theoretic neuroscience, synergy-redundancy decomposition, multi-region neural coding, higher-order functional connectivity, fMRI/EEG information analysis, cognitive task decoding, brain network complexity metrics. Activation: O-Information, synergy redundancy, higher-order information, multi-view information theory, brain information decomposition, neural coding synergy, redundant information, multi-region neural interactions.
version: 1.0.0
metadata:
  hermes:
    tags: [information-theory, brain-dynamics, synergy, redundancy, higher-order, fMRI, neural-coding, multi-view]
    source_paper: "Multi-View O-Information: A Framework for Synergy and Redundancy Analysis (arXiv:2504.19143)"
    date: 2025-04-28
---

# Multi-View O-Information Framework for Brain Dynamics

## Overview

O-Information decomposes the information in neural time series into synergistic and redundant components:
- **Synergy**: Information only available from the joint activity of 3+ regions (not from any subset)
- **Redundancy**: Information duplicated across multiple regions (available from any single region)

This framework goes beyond pairwise connectivity to capture genuine higher-order interactions in brain networks.

**Source Paper**: Multi-View O-Information (arXiv:2504.19143, 2025-04-28)

## Key Concepts

### O-Information Decomposition

The total shared information can be partitioned:
- **Redundant info**: What multiple regions carry about the same variable independently
- **Synergistic info**: What only emerges when multiple regions are considered together

### Multi-View Extension

Standard O-Information analyzes single sets of variables. Multi-view O-Information extends this to:
- Analyze information flow between different brain views/conditions
- Compare synergy/redundancy across task states
- Identify brain regions that serve as information integrators vs broadcasters

## Implementation Pattern

```python
import numpy as np
from itertools import combinations
from scipy.special import digamma

def o_information(X):
    """
    Compute O-Information for a set of variables.
    
    Args:
        X: Array of shape (n_samples, n_variables)
    
    Returns:
        Omega: O-Information value
        Positive = redundancy-dominated, Negative = synergy-dominated
    """
    n_vars = X.shape[1]
    
    # Estimate entropies using k-NN
    def entropy(data):
        n, d = data.shape
        # Simple Gaussian entropy estimator
        cov = np.cov(data.T)
        return 0.5 * d * (1 + np.log(2 * np.pi)) + 0.5 * np.log(np.linalg.det(cov) + 1e-10)
    
    # Total correlation decomposition
    omega = 0
    for k in range(1, n_vars + 1):
        sign = (-1) ** (k + 1)
        for combo in combinations(range(n_vars), k):
            subset = X[:, list(combo)]
            h = entropy(subset)
            omega += sign * h
    
    return omega


def compute_pairwise_o_info(X, n_regions=10):
    """
    Compute pairwise O-Information matrix between brain regions.
    Identifies which region pairs show synergy vs redundancy.
    """
    omega_matrix = np.zeros((n_regions, n_regions))
    
    for i in range(n_regions):
        for j in range(n_regions):
            if i != j:
                pair_data = X[:, [i, j]]
                omega_matrix[i, j] = o_information(pair_data)
    
    return omega_matrix


def identify_synergy_hubs(X, n_regions=10, k=3):
    """
    Find brain regions that serve as synergy hubs — 
    regions whose joint activity with others creates synergistic information.
    """
    synergy_scores = np.zeros(n_regions)
    
    for combo in combinations(range(n_regions), k):
        subset = X[:, list(combo)]
        omega = o_information(subset)
        if omega < 0:  # Synergy-dominated
            for region in combo:
                synergy_scores[region] += abs(omega)
    
    return synergy_scores
```

## Applications

- **Brain network analysis**: Identify hub regions in higher-order networks
- **Task state decoding**: Compare synergy/redundancy across cognitive tasks
- **Neurological biomarkers**: Detect altered higher-order connectivity in disease
- **Information flow**: Track how information propagates through brain networks

## Related Skills

- brain-higher-order-structures — Higher-order brain network analysis
- hermes-brain-connectivity — Brain connectivity analysis toolkit
- entropy-brain-connectivity-paths — Entropy-based connectivity analysis
