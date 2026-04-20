---
name: brain-foundation-model-batch-effects
description: "Batch effects analysis in brain foundation model embeddings — evaluating whether foundation models capture neurobiological signals vs scanner/protocol artifacts. Identifies and calibrates site-specific biases in fMRI embeddings. Activation: batch effects, fmri harmonization, foundation model calibration, site effects, neuroimaging bias."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Batch Effects In Brain Foundation Model Embeddings (arXiv:2604.14441)"
    tags: [neuroscience, fmri, foundation-model, batch-effects, harmonization]
---

# Batch Effects in Brain Foundation Model Embeddings

## Source Paper
- **Title**: Batch Effects In Brain Foundation Model Embeddings
- **arXiv**: 2604.14441
- **PDF**: https://arxiv.org/pdf/2604.14441

## Overview

Foundation models show strong potential for large-scale, high-dimensional biomedical applications, yet their ability to capture relevant neurobiological signals vs scanner and protocol artifacts remains poorly understood. This paper systematically analyzes **batch effects in brain foundation model embeddings**, showing how site-specific biases can dominate learned representations and proposing calibration methods.

## Core Concepts

### Batch Effect Sources in fMRI
- **Scanner differences**: Field strength (1.5T vs 3T vs 7T), manufacturer
- **Protocol variations**: TR, TE, resolution, slice order
- **Preprocessing pipelines**: Different motion correction, normalization
- **Population differences**: Age, demographics, health status

### Embedding Analysis Framework
1. Extract embeddings from foundation model for multi-site data
2. Quantify variance explained by site vs biology
3. Use ComBat-style harmonization on embedding space
4. Evaluate downstream task performance before/after calibration

### Key Findings
- Site effects can explain >30% of embedding variance
- Biological signals are often weaker than scanner artifacts
- Harmonization in embedding space is more effective than raw data
- Foundation models trained on diverse data reduce but don't eliminate batch effects

## Implementation Pattern

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class BatchEffectAnalyzer:
    """Analyze and correct batch effects in brain embeddings."""
    
    def __init__(self, embeddings, site_labels, bio_labels=None):
        self.embeddings = embeddings  # N x D
        self.sites = site_labels  # N
        self.bio_labels = bio_labels  # N (optional biological labels)
    
    def quantify_batch_effects(self):
        """Quantify variance explained by site vs biology."""
        from sklearn.linear_model import LinearRegression
        
        # One-hot encode sites
        unique_sites = np.unique(self.sites)
        site_onehot = np.eye(len(unique_sites))[
            np.searchsorted(unique_sites, self.sites)
        ]
        
        # Fit model: embeddings ~ sites
        model = LinearRegression().fit(site_onehot, self.embeddings)
        predicted = model.predict(site_onehot)
        residuals = self.embeddings - predicted
        
        # Variance explained by site
        var_total = np.var(self.embeddings, axis=0).sum()
        var_site = np.var(predicted, axis=0).sum()
        var_residual = np.var(residuals, axis=0).sum()
        
        return {
            'site_variance_ratio': var_site / var_total,
            'residual_variance_ratio': var_residual / var_total,
            'site_effect_size': np.sqrt(var_site / var_residual)
        }
    
    def combat_harmonize(self, bio_covariates=None):
        """Apply ComBat-style harmonization to embeddings."""
        unique_sites = np.unique(self.sites)
        harmonized = np.zeros_like(self.embeddings)
        
        # Grand mean across all sites
        grand_mean = np.mean(self.embeddings, axis=0)
        
        for site in unique_sites:
            mask = self.sites == site
            site_data = self.embeddings[mask]
            
            # Site-specific mean and variance
            site_mean = np.mean(site_data, axis=0)
            site_var = np.var(site_data, axis=0)
            
            # Shrinkage estimation (simplified)
            pooled_var = np.var(self.embeddings, axis=0)
            gamma = len(site_data) / (len(site_data) + 1)
            adjusted_var = gamma * site_var + (1-gamma) * pooled_var
            
            # Harmonize
            harmonized[mask] = (site_data - site_mean) / np.sqrt(adjusted_var + 1e-8)
            harmonized[mask] *= np.sqrt(pooled_var)
            harmonized[mask] += grand_mean
        
        return harmonized
    
    def visualize_batch_effects(self, n_components=2):
        """PCA visualization of batch effects."""
        pca = PCA(n_components=n_components)
        reduced = pca.fit_transform(self.embeddings)
        return reduced, pca.explained_variance_ratio_
```

## Calibration Pipeline
1. **Pre-training**: Train foundation model on diverse multi-site data
2. **Embedding extraction**: Get embeddings for new data
3. **Batch effect quantification**: Measure site variance
4. **Harmonization**: Apply ComBat or neural harmonization
5. **Downstream evaluation**: Verify task performance improvement

## Applications
- **Multi-site studies**: Harmonizing fMRI across hospitals
- **Clinical deployment**: Ensuring model generalization across scanners
- **Foundation model evaluation**: Assessing biological signal quality
- **Data sharing**: Cross-institutional collaboration

## Related Skills
- [[brain-dit-fmri-foundation-model]]
- [[brain-mri-foundation-clinical]]
- [[brain-network-controllability]]
