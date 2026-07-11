---
name: critical-patch-size-brain-networks
description: "Critical patch size problem in graph networks with applications to brain connectomes and ecology. Spectral theory for population persistence using Dirichlet eigenvalues on random graphs. Activation triggers: critical patch size, random graph, Dirichlet eigenvalue, graph Laplacian, population persistence, network viability, brain network ecology."
---

# The Critical Patch Size Problem in Random Graphs

> A spectral theory framework for critical patch size on discrete habitats modeled as graphs, with applications to ecology, synthetic biology, and brain connectome modeling.

## Metadata
- **Source**: arXiv:2604.00624v1
- **Authors**: Nicola Apollonio, Veronica Tora, Davide Vergni
- **Published**: 2026-04-01
- **Category**: Network Science, Mathematical Biology, Graph Theory

## Core Methodology

### The Critical Patch Size Problem

**Classical Definition**: The critical patch size is a threshold condition determining whether a population can persist in a bounded habitat. Below the critical size, diffusion losses exceed local growth, leading to extinction.

**Continuous Domain (Classic)**:
- Reaction-diffusion equation on bounded domain
- Critical size depends on geometry and diffusion/growth ratio
- Analogous to critical mass in nuclear physics

**This Work: Discrete Habitat as Graphs**

### Graph-Theoretic Formulation

#### Habitat Model
```
G = (V, E)                    # Graph representing habitat
S ⊂ V                         # Sink vertices (boundary-like)
V \ S                          # Viable habitat (population can survive)
```

**Key Components**:
1. **Population Dynamics**: Proliferation at vertices + diffusion across edges
2. **Graph Laplacian**: L = D - A (discrete diffusion operator)
3. **Dirichlet Condition**: Population = 0 at sink vertices S
4. **Dirichlet Eigenvalue**: λ₁(G,S) = smallest eigenvalue of L restricted to V\S

#### Mathematical Framework

**Population Evolution**:
```
du/dt = -L · u + R · u
```
Where:
- u: Population vector (one value per vertex)
- L: Graph Laplacian (diffusion/dispersal)
- R: Reaction/growth rate

**Persistence Condition**:
```
Population survives ⟺ λ₁(G,S) < R/D
```
Where:
- λ₁(G,S): Dirichlet eigenvalue of habitat
- R/D: Critical reaction-to-diffusion ratio
- D: Diffusion coefficient

**Sharp Threshold Phenomenon**:
For large random graphs:
- If R/D < λ₁: Extinction (whp)
- If R/D > λ₁: Survival (whp)
- At criticality: Phase transition

### Dirichlet Eigenvalue on Graphs

#### Definition
Given graph G = (V,E) and sink set S ⊂ V:

1. Construct Laplacian submatrix Lₛ by removing rows/columns for S
2. λ₁(G,S) = smallest eigenvalue of Lₛ

**Properties**:
- λ₁ > 0 (for non-empty S)
- λ₁ decreases as S decreases (larger habitat)
- λ₁ encodes "escape rate" to sinks

#### Spectral Interpretation
- Small λ₁: Easy to survive (low diffusion to sinks)
- Large λ₁: Hard to survive (high diffusion losses)
- Critical value: Balance point between growth and diffusion

### Random Graph Analysis

#### Binomial Random Graph Model
- G(n,p): n vertices, each edge exists with probability p
- Random sink set S (random subset of vertices)
- Sequence of random habitats with increasing n

#### Main Results

**1. Law of Large Numbers for Dirichlet Eigenvalues**
```
λ₁(Gₙ,Sₙ) / E[λ₁] → 1   as n → ∞
```
The Dirichlet eigenvalue concentrates around its mean for large random graphs.

**2. Sharp Threshold Phenomenon**
```
For G(n,p) with p fixed, define critical ratio:
    α* = lim_{n→∞} E[λ₁(Gₙ,Sₙ)]

Then:
    If R/D < α*: P(survival) → 0
    If R/D > α*: P(survival) → 1
```

**3. Phase Transition**
Near criticality (R/D ≈ α*), survival probability undergoes rapid transition:
```
P(survival) = Φ((R/D - α*)/σₙ)
```
Where Φ is standard normal CDF, σₙ → 0 as n → ∞.

## Implementation Guide

### Prerequisites
```python
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
```

### Step-by-Step

#### Step 1: Construct Random Habitat Graph
```python
def create_random_habitat(n, p, sink_fraction=0.1, seed=None):
    """
    Create a random habitat graph with sink vertices.
    
    Args:
        n: Number of vertices
        p: Edge probability (Erdős-Rényi G(n,p))
        sink_fraction: Fraction of vertices designated as sinks
        seed: Random seed
    
    Returns:
        G: NetworkX graph
        sinks: List of sink vertex indices
    """
    if seed:
        np.random.seed(seed)
    
    # Generate random graph
    G = nx.erdos_renyi_graph(n, p, seed=seed)
    
    # Ensure connectivity (add edges if needed)
    if not nx.is_connected(G):
        components = list(nx.connected_components(G))
        for i in range(len(components)-1):
            u = list(components[i])[0]
            v = list(components[i+1])[0]
            G.add_edge(u, v)
    
    # Randomly designate sinks
    n_sinks = int(n * sink_fraction)
    sinks = np.random.choice(G.nodes(), size=n_sinks, replace=False)
    
    return G, sinks

# Example: Create habitat
G, sinks = create_random_habitat(n=100, p=0.1, sink_fraction=0.1)
print(f"Habitat: {G.number_of_nodes()} vertices, {G.number_of_edges()} edges")
print(f"Sinks: {len(sinks)} vertices ({len(sinks)/G.number_of_nodes()*100:.1f}%)")
```

#### Step 2: Compute Dirichlet Eigenvalue
```python
def compute_dirichlet_eigenvalue(G, sinks, k=1):
    """
    Compute the smallest Dirichlet eigenvalue.
    
    Args:
        G: NetworkX graph
        sinks: List/array of sink vertex indices
        k: Number of eigenvalues to compute (default: smallest)
    
    Returns:
        eigenvalues: Array of k smallest eigenvalues
        eigenvectors: Corresponding eigenvectors
    """
    # Full Laplacian
    L_full = nx.laplacian_matrix(G).astype(float)
    n = G.number_of_nodes()
    
    # Identify viable vertices (non-sinks)
    viable = np.setdiff1d(np.arange(n), sinks)
    
    # Extract submatrix (Dirichlet restriction)
    L_dirichlet = L_full[viable][:, viable]
    
    # Compute smallest eigenvalue(s)
    eigenvalues, eigenvectors = eigsh(L_dirichlet, k=k, which='SM')
    
    return eigenvalues, eigenvectors, viable

# Example: Compute eigenvalue
eigenvalues, eigenvectors, viable = compute_dirichlet_eigenvalue(G, sinks)
lambda_1 = eigenvalues[0]
print(f"Dirichlet eigenvalue λ₁ = {lambda_1:.4f}")

# Visualize eigenvector (population distribution)
viable_nodes = list(viable)
node_colors = ['red' if n in sinks else 'blue' for n in G.nodes()]
pos = nx.spring_layout(G)

plt.figure(figsize=(10, 8))
nx.draw(G, pos, node_color=node_colors, with_labels=False, 
        node_size=50, edge_color='gray', alpha=0.5)
plt.title(f'Random Habitat (λ₁ = {lambda_1:.4f})')
plt.show()
```

#### Step 3: Simulate Population Dynamics
```python
def simulate_population_dynamics(G, sinks, R, D, u0, T, dt=0.01):
    """
    Simulate population evolution on graph.
    
    Args:
        G: NetworkX graph
        sinks: Sink vertices
        R: Reaction (growth) rate
        D: Diffusion coefficient
        u0: Initial population distribution
        T: Simulation time
        dt: Time step
    
    Returns:
        u_history: Population over time
        t: Time points
        survival: Whether population persisted
    """
    n = G.number_of_nodes()
    viable = np.setdiff1d(np.arange(n), sinks)
    
    # Laplacian
    L = nx.laplacian_matrix(G).astype(float)
    
    # Initialize population (zero at sinks)
    u = np.zeros(n)
    u[viable] = u0[viable]
    
    # Time evolution
    t = np.arange(0, T, dt)
    u_history = [u.copy()]
    
    for _ in t[1:]:
        # Reaction-diffusion dynamics
        dudt = -D * L.dot(u) + R * u * (1 - u)  # Logistic growth + diffusion
        
        # Enforce Dirichlet boundary (sinks = 0)
        dudt[sinks] = 0
        u[sinks] = 0
        
        # Euler step
        u = u + dt * dudt
        u = np.maximum(u, 0)  # Ensure non-negative
        
        u_history.append(u.copy())
    
    u_history = np.array(u_history)
    
    # Check survival (population above threshold at end)
    survival = u_history[-1].sum() > 1e-6
    
    return u_history, t, survival

# Example simulation
n = G.number_of_nodes()
u0 = np.random.rand(n) * 0.1  # Small initial population
R = 1.0  # Growth rate
D = 0.5  # Diffusion

u_history, t, survival = simulate_population_dynamics(G, sinks, R, D, u0, T=50)

print(f"Initial population: {u_history[0].sum():.4f}")
print(f"Final population: {u_history[-1].sum():.4f}")
print(f"Survival: {survival}")

# Critical ratio check
critical_ratio = R / D
print(f"R/D = {critical_ratio:.4f}")
print(f"λ₁ = {lambda_1:.4f}")
print(f"Survival condition (R/D > λ₁): {critical_ratio > lambda_1}")
```

#### Step 4: Phase Transition Analysis
```python
def phase_transition_analysis(G, sinks, lambda_1, R_values, n_trials=10):
    """
    Analyze survival probability vs. R/D ratio.
    
    Args:
        G: Graph
        sinks: Sink vertices
        lambda_1: Dirichlet eigenvalue
        R_values: Range of R values to test
        n_trials: Number of trials per R value
    
    Returns:
        survival_probs: Survival probability for each R
    """
    D = 1.0  # Fix diffusion, vary growth
    survival_probs = []
    
    for R in R_values:
        survivals = []
        for _ in range(n_trials):
            n = G.number_of_nodes()
            u0 = np.random.rand(n) * 0.1
            _, _, survival = simulate_population_dynamics(G, sinks, R, D, u0, T=30)
            survivals.append(survival)
        
        survival_probs.append(np.mean(survivals))
    
    return np.array(survival_probs)

# Run phase transition analysis
R_values = np.linspace(0.5, 2.0, 20) * lambda_1  # Test around critical value
survival_probs = phase_transition_analysis(G, sinks, lambda_1, R_values)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(R_values / lambda_1, survival_probs, 'o-', linewidth=2)
plt.axvline(x=1.0, color='r', linestyle='--', label='Critical (R/D = λ₁)')
plt.xlabel('R/D (normalized by λ₁)')
plt.ylabel('Survival Probability')
plt.title('Phase Transition in Population Persistence')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Step 5: Scaling Analysis for Large Graphs
```python
def scaling_analysis(n_values, p=0.1, sink_fraction=0.1, n_trials=5):
    """
    Analyze Dirichlet eigenvalue scaling with graph size.
    
    Args:
        n_values: List of graph sizes to test
        p: Edge probability
        sink_fraction: Fraction of sinks
        n_trials: Trials per size
    
    Returns:
        mean_eigenvalues: Mean λ₁ for each n
        std_eigenvalues: Standard deviation
    """
    mean_eigenvalues = []
    std_eigenvalues = []
    
    for n in n_values:
        eigenvalues_n = []
        for _ in range(n_trials):
            G, sinks = create_random_habitat(n, p, sink_fraction)
            lambda_1, _, _ = compute_dirichlet_eigenvalue(G, sinks)
            eigenvalues_n.append(lambda_1)
        
        mean_eigenvalues.append(np.mean(eigenvalues_n))
        std_eigenvalues.append(np.std(eigenvalues_n))
    
    return np.array(mean_eigenvalues), np.array(std_eigenvalues)

# Scaling analysis
n_values = [50, 100, 200, 400, 800]
means, stds = scaling_analysis(n_values, p=0.1, sink_fraction=0.1)

# Plot scaling
plt.figure(figsize=(10, 6))
plt.errorbar(n_values, means, yerr=stds, fmt='o-', capsize=5, linewidth=2)
plt.xlabel('Graph Size (n)')
plt.ylabel('Dirichlet Eigenvalue λ₁')
plt.title('Scaling of λ₁ with Graph Size')
plt.grid(True, alpha=0.3)
plt.show()

print("Concentration: std/mean ratio decreases with n")
for n, mean, std in zip(n_values, means, stds):
    print(f"n={n:4d}: λ₁={mean:.4f} ± {std:.4f} (CV={std/mean:.3f})")
```

## Applications

### Ecology and Conservation Biology
- **Habitat Fragmentation**: Model effects of habitat loss on population persistence
- **Reserve Design**: Optimize protected area configurations
- **Invasive Species**: Predict spread thresholds in heterogeneous landscapes
- **Climate Change**: Model shifting habitat viability

### Synthetic Biology
- **Cell Colony Design**: Engineer spatially structured microbial communities
- **Bioreactor Optimization**: Design vessel geometries for desired population dynamics
- **Biofilm Control**: Manage bacterial persistence on surfaces

### Brain Connectome Modeling
- **Neural Population Survival**: Model maintenance of functional neural assemblies
- **Disease Spread**: Threshold conditions for pathological protein propagation
- **Network Resilience**: Critical conditions for brain network integrity
- **Stroke Recovery**: Conditions for neural reorganization after injury

### Epidemiology
- **Disease Persistence**: Critical community size for endemic infections
- **Contact Network Design**: Understand spread on social networks
- **Intervention Planning**: Target nodes to alter persistence threshold

## Pitfalls

### Theoretical Limitations
- **Mean-Field Approximation**: Large graph limit may not apply to small real systems
- **Homogeneity Assumption**: Random graphs lack real-world spatial structure
- **Linear Stability**: Analysis assumes small perturbations (near extinction)

### Practical Challenges
- **Parameter Estimation**: R and D difficult to measure in real systems
- **Stochastic Effects**: Finite populations have demographic stochasticity
- **Environmental Variability**: Time-varying parameters not captured

### Graph Theory Considerations
- **Connectivity**: Disconnected graphs require per-component analysis
- **Degree Distribution**: Erdős-Rényi model may not match real networks
- **Spatial Embedding**: Brain networks have geometric constraints

## Related Skills
- graph-laplacian-denoising
- brain-network-controllability
- brain-state-transition-network-control
- complex-system-robustness-collapse
- entropy-brain-connectivity-paths

## References
- Apollonio et al. (2026). The Critical Patch Size Problem in Random Graphs. arXiv:2604.00624v1
- Skellam (1951). Random dispersal in theoretical populations. Biometrika.
- Kierstead & Slobodkin (1953). The size of water masses containing plankton blooms.
- Okubo & Levin (2001). Diffusion and Ecological Problems: Modern Perspectives.
