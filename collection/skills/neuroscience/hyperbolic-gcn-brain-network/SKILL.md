---
name: hyperbolic-gcn-brain-network
description: "Hyperbolic Graph Convolutional Network (Brain-HGCN) for brain functional network analysis using Lorentz model and signed aggregation for excitatory/inhibitory connections. Activation triggers: hyperbolic GNN, brain network, fMRI analysis, geometric deep learning, Lorentz model."
---

# Brain-HGCN: Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis

> Geometric deep learning framework leveraging hyperbolic geometry and negatively curved space to model hierarchical brain network structures with high fidelity.

## Metadata
- **Source**: arXiv:2509.14965 [cs.CV] (Accepted by ICASSP 2026)
- **Authors**: Junhao Jia, Yunyou Liu, Cheng Yang, Yifei Sun, Feiwei Qin, Changmiao Wang, Yong Peng
- **Published**: 2025-09-18

## Core Methodology

### Key Innovation
Standard Euclidean GNNs struggle to represent brain networks' hierarchical topologies without high distortion. Brain-HGCN leverages **hyperbolic geometry** (specifically the **Lorentz model**) to naturally embed hierarchical structures with minimal distortion, inspired by the tree-like organization of brain functional networks.

### Technical Framework

#### 1. Lorentz Model Foundation
- **Manifold**: $\mathbb{L}^n = \{x \in \mathbb{R}^{n+1} : \langle x, x \rangle_\mathcal{L} = -1, x_0 > 0\}$
- **Lorentz Inner Product**: $\langle x, y \rangle_\mathcal{L} = -x_0y_0 + \sum_{i=1}^n x_iy_i$
- **Distance Metric**: $d_\mathcal{L}(x, y) = \text{arccosh}(-\langle x, y \rangle_\mathcal{L})$

#### 2. Hyperbolic Graph Attention Layer
- Operates directly in hyperbolic space
- Preserves hierarchical relationships
- Avoids distortion from Euclidean projections

#### 3. Signed Aggregation Mechanism
- **Excitatory connections**: Positive weights (activation enhancement)
- **Inhibitory connections**: Negative weights (activation suppression)
- Distinct processing pathways preserve biological interpretation

#### 4. Fréchet Mean Readout
- Geometrically principled graph-level aggregation
- Computes centroid in hyperbolic space
- Preserves hierarchical information during pooling

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch with autograd support
- geoopt or similar hyperbolic optimization library
- NumPy, SciPy, NetworkX

### Step-by-Step Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from geoopt import Lorentz  # Hyperbolic manifold operations
import geoopt.manifolds as manifolds

class BrainHGCN(nn.Module):
    """
    Brain-HGCN: Hyperbolic GCN for brain functional network analysis
    """
    def __init__(self, in_features, hidden_dim, num_classes, curvature=1.0):
        super().__init__()
        self.curvature = curvature
        self.manifold = Lorentz(k=curvature)  # Lorentz model with curvature k
        
        # Dimension of hyperbolic space (ambient dimension = hyperbolic_dim + 1)
        self.hyperbolic_dim = hidden_dim
        
        # Input transformation (Euclidean to Hyperbolic)
        self.input_proj = nn.Linear(in_features, hidden_dim)
        
        # Hyperbolic graph convolution layers
        self.hgc_layers = nn.ModuleList([
            HyperbolicGraphConv(hidden_dim, hidden_dim, self.manifold)
            for _ in range(2)
        ])
        
        # Signed aggregation for excitatory/inhibitory connections
        self.signed_agg = SignedAggregation(self.manifold)
        
        # Fréchet mean pooling
        self.frechet_pool = FrechetMeanPooling(self.manifold)
        
        # Classification head
        self.classifier = nn.Linear(hidden_dim, num_classes)
    
    def expmap0(self, x):
        """Exponential map from tangent space at origin to hyperbolic space"""
        return self.manifold.expmap0(x)
    
    def logmap0(self, x):
        """Logarithmic map from hyperbolic space to tangent space at origin"""
        return self.manifold.logmap0(x)
    
    def forward(self, x, edge_index, edge_type=None, batch=None):
        # x: [N, in_features] - node features
        # edge_index: [2, E] - graph connectivity
        # edge_type: [E] - 1 for excitatory, -1 for inhibitory
        
        # Project to hyperbolic space
        h = self.input_proj(x)
        h = self.expmap0(h)  # Map to Lorentz manifold
        
        # Hyperbolic graph convolution with signed aggregation
        for hgc_layer in self.hgc_layers:
            h = hgc_layer(h, edge_index, edge_type)
            h = self.manifold.expmap0(F.relu(self.manifold.logmap0(h)))
        
        # Fréchet mean pooling for graph-level representation
        h_graph = self.frechet_pool(h, batch)  # [batch_size, hidden_dim]
        
        # Map back to Euclidean for classification
        h_euclidean = self.logmap0(h_graph)
        
        return self.classifier(h_euclidean)

class HyperbolicGraphConv(nn.Module):
    """
    Hyperbolic graph convolution with tangent space operations
    """
    def __init__(self, in_dim, out_dim, manifold):
        super().__init__()
        self.manifold = manifold
        self.linear = nn.Linear(in_dim, out_dim)
        
    def forward(self, x, edge_index, edge_type=None):
        # Aggregate neighbors in tangent space
        src, dst = edge_index
        
        # Log map to tangent space at each node
        x_tangent = self.manifold.logmap0(x)
        
        # Message passing (in tangent space for numerical stability)
        messages = x_tangent[src]
        
        # Apply edge type modulation if available
        if edge_type is not None:
            messages = messages * edge_type.unsqueeze(1)
        
        # Aggregate (mean aggregation)
        aggr = torch.zeros_like(x_tangent)
        aggr.index_add_(0, dst, messages)
        count = torch.bincount(dst, minlength=x.size(0)).float().unsqueeze(1)
        aggr = aggr / (count + 1e-8)
        
        # Transform
        aggr = self.linear(aggr)
        
        # Exp map back to hyperbolic space
        out = self.manifold.expmap0(aggr)
        
        return out

class SignedAggregation(nn.Module):
    """
    Handle excitatory and inhibitory connections separately
    """
    def __init__(self, manifold):
        super().__init__()
        self.manifold = manifold
        
    def forward(self, x, edge_index, edge_type):
        """
        Aggregate excitatory and inhibitory messages separately
        """
        excitatory_mask = edge_type > 0
        inhibitory_mask = edge_type < 0
        
        # Process excitatory connections
        exc_src = edge_index[0][excitatory_mask]
        exc_dst = edge_index[1][excitatory_mask]
        
        # Process inhibitory connections
        inh_src = edge_index[0][inhibitory_mask]
        inh_dst = edge_index[1][inhibitory_mask]
        
        # Combine with different weights (learnable)
        return x  # Simplified - actual implementation would aggregate

class FrechetMeanPooling(nn.Module):
    """
    Compute Fréchet mean in hyperbolic space for graph readout
    """
    def __init__(self, manifold, max_iter=10):
        super().__init__()
        self.manifold = manifold
        self.max_iter = max_iter
        
    def forward(self, x, batch):
        """
        Compute Fréchet mean for each graph in batch
        """
        if batch is None:
            return self.frechet_mean(x.unsqueeze(0)).squeeze(0)
        
        # Group nodes by graph
        num_graphs = batch.max().item() + 1
        means = []
        
        for i in range(num_graphs):
            mask = batch == i
            x_graph = x[mask]
            mean = self.frechet_mean(x_graph.unsqueeze(0))
            means.append(mean.squeeze(0))
        
        return torch.stack(means)
    
    def frechet_mean(self, x, eps=1e-6):
        """
        Iterative computation of Fréchet mean in hyperbolic space
        """
        # Initialize with Euclidean mean mapped to hyperbolic space
        mean = self.manifold.expmap0(x.mean(dim=1, keepdim=True))
        
        for _ in range(self.max_iter):
            # Log map all points to tangent space at current mean
            v = self.manifold.logmap(mean, x)
            
            # Compute mean in tangent space
            v_mean = v.mean(dim=1, keepdim=True)
            
            # Update mean via exponential map
            mean = self.manifold.expmap(mean, v_mean)
            
            if v_mean.norm(dim=-1).mean() < eps:
                break
        
        return mean
```

### Constructing Brain Networks for HGCN

```python
import numpy as np
import torch
from scipy import stats

def construct_brain_functional_network(fmri_time_series, atlas_regions, 
                                       correlation_threshold=0.5):
    """
    Construct functional brain network from fMRI time series
    
    Args:
        fmri_time_series: [num_regions, num_timepoints] BOLD signals
        atlas_regions: List of region names
        correlation_threshold: Threshold for binarizing connectivity
    
    Returns:
        edge_index: [2, num_edges] connectivity
        edge_type: [num_edges] 1 for excitatory, -1 for inhibitory
        node_features: [num_regions, feature_dim] regional features
    """
    num_regions = len(atlas_regions)
    
    # Compute correlation matrix (functional connectivity)
    corr_matrix = np.corrcoef(fmri_time_series)
    
    # Threshold to create edges
    edges = []
    edge_types = []
    
    for i in range(num_regions):
        for j in range(i+1, num_regions):
            if abs(corr_matrix[i, j]) > correlation_threshold:
                edges.append([i, j])
                edges.append([j, i])  # Undirected graph
                
                # Classify as excitatory or inhibitory
                edge_type = 1 if corr_matrix[i, j] > 0 else -1
                edge_types.extend([edge_type, edge_type])
    
    edge_index = torch.tensor(edges, dtype=torch.long).t()
    edge_type = torch.tensor(edge_types, dtype=torch.float)
    
    # Node features: regional time series statistics
    node_features = torch.tensor([
        [
            fmri_time_series[i].mean(),
            fmri_time_series[i].std(),
            stats.entropy(np.abs(fmri_time_series[i]) + 1e-10),
            np.percentile(fmri_time_series[i], 95),
            np.percentile(fmri_time_series[i], 5)
        ]
        for i in range(num_regions)
    ], dtype=torch.float)
    
    return edge_index, edge_type, node_features

# Example usage with ABIDE or similar fMRI dataset
# edge_index, edge_type, node_feats = construct_brain_functional_network(
#     fmri_data, atlas_regions
# )
# model = BrainHGCN(in_features=5, hidden_dim=64, num_classes=2)
# output = model(node_feats, edge_index, edge_type)
```

## Applications

### 1. Psychiatric Disorder Classification
- **Autism Spectrum Disorder (ASD)**: Classify ASD from healthy controls
- **Major Depressive Disorder (MDD)**: Identify depression-related connectivity patterns
- **Schizophrenia**: Detect disrupted hierarchical organization
- **ADHD**: Characterize attention network alterations

### 2. Brain Network Hierarchy Analysis
- **Hierarchical Modularity**: Quantify multi-scale organization
- **Hub Identification**: Find connector and provincial hubs
- **Network Resilience**: Assess robustness to targeted attacks
- **Developmental Trajectories**: Track hierarchy changes across lifespan

### 3. Connectome Fingerprinting
- **Individual Identification**: Unique connectivity signatures
- **Twin Studies**: Genetic vs. environmental influences
- **Longitudinal Tracking**: Stability of individual differences

## Pitfalls

1. **Numerical Stability**: Hyperbolic operations can be numerically unstable
   - *Mitigation*: Use tangent space operations, clamp values, check for NaN

2. **Curvature Selection**: Curvature parameter affects embedding quality
   - *Mitigation*: Treat curvature as learnable parameter or cross-validate

3. **Computational Complexity**: Fréchet mean computation is iterative
   - *Mitigation*: Limit iterations, use approximate methods for large graphs

4. **Edge Type Assignment**: fMRI correlations don't directly map to excitatory/inhibitory
   - *Mitigation*: Use structural connectivity (DWI) to inform sign, or learn from data

5. **Small Sample Sizes**: fMRI datasets often limited
   - *Mitigation*: Data augmentation, transfer learning, or self-supervised pretraining

## Related Skills
- functional-connectivity-graph-neural-networks: Combining structural and functional connectivity
- brain-graph-neural: General GNN methods for brain networks
- geometry-aware-spiking-gnn: Geometric methods in spiking networks
- graph-laplacian-denoising: Denoising for brain connectivity

## References
```bibtex
@article{jia2025brain,
  title={Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis},
  author={Jia, Junhao and Liu, Yunyou and Yang, Cheng and Sun, Yifei and Qin, Feiwei and Wang, Changmiao and Peng, Yong},
  journal={arXiv preprint arXiv:2509.14965},
  year={2025},
  note={Accepted by ICASSP 2026}
}
```

## Further Reading
- Hyperbolic Neural Networks: Ganea et al., "Hyperbolic Neural Networks" (NeurIPS 2018)
- Lorentz Model: Nickel & Kiela, "Learning Continuous Hierarchies in the Lorentz Model"
- Brain Hierarchy: Meunier et al., "Modular and Hierarchically Modular Organization of Brain Networks"
