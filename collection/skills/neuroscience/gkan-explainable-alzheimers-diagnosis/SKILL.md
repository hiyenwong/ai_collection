---
name: gkan-explainable-alzheimers-diagnosis
description: "GKAN (Graph Kolmogorov-Arnold Network) for explainable Alzheimer's disease diagnosis using GCN-KAN on ADNI data. Achieves 4-8% accuracy improvement over standard GCNs with interpretable B-spline activation functions. Activation: Alzheimer diagnosis, KAN, graph neural network Alzheimer, explainable brain disease, GKAN, Kolmogorov Arnold network neuroimaging."
---

# GKAN: Explainable Alzheimer's Diagnosis via Graph Kolmogorov-Arnold Networks

> Combines Graph Convolutional Networks with Kolmogorov-Arnold Networks for interpretable, accurate Alzheimer's disease diagnosis from brain connectivity data, achieving 4-8% improvement over standard GCN baselines.

## Metadata
- **Source**: arXiv:2504.00946
- **Authors**: Tianqi Ding, Dawei Xiang, Keith E Schubert, Liang Dong
- **Published**: 2025-04-01
- **Category**: cs.CV (Computer Vision and Pattern Recognition)
- **Dataset**: ADNI (Alzheimer's Disease Neuroimaging Initiative)

## Core Methodology

### Key Innovation
Replaces fixed activation functions in GCN layers with learnable **Kolmogorov-Arnold Network (KAN) layers** using B-spline basis functions. This enables:
1. **Higher accuracy**: Better function approximation capacity than fixed ReLU/sigmoid
2. **Interpretability**: B-spline activation functions are visually inspectable
3. **Explainability**: Can identify which brain regions and connections contribute most to diagnosis

### Architecture: GKAN
```
Input: Brain connectivity graph (nodes = ROI, edges = functional connections)
  ↓
GCN Layer (spatial feature aggregation from neighboring brain regions)
  ↓  
KAN Layer (B-spline based learnable activation on each node)
  ↓
[Repeat GCN + KAN blocks]
  ↓
Classification Head → AD / MCI / CN diagnosis
```

### Technical Components

#### Kolmogorov-Arnold Representation
- Based on the Kolmogorov-Arnold representation theorem: any continuous function can be decomposed into sums of univariate functions
- Uses B-spline parameterization for the univariate functions
- Grid size controls the approximation resolution

#### Graph Convolutional Component
- Standard GCN message passing for aggregating features from connected brain regions
- Brain ROIs as graph nodes, functional/structural connections as edges
- Multi-layer aggregation captures multi-hop neighborhood patterns

#### B-Spline Activation
- Replaces fixed nonlinearities (ReLU, sigmoid) with learnable B-splines
- Each node/feature has its own learned activation function
- Spline coefficients are optimized during training
- Visually interpretable — plot activation shapes to understand learned transformations

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch, PyTorch Geometric
- NumPy, SciPy
- ADNI dataset or similar brain connectivity data

### Step-by-Step
1. **Data Preparation**: Extract brain ROI time series from fMRI; compute functional connectivity matrices
2. **Graph Construction**: Build brain graph (nodes=ROIs, edges=connectivity threshold)
3. **Model Setup**: Initialize GKAN with desired number of GCN+KAN blocks
4. **Training**: Train with cross-entropy loss for AD/MCI/CN classification
5. **Interpretation**: Visualize learned B-spline activations; analyze node importance

### Code Example
```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv

class KANLayer(nn.Module):
    """Kolmogorov-Arnold Network layer with B-spline activation."""
    def __init__(self, in_features, out_features, grid_size=5):
        super().__init__()
        self.grid_size = grid_size
        self.in_features = in_features
        self.out_features = out_features
        # B-spline control points
        self.spline_weight = nn.Parameter(
            torch.randn(out_features, in_features, grid_size + 1)
        )
        self.base_weight = nn.Parameter(torch.randn(out_features, in_features))
        
    def forward(self, x):
        # B-spline basis expansion + linear transformation
        base_out = x @ self.base_weight.T
        spline_out = self.b spline_forward(x)
        return base_out + spline_out

class GKANBlock(nn.Module):
    """Graph KAN block: GCN spatial aggregation + KAN activation."""
    def __init__(self, in_dim, out_dim, grid_size=5):
        super().__init__()
        self.gcn = GCNConv(in_dim, out_dim)
        self.kan = KANLayer(out_dim, out_dim, grid_size)
        
    def forward(self, x, edge_index):
        x = self.gcn(x, edge_index)
        x = self.kan(x)
        return x

class GKAN(nn.Module):
    """Full GKAN model for brain connectivity classification."""
    def __init__(self, input_dim, hidden_dim, num_classes, num_layers=3):
        super().__init__()
        self.blocks = nn.ModuleList()
        dims = [input_dim] + [hidden_dim] * num_layers
        for i in range(num_layers):
            self.blocks.append(GKANBlock(dims[i], dims[i+1]))
        self.classifier = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x, edge_index):
        for block in self.blocks:
            x = torch.relu(block(x, edge_index))
        return self.classifier(x.mean(dim=0, keepdim=True))
```

## Applications
- **Alzheimer's disease diagnosis**: Classify AD, MCI, CN from brain connectivity
- **Explainable neuroimaging AI**: Visualize which connections drive predictions
- **Brain biomarker discovery**: Identify disease-relevant brain circuits
- **Clinical decision support**: Provide interpretable AI-assisted diagnosis
- **Other neurological disorders**: Framework generalizable to other brain connectivity disorders

## Pitfalls
- B-spline grid size is a sensitive hyperparameter — too small underfits, too large overfits
- Requires sufficient training samples (ADNI dataset provides adequate size)
- KAN layers add parameters — risk of overfitting on small datasets
- Brain parcellation choice (ROI atlas) significantly affects graph structure and results
- Interpretability of individual B-spline shapes requires domain expertise

## Performance Highlights
- **4-8% accuracy improvement** over standard GCN baselines on ADNI
- Competitive with state-of-the-art while providing interpretability
- Evaluated on ADNI dataset with standard train/val/test splits

## Related Skills
- brain-graph-neural
- multimodal-brain-connectivity-gnn
- okannet-brain-tumor-segmentation
- alzheimer-pet-suvr-network-models
- brain-mri-foundation-clinical
