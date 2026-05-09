---
name: multi-scale-info-geometry-neural
description: "Multi-scale information geometry framework for neural population coding. Derives unique Riemannian representational geometry from information contraction under coarse-graining, relating Fisher information metric to mutual information. Activation: neural coding geometry, Fisher information metric, neural population analysis, information geometry, mutual information neural, representational geometry"
---

# Multi-scale Information Geometry for Neural Populations

## Overview

This methodology establishes a **unique Riemannian representational geometry** on stimulus space, derived from first principles of how information distances contract under coarse-graining. The framework connects the geometry of neural population responses directly to **mutual information**, providing a principled way to characterize neural codes.

## Activation Keywords

- neural coding geometry
- Fisher information metric
- neural population analysis
- information geometry
- mutual information neural
- representational geometry
- neural code characterization
- diffusion model neural

## Key Problem

Existing approaches to neural representational geometry produce qualitatively different conclusions depending on how distances are constructed. There is no principled way to choose among competing constructions, and the relationship between geometry and information transmission is unclear.

## Core Methodology

### 1. Information Contraction Principle

The key insight: distances in stimulus space should contract as stimulus resolution is lost through coarse-graining. This principle **uniquely determines** the representational geometry.

```
Fine resolution --coarse-grain--> Coarse resolution
  (large distances)                  (contracted distances)
```

### 2. Multi-scale Fisher Information Metric

The framework produces a **multi-scale extension of the Fisher information metric**:

- **Fine scale**: Captures sensitivity to small stimulus perturbations
- **Coarse scale**: Captures global stimulus distinctions
- **Full spectrum**: All scales simultaneously encoded in the metric tensor

The metric tensor g_ij captures the local sensitivity of the neural response distribution to changes in stimulus parameters.

The multi-scale extension integrates over all coarse-graining levels.

### 3. Geometry-Mutual Information Relationship

The central result: **the metric tensor is exactly related to mutual information**.

- Well-encoded stimulus directions -> **expanded** in the geometry
- Poorly encoded directions -> **contracted**
- Eigenvectors of the metric tensor identify stimulus variations that contribute most to information transmission

### 4. Practical Estimation via Diffusion Models

The metric tensor can be estimated using **diffusion models**, making the framework applicable to:
- Large neural populations
- High-dimensional stimuli (natural images)
- Complex neural response distributions

### 5. Analysis Pipeline

```
1. Collect neural population responses to stimuli
2. Model conditional distribution p(neural_response | stimulus)
3. Estimate metric tensor via diffusion model
4. Compute eigendecomposition of metric tensor
5. Identify well-encoded stimulus directions (top eigenvectors)
6. Interpret eigenvectors as meaningful stimulus features
7. Validate robustness across modeling choices
```

## Key Findings from the Paper

- **Unique geometry**: Information contraction principle yields a unique Riemannian metric
- **Information encoding**: Metric eigenvalues directly relate to mutual information contribution
- **Natural image application**: Applied to visual cortical responses, eigenvectors yield interpretable features
- **Robustness**: Results robust to modeling choices
- **Practical**: Diffusion model estimation enables application to large populations

## Python Implementation Sketch

```python
import numpy as np
from scipy.linalg import eigh

def estimate_fisher_metric(neural_responses, stimuli, n_scales=10):
    """Estimate multi-scale Fisher information metric tensor."""
    stimulus_dim = stimuli.shape[1]
    multi_scale_metric = np.zeros((stimulus_dim, stimulus_dim))
    
    for scale in range(n_scales):
        # Coarse-grain stimuli at this scale
        coarse_stimuli = coarse_grain(stimuli, scale)
        
        # Estimate local Fisher information
        fisher = estimate_local_fisher(
            neural_responses, coarse_stimuli
        )
        
        # Weight by scale (finer scales get higher weight)
        weight = 1.0 / (scale + 1)
        multi_scale_metric += weight * fisher
    
    # Eigendecomposition
    eigenvalues, eigenvectors = eigh(multi_scale_metric)
    
    # Sort by eigenvalue (descending)
    idx = np.argsort(eigenvalues)[::-1]
    return multi_scale_metric, eigenvalues[idx], eigenvectors[:, idx]

def estimate_local_fisher(responses, stimuli, bandwidth=0.1):
    """Estimate Fisher information locally using score function."""
    n_dim = stimuli.shape[1]
    fisher = np.zeros((n_dim, n_dim))
    
    for i in range(len(stimuli) - 1):
        # Numerical gradient of log probability
        delta_s = stimuli[i+1] - stimuli[i]
        delta_r = responses[i+1] - responses[i]
        
        # Score function approximation
        score = delta_r / (np.linalg.norm(delta_r) + 1e-8)
        
        fisher += np.outer(score @ delta_s, score @ delta_s)
    
    return fisher / len(stimuli)

def coarse_grain(stimuli, scale):
    """Coarse-grain stimuli at given resolution scale."""
    sigma = 2 ** scale
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(stimuli, sigma=sigma, axis=0)

def interpret_eigenvectors(eigenvectors, stimulus_space):
    """Interpret metric eigenvectors as stimulus features."""
    features = []
    for vec in eigenvectors.T:
        # Project onto stimulus space to find meaningful features
        feature = project_to_interpretable(vec, stimulus_space)
        features.append(feature)
    return features
```

## Comparison to Existing Methods

| Method | Strength | Limitation |
|--------|----------|------------|
| RSA | Simple, widely used | No information-theoretic grounding |
| CCA | Captures linear relations | No geometric interpretation |
| Demixed PCA | Dimensionality reduction | Not uniquely determined |
| **Info Geometry** | **Unique, information-theoretic** | **Requires distribution modeling** |

## When to Use

- Characterizing neural population codes
- Identifying which stimulus features are best encoded
- Comparing encoding quality across brain regions
- Building principled representational geometries
- Analyzing high-dimensional neural data with natural stimuli

## Source

arXiv: 2605.06304 - "A multi-scale information geometry reveals the structure of mutual information in neural populations" by Simone Azeglio, Steeve Laquitaine, Ulisse Ferrari, Matthew Chalk (2026-05-07)

## Related Skills

- entropy-brain-connectivity-paths
- brain-dnn-transformation-alignment
- decoding-encoding-alignment-critique
