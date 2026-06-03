---
name: transport-mean-field-snn
description: >
  Transport Mean Field methodology for approximate macroscopic dynamics of spiking neural networks.
  Derives population firing rate evolution from initial voltage distributions via transport
  (advection) solution to the Fokker-Planck system, unlike earlier mean field approaches based
  on asynchronous steady-state solutions. Assumes slow time-varying inputs and excitation-driven
  regime. Use when: analyzing SNN population dynamics, deriving mean field approximations,
  studying firing rate fluctuations, modeling neural population responses to time-varying inputs,
  or understanding how initial conditions shape population-level dynamics.
---

# Transport Mean Field for Spiking Neural Network Population Dynamics

**Paper**: Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation
**Authors**: Wilten Nicola, Sue Ann Campbell (arXiv:2605.14319v1, May 2026)

## Core Idea

Derives an analytical approximation for the evolution of instantaneous population firing rate
as a function of the initial voltage distribution in networks of coupled integrate-and-fire neurons
with time-varying inputs. Uses the **transport solution** (advection equation) rather than
asynchronous steady-state solutions to the Fokker-Planck system.

## Key Distinction from Prior Mean Field Approaches

| Aspect | Prior Mean Field | Transport Mean Field (this work) |
|--------|-----------------|----------------------------------|
| Basis | Asynchronous/constant flux steady state | Transport solution to advection equation |
| Input assumption | Constant inputs | Slow time-varying inputs |
| Regime | General | Excitation-driven regime |
| Captures | Average firing rate | Firing rate fluctuations from initial conditions |

## Mathematical Framework

### Transport Mean Field System

For a population of coupled integrate-and-fire neurons:

1. **Voltage distribution evolution**: The population voltage density evolves via the
   transport (advection) equation derived from the Fokker-Planck system.

2. **Instantaneous flux/firing rate**: The firing rate at time t depends on:
   - The initial voltage distribution across the population
   - Time-varying external inputs (assumed slow)
   - Coupling strength between neurons

3. **Key insight**: Firing rate fluctuations emerge from dynamic interaction between:
   - Time-varying inputs
   - Initial voltage densities
   - Network coupling

### When the Approximation Holds

- Inputs vary slowly compared to neuronal timescales
- Neurons operate in excitation-driven regime
- Population is sufficiently large for mean field approximation

## Applications

### 1. Population Dynamics Analysis
- Predict how heterogeneous initial conditions affect population firing patterns
- Understand emergence of oscillations or transients in SNN populations

### 2. Firing Rate Fluctuation Modeling
- Explain experimentally observed multi-timescale firing rate fluctuations
- Connect single-neuron properties to population-level dynamics

### 3. Network Design
- Choose initial conditions to achieve desired population dynamics
- Understand how coupling strength shapes collective behavior

## Implementation Guide

### Numerical Simulation

```python
import numpy as np

def transport_mean_field(v0_dist, input_fn, coupling, dt=0.1, T=100):
    """
    Approximate population firing rate via transport solution.
    
    Args:
        v0_dist: Initial voltage distribution (array)
        input_fn: Function t -> external input at time t
        coupling: Coupling strength between neurons
        dt: Time step
        T: Total simulation time
    
    Returns:
        firing_rates: Array of instantaneous firing rates
    """
    n_steps = int(T / dt)
    firing_rates = np.zeros(n_steps)
    
    # Track voltage distribution evolution via transport
    # (simplified 1D advection with input-driven drift)
    v_dist = v0_dist.copy()
    
    for t in range(n_steps):
        # Compute drift from input and coupling
        I_ext = input_fn(t * dt)
        drift = I_ext + coupling * firing_rates[max(0, t-1)]
        
        # Transport: shift distribution by drift
        v_dist = np.roll(v_dist, -int(drift / dt))
        
        # Firing rate = flux at threshold
        firing_rates[t] = v_dist[-1] * drift
    
    return firing_rates
```

### Connection to Fokker-Planck

The full Fokker-Planck equation for the voltage density p(v, t):

```
∂p/∂t = -∂/∂v [μ(v,t) p] + (σ²/2) ∂²p/∂v²
```

The transport approximation neglects the diffusion term, keeping only the advection:

```
∂p/∂t = -∂/∂v [μ(v,t) p]
```

This is valid when drift dominates diffusion (excitation-driven regime).

## Activation Keywords

- transport mean field SNN, mean field approximation SNN
- population firing rate dynamics, neural population dynamics
- Fokker-Planck SNN, advection equation neural dynamics
- firing rate fluctuations, integrate-and-fire population
- 传输平均场, 脉冲神经网络群体动力学
- macroscopic neural dynamics, voltage distribution evolution

## Related Skills

- `transport-mean-field-snn-dynamics`: Extended version with transport-based mean field theory
- `snn-performance-analysis`: General SNN analysis methods
- `neural-population-dynamics`: Broader neural population analysis framework
