---
name: combinatorial-complex-brain-fmri
description: "The Human Brain as a Combinatorial Complex - framework for constructing combinatorial complexes from fMRI time series that captures both pairwise and higher-order neural interactions through information-theoretic measures. Bridges topological deep learning and network neuroscience."
---

# The Human Brain as a Combinatorial Complex

> Framework for constructing combinatorial complexes (CCs) from fMRI time series data that captures both pairwise and higher-order neural interactions, bridging topological deep learning and network neuroscience.

## Metadata
- **Source**: arXiv:2511.20692v2
- **Authors**: Valentina Sánchez, Çiçek Güven, Koen Haak, Theodore Papamarkou, Gonzalo Nápoles
- **Published**: 2025-11-22
- **Category**: q-bio.NC, cs.LG, math.AT

## Core Methodology

### Key Innovation
Traditional graph-based representations of brain networks systematically miss higher-order dependencies that characterize neural complexity. This methodology introduces **combinatorial complexes (CCs)** as a unified framework that captures:
- **Pairwise interactions** (edges)
- **Higher-order interactions** (simplices, hyperedges)
- **Information-theoretic relationships** between brain regions

### Theoretical Foundation

#### From Graphs to Combinatorial Complexes

**Graph Limitations**:
- Edges only capture pairwise relationships: G = (V, E)
- Cannot represent simultaneous activity of multiple brain regions
- Misses synergistic interactions (e.g., three regions co-activating)

**Combinatorial Complex Solution**:
- **0-cells**: Vertices (individual brain regions)
- **1-cells**: Edges (pairwise interactions)
- **k-cells**: k-simplices (k+1-way interactions)
- **Incidence relations**: How cells connect across dimensions

#### Information-Theoretic Construction

**Step 1: Time Series to Information Measures**
```
For each subset S ⊆ V of brain regions:
    Compute mutual information I(S) = H(S) - Σ H(v) for v ∈ S
    or multi-information (total correlation)
```

**Step 2: Threshold-Based Cell Construction**
```
For k = 1 to max_order:
    For each (k+1)-subset S of regions:
        If I(S) > θ_k:
            Add k-cell with vertices S to complex
```

**Step 3: Incidence Structure**
- Define boundary operator ∂_k: C_k → C_{k-1}
- ∂_k maps k-cells to their (k-1)-dimensional faces
- Forms chain complex: ... → C_2 → C_1 → C_0 → 0

### Combinatorial Complex Types

#### 1. Simplicial Complex (SC)
- **Property**: Closed under taking subsets
- **Interpretation**: If regions {A,B,C} co-activate, all pairs {A,B}, {B,C}, {A,C} also interact
- **Advantage**: Mathematically well-understood, persistent homology available
- **Constraint**: May overcount (strong closure property)

#### 2. Cell Complex (CC)
- **Property**: More flexible incidence relations
- **Interpretation**: Allows non-simplicial shapes (e.g., cycles without filling)
- **Advantage**: Better fits neural topology
- **Challenge**: More complex computational structure

#### 3. Hypergraph
- **Property**: No closure requirement
- **Interpretation**: Only specific higher-order interactions captured
- **Advantage**: Most flexible
- **Trade-off**: Less algebraic structure for analysis

### Deep Learning Integration

#### Combinatorial Complex Neural Networks (CCNN)

**Message Passing on CCs**:
```
For each cell c in dimension k:
    Aggregate messages from boundary ∂(c) and coboundary δ(c)
    Update representation: h_c^{(t+1)} = UPDATE(h_c^{(t)}, AGG({h_b for b ∈ N(c)}))
```

**Higher-Order Convolutions**:
- **0-order**: Standard node-level features
- **1-order**: Edge-level interactions
- **k-order**: k-way synergistic patterns

#### Brain Network Applications

**fMRI Pipeline**:
```
Preprocessed fMRI → ROI Time Series 
    → Information Estimation 
    → CC Construction 
    → CCNN Learning 
    → Clinical Prediction
```

**Information Estimators**:
- **Gaussian**: For linear correlations
- **K-nearest neighbors**: Non-parametric mutual information
- **Kernel density**: Smooth probability estimates

## Implementation Guide

### Prerequisites
```python
# Required libraries
pip install gudhi            # Topological data analysis
pip install torch-geometric   # Graph neural networks
pip install dit              # Information theory (discrete)
pip install nilearn          # fMRI processing
pip install scipy
```

### Step-by-Step Implementation

#### Step 1: fMRI Data Preparation
```python
import numpy as np
from nilearn import datasets
from nilearn.connectome import ConnectivityMeasure

def load_fmri_data(n_subjects=100):
    """Load and preprocess resting-state fMRI data."""
    # Use publicly available dataset
    dataset = datasets.fetch_abide_pcp(
        data_dir='./data',
        n_subjects=n_subjects,
        pipeline='cpac',
        band_pass_filter=True
    )
    
    # Extract time series using Schaefer atlas
    atlas = datasets.fetch_atlas_schaefer_2018(n_rois=200)
    
    time_series = []
    for func_file in dataset.func_preproc:
        from nilearn.maskers import NiftiLabelsMasker
        masker = NiftiLabelsMasker(
            labels_img=atlas.maps,
            standardize=True,
            detrend=True
        )
        ts = masker.fit_transform(func_file)
        time_series.append(ts)
    
    return time_series, atlas
```

#### Step 2: Information-Theoretic Cell Construction
```python
from sklearn.neighbors import NearestNeighbors
from scipy.stats import entropy

def estimate_mutual_information_knn(X, Y, k=5):
    """K-NN based mutual information estimation."""
    # Kraskov-Stögbauer-Grassberger estimator
    n = len(X)
    
    # Joint space
    XY = np.column_stack([X, Y])
    
    # Find k-nearest neighbors
    nbrs = NearestNeighbors(n_neighbors=k+1).fit(XY)
    distances, _ = nbrs.kneighbors(XY)
    epsilon = distances[:, k]  # Distance to k-th neighbor
    
    # Count neighbors in marginal spaces
    nx = np.array([np.sum(np.abs(X - X[i]) < epsilon[i]) - 1 for i in range(n)])
    ny = np.array([np.sum(np.abs(Y - Y[i]) < epsilon[i]) - 1 for i in range(n)])
    
    # MI estimate
    mi = np.mean(np.log(n / (nx * ny))) + np.log(k) + np.euler_gamma
    
    return max(0, mi)

def construct_simplicial_complex(time_series, threshold_percentile=90, max_dim=3):
    """
    Build simplicial complex from fMRI time series.
    
    Args:
        time_series: [n_regions, n_timepoints] array
        threshold_percentile: Percentile for edge threshold
        max_dim: Maximum simplex dimension
    
    Returns:
        simplices: List of (dimension, vertices) tuples
    """
    n_regions = time_series.shape[0]
    
    # Compute pairwise mutual information
    mi_matrix = np.zeros((n_regions, n_regions))
    for i in range(n_regions):
        for j in range(i+1, n_regions):
            mi = estimate_mutual_information_knn(
                time_series[i], time_series[j]
            )
            mi_matrix[i, j] = mi_matrix[j, i] = mi
    
    # Determine threshold
    threshold = np.percentile(mi_matrix[mi_matrix > 0], threshold_percentile)
    
    # Build edges (1-simplices)
    edges = []
    for i in range(n_regions):
        for j in range(i+1, n_regions):
            if mi_matrix[i, j] > threshold:
                edges.append((i, j))
    
    # Build higher-order simplices
    simplices = [(0, (i,)) for i in range(n_regions)]  # 0-simplices (vertices)
    simplices.extend([(1, edge) for edge in edges])   # 1-simplices (edges)
    
    # Add k-simplices (k >= 2) - check for cliques
    from itertools import combinations
    
    for k in range(2, max_dim + 1):
        # Find all (k+1)-cliques in edge graph
        for vertices in combinations(range(n_regions), k+1):
            # Check if all pairs are connected
            is_clique = all(
                (min(v1, v2), max(v1, v2)) in edges
                for v1, v2 in combinations(vertices, 2)
            )
            if is_clique:
                # Check information criterion for higher-order
                sub_matrix = mi_matrix[np.ix_(vertices, vertices)]
                avg_mi = np.mean(sub_matrix[np.triu_indices_from(sub_matrix, k=1)])
                if avg_mi > threshold * 0.9:  # Slightly relaxed for higher-order
                    simplices.append((k, vertices))
    
    return simplices, mi_matrix
```

#### Step 3: Combinatorial Complex Neural Network
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CCNNLayer(nn.Module):
    """Combinatorial Complex Neural Network Layer."""
    
    def __init__(self, in_channels, out_channels, max_dim=3):
        super().__init__()
        self.max_dim = max_dim
        
        # Separate convolutions for each dimension
        self.convs = nn.ModuleList([
            nn.Linear(in_channels, out_channels)
            for _ in range(max_dim + 1)
        ])
        
        # Inter-dimensional message passing
        self.boundary_convs = nn.ModuleDict()
        for k in range(1, max_dim + 1):
            self.boundary_convs[str(k)] = nn.Linear(in_channels, out_channels)
    
    def forward(self, x_dict, incidence_dict):
        """
        Args:
            x_dict: Dictionary {dim: features [n_cells, in_channels]}
            incidence_dict: Dictionary of boundary/coboundary operators
        Returns:
            out_dict: Updated features
        """
        out_dict = {}
        
        for k in range(self.max_dim + 1):
            h = self.convs[k](x_dict[k])
            
            # Aggregate from boundary (lower dimension)
            if k > 0 and str(k) in incidence_dict:
                boundary_msg = self.aggregate_from_boundary(
                    x_dict[k-1], incidence_dict[str(k)]
                )
                h = h + self.boundary_convs[str(k)](boundary_msg)
            
            # Aggregate from coboundary (higher dimension)
            if k < self.max_dim and str(k+1) in incidence_dict:
                coboundary_msg = self.aggregate_from_coboundary(
                    x_dict[k+1], incidence_dict[str(k+1)]
                )
                h = h + coboundary_msg
            
            out_dict[k] = F.relu(h)
        
        return out_dict
    
    def aggregate_from_boundary(self, x_lower, incidence_matrix):
        """Aggregate messages from boundary cells."""
        # incidence_matrix: [n_cells_k, n_cells_k-1]
        return torch.matmul(incidence_matrix, x_lower)
    
    def aggregate_from_coboundary(self, x_higher, incidence_matrix):
        """Aggregate messages from coboundary cells."""
        # incidence_matrix.T: [n_cells_k, n_cells_k+1]
        return torch.matmul(incidence_matrix.T, x_higher)


class BrainCCNN(nn.Module):
    """Complete CCNN for brain network analysis."""
    
    def __init__(self, feature_dims=[64, 128, 256], max_dim=3, num_classes=2):
        super().__init__()
        self.max_dim = max_dim
        
        # Feature encoder per dimension
        self.encoders = nn.ModuleList([
            nn.Sequential(
                CCNNLayer(feature_dims[i], feature_dims[i+1], max_dim),
                CCNNLayer(feature_dims[i+1], feature_dims[i+1], max_dim)
            )
            for i in range(len(feature_dims) - 1)
        ])
        
        # Global pooling and classification
        self.classifier = nn.Sequential(
            nn.Linear(feature_dims[-1] * (max_dim + 1), 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )
    
    def forward(self, x_dict, incidence_dict):
        # Encode features
        for encoder in self.encoders:
            x_dict = encoder(x_dict, incidence_dict)
        
        # Global average pooling per dimension
        pooled = []
        for k in range(self.max_dim + 1):
            if k in x_dict:
                pooled.append(x_dict[k].mean(dim=0))
        
        # Concatenate all dimensions
        x = torch.cat(pooled, dim=-1)
        
        return self.classifier(x)
```

#### Step 4: Persistent Homology (Optional Enhancement)
```python
import gudhi

def compute_persistent_features(simplices, max_dim=3):
    """Compute persistent homology features from simplicial complex."""
    # Build simplex tree
    st = gudhi.SimplexTree()
    
    for dim, vertices in simplices:
        st.insert(list(vertices), filtration=0.0)
    
    # Compute persistence
    st.compute_persistence()
    
    # Extract features
    features = {}
    for dim in range(max_dim + 1):
        persistence = st.persistence_intervals_in_dimension(dim)
        if len(persistence) > 0:
            features[f'pers_entropy_dim{dim}'] = -np.sum(
                (persistence[:, 1] - persistence[:, 0]) / 
                np.sum(persistence[:, 1] - persistence[:, 0]) * 
                np.log((persistence[:, 1] - persistence[:, 0]) / 
                       np.sum(persistence[:, 1] - persistence[:, 0]))
            )
            features[f'num_features_dim{dim}'] = len(persistence)
    
    return features
```

#### Step 5: Training Pipeline
```python
def train_brain_ccnn(model, train_loader, val_loader, epochs=100):
    """Training loop for brain CCNN."""
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    best_val_acc = 0
    for epoch in range(epochs):
        # Training
        model.train()
        train_loss = 0
        for batch in train_loader:
            x_dict, incidence_dict, labels = batch
            
            optimizer.zero_grad()
            outputs = model(x_dict, incidence_dict)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # Validation
        model.eval()
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for batch in val_loader:
                x_dict, incidence_dict, labels = batch
                outputs = model(x_dict, incidence_dict)
                _, predicted = torch.max(outputs, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()
        
        val_acc = val_correct / val_total
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_brain_ccnn.pt')
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}: Loss={train_loss/len(train_loader):.4f}, Val Acc={val_acc:.4f}")
    
    return best_val_acc
```

## Applications
- **Brain disorder classification** (ADHD, ASD, Alzheimer's)
- **Functional connectivity analysis** beyond pairwise
- **Neural complexity quantification**
- **Higher-order information flow** in brain networks
- **Multi-scale brain network dynamics**

## Advantages Over Graph Methods

| Aspect | Graph | Combinatorial Complex |
|--------|-------|----------------------|
| Interactions | Pairwise only | Any order |
| Structure | Edges | Simplices, cells |
| Algebra | Adjacency matrix | Boundary operators |
| Analysis | Spectral | Topological (homology) |
| Expressiveness | Limited | Rich |

## Pitfalls
- **Computational cost**: Higher-order complexes scale combinatorially
- **Threshold sensitivity**: Cell construction depends on MI threshold
- **Interpretation**: Higher-order features need neuroscientific validation
- **Data requirements**: Need sufficient time points for reliable MI estimation
- **Dimension choice**: Optimal max_dim varies by dataset

## Related Skills
- higher-order-brain-networks
- dcho-higher-order-brain-connectivity
- brain-higher-order-structures
- topological-quantum-computing

## References
```bibtex
@article{sanchez2025combinatorial,
  title={The Human Brain as a Combinatorial Complex},
  author={Sánchez, Valentina and Güven, Çiçek and Haak, Koen and Papamarkou, Theodore and Nápoles, Gonzalo},
  journal={arXiv preprint arXiv:2511.20692},
  year={2025}
}
```
