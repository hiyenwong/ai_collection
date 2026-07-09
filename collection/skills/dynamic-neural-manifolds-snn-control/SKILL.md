---
name: dynamic-neural-manifolds-snn-control
description: "Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware. Biological sequential activity evolves along low-dimensional manifolds; SpiNNaker 2 implementation enables real-time subspace rotations for behavior switching."
tags: [neuroscience, spiking-neural-network, neuromorphic, neural-manifolds, closed-loop-control, spinnaker]
source: arXiv:2607.07373v1
date: 2026-07-08
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

## Paper Information
- **Title**: Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
- **Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew Lehr
- **arXiv**: 2607.07373v1
- **Date**: 2026-07-08
- **Categories**: cs.NE

## Core Methodology

### Key Insight
Biological circuits generate sequential neural activity that evolves along **dynamic, low-dimensional manifolds**. This geometric structure enables flexible behavior — the network can switch between behavioral modes by rotating the manifold subspace, and fine-tune trajectories within a mode.

### Architecture Design
The framework implements dynamic neural manifolds on **SpiNNaker 2** neuromorphic hardware for real-time closed-loop control:

1. **Manifold Parameterization**: Spiking network models link sequential activity to manifold geometry through specific circuit mechanisms:
   - Heterogeneous inhibition
   - Gain modulation
   - Transient currents

2. **Sensory-Driven Modulation**: Sensory inputs modulate circuit parameters to drive:
   - **Rapid subspace rotations** → switch between behavioral modes
   - **Fine-grained trajectory control** → adjust within a behavioral mode

3. **Closed-Loop Validation**: Robotic simulation where agent uses sensory feedback to dynamically reconfigure manifold geometry for maze navigation.

## Technical Framework

### Neural Manifold Theory
```
Neural Population Activity → Low-Dimensional Manifold
                            ↓
                    Manifold Geometry encodes:
                    - Sequential activity patterns
                    - Behavioral mode structure
                    - Transition dynamics
```

### Circuit Mechanisms for Manifold Control
| Mechanism | Effect on Manifold | Behavioral Role |
|-----------|-------------------|-----------------|
| Heterogeneous inhibition | Subspace rotation | Mode switching |
| Gain modulation | Trajectory scaling | Speed/amplitude control |
| Transient currents | Trajectory initiation | Movement onset |

### Neuromorphic Implementation (SpiNNaker 2)
- Real-time spiking computation
- Closed-loop sensorimotor integration
- Energy-efficient edge deployment
- Biologically plausible dynamics

## Key Results
- Demonstrated feasible real-time dynamic manifold control on neuromorphic hardware
- Sensory feedback enables dynamic reconfiguration of manifold geometry
- Agent successfully navigates maze using manifold-based control
- Establishes framework for **explainable neuromorphic control**

## Applications
1. **Neuromorphic Robotics**: Energy-efficient autonomous agents with explainable control
2. **Brain-Machine Interfaces**: Manifold-based decoding for flexible prosthetic control
3. **Neural Prosthetics**: Closed-loop stimulation guided by manifold dynamics
4. **Cognitive Neuroscience**: Testing theories of motor cortex manifold structure

## Implementation Notes
- Platform: SpiNNaker 2 neuromorphic chip
- Network type: Recurrent spiking neural network
- Control: Heterogeneous inhibition + gain + transient currents
- Task: Maze navigation with sensory feedback

## Related Concepts
- Neural population dynamics (Churchland et al.)
- Motor cortex manifolds (Gallego et al.)
- Neuromorphic computing (SpiNNaker architecture)
- Closed-loop brain-machine interfaces
- Dynamical systems approaches to neuroscience

## Activation Triggers
- neural manifolds, neural dynamics, low-dimensional dynamics
- neuromorphic control, SpiNNaker, closed-loop SNN
- motor cortex, population dynamics, subspace rotation
- explainable neuromorphic computing
- flexible behavior, behavior switching
