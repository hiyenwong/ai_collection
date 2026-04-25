---
name: magnet-brain-structure-function-gnn
description: "Multi-scale Adaptive Graph Network (MAGNet) for learning structural-functional brain representations. Transformer-style GNN that adaptively learns structure-function interactions from multi-modal brain imaging (sMRI, fMRI). Use for: brain disorder diagnosis, cognitive state prediction, Alzheimer's detection, brain connectivity analysis. Activation keywords: MAGNet, brain structure-function, graph neural network, brain imaging, fMRI, sMRI, cognitive insight, brain disorder diagnosis."
---

# MAGNet: Multi-Scale Adaptive Graph Network for Brain Structure-Function Learning

MAGNet is a Transformer-style graph neural network framework that adaptively learns interactions between brain structure and function from multi-modal imaging data.

## Overview

Understanding how brain structure and function interact is key to explaining intelligence. MAGNet addresses the challenge of modeling these complementary aspects jointly:

- **Structural Connectome**: Captures anatomical connectivity between brain regions
- **Functional Connectome**: Captures dynamic activity correlations
- **Multi-Scale Learning**: Extracts features at multiple scales using adaptive attention

## Core Architecture

### Source-Based Morphometry (SBM)
- Extracts inter-regional morphological features from structural MRI
- Captures structural covariation patterns across brain regions
- Provides structural prior for functional analysis

### Adaptive Graph Attention
- Multi-head attention mechanism over brain regions
- Learns dynamic importance weights for structural-functional coupling
- Captures both local and global connectivity patterns

### Multi-Scale Feature Learning
- Hierarchical feature extraction at multiple spatial scales
- Aggregates information from micro to macro brain organization
- Enables comprehensive brain state representation

## Implementation

### Data Preprocessing

```python
import numpy as np
import torch
from torch_geometric.data import Data

def preprocess_brain_data(sMRI_path, fMRI_path, atlas):
    """Preprocess multi-modal brain imaging data."""
    # Load and parcellate sMRI
    sMRI_data = load_nifti(sMRI_path)
    structural_features = extract_sbm_features(sMRI_data, atlas)
    
    # Load and parcellate fMRI
    fMRI_data = load_nifti(fMRI_path)
    functional_features = extract_functional_connectivity(fMRI_data, atlas)
    
    # Build adjacency matrix from structural connectivity
    adj_matrix = build_structural_adjacency(structural_features)
    edge_index = dense_to_sparse(adj_matrix)
    
    # Create PyG Data object
    data = Data(
        x=torch.tensor(functional_features, dtype=torch.float),
        edge_index=edge_index,
        structural_attr=torch.tensor(structural_features, dtype=torch.float)
    )
    
    return data
```

### MAGNet Model

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GATConv, global_mean_pool

class MAGNet(nn.Module):
    """Multi-Scale Adaptive Graph Network for brain analysis."""
    
    def __init__(self, in_channels, hidden_channels=128, out_channels=2,
                 num_heads=4, num_layers=3):
        super().__init__()
        
        self.num_layers = num_layers
        
        # Initial projection
        self.node_encoder = nn.Linear(in_channels, hidden_channels)
        self.structural_encoder = nn.Linear(in_channels, hidden_channels)
        
        # Multi-scale GAT layers
        self.convs = nn.ModuleList()
        self.structural_fusion = nn.ModuleList()
        
        for i in range(num_layers):
            self.convs.append(
                GATConv(hidden_channels, hidden_channels // num_heads,
                       heads=num_heads, concat=True, dropout=0.1)
            )
            self.structural_fusion.append(
                nn.Sequential(
                    nn.Linear(hidden_channels * 2, hidden_channels),
                    nn.ReLU(),
                    nn.Dropout(0.1)
                )
            )
        
        # Multi-scale pooling
        self.scale_weights = nn.Parameter(torch.ones(num_layers))
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(hidden_channels * num_layers, hidden_channels),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_channels, out_channels)
        )
        
    def forward(self, data):
        """Forward pass."""
        x, edge_index = data.x, data.edge_index
        s_attr = data.structural_attr
        
        # Encode features
        x = F.relu(self.node_encoder(x))
        s = F.relu(self.structural_encoder(s_attr))
        
        # Multi-scale feature extraction
        multi_scale_features = []
        
        for i in range(self.num_layers):
            # Graph attention
            x = self.convs[i](x, edge_index)
            x = F.relu(x)
            
            # Fuse structural information
            x_fused = torch.cat([x, s], dim=-1)
            x = self.structural_fusion[i](x_fused)
            
            multi_scale_features.append(x)
        
        # Adaptive scale aggregation
        scale_weights = F.softmax(self.scale_weights, dim=0)
        aggregated = torch.cat([
            multi_scale_features[i] * scale_weights[i]
            for i in range(self.num_layers)
        ], dim=-1)
        
        # Global pooling
        if hasattr(data, 'batch'):
            pooled = global_mean_pool(aggregated, data.batch)
        else:
            pooled = aggregated.mean(dim=0, keepdim=True)
        
        # Classification
        out = self.classifier(pooled)
        
        return out
```

### Training

```python
def train_magnet(model, train_loader, val_loader, epochs=100, lr=1e-3):
    """Train MAGNet model."""
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)
    criterion = nn.CrossEntropyLoss()
    
    best_val_acc = 0
    
    for epoch in range(epochs):
        # Training
        model.train()
        train_loss = 0
        train_correct = 0
        
        for data in train_loader:
            optimizer.zero_grad()
            out = model(data)
            loss = criterion(out, data.y)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            pred = out.argmax(dim=1)
            train_correct += (pred == data.y).sum().item()
        
        # Validation
        model.eval()
        val_correct = 0
        
        with torch.no_grad():
            for data in val_loader:
                out = model(data)
                pred = out.argmax(dim=1)
                val_correct += (pred == data.y).sum().item()
        
        val_acc = val_correct / len(val_loader.dataset)
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_magnet.pt')
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Val Acc={val_acc:.4f}")
    
    return best_val_acc
```

## Applications

### Alzheimer's Disease Detection
- Classify AD vs. healthy controls
- Uses structural MRI for morphological features
- Uses fMRI for functional connectivity

### Cognitive State Prediction
- Predict cognitive scores from brain imaging
- Multi-task learning for different cognitive domains

### Brain Disorder Diagnosis
- Generalizable across different neurological conditions
- Transfer learning from large datasets

## Key Features

1. **Adaptive Attention**: Learns dynamic importance of connections
2. **Multi-Scale**: Captures brain organization at multiple levels
3. **Structure-Function Fusion**: Combines complementary information
4. **Interpretable**: Attention weights reveal important brain regions

## Data Requirements

- **sMRI**: T1-weighted structural MRI
- **fMRI**: Resting-state or task-based functional MRI
- **Atlas**: Brain parcellation (e.g., AAL, Desikan-Killiany)

## Performance

- State-of-the-art on ADNI dataset for Alzheimer's detection
- Improved generalization across different scanners/sites
- Robust to missing modalities

## Reference

- Paper: "Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight" (arXiv:2603.29967v1, March 2026)

## Tools

- PyTorch and PyTorch Geometric
- Nilearn for neuroimaging preprocessing
- ANTs or FSL for image registration
