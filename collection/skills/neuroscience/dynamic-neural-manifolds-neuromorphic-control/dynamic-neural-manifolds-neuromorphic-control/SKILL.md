---
name: dynamic-neural-manifolds-neuromorphic-control
category: neuroscience
created: 2026-07-13
arxiv_id: "2607.07373"
description: Dynamic neural manifold architecture for flexible closed-loop control on neuromorphic hardware — mapping spiking activity to low-dimensional manifold trajectories with sensory-modulated geometry for explainable neural computation.
trigger_words:
  - dynamic neural manifolds
  - neuromorphic closed-loop control
  - SpiNNaker neural manifold
  - manifold geometry neural computation
  - subspace rotation behavior switching
  - explainable neuromorphic architecture
  - ring attractor manifold
  - bump attractor propagation
---

# Dynamic Neural Manifolds for Neuromorphic Closed-Loop Control

## Paper Reference

- **Title**: Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
- **Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew Lehr
- **Published**: 2026-07-08
- **arXiv**: [2607.07373](https://arxiv.org/abs/2607.07373)
- **Categories**: cs.NE

## Core Concept

Biological neural circuits organize sequential activity along **dynamic, low-dimensional manifolds** to enable flexible behavior. This paper extends the dynamic manifold framework from biological modeling to **neuromorphic engineering**, implementing it on the **SpiNNaker 2 chip** for real-time closed-loop control.

## Key Innovations

1. **Manifold-Based Neuromorphic Architecture**: Spiking networks implement dynamic neural manifolds where behavior is encoded as trajectories through low-dimensional subspaces, making neural computation **explainable** and **parameterizable**.

2. **Sensory-Modulated Manifold Geometry**: Three control channels enable flexible behavior:
   - **Heterogeneous inhibition** modulation — drives rapid subspace rotations
   - **Gain modulation** — controls trajectory speed and stability
   - **Transient current injection** — enables fine-grained trajectory control

3. **Real-Time Closed-Loop on SpiNNaker2**: First demonstration of dynamic manifold control on actual neuromorphic hardware with sensory feedback loops operating in real-time.

4. **Behavioral Switching via Subspace Rotation**: Sensory inputs can rapidly reconfigure manifold geometry, enabling the agent to switch between different behavioral modes.

## Methodology

### Manifold Parameterization
- Sequential neural activity is mapped to trajectories on a low-dimensional manifold
- Circuit mechanisms (inhibition patterns, gain, transient currents) are explicitly linked to manifold geometry features
- This makes the system **explainable**: you can read behavior from manifold shape

### Control Architecture
```
Sensory Input → Manifold Modulation → Spiking Activity → Motor Output
                    ↑                                        ↓
                    └────────── Feedback Loop ──────────────┘
```

1. **Sensory encoding** maps environmental state to manifold modulation parameters
2. **Manifold modulation** rotates subspaces and adjusts trajectory parameters
3. **Spiking dynamics** evolve along the reconfigured manifold
4. **Readout** extracts motor commands from population activity
5. **Closed-loop feedback** continuously updates manifold geometry

### Validation
- Robotic agent navigation through a maze
- Agent uses sensory feedback to dynamically reconfigure its manifold geometry
- Demonstrates both **behavioral switching** (subspace rotation) and **fine-grained control** (trajectory modulation)

## Implementation Patterns

### For Neuromorphic Systems
- Use **heterogeneous inhibitory connectivity** to enable subspace rotation
- Implement **gain modulation** as multiplicative scaling of neuronal inputs
- Add **transient current injection** for rapid state transitions
- Design readout layers that project population activity to behavior space

### For Biological Modeling
- Map circuit-level mechanisms (inhibition, gain, transients) to manifold geometry
- Use manifold analysis to understand how biological circuits achieve flexibility
- Validate by comparing simulated manifold trajectories to neural recordings

## Pitfalls

1. **Manifold Dimensionality**: Too low → insufficient expressivity; too high → loss of explainability. Must balance based on behavioral complexity.
2. **Temporal Scales**: Subspace rotations must be faster than within-manifold trajectory dynamics, otherwise the controller can't switch behaviors fast enough.
3. **Hardware Constraints**: SpiNNaker2 has limited precision for current injection; discretization effects can distort manifold geometry.
4. **Sensory Encoding Quality**: Poor sensory→manifold mapping leads to unstable closed-loop behavior.

## Applications

- **Neuromorphic robotics**: Real-time adaptive control on edge hardware
- **Brain-computer interfaces**: Explainable decoding of motor intentions
- **Neuroscience experiments**: Testable predictions about how manifold geometry relates to behavior
- **Explainable AI**: Understanding how neural circuits implement computation through geometric lens

## Related Skills
- `spiking-neural-network-analysis`
- `neuromorphic-artificial-consciousness`
- `brain-network-controllability`