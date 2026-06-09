---
name: homology-morphometry-brain-atrophy
description: "Homology-based Morphometry (HBM) methodology for analyzing brain atrophy using persistent homology. Two complementary pipelines for quantifying multiscale geometric features of structural T1-weighted MRI scans: Pipeline 1 for regional thinning via Euclidean distance transform, Pipeline 2 for structural similarity via α-filtrations. Use for Alzheimer's disease detection, longitudinal brain change tracking, and topological biomarker extraction. Keywords: brain atrophy, persistent homology, TDA, MRI morphometry, Alzheimer's disease, topological biomarker."
---

# Homology-based Morphometry of Brain Atrophy

Homology-based Morphometry (HBM) is a topological data analysis framework for quantifying multiscale geometric features of structural T1-weighted MRI scans without requiring nonlinear registration to a standard template.

## Overview

Contemporary structural brain analysis relies on voxel-based morphometry (VBM) which requires normalization to a standard template, potentially obscuring subject-specific geometric features. HBM addresses this limitation using **persistent homology (PH)**, a tool from topological data analysis.

## Core Methodology

### Pipeline 1: Regional Thinning Analysis

**Purpose**: Quantify regional thinning via Euclidean distance transform

**Process**:
1. Apply Euclidean distance transform to tissue masks in a slice-wise manner
2. Capture regional thinning patterns
3. Best suited for **between-subject analyses**

**Key Applications**:
- Cross-sectional group comparisons
- Alzheimer's disease vs cognitively normal classification
- ROC-AUC = 0.895 on ADNI dataset

### Pipeline 2: Structural Similarity Analysis

**Purpose**: Measure structural similarity between pairs of scans

**Process**:
1. Use α-filtrations to capture multiscale geometric features
2. Detect sulcal widening and ventricular enlargement
3. Best suited for **within-subject designs**

**Key Applications**:
- Longitudinal change tracking
- Disease progression monitoring
- Follow-up scan comparison

## Methodological Advantages

| Feature | Traditional VBM | HBM (This Method) |
|---------|-----------------|-------------------|
| Registration | Required | Not required |
| Subject-specific features | May be obscured | Preserved |
| Pathological cases | Problematic | Handled robustly |
| Interpretability | Statistical | Topological |
| Multiscale analysis | Limited | Native support |

## Implementation Workflow

### Prerequisites

```python
import numpy as np
import gudhi  # For persistent homology
from scipy.ndimage import distance_transform_edt
import nibabel as nib
```

### Pipeline 1: Regional Thinning

```python
def pipeline1_regional_thinning(tissue_mask, slice_axis=2):
    """
    Quantify regional thinning using Euclidean distance transform
    
    Args:
        tissue_mask: Binary tissue mask (WM/GM segmentation)
        slice_axis: Axis for slice-wise processing (default: 2)
    
    Returns:
        Persistence diagrams for each slice
    """
    n_slices = tissue_mask.shape[slice_axis]
    persistence_diagrams = []
    
    for i in range(n_slices):
        # Extract slice
        if slice_axis == 0:
            slice_mask = tissue_mask[i, :, :]
        elif slice_axis == 1:
            slice_mask = tissue_mask[:, i, :]
        else:
            slice_mask = tissue_mask[:, :, i]
        
        # Apply Euclidean distance transform
        distance_map = distance_transform_edt(slice_mask)
        
        # Build cubical complex and compute persistence
        cc = gudhi.CubicalComplex(
            dimensions=slice_mask.shape,
            top_dimensional_cells=distance_map.flatten()
        )
        persistence = cc.persistence()
        persistence_diagrams.append(persistence)
    
    return persistence_diagrams
```

### Pipeline 2: Structural Similarity

```python
def pipeline2_structural_similarity(scan1, scan2, max_alpha=100):
    """
    Measure structural similarity between two scans using α-filtrations
    
    Args:
        scan1, scan2: Point cloud representations of brain structure
        max_alpha: Maximum α value for filtration
    
    Returns:
        Similarity score and persistence comparison
    """
    # Build α-complex for both scans
    alpha_complex1 = gudhi.AlphaComplex(points=scan1)
    simplex_tree1 = alpha_complex1.create_simplex_tree(max_alpha_square=max_alpha**2)
    persistence1 = simplex_tree1.persistence()
    
    alpha_complex2 = gudhi.AlphaComplex(points=scan2)
    simplex_tree2 = alpha_complex2.create_simplex_tree(max_alpha_square=max_alpha**2)
    persistence2 = simplex_tree2.persistence()
    
    # Compute persistence-based similarity
    similarity = compute_persistence_similarity(persistence1, persistence2)
    
    return similarity, persistence1, persistence2
```

## Performance Metrics

### Pipeline 1 Results (ADNI Dataset)
- **ROC-AUC**: 0.895 for AD vs CN classification
- **Peak effects**: Localized to medial temporal regions
- **Input**: Single-modality T1-weighted MRI
- **No nonlinear registration required**

### Pipeline 2 Results (Longitudinal)
- Follow-up scans remain closest to their own baselines
- AD subjects show greater short-interval change than CN subjects
- Captures disease-related longitudinal change patterns

## Interpretable Topological Biomarkers

### Key Topological Features

1. **Birth-death pairs**: Indicate scale of geometric features
2. **Persistence**: Measures feature significance
3. **Betti numbers**: Count of topological features (connected components, holes, voids)

### Clinical Interpretation

| Biomarker | Clinical Significance |
|-----------|----------------------|
| High persistence in temporal regions | Hippocampal atrophy |
| Increased void persistence | Ventricular enlargement |
| Reduced surface persistence | Cortical thinning |
| Altered connectivity patterns | White matter degradation |

## Use Cases

### Case 1: Alzheimer's Detection

```python
# Load MRI scan
mri_scan = nib.load('subject_t1w.nii.gz')
brain_mask = extract_brain_mask(mri_scan)

# Apply Pipeline 1
pdgm = pipeline1_regional_thinning(brain_mask)

# Extract features for classification
features = extract_persistence_features(pdgm)
prediction = classifier.predict(features)  # AD vs CN
```

### Case 2: Longitudinal Monitoring

```python
# Compare baseline and follow-up scans
baseline_scan = load_point_cloud('baseline.ply')
followup_scan = load_point_cloud('followup_6months.ply')

# Apply Pipeline 2
similarity, _, _ = pipeline2_structural_similarity(
    baseline_scan, followup_scan
)

# Track change over time
if similarity < threshold:
    print("Significant structural change detected")
```

## Integration with Existing Pipelines

### BIDS Compatibility

```python
# Load BIDS-formatted data
from bids import BIDSLayout

layout = BIDSLayout('/data/adni_bids')
t1w_files = layout.get(suffix='T1w', extension='nii.gz')

for t1w in t1w_files:
    # Process with HBM
    results = process_hbm(t1w.path)
```

### Comparison with VBM

HBM complements traditional VBM by:
- Providing registration-free analysis
- Preserving subject-specific morphological features
- Enabling robust analysis of pathological brains
- Offering interpretable topological biomarkers

## References

- Paper: arXiv:2604.24714v1 [math.AT]
- Title: "Homology-based Morphometry of Brain Atrophy: Methods and Applications"
- Authors: Donato Quiccione, Mariam Pirashvili, Nathan Broomhead, et al.
- Dataset: Alzheimer's Disease Neuroimaging Initiative (ADNI)

## Related Skills

- `brain-network-controllability`: Network control theory for brain networks
- `topological-ml-eeg-classification`: Topological methods for EEG analysis
- `brain-graph-neural`: GNN methods for brain connectivity

## Activation Keywords

- brain atrophy analysis
- persistent homology MRI
- topological morphometry
- homology-based brain measurement
- TDA neuroimaging
- 脑萎缩同调分析
- 拓扑脑形态学
