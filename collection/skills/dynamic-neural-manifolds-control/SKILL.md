---
name: dynamic-neural-manifolds-control
description: "Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware. Uses SpiNNaker 2 chip to implement spiking networks where sensory inputs modulate heterogeneous inhibition, gain, and transient currents, driving rapid subspace rotations for behavior switching and fine-grained trajectory control. Validated on robotic maze navigation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [dynamic-neural-manifolds, neuromorphic-hardware, spinnaker2, closed-loop-control, spiking-network, sequential-neural-activity, subspace-rotation, robotic-navigation, neural-computation]
    category: ai_collection/collection/skills
    arxiv_id: "2607.07373"
    arxiv_url: "https://arxiv.org/abs/2607.07373"
    published: "2026-07-08"
    authors: ["Oskar von Seeler", "Christian Tetzlaff", "Andrew Lehr"]
    categories: ["cs.NE"]
    trigger_words: ["dynamic neural manifolds", "neural manifold", "SpiNNaker 2", "closed-loop control", "neuromorphic", "subspace rotation", "sequential neural activity", "manifold geometry", "robotic navigation", "behavior switching"]
created: "2026-07-13"
updated: "2026-07-13"
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

**arXiv**: 2607.07373 | **Published**: 2026-07-08 | **Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew Lehr

## Core Innovation

Extends **dynamic neural manifold** framework from biological spiking networks to **neuromorphic engineering** by implementing on the **SpiNNaker 2 chip** for real-time, closed-loop control. The key insight: sequential neural activity in biological circuits evolves along dynamic, low-dimensional manifolds, and by making these manifolds **parameterizable through circuit mechanisms**, they become an explainable framework for neural computation.

## Key Concepts

### Dynamic Neural Manifolds

In biological circuits:
- Sequential neural activity evolves along **low-dimensional manifolds**
- Manifold geometry determines computational capabilities
- Specific circuit mechanisms link activity patterns to manifold features

### Neuromorphic Implementation

The architecture allows **sensory inputs** to modulate three aspects:
1. **Heterogeneous inhibition**: Varying inhibitory strength across the network
2. **Gain**: Scaling neural responsiveness
3. **Transient currents**: Short-duration current injections

These modulations enable:
- **Rapid subspace rotations** → switch between behaviors
- **Fine-grained trajectory control** within subspaces → precise behavior modulation

## Validation: Robotic Maze Navigation

- Agent uses **sensory feedback** to dynamically reconfigure its manifold geometry
- Navigates through a maze by switching between behavioral modes
- Demonstrates feasibility of manifold-based control on real neuromorphic hardware

## Practical Applications

### 1. Explainable Neuromorphic Architectures
- Dynamic manifolds provide interpretable computational substrate
- Each behavior corresponds to a specific manifold configuration
- Transitions between behaviors are explicit subspace rotations

### 2. Biological Neural Dynamics Investigation
- Same architecture serves as testbed for biological hypotheses
- Can test how circuit parameters affect manifold geometry
- Bridges theoretical neuroscience and neuromorphic engineering

### 3. Real-Time Closed-Loop Control
- SpiNNaker 2 enables real-time processing
- Suitable for robotics, prosthetics, and adaptive systems
- Low power consumption vs. GPU-based approaches

### 4. Behavior Switching Mechanisms
- Subspace rotation as a general mechanism for behavioral flexibility
- Applicable to any system requiring rapid mode switching
- Biologically inspired alternative to traditional control theory

## Key Insight

**Manifold geometry is computable**: By linking specific circuit mechanisms (inhibition patterns, gain modulation, transient currents) to manifold geometry, dynamic neural manifolds become not just a descriptive tool but a **parameterizable control substrate** — you can design the manifold you need by configuring the circuit.

## Trigger Words

dynamic neural manifolds, neural manifold, SpiNNaker 2, closed-loop control, neuromorphic, subspace rotation, sequential neural activity, manifold geometry, robotic navigation, behavior switching, heterogeneous inhibition, gain modulation, transient currents
