---
name: effective-plasticity
description: "Network-based framework for quantifying plasticity as system_size/connectivity_ratio. Defines effective plasticity as normalized measure linked to critical regime. Plasticity drives criticality causally. Activation: effective plasticity, plasticity quantification, network plasticity measure, plasticity criticality, system size connectivity, Branchi plasticity."
---

# Effective Plasticity: Network-Based Quantification Framework

> Operationalizes plasticity as the ratio between system size and connectivity strength, defining effective plasticity as a normalized measure that links structural properties to dynamical regimes, with plasticity driving criticality.

## Metadata
- **Source**: arXiv:2603.25180
- **Authors**: Igor Branchi
- **Published**: 2026-03-26
- **Categories**: q-bio.NC, cond-mat.dis-nn, cond-mat.stat-mech, nlin.AO, physics.bio-ph

## Core Methodology

### Key Innovation
Plasticity is transformed from a descriptive, retrospective concept into a **predictive, quantitative measure** by formalizing it as:

```
Plasticity = System_Size / Connectivity_Strength
```

Where:
- **System size** determines the dimensionality of the accessible state space
- **Connectivity strength** tunes the system's dynamical regime
- **Effective plasticity** emerges at intermediate connectivity, coinciding with the **critical regime**

### Technical Framework

1. **Define system size (N)**: Number of elements/nodes in the network
2. **Define connectivity strength (C)**: Average coupling/interaction strength among elements
3. **Compute plasticity ratio**: P = N / C
4. **Identify critical regime**: The optimal range where P balances capacity for change vs. capacity to maintain coherence
5. **Normalize as effective plasticity**: Use critical regime as theoretically motivated benchmark

### Causal Relationship: Plasticity → Criticality

The framework establishes that **plasticity drives criticality**, not merely accompanies it:
- Plasticity acts as a **structural tuning parameter** for criticality
- Larger systems can more robustly maintain critical dynamics through this relationship
- The relationship is causal: adjusting plasticity parameters shifts the system toward or away from criticality

### Distinguishing Regime Shifts vs. Phase Changes

The framework distinguishes:
- **Functional regime shifts**: Changes in dynamic repertoire driven by plasticity tuning
- **Thermodynamic phase changes**: Physical state transitions

Plasticity is the system-level regulator that shapes and constrains the dynamic repertoire.

## Applications
- **Cross-system comparison**: Normalized effective plasticity enables comparing adaptive efficacy across diverse systems (neural, ecological, economic, social)
- **Psychopathology prediction**: Anticipates transitions between mental states before they occur
- **Neural network design**: Optimal connectivity for balancing learning capacity and stability
- **Complexity science**: Unified measure for adaptive systems across domains
- **Criticality engineering**: Using plasticity as control knob for critical dynamics

## Implementation Guide

### Step-by-Step Analysis

1. **Map the network**: Identify nodes (N) and edges with weights
2. **Compute system size**: Count effective degrees of freedom
3. **Estimate connectivity strength**: Average absolute weight or coupling parameter
4. **Calculate plasticity ratio**: P = N / C
5. **Compare to critical benchmark**: Is P in the intermediate range associated with critical dynamics?
6. **Track over time**: Monitor how P changes and predict regime transitions

### Code Example
```python
import numpy as np

def compute_effective_plasticity(adjacency_matrix):
    """
    Compute effective plasticity from network adjacency matrix.
    
    Args:
        adjacency_matrix: N×N matrix of connection strengths
    
    Returns:
        plasticity_ratio, connectivity_strength, system_size
    """
    N = adjacency_matrix.shape[0]  # System size
    # Connectivity strength: mean absolute off-diagonal weight
    mask = ~np.eye(N, dtype=bool)
    C = np.mean(np.abs(adjacency_matrix[mask]))
    
    plasticity = N / C if C > 0 else float('inf')
    return plasticity, C, N

def is_critical(plasticity_ratio, critical_bounds=(0.5, 2.0)):
    """Check if system is in critical regime."""
    return critical_bounds[0] <= plasticity_ratio <= critical_bounds[1]
```

## Pitfalls
- **Domain-specific calibration**: Critical bounds may vary across domains; use empirical calibration
- **Dynamic systems**: For time-varying networks, compute plasticity in sliding windows
- **Not a standalone metric**: Effective plasticity should be combined with dynamical analysis (Lyapunov exponents, etc.)
- **Cross-domain comparison**: Requires careful normalization of system size definition across domains

## Related Skills
- complex-system-robustness-collapse
- brain-criticality-assessment
- brain-criticality-hypothesis-assessment
- brain-criticality-milro-assessment
- hierarchical-brain-criticality
- griffiths-phase-brain-criticality
- stochastic-synaptic-plasticity
- neuromodulated-synaptic-plasticity
- synaptic-weight-distributions-plasticity-geometry
