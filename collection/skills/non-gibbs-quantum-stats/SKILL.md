---
name: non-gibbs-quantum-stats
description: >
  Analysis of non-Gibbs quantum states in strongly interacting open quantum systems.
  Covers Redfield master equation, non-secular terms, bath-induced coherences,
  and conditions for deviation from Boltzmann thermal equilibrium. Based on arXiv:2606.00239.
---

# Non-Gibbs Quantum Statistics

## Problem

Redfield quantum master equation with secular approximation thermalizes to Gibbs state.
But non-secular terms can drive the system into a non-Gibbs steady state.

## Key Mechanism

For two strongly interacting quantum oscillators with independent baths at equal temperature:
- **Non-secular terms** → excitation flux driven by bath-induced coherences
- **Unequal damping** → steady state occupation deviates from Boltzmann distribution
- **Nearly-degenerate levels** → coherences between oscillator levels cause non-thermal occupation

## Mathematical Framework

### Redfield Equation
```
dρ/dt = -i[H, ρ] + R(ρ)
```
where R(ρ) contains secular and non-secular contributions.

### Secular Approximation
- Preserves positivity of reduced density operator
- Thermalizes to Gibbs state: ρ ∝ exp(-βH)

### Non-Secular Effects
- Drive system to non-Gibbs state
- Bath-induced coherences between nearly-degenerate levels
- Excitation flux depends on relative bath couplings

## Conditions for Gibbs Recovery

1. Equal damping by baths
2. Large level spacing (no near-degeneracy)
3. Weak system-bath coupling
4. Secular approximation valid

## Applications
- Open quantum system dynamics
- Quantum thermodynamics
- Quantum statistical mechanics
- Quantum heat engines and refrigerators
- Non-equilibrium quantum states

## Trigger Keywords
quantum statistics, Gibbs state, Redfield equation, non-secular, bath coherence, thermalization, open quantum systems, quantum thermodynamics, Boltzmann distribution

## Reference
- arXiv:2606.00239: "Bath-induced deviations from Gibbs statistics for strongly interacting oscillators" (Recabal et al., 2026)
