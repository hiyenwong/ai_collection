---
name: dynamic-neural-manifolds-neuromorphic-control
description: >
  Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware.
  Uses ring attractor networks with sensory-modulated control neurons (speed, shape, selection)
  to drive subspace rotations and fine-grained trajectory control in neural state space.
  Implemented on SpiNNaker 2 chip with robotic maze navigation validation.
version: 1.0.0
author: Hermes Agent (from arXiv:2607.07373v1)
license: MIT
metadata:
  hermes:
    tags: [neuromorphic, neural-manifolds, closed-loop-control, spiking-networks, spinnaker2, ring-attractor]
    trigger_words: [dynamic neural manifold, neuromorphic control, spinnaker 2, ring network,
      closed-loop spiking, subspace rotation, neural trajectory, manifold geometry,
      sequential neural activity, flexible behavior, activity bump, control neurons]
  paper:
    arxiv_id: "2607.07373v1"
    title: "Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware"
    authors: ["Oskar von Seeler", "Christian Tetzlaff", "Andrew B. Lehr"]
    published: "2026-07-08"
    categories: ["cs.NE"]
---

# Dynamic Neural Manifolds for Neuromorphic Closed-Loop Control

## Paper

- **Title**: Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
- **Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew B. Lehr
- **Affiliation**: University Medical Center Göttingen; Campus Institute Data Science, University of Göttingen; Circulant Labs
- **arXiv**: 2607.07373v1 [cs.NE] (2026-07-08)
- **License**: CC BY 4.0

## Core Concept

In biological circuits, sequential neural activity evolves along **dynamic, low-dimensional manifolds** to enable flexible behavior. This paper presents a framework that makes these manifolds **parameterizable through specific circuit mechanisms**, enabling explainable neuromorphic control on real hardware.

### Key Innovation

The architecture maps neural computation onto a **geometric manifold framework** where:
- Neural population activity = trajectory in N-dimensional state space
- Sequential activity = movement along low-dimensional curved manifold
- Control = modulation of manifold geometry (position, speed, shape) via simple neural mechanisms

## Architecture

### Ring Attractor Network

```
Input → Control Neurons → Ring Network → Readout → Motor Output
         (3 types)         (circulant)   neurons    (agent)
```

**Ring Network**: Circulant weight matrix with 50% connection sparsity (weights scaled 2x to compensate). Implements a ring attractor that produces a traveling "bump" of activity — a well-studied pattern in neuroscience (head direction cells, spatial navigation).

### Three Control Neuron Types

| Control Type | Function | Biological Analogy |
|---|---|---|
| **Speed control** | Modulates propagation speed of activity bump around ring | Neuromodulatory gain control |
| **Shape control** | Changes width of activity bump (narrow ↔ broad) | Heterogeneous inhibition tuning |
| **Selection control** | Selectively inhibits subsets of ring neurons | Targeted inhibitory interneurons |

These three simple mechanisms serve as "control knobs" that allow sensory feedback to:
1. **Switch behavioral states** (e.g., steering ↔ jumping) via subspace rotation
2. **Fine-tune trajectories** within a behavioral manifold via speed/shape modulation
3. **Redirect activity** to different readout pathways via selective inhibition

### Geometric Interpretation

The neural activity lives on a **low-dimensional manifold embedded in high-dimensional neural state space**. Control inputs cause:

- **Subspace rotation**: Changes which behavioral readout is active
- **Trajectory speed**: How fast the agent moves through the behavioral sequence
- **Bump width**: How many neurons are co-active (affects precision vs. robustness tradeoff)
- **Selective inhibition**: Redirects the activity bump to different ring sectors

## SpiNNaker 2 Implementation

- Ring network + readout neurons implemented **on-chip** on SpiNNaker 2
- Host interface communicates with external environment (robotic simulation)
- Real-time, closed-loop: sensory feedback → control neuron modulation → manifold reconfiguration → motor output
- **Energy-efficient, low-latency** compared to conventional deep learning approaches

### Implementation Details
- Circulant weight matrix structure enables efficient sparse connectivity
- Control neuron inputs modulate heterogeneous inhibition, gain, and transient currents
- Readout neurons decode manifold position into motor commands
- Agent navigates maze using environmental cues as real-time sensory feedback

## Why This Matters

1. **Explainability**: Both the predictable ring network activity and its geometric manifold interpretation make the system fully interpretable
2. **Neuroscientific validity**: Uses mechanisms observed in biological circuits (ring attractors, gain modulation, selective inhibition)
3. **Hardware feasibility**: Simple neural mechanisms readily implementable on neuromorphic chips
4. **Compositional design**: Provides a "building block" that can be combined with other neuromorphic components
5. **Bridge to biology**: Offers a computational testbed for studying how biological circuits translate spatiotemporal dynamics into behavior

## Application Patterns

### Closed-Loop Robotic Control
```
Sensory input → Control neurons → Ring attractor dynamics → Readout → Motor command
                                    ↑                           ↓
                              Manifold modulation          Agent behavior
                                    ↑                           ↓
                              Environmental feedback ← Environment state
```

### Behavioral State Switching
- Use **selection control** to inhibit different ring sectors → different behavioral readouts
- Example: one sector → forward motion, another sector → turn, another → stop

### Trajectory Modulation
- Use **speed control** to accelerate/decelerate behavioral sequences
- Use **shape control** to adjust precision (narrow bump = precise, broad bump = robust)

## Implementation Considerations

- **Circulant matrices**: Weights depend only on relative neuron position (w_ij = f(|i-j|))
- **50% sparsity**: Random pruning with 2x weight scaling to maintain dynamics
- **Control signal range**: Must be calibrated to avoid destabilizing the ring attractor
- **Readout training**: Downstream readout neurons need to learn the manifold-to-action mapping
- **SpiNNaker 2 mapping**: Each neuron → one core; spike-based communication via network-on-chip

## Related Work

- Ring attractor networks in neuroscience (head direction cells, spatial navigation)
- Neural manifold analysis in motor cortex (Churchland, Shenoy labs)
- Neuromorphic control architectures on Loihi, SpiNNaker, BrainScaleS
- Dynamic systems approaches to neural computation

## Trigger Words

dynamic neural manifold, neuromorphic control, spinnaker 2, ring attractor, ring network,
closed-loop spiking, subspace rotation, neural trajectory, manifold geometry,
sequential neural activity, flexible behavior, activity bump, control neurons,
circulant matrix, heterogeneous inhibition, gain modulation, transient currents,
behavioral state switching, explainable neuromorphic, low-dimensional manifold,
neural state space, readout neurons, motor control, embodied cognition
