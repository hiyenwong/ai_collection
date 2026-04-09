# PTGB: Pre-Train Graph Neural Networks for Brain Network Analysis

**Source:** arXiv:2305.14376 (CHIL 2023)
**Utility:** 0.94
**Created:** 2026-03-25

## Activation Keywords

- PTGB
- pre-train GNN brain network
- brain network pre-training
- unsupervised GNN brain
- parcellation atlas mapping
- transfer learning brain network

## Description

A GNN pre-training framework for brain network analysis that captures intrinsic brain network structures without task-specific labels, enabling knowledge transfer across datasets with different ROI systems.

## Core Methodology

### 1. Problem: Limited Labeled Brain Network Data

**Challenge:**
- Deep models require large labeled datasets
- Brain network data is scarce due to acquisition complexity
- Sharing restrictions limit dataset sizes

**Solution:** Pre-training framework that learns from unlabeled brain networks

### 2. PTGB Framework Components

**Component 1: Unsupervised Pre-training**
- Learns intrinsic brain network structures
- Does not require clinical outcome labels
- Can leverage large-scale unlabeled datasets

**Component 2: Data-Driven Parcellation Atlas**
- Maps across different ROI systems
- Facilitates knowledge transfer
- Handles heterogeneous datasets

### 3. Key Innovations

**Brain-Specific Pre-training:**
- Captures network topology patterns
- Preserves structural properties
- Adapts to downstream tasks

**Cross-Dataset Transfer:**
- Handles varying ROI definitions
- Atlas mapping enables transfer
- Works across different parcellations

## Implementation Framework

```python
# Conceptual PTGB framework
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv

class PTGBPreTrainer:
    """
    Pre-training framework for brain network GNNs
    """
    
    def __init__(self, gnn_encoder, hidden_dim=128):
        self.encoder = gnn_encoder
        self.projection_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def pretrain(self, brain_networks, epochs=100):
        """
        Unsupervised pre-training on brain networks
        
        Args:
            brain_networks: List of (adjacency_matrix, node_features)
        """
        for epoch in range(epochs):
            for adj, features in brain_networks:
                # Encode brain network
                embeddings = self.encoder(features, adj)
                
                # Pre-training objective (e.g., contrastive, reconstruction)
                loss = self.compute_pretrain_loss(embeddings, adj)
                
                loss.backward()
    
    def compute_pretrain_loss(self, embeddings, adj):
        """
        Brain network-specific pre-training loss
        
        Could include:
        - Edge prediction
        - Node attribute reconstruction
        - Contrastive learning
        """
        pass


class ParcellationAtlasMapper:
    """
    Maps brain networks across different ROI systems
    """
    
    def __init__(self, source_atlas, target_atlas):
        self.source_atlas = source_atlas
        self.target_atlas = target_atlas
        self.mapping_matrix = self.compute_mapping()
    
    def compute_mapping(self):
        """
        Compute mapping between atlas ROI systems
        
        Methods:
        - Spatial overlap
        - Functional similarity
        - Data-driven alignment
        """
        pass
    
    def transfer_network(self, source_network):
        """Transfer brain network to target atlas"""
        pass


class PTGBDownstream(nn.Module):
    """
    Fine-tuned model for downstream tasks
    """
    
    def __init__(self, pretrained_encoder, num_classes):
        super().__init__()
        self.encoder = pretrained_encoder
        self.classifier = nn.Linear(hidden_dim, num_classes)
        
        # Optionally freeze encoder
        # for param in self.encoder.parameters():
        #     param.requires_grad = False
    
    def forward(self, features, adj):
        embeddings = self.encoder(features, adj)
        logits = self.classifier(embeddings)
        return logits
```

## Applications

### 1. Disease Classification
- Alzheimer's disease detection
- Autism spectrum disorder classification
- Mental disorder diagnosis

### 2. Brain Development Analysis
- Developmental trajectory prediction
- Age estimation from brain networks

### 3. Multi-Site Studies
- Transfer across scanning sites
- Harmonize different parcellations

## Experimental Results

- **Superior performance** vs. training from scratch
- **Robust transfer** across datasets
- **Effective** with limited labeled data

## When to Use

- Brain network analysis with limited labels
- Transfer learning across ROI systems
- Multi-site neuroimaging studies
- When labeled brain network data is scarce

## Related Skills

- `gnn-transformer-fusion` - GNN architectures for neural data
- `multimodal-brain-connectivity-gnn` - Multi-modal integration
- `brain-graph-augmentation-template` - Brain graph preprocessing

## References

- Yang, Y., et al. "PTGB: Pre-Train Graph Neural Networks for Brain Network Analysis." CHIL 2023.
- Graph Neural Networks for brain networks
- Transfer learning in neuroimaging