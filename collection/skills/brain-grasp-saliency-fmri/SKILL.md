---
name: brain-grasp-saliency-fmri
description: "Brain-Grasp: Graph-based Saliency Priors for fMRI-based visual brain decoding. Uses graph-structured saliency priors to preserve object-level structure and semantic fidelity in fMRI-to-image reconstruction. Use when: fMRI decoding, visual reconstruction, brain-guided image generation, saliency-guided decoding, fMRI-to-image, neural representation decoding."
---

# Brain-Grasp: Graph-Based Saliency for fMRI Visual Decoding

## Overview

fMRI-based visual decoding enhanced by graph-structured saliency priors:
- **Saliency priors**: Object-level structure information extracted from fMRI patterns
- **Graph representation**: Spatial relationships between salient regions modeled as graphs
- **Semantic fidelity**: Preserves object identity and spatial arrangement in reconstructions

## Source

**Paper:** Brain-Grasp: Graph-based Saliency Priors for Improved fMRI-based Visual Brain Decoding
**arXiv:** 2604.10617v1

## Problem

Current fMRI-to-image reconstruction approaches often lose object-level structure, struggle with semantic fidelity, and treat fMRI voxels as flat vectors ignoring spatial organization.

## Solution

Use graph-based saliency to guide reconstruction:
1. Extract saliency maps from fMRI activity patterns
2. Build graph where nodes = salient regions, edges = spatial relationships
3. Use graph representation as prior for image generation

## Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SaliencyGraphBuilder(nn.Module):
    def __init__(self, n_regions=8, feature_dim=256):
        super().__init__()
        self.n_regions = n_regions
        self.saliency_predictor = nn.Sequential(
            nn.Linear(15000, 1024),
            nn.ReLU(),
            nn.Linear(1024, n_regions * 2)
        )
        self.region_encoder = nn.Sequential(
            nn.Linear(15000, 512),
            nn.ReLU(),
            nn.Linear(512, feature_dim)
        )
    
    def build_graph(self, fmri):
        positions = self.saliency_predictor(fmri)
        positions = positions.view(-1, self.n_regions, 2)
        region_features = self.region_encoder(fmri)
        region_features = region_features.view(-1, self.n_regions, -1)
        adj = self._compute_adjacency(positions)
        return region_features, adj, positions
    
    def _compute_adjacency(self, positions):
        dist = torch.cdist(positions, positions)
        adj = torch.exp(-dist ** 2 / 0.1)
        adj = adj * (1 - torch.eye(adj.shape[1], device=adj.device))
        return adj

class BrainGraspDecoder(nn.Module):
    def __init__(self, feature_dim=256, latent_dim=512):
        super().__init__()
        self.saliency_graph = SaliencyGraphBuilder(n_regions=8, feature_dim=feature_dim)
        self.graph_conv = nn.Sequential(
            nn.Linear(feature_dim, latent_dim),
            nn.ReLU(),
            nn.Linear(latent_dim, latent_dim)
        )
        self.conditioner = nn.Sequential(
            nn.Linear(latent_dim + feature_dim, 768),
            nn.ReLU()
        )
    
    def forward(self, fmri):
        region_features, adj, positions = self.saliency_graph.build_graph(fmri)
        enhanced = self.graph_conv(region_features)
        graph_repr = enhanced.mean(dim=1)
        condition = self.conditioner(
            torch.cat([graph_repr, region_features.mean(dim=1)], dim=-1)
        )
        return condition, positions, adj
```

## Key Advantages

1. **Object-level structure**: Saliency graph captures which objects are present and where
2. **Spatial relationships**: Edges encode relative positions, improving spatial fidelity
3. **Computationally efficient**: Graph is lightweight compared to full voxel processing
4. **Interpretable**: Saliency regions correspond to meaningful visual elements

## Applications

- Visual brain decoding for communication (locked-in patients)
- Neural representation analysis
- Understanding visual processing in the brain
- Dream content reconstruction research

## Activation Keywords
- brain-grasp, fMRI visual decoding, saliency-guided reconstruction, fMRI-to-image
- graph-based fMRI, brain-guided image generation, visual neural decoding
