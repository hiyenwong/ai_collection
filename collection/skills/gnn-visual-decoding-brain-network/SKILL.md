---
name: gnn-visual-decoding-brain-network
description: Graph Neural Network approach for decoding visual category representations from large-scale brain functional networks using 7T fMRI data.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-decoding, gnn, fmri, visual-processing, brain-network, cognitive-neuroscience]
    source_paper: "Decoding Functional Networks for Visual Categories via GNNs (arXiv:2603.28931v1)"
---

# GNN-Based Visual Category Decoding from Brain Networks

## Overview
This approach uses Graph Neural Networks to decode visual category representations from high-resolution 7T fMRI data (Natural Scenes Dataset). By modeling brain functional connectivity as a graph and learning category-specific network patterns, the method links perception to cortical organization.

## Core Concepts

### Graph Construction
- **Nodes**: Brain regions/voxels from fMRI
- **Edges**: Functional connectivity (correlation/coherence between regions)
- **Features**: BOLD signal patterns during visual stimulus presentation

### GNN Architecture
- Message passing over functional brain network
- Category-specific attention over brain regions
- Hierarchical aggregation from local to global network patterns

## Implementation Pattern
```python
class BrainNetworkGNN(nn.Module):
    def __init__(self, n_regions, hidden_dim, n_categories):
        super().__init__()
        self.node_encoder = nn.Linear(n_timepoints, hidden_dim)
        self.gcn1 = GraphConv(hidden_dim, hidden_dim)
        self.gcn2 = GraphConv(hidden_dim, hidden_dim)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, n_categories)
        )
    
    def forward(self, bold_signals, adj_matrix):
        h = self.node_encoder(bold_signals)
        h = self.gcn1(h, adj_matrix).relu()
        h = self.gcn2(h, adj_matrix).relu()
        h = h.mean(dim=0)  # Graph-level readout
        return self.classifier(h)
```

## Applications
- Visual cortex mapping and analysis
- Brain-computer interfaces for visual perception
- Cognitive neuroscience research
- Neuroimaging-based category decoding

## Activation Keywords
- brain network decoding, GNN fMRI analysis, visual category decoding, functional connectivity graph, 7T fMRI analysis, Natural Scenes Dataset, 脑网络解码, 图神经网络脑成像

## References
- Decoding Functional Networks for Visual Categories via GNNs
- Authors: Shira Karmi, Galia Avidan, Tammy Riklin Raviv
- Published: 2026-03-30
- arXiv: https://arxiv.org/abs/2603.28931v1