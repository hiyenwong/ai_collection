---
name: distribution-based-brain-connectivity
description: "Distribution-valued brain connectivity analysis using vector quantiles instead of scalar edge weights. Based on Mhanna, Achard, Petersen (2026, HAL). Use when building brain connectivity graphs from fMRI/EEG, improving connectome classification, or representing higher-order connectivity statistics. Activation: distribution-valued brain connectivity, graph brain representation, fMRI connectome classification, voxel clustering, brain network edges, vector quantile connectivity."
---

# Distribution-Based Brain Connectivity

Represent brain connectivity graphs with distribution-valued edges (vector quantiles) instead of scalar Pearson correlation weights, capturing richer connectivity information from fMRI data.

## Problem with Standard Approach

Traditional pipeline:
1. Parcellate brain into ROIs
2. Compute Pearson correlation between ROI time series → scalar edge weight
3. Build weighted graph → classify

**Limitation**: Scalar correlation discards the full distribution of voxel-level interactions within each ROI pair.

## Distribution-Valued Edges

Instead of a single scalar weight wᵢⱼ for each edge (i,j), use a vector of quantiles:

```
qᵢⱼ = [Q(p₁), Q(p₂), ..., Q(pₖ)]
```

where Q(p) is the p-th quantile of the distribution of all voxel-pair correlations between ROI i and ROI j.

### Computation Pipeline

```python
import numpy as np
from scipy.stats import mstats

def distribution_valued_connectivity(fmri_data, atlas, quantiles=None):
    """Compute distribution-valued brain connectivity.
    
    Args:
        fmri_data: (n_timepoints, n_voxels) BOLD signal
        atlas: (n_voxels,) ROI assignment for each voxel
        quantiles: array of quantile levels, e.g. [0.1, 0.25, 0.5, 0.75, 0.9]
    
    Returns:
        edges: (n_roi, n_roi, n_quantiles) distribution-valued connectivity
    """
    if quantiles is None:
        quantiles = np.array([0.1, 0.25, 0.5, 0.75, 0.9])
    
    roi_ids = np.unique(atlas)
    n_roi = len(roi_ids)
    n_q = len(quantiles)
    edges = np.zeros((n_roi, n_roi, n_q))
    
    for i, ri in enumerate(roi_ids):
        for j, rj in enumerate(roi_ids):
            if i >= j:
                continue
            # Get voxel signals for each ROI
            vox_i = fmri_data[:, atlas == ri]  # (T, n_vox_i)
            vox_j = fmri_data[:, atlas == rj]  # (T, n_vox_j)
            
            # All pairwise correlations
            n_vi, n_vj = vox_i.shape[1], vox_j.shape[1]
            corrs = np.zeros(n_vi * n_vj)
            idx = 0
            for vi in range(n_vi):
                for vj in range(n_vj):
                    corrs[idx] = np.corrcoef(vox_i[:, vi], vox_j[:, vj])[0, 1]
                    idx += 1
            
            # Quantile representation
            edges[i, j] = np.quantile(corrs, quantiles)
            edges[j, i] = edges[i, j]
    
    return edges
```

### Voxel Clustering Estimator

For computational efficiency with large voxel counts:

```python
from sklearn.cluster import KMeans

def voxel_cluster_connectivity(fmri_data, atlas, n_clusters=20):
    """Efficient distribution-valued connectivity via voxel clustering."""
    roi_ids = np.unique(atlas)
    n_roi = len(roi_ids)
    
    cluster_profiles = []
    for roi in roi_ids:
        vox_signals = fmri_data[:, atlas == roi]
        # Cluster voxels by temporal profile
        kmeans = KMeans(n_clusters=min(n_clusters, vox_signals.shape[1]))
        labels = kmeans.fit_predict(vox_signals.T)
        cluster_profiles.append(vox_signals)
    
    # Compute correlations between cluster representatives
    # ...
```

## Classification with Distribution-Valued Edges

Standard graph kernels / GNNs expect scalar edges. For distribution-valued edges:

1. **Vectorize**: Flatten quantile vectors → feature per edge
2. **Kernel methods**: Use Wasserstein kernel or sliced Wasserstein distance
3. **GNN adaptation**: Message passing on distribution-valued edges

```python
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

def classify_brain_connectivity(dist_edges, labels):
    """Classification with distribution-valued connectivity."""
    n_subjects = dist_edges.shape[0]
    n_roi = dist_edges.shape[1]
    n_q = dist_edges.shape[2]
    
    # Flatten upper triangle of each subject's connectivity
    triu_idx = np.triu_indices(n_roi, k=1)
    X = dist_edges[:, triu_idx[0], triu_idx[1], :]  # (N, n_edges, n_q)
    X = X.reshape(n_subjects, -1)  # (N, n_edges * n_q)
    
    clf = Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='rbf', C=1.0))
    ])
    
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(clf, X, labels, cv=5)
    return scores
```

## Advantages Over Scalar Weights

| Property | Scalar Correlation | Distribution-Valued |
|----------|-------------------|-------------------|
| Information | Single summary | Full distribution shape |
| Sensitivity | Outlier-sensitive | Robust via quantiles |
| Heterogeneity | Assumes homogeneity | Captures within-ROI variance |
| Classification | Moderate | Improved |

## Pitfalls

- Computationally expensive: O(n_vox_i × n_vox_j) per ROI pair
- Voxel clustering approximation trades accuracy for speed
- Choice of quantile levels affects discriminative power
- Standard GNN architectures need adaptation for distribution-valued edges
- Small sample sizes may lead to overfitting with high-dimensional feature vectors

## Reference

- Mhanna, R., Achard, S., & Petersen, A. (2026). Distribution-based brain connectivity graph representations for classification. HAL.
