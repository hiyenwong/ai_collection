---
name: soliton-waves-wstdp-snn
description: "Soliton-like wave propagation in 2D recurrent SNNs with weighted STDP - minimal biologically plausible spiking model combining multiplicative STDP, divisive normalization, homeostatic threshold adaptation, and refractory period to produce self-propagating dissipative soliton waves, wave collision encoding, and spatial memory from local plasticity alone"
tags: [spiking-neural-network, soliton-waves, wave-propagation, spike-timing-dependent-plasticity, divisive-normalization, homeostatic-plasticity, cortical-traveling-waves, spatial-memory, local-plasticity, 2d-recurrent-network]
---

# Soliton-like Wave Propagation in 2D Recurrent SNNs with Weighted STDP

**arXiv:** 2606.21432  
**Authors:** Ch. Meessen  
**Published:** 2026-06-19  
**Categories:** cs.NE, q-bio.NC  

## Core Contribution

This paper constructs a **minimal but biologically plausible spiking neuron model** operating in discrete time that spontaneously generates **dissipative soliton waves** in a 2D recurrent network. The key finding: cortical traveling waves, activity zone delimitation, and spatial memory can emerge from **local plasticity rules alone**, without any engineered connectivity or global coordination.

## Model Architecture

### Single Neuron Model Components
The neuron model integrates four minimal mechanisms:

1. **Multiplicative Weighted STDP (WSTDP)**: Synaptic weights update multiplicatively based on spike timing correlations, with a geometric asymmetry requirement between excitatory and inhibitory connection radii
2. **Divisive Normalization**: Synaptic integration is normalized by total input, admitting a biologically plausible dendritic implementation where each binary junction uses only locally available information
3. **Homeostatic Threshold Adaptation**: Firing threshold adapts to maintain stable activity levels across the network
4. **One-Step Refractory Period**: Simple refractory mechanism preventing immediate re-firing

### Network Architecture
- **2D recurrent grid** of excitatory-inhibitory neuron pairs
- **Periodic localized stimulation** provides initial wave sources
- **Geometric asymmetry**: excitatory and inhibitory connection radii must differ
- **Initial condition**: inhibitory synapses stronger than excitatory ones

## Key Findings

### Dissipative Soliton Waves
The network spontaneously generates stable, self-propagating wave packets with soliton-like properties:
- **Stable spatial profile**: wave shape persists during propagation
- **Constant propagation speed**: waves travel at uniform velocity
- **Annihilation upon collision**: frontal collisions result in wave annihilation
- **Direction learning**: WSTDP engraves propagation direction into synaptic weights, so the network learns to sustain propagation in one direction while suppressing the reverse

### Wave Collision as Spatial Encoding
When two sources are active simultaneously:
- Waves annihilate upon collision
- The collision defines a **semi-persistent boundary**
- The boundary position **encodes the relative phase and frequency** of the two sources
- This provides a mechanism for **spatial memory** from purely local interactions

### Biological Plausibility
- Divisive normalization admits dendritic implementation with local information only
- Each binary junction operates independently
- No global coordination or engineered connectivity required
- Minimal model with only essential components

## Applications

- **Cortical traveling waves**: Understanding emergence of propagating waves in cortex
- **Activity zone delimitation**: Self-organizing spatial partitioning of neural activity
- **Spatial memory**: Wave collision boundaries as memory traces
- **Pattern separation**: Collision-based encoding of multiple input sources
- **Neuromorphic computing**: Self-organizing wave-based computation

## Mathematical Framework

### WSTDP Update Rule
```
Δw_ij = η * (pre_spike_i * post_spike_j - decay * w_ij)
```
Multiplicative update ensures weights remain bounded while preserving relative differences.

### Divisive Normalization
```
output_i = f(Σ_j w_ij * input_j / (σ + Σ_j |input_j|))
```
Local divisive normalization ensures stable dynamics across varying input strengths.

### Soliton Conditions
1. Geometric asymmetry: r_exc ≠ r_inh
2. Initial inhibitory dominance: w_inh(0) > w_exc(0)
3. Periodic stimulation: maintains wave energy
4. WSTDP learning: stabilizes propagation direction

## Comparison to Related Work

| Approach | Wave Generation | Plasticity | Spatial Memory | Biological Plausibility |
|----------|----------------|------------|----------------|-------------------------|
| Engineered CANNs | Pre-wired | None | Manual | Low |
| Rate-based models | Approximate | Global | Engineered | Medium |
| This work (WSTDP SNN) | Emergent | Local | Self-organized | High |

## Pitfalls

- **Geometric asymmetry requirement**: Must have different excitatory/inhibitory radii; symmetric networks don't produce solitons
- **Initial condition sensitivity**: Inhibitory synapses must start stronger than excitatory
- **Discrete time approximation**: Model operates in discrete timesteps; continuous-time behavior may differ
- **Stimulation protocol**: Requires periodic localized stimulation; spontaneous wave generation without stimulation not demonstrated
- **Scale limitations**: Demonstrated on 2D grids; 3D or irregular topologies may behave differently

## Activation Keywords

soliton waves, weighted STDP, WSTDP, divisive normalization, homeostatic threshold, cortical traveling waves, spatial memory, 2D recurrent SNN, wave propagation, wave collision, dissipative soliton, local plasticity, activity zone delimitation, pattern separation
