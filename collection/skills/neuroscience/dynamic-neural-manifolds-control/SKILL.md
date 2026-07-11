---
name: dynamic-neural-manifolds-control
description: "Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware. Uses sensory inputs to modulate heterogeneous inhibition, gain, and transient currents, driving rapid subspace rotations to switch between behaviors and fine-grained trajectory control within them."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuroscience, neuromorphic, dynamic-manifolds, closed-loop-control, spiking-neural-networks, spinnaker2, robotic-navigation, explainable-ai]
    category: ai_collection
    arxiv_id: "2607.07373"
    arxiv_url: "https://arxiv.org/abs/2607.07373"
    published: "2026-07-08"
    authors: ["Oskar von Seeler", "Christian Tetzlaff", "Andrew Lehr"]
    categories: ["cs.NE"]
    trigger_words: ["dynamic neural manifolds", "closed-loop control", "neuromorphic hardware", "spinnaker", "subspace rotation", "manifold geometry", "behavior switching", "trajectory control", "spiking network", "heterogeneous inhibition"]
created: "2026-07-12"
updated: "2026-07-12"
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

**arXiv**: 2607.07373 | **Published**: 2026-07-08 | **Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew Lehr

## Core Thesis

Sequential neural activity in biological circuits evolves along **dynamic, low-dimensional manifolds** to enable flexible behavior. This paper extends the dynamic neural manifold framework to **neuromorphic engineering**, implementing it on the **SpiNNaker 2 chip** for real-time, closed-loop control.

By allowing sensory inputs to modulate **heterogeneous inhibition**, **gain**, and **transient currents**, the architecture drives:
1. **Rapid subspace rotations** to switch between behaviors
2. **Fine-grained trajectory control** within subspaces

## Key Concepts

### Dynamic Neural Manifolds

- Biological neural activity doesn't explore the full high-dimensional state space; it evolves along **low-dimensional manifolds**
- These manifolds are **dynamic** — they can be reshaped by external inputs
- Specific circuit mechanisms link manifold geometry to computational function

### Sensory Modulation Mechanisms

Three types of sensory input modulation enable manifold control:

1. **Heterogeneous inhibition**: Different neurons receive different levels of inhibitory input, reshaping the manifold's curvature
2. **Gain modulation**: Multiplicative scaling of neuronal responses changes the manifold's scale and direction
3. **Transient currents**: Brief current injections cause rapid manifold rotations

### Subspace Rotations

When the agent needs to switch behaviors (e.g., from "explore" to "avoid"), sensory inputs trigger a rotation of the active subspace, redirecting the trajectory to a different behavioral attractor.

## Implementation on SpiNNaker 2

### Architecture

```
Sensory Input → [Inhibition Modulator, Gain Modulator, Transient Current Injector]
                    ↓
              Spiking Network (with dynamic manifold structure)
                    ↓
              Motor Output → Robotic Agent
                    ↓
              Sensory Feedback (closed loop)
```

### Key Design Decisions

- **Real-time operation**: SpiNNaker 2 enables real-time spike processing
- **Parameterizable manifolds**: Circuit mechanisms are explicitly tied to manifold geometry
- **Explainable**: Each circuit mechanism has a clear geometric interpretation

## Validation: Robotic Maze Navigation

The framework is validated via a robotic simulation where an agent:
1. Uses sensory feedback to dynamically reconfigure its manifold geometry
2. Switches between exploration and goal-directed navigation
3. Navigates through a maze using dynamically reconfigured trajectories

## Practical Applications

### 1. Neuromorphic Robotics

- Deploy spiking controllers on neuromorphic chips for autonomous robots
- Use manifold geometry as a debugging/analysis tool
- Design controllers by specifying desired manifold properties

### 2. Neuroscience Research

- Use the implementation as a testbed for hypotheses about biological neural dynamics
- Validate theories about how circuit mechanisms shape manifold geometry

### 3. Explainable Neuromorphic AI

- Unlike black-box neural controllers, manifold-based controllers are interpretable
- Each behavior corresponds to a specific manifold geometry
- Behavior switching corresponds to subspace rotations

## Implementation Guidelines

### Designing a Dynamic Manifold Controller

1. **Define the manifold**: Choose the low-dimensional subspace that encodes the behavior
2. **Specify circuit mechanisms**: Map each manifold property to a circuit parameter (inhibition, gain, transient currents)
3. **Design sensory modulation**: Determine how sensory inputs modulate each mechanism
4. **Implement on hardware**: Deploy on neuromorphic chip (SpiNNaker 2, Loihi, etc.)
5. **Validate closed-loop**: Test in simulation before hardware deployment

### Debugging with Manifold Geometry

- **PCA on spike trains**: Extract the low-dimensional manifold from recorded activity
- **Track rotations**: Monitor how the manifold rotates during behavior switches
- **Compare to target**: Check if the actual manifold matches the designed manifold

## References

- von Seeler, Tetzlaff, Lehr (2026) — Dynamic neural manifolds for flexible closed-loop control (this paper)

## Trigger Words

dynamic neural manifolds, closed-loop control, neuromorphic hardware, spinnaker, subspace rotation, manifold geometry, behavior switching, trajectory control, spiking network, heterogeneous inhibition
