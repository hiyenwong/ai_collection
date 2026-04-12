# Dynamic Gated Neuron Spiking Neural Networks

## Overview
This skill implements the Dynamic Gated Neuron (DGN) model from the paper "A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks" (arXiv:2509.03281). The DGN introduces dynamic conductance as a biologically plausible gating mechanism that modulates information flow, enabling selective input filtering and adaptive noise suppression.

## Key Features
- **Dynamic Conductance**: Membrane conductance evolves in response to neuronal activity
- **Enhanced Stochastic Stability**: Superior robustness compared to standard LIF models
- **Noise Suppression**: Adaptive filtering of noisy inputs
- **Biological Plausibility**: Based on real neural mechanisms

## Implementation Details
The DGN model extends the traditional Leaky Integrate-and-Fire (LIF) neuron by incorporating dynamic conductance mechanisms that:
1. Act as a disturbance rejection mechanism
2. Provide selective input filtering capabilities  
3. Enable adaptive noise suppression
4. Maintain energy efficiency while improving robustness

## Applications
- Anti-noise tasks in spiking neural networks
- Temporal-related benchmarks (TIDIGITS, SHD)
- Robust spike-based computation
- Energy-efficient neuromorphic computing

## References
- arXiv:2509.03281 - "A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks"
- Related work: CMOS+X spiking neurons with magnetic tunnel junctions (arXiv:2604.03187)

## Usage
This skill can be used for implementing robust SNNs that require noise resilience and temporal processing capabilities. The dynamic gating mechanism provides theoretical guarantees of enhanced stochastic stability while maintaining biological plausibility.