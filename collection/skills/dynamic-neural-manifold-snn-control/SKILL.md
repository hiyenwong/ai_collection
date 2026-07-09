---
name: dynamic-neural-manifold-snn-control
description: Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware (SpiNNaker 2). Sensory-modulated heterogeneous inhibition drives subspace rotations for behavior switching.
tags: [neural-manifolds, neuromorphic-control, spiking-neural-network, closed-loop, SpiNNaker2, subspace-rotation, robotics]
arxiv_id: 2607.07373v1
date: 2026-07-08
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

## Core Innovation

**Key Insight**: Sequential neural activity evolves along low-dimensional dynamic manifolds in biological circuits. By allowing sensory inputs to modulate heterogeneous inhibition, gain, and transient currents, one can drive rapid subspace rotations to switch between behaviors and achieve fine-grained trajectory control within them — all on neuromorphic hardware in real-time.

**Problem Solved**: Bridging the gap between theoretical neural manifold analysis and practical neuromorphic control systems that need explainable, flexible behavior switching.

**Platform**: SpiNNaker 2 chip for real-time, closed-loop robotic control.

## Methodology

### Biological Foundation
- In biological circuits, sequential activity evolves along **low-dimensional manifolds**
- Manifold geometry links to circuit mechanisms (inhibition, gain, transients)
- This makes manifolds **parameterizable** and **explainable**

### Architecture
1. **Sensory Input Modulation** of:
   - Heterogeneous inhibition
   - Neural gain
   - Transient currents

2. **Subspace Rotations**: Rapid switching between behavioral manifolds
3. **Trajectory Control**: Fine-grained movement within a manifold
4. **Closed-Loop**: Sensory feedback dynamically reconfigures manifold geometry

### Hardware Implementation
- **Chip**: SpiNNaker 2
- **Real-time**: Closed-loop control at hardware speed
- **Validated**: Robotic maze navigation with sensory feedback

## Key Results

### Robotic Simulation
- Agent uses sensory feedback to **dynamically reconfigure** manifold geometry
- Navigates through maze using behavior switching via subspace rotations
- Establishes dynamic manifolds as feasible approach for:
  1. Explainable neuromorphic architectures
  2. Substrate for investigating biological neural dynamics

### Performance Characteristics
- Real-time operation on SpiNNaker 2
- Explainable behavior switching (not black-box)
- Biologically plausible dynamics
- Energy-efficient neuromorphic computation

## Technical Details

### Manifold Geometry Control
- **Heterogeneous inhibition**: Controls manifold curvature and dimensionality
- **Gain modulation**: Scales activity along manifold trajectories
- **Transient currents**: Drive rapid transitions between subspaces

### Subspace Rotation Mechanism
- Sensory inputs change the effective connectivity
- This rotates the low-dimensional subspace in which activity evolves
- Different sensory contexts → different subspaces → different behaviors
- Smooth transitions possible via gradual modulation

### Closed-Loop Architecture
```
Sensory Input → Manifold Modulation → Motor Output
      ↑                                    ↓
      └────── Environment Feedback ────────┘
```

## Applications

### Immediate Applications
1. **Robotics**: Adaptive behavior switching in autonomous agents
2. **BCI**: Explainable neural control with dynamic repertoire
3. **Neuroprosthetics**: Context-aware motor control
4. **Edge AI**: Real-time adaptive control on neuromorphic hardware

### Research Directions
1. **Multi-manifold learning**: Discover manifold repertoire from data
2. **Manifold composition**: Combine primitives for complex behaviors
3. **Transfer learning**: Reuse manifolds across tasks
4. **Biological validation**: Compare with recorded neural data

## Comparison with Existing Approaches

| Approach | Explainable | Real-time | Flexible | Biologically Plausible |
|----------|-------------|-----------|----------|----------------------|
| RL on neuromorphic | No | Yes | Limited | Medium |
| Central pattern generators | Partial | Yes | Limited | High |
| End-to-end SNN | No | Yes | Yes | Medium |
| **Dynamic Manifolds** | **Yes** | **Yes** | **Yes** | **High** |

## Theoretical Implications

### For Neuroscience
- Provides mechanistic link between circuit parameters and manifold geometry
- Explains how biological circuits achieve flexible behavior
- Connects inhibition/gain to computational geometry

### For Neuromorphic Engineering
- Establishes design principles for explainable neuromorphic controllers
- Shows SpiNNaker 2 can support sophisticated manifold-based computation
- Bridges neuroscience theory and engineering practice

## Limitations and Open Questions

1. **Scalability**: How many manifolds can be maintained simultaneously?
2. **Learning**: How are manifold parameters learned from experience?
3. **Generalization**: Can manifolds transfer across environments?
4. **Complexity**: Maze navigation is simple; complex tasks need validation

## Key Takeaways

1. **Manifolds are parameterizable** via circuit mechanisms (inhibition, gain, transients)
2. **Subspace rotations** enable rapid behavior switching
3. **SpiNNaker 2** supports real-time manifold-based control
4. **Explainability** comes from geometric interpretation of neural activity
5. **Biological plausibility** maintained while achieving engineering goals

## Activation Triggers
- neural manifolds
- subspace rotation
- neuromorphic control
- SpiNNaker
- closed-loop control
- behavior switching
- heterogeneous inhibition
- explainable SNN
- robotic navigation
- manifold geometry

## Related Skills
- [[dynamic-neural-manifolds-snn-control]]
- [[spiking-oscillation-mapping]]
- [[neuromorphic-oscillator-reservoir-computing]]
- [[spiking-free-energy-control]]
- [[working-memory-heterogeneous-delays]]
