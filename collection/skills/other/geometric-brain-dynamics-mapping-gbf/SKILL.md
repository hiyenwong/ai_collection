---
name: geometric-brain-dynamics-mapping-gbf
description: Geometric Basis Functions (GBF) methodology for noninvasive whole human brain dynamics mapping using participant-specific cortical eigenmodes. Reconstructs whole-brain spatiotemporal dynamics from EEG/MEG with anatomically-constrained source imaging. Activation - geometric basis functions, GBF, brain dynamics, source imaging, cortical geometry, EEG/MEG reconstruction.
---

# Geometric Brain Dynamics Mapping with GBF

## Overview

Geometric Basis Functions (GBF) framework for accurate reconstruction of whole-brain spatiotemporal dynamics from non-invasive electrophysiology (EEG/MEG). Uses participant-specific eigenmodes derived from individual cortical surfaces to resolve the inverse problem with anatomically-consistent priors.

## Core Methodology

### 1. Geometric Basis Functions Construction

**Cortical Surface Eigenmodes:**
- Extract individual participant's cortical surface mesh
- Compute geometric eigenmodes (vibration modes) of the cortical surface
- These modes form a compact, anatomically-meaningful basis set
- Typically hundreds of modes capture whole-brain dynamics

**Mathematical Formulation:**
```
Source activity s(r,t) = Σ_i α_i(t) * φ_i(r)

Where:
- φ_i(r) = i-th geometric eigenmode at location r
- α_i(t) = time-varying coefficient for mode i
- r = position on cortical surface
- t = time
```

### 2. EEG/MEG Forward Model

**Forward Solution:**
```
Measurements m(t) = L * s(t) + noise

Where L is the lead field matrix mapping sources to sensors
```

**GBF-Forward Projection:**
```
m(t) = L * Φ * α(t)

Where:
- Φ = [φ_1, φ_2, ..., φ_n] (geometric basis matrix)
- α(t) = [α_1(t), α_2(t), ..., α_n(t)]^T
```

### 3. Source Reconstruction

**Inverse Problem Solution:**
```
α̂(t) = argmin_α ||m(t) - L*Φ*α||² + λ * ||α||²

Source estimate ŝ(t) = Φ * α̂(t)
```

### 4. Key Advantages

| Feature | Traditional Methods | GBF Method |
|---------|-------------------|------------|
| Prior | Generic (LORETA, MNE) | Individual geometry |
| Dimension | ~10k sources | ~100-500 modes |
| Anatomical | Weak | Strong constraint |
| Noise | Voxel-wise correlated | Mode-wise decorrelated |
| Interpretation | Location-based | Geometry-based |

## Implementation Workflow

### Step 1: Data Preparation

```python
# Required inputs
subject_mri = "t1w.nii.gz"  # Individual T1-weighted MRI
cortical_surface = "pial.surf"  # Cortical surface mesh
sensor_locations = "electrode_xyz.csv"  # EEG/MEG sensor positions
conductivity_profile = "conductivity.json"  # Head conductivity model
```

### Step 2: Compute Geometric Eigenmodes

```python
import numpy as np
from scipy.sparse.linalg import eigsh

def compute_geometric_modes(surface_mesh, n_modes=500):
    """
    Compute geometric eigenmodes of cortical surface.
    """
    # Compute cotangent Laplacian
    L = compute_cotangent_laplacian(surface_mesh)
    M = compute_mass_matrix(surface_mesh)
    
    # Solve generalized eigenvalue problem
    eigenvalues, eigenvectors = eigsh(L, k=n_modes, M=M, sigma=0)
    
    return eigenvalues, eigenvectors
```

### Step 3: Build GBF Forward Model

```python
def build_gbf_forward_model(lead_field, geometric_modes):
    """
    Project lead field to geometric basis.
    """
    return lead_field @ geometric_modes
```

### Step 4: Source Reconstruction

```python
def reconstruct_gbf_sources(measurements, gbf_forward, lambda_reg=0.01):
    """
    Reconstruct source activity in GBF space.
    """
    n_modes = gbf_forward.shape[1]
    I = np.eye(n_modes)
    
    source_modes = np.linalg.solve(
        gbf_forward.T @ gbf_forward + lambda_reg * I,
        gbf_forward.T @ measurements
    )
    
    # Project back to source space
    source_space = geometric_modes @ source_modes
    
    return source_modes, source_space
```

## Validation Benchmarks

### Meta-Source Benchmark
- 10,000+ source configurations
- Multiple cortical regions
- Quantitative localization error metrics

### Task-Evoked Validation
- Auditory oddball tasks
- Motor paradigms
- Visual processing

### Resting-State Networks
- Default mode network
- Visual network
- Sensorimotor network
- Dorsal attention network

### Clinical Applications
- Intracranial stimulation validation
- Epilepsy source localization
- Pre-surgical planning

## Applications

### 1. High-Resolution Source Imaging
- Improved spatial resolution over traditional methods
- Better localization accuracy
- Reduced spatial smearing

### 2. Dynamic Brain Network Analysis
- Track network evolution over time
- Study connectivity patterns
- Analyze frequency-specific dynamics

### 3. Clinical Diagnostics
- Epileptic focus localization
- Pre-surgical mapping
- Disease biomarker extraction

### 4. Cognitive Neuroscience
- Study cognitive processes
- Brain-behavior relationships
- Individual differences

## References

- Wang et al. (2026): "A geometry aware framework enhances noninvasive mapping of whole human brain dynamics"
- arXiv:2604.25592
- Categories: q-bio.NC, eess.SP

## Activation Triggers

Use this skill when working with:
- EEG/MEG source localization
- Brain dynamics reconstruction
- Cortical surface modeling
- Anatomically-constrained inverse problems
- Individual-specific brain imaging
