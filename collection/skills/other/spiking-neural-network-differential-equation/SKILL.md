---
name: spiking-neural-network-differential-equation
description: "Differential equation analysis of SNN dynamics. Translates discrete spiking models into continuous ODE/PDE formulations for stability analysis, bifurcation study, and dynamical systems characterization. Activation: SNN differential equations, spiking dynamics analysis, ODE neuron model, bifurcation SNN, continuous-time spiking, dynamical systems neuroscience"
version: 1.0.0
metadata:
  hermes:
    tags: [spiking-neural-networks, dynamical-systems, differential-equations, analysis]
    source_paper: "arXiv:2501.05432"
---

# Differential Equation Framework for Spiking Neural Network Dynamics

## Overview

Analyzes SNN dynamics through continuous differential equation formulations. By translating discrete spike events into smooth ODE/PDE representations, enables classical dynamical systems analysis (stability, bifurcation, chaos detection) for spiking networks, bridging computational neuroscience with control theory.

## Core Concepts

### Continuous-time LIF Model (ODE)

```python
import numpy as np
from scipy.integrate import solve_ivp

def lif_ode(t, state, tau_mem=10.0, v_threshold=1.0, tau_syn=5.0, I_ext=0.5, refractory=2.0):
    v, i_syn, t_last_spike = state
    if t - t_last_spike < refractory:
        return [0, 0, t_last_spike]
    di_dt = -i_syn / tau_syn
    dv_dt = (-v + i_syn + I_ext) / tau_mem
    return [dv_dt, di_dt, t_last_spike]

sol = solve_ivp(lif_ode, [0, 100], [0, 0, -10], dense_output=True, max_step=0.1)
```

### Population Mean-Field Approximation

```python
def population_mean_field(v, t, N, tau, J, I_ext, v_threshold=1.0):
    phi = lambda x: 1 / (1 + np.exp(-5 * (x - v_threshold)))
    dvdt = (-v + J * N * phi(v) + I_ext) / tau
    return dvdt

def find_fixed_points(N, tau, J, I_ext):
    from scipy.optimize import fsolve
    phi = lambda v: 1 / (1 + np.exp(-5 * (v - 1.0)))
    eq_fn = lambda v: (-v + J * N * phi(v) + I_ext)
    v_stars = []
    for v0 in np.linspace(-2, 3, 20):
        v_star, _, ier, _ = fsolve(eq_fn, v0, full_output=True)
        if ier == 1 and -5 < v_star[0] < 5:
            if not any(abs(v_star[0] - vs) < 0.01 for vs in v_stars):
                v_stars.append(v_star[0])
    return sorted(v_stars)
```

### Bifurcation Analysis

```python
def bifurcation_diagram(J_range, N, tau, I_ext):
    return [(J, find_fixed_points(N, tau, J, I_ext)) for J in J_range]
```

## Applications

- Stability analysis of trained SNNs
- Bifurcation-based hyperparameter tuning
- Understanding oscillatory dynamics in recurrent SNNs
- Transfer learning between continuous and discrete models

## Pitfalls

1. Mean-field approximation loses single-neuron precision
2. Discontinuous spiking requires careful event detection
3. Bifurcation analysis assumes smooth dynamics
4. Large networks require moment closure approximations

## References

- arXiv:2501.05432
- Related: attractor-metadynamics-neural, neural-dynamics-criticality

## Activation Keywords

- SNN differential equations, spiking dynamics analysis, ODE neuron model, bifurcation SNN, continuous-time spiking, dynamical systems neuroscience, neural ODE spiking
