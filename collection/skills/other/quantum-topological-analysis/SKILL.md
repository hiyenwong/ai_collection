---
name: quantum-topological-analysis
description: "Quantum and classical algorithms for topological data analysis (TDA) including persistent Betti numbers computation, simplicial complex construction, and persistence diagram interpretation. Use when analyzing topological features of data, persistent homology, Betti numbers, simplicial complexes, or topological data analysis. Triggers: TDA, 拓扑数据分析, Betti numbers, Betti数, persistent homology, 持久同调, simplicial complex, 单纯复形, quantum TDA, quantum topology."
---

# Quantum Topological Data Analysis

Algorithms for extracting topological features from data using both classical and quantum methods.

## What It Does

Provides topological data analysis workflows:
- Persistent homology computation
- Betti numbers calculation (β₀, β₁, β₂, ...)
- Simplicial complex construction
- Persistence diagram generation and interpretation
- Quantum vs classical TDA method selection

## Activation Keywords

- topological data analysis
- 拓扑数据分析
- TDA
- Betti numbers
- Betti数
- persistent homology
- 持久同调
- simplicial complex
- 单纯复形
- quantum TDA
- quantum topology
- persistence diagram
- 持久图
- topological features
- 拓扑特征

## Tools Used

- `exec`: Run TDA libraries (Ripser, GUDHI), Python scripts
- `read`: Load point cloud data, reference materials
- `write`: Save persistence diagrams, analysis results
- `image`: Generate visualization plots

## When to Use This Skill

Use this skill when:
1. User asks about topological features of data
2. Need to compute Betti numbers or persistent homology
3. Analyzing shape/structure of point cloud data
4. Working with simplicial complexes
5. Interested in quantum algorithms for TDA
6. Extracting geometric features from high-dimensional data

## Key Concepts

### Betti Numbers

**Definition:** Topological invariants counting independent features

| Betti Number | Dimension | Meaning |
|-------------|-----------|---------|
| β₀ | 0 | Connected components |
| β₁ | 1 | Independent loops (holes) |
| β₂ | 2 | Voids (cavities) |
| βₖ | k | k-dimensional holes |

**Example:**
```
Circle: β₀=1 (one component), β₁=1 (one loop)
Sphere: β₀=1, β₁=0, β₂=1 (one void)
Torus: β₀=1, β₁=2 (two loops), β₂=1
```

### Persistent Homology

**Core idea:** Track topology across different scales

```
At scale ε=0.1: Many small clusters (high β₀)
At scale ε=0.5: Clusters merge (β₀ decreases)
At scale ε=1.0: One big cluster (β₀=1)
At scale ε=2.0: Loops appear (β₁ increases)
```

**Key metric: Persistence**
```
Persistence = Death_time - Birth_time

Long persistence → Stable feature (signal)
Short persistence → Transient feature (noise)
```

### Simplicial Complexes

**Vietoris-Rips Complex:**
```
Input: Point cloud X, scale parameter ε
Construction:
- 0-simplex: Each point
- 1-simplex: Edge if distance < ε
- 2-simplex: Triangle if all edges < ε
- k-simplex: k+1 points pairwise < ε
```

**Čech Complex:**
```
More geometrically accurate:
- k-simplex: k+1 points in common ε-ball
```

## Core Workflow

### Step 1: Problem Assessment

```python
def assess_tda_problem(point_cloud, dimension):
    """
    Assess TDA problem and recommend approach.
    
    Args:
    - point_cloud: Data array (n × d)
    - dimension: Maximum homology dimension
    
    Returns:
    - recommendation: 'quantum' or 'classical'
    - tools_needed: List of required tools
    - estimated_resources: Memory/time estimates
    """
    
    n_points = len(point_cloud)
    data_dim = point_cloud.shape[1]
    
    # Simplicial complex size
    complex_size = estimate_complex_size(n_points, dimension)
    
    if complex_size > 1e9 and dimension > 3:
        return {
            'recommendation': 'quantum',
            'reason': 'Massive complex size, quantum algorithms provide exponential speedup',
            'tools': ['quantum_phase_estimation', 'quantum_state_preparation'],
            'resources': 'Requires fault-tolerant quantum computer'
        }
    else:
        return {
            'recommendation': 'classical',
            'reason': 'Reasonable size for classical computation',
            'tools': ['ripser', 'gudhi', 'persim'],
            'resources': f'Memory: {complex_size * 8 / 1e6:.1f}MB'
        }
```

### Step 2: Simplicial Complex Construction

**Vietoris-Rips (VR) Complex:**

```python
import numpy as np
from scipy.spatial.distance import pdist, squareform

def build_vr_complex(points, epsilon, max_dim=3):
    """
    Build Vietoris-Rips simplicial complex.
    
    Args:
    - points: Point cloud (n × d)
    - epsilon: Scale parameter
    - max_dim: Maximum simplex dimension
    
    Returns:
    - simplices: List of simplices by dimension
    """
    
    # Compute pairwise distances
    distances = squareform(pdist(points))
    
    # Find edges (1-simplices)
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if distances[i, j] < epsilon:
                edges.append([i, j])
    
    # Build higher simplices
    simplices = {0: [[i] for i in range(len(points))], 1: edges}
    
    for dim in range(2, max_dim + 1):
        simplices[dim] = []
        # Find (dim+1)-simplices
        # All pairwise distances < epsilon
        # (Implementation uses combinatorial search)
    
    return simplices
```

### Step 3: Betti Numbers Computation

**Classical Method (Ripser):**

```python
import ripser

def compute_persistent_homology(points, max_dim=2):
    """
    Compute persistent homology using Ripser.
    
    Args:
    - points: Point cloud
    - max_dim: Maximum homology dimension
    
    Returns:
    - persistence_diagram: Birth-death pairs
    - betti_numbers: Betti numbers at each scale
    """
    
    # Ripser automatically builds VR complex
    # and computes persistent homology
    result = ripser.ripser(points, maxdim=max_dim)
    
    # Extract persistence diagrams
    diagrams = result['dgms']
    
    # Extract Betti numbers
    betti = {}
    for dim in range(max_dim + 1):
        if dim < len(diagrams):
            # Count features at each scale
            betti[dim] = len(diagrams[dim])
    
    return {
        'diagrams': diagrams,
        'betti_numbers': betti,
        'birth_death_pairs': diagrams
    }
```

**Quantum Method (Conceptual):**

```python
def quantum_compute_betti(simplicial_complex, scale_range):
    """
    Quantum algorithm for Betti numbers (conceptual).
    
    Based on Hayakawa (2021) arXiv:2111.00433
    
    Note: Requires quantum hardware
    """
    
    # Step 1: Encode simplicial complex as quantum state
    quantum_state = encode_complex(simplicial_complex)
    
    # Step 2: Compute boundary operators
    boundary_matrix = compute_boundary_operators(simplicial_complex)
    
    # Step 3: Quantum Phase Estimation (QPE)
    # QPE reveals eigenvalues → rank → Betti numbers
    eigenvalues = quantum_phase_estimation(boundary_matrix)
    
    # Step 4: Extract Betti numbers from eigenvalues
    betti = extract_betti_from_eigenvalues(eigenvalues)
    
    return betti
```

### Step 4: Persistence Diagram Interpretation

```python
def interpret_persistence_diagram(diagrams, threshold=0.5):
    """
    Interpret persistence diagrams to identify significant features.
    
    Args:
    - diagrams: Persistence diagrams by dimension
    - threshold: Minimum persistence for significance
    
    Returns:
    - significant_features: List of important topological features
    - interpretations: Human-readable descriptions
    """
    
    features = []
    
    for dim, diagram in enumerate(diagrams):
        for birth, death in diagram:
            persistence = death - birth
            
            if persistence > threshold:
                feature = {
                    'dimension': dim,
                    'birth': birth,
                    'death': death,
                    'persistence': persistence,
                    'significance': 'stable',
                    'interpretation': interpret_betti(dim)
                }
                features.append(feature)
    
    return features

def interpret_betti(dim):
    """
    Human-readable interpretation of Betti numbers.
    """
    interpretations = {
        0: "Connected component (cluster)",
        1: "Loop or cycle (ring structure)",
        2: "Void or cavity (hollow region)",
        3: "3-dimensional hole"
    }
    return interpretations.get(dim, f"{dim}-dimensional topological feature")
```

### Step 5: Visualization

```python
import matplotlib.pyplot as plt
import persim

def visualize_persistence(diagrams):
    """
    Visualize persistence diagrams.
    """
    
    # Persistence diagram plot
    fig, axes = plt.subplots(1, len(diagrams), figsize=(12, 4))
    
    for dim, ax in enumerate(axes):
        if dim < len(diagrams):
            persim.plot_diagrams(
                diagrams[dim],
                ax=ax,
                title=f'Dimension {dim}',
                labels=['Persistence points']
            )
    
    plt.tight_layout()
    plt.savefig('persistence_diagram.png')
    
    # Barcode plot (alternative)
    plt.figure(figsize=(10, 6))
    persim.plot_barcodes(diagrams)
    plt.savefig('barcode.png')
```

## Algorithm Selection Guide

### When to Use Quantum TDA

```
Quantum TDA advantages:
1. Exponential speedup for high-dimensional complexes
2. Can handle massive datasets (>10⁶ points)
3. Parallel computation of multiple scales

Requirements:
- Fault-tolerant quantum computer (currently unavailable)
- Efficient state preparation
- High-dimensional simplices (>d=3)

Current recommendation: Use classical for now
```

### When to Use Classical TDA

```
Classical TDA tools:

Ripser:
- Fast C++ implementation
- Optimized for VR complexes
- Handles up to ~10⁵ points

GUDHI:
- Comprehensive TDA library
- Multiple complex types
- Python/C++ interfaces

Dionysus:
- Flexible topology computations
- Good for research

Recommendation: Ripser for production, GUDHI for research
```

### Classical Speedup Techniques

```python
def optimize_classical_tda(point_cloud, method='sparse'):
    """
    Optimization strategies for classical TDA.
    
    Methods:
    - sparse: Use sparse boundary matrices
    - approximate: Approximate VR complex
    - subsampling: Compute on subsample, extrapolate
    """
    
    if method == 'sparse':
        # Use sparse matrices for boundary operators
        from scipy.sparse import csr_matrix
        boundary_sparse = csr_matrix(boundary_dense)
        
    elif method == 'approximate':
        # Sample points to reduce complex size
        subsample = np.random.choice(len(point_cloud), 10000)
        points_sub = point_cloud[subsample]
        
    elif method == 'subsampling':
        # Bootstrap approach
        results = []
        for _ in range(10):
            sample = random_sample(point_cloud)
            betti = compute_betti(sample)
            results.append(betti)
        # Aggregate results
```

## Example Applications

### Example 1: Protein Structure Analysis

```python
# Analyze protein backbone topology
protein_coords = load_protein_structure('protein.pdb')

# Compute persistent homology
result = compute_persistent_homology(protein_coords, max_dim=2)

# Interpret features
features = interpret_persistence_diagram(result['diagrams'])

# Typical protein findings:
# - β₀: Number of separate chains
# - β₁: Loops in backbone (beta sheets)
# - β₂: Cavities (binding sites)
```

### Example 2: Brain Network Topology

```python
# Analyze brain connectivity topology
brain_network = load_connectome('subject_001.mat')

# Points = brain regions in connectivity space
points = connectivity_embedding(brain_network)

# TDA analysis
tda_result = compute_persistent_homology(points)

# Findings:
# - β₁ loops: Neural circuits
# - Persistence: Stable circuits vs transient
```

### Example 3: Material Structure

```python
# Analyze porous material topology
material_points = load_microstructure_scan('sample_01.nii')

# High-dimensional TDA for 3D structure
result = compute_persistent_homology(material_points, max_dim=3)

# β₀: Number of separate regions
# β₁: Channels/pores (loops)
# β₂: Voids/cavities in material
```

## Common Pitfalls

### Pitfall 1: Wrong Scale Parameter

```python
# Problem: epsilon too large or too small

epsilon_too_small = 0.01  # Everything disconnected (β₀=n)
epsilon_too_large = 100   # Everything connected (β₀=1, no higher features)

# Solution: Try multiple scales
epsilon_range = np.linspace(0.1, 2.0, 20)
for eps in epsilon_range:
    result = compute_homology(points, eps)
```

### Pitfall 2: Ignoring Data Preprocessing

```python
# TDA sensitive to scale and outliers

# Normalize data
points_normalized = (points - points.mean()) / points.std()

# Remove outliers (optional)
from sklearn.neighbors import LocalOutlierFactor
outlier_detector = LocalOutlierFactor()
inliers = outlier_detector.fit_predict(points_normalized) == 1
points_clean = points_normalized[inliers]
```

### Pitfall 3: Over-interpreting Features

```python
# Not all topological features are meaningful

# Check persistence relative to noise level
noise_persistence = estimate_noise_persistence(points)
significant_features = [
    f for f in features 
    if f['persistence'] > 2 * noise_persistence
]
```

## Quantum Algorithm Details

### Quantum Phase Estimation for Betti Numbers

**Conceptual algorithm:**

```
Step 1: Encode simplicial complex
- k-simplex → quantum state basis
- Boundary matrix → Hamiltonian H

Step 2: Quantum Phase Estimation (QPE)
- Apply QPE to H
- Eigenvalues reveal kernel dimension → Betti

Step 3: Extract Betti numbers
- β_k = dim(kernel(∂_k)) - dim(image(∂_{k+1}))
- Quantum counting reveals dimensions

Complexity: O(poly(d, log n))
vs Classical: O(n^{d+1})
```

**Current status:** Requires fault-tolerant quantum computers.

## Related Skills

- **quantum-algorithms**: General quantum algorithms
- **simplicial-complex**: Complex construction methods
- **homology-theory**: Mathematical foundations
- **data-visualization**: Plotting persistence diagrams

## References

### Key Papers
1. Hayakawa, R. (2021). Quantum algorithm for persistent Betti numbers. arXiv:2111.00433
2. Edelsbrunner & Harer (2008). Persistent homology—A survey
3. Lloyd et al. (2016). Quantum algorithm for topological analysis

### Libraries
- Ripser: https://github.com/Ripser/ripser
- GUDHI: https://gudhi.inria.fr/
- Persim: https://persim.readthedocs.io/

## Limitations

- Quantum TDA requires unavailable hardware
- High-dimensional complexes computationally expensive
- Interpretation requires domain expertise
- Scale parameter selection non-trivial
- Noise and outliers affect topology

## Notes

- Start with classical TDA tools (Ripser)
- Quantum TDA is theoretical for now
- Persistence diagrams reveal stable features
- Always preprocess data before TDA
- Multiple scales reveal full topology