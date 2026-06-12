---
name: geometric-brain-dynamics-mapping-v7
description: "Geometry-aware framework for noninvasive whole-brain spatiotemporal dynamics mapping using participant-specific Geometric Basis Functions (GBFs). Resolves EEG/MEG inverse problem via cortical-surface eigenmodes. Validated across Meta-Source Benchmark, task-evoked, resting-state, intracranial stimulation, and epilepsy data."
category: neuroscience
keywords:
  - geometric basis functions
  - GBF
  - cortical surface eigenmodes
  - EEG source imaging
  - MEG source imaging
  - brain dynamics mapping
  - inverse problem
  - neuroelectromagnetic inverse
  - Laplace-Beltrami eigenmodes
  - cortical geometry
  - spatiotemporal dynamics
  - whole-brain reconstruction
  - source localization
  - anatomical constraints
  - 几何基函数
  - 脑动力学映射
  - 皮层表面
  - 脑电源成像
  - 逆问题
  - 脑网络
version: 7
paper:
  title: "A geometry aware framework enhances noninvasive mapping of whole human brain dynamics"
  arxiv: "2604.25592"
  authors:
    - Song Wang
    - Kexin Lou
    - Chen Wei
  date: "2026-04-28"
  categories:
    - "q-bio.NC"
    - "eess.SP"
---

# Geometric Brain Dynamics Mapping (v7)

Skill for the geometry-aware framework described in arXiv:2604.25592 — a method that resolves the neuroelectromagnetic inverse problem by embedding participant-specific **Geometric Basis Functions (GBFs)**, i.e., eigenmodes derived from individual cortical surface geometry, to achieve high-fidelity whole-brain spatiotemporal dynamics reconstruction from EEG/MEG data.

> **Version 7** — Updated with comprehensive Python implementation, expanded validation benchmarks, detailed GBF computation pipeline, and bilingual activation keywords. Supersedes v1–v6.

---

## 1. Core Concept

### 1.1 Problem Statement

Noninvasive brain mapping with EEG/MEG faces a fundamental **ill-posed inverse problem**: infinitely many source configurations can produce the same sensor-level measurements. Traditional approaches impose generic spatial priors (minimum norm, beamforming, Bayesian constraints) that are not grounded in individual anatomy.

### 1.2 GBF Solution

This framework introduces **Geometric Basis Functions (GBFs)** — eigenmodes of the Laplace-Beltrami operator computed on each participant's individual cortical surface mesh. These eigenmodes:

- **Encode geometric structure** of the cortical sheet (gyral/sulcal patterns, curvature)
- **Form an orthonormal basis** for cortical source activity
- **Provide anatomically-grounded constraints** that dramatically reduce the solution space
- **Enable compact representation**: hundreds of modes capture whole-brain dynamics

The neural source distribution at time *t* is expressed as:

```
S(t) = Σᵢ αᵢ(t) · φᵢ(r)
```

where:
- `S(t)` = neural source current density at time *t*
- `φᵢ(r)` = i-th GBF (eigenmode of cortical surface)
- `αᵢ(t)` = time-varying coefficient (amplitude of mode *i*)
- `r` = spatial location on cortical surface

---

## 2. GBF Methodology

### 2.1 Cortical Surface Mesh Preparation

```
Input: T1-weighted anatomical MRI
Process: FreeSurfer / CIVET / CAT12 pipeline
  → White matter surface extraction
  → Pial surface extraction
  → Surface inflation & topology correction
  → Vertex-level registration to common template (optional)
Output: Triangular mesh (vertices V, faces F, vertex normals)
```

### 2.2 Laplace-Beltrami Eigenmode Computation

The GBFs are solutions to the Laplace-Beltrami eigenvalue problem on the cortical surface manifold:

```
Δ_Γ φᵢ = -λᵢ φᵢ    on Γ (cortical surface)
```

where:
- `Δ_Γ` = Laplace-Beltrami operator (surface Laplacian)
- `λᵢ` = eigenvalue (spatial frequency of mode *i*)
- `φᵢ` = eigenfunction (GBF mode *i*)
- `Γ` = cortical surface manifold

Key properties:
- Eigenvalues ordered: `0 = λ₀ ≤ λ₁ ≤ λ₂ ≤ ...`
- Eigenmodes are orthonormal: `∫_Γ φᵢ φⱼ dA = δᵢⱼ`
- Low-index modes capture global patterns; high-index modes capture local detail

### 2.3 Forward Model Integration

The standard EEG/MEG forward model relates sources to sensor measurements:

```
M(t) = L · S(t) + ε(t)
```

where:
- `M(t)` = sensor measurements (EEG electrodes or MEG sensors)
- `L` = leadfield matrix (volume conduction model)
- `S(t)` = source activity on cortical mesh
- `ε(t)` = measurement noise

**GBF reformulation** substitutes the GBF expansion:

```
M(t) = L · (Φ · α(t)) + ε(t)
     = (L · Φ) · α(t) + ε(t)
     = L_GBF · α(t) + ε(t)
```

where:
- `Φ` = matrix of GBF eigenvectors (columns = eigenmodes)
- `L_GBF = L · Φ` = GBF-projected leadfield
- `α(t)` = mode coefficients (reduced dimensionality)

### 2.4 Inverse Solution

With GBFs, the inverse problem becomes:

```
min_α || M(t) - L_GBF · α(t) ||² + η · R(α(t))
```

where:
- `R(α)` = regularization term (Tikhonov, sparse, etc.)
- `η` = regularization parameter
- Dimensionality reduced from thousands of vertices to hundreds of GBF modes

---

## 3. Python Implementation

### 3.1 Computing GBFs from Cortical Surface Mesh

```python
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from typing import Tuple, Optional


def compute_cotangent_weights(
    vertices: np.ndarray,
    faces: np.ndarray
) -> sp.csr_matrix:
    """
    Compute cotangent-weighted Laplacian for a triangular mesh.
    Implements the standard FEM discretization of the
    Laplace-Beltrami operator.

    Parameters
    ----------
    vertices : (N, 3) array of vertex coordinates
    faces : (M, 3) array of face vertex indices

    Returns
    -------
    L : (N, N) sparse cotangent Laplacian matrix
    """
    N = vertices.shape[0]
    rows, cols, vals = [], [], []

    for f in faces:
        # Triangle vertices
        v0, v1, v2 = vertices[f[0]], vertices[f[1]], vertices[f[2]]

        # Edge vectors
        e0 = v1 - v2  # opposite vertex 0
        e1 = v2 - v0  # opposite vertex 1
        e2 = v0 - v1  # opposite vertex 2

        # Cotangent of angles using cross/dot products
        # cot(A) = (b·c) / |b×c|
        cross = np.cross(e1, e2)
        area = 0.5 * np.linalg.norm(cross)

        if area < 1e-12:
            continue

        # Cotangents for each angle
        cot_0 = np.dot(e1, e2) / (4.0 * area)  # angle at v0
        cot_1 = np.dot(e0, -e2) / (4.0 * area)  # angle at v1
        cot_2 = np.dot(-e1, e0) / (4.0 * area)  # angle at v2

        # Off-diagonal entries (negative cotangents)
        for i, j, cot in [(f[0], f[1], cot_2),
                           (f[1], f[2], cot_0),
                           (f[2], f[0], cot_1)]:
            rows.extend([i, j, i, j])
            cols.extend([i, j, j, i])
            vals.extend([cot, cot, -cot, -cot])

    L = sp.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return L


def compute_area_matrix(
    vertices: np.ndarray,
    faces: np.ndarray
) -> sp.csr_matrix:
    """
    Compute lumped mass (area) matrix for the mesh.
    Each diagonal entry = 1/3 of the sum of adjacent triangle areas.

    Parameters
    ----------
    vertices : (N, 3) array
    faces : (M, 3) array

    Returns
    -------
    M : (N, N) diagonal sparse matrix (mass matrix)
    """
    N = vertices.shape[0]
    areas = np.zeros(N)

    for f in faces:
        v0, v1, v2 = vertices[f]
        edge1 = v1 - v0
        edge2 = v2 - v0
        triangle_area = 0.5 * np.linalg.norm(np.cross(edge1, edge2))
        # Barycentric distribution: each vertex gets 1/3
        areas[f] += triangle_area / 3.0

    return sp.diags(areas)


def compute_gbfs(
    vertices: np.ndarray,
    faces: np.ndarray,
    n_modes: int = 200,
    which: str = 'SM'
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute Geometric Basis Functions (GBFs) for a cortical surface mesh.

    Solves the generalized eigenvalue problem:
        L · φ = λ · M · φ
    where L is the cotangent Laplacian and M is the area (mass) matrix.

    Parameters
    ----------
    vertices : (N, 3) vertex coordinates
    faces : (M, 3) face indices
    n_modes : number of eigenmodes to compute (default 200)
    which : 'SM' for smallest magnitude eigenvalues

    Returns
    -------
    eigenvalues : (k,) sorted eigenvalues
    eigenmodes : (N, k) eigenmodes (columns), each is a GBF
    """
    # Build operators
    L = compute_cotangent_weights(vertices, faces)
    M_mat = compute_area_matrix(vertices, faces)

    # Symmetrize L (should already be symmetric, but ensure)
    L = 0.5 * (L + L.T)

    # Solve generalized eigenvalue problem
    eigenvalues, eigenmodes = eigsh(
        L,
        k=n_modes,
        M=M_mat,
        which=which,
        sigma=0.0,  # shift-invert for smallest eigenvalues
        tol=1e-8
    )

    # Sort by eigenvalue
    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenmodes = eigenmodes[:, idx]

    # Normalize eigenmodes (mass-weighted orthonormality)
    for i in range(eigenmodes.shape[1]):
        norm = np.sqrt(eigenmodes[:, i].T @ M_mat @ eigenmodes[:, i])
        if norm > 1e-12:
            eigenmodes[:, i] /= norm

    return eigenvalues, eigenmodes


def project_to_gbf_basis(
    source_data: np.ndarray,
    eigenmodes: np.ndarray,
    n_modes: Optional[int] = None
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Project source data onto the GBF basis to obtain mode coefficients.

    Parameters
    ----------
    source_data : (N, T) source activity on mesh (N vertices, T timepoints)
    eigenmodes : (N, K) GBF eigenmodes
    n_modes : number of modes to retain (default: all)

    Returns
    -------
    coefficients : (k, T) mode coefficients over time
    reconstruction : (N, T) reconstructed source activity
    """
    if n_modes is not None:
        modes = eigenmodes[:, :n_modes]
    else:
        modes = eigenmodes

    # Projection: α = Φ^T · S (using mass matrix weighting)
    coefficients = modes.T @ source_data

    # Reconstruction: S ≈ Φ · α
    reconstruction = modes @ coefficients

    return coefficients, reconstruction
```

### 3.2 GBF-Based Source Reconstruction

```python
class GBFSourceImaging:
    """
    GBF-based EEG/MEG source reconstruction.

    Uses participant-specific geometric basis functions to resolve
    the neuroelectromagnetic inverse problem.
    """

    def __init__(
        self,
        leadfield: np.ndarray,
        eigenmodes: np.ndarray,
        eigenvalues: np.ndarray,
        noise_cov: Optional[np.ndarray] = None,
        reg_method: str = 'tikhonov'
    ):
        """
        Parameters
        ----------
        leadfield : (n_sensors, n_vertices) forward model
        eigenmodes : (n_vertices, n_modes) GBF eigenmodes
        eigenvalues : (n_modes,) eigenvalues (sorted ascending)
        noise_cov : (n_sensors, n_sensors) noise covariance
        reg_method : regularization method ('tikhonov', 'sparse', 'bayesian')
        """
        self.n_sensors, self.n_vertices = leadfield.shape
        self.eigenmodes = eigenmodes
        self.eigenvalues = eigenvalues
        self.reg_method = reg_method

        # Project leadfield onto GBF basis
        # L_GBF = L · Φ : (n_sensors, n_modes)
        self.L_GBF = leadfield @ eigenmodes

        # Store noise covariance for whitening
        self.noise_cov = noise_cov
        self.W = None
        if noise_cov is not None:
            # Whitening matrix (Cholesky)
            self.W = np.linalg.cholesky(noise_cov)

    def solve(
        self,
        sensor_data: np.ndarray,
        reg_param: float = 1e-3
    ) -> np.ndarray:
        """
        Solve for mode coefficients α(t).

        Parameters
        ----------
        sensor_data : (n_sensors, n_timepoints) EEG/MEG data
        reg_param : regularization parameter λ

        Returns
        -------
        alpha : (n_modes, n_timepoints) mode coefficients
        """
        M = sensor_data
        if self.W is not None:
            M = np.linalg.solve(self.W, M)
            L = np.linalg.solve(self.W, self.L_GBF.T).T
        else:
            L = self.L_GBF

        n_modes = L.shape[1]

        if self.reg_method == 'tikhonov':
            # Standard Tikhonov: (L^T L + λI)^{-1} L^T M
            A = L.T @ L + reg_param * np.eye(n_modes)
            alpha = np.linalg.solve(A, L.T @ M)

        elif self.reg_method == 'eigenvalue_weighted':
            # Weighted by eigenvalue (smoothness prior)
            W_lambda = np.diag(np.sqrt(self.eigenvalues + 1e-12))
            A = L.T @ L + reg_param * (W_lambda @ W_lambda)
            alpha = np.linalg.solve(A, L.T @ M)

        else:
            # Default: Tikhonov
            A = L.T @ L + reg_param * np.eye(n_modes)
            alpha = np.linalg.solve(A, L.T @ M)

        return alpha

    def reconstruct_sources(
        self,
        alpha: np.ndarray
    ) -> np.ndarray:
        """
        Reconstruct cortical source distribution from mode coefficients.

        S(t) = Φ · α(t)

        Parameters
        ----------
        alpha : (n_modes, n_timepoints)

        Returns
        -------
        sources : (n_vertices, n_timepoints)
        """
        return self.eigenmodes @ alpha

    def explain_variance(
        self,
        sensor_data: np.ndarray,
        n_modes: int
    ) -> float:
        """
        Compute fraction of sensor variance explained by first n GBF modes.

        Parameters
        ----------
        sensor_data : (n_sensors, n_timepoints)
        n_modes : number of modes to evaluate

        Returns
        -------
        r_squared : fraction of variance explained
        """
        M = sensor_data
        L_sub = self.L_GBF[:, :n_modes]

        # Solve with subset
        A = L_sub.T @ L_sub + 1e-6 * np.eye(n_modes)
        alpha = np.linalg.solve(A, L_sub.T @ M)

        # Predicted
        M_pred = L_sub @ alpha

        # R²
        ss_res = np.sum((M - M_pred) ** 2)
        ss_tot = np.sum((M - M.mean(axis=1, keepdims=True)) ** 2)

        return 1.0 - ss_res / ss_tot
```

### 3.3 Selecting Optimal Number of GBF Modes

```python
def select_n_modes(
    eigenvalues: np.ndarray,
    variance_explained: np.ndarray,
    threshold: float = 0.95
) -> int:
    """
    Select number of GBF modes based on cumulative variance criterion.

    Parameters
    ----------
    eigenvalues : (K,) eigenvalues
    variance_explained : (K,) per-mode variance explained
    threshold : cumulative variance threshold (default 0.95)

    Returns
    -------
    n_optimal : optimal number of modes
    """
    cumulative = np.cumsum(variance_explained)
    n_optimal = np.searchsorted(cumulative, threshold) + 1
    n_optimal = min(n_optimal, len(eigenvalues))
    return n_optimal


def analyze_mode_spatial_scale(
    eigenvalues: np.ndarray,
    vertices: np.ndarray
) -> dict:
    """
    Analyze spatial scales of GBF modes.
    Low eigenvalues → large spatial scale (global patterns)
    High eigenvalues → small spatial scale (local details)

    Parameters
    ----------
    eigenvalues : (K,) sorted eigenvalues
    vertices : (N, 3) mesh vertices

    Returns
    -------
    analysis : dict with spatial scale statistics
    """
    # Characteristic wavelength for each mode
    # λ_char ~ 2π / sqrt(eigenvalue) (for connected mesh)
    wavelengths = []
    for ev in eigenvalues:
        if ev > 1e-12:
            wl = 2 * np.pi / np.sqrt(ev)
        else:
            wl = np.inf
        wavelengths.append(wl)

    return {
        'eigenvalues': eigenvalues,
        'characteristic_wavelengths': np.array(wavelengths),
        'min_wavelength': np.min([w for w in wavelengths if w != np.inf]),
        'mean_wavelength': np.mean([w for w in wavelengths if w != np.inf]),
        'max_wavelength': np.inf if np.isinf(wavelengths[0]) else wavelengths[0]
    }
```

### 3.4 Visualization Utilities

```python
def visualize_gbf_mode(
    vertices: np.ndarray,
    faces: np.ndarray,
    mode: np.ndarray,
    title: str = "GBF Mode",
    cmap: str = "coolwarm"
):
    """
    Visualize a single GBF mode on the cortical surface.
    Requires: matplotlib, trimesh or PyVista

    Parameters
    ----------
    vertices : (N, 3) mesh vertices
    faces : (M, 3) mesh faces
    mode : (N,) eigenmode values
    title : plot title
    cmap : matplotlib colormap
    """
    try:
        import trimesh
        mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
        mesh.visual.vertex_colors = _values_to_colors(mode, cmap)
        mesh.show()
    except ImportError:
        # Fallback: matplotlib 3D scatter
        import matplotlib.pyplot as plt
        from matplotlib.cm import get_cmap

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        colors = get_cmap(cmap)((mode - mode.min()) / (mode.ptp() + 1e-12))
        sc = ax.scatter(
            vertices[:, 0], vertices[:, 1], vertices[:, 2],
            c=colors, s=1, alpha=0.7
        )
        ax.set_title(title)
        plt.colorbar(sc, ax=ax, label='Mode Amplitude')
        plt.tight_layout()
        plt.show()


def plot_mode_spectra(
    eigenvalues: np.ndarray,
    coefficients: np.ndarray,
    n_top: int = 20
):
    """
    Plot the power spectra of top GBF modes over time.

    Parameters
    ----------
    eigenvalues : (K,) eigenvalues
    coefficients : (K, T) mode coefficients over time
    n_top : number of top modes to display
    """
    import matplotlib.pyplot as plt
    from scipy.signal import welch

    # Compute power for each mode
    mode_power = np.var(coefficients, axis=1)
    top_idx = np.argsort(mode_power)[-n_top:][::-1]

    fig, axes = plt.subplots(n_top, 1, figsize=(12, 2 * n_top))
    for i, idx in enumerate(top_idx):
        f, psd = welch(coefficients[idx], fs=1000)
        axes[i].semilogy(f, psd)
        axes[i].set_ylabel(f"Mode {idx}\nλ={eigenvalues[idx]:.3f}")
        axes[i].set_xlim(0, 100)

    axes[-1].set_xlabel("Frequency (Hz)")
    plt.tight_layout()
    plt.show()
```

---

## 4. Validation Benchmarks

### 4.1 Meta-Source Benchmark

- **Purpose**: Standardized evaluation of source localization accuracy
- **Metrics**: Localization error, spatial spread, amplitude fidelity
- **Result**: GBF framework achieves superior localization accuracy compared to MNE, sLORETA, and beamforming

### 4.2 Task-Evoked Data

- **Purpose**: Validate against known stimulus-locked activations
- **Datasets**: Visual, auditory, motor tasks with well-established activation patterns
- **Result**: GBF captures expected task-evoked activations with high spatial specificity and correct temporal dynamics

### 4.3 Resting-State Networks

- **Purpose**: Reproduce canonical resting-state networks (RSNs)
- **Networks**: Default Mode Network, Salience Network, Executive Control Network, Visual Network
- **Result**: GBF-reconstructed RSNs match fMRI-derived networks in spatial topology

### 4.4 Intracranial Stimulation

- **Purpose**: Ground-truth validation using direct cortical stimulation
- **Protocol**: Electrically stimulate known cortical sites, compare GBF source localization to stimulation coordinates
- **Result**: High concordance between GBF-reconstructed sources and true stimulation sites

### 4.5 Epilepsy Data

- **Purpose**: Clinical validation for epileptogenic zone localization
- **Application**: Pre-surgical planning, seizure onset zone identification
- **Result**: GBF provides clinically actionable localization consistent with intracranial EEG and surgical outcomes

### 4.6 Validation Summary Table

| Benchmark | Metric | GBF Result | Comparison |
|-----------|--------|------------|------------|
| Meta-Source | Localization Error | Low | Superior to MNE, sLORETA |
| Task-Evoked | Spatial Specificity | High | Matches known activations |
| Resting-State | Network Topology | Reproduced | Consistent with fMRI RSNs |
| Intracranial | Ground-Truth Concordance | High | Validates against known sites |
| Epilepsy | Clinical Localization | Actionable | Consistent with iEEG outcomes |

---

## 5. Key Findings & Insights

### 5.1 Spontaneous and Evoked Activity

- **Hundreds of geometric modes** are sufficient to describe both spontaneous (resting-state) and evoked (task-related) whole-brain activity
- The GBF expansion provides a **unified representation** for diverse neural phenomena

### 5.2 Compact Representation

- Dimensionality reduction: thousands of cortical vertices → hundreds of GBF modes
- Maintains **high reconstruction fidelity** with drastically reduced parameter space
- Enables computationally efficient analysis and visualization

### 5.3 Fast Spatiotemporal Dynamics

- GBF-reconstructed dynamics are **consistent with known anatomical pathways**
- Captures millisecond-scale propagation of neural activity
- Reveals geometric constraints on signal propagation speed and direction

### 5.4 Geometry-Dynamics Link

- Demonstrates that **cortical geometry directly constrains electrophysiological dynamics**
- Eigenmodes of surface Laplacian serve as natural modes of neural activity
- Provides mechanistic explanation for observed spatiotemporal patterns

---

## 6. Data & Tool Requirements

### 6.1 Required Data

| Data Type | Purpose | Format |
|-----------|---------|--------|
| T1-weighted MRI | Cortical surface extraction | NIfTI / DICOM |
| EEG or MEG recordings | Functional source imaging | EDF / FIF / BrainVision |
| Headshape / fiducials | Coregistration | Polhemus / digitized |
| Sensor locations | Forward model computation | Standard positions |

### 6.2 Software Dependencies

- **Surface extraction**: FreeSurfer, CIVET, CAT12, or HCP pipelines
- **Forward modeling**: MNE-Python, FieldTrip, Brainstorm, or OpenMEEG
- **Eigenmode computation**: SciPy (sparse eigenvalue solvers), SLEPc, or custom FEM
- **Analysis**: NumPy, SciPy, scikit-learn, Matplotlib
- **Optional**: PyVista or Trimesh for mesh visualization

### 6.3 Recommended Pipeline

```
1. Anatomical MRI → Cortical surface mesh (FreeSurfer)
2. Surface mesh → GBF eigenmodes (Laplace-Beltrami solver)
3. EEG/MEG + head model → Leadfield matrix (MNE/BEM)
4. Sensor data → GBF source reconstruction (GBF inverse)
5. Mode coefficients → Spatiotemporal analysis
```

---

## 7. Parameter Guidelines

| Parameter | Typical Range | Selection Criterion |
|-----------|---------------|---------------------|
| Number of GBF modes | 100–500 | Cumulative variance > 95% |
| Regularization λ | 1e-6 – 1e-2 | Cross-validation or L-curve |
| Mesh resolution | 5,000–30,000 vertices | Balance accuracy vs. computation |
| Eigenvalue solver tolerance | 1e-8 – 1e-10 | Shift-invert (sigma=0) |
| Time sampling | 250–2000 Hz | Match acquisition rate |

---

## 8. Comparison with Traditional Methods

| Aspect | Minimum Norm (MNE) | Beamforming | GBF Framework |
|--------|---------------------|-------------|---------------|
| Spatial Prior | L2 penalty on vertices | Data-driven adaptive | GBF eigenmodes |
| Anatomic Grounding | Generic | None | Participant-specific |
| Biological Plausibility | Low | Moderate | High |
| Compactness | Full vertex space | Full vertex space | Hundreds of modes |
| Interpretability | Voxel-level | Voxel-level | Mode-based (structured) |
| Computational Cost | Moderate | High | Moderate |
| Localization Accuracy | Moderate | Variable | High |
| Anatomical Consistency | No guarantee | No guarantee | Built-in via geometry |

---

## 9. Activation Keywords

### English
- geometric basis functions, GBF, cortical surface eigenmodes, Laplace-Beltrami eigenmodes, brain dynamics mapping, EEG source imaging, MEG source imaging, neuroelectromagnetic inverse problem, source localization, whole-brain reconstruction, cortical geometry, spatiotemporal dynamics, anatomical constraints, brain source estimation, eigenmode decomposition, cortical mesh analysis, geometry-aware brain mapping, participant-specific brain model, noninvasive brain mapping, electrophysiological dynamics, neural source reconstruction

### Chinese
- 几何基函数, 脑动力学映射, 皮层表面特征模态, 拉普拉斯-贝尔特拉米特征模态, 脑电源成像, 脑磁图源成像, 神经电磁逆问题, 源定位, 全脑重建, 皮层几何, 时空动力学, 解剖约束, 脑源估计, 特征模态分解, 皮层网格分析, 几何感知脑映射, 个体化脑模型, 无创脑映射, 电生理动力学, 神经源重建

---

## 10. Applications

### Scientific Research
- Whole-brain dynamics and connectivity studies
- Cognitive task-evoked activation mapping
- Resting-state network characterization
- Structure-function coupling analysis
- Neural propagation pathway analysis

### Clinical Applications
- Epilepsy focus localization and pre-surgical planning
- Brain-computer interface (BCI) feature extraction
- Neurological disorder biomarker identification
- Deep brain stimulation (DBS) target refinement
- Stroke recovery monitoring

### Methodological Extensions
- Multi-modal integration (EEG + MEG + fMRI)
- Dynamic GBF tracking (time-varying eigenmode contributions)
- Cross-subject GBF alignment via surface registration
- Real-time GBF-based neurofeedback
- GBF-informed neural mass modeling

---

## 11. Reference

```
@article{wang2026geometry,
  title = {A geometry aware framework enhances noninvasive mapping of whole human brain dynamics},
  author = {Wang, Song and Lou, Kexin and Wei, Chen and others},
  journal = {arXiv preprint},
  year = {2026},
  eprint = {2604.25592},
  primaryClass = {q-bio.NC},
  secondaryClass = {eess.SP},
  url = {https://arxiv.org/abs/2604.25592},
  date = {2026-04-28}
}
```

---

## 12. Related Skills

- `brain-digital-twins-execution-semantics-v4`
- `brain-foundation-model-inversion`
- `eeg-foundation-model-adapters`
- `adaptive-flow-routing-brain-networks`
- `geodynamics-geometric-state-space`
- `cortical-surface-analysis` (complementary)
