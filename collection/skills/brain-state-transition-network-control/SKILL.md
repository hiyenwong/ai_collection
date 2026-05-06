---
name: brain-state-transition-network-control
description: Brain state transition dynamics and network control methodology. Studies how brain networks transition between cognitive states, combining controllability theory with functional connectivity analysis. Applicable to brain stimulation, cognitive state manipulation, and neurological disorder intervention.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-network, state-transition, controllability, neural-dynamics, cognitive-states]
---

# Brain State Transition Network Control

## Overview
Methodology for analyzing and controlling brain state transitions using network controllability theory. Combines structural and functional brain connectivity to model how the brain transitions between different cognitive, emotional, and behavioral states.

## Core Concepts

### State Space Model
- **Brain states**: Represented as points in a high-dimensional space defined by regional activity
- **State transitions**: Governed by network connectivity and external inputs
- **Minimum control energy**: Energy required to drive brain from one state to another

### Controllability Framework
- **Structural controllability**: Based on white matter tract connectivity (DTI)
- **Functional controllability**: Based on functional connectivity patterns (fMRI)
- **Modal controllability**: Ability to control specific modes of brain dynamics

### Key Metrics
- **Average controllability**: How easily a region can drive the network to many states
- **Modal controllability**: How well a region can drive specific dynamical modes
- **Control energy**: Energy required for state-to-state transitions
- **Boundary controllability**: Integration vs. segregation of functional communities

## Implementation

```python
import numpy as np
from numpy.linalg import inv, eig, matrix_rank

def controllability_gramian(A, B, T=10):
    """Compute finite-horizon controllability Gramian."""
    n = A.shape[0]
    Wc = np.zeros((n, n))
    
    # Discrete-time approximation
    dt = T / 100
    for k in range(100):
        t = k * dt
        exp_At = _matrix_exp(A * t)
        Wc += exp_At @ B @ B.T @ exp_At.T * dt
    
    return Wc

def average_controllability(A):
    """Average controllability of network with A as adjacency matrix."""
    n = A.shape[0]
    B = np.eye(n)  # All nodes as control inputs
    Wc = controllability_gramian(-np.eye(n) + A, B)
    return np.trace(Wc) / n

def modal_controllability(A):
    """Modal controllability - ability to control specific eigenmodes."""
    eigenvalues, eigenvectors = eig(A)
    n = A.shape[0]
    
    # Modal controllability for each node
    MC = np.zeros(n)
    for i in range(n):
        MC[i] = 1 - np.sum(np.abs(eigenvectors[i, :]) ** 2 * np.abs(eigenvalues))
    
    return MC

def minimum_control_energy(A, x0, xf, T=10):
    """Minimum energy to transition from state x0 to xf."""
    n = A.shape[0]
    B = np.eye(n)
    Wc = controllability_gramian(-np.eye(n) + A, B, T)
    
    # Control energy
    diff = xf - _matrix_exp(A * T) @ x0
    energy = diff.T @ inv(Wc) @ diff
    return energy.real

def _matrix_exp(M):
    """Matrix exponential approximation."""
    from scipy.linalg import expm
    return expm(M)
```

## Applications
- **Transcranial magnetic stimulation (TMS)**: Optimal stimulation targets
- **Deep brain stimulation (DBS)**: Electrode placement optimization
- **Cognitive enhancement**: Identifying control nodes for specific cognitive states
- **Neurological disorders**: Understanding impaired state transitions in depression, schizophrenia

## References
- Gu, S. et al. (2015). Controllability of structural brain networks. Nature Communications.
- Muldoon, S.F. et al. (2016). Stimulation-based control of dynamic brain networks. PLoS Computational Biology.

## Related
- [[brain-network-controllability]]
- [[brain-network-topology]]
- [[neural-dynamics-criticality]]
- [[brain-stimulation-dynamics-state]]
