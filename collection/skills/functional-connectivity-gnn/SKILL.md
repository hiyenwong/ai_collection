---
name: functional-connectivity-graph-neural-networks-(fcg
description: Skill for AI agent capabilities
---

# Functional Connectivity Graph Neural Networks (FCGNN)

## Overview

**Source:** arXiv:2508.05786v1
**Utility:** 0.91
**Topic:** Brain-inspired GNN with structural + functional connectivity
**Key Contribution:** Persistent graph homology for global topological features

## Activation Keywords

- functional connectivity GNN
- FCGNN
- persistent graph homology
- structural functional GNN
- multi-modal graph neural network

## Core Innovation

### Problem
- Real-world networks need **local + global** interactions
- Traditional GNNs focus on local message passing
- Global topology often missed

### Solution
**Functional Connectivity GNN (FCGNN):**
- **Functional Connectivity Block** - Captures global topology via persistent homology
- **Structural Connectivity Block** - Local graph convolution
- **Multi-modal Fusion** - Brain-inspired architecture

### Brain Inspiration

| Brain Imaging | FCGNN |
|---------------|-------|
| Structural Connectivity (SC) | Graph convolution (local) |
| Functional Connectivity (FC) | Persistent homology (global) |
| Multi-modal Fusion | SC + FC fusion layer |

## Architecture

```
Input Graph → [Structural Block] → Local Features
           → [Functional Block] → Global Features (Persistent Homology)
           → [Fusion Layer] → Graph-level Classification
```

### Structural Connectivity Block

```python
class StructuralBlock(nn.Module):
    """Local graph convolution - captures pairwise interactions"""
    def forward(self, x, edge_index):
        # Standard GCN/GAT message passing
        for layer in self.layers:
            x = layer(x, edge_index)
        return x  # Node embeddings
```

### Functional Connectivity Block

```python
class FunctionalBlock(nn.Module):
    """Global topology via persistent graph homology"""
    def forward(self, x, edge_index):
        # Compute persistent homology
        persistence_diagram = compute_persistence(x, edge_index)
        
        # Convert to features
        global_features = persistence_to_features(persistence_diagram)
        return global_features  # Graph-level features
```

### Persistent Graph Homology

```python
def compute_persistence(node_features, edge_index):
    """
    Compute persistent homology of graph
    Captures topological features: connected components, cycles, voids
    """
    # Build filtration (node importance ordering)
    filtration = build_filtration(node_features)
    
    # Compute persistence diagrams
    diagrams = persistent_homology(filtration)
    
    # Extract features from diagrams
    features = extract_persistence_features(diagrams)
    return features
```

### Multi-Modal Fusion

```python
class FCGNN(nn.Module):
    def forward(self, x, edge_index, batch):
        # Local features (structural)
        local_features = self.structural_block(x, edge_index)
        local_graph = global_mean_pool(local_features, batch)
        
        # Global features (functional/topological)
        global_features = self.functional_block(x, edge_index)
        
        # Fusion
        combined = torch.cat([local_graph, global_features], dim=-1)
        output = self.classifier(combined)
        return output
```

## Key Features

| Feature | Local (SC) | Global (FC) |
|---------|------------|-------------|
| Captures | Pairwise edges | Topological structure |
| Method | Message passing | Persistent homology |
| Output | Node embeddings | Persistence features |
| Scale | Neighborhood | Whole graph |

## Benefits

1. **Complementary Views** - Local structure + global topology
2. **Brain-Inspired** - Generalizes SC/FC analysis to other domains
3. **Performance Gains** - Consistent improvements across datasets
4. **Interpretability** - Persistence features are meaningful

## Applications

- **Graph Classification** - Molecular, social, biological networks
- **Brain Network Analysis** - Disease classification
- **Multi-modal Networks** - Any domain with structure + function
- **Topological ML** - Persistent homology for GNNs

## Implementation

```python
import torch
import torch_geometric

class FCGNN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        
        # Structural block (GCN layers)
        self.structural = torch_geometric.nn.Sequential(
            torch_geometric.nn.GCNConv(input_dim, hidden_dim),
            torch_geometric.nn.GCNConv(hidden_dim, hidden_dim),
        )
        
        # Functional block (persistent homology)
        self.functional = PersistenceFeatureExtractor(hidden_dim)
        
        # Fusion classifier
        self.classifier = torch.nn.Sequential(
            torch.nn.Linear(hidden_dim * 2, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        
        # Structural
        local = self.structural(x, edge_index)
        local_graph = torch_geometric.nn.global_mean_pool(local, batch)
        
        # Functional
        global_feat = self.functional(x, edge_index, batch)
        
        # Fusion
        combined = torch.cat([local_graph, global_feat], dim=-1)
        return self.classifier(combined)
```

## Connection to Existing Skills

| Skill | Relation |
|-------|----------|
| `gnn-transformer-fusion` | Similar multi-modal fusion concept |
| `dcho-higher-order-brain-connectivity` | Higher-order topology |
| `discrete-heat-kernels-simplicial` | Topological methods |
| `graph-laplacian-denoising` | Graph spectral methods |

## Description

Functional Connectivity Graph Neural Networks (FCGNN)

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Complementary Views

### Step 2: Brain-Inspired

### Step 3: Performance Gains

### Step 4: Interpretability

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Functional Connectivity Graph Neural Networks (FCGNN) to my analysis.

**Agent:** I'll help you apply functional-connectivity-gnn. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for functional-connectivity-gnn?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2508.05786
- DOI: https://doi.org/10.48550/arXiv.2508.05786
- Related: Brain SC/FC analysis, persistent homology

---

**Created:** 2026-03-28
**Source:** arXiv:2508.05786v1 - "Functional Connectivity Graph Neural Networks"