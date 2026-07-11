---
name: random-graph-datacenter-networks
description: "Random graph-based datacenter network design (RNG) for cost-optimized, fault-tolerant distributed systems. Covers distributed routing protocols exploiting random graph properties, passive optical cabling shuffles, and production deployment patterns. Use when: designing datacenter topologies, optimizing network cost vs performance, implementing distributed routing on non-hierarchical graphs, deploying fault-tolerant network fabrics, or evaluating random graph vs fat-tree tradeoffs."
---

# Random Graph Datacenter Networks (RNG)

## Overview

First production deployment of **random graph-based datacenter fabrics** (at Amazon). Random graph topologies provide cost and fault-tolerance advantages over traditional fat-tree designs, but require novel routing and cabling solutions.

## Core Contributions

### 1. RNG Topology Design

- Random graph fabric replacing hierarchical fat-tree architecture
- Up to **45% cheaper** than fat-tree while matching/exceeding performance
- Fault-tolerance inherent in random graph connectivity

### 2. Distributed Routing Protocol

- Exploits random graph properties to find large number of **edge-disjoint paths** between endpoint pairs
- Enables load balancing across diverse paths
- No single point of failure in routing

### 3. Passive Optical Shuffle Device

- Novel passive optical device internally shuffles cable endpoints
- Reduces cabling complexity to match fat-tree levels
- Solves the key practical barrier to random graph deployment

### 4. Production Deployment

- Made default datacenter fabric for most Amazon workloads
- Validated across range of traffic patterns
- Cost-performance tradeoff heavily favors RNG

## Design Principles

### Random Graph Construction

```
For N switches with degree d:
1. Generate random d-regular graph on N nodes
2. Verify connectivity and diameter properties
3. Map to physical switch/rack topology
4. Apply optical shuffle for cabling simplification
```

### Edge-Disjoint Path Routing

```python
def find_edge_disjoint_paths(graph, source, dest, k_paths):
    """Find k edge-disjoint paths in random graph.
    Random graphs typically have many short edge-disjoint paths."""
    paths = []
    working_graph = graph.copy()
    for _ in range(k_paths):
        path = shortest_path(working_graph, source, dest)
        if path:
            paths.append(path)
            # Remove edges used by this path
            for i in range(len(path)-1):
                working_graph.remove_edge(path[i], path[i+1])
        else:
            break
    return paths
```

### Cabling Complexity Reduction

Optical shuffle maps:
- Random graph logical topology → simplified physical cabling
- Each switch port connects through shuffle device
- Shuffle internally permutes connections to maintain random graph properties
- Result: O(N) cabling complexity (same as fat-tree)

## Cost Analysis

| Metric | Fat-Tree | RNG |
|--------|----------|-----|
| Switch count | O(N·log N) | O(N) |
| Cable count | O(N·log N) | O(N) |
| Path diversity | Limited by hierarchy | High (random) |
| Fault tolerance | Hierarchical bottlenecks | Inherent redundancy |
| Cost baseline | 1.0x | 0.55-0.75x |

## Performance Characteristics

- **Throughput**: Matches fat-tree for uniform traffic, exceeds for skewed patterns
- **Latency**: Comparable (slight increase from non-hierarchical routing offset by shorter average path)
- **Fault tolerance**: Superior — random graph has no critical single point of failure
- **Scalability**: Better — adding nodes doesn't require restructuring hierarchy

## Implementation Workflow

### Step 1: Generate Random Topology

```python
import networkx as nx
import random

def generate_rng_topology(n_switches, degree=4):
    """Generate a random regular graph for datacenter fabric."""
    G = nx.random_regular_graph(degree, n_switches)
    # Verify connectivity
    assert nx.is_connected(G)
    # Check diameter
    diameter = nx.diameter(G)
    return G, diameter
```

### Step 2: Compute Routing Tables

```python
def build_routing_tables(G, k_paths=8):
    """Build distributed routing tables using edge-disjoint paths."""
    routing = {}
    for src in G.nodes():
        routing[src] = {}
        for dst in G.nodes():
            if src != dst:
                paths = find_edge_disjoint_paths(G, src, dst, k_paths)
                routing[src][dst] = paths
    return routing
```

### Step 3: Deploy Shuffle Mapping

- Design optical shuffle permutation matrix
- Map logical random graph to physical ports
- Verify cabling matches shuffle specification

### Step 4: Validate Performance

- Simulate traffic patterns (uniform, incast, all-to-all)
- Measure throughput, latency, packet loss
- Compare against fat-tree baseline

## Pitfalls

- Random graph diameter can be larger than fat-tree — verify worst-case latency
- Routing tables grow as O(N²) — consider hierarchical caching for large deployments
- Optical shuffle must be manufactured to specification — tolerances matter
- Traffic patterns matter: RNG excels with diverse traffic, may underperform on highly localized traffic

## References

- arXiv: 2604.15261v1
- Authors: Giacomo Bernardi, Ratul Mahajan, C. Seshadhri et al.
- PDF: https://arxiv.org/pdf/2604.15261v1
