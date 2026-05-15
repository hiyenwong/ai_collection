---
name: transport-mean-field-snn-dynamics
description: >
  Transport-based mean field theory for spiking neural network population dynamics.
  Derives approximate macroscopic firing rate evolution from Fokker-Planck transport
  solutions rather than steady-state assumptions. Use when: studying SNN population
  dynamics, firing rate fluctuations, mean field theory beyond asynchronous steady state,
  transport equations for neural populations, or integrate-and-fire network analysis.
  Based on arXiv:2605.14319 (Nicola & Campbell, May 2026).
---

# Transport Mean Field SNN Dynamics

Based on: *Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation* (arXiv:2605.14319, May 2026).

## Core Insight

Traditional mean field approaches assume asynchronous or constant-flux steady states. This work derives firing rate dynamics from the **transport (advection) solution** of the Fokker-Planck system, assuming:
1. Time-varying inputs are slow relative to neuronal dynamics
2. Neurons operate in the excitation-driven regime

This captures how firing rate fluctuations emerge from dynamic interaction between time-varying inputs, initial voltage distributions, and network coupling.

## Mathematical Framework

### Fokker-Planck System for IF Neurons

The population density rho(v,t) evolves as:

    d rho/dt = -d/dv[mu(t) * rho] + (sigma^2 / 2) * d^2 rho/dv^2 + boundary conditions

### Transport Approximation

For slow inputs and excitation-driven regime:
1. Solve the advection equation: d rho/dt = -d/dv[mu(t) * rho]
2. The instantaneous firing rate (flux) at threshold v_th: J(t) = mu(t) * rho(v_th, t)
3. Initial voltage distribution determines transient dynamics

### Key Equations

    d rho/dt + v * grad(rho) = 0   (transport equation)
    J(t) = integral of mu(t)*rho(v_th,t) dv   (instantaneous flux)

## Implementation Steps

1. Define initial voltage distribution rho(v, 0) - can be Gaussian, uniform, or empirical
2. Compute transport solution via method of characteristics
3. Derive flux at threshold boundary
4. Iterate with coupling: J(t) feeds back into mu(t) for recurrent networks

### Python Implementation Sketch

See scripts/transport_meanfield.py for full implementation.

## Applications

- **Population coding**: Understanding how neural populations encode time-varying stimuli
- **Working memory**: How initial state distributions affect sustained activity
- **Oscillatory dynamics**: Emergence of collective rhythms from coupled populations
- **Network stability**: When does coupling amplify vs. suppress fluctuations?

## Key Differences from Existing Approaches

| Approach | Assumption | Captures |
|----------|-----------|----------|
| Async steady-state | Constant flux | Equilibrium only |
| Linear response | Small perturbations | Near-equilibrium |
| Transport mean field | Slow inputs, excitation-driven | Full transient dynamics |

## Activation Keywords

- transport mean field
- SNN population dynamics
- Fokker-Planck neural
- firing rate fluctuations
- integrate-and-fire mean field
- neural transport equation
- macroscopic neural dynamics
- arXiv 2605.14319

## References

- Nicola, W. & Campbell, S.A. (2026). Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation. arXiv:2605.14319 [q-bio.NC, math.DS].
- Related: Brunel (2000) async state theory; Fourcaud & Brunel (2002) linear response
