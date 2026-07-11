---
name: corsw-sliced-wasserstein-eeg-decoding
description: "Correlation Sliced-Wasserstein (CorSW) framework for EEG decoding with domain generalization. Use when: (1) EEG cross-subject/cross-session decoding with distribution shifts, (2) Scale-invariant correlation matrix representations for BCI, (3) Pullback Euclidean Metric Sliced Wasserstein on manifold geometries, (4) Domain generalization for EEG classification tasks. Triggers: CorSW, EEG decoding, correlation matrix, sliced Wasserstein, domain generalization, BCI, cross-subject, distribution shift."
license: Complete terms in LICENSE.txt
---

# Correlation Sliced-Wasserstein (CorSW) for EEG Decoding

arXiv:2606.06104 - Accepted by KDD 2026

## Core Innovation

**CorSW** introduces a Pullback Euclidean Metric Sliced Wasserstein (PEMSW) framework on the manifold of full-rank correlation matrices, enabling scale-invariant EEG decoding with improved domain generalization.

### Key Components

1. **Manifold Geometry**: Two correlation geometries - Off-Log Metric (OLM) and Log-Scaled Metric (LSM)
2. **PEMSW Framework**: Sliced Wasserstein discrepancies adapted to correlation manifolds via pullback metrics
3. **Domain Generalization**: Robust cross-subject/cross-session transfer under distribution shifts

## Implementation Guide

### 1. Correlation Matrix Representation

```python
import numpy as np
from scipy.linalg import sqrtm

def compute_correlation_matrix(eeg_data):
    """
    Compute scale-invariant correlation matrix from EEG covariance.
    
    Args:
        eeg_data: (n_samples, n_channels) or (n_trials, n_samples, n_channels)
    
    Returns:
        R: Full-rank correlation matrix (n_channels, n_channels)
    """
    # Compute covariance
    cov = np.cov(eeg_data.T)
    
    # Convert to correlation (scale-invariant)
    std = np.sqrt(np.diag(cov))
    R = cov / (std[:, None] * std[None, :])
    
    return R
```

### 2. Pullback Euclidean Metric Operations

```python
def off_log_metric(R):
    """
    Off-Log Metric (OLM) correlation geometry.
    Maps correlation matrix to Euclidean space via pullback.
    """
    # Regularize to ensure positive definiteness
    R_reg = R + 1e-6 * np.eye(R.shape[0])
    
    # Log transformation
    R_sqrt = sqrtm(R_reg)
    log_R = np.log(R_sqrt + 1e-6)
    
    return log_R

def log_scaled_metric(R):
    """
    Log-Scaled Metric (LSM) correlation geometry.
    Alternative pullback metric for correlation manifold.
    """
    R_reg = R + 1e-6 * np.eye(R.shape[0])
    
    # Scaled log transformation
    diag_sqrt = np.sqrt(np.diag(R_reg))
    R_scaled = R_reg / (diag_sqrt[:, None] * diag_sqrt[None, :])
    
    return np.log(R_scaled + 1e-6)
```

### 3. Sliced Wasserstein Distance

```python
def sliced_wasserstein_correlation(R1, R2, n_projections=100, metric='OLM'):
    """
    Compute Sliced Wasserstein distance between correlation matrices.
    
    Args:
        R1, R2: Correlation matrices
        n_projections: Number of random projections for slicing
        metric: 'OLM' or 'LSM'
    
    Returns:
        SW_distance: Sliced Wasserstein distance on correlation manifold
    """
    # Map to Euclidean space via pullback
    if metric == 'OLM':
        X1 = off_log_metric(R1).flatten()
        X2 = off_log_metric(R2).flatten()
    else:
        X1 = log_scaled_metric(R1).flatten()
        X2 = log_scaled_metric(R2).flatten()
    
    # Random projections for slicing
    d = len(X1)
    distances = []
    
    for _ in range(n_projections):
        # Random projection vector
        theta = np.random.randn(d)
        theta = theta / np.linalg.norm(theta)
        
        # Project onto 1D
        proj1 = np.dot(X1, theta)
        proj2 = np.dot(X2, theta)
        
        # Sort projections
        proj1_sorted = np.sort(proj1)
        proj2_sorted = np.sort(proj2)
        
        # 1D Wasserstein distance
        wd = np.mean(np.abs(proj1_sorted - proj2_sorted))
        distances.append(wd)
    
    return np.mean(distances)
```

### 4. Domain Generalization Framework

```python
class CorSWDGModel:
    """
    Domain Generalization model using CorSW for EEG decoding.
    """
    
    def __init__(self, n_channels, n_classes, metric='OLM'):
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.metric = metric
        
    def extract_features(self, eeg_data):
        """
        Extract correlation-based features with pullback metric.
        """
        R = compute_correlation_matrix(eeg_data)
        
        if self.metric == 'OLM':
            features = off_log_metric(R).flatten()
        else:
            features = log_scaled_metric(R).flatten()
        
        return features
    
    def domain_align(self, source_features, target_features):
        """
        Align source domain to target domain via SW minimization.
        """
        # Compute domain shift via SW distance
        shift = sliced_wasserstein_correlation(
            np.eye(self.n_channels), 
            np.cov(target_features.T),
            metric=self.metric
        )
        
        # Apply domain correction
        aligned = source_features - shift * np.mean(target_features)
        
        return aligned
```

## Experimental Results

- **Three EEG datasets**: Enhanced generalization under distribution shifts
- **Training overhead**: Low (no additional inference cost)
- **Performance**: Superior to covariance-based methods
- **Code**: https://github.com/ChenHu-ML/CorSW

## Key Advantages

1. **Scale-Invariant**: Robust to channel-wise scaling variations
2. **Manifold-Aware**: Preserves correlation geometry structure
3. **Domain Generalization**: Improved cross-subject/cross-session transfer
4. **Efficient**: Sliced Wasserstein reduces computational complexity

## Applications

- Cross-subject BCI decoding
- Cross-session EEG classification
- Domain-shift robust EEG analysis
- Motor imagery classification
- Emotion recognition from EEG
- Clinical EEG diagnostics

## Activation Keywords

- CorSW
- EEG decoding
- correlation matrix
- sliced Wasserstein
- domain generalization
- BCI
- cross-subject decoding
- correlation geometry
- pullback metric
- Off-Log Metric
- Log-Scaled Metric