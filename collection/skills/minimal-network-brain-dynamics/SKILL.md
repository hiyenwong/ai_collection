---
name: minimal-network-brain-dynamics
description: "Minimal Network Models of Brain Dynamics — studying how sparse, optimized network topologies reproduce neural dynamics. Covers structural-functional coupling, criticality in minimal networks, and topology-dynamics relationships. Use when analyzing brain network dynamics with minimal/sparse models, studying structure-function coupling, investigating criticality in neural networks, or comparing real vs. minimal network architectures. Triggers: minimal network, brain dynamics, sparse connectivity, structure-function coupling, network topology dynamics, criticality, neural oscillations."
---

## Minimal Network Models of Brain Dynamics

### Core Concept

Minimal network models identify the sparsest connectivity that reproduces key dynamical features of brain activity (functional connectivity patterns, oscillatory dynamics, critical behavior). This reveals which connections are computationally essential.

### Methodology

#### 1. Network Optimization

Minimize connections while preserving dynamics:

```
min ||A||_0  s.t.  D(sim(F(A), F_target)) < ε
```

Where A = adjacency matrix, F = dynamics function, F_target = target brain activity.

#### 2. Key Approaches

- **Greedy pruning**: Iteratively remove weakest edges while monitoring FC reconstruction error
- **L1-regularized optimization**: Continuous relaxation with sparsity penalty
- **Genetic algorithms**: Evolutionary search for minimal topologies
- **Information-theoretic**: Retain edges maximizing mutual information with target dynamics

#### 3. Evaluation Metrics

- **FC reconstruction**: Correlation between model and empirical functional connectivity
- **Dynamic repertoire**: Diversity of metastable states compared to empirical data
- **Criticality indices**: Avalanche size distributions, branching ratio, susceptibility
- **Structural efficiency**: Connection cost vs. dynamical fidelity trade-off

#### 4. Key Findings

- ~10-30% of structural connections can reproduce ~80% of FC patterns
- Hub nodes disproportionately preserved in minimal networks
- Rich-club organization emerges as dynamical necessity
- Minimal networks often exhibit enhanced criticality compared to full networks

### Implementation Pattern

```python
import numpy as np
from sklearn.metrics import mutual_info_score

def minimal_network_dynamics(SC, empirical_FC, n_nodes, 
                              target_sparsity=0.2, max_iter=1000):
    """Find minimal network reproducing empirical FC dynamics."""
    # Initialize with full structural connectome
    A = SC.copy()
    
    # Simulate dynamics (e.g., Kuramoto, Hopf, Wilson-Cowan)
    fc_model = simulate_dynamics(A, n_nodes)
    
    # Iterative pruning
    for iteration in range(max_iter):
        current_sparsity = np.count_nonzero(A) / (n_nodes * n_nodes)
        if current_sparsity <= target_sparsity:
            break
            
        # Score edges by contribution to FC fidelity
        edge_scores = score_edge_importance(A, fc_model, empirical_FC)
        
        # Remove lowest-scoring edge
        min_edge = np.unravel_index(np.argmin(edge_scores), A.shape)
        A[min_edge] = 0
        A[min_edge[1], min_edge[0]] = 0  # Undirected
        
        fc_model = simulate_dynamics(A, n_nodes)
        
    return A, fc_model
```

### Dynamics Models

- **Kuramoto oscillator model**: Phase synchronization, frequency analysis
- **Hopf normal form**: Bifurcation-based oscillatory dynamics  
- **Wilson-Cowan**: Excitatory-inhibitory population dynamics
- **Ising model**: Binary state criticality analysis

### When to Use

- Identifying essential pathways in brain networks
- Testing structure-function coupling hypotheses
- Reducing computational cost of whole-brain simulations
- Understanding criticality emergence from topology
- Comparing healthy vs. pathological network efficiency

### Pitfalls

- Different dynamics models may yield different minimal networks
- Sparsity threshold choice significantly affects results
- Directional connectivity often lost in undirected models
- Empirical FC noise can misguide pruning decisions

## Activation Keywords

- "minimal-network-brain-dynamics"
- "minimal network brain dynamics"
- "use minimal network brain dynamics"
- "minimal network brain dynamics help"
- "minimal network brain dynamics analysis"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify the user's specific question or task related to Minimal Network Brain Dynamics
2. Gather relevant context from files or user input
3. Apply Minimal Network Brain Dynamics methodology to address the request
4. Provide clear results with actionable insights

## Examples

### Basic usage
```
User: "Help me with minimal network brain dynamics"
→ Understand requirements → Apply methodology → Provide results
```

### Advanced usage
```
User: "I need detailed Minimal Network Brain Dynamics assistance"
→ Clarify scope → Execute analysis → Present findings
```
