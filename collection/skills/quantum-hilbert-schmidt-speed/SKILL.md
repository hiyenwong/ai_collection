---
name: quantum-hilbert-schmidt-speed
description: "Hilbert-Schmidt Speed (HSS) contractivity analysis for quantum channels — proves HSS contracts under unital CPTP maps, enabling non-Markovianity detection and discrimination of unital vs non-unital Markovian dynamics. Activation: hilbert schmidt speed, quantum channel contractivity, non-Markovianity detection, CPTP maps, open quantum systems, quantum dynamics monitoring."
---

## Overview

This skill provides a methodology for analyzing quantum channel dynamics using the Hilbert-Schmidt Speed (HSS) — a geometric indicator defined through the Hilbert-Schmidt norm of the tangent vector to a parametrized family of quantum states. The key theoretical result: HSS is contractive under every unital CPTP map, providing a foundation for witnessing non-Markovianity and discriminating unital from non-unital Markovian dynamics.

## Core Theory

### Hilbert-Schmidt Speed Definition

For a parametrized family of quantum states ρ(θ):
```
HSS(θ) = ||dρ(θ)/dθ||_HS = sqrt(Tr[(dρ/dθ)²])
```

### Contractivity Theorem

For any unital CPTP map Φ and parameter-dependent states ρ(θ):
```
HSS(Φ(ρ(θ))) ≤ HSS(ρ(θ))
```

This means the "speed" of state evolution can only decrease under unital channels.

### Non-Markovianity Witness

If HSS *increases* at any point during evolution:
```
d/dt HSS(ρ(t)) > 0
```
This signals information backflow → non-Markovian dynamics.

## Implementation Steps

### Step 1: Compute HSS for Parametrized States

```python
import numpy as np
from scipy.linalg import norm

def hilbert_schmidt_speed(rho_plus_eps, rho_minus_eps, eps):
    """
    Compute HSS via finite differences.
    
    Args:
        rho_plus_eps: ρ(θ + ε) density matrix
        rho_minus_eps: ρ(θ - ε) density matrix
        eps: Step size
    
    Returns:
        hss: Hilbert-Schmidt speed at θ
    """
    drho = (rho_plus_eps - rho_minus_eps) / (2 * eps)
    return norm(drho, 'fro')  # Frobenius norm = HS norm for matrices
```

### Step 2: Detect Non-Markovianity

```python
def detect_nonmarkovianity(state_trajectory, dt):
    """
    Detect non-Markovian dynamics via HSS increase.
    
    Args:
        state_trajectory: List of density matrices [ρ(t₀), ρ(t₁), ...]
        dt: Time step
    
    Returns:
        nonmarkovian_times: Time points where HSS increased
    """
    hss_values = []
    for i in range(1, len(state_trajectory) - 1):
        hss = hilbert_schmidt_speed(
            state_trajectory[i + 1],
            state_trajectory[i - 1],
            2 * dt
        )
        hss_values.append(hss)
    
    # Non-Markovianity: HSS increase
    nonmarkovian_times = []
    for i in range(1, len(hss_values)):
        if hss_values[i] > hss_values[i-1]:
            nonmarkovian_times.append(i * dt)
    
    return nonmarkovian_times, hss_values
```

### Step 3: Discriminate Unital vs Non-Unital Channels

```python
def test_unital_channel(channel_map, test_states):
    """
    Test if a channel is unital by checking HSS contractivity.
    
    A channel is unital iff HSS is contractive for ALL input state families.
    
    Args:
        channel_map: Function implementing the quantum channel
        test_states: List of parametrized state families
    
    Returns:
        is_unital: Boolean
        violations: Contractivity violations found
    """
    violations = []
    
    for state_family in test_states:
        hss_input = compute_hss_family(state_family)
        hss_output = compute_hss_family([channel_map(rho) for rho in state_family])
        
        if np.any(hss_output > hss_input + 1e-10):  # tolerance
            violations.append({
                'input_hss': hss_input.tolist(),
                'output_hss': hss_output.tolist(),
                'is_unital': False
            })
    
    return len(violations) == 0, violations
```

### Step 4: Monitor Quantum Dynamics

```python
def monitor_dynamics(initial_state, time_evolution, t_max, n_steps):
    """
    Continuous monitoring of quantum dynamics using HSS.
    
    Returns timeline of HSS values, flagging any increases
    as potential non-Markovian events.
    """
    times = np.linspace(0, t_max, n_steps)
    states = [time_evolution(initial_state, t) for t in times]
    
    hss = [hilbert_schmidt_speed(states[i+1], states[i-1], 
                                 2*(times[1]-times[0]))
           for i in range(1, n_steps-1)]
    
    return {
        'times': times[1:-1],
        'hss': hss,
        'nonmarkovian_events': [
            {'time': times[i], 'hss_before': hss[i-1], 'hss_after': hss[i]}
            for i in range(1, len(hss))
            if hss[i] > hss[i-1]
        ]
    }
```

## When to Use

- Detecting non-Markovian dynamics in open quantum systems
- Characterizing quantum channels as unital vs non-unital
- Monitoring quantum evolution for information backflow
- Quantum error detection: unexpected HSS increases signal errors
- Benchmarking quantum simulators against theoretical bounds
- Studying decoherence mechanisms and memory effects

## Key Reference

- arXiv:2607.05619 — "Contractivity of the Hilbert--Schmidt Speed in Unital Quantum Channels"
- Framework: Finite-dimensional, parameter-independent CPTP evolution
- Parameter encoded solely in initial state
