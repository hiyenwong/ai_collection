---
name: functional-connectivity-graph-neural-networks
description: "Functional Connectivity Graph Neural Networks methodology combining structural and functional connectivity with persistent graph homology for brain-inspired graph classification. Activation triggers: functional connectivity, graph neural network, persistent homology, brain network, multi-modal GNN."
---

# Functional Connectivity Graph Neural Networks (FC-GNN)

> Brain-inspired graph neural network framework that combines local structural and global functional connectivity through persistent graph homology for improved graph-level classification across diverse networks.

## Metadata
- **Source**: arXiv:2508.05786 [cs.NE]
- **Authors**: Yang Li, Luopeiwen Yi, Tananun Songdechakraiwut
- **Published**: 2025-08-07

## Core Methodology

### Key Innovation
Traditional GNNs typically rely solely on structural connectivity (adjacency information), missing the rich global interaction patterns. FC-GNN introduces a **functional connectivity block** based on **persistent graph homology** to capture global topological features, inspired by multi-modal brain imaging where structural and functional connectivity offer complementary views.

### Technical Framework

#### 1. Structural Connectivity Component
- Standard message passing on the graph structure
- Captures local neighborhood information
- Node features propagate through edges

#### 2. Functional Connectivity Block
- **Persistent Graph Homology**: Computes topological features across multiple scales
- Captures higher-order interactions beyond pairwise connections
- Identifies persistent topological structures (loops, voids, clusters)
- Provides global network organization information

#### 3. Multi-Modal Fusion
- Combines structural and functional representations
- Joint learning from complementary connectivity views
- Enhanced graph-level embeddings for classification

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch Geometric or DGL
- GUDHI or Ripser for persistent homology
- NumPy, SciPy

### Step-by-Step Implementation

```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv, global_mean_pool
from gudhi import RipsComplex  # or alternative PH library

class FunctionalConnectivityGNN(nn.Module):
    """
    FC-GNN: Combining structural and functional connectivity
    """
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        # Structural connectivity layers
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        
        # Functional connectivity processing
        self.fc_encoder = FunctionalConnectivityEncoder(hidden_channels)
        
        # Fusion and classification
        self.fusion = nn.Linear(hidden_channels * 2, hidden_channels)
        self.classifier = nn.Linear(hidden_channels, out_channels)
    
    def forward(self, x, edge_index, batch, node_positions=None):
        # Structural connectivity path
        h_struct = self.conv1(x, edge_index).relu()
        h_struct = self.conv2(h_struct, edge_index)
        
        # Functional connectivity path
        h_func = self.fc_encoder(h_struct, node_positions)
        
        # Multi-modal fusion
        h_combined = torch.cat([h_struct, h_func], dim=-1)
        h_fused = self.fusion(h_combined).relu()
        
        # Graph-level readout
        h_graph = global_mean_pool(h_fused, batch)
        return self.classifier(h_graph)

class FunctionalConnectivityEncoder(nn.Module):
    """
    Encode functional connectivity via persistent homology features
    """
    def __init__(self, hidden_dim):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(10, hidden_dim),  # 10 PH features as example
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def compute_persistence_features(self, node_features, positions):
        """
        Compute persistent homology features from node activations
        """
        # Construct distance matrix based on feature similarity
        dist_matrix = torch.cdist(node_features, node_features)
        
        # Compute persistent homology (simplified)
        # In practice, use GUDHI or Ripser
        persistence_pairs = self._compute_persistence(dist_matrix)
        
        # Extract features: persistence entropy, Betti numbers, etc.
        features = self._extract_topo_features(persistence_pairs)
        return features
    
    def forward(self, node_features, positions):
        ph_features = self.compute_persistence_features(node_features, positions)
        return self.mlp(ph_features)
```

### Persistent Homology Integration

```python
from gudhi import RipsComplex
import numpy as np

def compute_persistent_homology_features(distance_matrix, max_dim=2):
    """
    Compute persistent homology features from distance matrix
    
    Args:
        distance_matrix: Pairwise distance matrix (N x N)
        max_dim: Maximum homology dimension
    
    Returns:
        Dictionary of topological features
    """
    # Create Rips complex
    rips = RipsComplex(distance_matrix=distance_matrix, max_edge_length=2.0)
    simplex_tree = rips.create_simplex_tree(max_dimension=max_dim)
    
    # Compute persistence
    persistence = simplex_tree.persistence()
    
    # Extract features
    features = {
        'betti_0': count_betti_numbers(persistence, 0),
        'betti_1': count_betti_numbers(persistence, 1),
        'persistence_entropy': compute_persistence_entropy(persistence),
        'total_persistence': compute_total_persistence(persistence),
        'lifetime_statistics': compute_lifetime_stats(persistence)
    }
    
    return features

def functional_connectivity_from_activations(node_activations, threshold=0.5):
    """
    Construct functional connectivity from node activations
    
    Similar to fMRI functional connectivity: correlation between
    time series (here: node activations across layers)
    """
    # Correlation-based functional connectivity
    corr_matrix = torch.corrcoef(node_activations.T)
    
    # Threshold to create binary/adjacency representation
    func_adj = (corr_matrix.abs() > threshold).float()
    
    return func_adj
```

## Applications

### 1. Brain Network Analysis
- **fMRI Connectome Classification**: Classify psychiatric disorders from functional connectivity
- **Structural-Functional Integration**: Combine DTI structural and fMRI functional connectivity
- **Multi-Modal Brain Imaging**: Leverage complementary information from different modalities

### 2. General Graph Classification
- **Social Networks**: Capture community structures via functional connectivity
- **Molecular Graphs**: Encode topological drug features
- **Citation Networks**: Model semantic relationships beyond direct citations

### 3. Network Neuroscience
- **Connectome Comparison**: Compare brain networks across populations
- **Developmental Studies**: Track connectivity changes over time
- **Disease Biomarkers**: Identify disrupted connectivity patterns

## Pitfalls

1. **Computational Cost**: Persistent homology computation can be expensive for large graphs
   - *Mitigation*: Use approximations or subsampling for large-scale graphs

2. **Feature Engineering**: Choice of persistence features affects performance
   - *Mitigation*: Experiment with different topological descriptors

3. **Fusion Balance**: Combining structural and functional information requires careful weighting
   - *Mitigation*: Use attention mechanisms or learned fusion strategies

4. **Interpretability**: Topological features can be abstract
   - *Mitigation*: Visualize persistence diagrams and barcode representations

## Related Skills
- brain-graph-neural: GNN methods for brain connectivity
- higher-order-brain-networks: Topological analysis of brain networks
- persistent-homology-brain: Persistent homology applications in neuroscience
- graph-laplacian-denoising: Graph-based denoising for brain networks

## References
```bibtex
@article{li2025functional,
  title={Functional Connectivity Graph Neural Networks},
  author={Li, Yang and Yi, Luopeiwen and Songdechakraiwut, Tananun},
  journal={arXiv preprint arXiv:2508.05786},
  year={2025}
}
```

## Further Reading
- Persistent Homology: Edelsbrunner & Harer, "Computational Topology"
- Brain Functional Connectivity: Fornito et al., "Fundamentals of Brain Network Analysis"
- Graph Neural Networks: Kipf & Welling, "Semi-Supervised Classification with GCN"
