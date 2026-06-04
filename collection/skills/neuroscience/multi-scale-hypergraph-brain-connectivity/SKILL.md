---
name: multi-scale-hypergraph-brain-connectivity
description: "Multi-scale hypergraph learning (MuHL) methodology for high-order brain connectivity analysis beyond pairwise GNNs. Accepted to ICML 2026. Use for: brain network analysis, neurodegenerative disease classification (Alzheimer's, Parkinson's), higher-order functional connectivity, hypergraph neural networks."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.03310"
  published: "2026-06-03"
  authors: "Jaeyoon Sim, Soojin Hwang, Seunghun Baek, Guorong Wu, Won Hwa Kim"
  conference: "ICML 2026"
  tags: [brain-network, hypergraph, multi-scale, neurodegenerative, Alzheimer's, Parkinson's]
---

# MuHL: Multi-Scale Hypergraph Learning for High-Order Brain Connectivity

> **Paper**: "Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis" (arXiv:2606.03310, ICML 2026)
> **Authors**: Jaeyoon Sim, Soojin Hwang, Seunghun Baek, Guorong Wu, Won Hwa Kim

## Core Problem

Graph-based models for brain network analysis primarily focus on **pairwise interactions** (edge = connection between 2 nodes). This misses **higher-order dependencies** across 3+ brain regions that are critical for understanding neurodegenerative disease progression (Alzheimer's, Parkinson's).

## MuHL Methodology

### Architecture

1. **Hierarchical Node Feature Construction**: Build multi-resolution graph signals at different scales of brain network granularity
2. **Adaptive Multi-Scale Hyperedge Learning**: Dynamically construct hyperedges over multi-resolution graph signals (not predefined)
3. **Continuous Hyperedge Construction**: Learn hyperedges continuously rather than discrete predefined sets

### Key Innovation: Dynamic vs Predefined Hyperedges

| Approach | Hyperedge Source | Flexibility | Multi-Resolution |
|----------|-----------------|-------------|-----------------|
| Traditional hypergraphs | Predefined (fixed) | Low | No |
| Weight-only learning | Weights of fixed hyperedges | Medium | No |
| **MuHL (this work)** | **Learned dynamically** | **High** | **Yes** |

### Technical Details

- **Multi-resolution graph signals**: Decompose brain network features at multiple scales
- **Continuous hyperedge construction**: Soft assignment of nodes to hyperedges via learnable parameters
- **Hierarchical aggregation**: Pool features across scales to capture both local and global patterns

### Application Results

- **Alzheimer's Disease classification**: Improved performance across different disease stages
- **Parkinson's Disease classification**: Consistent improvement over graph-based baselines
- **ROI identification**: Learned hyperedges identify key regions and group-wise interactions associated with disease progression

## Reusable Patterns

### Pattern 1: Higher-Order Connectivity Modeling

When pairwise GNNs underperform on brain network tasks:
```
1. Construct multi-scale graph representations
2. Learn hyperedges adaptively (not predefined)
3. Aggregate across hyperedge scales hierarchically
4. Identify disease-relevant ROI groups from learned hyperedges
```

### Pattern 2: Multi-Resolution Brain Network Analysis

```
Input: Brain ROI features + connectivity matrix
├── Scale 1: Fine-grained (individual ROIs)
├── Scale 2: Medium-grained (ROI clusters)
└── Scale 3: Coarse-grained (network modules)
    → Learn hyperedges spanning all scales
    → Hierarchical message passing
    → Disease classification + ROI importance
```

## Comparison with Existing Methods

| Method | Interaction Order | Hyperedge Learning | Disease Classification |
|--------|------------------|-------------------|----------------------|
| GCN/GAT | Pairwise (2-node) | N/A | Baseline |
| Predefined hypergraph | Fixed higher-order | Weights only | Medium |
| **MuHL** | **Adaptive higher-order** | **Full structure learning** | **Best** |

## Pitfalls

- **Predefined hyperedges underutilized**: Manually defining hyperedges from known anatomical regions misses dynamic disease-specific patterns. Always learn hyperedges adaptively from data.
- **Scale mismatch**: Using single-scale features ignores multi-resolution disease signatures. Construct hierarchical features at fine/medium/coarse granularity.
- **Hyperedge cardinality imbalance**: Overly large hyperedges (10+ nodes) dilute signal; overly small (2-3 nodes) revert to pairwise. Balance via learnable cardinality constraints.

## Activation

hypergraph brain connectivity, higher-order brain network, multi-scale hypergraph, neurodegenerative disease classification, Alzheimer's GNN, Parkinson's brain network, MuHL, ICML 2026, brain ROI analysis, multi-resolution brain network

## Related Skills

- [[brain-graph-neural]] - Graph neural networks for brain connectivity
- [[brain-higher-order-structures]] - Higher-order brain network analysis with simplicial complexes
- [[higher-order-brain-networks]] - Higher-order brain network analysis using topological signatures
- [[dcho-higher-order-brain-connectivity]] - DCHO higher-order brain connectivity prediction