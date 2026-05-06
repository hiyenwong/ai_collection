---
name: discrete-heat-kernels-simplicial
description: "Discrete Heat Kernels on Simplicial Complexes and Its Application to Functional Brain Networks. Unified framework for heat kernel smoothing on simplicial complexes extending classical signal processing methods to higher-order network structures."
---

# Discrete Heat Kernels on Simplicial Complexes

> Unified framework for heat kernel smoothing on simplicial complexes, extending classical signal processing methods to higher-order network structures for functional brain network analysis.

## Metadata
- **Source**: arXiv:2509.16908v2
- **Authors**: Sixtus Dakurah
- **Published**: 2025-09-21
- **Category**: cs.SI, q-bio.NC, math.CO

## Core Methodology

### Key Innovation
Conventional graph-theoretic analyses capture exclusively pairwise interactions, omitting intricate higher-order relationships. This methodology introduces a **unified framework for heat kernel smoothing on simplicial complexes**, extending classical signal processing to higher-order structures.

### Theoretical Foundation

#### Heat Equation on Graphs (Review)

**Standard Graph Heat Equation**:
```
∂u/∂t = -L u

where L = D - A (Laplacian)
      u(t) = vertex signal at time t
```

**Solution - Heat Kernel**:
```
u(t) = e^(-tL) u(0)

Heat kernel H_t = e^(-tL) = Σ_k e^(-tλ_k) φ_k φ_k^T

where λ_k, φ_k are eigenvalues/vectors of L
```

**Properties**:
- Smoothing increases with time t
- Eigenvalues λ_k control frequency
- High λ_k (high frequency) decay faster

#### Extension to Simplicial Complexes

**Simplicial Complex Structure**:
- **k-simplices**: {v_0, ..., v_k} where (k+1) nodes all interact
- **Boundary operator** ∂_k: maps k-simplices to (k-1)-simplices
- **Coboundary operator** δ_k: adjoint of ∂_k

**Hodge Laplacian**:
```
L_k = ∂_{k+1} ∘ δ_k + δ_{k-1} ∘ ∂_k

= L_k^{up} + L_k^{down}

where L_k^{up} = ∂_{k+1} δ_k      (upper Laplacian)
      L_k^{down} = δ_{k-1} ∂_k    (lower Laplacian)
```

**Interpretation**:
- **L_0**: Standard graph Laplacian (on vertices)
- **L_1**: Edge Laplacian - captures flow/circulation
- **L_2**: Face Laplacian - captures voids/cavities

#### Heat Equation on k-simplices

```
∂u_k/∂t = -L_k u_k

Solution: u_k(t) = e^(-t L_k) u_k(0)
```

**Key Insight**: Heat diffusion occurs simultaneously on all dimensions, capturing different aspects of network dynamics.

### Heat Kernel Applications

#### 1. Signal Smoothing

**Standard (Vertex-level)**:
```
u_smoothed = H_t^(0) * u_0
```

**Higher-order (Edge-level)**:
```
flow_smoothed = H_t^(1) * f_0

where f_0 is initial edge flow
```

**Application to fMRI**:
- Vertex signals: Regional BOLD activity
- Edge signals: Information flow between regions
- Face signals: Multi-region coordination

#### 2. Distance Metrics

**Diffusion Distance**:
```
d_t(i, j)^2 = ||H_t(δ_i - δ_j)||^2

= Σ_k e^(-2tλ_k) (φ_k(i) - φ_k(j))^2
```

**Interpretation**: Measures connectivity strength considering all paths, not just shortest.

#### 3. Clustering and Segmentation

**Spectral Clustering on SC**:
```
1. Compute L_k for target dimension k
2. Eigen-decomposition: L_k = Φ Λ Φ^T
3. Use first m eigenvectors for k-means
4. Clusters represent cohesive higher-order structures
```

### Functional Brain Network Pipeline

```
Preprocessed fMRI
    ↓
1. Time Series Extraction
    - ROI-based parcellation
    - BOLD signal extraction
    ↓
2. Simplicial Complex Construction
    - Compute correlations
    - Threshold to create edges
    - Find cliques → simplices
    ↓
3. Heat Kernel Computation
    - Build Hodge Laplacian L_k
    - Compute eigen-decomposition
    - Construct H_t = e^(-tL_k)
    ↓
4. Signal Processing
    - Apply heat kernel smoothing
    - Extract features
    - Classification/Analysis
```

## Implementation Guide

### Prerequisites
```python
# Required libraries
pip install numpy scipy
pip install scikit-learn
pip install networkx
pip install gudhi          # For persistent homology/simplicial complexes
pip install nilearn        # fMRI processing
```

### Step-by-Step Implementation

#### Step 1: Simplicial Complex Construction from fMRI
```python
import numpy as np
from itertools import combinations
import networkx as nx

def build_simplicial_complex(time_series, correlation_threshold=0.5, max_dim=3):
    """
    Build simplicial complex from fMRI time series.
    
    Args:
        time_series: [n_timepoints, n_regions] array
        correlation_threshold: Minimum correlation for edge
        max_dim: Maximum simplex dimension
    
    Returns:
        simplices: List of (dimension, vertices) tuples
        L_k: Dictionary of Hodge Laplacians
    """
    n_regions = time_series.shape[1]
    
    # Compute correlation matrix
    corr_matrix = np.corrcoef(time_series.T)
    
    # Build graph from thresholded correlations
    G = nx.Graph()
    G.add_nodes_from(range(n_regions))
    
    edges = []
    for i in range(n_regions):
        for j in range(i+1, n_regions):
            if abs(corr_matrix[i, j]) > correlation_threshold:
                G.add_edge(i, j, weight=corr_matrix[i, j])
                edges.append((i, j))
    
    # Find cliques and build simplices
    simplices = {0: [(i,) for i in range(n_regions)]}
    
    for k in range(1, max_dim + 1):
        simplices[k] = []
        # Find all (k+1)-cliques
        for clique in nx.find_cliques(G):
            if len(clique) >= k + 1:
                for simplex in combinations(clique, k + 1):
                    simplices[k].append(tuple(sorted(simplex)))
        # Remove duplicates
        simplices[k] = list(set(simplices[k]))
    
    return simplices, G, corr_matrix

# Example usage
time_series = np.random.randn(200, 68)  # 200 timepoints, 68 regions (AAL)
simplices, graph, corr = build_simplicial_complex(time_series, max_dim=2)

print(f"0-simplices (vertices): {len(simplices[0])}")
print(f"1-simplices (edges): {len(simplices[1])}")
print(f"2-simplices (triangles): {len(simplices[2])}")
```

#### Step 2: Boundary Operators and Hodge Laplacian
```python
def construct_boundary_operators(simplices):
    """
    Construct boundary operators ∂_k for k = 1, 2, ..., max_dim.
    
    Args:
        simplices: Dictionary {k: list of k-simplices}
    
    Returns:
        boundary_ops: Dictionary {k: ∂_k as sparse matrix}
    """
    from scipy.sparse import csr_matrix
    
    boundary_ops = {}
    max_dim = max(simplices.keys())
    
    for k in range(1, max_dim + 1):
        k_simplices = simplices[k]
        k_minus_1_simplices = simplices[k-1]
        
        # Create index mapping for (k-1)-simplices
        idx_map = {simplex: i for i, simplex in enumerate(k_minus_1_simplices)}
        
        rows = []
        cols = []
        data = []
        
        for j, k_simplex in enumerate(k_simplices):
            # Faces of k-simplex (oriented boundary)
            for i, vertex in enumerate(k_simplex):
                face = k_simplex[:i] + k_simplex[i+1:]
                orientation = (-1) ** i
                
                if face in idx_map:
                    rows.append(idx_map[face])
                    cols.append(j)
                    data.append(orientation)
        
        boundary_ops[k] = csr_matrix(
            (data, (rows, cols)),
            shape=(len(k_minus_1_simplices), len(k_simplices))
        )
    
    return boundary_ops


def compute_hodge_laplacian(boundary_ops, k):
    """
    Compute Hodge Laplacian L_k.
    
    L_k = ∂_{k+1} ∂_{k+1}^T + ∂_k^T ∂_k
        = L_k^{up} + L_k^{down}
    """
    if k == 0:
        # For vertices, only upper Laplacian
        B1 = boundary_ops[1]
        L_0 = B1 @ B1.T
        return L_0
    
    B_k = boundary_ops[k]
    L_down = B_k.T @ B_k
    
    if k + 1 in boundary_ops:
        B_k_plus_1 = boundary_ops[k + 1]
        L_up = B_k_plus_1 @ B_k_plus_1.T
    else:
        L_up = 0
    
    L_k = L_up + L_down
    return L_k


# Example
boundary_ops = construct_boundary_operators(simplices)
L_0 = compute_hodge_laplacian(boundary_ops, 0)  # Vertex Laplacian
L_1 = compute_hodge_laplacian(boundary_ops, 1)  # Edge Laplacian
L_2 = compute_hodge_laplacian(boundary_ops, 2)  # Face Laplacian

print(f"L_0 shape: {L_0.shape}")
print(f"L_1 shape: {L_1.shape}")
print(f"L_2 shape: {L_2.shape}")
```

#### Step 3: Heat Kernel Computation
```python
def compute_heat_kernel(L_k, time_points, method='eigen'):
    """
    Compute heat kernel H_t = e^(-t * L_k).
    
    Args:
        L_k: Hodge Laplacian (sparse or dense matrix)
        time_points: List of time values t
        method: 'eigen' (eigendecomposition) or 'taylor' (series expansion)
    
    Returns:
        heat_kernels: Dictionary {t: H_t}
    """
    from scipy.linalg import expm
    from scipy.sparse.linalg import eigsh
    
    n = L_k.shape[0]
    heat_kernels = {}
    
    if method == 'eigen':
        # Eigendecomposition (for smaller matrices)
        # For sparse matrices, use eigsh for partial decomposition
        if n < 1000:
            eigenvalues, eigenvectors = np.linalg.eigh(L_k.toarray() if hasattr(L_k, 'toarray') else L_k)
        else:
            # Partial eigendecomposition for large matrices
            k = min(n - 2, 100)  # Top k eigenvalues
            eigenvalues, eigenvectors = eigsh(L_k, k=k, which='SM')
        
        for t in time_points:
            # H_t = Φ * diag(e^(-t*λ)) * Φ^T
            H_t = eigenvectors @ np.diag(np.exp(-t * eigenvalues)) @ eigenvectors.T
            heat_kernels[t] = H_t
    
    elif method == 'taylor':
        # Matrix exponential via scipy
        L_dense = L_k.toarray() if hasattr(L_k, 'toarray') else L_k
        for t in time_points:
            H_t = expm(-t * L_dense)
            heat_kernels[t] = H_t
    
    return heat_kernels


# Example usage
time_points = [0.1, 0.5, 1.0, 2.0, 5.0]
H_0 = compute_heat_kernel(L_0, time_points)  # Vertex heat kernels
H_1 = compute_heat_kernel(L_1, time_points)  # Edge heat kernels

print(f"Heat kernels computed for {len(time_points)} time points")
print(f"H_0 at t=1.0 shape: {H_0[1.0].shape}")
```

#### Step 4: Signal Smoothing and Feature Extraction
```python
class SimplicialSignalProcessor:
    """Process signals on simplicial complexes using heat kernels."""
    
    def __init__(self, simplices, boundary_ops):
        self.simplices = simplices
        self.boundary_ops = boundary_ops
        self.heat_kernels = {}
    
    def compute_all_heat_kernels(self, time_points):
        """Pre-compute heat kernels for all dimensions."""
        for k in self.simplices.keys():
            if k < max(self.simplices.keys()):
                L_k = compute_hodge_laplacian(self.boundary_ops, k)
                self.heat_kernels[k] = compute_heat_kernel(L_k, time_points)
    
    def smooth_signal(self, signal, k, t):
        """
        Apply heat kernel smoothing to k-dimensional signal.
        
        Args:
            signal: Initial signal on k-simplices [n_k]
            k: Simplex dimension
            t: Diffusion time
        
        Returns:
            smoothed: Smoothed signal
        """
        H_t = self.heat_kernels[k][t]
        smoothed = H_t @ signal
        return smoothed
    
    def extract_features(self, time_series, time_points):
        """
        Extract heat kernel features for classification.
        
        Args:
            time_series: Brain activity time series
            time_points: List of diffusion times
        
        Returns:
            features: Feature vector
        """
        features = {}
        
        # Vertex-level features (standard BOLD signals)
        v_signal = time_series.mean(axis=0)  # Average over time
        for t in time_points:
            v_smooth = self.smooth_signal(v_signal, 0, t)
            features[f'vertex_mean_t{t}'] = np.mean(v_smooth)
            features[f'vertex_std_t{t}'] = np.std(v_smooth)
        
        # Edge-level features (information flow)
        if 1 in self.heat_kernels:
            # Use correlation as initial edge signal
            edge_signal = np.array([
                corr[e] for e in self.simplices[1]
            ])
            for t in time_points:
                e_smooth = self.smooth_signal(edge_signal, 1, t)
                features[f'edge_mean_t{t}'] = np.mean(e_smooth)
                features[f'edge_energy_t{t}'] = np.sum(e_smooth**2)
        
        return features


# Example
processor = SimplicialSignalProcessor(simplices, boundary_ops)
processor.compute_all_heat_kernels([0.1, 0.5, 1.0, 2.0])

# Extract features
features = processor.extract_features(time_series, [0.1, 0.5, 1.0, 2.0])
print(f"Extracted {len(features)} features")
```

#### Step 5: Complete fMRI Analysis Pipeline
```python
class fMRIHeatKernelAnalysis:
    """Complete pipeline for fMRI analysis using heat kernels on SC."""
    
    def __init__(self, max_dim=2, time_points=None):
        self.max_dim = max_dim
        self.time_points = time_points or [0.1, 0.5, 1.0, 2.0, 5.0]
    
    def process_subject(self, fmri_data, atlas):
        """
        Process single subject fMRI data.
        
        Args:
            fmri_data: 4D fMRI volume
            atlas: Parcellation atlas
        
        Returns:
            features: Dictionary of features
        """
        # Extract time series
        from nilearn.maskers import NiftiLabelsMasker
        masker = NiftiLabelsMasker(labels_img=atlas, standardize=True)
        time_series = masker.fit_transform(fmri_data)
        
        # Build simplicial complex
        simplices, graph, corr = build_simplicial_complex(
            time_series, 
            max_dim=self.max_dim
        )
        
        # Compute boundary operators and heat kernels
        boundary_ops = construct_boundary_operators(simplices)
        processor = SimplicialSignalProcessor(simplices, boundary_ops)
        processor.compute_all_heat_kernels(self.time_points)
        
        # Extract features
        features = processor.extract_features(time_series, self.time_points)
        
        return features
    
    def analyze_group(self, subject_list, labels=None):
        """
        Analyze group of subjects.
        
        Args:
            subject_list: List of (fmri_file, atlas) tuples
            labels: Optional group labels
        
        Returns:
            feature_matrix: Subject × Feature matrix
        """
        all_features = []
        
        for fmri_file, atlas in subject_list:
            fmri_data = nibabel.load(fmri_file)
            features = self.process_subject(fmri_data, atlas)
            all_features.append(features)
        
        # Convert to matrix
        import pandas as pd
        df = pd.DataFrame(all_features)
        
        return df
```

## Applications
- **Functional connectivity smoothing** with higher-order context
- **Network distance metrics** for brain connectivity analysis
- **Multi-scale clustering** of brain regions
- **Disease classification** (ADHD, ASD, Alzheimer's)
- **Dynamic network analysis** with time-varying heat kernels

## Advantages Over Standard Graph Methods

| Aspect | Graph Laplacian | Simplicial Heat Kernel |
|--------|-----------------|------------------------|
| Structure | Vertices, edges | Vertices, edges, faces, ... |
| Laplacian | L_0 only | L_0, L_1, L_2, ... |
| Signal | Vertex signals | Signals on all dimensions |
| Smoothing | Local averaging | Multi-scale diffusion |
| Higher-order | Not captured | Explicitly modeled |

## Pitfalls
- **Computational cost**: Hodge Laplacian computation scales with simplex count
- **Simplex explosion**: Large cliques create many higher-order simplices
- **Threshold sensitivity**: Correlation threshold affects simplex structure
- **Interpretation**: Higher-order features need domain expertise
- **Eigenvalue computation**: Large matrices require approximate methods

## Related Skills
- combinatorial-complex-brain-fmri
- higher-order-brain-networks
- dcho-higher-order-brain-connectivity
- brain-higher-order-structures

## References
```bibtex
@article{dakurah2025heatkernels,
  title={Discrete Heat Kernels on Simplicial Complexes and Its Application to Functional Brain Networks},
  author={Dakurah, Sixtus},
  journal={arXiv preprint arXiv:2509.16908},
  year={2025}
}
```
