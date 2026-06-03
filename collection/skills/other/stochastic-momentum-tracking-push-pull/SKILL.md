---
name: stochastic-momentum-tracking-push-pull
description: "Stochastic Momentum Tracking Push-Pull (SMTPP) algorithm for decentralized optimization over directed graphs. Decouples variance reduction from graph connectivity for robust convergence. Use for: directed graph optimization, decentralized learning, push-pull algorithms, network topology optimization, asymmetric communication. Activation: push-pull, directed graph optimization, SMTPP, momentum tracking, decentralized directed, asymmetric network."
---

# Stochastic Momentum Tracking Push-Pull (SMTPP)

Decentralized optimization algorithm for directed graphs that tracks momentum rather than raw gradients, achieving robust convergence despite asymmetric communication and high gradient variance.

## Overview

Decentralized optimization over directed networks faces unique challenges:
- **Asymmetric communication**: Different weights for sending/receiving
- **High variance**: Stochastic gradients cause oscillations
- **Topology sensitivity**: Convergence depends heavily on graph structure

**SMTPP** addresses these by tracking momentum within the Push-Pull architecture, successfully decoupling variance reduction from algebraic connectivity.

## Key Innovations

### 1. Momentum Tracking in Push-Pull

```
Traditional Push-Pull: Track raw stochastic gradients
SMTPP: Track momentum term

Benefit: Reduces oscillations from stochastic noise
```

### 2. Variance-Topology Decoupling

```
Traditional: Variance reduction ↔ Graph connectivity (coupled)
SMTPP: Variance reduction ⊥ Graph connectivity (decoupled)

Result: Robust performance regardless of network sparsity
```

### 3. Directed Graph Convergence

- Guarantees convergence on any strongly connected directed graph
- Compresses steady-state error to minimal neighborhood
- Robust to network topology variations

## Push-Pull Architecture

### Directed Graph Setting

```
In undirected graphs: W is symmetric (W = W^T)
In directed graphs: Different matrices for row/column stochasticity

Push-Pull uses:
- R: Row-stochastic (for averaging)
- C: Column-stochastic (for tracking)

R ≠ C in general (only for undirected graphs: R = C = W)
```

### Why Push-Pull?

| Property | Standard Consensus | Push-Pull |
|----------|-------------------|-----------|
| Undirected graphs | ✓ | ✓ |
| Directed graphs | ✗ | ✓ |
| Asymmetric weights | ✗ | ✓ |
| Balanced graphs only | Yes | No |

## SMTPP Algorithm

### Mathematical Formulation

```
At each agent i and iteration t:

1. Pull Step (Information Gathering):
   x_i^{t+½} = Σ_j R_ij x_j^t

2. Local Update with Momentum:
   x_i^{t+1} = x_i^{t+½} - α [g_i^t + m_i^t]
   
3. Momentum Tracking:
   m_i^{t+1} = Σ_j C_ij m_j^t + β [g_i^{t+1} - g_i^t]

where:
- R: Row-stochastic mixing matrix
- C: Column-stochastic mixing matrix
- g_i: Stochastic gradient at agent i
- m_i: Momentum tracker
- α: Step size
- β: Momentum parameter
```

### Intuition

```
Pull Step: Gather neighbor information (row-stochastic)
Local Update: Apply gradient step with momentum assistance
Momentum Tracking: Propagate gradient changes (column-stochastic)
```

## Convergence Theory

### Directed Graph Convergence

**Theorem**: SMTPP converges on any strongly connected directed graph.

**Requirements:**
- Graph is strongly connected
- R is row-stochastic
- C is column-stochastic
- Step size α is sufficiently small

### Steady-State Error

```
In directed graphs with persistent noise:
  Exact convergence is IMPOSSIBLE (topology mismatch)

SMTPP achieves:
  Error ≤ ε_min(network_connectivity, gradient_variance)

This is the MINIMAL achievable error for directed graphs.
```

### Convergence Rate

```
For non-convex problems:
  (1/T) Σ E[||∇f(x^t)||^2] ≤ O(1/T) + O(ε_ss)

where ε_ss is the steady-state error floor.
```

## Variance-Topology Decoupling

### The Problem with Traditional Methods

```
Traditional Push-Pull:
  Error ∝ (gradient_variance) / (spectral_gap)

As graph becomes sparser:
  - Spectral gap → 0
  - Error → ∞
```

### SMTPP Solution

```
SMTPP:
  Error ∝ gradient_variance + topology_effect

Key insight: Additive not multiplicative!

As graph becomes sparser:
  - Topology effect increases
  - But gradient variance effect unchanged
  - Total error remains bounded
```

## Implementation

### Algorithm Pseudocode

```python
def smtp_update(agent_id, local_state, neighbors_in, neighbors_out, 
                step_size, momentum, R, C):
    """
    SMTPP update for a single agent
    
    Args:
        agent_id: ID of current agent
        local_state: Current local optimization variable
        neighbors_in: Incoming neighbors (for pull)
        neighbors_out: Outgoing neighbors (for push)
        step_size: Learning rate α
        momentum: Momentum parameter β
        R: Row-stochastic weights (incoming)
        C: Column-stochastic weights (outgoing)
    
    Returns:
        Updated state and momentum
    """
    # Pull step: gather from incoming neighbors
    pulled_state = sum(R[agent_id][j] * neighbor_states[j] 
                       for j in neighbors_in)
    
    # Compute stochastic gradient
    gradient = compute_stochastic_gradient(pulled_state, agent_id)
    
    # Local update with momentum
    updated_state = pulled_state - step_size * (gradient + momentum_tracker[agent_id])
    
    # Momentum tracking: push to outgoing neighbors
    new_momentum = sum(C[j][agent_id] * momentum_tracker[j] 
                       for j in neighbors_out)
    new_momentum += momentum * (gradient - previous_gradient[agent_id])
    
    # Store for next iteration
    previous_gradient[agent_id] = gradient
    momentum_tracker[agent_id] = new_momentum
    
    return updated_state, new_momentum
```

### Mixing Matrix Construction

```python
def construct_mixing_matrices(graph):
    """
    Construct row and column stochastic matrices for directed graph
    
    Args:
        graph: NetworkX directed graph
    
    Returns:
        R: Row-stochastic matrix
        C: Column-stochastic matrix
    """
    n = graph.number_of_nodes()
    
    # Row-stochastic: R_ij = weight from j to i
    R = np.zeros((n, n))
    for i in graph.nodes():
        in_neighbors = list(graph.predecessors(i))
        if in_neighbors:
            for j in in_neighbors:
                R[i][j] = 1.0 / len(in_neighbors)
        R[i][i] = 1.0 - sum(R[i])
    
    # Column-stochastic: C_ij = weight from i to j
    C = np.zeros((n, n))
    for j in graph.nodes():
        out_neighbors = list(graph.successors(j))
        if out_neighbors:
            for i in out_neighbors:
                C[i][j] = 1.0 / graph.out_degree(j)
        C[j][j] = 1.0 - sum(C[:, j])
    
    return R, C
```

### Hyperparameter Selection

```python
def select_smtp_hyperparameters(graph, gradient_variance):
    """
    Select step size and momentum for SMTPP
    
    Guidelines:
    - Step size: Smaller for sparse graphs
    - Momentum: Higher for high variance
    - Balance between convergence speed and stability
    """
    # Graph connectivity measure
    spectral_gap = compute_spectral_gap(graph)
    
    # Step size: inverse relationship with variance and graph size
    step_size = min(0.1, spectral_gap / (2 * gradient_variance))
    
    # Momentum: higher for high variance
    momentum = min(0.9, 0.5 + 0.4 * gradient_variance / (1 + gradient_variance))
    
    return step_size, momentum
```

## Applications

### Wireless Sensor Networks

- **Asymmetric links**: Different transmission ranges
- **Battery constraints**: Unidirectional communication
- **Dynamic topology**: Nodes joining/leaving

### Social Networks

- **Influence propagation**: Directed follower relationships
- **Opinion dynamics**: Asymmetric influence weights
- **Viral marketing**: Directional information flow

### Transportation Networks

- **Traffic flow**: One-way streets
- **Logistics**: Directed supply chains
- **Autonomous vehicles**: V2V communication

### Distributed Learning

- **Heterogeneous devices**: Different capabilities
- **Asymmetric bandwidth**: Upload/download differences
- **Peer-to-peer**: Direct device communication

## Comparison with Alternatives

| Method | Directed Graphs | Variance Robust | Topology Robust |
|--------|----------------|-----------------|-----------------|
| DSGD | ✗ | ✗ | ✗ |
| Push-Sum | ✓ | ✗ | ✗ |
| Push-Pull | ✓ | ✗ | Partial |
| **SMTPP** | **✓** | **✓** | **✓** |

## Experimental Results

### Non-Convex Logistic Regression

**Setup:**
- Dataset: Distributed across agents
- Graph: Various directed topologies
- Metric: Convergence rate, final error

**Results:**
- SMTPP matches centralized baseline
- Robust to network sparsity
- Outperforms standard Push-Pull with high variance

### Network Topology Robustness

| Graph Type | Density | SMTPP | Push-Pull | DSGD |
|------------|---------|-------|-----------|------|
| Complete | 100% | ✓ | ✓ | ✓ |
| Erdős-Rényi | 30% | ✓ | △ | ✗ |
| Ring | 2/n | ✓ | ✗ | ✗ |
| Star | 2/n | ✓ | ✗ | ✗ |

Legend: ✓ Good, △ Fair, ✗ Poor

## Theoretical Insights

### Why Momentum Helps

1. **Oscillation Damping**: Momentum smooths gradient estimates
2. **Variance Reduction**: Temporal averaging reduces noise
3. **Tracking Improvement**: Better gradient change estimation

### Topology Mismatch

```
In directed graphs:
  Row-stochastic ≠ Column-stochastic
  
This asymmetry creates:
  - Steady-state error (unavoidable)
  - Convergence to neighborhood (not point)

SMTPP minimizes this error through:
  - Careful momentum design
  - Decoupled variance reduction
```

## References

- **Paper**: "Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs" by Fan et al. (arXiv:2604.08219v1, 2026)
- **Categories**: math.OC

## Related Skills

- **decentralized-stochastic-momentum-admm**: For biased gradient handling
- **push-pull-optimization**: General Push-Pull methods
- **directed-graph-consensus**: Consensus on directed graphs

## Activation Keywords

- push-pull
- directed graph optimization
- SMTPP
- momentum tracking
- decentralized directed
- asymmetric network
- directed consensus
- column-stochastic
