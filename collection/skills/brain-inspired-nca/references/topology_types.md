# BraiNCA Topology Types

## Local Topologies

### Moore Neighborhood (Traditional)
- 8 adjacent cells in 2D grid
- Simple local interactions
- Limited connectivity

### Von Neumann Neighborhood
- 4 adjacent cells (orthogonal)
- Simpler than Moore
- Good for directional processes

## Brain-Inspired Topologies

### Small-World Networks
- High local clustering
- Few long-range connections
- Efficient information propagation
- Characteristics: High clustering coefficient, low average path length

### Scale-Free Networks
- Few hub nodes with many connections
- Many nodes with few connections
- Power-law degree distribution
- Robust to random failures

### Modular Networks
- Dense connections within modules
- Sparse connections between modules
- Mimics brain functional segregation
- Characteristics: High modularity score

### Hierarchical Modular Networks
- Modules within modules
- Multi-scale organization
- Brain-like structure
- Characteristics: Hierarchical modularity, fractal structure

## Topology Parameters

| Topology | Clustering | Path Length | Modularity | Brain Similarity |
|----------|------------|-------------|------------|------------------|
| Moore | High | Medium | Low | Low |
| Small-World | High | Low | Medium | Medium |
| Scale-Free | Low | Low | Low | Medium |
| Modular | High | High | High | High |
| Hierarchical Modular | High | Medium | High | Very High |

## Implementation Examples

### Small-World Topology
```python
import networkx as nx

# Watts-Strogatz small-world network
G = nx.watts_strogatz_graph(n=1000, k=10, p=0.1)
```

### Scale-Free Topology
```python
# Barabási-Albert scale-free network
G = nx.barabasi_albert_graph(n=1000, m=3)
```

### Modular Topology
```python
# Create modular network
G = nx.random_partition_graph(sizes=[100, 100, 100], 
                               p_in=0.3, p_out=0.01)
```

## Choosing Topology

1. **Morphogenesis**: Hierarchical Modular (multi-scale pattern formation)
2. **Motor Control**: Small-World (efficient signal propagation)
3. **Self-Organization**: Scale-Free (emergent hubs)
4. **General**: Modular (balanced local/global dynamics)

---
Reference: BraiNCA paper (arXiv:2604.01932)