---
name: spiking-neural-networks-elephant-reinforcement
description: Spiking Neural Networks with Elephant Reinforcement — finite stochastic SNN model where past firing activity modifies future excitability through reinforcement-dependent threshold. Use for modeling neuronal adaptation, extinction behavior, and mean-field dynamics.
trigger_words:
  - elephant reinforcement
  - spiking neural networks elephant
  - SNN elephant memory
  - reinforced spiking networks
  - elephant-type memory SNN
---

# Spiking Neural Networks with Elephant Reinforcement

## Overview
This skill implements the mathematical framework from arXiv:2608.12839 for finite stochastic spiking-neuron networks with Elephant-type memory. The model incorporates history-dependent neuronal excitability where past firing activity modifies future firing probabilities through a reinforcement-dependent threshold mechanism.

## Key Features
- **Elephant Memory Mechanism**: Each neuron carries three state variables:
  - Membrane potential `Vi`
  - Signed reinforcement variable `Si` 
  - Reinforcement counter `Ki`
- **Reinforcement Rule**: When neuron `i` fires, `(Si, Ki)` updates via Elephant-type rule
- **Threshold Modulation**: Firing threshold becomes `Vi > αSi+` where `Si+` is positive part
- **Persistence Control**: Parameter `p` controls memory behavior:
  - `p > 1/2`: favors persistence of previous reinforcement directions
  - `p < 1/2`: favors anti-persistence  
  - `p = 1/2`: memory-neutral reference case
- **Bounded Hard-Threshold**: Ensures mathematical tractability and non-explosion

## Mathematical Properties
- **Non-explosion**: Proven for finite system with bounded firing rate
- **Contraction**: Conditional exponential contraction in (1)-Wasserstein distance on truncated potential space
- **Mean-Field Dynamics**: Replica mean-field formulation with global existence and uniqueness in law
- **Invariant Measures**: Characterization of steady-state distributions

## Applications
- **Firing-rate adaptation** under sustained stimulation
- **Extinction behavior** analysis in neural populations
- **Finite-network dynamics** approximation via mean-field methods
- **Neuronal spike-frequency adaptation** modeling with power-law relaxation

## Implementation Guidelines
1. Initialize neurons with `Vi(0) = 0`, `Si(0) = Ki(0) = 1`
2. Set parameters: `N` (network size), `α` (threshold scaling), `γ` (decay rate), `p` (memory parameter)
3. For numerical experiments, use time windows of length `Δ = 5` for firing rate evaluation
4. Run simulations up to `Tmax = 300` with multiple independent runs (e.g., 50) for statistical reliability

## Numerical Results
- Elephant memory produces `p`-dependent decline in firing activity
- Alters extinction behavior compared to memory-neutral systems
- Finite-network dynamics closely matched by replica mean-field approximation
- Demonstrates biologically plausible spike-frequency adaptation

## References
- Najman, F. A., Papageorgiou, I., & da Silveirau, S. K. C. A. (2026). Spiking Neural Networks with Elephant Reinforcement. arXiv:2608.12839 [math.PR]
- Galves–Löcherbach framework for interacting spiking neurons
- Elephant random walk literature for reinforcement mechanisms

## Activation Keywords
Use this skill when working with:
- History-dependent neuronal models
- Spike-frequency adaptation mechanisms  
- Stochastic spiking network analysis
- Mean-field approximations for neural dynamics
- Reinforcement learning in biological neural networks
- Power-law relaxation in neuronal excitability