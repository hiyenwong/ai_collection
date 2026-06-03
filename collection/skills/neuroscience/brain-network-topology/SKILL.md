---
name: brain-network-topology
description: "Graph-theoretic analysis methods for brain connectivity. Covers small-world networks, rich-club organization, modularity, hub detection, and connectome analysis. Activation: brain network, graph theory, connectome, small-world, rich-club."
---

# Brain Network Topology and Graph Analysis

## Overview

Brain networks can be represented as graphs where nodes are brain regions and edges represent connections. Graph theory provides tools to characterize network topology including small-worldness, rich-club structure, and modularity.

## Key Concepts

### Graph Representation

**Nodes**: Brain regions, neurons, or recording channels
**Edges**: Structural or functional connections

### Small-World Networks

Balance local specialization with global integration:
- **High clustering**: Dense local connections
- **Short path length**: Efficient global communication
- **Small-world coefficient**: σ = (C/C_random) / (L/L_random) > 1

### Rich-Club Organization

Hub regions are more densely interconnected than expected.

## Methodology

### Basic Graph Metrics

```python
import numpy as np
import networkx as nx

def compute_basic_metrics(adj_matrix):
    """Compute basic graph metrics for brain network."""
    G = nx.from_numpy_array(adj_matrix)
    
    metrics = {
        'density': nx.density(G),
        'clustering_coeff': nx.average_clustering(G),
        'characteristic_path_length': nx.average_shortest_path_length(G) 
            if nx.is_connected(G) else np.inf,
        'efficiency': nx.global_efficiency(G),
    }
    
    return metrics
```

### Small-World Analysis

```python
def small_world_coefficient(adj_matrix, n_random=100):
    """Calculate small-world coefficient."""
    G = nx.from_numpy_array(adj_matrix)
    n_nodes = len(G)
    n_edges = G.number_of_edges()
    
    C = nx.average_clustering(G)
    L = nx.average_shortest_path_length(G) if nx.is_connected(G) else np.inf
    
    C_randoms = []
    for _ in range(n_random):
        G_random = nx.gnm_random_graph(n_nodes, n_edges)
        C_randoms.append(nx.average_clustering(G_random))
    
    C_random = np.mean(C_randoms)
    sigma = C / C_random if C_random > 0 else np.inf
    
    return sigma, C, L
```

### Community Detection

```python
def detect_communities(adj_matrix, resolution=1.0):
    """Detect network communities using Louvain algorithm."""
    import community as community_louvain
    
    G = nx.from_numpy_array(adj_matrix)
    partition = community_louvain.best_partition(G, weight='weight', 
                                                  resolution=resolution)
    modularity = community_louvain.modularity(partition, G, weight='weight')
    
    return partition, modularity
```

## References

- Sporns, O. (2011). *Networks of the Brain*. MIT Press.
- Bullmore, E., & Sporns, O. (2009). Complex brain networks. *Nature Reviews Neuroscience*, 10(3), 186-198.

## Activation Keywords

- brain network
- graph theory
- connectome
- small-world
- rich-club
- network topology
- modularity


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`
