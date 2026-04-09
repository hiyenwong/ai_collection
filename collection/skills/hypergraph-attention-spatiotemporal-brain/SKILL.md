# Hypergraph Attention Spatio-Temporal Brain Network

## Overview

**Source:** arXiv:2505.12068v1
**Utility:** 0.93
**Topic:** Learning high-order brain relationships with hypergraph attention
**Key Contribution:** Jointly learns informative sparse hypergraph structures + temporal dynamics

## Activation Keywords

- hypergraph brain network
- high-order brain connectivity
- hyperedge spatio-temporal
- brain disease hypergraph
- attention hypergraph fMRI

## Core Innovation

### Problem
- Traditional FC captures only **pairwise** interactions
- Existing hypergraph methods use **predefined** structures
- **Temporal information** often overlooked

### Solution
Three-module framework:

1. **Multi-Hyperedge Binary Mask** - Hypergraph structure learning
2. **Hypergraph Self-Attention Aggregation** - Spatial features via adaptive attention
3. **Spatio-Temporal Low-Dimensional Network** - Discriminative representations

### Information Bottleneck Principle

Objective: **Maximize information + Minimize redundancy**
- Retain disease-relevant high-order features
- Suppress irrelevant signals

## Architecture

```
fMRI Data → Multi-Hyperedge Mask → Self-Attention Aggregation → Spatio-Temporal Network → Classification
                ↓                        ↓                            ↓
          Structure Learning       Spatial Features              Temporal Dynamics
```

### Multi-Hyperedge Binary Mask

- Learn sparse hypergraph structure
- Each hyperedge connects multiple brain regions
- Binary mask for structure selection

### Hypergraph Self-Attention

- Adaptive attention across nodes and hyperedges
- Captures spatial high-order features
- Aggregation: node-to-hyperedge + hyperedge-to-node

### Spatio-Temporal Network

- Low-dimensional representation extraction
- Temporal dynamics modeling
- Disease classification

## Implementation Steps

### 1. Hypergraph Construction

```python
# Binary mask for hyperedge selection
class MultiHyperedgeMask(nn.Module):
    def __init__(self, n_nodes, n_hyperedges, sparsity=0.1):
        self.mask = nn.Parameter(torch.rand(n_nodes, n_hyperedges))
        self.sparsity = sparsity
    
    def forward(self):
        # Apply threshold for sparse structure
        return (self.mask > self.sparsity).float()
```

### 2. Self-Attention Aggregation

```python
class HypergraphAttention(nn.Module):
    def forward(self, node_features, hyperedge_mask):
        # Node-to-hyperedge aggregation
        hyperedge_features = torch.matmul(hyperedge_mask.T, node_features)
        
        # Self-attention across hyperedges
        attention = F.softmax(self.attention_weights, dim=-1)
        return torch.matmul(attention, hyperedge_features)
```

### 3. Information Bottleneck Loss

```python
def info_bottleneck_loss(features, labels, beta=0.1):
    # Maximize mutual information with labels
    mutual_info = compute_mutual_info(features, labels)
    
    # Minimize redundancy (entropy)
    redundancy = compute_entropy(features)
    
    return -mutual_info + beta * redundancy
```

## Key Features

| Feature | Description |
|---------|-------------|
| Sparse Learning | Only keep informative hyperedges |
| Temporal Dynamics | Capture high-order temporal patterns |
| Disease-Relevant | Focus on features that matter |
| Adaptive Attention | Node-hyperedge importance weighting |

## Applications

- **Brain Disease Classification** - Alzheimer's, Parkinson's, etc.
- **High-Order Interaction Analysis** - Multi-region relationships
- **Temporal Pattern Discovery** - Dynamic hypergraph evolution
- **Feature Selection** - Identify disease-relevant hyperedges

## Connection to sqlite-knowledge-graph

This paper aligns with v0.10.0 Hyperedge features:

| Concept | sqlite-kg | Paper Method |
|---------|-----------|--------------|
| Hyperedge | `kg_add_hyperedge()` | Multi-hyperedge mask |
| Hyperedge Neighbors | `kg_hyperedge_neighbors()` | Node aggregation |
| PageRank | `kg_hypergraph_pagerank()` | Attention weighting |
| Export | `export_dot()` / `export_json()` | Visualization |

## References

- Paper: https://arxiv.org/abs/2505.12068
- DOI: https://doi.org/10.48550/arXiv.2505.12068
- Related: sqlite-knowledge-graph v0.10.0

---

**Created:** 2026-03-28
**Source:** arXiv:2505.12068v1 - "Learning High-Order Relationships with Hypergraph Attention"