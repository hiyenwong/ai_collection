---
name: spiking-tolman-eichenbaum-machine
description: "Spiking Tolman-Eichenbaum Machine (sTEM) — biologically realistic spiking neural network implementation of the TEM framework for spatial navigation and memory. Combines grid-place cell dynamics, sequence learning, and hippocampal-entorhinal circuit modeling with spiking neurons. Use when building spiking models of spatial cognition, hippocampal memory systems, grid-place cell interactions, or neuro-inspired navigation in robotics."
activation_keywords:
  - spiking tolman-eichenbaum
  - sTEM model
  - spiking spatial navigation
  - hippocampal entorhinal spiking
  - grid place cell spiking
  - spiking cognitive map
  - neuro-inspired navigation SNN
  - spatial memory spiking neural network
tags:
  - spiking-neural-network
  - spatial-navigation
  - hippocampal-modeling
  - cognitive-map
  - grid-cells
  - place-cells
  - entorhinal-cortex
  - memory
  - neuromorphic-robotics
---

# Spiking Tolman-Eichenbaum Machine (sTEM)

## Description

Biologically realistic spiking neural network implementation of the Tolman-Eichenbaum Machine (TEM) framework. The TEM is a unified generative model explaining the emergence of grid cells and place cells from spatial navigation. The spiking version (sTEM) adds biologically realistic temporal dynamics, spike-timing dependent plasticity, and event-based processing for neuromorphic deployment.

Based on crossref:2025.10.16.682754 "The Spiking Tolman-Eichenbaum Machine: Emergent Spatial and Temporal Coding through Spiking Network Dynamics."

## Core Concepts

### Tolman-Eichenbaum Machine (TEM)

A generative model of the hippocampal-entorhinal system that:
- **Grid cells** (entorhinal cortex): hexagonal firing fields providing metric spatial representation
- **Place cells** (hippocampus): localized firing fields representing specific locations
- **Generative inference**: jointly infers position and environmental layout from sensory input
- **Predictive coding**: predicts future sensory input based on current position estimate

### Spiking Extensions

| TEM Component | Spiking Implementation |
|---|---|
| Grid cell population | Leaky Integrate-and-Fire (LIF) neurons with ring attractor connectivity |
| Place cell population | LIF neurons with competitive dynamics and Hebbian plasticity |
| Sensory input | Event-based encoding (spike trains from continuous signals) |
| Path integration | Spike-timing dependent integration of velocity signals |
| Memory replay | Spatiotemporal replay sequences during rest/sleep phases |

## Mathematical Framework

### Grid Cell Formation

Grid cells emerge from continuous attractor dynamics on a 2D toroidal manifold:

```
dv_i/dt = -v_i/τ + Σ_j W_ij · spike_j(t) + I_vel(t) + I_noise(t)
```

Where:
- `W_ij`: Mexican-hat connectivity (local excitation, distant inhibition)
- `I_vel(t)`: Velocity-driven input that translates the activity bump
- The bump position on the torus encodes the animal's estimated position

### Place Cell Learning

Place cells learn through spike-timing dependent plasticity (STDP):

```
Δw_ij = η · (pre_spike_time - post_spike_time) · exp(-|Δt|/τ_stdp)
```

Place fields emerge as associations between grid cell activity patterns and sensory inputs.

### Temporal Coding

The spiking TEM naturally encodes temporal information through:
1. **Spike latency coding**: Earlier spikes = stronger stimulus
2. **Phase precession**: Place cell spikes advance relative to theta rhythm as animal traverses field
3. **Sequence learning**: STDP encodes temporal order of visited locations

## Usage Patterns

### Pattern 1: Spatial Navigation Model
Build a spiking neural network model of hippocampal-entorhinal spatial navigation:
1. Define grid cell population with toroidal attractor connectivity
2. Define place cell population with competitive dynamics
3. Implement velocity integration via bump translation
4. Add STDP for place cell learning from grid input + sensory signals
5. Train by simulating random walk trajectories

### Pattern 2: Memory Replay System
Implement hippocampal replay of learned trajectories:
1. After exploration phase, replay sequences during rest
2. Use spontaneous activity in grid cell attractor to generate trajectories
3. Place cells fire in sequence corresponding to learned paths
4. STDP strengthens or consolidates spatial memories

### Pattern 3: Neuromorphic Robot Navigation
Deploy sTEM on neuromorphic hardware (Loihi, SpiNNaker) for robot navigation:
1. Map grid/place cell populations to neuromorphic cores
2. Use event-based sensors (DVS camera) for sensory input
3. Implement velocity integration from wheel encoders/IMU
4. Real-time spatial mapping and localization

## Key Parameters

| Parameter | Description | Typical Value |
|---|---|---|
| Grid cell population size | Number of grid cells | 100-1000 |
| Place cell population size | Number of place cells | 100-500 |
| τ_membrane | LIF membrane time constant | 20ms |
| τ_stdp | STDP time window | 20-50ms |
| Grid spacing | Distance between grid field peaks | Environment-dependent |
| Grid orientation | Angle of hexagonal grid axes | Random per module |

## Error Handling

### Grid Cells Don't Form Hexagonal Patterns
- Check Mexican-hat connectivity weights (excitation/inhibition ratio)
- Verify velocity input is properly integrated (not too strong/weak)
- Add appropriate noise level for stochastic resonance

### Place Cells Don't Localize
- Ensure STDP learning rate is in correct range
- Verify grid-to-place connectivity is sparse enough
- Check that competitive dynamics (winner-take-all) is active

### Replay Sequences Are Disordered
- Verify STDP window matches temporal scale of exploration
- Ensure proper theta oscillation modulation
- Check that place cell inhibition creates sequential firing

## Related Skills

- **snn-sequence-timing-replay**: Spiking temporal memory for sequence learning
- **learning-sequence-timing-replay-speed-snn**: Replay speed control in SNNs
- **transport-mean-field-snn-dynamics**: Mean field theory for SNN population dynamics
- **energy-based-neurocomputation**: Energy-based frameworks including equilibrium propagation
- **three-layer-quantum-brain**: Quantum brain modeling (alternative computational approach)
- **hippocampal-entorhinal-world-model**: Non-spiking world model using HPC-MEC

## Resources

- Original TEM paper: Whittington et al., "The Tolman-Eichenbaum Machine"
- Spiking TEM: crossref:2025.10.16.682754
- Grid cell attractor models: Burak & Fiete (2009)
- STDP review: Caporale & Dan (2008)
