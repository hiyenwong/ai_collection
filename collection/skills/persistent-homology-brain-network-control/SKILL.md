---
name: persistent-homology-brain-network-control
description: Methodology for applying persistent homology to brain network control theory, revealing how topological features broaden the controllable subspace beyond what scalar energy measures capture. Use when analyzing brain structural connectomes, network control theory, or topological data analysis in neuroscience contexts.
license: Complete terms in LICENSE.txt
---

# Persistent Homology Brain Network Control

This skill provides the methodology from the arXiv paper "Persistent homology broadens the controllable subspace in human structural connectomes" (arXiv:2608.03181) for applying topological data analysis to brain network control theory.

## Core Concepts

### Dissociation Between Control Cost and Control Geometry

The key insight is that **scalar control energy** (traditional network control metric) and **control geometry** (distribution of controllability across state space dimensions) can be dissociated:

- **Traditional approach**: Ranks brain regions as driver nodes by structural connectivity strength (degree)
- **Topological approach**: Ranks brain regions by persistent topological cycles participation (mesoscale integration measure)

Both approaches achieve nearly identical scalar control energy (differing by ~0.2%), but produce substantially different controllable subspaces.

### Key Advantages of Topology-Informed Driver Selection

1. **Better-conditioned controllability matrices**: More stable numerical properties
2. **Broader distribution across state space**: Controllability spread across more dimensions
3. **Robustness to hub removal**: Geometric advantage preserved even when high-degree hubs are removed
4. **Functional signature**: Different cortical territories reached efficiently, shaping which brain-state transitions are energetically favored

## Implementation Workflow

### 1. Data Preparation and Preprocessing
```python
# Load adjacency matrix A_raw from diffusion MRI tractography
# Symmetrize: A_sym = 0.5 * (A_raw + A_raw.T)  
# Set diagonal to zero
# Apply log transform: A_log = np.log(1 + A_sym) to reduce skew
# Normalize: A_0 = A_log / np.max(A_log) to [0,1] range
```

### 2. Node Ranking Methods
**Degree Strength:**
```python
degree_strength = np.sum(A_0, axis=1)  # Weighted sum of incident edges
```

**Cycle Participation (H1 Persistent Homology):**
```python
# Convert to distance matrix D where strong edges = short distances
D = np.ones_like(A_0)
D[A_0 > 0] = 1 - A_0[A_0 > 0]  
np.fill_diagonal(D, 0)

# Compute H1 persistent homology using Ripser with cocycle extraction
# For each finite H1 feature f with birth bf, death df, persistence = df - bf
# Get representative cocycle zf from Ripser
# Cycle participation for node i: CP_i = sum(persistence_f for f where i in support(zf))
# Min-max normalize CP within subject/scale before ranking
```

### 3. System Stabilization and Control Setup
```python
# Stabilize system matrix: A = A_0 - (lambda_max(A_0) + c) * I
# Use c = 0.1 as standard stabilization margin
# Construct input matrix B: columns are canonical basis vectors for selected driver nodes
```

### 4. Controllability Analysis
**Gramian Computation:**
```python
# Solve continuous Lyapunov equation: A*W + W*A.T + B*B.T = 0
# Regularize: W_eps = W + epsilon*I (epsilon = 1e-5 standard)
# Handle small eigenvalues: set lambda_i = max(lambda_i, epsilon)
```

**Control Metrics:**
- **Scalar Energy**: `E_avg = trace(W_eps_inv)`
- **Effective Rank**: `reff = exp(-sum(p_i * log(p_i)))` where `p_i = lambda_i / sum(lambda_j)`
- **Participation Ratio**: `PR = (sum(lambda_i))^2 / sum(lambda_i^2)`
- **Condition Number**: `kappa = lambda_max / lambda_min` (use log10 scale)

### 5. Advanced Analyses
**Hub Lesioning:**
- Remove top h degree-strength nodes (h = 5, 10, 15)
- Recompute Gramian with same driver identities (no reselection)
- Compare degradation: intact vs lesioned metrics

**Target-State Control:**
```python
# For target state x_star: E_target = x_star.T @ W_eps_inv @ x_star  
# Test targets: V1, M1, PCC/precuneus, lPFC, occipital module, association module
# Report percent differences: 100 * (E_cycle - E_degree) / E_degree
```

### 6. Validation and Robustness
- Test across parcellation scales (68, 114, 219 regions)
- Sweep regularization: epsilon ∈ [1e-8, 1e-5]
- Compare finite-horizon (T = 1, 2.5, 5) vs infinite-horizon Gramians
- Verify representative construction sensitivity (Ripser cocycles vs alternatives)

## Mathematical Framework

### Controllability Gramian
For linear system `dx/dt = Ax + Bu`, the controllability Gramian is:
```
W = ∫₀^∞ e^(At)BBᵀe^(Aᵀt) dt
```

### Scalar Control Energy
```
E = trace(W⁻¹)
```

### Topological Cycle Participation
Measure based on persistent homology barcode analysis, capturing:
- Number of persistent cycles a node participates in
- Persistence intervals of those cycles
- Integration across multiple topological dimensions

## Applications

### Neuroscience Research
- Brain network control analysis beyond scalar metrics
- Understanding mesoscale integration in structural connectomes
- Relating topology to functional brain dynamics

### Clinical Applications
- Identifying optimal stimulation targets for neuromodulation
- Understanding network resilience in neurological disorders
- Personalized brain network intervention planning

### Computational Methods
- Integrating topological data analysis with control theory
- Multi-scale brain network analysis
- Geometric approaches to network science

## Activation Keywords

- persistent homology brain network
- topological brain control
- controllable subspace topology
- brain network control geometry
- mesoscale integration connectome
- persistent cycles brain network

## References

- Sale, C., Coraggio, M., Zhang, M., & Richardson, M. J. (2026). Persistent homology broadens the controllable subspace in human structural connectomes. arXiv:2608.03181 [q-bio.NC]
- Network control theory fundamentals
- Topological data analysis in neuroscience
- Structural connectome analysis methods