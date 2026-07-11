---
name: dynamic-neural-manifolds-snn-control
description: "Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware. Spiking ring networks with control knobs (gain, inhibition, transient currents) that steer low-dimensional manifold geometry for explainable autonomous behavior. Implemented on SpiNNaker 2 chip. Activation: neural manifolds, neuromorphic control, SpiNNaker, ring network, subspace rotation, explainable SNN, closed-loop control, dynamic manifolds."
tags: [neuroscience, neuromorphic, SNN, control, manifolds, SpiNNaker, explainable-AI]
version: 1.0.0
author: agent
date: 2026-07-12
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

**arXiv: [2607.07373](https://arxiv.org/abs/2607.07373v1)** | cs.NE | von Seeler, Tetzlaff, Lehr (Göttingen)

## Overview

Biological circuits evolve sequential neural activity along dynamic, low-dimensional manifolds to enable flexible behavior. This paper presents a framework for implementing **dynamic neural manifolds on the SpiNNaker 2 neuromorphic chip** for real-time, closed-loop control, establishing an explainable approach to neuromorphic engineering.

## Core Methodology

### Ring Network Architecture
- **Canonical oscillatory sequences** modeled as a bump of activity moving along a ring of neurons
- **Asymmetric recurrent connectivity** leads to stable bump progression → oscillatory sequences
- **Circulant weight matrix** with configurable sparsity (e.g., 50%) for efficiency
- Maps to observed oscillatory sequences across brain regions (spinal cord, MEC, motor cortex)

### Three Control Knobs
1. **Trajectory Shape (Additive current I)**: Controls bump size → trajectory radius in state space
   - Excitatory current (I>0) increases bump size and radius
   - Maps to spatial extent of neural representation

2. **Trajectory Speed (Multiplicative gain S)**: Controls how fast bump travels around ring
   - Gain amplifies inputs → faster sequence progression
   - Maps to velocity/timing of neural trajectories

3. **Subspace Rotation (Heterogeneous inhibition p_inh)**: Selective silencing of neuron subsets
   - Inhibitory ensembles silence random subsets of neurons
   - Switching ensembles rotates neural subspace → enables behavior switching
   - Angle between orientations: arccos(1 - p_inh)
   - Each subspace encodes a different behavior/motor output

### SpiNNaker 2 Implementation
- **Spike-based communication**: Rates → probabilistic spikes for neuron-to-neuron communication
- **Sparse connectivity**: Reduces computation (e.g., 20-50% sparsity with weight scaling 1/p)
- **Circulant structure**: Store single row + bitmask → saves memory
- **Streaming control**: Control parameters streamed in during runtime (no pre-specified sequences)
- **Closed-loop latency**: As low as 3 time steps (~3ms) from spike to control update

### Key Equations
```
x_i(t+1) = Σ_j W_ji * r_j(t) + I(t)
r_i(t+1) = F(r_i(t) + 1/τ * (-r_i(t) + p_i(t) * S(t) * x_i(t+1)))
```
where W is circulant, p_i indicates active (non-inhibited) neurons, S is speed control, I is shape control.

### Motor Readout
- Linear readout weights learned from ring network spike activity
- Spike smoothing via exponential moving average: s̄_i(t) = (1-α)s_i(t) + α·s̄_i(t-1)
- Motor speeds and actions decoded as: y_x = (s̄_1, ..., s̄_n, 1) · w_x

## Applications

### Robotic Navigation
- 2-wheeled robot navigating maze with sensory feedback
- Three subspaces: move forward, turn in place, jump
- Sensory inputs modulate control parameters → dynamic manifold reconfiguration
- High-level plan + local adaptation → integrated manifold representation

### Biological Research
- Computational testbed for investigating biological neural dynamics
- Validates theoretical predictions from Lehr et al. (2024, 2025) on subspace rotations
- Bridge between circuit mechanisms and geometric manifold properties

## Key Findings
1. Dynamic manifold control **works robustly on neuromorphic hardware**
2. Runtime scales **linearly with spike count** → efficient for sparse activity
3. All three control mechanisms (shape, speed, rotation) **reproduce theoretical predictions**
4. Subspace rotations enable **behavioral switching** with predictable geometry
5. Framework provides **mathematically interpretable** internal states → explainable AI

## Pitfalls
- **SRAM memory constraint**: Recording rates fills 128KB SRAM quickly; use streaming instead
- **Memory limits simulation time**: Streaming control parameters avoids pre-specified sequences
- **Weight precision**: 8-bit integers with shared exponent; precision loss for large networks
- **Latency budget**: Must complete all updates within 1ms time step on each PE

## Related Skills
- `snn-learning-survey` - SNN learning rules
- `spiking-neural-network-analysis` - SNN paper analysis
- `spiking-oscillation-mapping` - Oscillatory states in balanced SNNs
