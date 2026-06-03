# Percolation Methods for Network Robustness Analysis

## Overview

Percolation theory provides mathematical framework for analyzing network connectivity and robustness under perturbations.

## Core Concepts

### Node Percolation

**Definition**: Random removal of nodes from network.

**Giant Component**:
```python
def giant_component_size(G, p):
    """
    Compute giant component size after removing (1-p) fraction of nodes.
    
    Args:
        G: NetworkX graph
        p: Fraction of nodes remaining
    
    Returns:
        P_inf: Relative size of giant component
    """
    # Remove nodes randomly
    nodes_to_remove = random.sample(list(G.nodes()), int((1-p) * G.number_of_nodes()))
    H = G.copy()
    H.remove_nodes_from(nodes_to_remove)
    
    # Find largest connected component
    largest_cc = max(nx.connected_components(H), key=len)
    P_inf = len(largest_cc) / G.number_of_nodes()
    
    return P_inf
```

### Edge Percolation

**Definition**: Random removal of edges from network.

**Implementation**:
```python
def edge_percolation_threshold(G):
    """
    Estimate critical threshold for edge percolation.
    
    For random networks (ER): pc = 1 / (⟨k⟩ - 1)
    For scale-free networks: pc ≈ 0 (no finite threshold)
    """
    avg_k = 2 * G.number_of_edges() / G.number_of_nodes()
    pc_ER = 1 / (avg_k - 1) if avg_k > 1 else 1
    
    return pc_ER
```

## Percolation Threshold

### Random Networks (Erdős–Rényi)

**Formula**:
```
pc = 1 / ⟨k⟩

where ⟨k⟩ = average degree
```

### Scale-Free Networks

**Characteristic**: No finite percolation threshold (pc → 0)

**Reason**: Hub nodes maintain connectivity even under massive removal

**Implication**: Highly robust to random failures, but vulnerable to targeted attacks

### Spatial Networks

**Characteristic**: Higher percolation threshold due to locality constraints

**Formula**:
```
pc_spatial > pc_random

Due to limited long-range connections
```

## Critical Nodes Identification

### Betweenness Centrality

**High betweenness nodes**: Critical for connectivity

```python
def find_critical_nodes(G, top_k=10):
    """
    Identify most critical nodes for network connectivity.
    """
    betweenness = nx.betweenness_centrality(G)
    sorted_nodes = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
    critical = sorted_nodes[:top_k]
    
    return critical
```

### Targeted Attack vs. Random Failure

**Targeted Attack**: Remove high-degree nodes → rapid fragmentation
**Random Failure**: Remove random nodes → gradual degradation

**Robustness Ratio**:
```
R = P_inf(targeted) / P_inf(random)
R < 1 indicates vulnerability to targeted attacks
```

## Temporal Percolation

**Concept**: Percolation dynamics over time

**Implementation**:
```python
def temporal_percolation(G_temporal, time_windows):
    """
    Analyze percolation across temporal network snapshots.
    
    Args:
        G_temporal: Temporal network (edge list with timestamps)
        time_windows: List of time periods
    
    Returns:
        pc_time: Percolation threshold for each window
        critical_time: Critical nodes for each window
    """
    results = []
    for t_start, t_end in time_windows:
        # Extract subgraph for time window
        edges_t = [(u, v) for u, v, t in G_temporal.edges(data='time') 
                   if t_start <= t <= t_end]
        G_t = nx.Graph()
        G_t.add_edges_from(edges_t)
        
        # Compute percolation metrics
        pc_t = estimate_percolation_threshold(G_t)
        critical_t = find_critical_nodes(G_t)
        
        results.append({
            'time_window': (t_start, t_end),
            'pc': pc_t,
            'critical_nodes': critical_t
        })
    
    return results
```

## Phase Transitions

### Percolation Transition

**Characteristics**:
- Second-order phase transition (continuous)
- Critical exponents describe scaling near threshold
- Universal behavior across network types

**Critical Exponents**:
```
P∞ ∝ (p - pc)^β  for p > pc

β ≈ 1 for mean-field (high-dimensional)
β ≈ 0.59 for 2D lattices
```

### Percolation as Phase Diagram

```
Connected Phase | Fragmented Phase
----------------|------------------
    p > pc      |     p < pc
    P∞ > 0      |     P∞ = 0
```

## Applications

1. **Network Design**: Ensure connectivity above percolation threshold
2. **Vulnerability Assessment**: Identify critical nodes for targeted protection
3. **Resilience Planning**: Design redundant pathways
4. **Early Warning**: Monitor percolation metrics approaching threshold

## References

- Newman, M.E.J. (2010). Networks: An Introduction. Oxford University Press.
- Cohen, R., et al. (2000). "Resilience of the Internet to Random Breakdowns." Physical Review Letters.
- Buldyrev, S.V., et al. (2010). "Catastrophic cascade of failures in interdependent networks." Nature.

---