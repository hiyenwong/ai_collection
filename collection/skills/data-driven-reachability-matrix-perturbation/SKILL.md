---
name: data-driven-reachability-matrix-perturbation
description: Data-driven reachability analysis using matrix perturbation bounds for verifying system safety and control properties without explicit system models.
version: 1.0.0
metadata:
  hermes:
    tags: [control-theory, reachability, data-driven, verification]
---

# Data-Driven Reachability via Matrix Perturbation

## Overview
Computes reachable sets for dynamical systems using only trajectory data, leveraging matrix perturbation theory to bound uncertainties.

## Core Method
- Collect input-output trajectory data
- Construct Hankel matrices from data
- Apply perturbation bounds to characterize uncertainty
- Compute over-approximation of reachable sets

## Implementation
```python
import numpy as np

def hankel_matrix(data, L):
    '''Construct Hankel matrix from trajectory data.'''
    T = len(data)
    return np.array([data[i:i+L] for i in range(T-L+1)]).T

def data_driven_reachability(U, Y, horizon, perturbation_bound=0.01):
    '''Compute reachable set from input-output data.'''
    # Hankel matrices
    Hu = hankel_matrix(U, horizon)
    Hy = hankel_matrix(Y, horizon)
    
    # Solve for trajectory representation
    alpha = np.linalg.lstsq(Hu, Y[:horizon], rcond=None)[0]
    
    # Perturbation bounds
    reachable = Hy @ alpha
    uncertainty = perturbation_bound * np.linalg.norm(alpha)
    return reachable, uncertainty
```
