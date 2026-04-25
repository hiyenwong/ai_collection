---
name: dual-timescale-memory-astrocyte-network
description: "Spiking neuron-astrocyte network implementing dual-timescale memory: astrocytic calcium dynamics (slow, seconds-to-minutes) for long-term spatial memory and short-term synaptic depression (fast, ~hundreds of ms) for inhibition-of-return. Enables biologically plausible navigation without reward signals. Activation: astrocyte, spiking, neuron, dual-timescale, calcium, synaptic depression, heterosynaptic, navigation, spatial memory, SAN"
version: 1.0.0
author: Hermes Agent
source_paper: "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation"
paper_url: https://arxiv.org/abs/2604.15391
arxiv_id: 2604.15391v1
date: 2026-04-16
tags: [spiking-neural-networks, astrocyte, dual-timescale, calcium-dynamics, synaptic-depression, heterosynaptic-plasticity, spatial-memory, navigation, neuromorphic, biologically-plausible, tripartite-synapse]
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Networks

## Overview

Biological agents navigate complex environments by combining **long-term memory** of successful actions with **short-term suppression** of recently visited locations — a capability that remains difficult to replicate in artificial systems, especially under partial observability and without reward feedback.

This skill implements a **Spiking Neuron-Astrocyte Network (SAN)** that achieves dual-timescale memory through two complementary mechanisms:

- **Slow timescale (seconds–minutes):** Astrocytic calcium dynamics provide long-term potentiation traces that encode environmental structure and spatial regularities
- **Fast timescale (~hundreds of ms):** Short-term synaptic depression (STD) prevents immediate revisits to recently explored locations, implementing local inhibition-of-return

The astrocyte-mediated **heterosynaptic plasticity** enables the network to form spatial memory maps from spike-timing patterns alone, without explicit reward signals. Evaluated on maze navigation tasks, the SAN achieves **89% success rate on partially observable mazes** and **reduces path length by 43%** compared to standard SNNs.

## Core Concepts

### 1. Astrocytic Calcium Dynamics (Slow Timescale)

Astrocytes maintain an internal state driven by intracellular calcium (Ca²⁺) concentration that integrates presynaptic activity over extended windows:

- **Ca²⁺ accumulation:** Triggered by neurotransmitter spillover from presynaptic neurons binding to astrocytic receptors (e.g., mGluRs)
- **Timescale:** Seconds to minutes — orders of magnitude slower than neuronal spiking
- **Role:** Encodes environmental regularities and spatial structure as persistent traces
- **Output:** Gliotransmitter release rate is a monotonically increasing function of [Ca²⁺]
- **Memory function:** Long-term potentiation trace that captures which pathways have been successful

**Mathematical model (simplified):**
```
τ_ca · d[Ca²⁺]/dt = -[Ca²⁺] + Σ_j α_j · spike_j(t)
```
where τ_ca ≈ 1–10 s, α_j is the coupling strength from synapse j, and spike_j(t) is the presynaptic spike train.

### 2. Short-Term Synaptic Depression (Fast Timescale)

STD implements a fast, local form of inhibition-of-return at the synapse level:

- **Mechanism:** Repeated presynaptic activation depletes the readily-releasable pool of synaptic vesicles
- **Timescale:** ~100–500 ms recovery
- **Role:** Suppresses recently visited locations/paths, biasing exploration toward novel areas
- **Function:** Acts as a "working memory" of recently traversed routes
- **No external reward needed:** Emerges from local synaptic dynamics alone

**Mathematical model (Tsodyks-Markram style):**
```
τ_std · dx/dt = (1 - x) - u · x · spike(t)
```
where x ∈ [0,1] is the available resource fraction, τ_std ≈ 100–500 ms, and u is the utilization parameter. The effective synaptic weight becomes: `w_eff = w_base · x`.

### 3. Heterosynaptic Plasticity (Cross-Synapse Modulation)

Astrocytes enable heterosynaptic plasticity — modulation of one synapse based on activity at neighboring synapses:

- **Tripartite synapse architecture:** Each astrocyte contacts multiple synapses within its domain
- **Mechanism:** Elevated astrocytic Ca²⁺ triggers gliotransmitter release that affects all contacted synapses
- **Role:** Spreads learned spatial information across related pathways
- **Emergent behavior:** Formation of coherent spatial memory maps from local interactions
- **Key advantage:** Global-like coordination emerges from purely local rules

**Implementation pattern:**
```
For each astrocyte A with domain D = {synapse_k}:
    Ca_A(t) = Σ_{k∈D} coupling_k · presynaptic_activity_k(t)
    gliotransmitter_A(t) = f(Ca_A(t))  # monotonic function

    For each synapse k in D:
        w_eff_k = w_base_k · x_k · g(gliotransmitter_A(t))
        # x_k: STD state (fast), g: astrocytic modulation (slow)
```

## Implementation Pattern

### Architecture

```
Input Layer (sensory encoding)
    ↓ spikes
Hidden Layer (LIF/Izhikevich neurons)
    ├── Fast path: STD at each synapse (τ ≈ 100-500ms)
    └── Slow path: Astrocyte per neuron cluster (τ ≈ 1-10s)
    ↓ modulated spikes
Output Layer (action selection: turn left/right/move forward)
```

### Algorithm

```python
# At each simulation time step dt:

# 1. Encode sensory input as spike trains
spike_input = encode_sensory(observation)

# 2. Update neuronal membrane potentials (fast)
for neuron in neurons:
    V[neuron] += dt * (-V[neuron] + I_syn[neuron]) / tau_m
    if V[neuron] > threshold:
        spike[neuron] = 1
        V[neuron] = reset_potential

# 3. Update short-term synaptic depression (fast)
for synapse in synapses:
    x[synapse] += dt * ((1 - x[synapse]) / tau_std)
    if presynaptic_spike[synapse]:
        x[synapse] -= u * x[synapse]

# 4. Update astrocytic calcium dynamics (slow)
for astrocyte in astrocytes:
    Ca[astrocyte] += dt * (-Ca[astrocyte] / tau_ca)
    Ca[astrocyte] += coupling * sum(presynaptic_spikes_in_domain)

# 5. Compute heterosynaptic modulation
for synapse in synapses:
    astro = get_associated_astrocyte(synapse)
    modulation = gliotransmitter_release(Ca[astro])
    w_eff[synapse] = w_base[synapse] * x[synapse] * modulation

# 6. Propagate spikes through modulated synapses
# 7. Select action from output layer activity
# 8. Move agent, observe new state
```

### Parameter Guidelines

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| τ_ca (astrocyte time constant) | 1–10 s | Must be >> τ_m for timescale separation |
| τ_std (STD recovery) | 100–500 ms | Should match environment traversal speed |
| τ_m (membrane time constant) | 10–20 ms | Standard LIF parameter |
| Astrocyte coupling strength | 0.1–0.5 | Tunable; too high causes over-modulation |
| STD utilization (u) | 0.2–0.5 | Controls depth of depression |
| Neuron threshold | -50 to -40 mV | Standard LIF range |

## Activation Keywords

- astrocyte, spiking neuron, dual-timescale, calcium dynamics
- short-term synaptic depression, STD, inhibition-of-return
- heterosynaptic plasticity, tripartite synapse, gliotransmitter
- spatial memory, maze navigation, partial observability
- SAN, spiking neuron-astrocyte network
- neuromorphic navigation, biologically plausible memory
- topological-context memory, working memory SNN
- 星形胶质细胞, 双时间尺度, 突触抑制

## Applications

1. **Neuromorphic Robotics:** Energy-efficient navigation on neuromorphic hardware (e.g., Loihi, SpiNNaker) without reinforcement learning overhead
2. **Autonomous Exploration:** Robots that explore unknown environments with minimal computational resources and no reward signal
3. **Computational Neuroscience:** Modeling how glial-neuronal interactions support spatial cognition in biological systems
4. **Edge AI Navigation:** Deploying navigation-capable networks on resource-constrained embedded devices
5. **Memory-Augmented SNNs:** Adding persistent spatial memory to spiking networks that lack it natively
6. **SLAM Alternative:** Lightweight spatial mapping without maintaining explicit geometric maps

## Performance Benchmarks (from paper)

| Metric | SAN | Standard SNN | Improvement |
|--------|-----|-------------|-------------|
| Success rate (partial observability) | 89% | ~62% | +27 pp |
| Path length reduction | — | baseline | -43% |
| Exploration efficiency | 6× better median path | baseline | — |

## Related Skills

- `astrocyte-resource-diffusion-neural-fields` — Astrocyte modeling in neural field equations
- `dual-timescale-memory-astrocyte` — General dual-timescale framework for environment learning
- `snn-learning-rules-dynamics` — SNN learning rules and dynamics
- `tsodyks-markram-chaotic-dynamics` — Tsodyks-Markram synaptic dynamics model
- `atp-hysteresis-tripartite-synapse` — Tripartite synapse ATP mechanisms
- `ember-hybrid-snn-llm-architecture` — Hybrid SNN cognitive architectures

## References

- Tsybina, Y., Antonova, E., Shchanikov, S. et al. (2026). "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation." arXiv:2604.15391v1.
- Full paper: https://arxiv.org/abs/2604.15391
- Related: Tsodyks-Markram model of short-term synaptic plasticity
- Related: Tripartite synapse theory (Volterra & Meldolesi, 2009)
- Related: Astrocyte Ca²⁺ signaling and gliotransmission
