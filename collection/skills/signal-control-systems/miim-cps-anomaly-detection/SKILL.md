---
name: miim-cps-anomaly-detection
description: >
  Joint latent clustering anomaly detection for multimodal cyber-physical systems
  (CPS). Models normal behaviour under the MIIM assumption set (Massive, Implicit,
  Imbalanced Multimodality) with explicit Gaussian-mixture mode clustering in latent
  space, scored without reconstruction residuals. Includes difficulty-stratified
  fair evaluation protocol with raw point-wise metrics, trivial-detector splits,
  and prevalence-matched F1.
category: systems-engineering
tags: [cps, anomaly-detection, miim, latent-clustering, systems-engineering, control-systems]
source: arxiv:2607.06094
date: 2026-07-09
---

# MIIM: Joint Latent Clustering for CPS Anomaly Detection

## Paper

- **Title**: Modeling Normal Is All You Need: Joint Latent Clustering for Anomaly Detection in Multimodal Cyber-Physical Systems
- **Authors**: Alexander Apartsin, Yehudit Aperstein
- **arXiv**: [2607.06094](https://arxiv.org/abs/2607.06094)
- **Date**: 2026-07-09
- **Category**: cs.LG (applied to CPS anomaly detection)

## Problem

CPS faults are too rare and unrepresentative to characterize directly, so detection must model normal behaviour. However:
- Normal CPS behaviour is a union of **many imbalanced, curved, thin-fringed operating regimes** (not a single blob)
- Standard point-adjusted evaluation rewards detectors that never learn meaningful models
- Deep detectors (USAD, TranAD, GDN) collapse on difficult correlation/dynamics faults

## MIIM Assumption Set (A1–A10)

**MIIM = Massive, Implicit, Imbalanced Multimodality**

1. **Massive**: Normal behaviour spans many operating regimes (not one blob)
2. **Implicit**: Regimes are not pre-labeled; must be discovered from data
3. **Imbalanced**: Some regimes dominate; minority regimes are thin-fringed
4. **Curved**: Regimes are nonlinear manifolds, not linear subspaces
5. **Thin-fringed**: Boundaries between regimes are sharp
6. **Temporal**: Temporal dynamics and cross-variable correlations are key fault signatures
7. **Point-adjustment bias**: Standard evaluation inflates scores by grouping adjacent anomalies
8. **Prevalence mismatch**: Fault prevalence in test data differs from training
9. **Trivial detector baseline**: Simple threshold detectors should be outperformed
10. **Calibration requirement**: Detectors must calibrate on train-normal-only data

## Core Methodology

### 1. Joint Latent Representation + GMM Clustering

```
Data → Encoder → Latent Space → Gaussian Mixture Model → Anomaly Score
```

- Learn a latent representation jointly with explicit Gaussian-mixture mode clustering
- Score anomalies **in latent space** (not by global density or reconstruction residual)
- **Key insight**: A flexible decoder rebuilds hard faults faithfully, so reconstruction residuals are unreliable

### 2. Latent-Only Scoring

- Drop reconstruction entirely — flexible decoders faithfully reconstruct even hard faults
- Score based on distance from GMM components in latent space
- Components capture the multiple normal operating regimes (MIIM structure)

### 3. Fair Evaluation Protocol

- **Raw point-wise metrics**: No point adjustment (avoid inflating scores)
- **Trivial-detector difficulty split**: Separate easy vs. hard faults
- **Prevalence-matched F1**: Account for class imbalance
- **Train-normal-only calibration**: Detectors trained only on normal data

## Implementation Pattern

```python
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

class MIIMDetector:
    """Joint latent clustering anomaly detector for multimodal CPS."""
    
    def __init__(self, latent_dim=32, n_components=10, window=60):
        self.latent_dim = latent_dim
        self.n_components = n_components
        self.window = window
        self.encoder = None  # Train encoder jointly with GMM
        self.gmm = None
        self.scaler = StandardScaler()
    
    def _extract_windows(self, data):
        """Extract sliding windows from multivariate time series."""
        windows = []
        for i in range(len(data) - self.window + 1):
            windows.append(data[i:i+self.window].flatten())
        return np.array(windows)
    
    def fit(self, normal_data):
        """Fit on normal-only data."""
        # Scale and extract windows
        scaled = self.scaler.fit_transform(normal_data)
        windows = self._extract_windows(scaled)
        
        # Joint training: encoder + GMM (alternating optimization)
        # Phase 1: Initialize encoder (e.g., autoencoder trained on normal)
        # Phase 2: Fit GMM on latent representations
        # Phase 3: Alternate between encoder updates and GMM updates
        latent = self._encode(windows)
        self.gmm = GaussianMixture(
            n_components=self.n_components,
            covariance_type='full',
            n_init=10
        ).fit(latent)
        return self
    
    def _encode(self, windows):
        """Encode windows to latent space."""
        # Replace with actual encoder (autoencoder, transformer, etc.)
        from sklearn.decomposition import PCA
        pca = PCA(n_components=self.latent_dim)
        return pca.fit_transform(windows)
    
    def score(self, data):
        """Compute anomaly scores for each time step."""
        scaled = self.scaler.transform(data)
        windows = self._extract_windows(scaled)
        latent = self._encode(windows)
        
        # Negative log-likelihood under GMM (lower = more anomalous)
        scores = -self.gmm.score_samples(latent)
        
        # Expand window scores back to point-wise scores
        point_scores = np.zeros(len(data))
        counts = np.zeros(len(data))
        for i, score in enumerate(scores):
            for j in range(i, i + self.window):
                if j < len(data):
                    point_scores[j] += score
                    counts[j] += 1
        return point_scores / np.maximum(counts, 1)
    
    def evaluate(self, scores, labels, threshold=None):
        """Fair evaluation: raw metrics, no point adjustment."""
        from sklearn.metrics import roc_auc_score, f1_score
        
        if threshold is None:
            # Use prevalence-matched threshold
            threshold = np.percentile(scores, 95)
        
        predictions = (scores > threshold).astype(int)
        
        # Raw point-wise AUROC
        auroc = roc_auc_score(labels, scores)
        
        # Raw point-wise F1
        f1 = f1_score(labels, predictions)
        
        return {'auroc': auroc, 'f1': f1, 'threshold': threshold}
```

## Performance (Paper Results)

| Dataset | Difficult AUROC | Easy AUROC |
|---------|----------------|------------|
| HAI | 0.831 | — |
| WADI | 0.726 | — |
| SKAB | 0.610 | — |

Margin is largest on multimodal datasets (HAI, WADI) and slimmest on near-unimodal (SKAB), tracking MIIM assumptions.

## Key Insights for Systems Engineering

1. **Reconstruction is not reliable for CPS anomaly detection**: Flexible decoders can reconstruct hard faults, making residual-based scoring ineffective
2. **Multimodality must be modeled explicitly**: CPS normal behaviour is not a single distribution — it's a union of many operating regimes
3. **Fair evaluation matters**: Standard point-adjusted metrics hide detector failures; raw point-wise metrics with difficulty splits reveal true performance
4. **Latent space scoring > reconstruction**: Score anomalies by their position in the learned latent space relative to GMM components

## Activation Keywords

cps anomaly detection, miim, multimodal anomaly, latent clustering, cyber-physical systems, anomaly detection, gaussian mixture model, system monitoring, fault detection, industrial iot anomaly, water distribution monitoring, power grid anomaly
