---
name: brain-rhythm-synchronization-connectome
description: Kuramoto oscillator model for brain rhythm synchronization using empirical connectome data. Studies how structural connectivity shapes synchronized oscillations, identifies critical coupling thresholds, and reveals community-based synchronization patterns. Applies to resting-state networks and functional connectivity prediction.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-rhythms, synchronization, kuramoto-model, connectome, functional-connectivity, phase-dynamics, resting-state, multistability]
    source_paper: "Synchronization of brain rhythms in the connectome (arXiv:2603.15066)"
    published: 2026-03-19
---

# Brain Rhythm Synchronization in the Connectome

## Overview

Studies how the brain's structural connectome shapes synchronized oscillatory dynamics using the **Kuramoto model**. Maps structural connectivity to functional synchronization patterns and identifies critical coupling thresholds for synchronization onset.

## Core Problem

How does the brain's physical wiring (structural connectivity) constrain and shape the emergence of synchronized oscillatory activity? Understanding this link is essential for predicting functional connectivity from structural data, identifying brain rhythm disorders, and understanding how hub regions coordinate global brain dynamics.

## Kuramoto Model on Connectome

```python
import numpy as np
from scipy.integrate import solve_ivp

def kuramoto_on_connectome(SC, K, omega=None):
    """
    Kuramoto model on structural connectome.
    
    Args:
        SC: N×N structural connectivity matrix (weights)
        K: global coupling strength
        omega: natural frequencies (optional, default: random)
    
    Returns:
        Phase trajectories for each brain region
    """
    N = SC.shape[0]
    if omega is None:
        omega = np.random.randn(N) * 0.1  # small heterogeneity
    
    def dphi_dt(t, phi):
        dphi = np.zeros(N)
        for i in range(N):
            coupling = np.sum(SC[i, :] * np.sin(phi - phi[i]))
            dphi[i] = omega[i] + K * coupling
        return dphi
    
    phi0 = np.random.uniform(0, 2*np.pi, N)
    t_span = (0, 100)
    t_eval = np.linspace(0, 100, 1000)
    
    sol = solve_ivp(dphi_dt, t_span, phi0, t_eval=t_eval, method='RK45')
    return sol.t, sol.y

# Synchronization order parameter
def order_parameter(phi):
    """Compute global synchronization level: R = |mean(exp(i*phi))|"""
    return np.abs(np.mean(np.exp(1j * phi), axis=0))
```

## Analysis Pipeline

1. **Obtain structural connectivity matrix** from DTI/tractography data
2. **Define Kuramoto oscillator equations** per brain region node
3. **Vary global coupling parameter K** systematically (bifurcation analysis)
4. **Measure order parameter** (synchronization level) as function of K
5. **Identify critical transitions** where synchronization emerges
6. **Characterize metastable states** near critical coupling
7. **Compare predicted FC** with empirical resting-state FC

## Key Findings

### Structural Constraints on Synchronization

- SC topology determines which rhythms can synchronize
- Community structure creates multi-cluster synchronization states
- Hub regions (high degree/strength) drive global synchronization transitions
- Rich-club organization facilitates long-range synchronization

### Critical Coupling and Multistability

- Sharp transition from desynchronized to synchronized states at critical K
- Multiple stable synchronization patterns coexist near critical point
- Metastable switching between patterns mirrors resting-state dynamics
- Critical region maximizes dynamic repertoire and functional flexibility

### Functional Connectivity Prediction

- Time-averaged phase correlations predict empirical FC patterns
- Model captures both positive and negative functional connections
- Community structure in SC manifests as FC modules
- Individual SC variation explains individual FC variation

## Applications

- **Resting-state network modeling**: Predict FC from SC
- **Brain rhythm disorders**: Identify coupling abnormalities in epilepsy, schizophrenia
- **Connectome-constrained dynamical modeling**: Bridge structure and function
- **Multistability analysis**: Understand brain state transitions
- **Individual differences**: Link structural variation to functional differences

## Implementation Tips

### Parameter Selection
- Use empirically measured SC weights (normalized)
- Natural frequencies: small Gaussian spread (~1 Hz for alpha band)
- Integration: adaptive step size for accuracy near critical points

### Analysis Methods
- Order parameter for global synchronization
- Kuramoto order parameter per community for cluster synchronization
- Bifurcation diagrams for critical coupling identification
- Dwell time analysis for metastable state characterization

### Validation
- Compare predicted FC matrices with empirical FC (correlation)
- Test against shuffled SC (destroy topology, preserve weight distribution)
- Individual-level prediction accuracy

## Limitations

- Simplified oscillator model (ignores amplitude dynamics)
- Static connectome (no structural plasticity)
- No time delays (can be added for realism)
- Linear coupling assumption

## Extensions

- Add time delays from fiber tract lengths
- Include adaptive coupling (structural plasticity)
- Use more realistic neural mass models
- Study effects of lesions on synchronization

## Reference

- Paper: "Synchronization of brain rhythms in the connectome"
- arXiv: 2603.15066
- Published: 2026-03-19
