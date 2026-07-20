---
name: unified-dynamics-graph-neural-computation
description: "Unifying dynamical systems and graph theory to mechanistically understand computation in neural networks. Combines spectral analysis, community detection, and dynamical systems theory to decompose RNN computation into interpretable sub-circuits. Activation: graph theory neural networks, dynamical systems RNN, mechanistic interpretability, spectral analysis RNN, community detection neural computation."
---

# Unifying Dynamical Systems and Graph Theory for Neural Network Computation

> Framework that models recurrent neural networks as graphs and combines spectral analysis, community detection, and dynamical systems theory to mechanistically decompose RNN computation into interpretable sub-circuits.

## Metadata
- **Source**: arXiv:2605.03598v1
- **Authors**: Jatin Sharma, Danyal Akarca, Dan F. M Goodman
- **Published**: 2026-05-05
- **Categories**: cs.NE, cs.AI

## Core Problem

Understanding how biological and artificial neural networks implement computation from connectivity is a central problem in neuroscience and machine learning. In neural systems, structural and functional connectivity are known to diverge, motivating approaches that move beyond direct connections alone.

## Key Innovation

The spatial and temporal function of RNNs trained on hierarchically modular tasks can be recovered by modelling the network as a graph and analyzing its structural properties. The framework introduces a graph-theoretic approach that combines **spectral analysis**, **community detection**, and **dynamical systems theory** to mechanistically decompose RNN computation into interpretable sub-circuits.

### Analysis Pipeline
```
RNN Weight Matrix W
    ↓
Graph Construction (nodes=neurons, edges=weights)
    ↓
├── Spectral Analysis (eigenvalues, eigenvectors)
│   → Dominant modes, stability analysis
├── Community Detection (modularity maximization)
│   → Functional sub-circuits
└── Dynamical Analysis (fixed points, attractors)
    → Computational roles per sub-circuit
    ↓
Mechanistic Interpretation:
  - Which sub-circuit handles which task component?
  - How do sub-circuits interact temporally?
  - What is the information flow between modules?
```

## Implementation Guide

### Step 1: Extract Weight Graph
```python
import numpy as np
import networkx as nx

def rnn_to_graph(weight_matrix, threshold=0.01):
    """Convert RNN weight matrix to graph."""
    G = nx.DiGraph()
    n = weight_matrix.shape[0]
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if abs(weight_matrix[i, j]) > threshold:
                G.add_edge(j, i, weight=weight_matrix[i, j])
    return G
```

### Step 2: Spectral Analysis
```python
from scipy.linalg import eig

def spectral_analysis(weight_matrix):
    """Compute spectral properties of RNN weight matrix."""
    eigenvalues, eigenvectors = eig(weight_matrix)
    spectral_radius = max(abs(eigenvalues))
    sorted_idx = np.argsort(np.abs(eigenvalues))[::-1]
    return {
        'spectral_radius': spectral_radius,
        'dominant_modes': eigenvalues[sorted_idx[:10]],
        'stability': 'stable' if spectral_radius < 1.0 else 'unstable/chaotic'
    }
```

### Step 3: Community Detection
```python
def detect_communities(graph):
    """Detect functional communities in RNN graph."""
    import community as community_louvain
    G_undirected = graph.to_undirected()
    partition = community_louvain.best_partition(G_undirected)
    communities = {}
    for node, comm_id in partition.items():
        communities.setdefault(comm_id, []).append(node)
    return communities, partition
```

## Applications
- **Mechanistic interpretability**: Understanding what RNNs compute and how
- **Architecture analysis**: Comparing biological vs artificial neural networks
- **Task decomposition**: Identifying sub-circuits responsible for task sub-components
- **Neuroscience**: Bridging structural connectivity to functional computation

## Pitfalls
- **Spectral analysis assumes linearity**: RNN dynamics are nonlinear; spectral properties only approximate local behavior
- **Community detection is stochastic**: Run multiple times and use consensus clustering
- **Scale limitations**: Eigendecomposition is O(N³) — challenging for very large networks

## Related Skills
- brain-connectivity-analysis
- neural-population-dynamics
- neuroscience-of-transformers
- computational-neuroscience-in-llm-era