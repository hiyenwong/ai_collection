---
name: soliton-waves-wstdp-snn
description: "Soliton-like Waves in 2D Recurrent Spiking Neural Networks with Weighted Spike-Timing-Dependent Plasticity (WSTDP). Minimal biologically plausible SNN model combining WSTDP, divisive normalization, homeostatic threshold adaptation. Demonstrates self-propagating wave packets as dissipative solitons. Activation: WSTDP, soliton waves, SNN, wave propagation, dendritic normalization, spiking network dynamics."
---

## Methodology Overview

Weighted Spike-Timing-Dependent Plasticity (WSTDP) + divisively normalized synaptic integration yields stable, self-propagating soliton-like wave packets in 2D recurrent spiking neural networks.

### Key Innovation Points

1. **Minimal Biologically Plausible SNN Model**
   - Discrete time operation
   - Multiplicative WSTDP: weight change proportional to current weight
   - Divisive normalization of synaptic integration
   - Homeostatic threshold adaptation
   - One-step refractory period

2. **Dendritic Implementation**
   - Binary junctions operate on locally available information
   - No global coordination needed
   - Divisive normalization via dendritic computation

3. **Dissipative Soliton Waves**
   - Stable spatial profile propagation
   - Constant speed wave packets
   - Self-propagating without external drive
   - Excitatory-inhibitory neuron pairs

4. **Two-Dimensional Network Dynamics**
   - Recurrent excitatory-inhibitory pairs
   - Periodic localized stimulation triggers waves
   - Wave collision and annihilation behavior

### Activation Keywords

- WSTDP, weighted STDP, spike-timing plasticity
- Soliton waves, dissipative solitons
- Wave propagation in neural networks
- Dendritic normalization, synaptic integration
- Homeostatic threshold adaptation
- Spiking neural network dynamics
- Recurrent SNN, 2D neural networks

### Technical Details

#### Neuron Model Components

```
Neuron model (discrete time):
- WSTDP: Δw = η * w * f(Δt) where f encodes spike timing
- Divisive normalization: I_syn = Σ(w_i * s_i) / Σ|w_i|
- Homeostatic threshold: θ → θ + α*(target_rate - actual_rate)
- Refractory: one-step silence after spike
```

#### Network Architecture

```
- 2D lattice of E-I neuron pairs
- Local recurrent connections
- Periodic localized stimulation at fixed positions
- Weighted connections with WSTDP plasticity
```

#### Wave Properties

```
Soliton characteristics:
- Stable spatial profile (shape preserved)
- Constant propagation velocity
- Self-sustained propagation
- Collision dynamics (annihilation/merger)
```

### Biological Plausibility

**Dendritic Normalization Mechanism**
- Each dendritic junction computes: output = input / Σ|inputs|
- Locally implementable without global signals
- Matches biological dendritic computation

**Homeostatic Mechanism**
- Threshold adapts to maintain target firing rate
- Prevents runaway excitation/inhibition
- Stable network dynamics

### Applications

1. **Neuromorphic Computing**
   - Wave-based computation paradigms
   - Local plasticity rules for hardware
   - Energy-efficient wave propagation

2. **Computational Neuroscience**
   - Understanding cortical wave dynamics
   - Soliton models for neural propagation
   - STDP variants with normalization

3. **Brain Dynamics Modeling**
   - Traveling waves in cortex
   - Synaptic normalization mechanisms
   - Homeostatic stability analysis

### Implementation Notes

- Use discrete-time simulation (not continuous)
- Implement divisive normalization at integration step
- WSTDP: multiplicative weight updates, not additive
- Monitor wave stability and propagation speed

### Key Equations

**WSTDP Rule**
```
Δw_ij = η * w_ij * exp(-(Δt/τ))
where Δt = t_j - t_i (pre-post timing)
```

**Normalized Synaptic Current**
```
I_syn = Σ(w_i * spike_i) / Σ|w_i|
```

**Homeostatic Threshold**
```
θ_i(t+1) = θ_i(t) + β(r_target - r_i(t))
```

### Experimental Observations

- Wave speed depends on WSTDP parameters
- Normalization prevents runaway weight growth
- Solitons emerge spontaneously under stimulation
- E-I balance crucial for wave stability

### Related Skills

- stdp-spiking-transformer-attention
- spiking-oscillation-mapping
- adaptive-spiking-neuron-asn
- spiking-transformer-unification

### Source

arXiv:2606.21432 - "Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity"
Author: Ch. Meessen
Published: 2026-06-19
Link: http://arxiv.org/abs/2606.21432v1