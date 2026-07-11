---
name: dynamic-neural-manifolds-snn-control
description: Dynamic neural manifold methodology for neuromorphic closed-loop control using ring attractor networks with sensory-modulated subspace rotations. Implemented on SpiNNaker 2 for real-time embodied robotics.
tags:
  - neuromorphic-control
  - neural-manifolds
  - spiking-neural-networks
  - closed-loop-control
  - SpiNNaker
  - embodied-AI
---

## Overview

This methodology maps biological sequential neural activity onto low-dimensional manifolds and uses circuit-level "control knobs" to dynamically manipulate manifold geometry for flexible behavior. Implemented on the SpiNNaker 2 neuromorphic chip for real-time, closed-loop control of a robotic agent navigating a maze.

**Paper**: von Seeler, Tetzlaff, & Lehr (2026). "Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware." arXiv:2607.07373 [cs.NE].

## Core Concept

### Neural Manifolds as Control Substrate

Neural population activity is represented as a trajectory in N-dimensional state space (one dimension per neuron). Biological activity is constrained to low-dimensional manifolds that capture task latent variables. The geometry of these manifolds maps to behavioral execution:
- **Subspace rotations** → switching between movements/behaviors
- **Trajectory speed** → adapting movement timing
- **Trajectory shape** → modulating spatial extent

### Ring Attractor Network

A ring of neurons with asymmetric recurrent connectivity produces a stable "bump" of activity that propagates around the ring — a canonical object in computational neuroscience observed across:
- Rat spinal cord
- Drosophila larvae ganglia
- Turtle spinal cord
- Mouse medial entorhinal cortex (MEC)

## Three Control Parameters

The network exposes three distinct circuit mechanisms that function as "control knobs":

### 1. Trajectory Shape (Additive Current `I`)
- **Mechanism**: Additive excitatory/inhibitory current to the ring
- **Effect**: Changes the spatial extent/size of the activity bump
- **Geometric mapping**: Controls the **radius** of the neural trajectory
- **Implementation**: Gaussian-shaped additive current `I(t)` with amplitude `A`

### 2. Trajectory Speed (Multiplicative Gain `S`)
- **Mechanism**: Multiplicative gain modulation of neural responses
- **Effect**: Amplifies inputs → faster responses → faster sequence progression
- **Geometric mapping**: Controls **velocity** along the manifold trajectory
- **Implementation**: Gain factor `S` applied to recurrent connections
- **Note**: Behavior matches rate-based model until `S > 30` (marginal deviation on SpiNNaker 2)

### 3. Subspace Rotation (Random Silencing `p_inh`)
- **Mechanism**: Inhibitory ensembles silence random subsets of neurons
- **Effect**: Switches which neurons support the sequence while maintaining sequential dynamics
- **Geometric mapping**: Rotates the neural subspace by angle `θ = arccos(1 - p_inh)`
- **Implementation**: Each inhibitory ensemble silences fraction `p_inh ∈ [0,1]` of neurons
- **Application**: Each behavioral readout = neural trajectories traversing a unique manifold orientation

## SpiNNaker 2 Implementation

### Architecture Optimizations

1. **Spike-based communication**: Rate-based neurons converted to probabilistic spiking (rate = spike probability per timestep)
2. **Circulant weight matrix**: Stores single row + sparsity mask (1 bit per synapse) → 50% connection sparsity with 2× weight compensation
3. **Streaming I/O**: Control parameters streamed into chip during execution; spikes streamed to host for action decoding

### Hardware Constraints

- **Memory limit**: 128 kB SRAM per core
- **Recording limit**: 32 neurons' internal rates fill SRAM in ~1 second (1000 timesteps at 1ms)
- **Solution**: Stream parameters in, stream spikes out — no on-chip long-term storage

### Closed-Loop Pipeline

```
Environment → Agent (maze navigation) → Sensory cues
                    ↓                          ↑
              Host processor ← SPIP ← SpiNNaker 2 chip
                    ↓                          ↑
           Control parameters → SI interface → Ring network + readout
```

## Validation Results

### Parameter Response Validation

| Parameter | Effect | SpiNNaker 2 Match | CPU Model Match |
|---|---|---|---|
| Additive current `A` | Bump size / trajectory radius | ✅ Matches | ✅ Reference |
| Multiplicative gain `S` | Sequence speed | ✅ Matches (until S>30) | ✅ Reference |
| Silencing fraction `p_inh` | Subspace rotation angle `arccos(1-p_inh)` | ✅ Matches | ✅ Reference |

### Maze Navigation Demo

- Two-wheeled robotic agent navigates virtual maze
- Sensory feedback modulates inhibition, gain, transient currents in real-time
- Agent dynamically reconfigures manifold geometry to switch behaviors (steering vs. jumping)
- Fine-grained trajectory control within behavioral states

## Design Principles for Neuromorphic Engineering

1. **Explainable by construction**: Internal state is mathematically interpretable via manifold geometry
2. **Low-level → high-level mapping**: Circuit mechanisms → geometric features → behavioral primitives
3. **Energy efficient**: Spike-based communication on neuromorphic hardware
4. **Low latency**: Real-time closed-loop control without cloud dependency
5. **Biologically plausible**: Based on observed neural dynamics across species

## Implementation Guide

### Ring Network Setup

```python
# Network parameters
n_neurons = 32          # Neurons in ring
connectivity = "circulant"  # Weight matrix structure
sparsity = 0.5          # 50% connection sparsity

# Weight matrix: store single row + sparsity mask
# Weights scaled 2× to compensate for sparsity
```

### Control Interface

```python
# Three independent control channels
shape_control = A       # Additive current amplitude
speed_control = S       # Multiplicative gain (optimal range: S ≤ 30)
rotation_control = p_inh  # Fraction of neurons silenced [0, 1]

# Combined control for complex trajectories
# shape + speed + rotation can vary concurrently
```

### Subspace Rotation Calculation

```python
import numpy as np

# Angle between subspaces defined by two inhibitory ensembles
def subspace_angle(p_inh):
    """First principal angle between subspaces under silencing."""
    return np.arccos(1 - p_inh)

# Example: 4 inhibitory ensembles with p_inh = 0.3
# → rotation angle ≈ arccos(0.7) ≈ 0.795 rad ≈ 45.6°
```

## Applications

- **Embodied robotics**: Real-time adaptive control on neuromorphic hardware
- **Brain-computer interfaces**: Interpretable neural state decoding
- **Computational neuroscience**: Testbed for investigating biological neural dynamics
- **Autonomous systems**: Energy-efficient, low-latency behavior switching

## Biological Evidence

Sequential neural activity observed across diverse structures and species:
- **Rat spinal cord**: Calcium waves during locomotion
- **Drosophila larvae**: Ganglia oscillations (T3 to A8/9 segments)
- **Turtle spinal cord**: Cyclical motor patterns
- **Mouse MEC**: Theta-rhythmic sequences in entorhinal cortex

## Related Skills

- `spiking-neural-network-analysis` — General SNN paper analysis
- `neuromorphic-supremacy` — Hybrid astrocytic-spiking computing
- `spiking-free-energy-control` — SNN control via Free Energy Principle
- `clockless-neuromorphic-snn` — Asynchronous neuromorphic computing
- `neuromorphic-oscillator-reservoir-computing` — Parametrically-driven oscillator RC
