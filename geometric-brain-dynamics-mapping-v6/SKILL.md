---
name: geometric-brain-dynamics-mapping-v6
description: Geometric Basis Functions (GBF) framework for noninvasive whole human brain dynamics mapping using participant-specific eigenmodes derived from cortical geometry. Use when working with EEG/MEG source imaging, brain dynamics reconstruction, neuroimaging inverse problems, or cortical geometry-based neural activity mapping. Enables high-fidelity spatiotemporal reconstruction of neural sources using geometric constraints.
---

# Geometric Brain Dynamics Mapping v6 (GBF Framework)

Geometric Basis Functions (GBF) methodology for noninvasive mapping of whole human brain dynamics using participant-specific cortical geometry eigenmodes.

## Overview

The GBF framework addresses the fundamental limitation of EEG/MEG source imaging: low-dimensional, indirect observations of high-dimensional neural dynamics. By embedding participant-specific geometric basis functions (eigenmodes derived from each individual's cortical surface), GBF provides powerful anatomical constraints that resolve the inverse problem and improve reconstruction fidelity.

### Core Innovation

Traditional EEG/MEG source imaging relies on simplistic or biologically implausible priors. GBF reconstructs neural sources as **linear combinations of geometric basis functions**, aligning source estimates with the geometric organization of neural dynamics.

### Key Capabilities

1. **Participant-Specific Modeling**: Uses each individual's cortical surface geometry
2. **High Localization Accuracy**: Validated across multiple benchmarks and datasets
3. **Fast Spatiotemporal Dynamics**: Captures dynamics consistent with anatomical pathways
4. **Compact Representation**: Describes whole-brain activity with hundreds of geometric modes
5. **Versatile Applications**: Scientific research and clinical applications

## Theoretical Foundation

### Geometric Basis Functions

GBFs are eigenmodes derived from the Laplace-Beltrami operator on each participant's cortical surface mesh:

```
Δφ_k = -λ_k φ_k
```

Where:
- `Δ` is the Laplace-Beltrami operator on the cortical surface
- `φ_k` are the eigenfunctions (geometric basis functions)
- `λ_k` are the corresponding eigenvalues

### Forward Model

The EEG/MEG forward model relates neural sources to sensor measurements:

```
Y = LX + ε
```

Where:
- `Y` is the sensor data (channels × timepoints)
- `L` is the leadfield matrix (channels × sources)
- `X` is the neural source activity (sources × timepoints)
- `ε` is noise

### GBF Source Representation

Neural sources are represented as linear combinations of GBFs:

```
X = Φα
```

Where:
- `Φ` is the GBF matrix (sources × modes)
- `α` are the GBF coefficients (modes × timepoints)

### Inverse Solution

The inverse problem becomes estimating GBF coefficients:

```
α̂ = argmin_α ||Y - LΦα||²_F + λR(α)
```

Where `R(α)` is a regularization term (e.g., L2 norm).

## Workflow

### 1. Data Preparation

**Requirements:**
- Individual T1-weighted MRI scan
- Cortical surface reconstruction (e.g., FreeSurfer)
- EEG/MEG sensor positions co-registered to MRI space
- EEG/MEG recordings

**Surface Processing:**
```python
# Load cortical surface mesh
vertices, faces = load_cortical_surface('lh.pial')

# Compute Laplace-Beltrami operator
L = compute_laplacian_beltrami(vertices, faces)

# Compute eigenmodes (GBFs)
eigenvalues, eigenvectors = eigsh(L, k=500, sigma=0)
```

### 2. Forward Model Computation

```python
# Compute leadfield matrix
leadfield = compute_leadfield(
    subjects_dir='subjects/',
    subject='subject_id',
    src=source_space,
    bem=boundary_element_model,
    meg=True,  # or eeg=True
    mindist=5.0  # minimum distance from inner skull
)

# Project leadfield to GBF space
leadfield_gbf = leadfield @ gbf_matrix
```

### 3. GBF Coefficient Estimation

```python
# Standard approach: Minimum norm estimate
from scipy.linalg import solve

# L2-regularized solution
lambda_reg = 0.1  # regularization parameter
alpha_hat = solve(
    leadfield_gbf.T @ leadfield_gbf + lambda_reg * np.eye(n_modes),
    leadfield_gbf.T @ sensor_data
)

# Reconstruct source activity in original space
source_activity = gbf_matrix @ alpha_hat
```

### 4. Advanced Estimation Methods

**Weighted Minimum Norm:**
```python
# Depth-weighted inverse
w = np.linalg.norm(leadfield_gbf, axis=0)
W_inv = np.diag(1.0 / (w + epsilon))

alpha_hat = W_inv @ solve(
    W_inv.T @ leadfield_gbf.T @ leadfield_gbf @ W_inv + lambda_reg * np.eye(n_modes),
    W_inv.T @ leadfield_gbf.T @ sensor_data
)
```

**Mixed Norm (MNE + L1):**
```python
# Promotes sparse solutions while maintaining smoothness
from sklearn.linear_model import MultiTaskLasso

alpha_hat = MultiTaskLasso(
    alpha=0.01,
    max_iter=10000
).fit(leadfield_gbf, sensor_data).coef_.T
```

## Implementation Details

### Surface Eigenmode Computation

```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh

def compute_cotangent_laplacian(vertices, faces):
    """
    Compute cotangent Laplacian for triangular mesh.
    
    Parameters:
    -----------
    vertices : ndarray (n_vertices, 3)
        Vertex coordinates
    faces : ndarray (n_faces, 3)
        Triangle indices
    
    Returns:
    --------
    L : sparse matrix
        Cotangent Laplacian
    """
    n_vertices = len(vertices)
    
    # Compute edge vectors
    v0 = vertices[faces[:, 0]]
    v1 = vertices[faces[:, 1]]
    v2 = vertices[faces[:, 2]]
    
    # Edge lengths
    e0 = v2 - v1
    e1 = v0 - v2
    e2 = v1 - v0
    
    # Cotangent weights
    cot0 = np.sum(e1 * e2, axis=1) / np.linalg.norm(np.cross(e1, e2), axis=1)
    cot1 = np.sum(e2 * e0, axis=1) / np.linalg.norm(np.cross(e2, e0), axis=1)
    cot2 = np.sum(e0 * e1, axis=1) / np.linalg.norm(np.cross(e0, e1), axis=1)
    
    # Build sparse matrix
    row = np.concatenate([faces[:, 0], faces[:, 1], faces[:, 2],
                          faces[:, 1], faces[:, 2], faces[:, 0],
                          faces[:, 0], faces[:, 1], faces[:, 2]])
    col = np.concatenate([faces[:, 1], faces[:, 2], faces[:, 0],
                          faces[:, 0], faces[:, 1], faces[:, 2],
                          faces[:, 0], faces[:, 1], faces[:, 2]])
    data = np.concatenate([cot2, cot0, cot1,
                           cot2, cot0, cot1,
                           -(cot0 + cot1 + cot2)] * 2)
    
    L = csr_matrix((data, (row, col)), shape=(n_vertices, n_vertices))
    return L


def compute_geometric_basis_functions(vertices, faces, n_modes=500):
    """
    Compute GBFs (eigenmodes) of cortical surface.
    
    Parameters:
    -----------
    vertices : ndarray
        Surface vertices
    faces : ndarray
        Surface faces
    n_modes : int
        Number of eigenmodes to compute
    
    Returns:
    --------
    eigenvalues : ndarray (n_modes,)
    eigenvectors : ndarray (n_vertices, n_modes)
    """
    L = compute_cotangent_laplacian(vertices, faces)
    
    # Compute smallest eigenvalues (excluding zero mode)
    eigenvalues, eigenvectors = eigsh(L, k=n_modes + 1, sigma=0)
    
    # Remove constant mode (first eigenvalue ≈ 0)
    eigenvalues = eigenvalues[1:]
    eigenvectors = eigenvectors[:, 1:]
    
    return eigenvalues, eigenvectors
```

### Sensor-Space to Source-Space Mapping

```python
def map_sensors_to_gbf_space(sensor_data, leadfield_gbf, method='mne', lambda_reg=0.1):
    """
    Map sensor-space EEG/MEG data to GBF coefficients.
    
    Parameters:
    -----------
    sensor_data : ndarray (n_sensors, n_timepoints)
        EEG/MEG sensor recordings
    leadfield_gbf : ndarray (n_sensors, n_modes)
        Leadfield projected to GBF space
    method : str
        'mne' (minimum norm), 'wmne' (weighted), 'lasso'
    lambda_reg : float
        Regularization parameter
    
    Returns:
    --------
    alpha : ndarray (n_modes, n_timepoints)
        GBF coefficients
    """
    if method == 'mne':
        # Standard minimum norm
        LTL = leadfield_gbf.T @ leadfield_gbf
        alpha = np.linalg.solve(LTL + lambda_reg * np.eye(LTL.shape[0]),
                                leadfield_gbf.T @ sensor_data)
    
    elif method == 'wmne':
        # Depth-weighted minimum norm
        w = np.linalg.norm(leadfield_gbf, axis=0)
        W = np.diag(1.0 / (w + 1e-6))
        LTL = W @ leadfield_gbf.T @ leadfield_gbf @ W
        alpha = W @ np.linalg.solve(LTL + lambda_reg * np.eye(LTL.shape[0]),
                                     W @ leadfield_gbf.T @ sensor_data)
    
    elif method == 'lasso':
        # Sparse reconstruction
        from sklearn.linear_model import MultiTaskLasso
        alpha = MultiTaskLasso(alpha=lambda_reg, max_iter=10000).fit(
            leadfield_gbf, sensor_data.T).coef_.T
    
    return alpha
```

### Source Activity Visualization

```python
def visualize_gbf_reconstruction(vertices, faces, gbf_coefficients, gbf_matrix,
                                  timepoint=0, cmap='coolwarm'):
    """
    Visualize reconstructed source activity on cortical surface.
    
    Parameters:
    -----------
    vertices : ndarray
        Surface vertices
    faces : ndarray
        Surface faces
    gbf_coefficients : ndarray (n_modes, n_timepoints)
        GBF coefficients over time
    gbf_matrix : ndarray (n_vertices, n_modes)
        GBF matrix
    timepoint : int
        Timepoint to visualize
    cmap : str
        Colormap name
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    # Reconstruct activity at specific timepoint
    activity = gbf_matrix @ gbf_coefficients[:, timepoint]
    
    # Create 3D plot
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface with activity coloring
    triang = ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2],
                             triangles=faces, cmap=cmap,
                             linewidth=0, antialiased=False)
    triang.set_array(activity)
    
    plt.colorbar(triang, ax=ax, label='Activity')
    ax.set_title(f'Source Activity at t={timepoint}')
    plt.tight_layout()
    
    return fig
```

## Validation Results

The GBF framework has been validated across multiple datasets:

### Meta-Source Benchmark
- High localization accuracy for simulated sources
- Improved spatial precision compared to traditional methods

### Task-Evoked Data
- Accurate reconstruction of evoked responses
- Consistent with known functional neuroanatomy

### Resting-State Networks
- Captures canonical resting-state networks
- Spatial patterns match fMRI-derived networks

### Intracranial Stimulation
- Validated against ground-truth intracranial recordings
- High correlation with stimulated cortical regions

### Epilepsy Data
- Accurate localization of epileptogenic zones
- Clinical utility for pre-surgical evaluation

## Best Practices

### 1. Mode Selection

**How many GBF modes?**
- Default: 200-500 modes capture most relevant spatial scales
- More modes: Higher spatial resolution, more computation
- Fewer modes: Smoother solutions, faster computation
- Rule of thumb: Include modes up to spatial frequency relevant for your research question

### 2. Regularization

**L2 regularization (λ):**
- Start with λ = 0.1 (SNR-dependent)
- Higher λ: Smoother solutions, less overfitting
- Lower λ: Sharper reconstructions, risk of noise amplification
- Cross-validation recommended for optimal selection

### 3. Surface Processing

**Cortical surface quality:**
- Ensure accurate surface reconstruction
- Check for topological defects
- Smooth surface if needed (e.g., 10 iterations)
- Use inflated surfaces for visualization

### 4. Sensor Co-registration

**Accurate head positioning:**
- Use fiducial-based co-registration
- Verify alignment with scalp surface
- Consider using ICP refinement
- Check for systematic displacements

## Common Pitfalls

### 1. Insufficient Modes

**Problem**: Using too few modes loses spatial detail
**Solution**: Start with 500 modes, validate with localization metrics

### 2. Over-regularization

**Problem**: Excessive smoothing obscures true activity patterns
**Solution**: Use cross-validation to optimize λ

### 3. Leadfield Errors

**Problem**: Inaccurate forward model causes systematic biases
**Solution**: Careful BEM model construction, validation with phantom data

### 4. Surface Misalignment

**Problem**: Mismatch between electrode positions and anatomy
**Solution**: Rigorous co-registration, visual inspection

## Comparison with Other Methods

| Method | Spatial Resolution | Biological Plausibility | Computational Cost | Individual Variability |
|--------|-------------------|------------------------|-------------------|----------------------|
| GBF | High | High (geometry-based) | Medium | Participant-specific |
| MNE | Medium | Low | Low | Generic |
| dSPM | Medium | Low | Low | Generic |
| sLORETA | Medium | Medium | Low | Generic |
| Beamformer | High | Low | Medium | Participant-specific |

## Applications

### Research Applications

1. **Cognitive Neuroscience**: Mapping task-related brain activity
2. **Clinical Research**: Studying pathological brain dynamics
3. **Brain-Computer Interfaces**: High-resolution feature extraction
4. **Network Neuroscience**: Studying large-scale brain networks

### Clinical Applications

1. **Epilepsy**: Localization of epileptogenic zones
2. **Stroke**: Mapping peri-lesional activity
3. **Brain Tumors**: Pre-surgical functional mapping
4. **Neurodegenerative Diseases**: Tracking disease progression

## References

### Primary Source
- Wang, S., Lou, K., Wei, C., et al. (2026). A geometry aware framework enhances noninvasive mapping of whole human brain dynamics. arXiv:2604.25592 [q-bio.NC].

### Related Methods
- Laplace-Beltrami eigenfunctions for cortical surface analysis
- Minimum norm estimation (MNE) for EEG/MEG source imaging
- Eigenmode-based brain mapping (BrainEigen)
- Geometric constraints in neural mass models

### Software Dependencies
- MNE-Python: EEG/MEG analysis
- FreeSurfer: Cortical surface reconstruction
- NumPy/SciPy: Numerical computations
- Scikit-learn: Machine learning utilities

## Further Reading

See `references/` directory for:
- `mathematical_formulation.md`: Detailed mathematical derivations
- `validation_studies.md`: Comprehensive validation results
- `implementation_examples.md`: Complete code examples
- `clinical_applications.md`: Clinical use cases and protocols

## Updates

v6 (April 2026):
- Initial skill creation based on arXiv:2604.25592
- Comprehensive workflow documentation
- Validation results from Meta-Source Benchmark
- Clinical application guidelines
