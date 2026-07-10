---
name: dynamic-neural-manifolds-snn-control
category: ai_collection
description: 动态神经流形方法论用于神经形态硬件上的灵活闭环控制，实现可解释的脉冲网络行为切换。arXiv:2607.07373，2026-07-08 更新。
source: "arXiv:2607.07373"
arxiv_id: "2607.07373"
trigger_words:
  - dynamic neural manifolds
  - neuromorphic closed-loop control
  - manifold geometry switching
  - spinnaker2 implementation
  - spiking sequence generation
  - subspace rotation
  - trajectory control neuromorphic
created: "2026-07-11"
updated: "2026-07-11"
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

> **Paper**: von Seeler, O. et al. "Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware" — arXiv:2607.07373 [cs.NE], July 8, 2026

## Abstract Summary

In biological circuits, sequential neural activity evolves along dynamic, low-dimensional manifolds to enable flexible behavior. This paper presents spiking network models that link sequential activity to manifold geometry through specific circuit mechanisms, making dynamic neural manifolds parameterizable — offering an explainable framework for neural computation. Extending to neuromorphic engineering, they implement this on the **SpiNNaker 2 chip** for real-time, closed-loop control.

## Key Innovations

1. **Dynamic Manifold Parameterization**: Links spiking network sequential activity to manifold geometry features through specific circuit mechanisms, making manifolds *parameterizable* rather than learned end-to-end.

2. **Sensory-Modulated Architecture**: Sensory inputs modulate three distinct circuit parameters:
   - **Heterogeneous inhibition** — controls subspace structure
   - **Gain modulation** — controls trajectory speed
   - **Transient currents** — controls trajectory direction

3. **Subspace Rotation for Behavior Switching**: Rapid rotations in neural state space enable discrete behavior switching, while fine-grained trajectory control operates within each behavior manifold.

4. **SpiNNaker 2 Implementation**: First demonstration of dynamic neural manifold control on real neuromorphic hardware for closed-loop tasks.

## Technical Framework

### Circuit Mechanism → Manifold Geometry Mapping

```
Circuit Parameters → Neural Dynamics → Manifold Geometry → Behavior
  ├── Heterogeneous Inhibition → Subspace structure → Behavior type
  ├── Gain Modulation → Trajectory speed → Movement velocity  
  └── Transient Currents → Trajectory direction → Movement direction
```

### Mathematical Foundation

- Neural activity evolves in **low-dimensional state space**
- Sequential activity traces **parameterized trajectories** on manifolds
- Sensory feedback **modulates circuit parameters** → reshapes manifold geometry in real-time
- Behavior switching = **subspace rotation** in state space
- Trajectory control = **parameter tuning** within current manifold

## Experimental Validation

- **Task**: Robotic maze navigation using sensory feedback
- **Platform**: SpiNNaker 2 neuromorphic chip
- **Mechanism**: Agent dynamically reconfigures manifold geometry based on sensory input to navigate
- **Results**: Real-time closed-loop control with behavior switching and fine-grained trajectory modulation

## Relationship to Existing Work

| Concept | Prior Work | This Paper |
|---------|-----------|------------|
| Neural Manifolds | Analysis/observation tools | Parameterizable, controllable |
| Neuromorphic Control | Learned end-to-end | Explainable, circuit-level |
| SNN Behavior | Static/one behavior | Dynamic multi-behavior switching |
| Implementation | Simulation only | Real SpiNNaker 2 hardware |

## Applications

- **Neuromorphic robotics**: Explainable SNN controllers for autonomous agents
- **Neuroscience research**: Substrate for investigating biological neural dynamics
- **BCI**: Decoding intended behaviors from neural manifold trajectories
- **Adaptive control**: Real-time behavior switching based on environmental feedback

## Connection to Other Skills

- Related to `dynamic-neural-manifolds-neuromorphic` (same paper, different angle)
- Builds on `spiking-neural-network-analysis` for SNN mechanism understanding
- Complements `working-memory-heterogeneous-delays` for sequence generation in SNNs
- Related to `neuromorphic-fw mav-snn-control` for neuromorphic control systems

## Activation Keywords

dynamic neural manifolds, neuromorphic closed-loop control, manifold geometry switching, spinnaker2, spiking sequence generation, subspace rotation, trajectory control, explainable neuromorphic, flexible behavior switching, sensory-modulated SNN
