---
name: soliton-waves-wstdp-snn
description: "Soliton-like wave propagation in recurrent spiking neural networks with weighted STDP. Use when studying cortical traveling waves, activity zone delimitation, spatial memory formation, or self-propagating neural activity patterns."
tags: [spiking-neural-networks, STDP, cortical-waves, soliton, recurrent-networks]
---

# Soliton-like Waves in Two-Dimensional Recurrent Spiking Neural Networks with Weighted STDP

**arXiv**: 2606.21432v1 (June 19, 2026)
**Authors**: Ch. Meessen
**Categories**: cs.NE, q-bio.NC

## Core Contribution

Demonstrates that recurrent spiking neural networks with weighted STDP spontaneously generate **stable, self-propagating wave packets** (dissipative solitons) that maintain spatial profiles, propagate at constant speed, and annihilate upon collision.

## Key Methodology

### 1. Minimal Biologically Plausible Neuron Model
Discrete-time spiking neuron combining:
- **Multiplicative STDP (WSTDP)**: Weight-dependent spike-timing-dependent plasticity
- **Divisive normalization**: Biologically plausible dendritic implementation using only local information
- **Homeostatic threshold adaptation**: Maintains stability
- **One-step refractory period**: Prevents immediate re-firing

### 2. Network Architecture
- Excitatory-inhibitory neuron pairs in 2D recurrent network
- Periodic localized stimulation
- Geometric asymmetry: inhibitory radius > excitatory radius
- Initial inhibitory synapses stronger than excitatory

### 3. Emergent Phenomena
- **Soliton formation**: Self-propagating wave packets with stable spatial profiles
- **Constant velocity propagation**: Waves travel at fixed speed
- **Collision annihilation**: Frontal collisions destroy waves
- **Direction learning**: WSTDP engraves propagation direction into synaptic weights
- **Boundary formation**: Simultaneous sources create semi-persistent boundaries encoding relative phase/frequency

## Key Findings

1. **Self-organizing propagation**: Network learns to sustain propagation in one direction while suppressing reverse propagation
2. **Phase encoding**: Boundary position between competing waves encodes relative phase and frequency of sources
3. **Local computation only**: Dendritic implementation requires only locally available information at each binary junction

## Implications

Provides minimal computational framework for studying:
- Cortical traveling waves
- Activity zone delimitation
- Spatial memory formation from local plasticity rules

## Activation Keywords
soliton waves, STDP, traveling waves, cortical dynamics, recurrent SNN, self-propagating activity, collision annihilation, spatial memory, divisive normalization

## Related Work
- Dissipative solitons in physics
- Cortical traveling waves in visual cortex
- STDP-based learning rules
- Recurrent neural network dynamics
