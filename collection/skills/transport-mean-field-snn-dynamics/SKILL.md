---
name: transport-mean-field-snn-dynamics
description: >
  Transport-based mean field theory for spiking neural network population dynamics. Analytically
  derives firing rate fluctuations from initial voltage distributions via transport equation
  solutions to the Fokker-Planck system. Use when: SNN mean field theory, neural population
  dynamics, firing rate fluctuations, Fokker-Planck analysis, transport equation for neurons,
  LIF/QIF network analysis, asynchronous state theory, neural mass models.
---

# Transport Mean Field Theory for SNN Dynamics

## Overview

Analytical framework for understanding how firing rate fluctuations emerge in coupled spiking
neural networks as a function of initial voltage distributions and time-varying inputs.

**Paper**: Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation (arXiv:2605.14319v1)

**Authors**: Wilten Nicola, Sue Ann Campbell (University of Calgary, University of Waterloo)

## Key Theoretical Contributions

### Transport Mean Field System
Unlike traditional mean field theories assuming asynchronous steady states, this approach:
- Uses transport solution to the advection equation
- Assumes slow time-varying inputs and excitation-driven regime
- Predicts firing rate fluctuations from dynamic interaction between:
  1. Time-varying inputs
  2. Initial voltage densities
  3. Network coupling strength

### Mathematical Framework

#### Fokker-Planck System
Starting point for population-level description of coupled integrate-and-fire neurons:
- Density evolution: ∂ρ/∂t + ∂/∂v[(F(v) + I(t))ρ] = diffusion terms
- Flux at threshold gives population firing rate

#### Transport Equation Solution
For excitation-driven regime with slow inputs:
- Probability integral transform maps voltage domain to phase domain
- Density evolves as rigid rotation in phase space
- Conversion back to voltage domain produces non-constant flux

#### Firing Rate Formulas

**LIF Neuron**:
- ν_LIF(t) = ρ_v0(ṽ(t)) · (-ṽ(t) + I)
- Ω(I) = [log(-v_reset + I) - log(v_thr + I)]^(-1)

**QIF Neuron**:
- ν_QIF(t) = ρ_v0(ṽ(t)) · (ṽ(t)² + I)
- Ω(I) = [arctan(v_thr/√I) - arctan(v_reset/√I)] / √I

### Flux Operator Invertibility
The flux operator R mapping initial densities to firing rates is **explicitly invertible**:
- Given desired firing rate ν(t) = z(t), recover initial density:
  ρ_v(ṽ) = z(t⁻¹(ṽ)) / (F(ṽ) + I)
- This enables inverse design: specify target dynamics, find required initial conditions

## Key Properties

### Captures Fast Fluctuations
- Predicts instantaneous firing rate fluctuations from initial density structure
- Handles unimodal and bimodal initial densities
- Works for both excitatory and inhibitory coupling (weak/intermediate strength)

### Limitations
- Accuracy decreases asymptotically (t → ∞) as system evolves toward synchronous/asynchronous states
- Violates F'(v) + Ī(t) > 0 condition for strong inhibitory coupling (periodic bursting)
- Cannot predict long-time density evolution from changing neuronal synchrony

### Extensions
- Single coupled population with time-varying input c(t)
- Two interacting populations with cross-coupling
- Generalizes beyond Ott-Antonsen Lorentzian assumption

## Activation Keywords
- transport mean field
- firing rate fluctuations
- Fokker-Planck neural dynamics
- population density approach
- LIF mean field theory
- QIF neuron dynamics
- neural mass model
- initial density effects
- flux operator invertibility
- 脉冲神经网络均值场
- 传输方程神经动力学

## Implementation Notes

1. **Transport Solution**: Use probability integral transform g(v) for phase domain mapping
2. **LIF vs QIF**: Choose neuron model based on problem (LIF for leaky dynamics, QIF for oscillatory analysis)
3. **Coupling Strength**: Theory valid for weak/intermediate coupling; strong coupling requires bifurcation analysis
4. **Initial Conditions**: Initial voltage density critically determines fluctuation pattern

## Related Work
- Traditional mean field: Assumes asynchronous steady state (Abbott & Van Vreeswijk 1993)
- Ott-Antonsen: Requires Lorentzian heterogeneity assumption (Ott & Antonsen 2008)
- Modern neural mass: Heterogeneous networks (Montbrió, Pazó, Roxin 2015-2025)
- This work: Transport-based, no distribution assumption, handles fast fluctuations
