---
name: dynamic-neural-manifolds-snn-control
description: Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware — using circuit mechanisms (heterogeneous inhibition, gain modulation, transient currents) as control knobs for manifold geometry, enabling explainable, energy-efficient autonomous behavior. Implemented on SpiNNaker 2 chip with robotic maze navigation validation.
category: neuroscience
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control

## Overview

This skill implements the **dynamic neural manifold** framework from arXiv:2607.07373v1, which bridges biological neural dynamics with neuromorphic engineering for explainable closed-loop control. The core insight: neural activity in biological circuits evolves along dynamic, low-dimensional manifolds, and specific circuit mechanisms can serve as "control knobs" for manifold geometry.

**Key paper**: *Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware* (von Seeler, Tetzlaff, Lehr — 2026-07-08)

## Core Methodology

### Neural Manifold Framework

Population activity of N neurons is represented as a trajectory in N-dimensional state space, constrained to low-dimensional manifolds capturing latent task variables. Geometric features map to behavioral execution:
- **Subspace rotations**: switching between behaviors/movements
- **Trajectory speed**: adapting movement timing
- **Trajectory curvature**: controlling execution dynamics

### Circuit Control Knobs

Three circuit-level mechanisms provide geometric control:

1. **Heterogeneous Inhibition**: Facilitates subspace reorientation, allowing sequences to rotate into new hyperplanes to switch behavioral states.

2. **Gain Modulation**: Regulates sequence propagation speed, providing direct control over neural trajectory velocity.

3. **Transient Synaptic Currents**: Control trajectory curvature, enabling fine-grained adjustments during behavior execution.

### Ring Network Architecture

```
Control Neurons (speed, shape, selection)
         ↓
    Ring Network (circulant weight matrix, ~50% sparsity)
         ↓
    Downstream Readout Neurons
```

The ring network generates oscillatory sequential activity on low-dimensional manifolds. Control neurons modulate:
- Propagation speed around the ring
- Width of activity bump
- Activation sparsity

### Closed-Loop Implementation

Sensory inputs modulate circuit mechanisms in real-time:
- Environmental cues → heterogeneous inhibition → behavioral state switching
- Sensory feedback → gain modulation → trajectory adjustment
- Task demands → transient currents → execution timing

## Implementation Patterns

### SpiNNaker 2 Hardware Deployment

```python
# SpiNNaker 2 ring network implementation
# Ring network + readout on-chip, host interface for agent-environment interaction
# Energy-efficient, low-latency substrate for adaptive neuromorphic control

# Key mapping:
# - Circuit mechanisms → SpiNNaker neuron/synapse parameters
# - Sensory inputs → real-time neuromodulation signals
# - Readout → motor commands / action selection
```

### Robotic Navigation Agent

The validated application: two-wheeled robot navigating a maze using:
- Local environmental cues as sensory feedback
- Dynamic manifold reconfiguration for behavior switching (steering vs. jumping)
- Velocity and trajectory adjustment during task execution

## Biological Validation

The framework connects to observed biological phenomena:
- Rat spinal cord oscillatory sequences
- Drosophila larvae ganglia dynamics
- Turtle spinal cord patterns
- Mouse medial entorhinal cortex (MEC) sequences

All species show structured dynamic sequences on low-dimensional manifolds, supporting the universality of this computational principle.

## Key Advantages

1. **Explainability**: Internal state is mathematically interpretable — map circuit architecture to geometric features to behavior
2. **Energy Efficiency**: Neuromorphic hardware enables biological-level efficiency
3. **Flexibility**: Rapid subspace rotations switch behaviors; fine-grained trajectory control within behaviors
4. **Biological Plausibility**: Grounded in observed neural dynamics across species

## Pitfalls

- **Ring network requires circulant weight structure**: Non-circulant connectivity breaks the manifold geometry
- **Control neuron inputs must be properly scaled**: Unbounded inputs can destabilize the manifold
- **Hardware mapping needs calibration**: SpiNNaker 2 parameters don't map 1:1 to biological parameters
- **Readout layer must be designed for the specific task**: Generic decoders may not capture manifold-relevant features

## Activation Keywords

dynamic neural manifolds, neuromorphic control, SpiNNaker, closed-loop control, neural manifold, ring attractor, geometric neural computation, explainable neuromorphic, behavioral switching, subspace rotation, neural trajectory, oscillatory sequences, brain-inspired control
