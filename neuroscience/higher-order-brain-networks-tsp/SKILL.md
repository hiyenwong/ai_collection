---
name: higher-order-brain-networks-tsp
description: "Multimodal higher-order brain networks using Topological Signal Processing (TSP). Models brain as higher-order topological domain with discrete vector fields. Integrates diffusion MRI and resting-state fMRI to learn subject-specific brain cell complexes for analyzing circulatory information flows beyond pairwise interactions. Activation: higher-order brain networks, topological signal processing, cell complex, circulatory interactions, topological data analysis, dmri fmri integration."
---

# Higher-Order Brain Networks: A Topological Signal Processing Perspective

## Overview

Traditional brain network analysis relies on **pairwise-based models** (graphs) which cannot represent **circulatory** or **higher-order functional interactions** involving three or more brain regions. This framework uses **Topological Signal Processing (TSP)** to model the brain as a **higher-order topological domain** and treats functional interactions as **discrete vector fields** on cell complexes.

**Core Innovation**: Integration of diffusion MRI (structural) and resting-state fMRI (functional) to learn subject-specific **brain cell complexes** that capture statistically validated higher-order interactions.

## Key Features

### 1. Higher-Order Interactions
- **Beyond Pairs**: Captures 3-way, 4-way, and n-way interactions
- **Cell Complexes**: Simplicial complexes and cubical complexes
- **Circulatory Flows**: Cyclic information flows in brain networks

### 2. Topological Signal Processing
- **Discrete Vector Fields**: Functional interactions as flows
- **Hodge Theory**: Decomposition of flows (gradient, curl, harmonic)
- **Spectral Analysis**: Topology-aware frequency analysis

### 3. Multimodal Integration
- **dMRI**: Structural connectivity constraints
- **rs-fMRI**: Functional activity patterns
- **Joint Learning**: Unified topological domain

## Mathematical Background

### Cell Complex
A cell complex **K** consists of:
- **0-cells**: Brain regions (nodes)
- **1-cells**: Pairwise connections (edges)
- **2-cells**: Triple interactions (triangles)
- **k-cells**: k+1-way interactions

### Boundary and Coboundary Operators
```
∂_k: k-cells → (k-1)-cells  (boundary)
δ_k: k-cells → (k+1)-cells  (coboundary)

Laplacian: L_k = ∂_{k+1} δ_k + δ_{k-1} ∂_k
```

### Hodge Decomposition
Any k-field f can be decomposed:
```
f = ∇φ + curl(w) + h

where:
- ∇φ: Gradient component (irrotational)
- curl(w): Curl component (solenoidal)
- h: Harmonic component (both curl-free and divergence-free)
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│          Higher-Order Brain Network Framework                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  dMRI Input              rs-fMRI Input                          │
│  ┌──────────┐           ┌──────────────┐                       │
│  │ Structural│           │   Functional │                       │
│  │ Connectivity│         │   Activity   │                       │
│  └─────┬────┘           └──────┬───────┘                       │
│        │                       │                                │
│        ▼                       ▼                                │
│  ┌──────────┐           ┌──────────────┐                       │
│  │  Streamline│         │  Time Series │                       │
│  │  Tracking │          │   Analysis   │                       │
│  └─────┬────┘           └──────┬───────┘                       │
│        │                       │                                │
│        └───────────┬───────────┘                                │
│                    │                                            │
│                    ▼                                            │
│        ┌──────────────────────┐                                │
│        │   Cell Complex       │                                │
│        │   Construction       │                                │
│        │  ┌────────────────┐  │                                │
│        │  │ 0-cells: Nodes │  │  ← Brain regions               │
│        │  │ 1-cells: Edges │  │  ← Pairwise connections        │
│        │  │ 2-cells: Triangles│ │  ← Triple interactions        │
│        │  │ 3-cells: Tetra │  │  ← 4-way interactions          │
│        │  └────────────────┘  │                                │
│        └──────────┬───────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │  Topological Signal  │                                │
│        │  Processing (TSP)    │                                │
│        │  ┌────────────────┐  │                                │
│        │  │ Hodge Laplacian│  │                                │
│        │  │   L = B B^T    │  │                                │
│        │  └────────────────┘  │                                │
│        └──────────┬───────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │   Flow Analysis      │                                │
│        │  ┌────────────────┐  │                                │
│        │  │ Gradient Flow  │  │  ← Diffusion processes         │
│        │  │ Curl Flow      │  │  ← Circulatory patterns        │
│        │  │ Harmonic Flow  │  │  ← Persistent patterns         │
│        │  └────────────────┘  │                                │
│        └──────────┬───────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │   Higher-Order       │                                │
│        │   Network Metrics    │                                │
│        └──────────────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: Process Structural MRI (dMRI)

```python
from higher_order_networks import dMRIProcessor

# Initialize processor
dmri_proc = dMRIProcessor(
    atlas='desikan_killiany',
    tracking_method='probabilistic',
    n_streamlines=100000
)

# Process dMRI data
dmri_data = load_nifti('subject_dmri.nii.gz')
structural_graph = dmri_proc.process(
    dmri_data,
    bvals='bvals.txt',
    bvecs='bvecs.txt'
)

# Extract structural connectivity matrix
sc_matrix = structural_graph.connectivity_matrix
```

### Step 2: Process Functional MRI (rs-fMRI)

```python
from higher_order_networks import fMRIProcessor

# Initialize processor
fmri_proc = fMRIProcessor(
    atlas='desikan_killiany',
    tr=2.0,  # Repetition time
    bandpass=(0.01, 0.1)  # Hz
)

# Process rs-fMRI data
fmri_data = load_nifti('subject_rsfmri.nii.gz')
time_series = fmri_proc.extract_timeseries(fmri_data)

# Compute functional connectivity
fc_matrix = fmri_proc.compute_fc(time_series)
```

### Step 3: Construct Cell Complex

```python
from higher_order_networks import BrainCellComplex

# Initialize cell complex builder
complex_builder = BrainCellComplex(
    n_regions=68,
    max_order=3  # Include up to tetrahedra (4-way)
)

# Build from structural constraints
complex_builder.build_from_structure(
    sc_matrix=sc_matrix,
    threshold=0.01  # Keep top 1% structural connections
)

# Add functional interactions
complex_builder.add_functional_interactions(
    fc_matrix=fc_matrix,
    significance_test='fdr',
    alpha=0.05
)

# Get cell complex
cell_complex = complex_builder.get_complex()
```

### Step 4: Extract Higher-Order Interactions

```python
# Identify significant higher-order interactions
from higher_order_networks import HigherOrderAnalysis

ho_analysis = HigherOrderAnalysis(cell_complex)

# Extract triple interactions (triangles)
triangles = ho_analysis.extract_simplices(order=2)
print(f"Found {len(triangles)} significant triple interactions")

# Extract quadruple interactions (tetrahedra)
tetrahedra = ho_analysis.extract_simplices(order=3)
print(f"Found {len(tetrahedra)} significant quadruple interactions")

# Analyze circulatory patterns
circulatory_flows = ho_analysis.find_circulatory_flows()
```

### Step 5: Apply Topological Signal Processing

```python
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

# Build Hodge Laplacian
L0 = cell_complex.hodge_laplacian(order=0)  # Node Laplacian
L1 = cell_complex.hodge_laplacian(order=1)  # Edge Laplacian
L2 = cell_complex.hodge_laplacian(order=2)  # Face Laplacian

# Compute eigenvectors (topological Fourier modes)
eigenvalues, eigenvectors = eigsh(L1, k=20, which='SM')

# Decompose functional signals
functional_flow = fc_to_flow(fc_matrix, cell_complex)

# Hodge decomposition
gradient_component, curl_component, harmonic_component = \
    hodge_decomposition(functional_flow, L1)
```

### Step 6: Analyze Flow Components

```python
# Gradient flow: Diffusion-like processes
gradient_energy = np.linalg.norm(gradient_component)
print(f"Gradient component energy: {gradient_energy:.4f}")

# Curl flow: Circulatory processes
curl_energy = np.linalg.norm(curl_component)
print(f"Curl component energy: {curl_energy:.4f}")

# Harmonic flow: Persistent patterns
harmonic_energy = np.linalg.norm(harmonic_component)
print(f"Harmonic component energy: {harmonic_energy:.4f}")

# Flow ratios
total_energy = gradient_energy + curl_energy + harmonic_energy
print(f"Gradient ratio: {gradient_energy/total_energy:.2%}")
print(f"Curl ratio: {curl_energy/total_energy:.2%}")
print(f"Harmonic ratio: {harmonic_energy/total_energy:.2%}")
```

## Implementation Details

### Hodge Laplacian Construction

```python
class HodgeLaplacian:
    """Construct Hodge Laplacian for cell complexes."""
    
    def __init__(self, cell_complex):
        self.cc = cell_complex
        
    def build_laplacian(self, k):
        """Build k-th Hodge Laplacian."""
        
        # Boundary operator B_{k+1}: (k+1)-cells → k-cells
        B_next = self.cc.boundary_operator(k + 1)
        
        # Boundary operator B_k: k-cells → (k-1)-cells
        B_curr = self.cc.boundary_operator(k)
        
        # L_k = B_{k+1} B_{k+1}^T + B_k^T B_k
        L_k = B_next @ B_next.T + B_curr.T @ B_curr
        
        return L_k
```

### Hodge Decomposition

```python
def hodge_decomposition(flow, laplacian):
    """
    Decompose flow into gradient, curl, and harmonic components.
    
    Args:
        flow: Vector field on edges
        laplacian: Hodge Laplacian matrix
        
    Returns:
        gradient, curl, harmonic components
    """
    # Solve for potential (gradient component)
    L0 = get_0_laplacian(laplacian)
    potential = solve(L0, divergence(flow))
    gradient = grad(potential)
    
    # Solve for curl potential
    L2 = get_2_laplacian(laplacian)
    curl_potential = solve(L2, curl(flow))
    curl_comp = curl_T(curl_potential)
    
    # Harmonic is the remainder
    harmonic = flow - gradient - curl_comp
    
    return gradient, curl_comp, harmonic
```

## Use Cases

1. **Circulatory Pattern Analysis**: Identify cyclic information flows
2. **Higher-Order FC Metrics**: Beyond pairwise connectivity
3. **Brain State Characterization**: Multi-region coordination patterns
4. **Disease Biomarkers**: Altered higher-order interactions
5. **Developmental Trajectories**: Changes in complexity over lifespan

## Research Paper Reference

**Title**: Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective  
**Authors**: Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, et al.  
**arXiv**: 2603.29903v1  
**Published**: 2026-03-31  
**Categories**: q-bio.NC, eess.SP

**Key Contributions**:
1. First comprehensive TSP framework for brain networks
2. Joint learning from dMRI and rs-fMRI
3. Subject-specific cell complex construction
4. Analysis of circulatory information flows

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/topology-basics.md](references/topology-basics.md) for TDA background
