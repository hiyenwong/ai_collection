# SKILL.md - Dynamic Brain Connectivity Topology Imaging

## Activation Keywords

- dynamic functional connectivity, brain topology imaging
- persistent homology, graph homology, Wasserstein distance
- time-varying brain networks, non-Euclidean learning
- topology embedding, brain connectivity visualization

## What It Does

Encodes dynamic functional connectivity as image representations of evolving network topology using persistent graph homology. Creates Wasserstein distance-preserving embeddings that are stable under network perturbations.

## When To Use

**Use this skill when:**
- Analyzing time-varying brain connectivity
- Learning from non-Euclidean dynamic networks
- Visualizing dynamic brain topology changes
- Creating stable embeddings for dynamic graphs
- Detecting topological changes in functional connectivity

**Do NOT use for:**
- Static connectivity analysis (no temporal dynamics)
- Simple correlation matrices (no topological analysis)
- Euclidean data processing (standard methods apply)

## How To Use

### Step-by-Step Workflow

1. **Extract Dynamic Functional Connectivity**
   - Sliding window correlation on fMRI time series
   - Window size: typically 30-60 TRs
   - Step size: 1 TR for high temporal resolution
   - Result: sequence of connectivity matrices {C(t₁), C(t₂), ...}

2. **Convert to Graph Sequence**
   - Threshold each connectivity matrix
   - Extract graph G(t) with nodes = brain regions
   - Edges = significant connections

3. **Compute Persistent Graph Homology**
   - Build filtration: start with empty graph, add edges by weight
   - Track birth/death of topological features (connected components, cycles)
   - Generate persistence diagram for each time point

4. **Create Topology Image Representation**
   - Convert persistence diagrams to 2D images
   - Encode birth/death times as pixel coordinates
   - Use kernel density estimation for smooth representation
   - Result: image sequence showing topology evolution

5. **Generate Wasserstein Embeddings**
   - Compute Wasserstein distance between persistence diagrams
   - Use distance-preserving embedding (e.g., MDS, t-SNE)
   - Result: low-dimensional representation of dynamic topology

### Key Parameters

| Parameter | Range | Purpose |
|-----------|-------|---------|
| Window size | 30-60 TRs | Temporal smoothing |
| Step size | 1-5 TRs | Resolution vs computation |
| Threshold | 0.1-0.3 | Graph sparsification |
| Max filtration | 1.0 | Homology computation range |

### Persistence Diagram Features

**H₀ (Connected components):**
- Number of clusters/communities
- Isolation vs integration

**H₁ (Cycles):**
- Information flow loops
- Recurrent processing

## Example Usage

### Dynamic FC Topology Analysis

**Problem:** Track topological changes in brain connectivity during task

**Input:**
```
fMRI time series: T x N matrix (T time points, N regions)
Task: Rest → Task → Rest
```

**Pipeline:**
```python
import numpy as np
from gudhi import RipsComplex

def dynamic_topology_images(fmri_data, window=44, step=1, threshold=0.2):
    """
    Convert fMRI to topology image sequence
    """
    T, N = fmri_data.shape
    topology_images = []
    
    for t in range(0, T - window, step):
        # Extract window
        window_data = fmri_data[t:t+window, :]
        
        # Compute correlation
        corr = np.corrcoef(window_data.T)
        
        # Threshold to graph
        adj = (np.abs(corr) > threshold).astype(float)
        
        # Compute persistence
        rips = RipsComplex(distance_matrix=1 - adj, max_edge_length=1.0)
        simplex_tree = rips.create_simplex_tree(max_dimension=2)
        persistence = simplex_tree.persistence()
        
        # Convert to image (birth, death coordinates)
        pd_h0 = [(b, d) for dim, (b, d) in persistence if dim == 0]
        pd_h1 = [(b, d) for dim, (b, d) in persistence if dim == 1]
        
        # Create image representation
        img = persistence_diagram_to_image(pd_h0, pd_h1)
        topology_images.append(img)
    
    return np.array(topology_images)
```

**Output:**
```
Topology images: (T-window)/step x H x W
Wasserstein distances between consecutive frames
```

### Detecting State Transitions

**Analysis:**
```python
# Compute Wasserstein distance between consecutive topology images
distances = []
for i in range(len(topology_images) - 1):
    d = wasserstein_distance(
        persistence_from_image(topology_images[i]),
        persistence_from_image(topology_images[i+1])
    )
    distances.append(d)

# Detect transitions (peaks in distance)
transitions = find_peaks(distances, threshold=0.1)
```

**Result:** Detected topology changes at task transitions

## Key Advantages

| Property | Benefit |
|----------|---------|
| Wasserstein distance | Stable under perturbations |
| Persistent homology | Multi-scale topology |
| Image representation | CNN-compatible |
| Topology focus | Invariant to node ordering |

## Related Skills

- **brain-higher-order-structures** - Higher-order brain connectivity
- **time-varying-brain-connectivity** - Time-varying analysis
- **discrete-heat-kernels-simplicial** - Simplicial complex methods

## Source

- arXiv:2511.09949v1
- Title: Imaging the Topology of Dynamic Brain Connectivity
- Utility: 0.88
- Authors: (from arxiv)

## Notes

- Key innovation: Image representation of dynamic topology
- Uses persistent graph homology for multi-scale analysis
- Wasserstein distance provides stable embeddings
- Applications: brain state detection, clinical neuroscience
- Compatible with deep learning (CNN on topology images)

---

_Created: 2026-04-01_