---
name: counterfactual-brain-dynamics
description: >
  Counterfausal causal analysis framework for brain network dynamics using Hodge theory 
  and minimum-energy principles. Models pathological disruptions and therapeutic interventions 
  as energy-perturbation problems on network flows. Decomposes directed communication into 
  dissipative and persistent (harmonic) components. Use when analyzing brain network causality, 
  counterfactual interventions, network resilience, epilepsy models, Hodge decomposition on 
  brain graphs, or causal inference beyond Granger/DCM. Triggered by: counterfactual brain, 
  Hodge theory brain, causal brain network, brain network intervention, harmonic flow brain, 
  Dirichlet energy network, temporal lobe epilepsy network, brain network resilience, 
  counterfausal neuroimaging.
license: CC BY-NC-SA 4.0
---

# Counterfausal Analysis of Brain Network Dynamics

Based on: Chung et al., "Counterfausal Analysis of Brain Network Dynamics" (arXiv:2603.29843, ISBI 2026)

## Core Framework

Traditional causal inference methods (Granger causality, SEM, DCM) are descriptive and acyclic — they identify directed associations but cannot model interventions. This framework answers **"what would happen if a pathway were disrupted?"** by modeling perturbations as energy changes on network flows.

### Key Mathematical Components

1. **Spatial Scaffold**: Build simplicial complexes from brain parcellation (e.g., AAL 116 regions) to capture pairwise AND higher-order interactions
2. **Dirichlet Potential Energy**: Represent directed functional interactions as energy-carrying edge flows
3. **Hodge Decomposition**: Decompose flows into:
   - **Gradient (dissipative)**: Potential-driven flow that dissipates energy
   - **Harmonic (persistent)**: Circulating flow that persists without energy loss
   - **Curl (local circulation)**: Local cyclic patterns

### Counterfausal Protocol

```
1. Construct baseline brain network from rs-fMRI (or task fMRI)
2. Compute Hodge decomposition of edge flows
3. Define perturbation (lesion, neuromodulation, disconnection)
4. Recompute energy landscape under perturbation
5. Compare pre/post harmonic flow patterns
6. Quantify: resilience, compensation, control capacity
```

### Applications

- **Pathological disruption modeling**: Simulate disease effects (e.g., TLE recurrence patterns)
- **Therapeutic intervention planning**: Predict outcomes of surgical disconnection or neuromodulation
- **Network resilience quantification**: Measure how well network maintains function under perturbation
- **Compensation analysis**: Identify alternative pathways that emerge after disruption

## Implementation Workflow

### Data Requirements
- rs-fMRI or task-fMRI time series (minimum ~1200 time points recommended)
- Brain parcellation atlas (AAL 116, Schaefer, etc.)
- Preprocessed with standard pipelines (motion correction, normalization)

### Hodge Decomposition on Brain Networks

```python
import numpy as np
from scipy.sparse import csr_matrix

def hodge_decomposition(adjacency, edge_flows):
    """
    Decompose edge flows on brain network using Hodge theory.
    
    Args:
        adjacency: NxN adjacency matrix (structural or functional connectivity)
        edge_flows: directed flow values on edges
    
    Returns:
        gradient: dissipative component
        harmonic: persistent component  
        curl: local circulation component
    """
    # Build boundary operators from simplicial complex
    # B1: edge-to-node boundary (gradient operator)
    # B2: triangle-to-edge boundary (curl operator)
    
    # Gradient component: phi = (B1^T B1)^{-1} B1^T flow
    # Harmonic component: in null space of both B1^T and B2
    # Curl component: B2 * psi
    
    pass
```

### Dirichlet Energy Computation

The Dirichlet energy of a network flow measures total "effort" of communication:

```
E_D = sum over edges (w_ij * (f_i - f_j)^2)
```

where w_ij is edge weight and f_i, f_j are node potentials.

Perturbations change this energy landscape — counterfactual analysis tracks how energy redistributes.

## Key Insights from ISBI 2026 Paper

- Applied to 400 HCP subjects with AAL 116 parcellation
- Demonstrated on temporal lobe epilepsy (TLE): pathological recurrence vs therapeutic disconnection
- Harmonic flow captures the "persistent" communication patterns resistant to disruption
- Framework provides principled quantification of network resilience without needing interventional data

## When to Use vs Alternatives

| Method | Captures | Interventional? | Cyclic? |
|--------|----------|-----------------|---------|
| Granger | Directed association | No | No |
| DCM | Effective connectivity | Hypothesis testing | No |
| **Hodge/Counterfactual** | **Energy-based causality** | **Yes (simulated)** | **Yes** |

## Related Skills
- `brain-network-controllability` - Network control theory metrics
- `time-varying-brain-connectivity` - Dynamic connectivity analysis
- `hermes-brain-connectivity` - HERMES toolbox for connectivity analysis
