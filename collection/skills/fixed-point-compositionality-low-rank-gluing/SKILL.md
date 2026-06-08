---
name: fixed-point-compositionality-low-rank-gluing
description: "Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks — mathematical framework for understanding how structural modularity supports functional compositionality. Proves global fixed points are constrained to combinations of local fixed points. Activation: fixed point, compositionality, gluing, threshold-linear network, TLN, modular network, attractor, neural dynamics."
---

## Context

Brains generate complex behaviors through compositionality — decomposing tasks into reusable primitives. This paper provides rigorous mathematical characterization of how structural modularity supports functional compositionality in nonlinear networks using threshold-linear networks (TLNs).

**Key Contribution**: Introduces **low-rank gluings** — a novel class of modular network assembly where subnetworks are connected via specific low-rank couplings, enabling combinatorially large repertoire of predictable attractors.

**Paper**: arXiv:2606.07336 (Juniana Londono Alvarez, 2026-06-05)
**Category**: q-bio.NC (Neurons and Cognition)
**Pages**: 39 pages, 18 figures

## Core Methodology

### 1. Low-Rank Gluing Rules

**Definition**: Modular networks where component subnetworks with arbitrary internal connectivity are connected via specific low-rank couplings.

**Key Property**: Global fixed points are constrained to be combinations of local fixed points of constituent modules.

**Rank-1 Gluings (Structured Subclass)**:
- Complete characterization of which combinations of local fixed points yield global ones
- More tractable analysis than general low-rank gluings
- Explicit construction rules for compositional dynamics

### 2. Fixed Point Decomposition Rules

**Theorem**: For low-rank glued TLNs:
```
Global fixed points = Combinations of local fixed points
```

**Proof Framework**:
- Structural modularity → functional compositionality
- Inhibition-dominated networks have bounded attractor repertoire
- Gluing rules preserve combinatorial structure

### 3. Generalized CTLNs (gCTLNs)

**Extension**: From combinatorial threshold-linear networks (CTLNs) to generalized CTLNs:
- More flexible connectivity patterns
- Fixed point decomposition rules proven more robust than initially posited
- Graph-based networks support compositional attractors

### 4. Engineering Compositional Dynamics

**Recipe for Network Construction**:
1. Design component motifs with desired local fixed points
2. Apply rank-1 gluing rules to connect modules
3. Verify fixed point combinations via decomposition theorem
4. Result: Combinatorially large repertoire of predictable attractors

**Applications**:
- Fixed point compositions
- Compositional limit cycles
- Task-decomposition networks

## Implementation Steps

### Step 1: Define Component Motifs

```python
# Example: Simple fixed point motifs in TLN
import numpy as np

def create_tln_module(n_neurons, connectivity_matrix, thresholds):
    """Create a threshold-linear network module."""
    # TLN dynamics: dx/dt = -x + [Wx - T]_+
    # where [·]_+ is ReLU activation
    W = connectivity_matrix  # nxn matrix
    T = thresholds           # n-vector
    return {'W': W, 'T': T, 'n': n_neurons}
```

### Step 2: Apply Low-Rank Gluing

```python
def rank1_gluing(module1, module2, coupling_matrix):
    """
    Connect two TLN modules via rank-1 coupling.
    
    coupling_matrix: low-rank connection between modules
    """
    # Global network = module1 ⊕ module2 with coupling
    n_total = module1['n'] + module2['n']
    
    # Construct global connectivity
    W_global = np.zeros((n_total, n_total))
    W_global[:module1['n'], :module1['n']] = module1['W']
    W_global[module1['n']:, module1['n']:] = module2['W']
    
    # Add low-rank coupling
    W_global = add_lowrank_coupling(W_global, coupling_matrix)
    
    return W_global
```

### Step 3: Verify Fixed Point Compositions

```python
def verify_compositional_fixedpoints(module1_fps, module2_fps, global_network):
    """
    Check if global fixed points decompose into local combinations.
    
    Returns: dict of valid combinations
    """
    valid_combinations = {}
    
    for fp1 in module1_fps:
        for fp2 in module2_fps:
            candidate = combine_fixedpoints(fp1, fp2)
            if is_fixedpoint(candidate, global_network):
                valid_combinations[(fp1, fp2)] = candidate
    
    return valid_combinations
```

### Step 4: Generate Compositional Dynamics

```python
def simulate_compositional_tln(network, initial_state):
    """
    Simulate TLN dynamics and observe fixed point convergence.
    """
    # dx/dt = -x + [Wx - T]_+
    trajectory = []
    x = initial_state
    
    for t in range(max_iterations):
        dx = -x + np.maximum(network['W'] @ x - network['T'], 0)
        x = x + dt * dx
        trajectory.append(x)
        
        if converged(x, trajectory[-1]):
            break
    
    return trajectory, x  # final fixed point
```

## Key Results

1. **Mathematical Rigor**: First formal proof of compositionality in nonlinear TLNs
2. **Combinatorial Explosion**: n modules → potentially 2^n fixed point combinations
3. **Engineering Framework**: Recipe for constructing networks with predictable dynamics
4. **Robustness**: Decomposition rules hold beyond CTLNs to gCTLNs

## Pitfalls

- **High Inhibition Required**: Results specific to inhibition-dominated networks
- **Rank-1 Simplicity**: General low-rank gluings may not have complete characterization
- **Discrete Fixed Points**: Limit cycles require additional structure
- **Biological Validation**: Mathematical framework needs empirical confirmation

## Verification

- Fixed point decomposition theorem proven for rank-1 gluings
- Construction rules yield predicted attractors in simulations
- gCTLN extension verified across graph structures
- Compositional limit cycles demonstrated in structured cases

## Activation

- fixed point compositionality
- low-rank gluing
- threshold-linear network
- TLN
- modular network
- attractor decomposition
- compositional dynamics
- inhibition-dominated network
- gCTLN