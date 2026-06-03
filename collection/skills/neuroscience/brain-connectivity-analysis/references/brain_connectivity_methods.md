# Brain Connectivity Analysis Methods

## Graph Theory Basics

### Network Representations

Brain networks represented as graphs G = (V, E):
- **Nodes (V)**: Brain regions, neurons, or ROIs
- **Edges (E)**: Connections (structural, functional, or effective)
- **Weights**: Connection strength

### Key Metrics

| Metric | Description | Interpretation |
|--------|-------------|----------------|
| Degree | Number of connections | Hub identification |
| Clustering | Local connectivity | Modularity |
| Path Length | Shortest path between nodes | Integration |
| Modularity | Community structure | Functional segregation |
| Centrality | Node importance | Critical regions |

## Analysis Methods

### 1. Structural Connectivity

Physical connections (white matter tracts):

```python
# DTI-based connectivity
import numpy as np

# Connectivity matrix from DTI
connectivity_matrix = np.load('dti_matrix.npy')

# Threshold to create graph
threshold = 0.3
graph_matrix = connectivity_matrix > threshold
```

### 2. Functional Connectivity

Statistical dependencies (fMRI, EEG):

```python
# Correlation-based FC
from scipy import stats

# fMRI time series
time_series = np.load('fmri_signals.npy')  # shape: (n_regions, n_timepoints)

# Correlation matrix
fc_matrix = np.corrcoef(time_series)

# Fisher z-transformation
z_matrix = np.arctanh(fc_matrix)
```

### 3. Effective Connectivity

Causal influences (DTI, CCEP):

```python
# Granger causality
from statsmodels.tsa.stattools import grangercausalitytests

# Test causality between regions
max_lag = 5
result = grangercausalitytests([region1_signal, region2_signal], max_lag)
```

## Graph Analysis Algorithms

### PageRank

Identifies important nodes based on connectivity:

```python
import networkx as nx

# Create graph
G = nx.from_numpy_array(connectivity_matrix)

# PageRank
pagerank_scores = nx.pagerank(G, alpha=0.85)

# Top hubs
top_hubs = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:10]
```

### Louvain Community Detection

Identifies network modules:

```python
import community as community_louvain

# Community detection
partition = community_louvain.best_partition(G)

# Number of communities
n_communities = len(set(partition.values()))

# Module assignments
for node, community_id in partition.items():
    print(f"Node {node}: Community {community_id}")
```

### Small-World Analysis

Quantifies network topology:

```python
# Small-world coefficient
clustering_coeff = nx.average_clustering(G)
path_length = nx.average_shortest_path_length(G)

# Compare to random network
random_G = nx.random_graphs.erdos_renyi_graph(n_nodes, p_connection)
random_clustering = nx.average_clustering(random_G)
random_path = nx.average_shortest_path_length(random_G)

# Small-world index
sigma = (clustering_coeff / random_clustering) / (path_length / random_path)
```

## Connectivity Types

| Type | Method | Data | Interpretation |
|------|--------|------|----------------|
| Structural | DTI, DSI | White matter | Physical wiring |
| Functional | fMRI, EEG | Correlations | Statistical dependencies |
| Effective | CCEP, DCM | Causal models | Directed influences |
| Morphometric | MRI | Covariance | Structural co-variation |

## Common Software

- **NetworkX**: Python graph library
- **Brain Connectivity Toolbox**: MATLAB toolbox
- **CONN**: fMRI connectivity analysis
- **Dipy**: DTI processing
- ** Nilearn**: fMRI machine learning

## Visualization

```python
import matplotlib.pyplot as plt
import networkx as nx

# Plot connectivity matrix
plt.figure(figsize=(10, 8))
plt.imshow(connectivity_matrix, cmap='viridis')
plt.colorbar()
plt.title('Brain Connectivity Matrix')
plt.xlabel('Region')
plt.ylabel('Region')

# Plot graph
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=partition.values(), cmap=plt.cm.jet, 
        node_size=100, with_labels=False)
plt.title('Brain Network Graph')
```

## Integration with Knowledge Graph

### Workflow

1. Extract connectivity data from papers
2. Create entities in kg.db
3. Generate vector embeddings
4. Run PageRank and Louvain
5. Find similar papers
6. Extract reusable patterns

### Example

```bash
# Add paper to knowledge graph
./scripts/kg_tool/target/release/kg_tool add-entity kg.db paper "Brain Connectivity Paper"

# Generate vectors
python3 scripts/generate_vectors.py --db kg.db --model text-embedding-ada-002

# Run analysis
./scripts/kg_tool/target/release/kg_tool pagerank kg.db
./scripts/kg_tool/target/release/kg_tool louvain kg.db

# Similarity search
./scripts/kg_tool/target/release/kg_tool similar kg.db 505 5
```

## Best Practices

1. **Preprocessing**: Normalize connectivity matrices
2. **Thresholding**: Use data-driven thresholds
3. **Validation**: Compare across subjects/conditions
4. **Visualization**: Use appropriate color schemes
5. **Interpretation**: Consider neurobiological context

## References

1. Sporns, O. (2010). Networks of the Brain. MIT Press.
2. Bullmore, E., & Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. Nature Reviews Neuroscience.
3. Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: uses and interpretations. NeuroImage.