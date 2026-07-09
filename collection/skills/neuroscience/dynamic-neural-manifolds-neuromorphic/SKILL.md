---
name: dynamic-neural-manifolds-neuromorphic
description: Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware (SpiNNaker 2). Maps circuit mechanisms to manifold geometry for explainable autonomous behavior.
trigger_words:
  - neural manifold
  - dynamic manifold
  - neuromorphic control
  - SpiNNaker 2
  - subspace rotation
  - closed-loop control
  - bump attractor
  - ring network
categories:
  - neuroscience
  - neuromorphic
  - computational neuroscience
  - brain-inspired control
arxiv_id: "2607.07373v1"
date_added: "2026-07-10"
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

## Overview

This methodology implements **dynamic neural manifolds** on the SpiNNaker 2 neuromorphic chip for real-time, closed-loop control. The core insight is that biological sequential neural activity evolves along low-dimensional manifolds, and specific circuit mechanisms serve as "control knobs" for manifold geometry.

**Paper**: von Seeler, Tetzlaff & Lehr (2026). Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware. arXiv:2607.07373v1

## Core Architecture

### Ring Network with Control Mechanisms

The architecture uses a **ring network** (500 neurons, 20% connectivity) with asymmetric recurrent connections that generates a stable bump of activity propagating around the ring. Three control mechanisms modulate the manifold geometry:

1. **Shape Control (Additive Current I)**: Controls bump width → trajectory radius
   - Positive I → larger bump → larger trajectory radius
   - Negative I → smaller bump → smaller trajectory radius

2. **Speed Control (Multiplicative Gain S)**: Controls propagation speed → trajectory velocity
   - Higher S → faster bump propagation → faster neural trajectory
   - Maps directly to movement timing control

3. **Subspace Selection (Heterogeneous Inhibition p_inh)**: Controls manifold orientation
   - Random silencing of neuron subsets rotates the neural subspace
   - Angle between subspaces = arccos(1 - p_inh)
   - Enables switching between behavioral states (e.g., steering vs. jumping)

### Key Mathematical Relationships

```
Subspace rotation angle: θ = arccos(1 - p_inh)
Trajectory speed: v ∝ S (multiplicative gain)
Bump size: N_active ∝ I (additive current)
```

## Implementation on SpiNNaker 2

### Optimizations for Hardware

- **Spike-based communication**: Probabilistic rate-to-spike conversion reduces inter-chip communication
- **Circulant weight matrix**: Store single row + sparsity mask (50% sparsity) to save memory
- **Streaming architecture**: Control parameters streamed in, spikes streamed out (overcomes 128kB SRAM limit)
- **Real-time performance**: <1ms per timestep for 500 neurons, 20% connectivity

### Closed-Loop Control Architecture

```
[Sensory Input] → [Control Parameter Generator] → [SpiNNaker 2 Ring Network]
       ↑                                                        ↓
       └────────── [Motor Output / Action] ← [Readout Weights] ─┘
```

## Applications

### Maze Navigation (Proof of Concept)

- **Agent**: Two-wheeled robot with jump capability
- **Subspaces**: 3 subspaces (40% neurons each) for forward, turn, jump
- **Training**: Random exploration → learn readout weights from spikes to motor controls
- **Execution**: High-level plan + sensory feedback → dynamic manifold reconfiguration

### Key Results

- Successfully navigates virtual maze using sensory feedback
- Subspace rotations enable behavioral switching
- Speed/shape control enables fine-grained trajectory adjustment
- Runtime scales linearly with spike count (efficient for sparse activity)

## Design Principles

1. **Explainability**: Circuit mechanisms → manifold geometry → behavior (full interpretability chain)
2. **Composability**: Control mechanisms are independent and combinable
3. **Biological Plausibility**: Based on observed neural dynamics across spinal cord, motor cortex, MEC
4. **Energy Efficiency**: Neuromorphic implementation enables low-power deployment

## Activation Triggers

Use this skill when working on:
- Neuromorphic computing and brain-inspired hardware
- Neural manifold analysis and dynamical systems
- Closed-loop control systems with biological inspiration
- Explainable AI architectures
- Bump attractor networks and sequential activity
- Subspace rotations and behavioral switching

## Related Concepts

- Ring attractors / bump attractors
- Principal component analysis of neural population activity
- Motor cortex dynamics and movement preparation
- SpiNNaker / neuromorphic engineering
- Low-dimensional neural manifolds
