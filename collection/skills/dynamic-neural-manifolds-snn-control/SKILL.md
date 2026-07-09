---
name: dynamic-neural-manifolds-snn-control
description: "Dynamic neural manifold methodology for flexible closed-loop control on neuromorphic hardware. Implements biologically-inspired sequential neural activity along low-dimensional manifolds using SpiNNaker 2 chip for real-time robotic control. Activation: neural manifold, neuromorphic control, closed-loop, spiking network, subspace rotation, SpiNNaker, robotic navigation, manifold geometry"
metadata:
  arxiv_id: "2607.07373"
  published: "2026-07-08"
  authors: "Oskar von Seeler, Christian Tetzlaff, Andrew Lehr"
  tags: [neural manifold, neuromorphic computing, closed-loop control, spiking neural network, SpiNNaker 2, robotic control]
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

## Core Concept

Biological circuits generate sequential neural activity along dynamic, low-dimensional manifolds that enable flexible behavior. This methodology extends the neural manifold framework to neuromorphic engineering, implementing parameterizable dynamic manifolds on the SpiNNaker 2 chip for real-time closed-loop control.

## Key Innovations

### 1. Dynamic Neural Manifold Parameterization
- Sequential activity evolves along low-dimensional manifolds in biological circuits
- Spiking network models link sequential activity to manifold geometry through circuit mechanisms
- Manifolds become parameterizable, providing an explainable framework for neural computation

### 2. Neuromorphic Implementation (SpiNNaker 2)
- Real-time closed-loop control on neuromorphic hardware
- Sensory inputs modulate:
  - **Heterogeneous inhibition** - controls subspace rotations
  - **Gain modulation** - adjusts trajectory speed
  - **Transient currents** - enables fine-grained trajectory control

### 3. Behavioral Switching via Subspace Rotations
- Rapid subspace rotations switch between behavioral modes
- Sensory feedback dynamically reconfigures manifold geometry
- Enables flexible navigation and decision-making

## Methodology

### Architecture Design
1. Define low-dimensional manifold structure for target behavior
2. Implement spiking network with heterogeneous inhibition, gain, and transient current mechanisms
3. Map sensory inputs to manifold control parameters
4. Deploy on SpiNNaker 2 for real-time execution

### Control Mechanisms
- **Subspace rotation**: Switch between behavioral modes (e.g., navigate left vs. right)
- **Trajectory control**: Fine-grained movement within a behavioral mode
- **Sensory modulation**: Real-time adaptation based on environmental feedback

### Validation
Robotic simulation demonstrates:
- Agent uses sensory feedback to navigate maze
- Dynamic reconfiguration of manifold geometry
- Real-time closed-loop control on neuromorphic hardware

## Applications

### Neuromorphic Robotics
- Real-time robotic control with explainable neural dynamics
- Energy-efficient closed-loop systems
- Adaptive navigation in dynamic environments

### Neuroscience Research
- Substrate for investigating biological neural dynamics
- Test hypotheses about manifold geometry and behavior
- Bridge between neural computation and motor control

### Brain-Computer Interfaces
- Low-latency neural decoding
- Flexible control strategies
- Biologically-plausible neural interfaces

## Implementation Considerations

### SpiNNaker 2 Specifics
- Leverage heterogeneous inhibition for subspace control
- Use gain modulation for trajectory scaling
- Implement transient currents for rapid state transitions

### Pitfalls
- **Manifold dimensionality**: Too high → loss of explainability; too low → insufficient behavioral flexibility
- **Sensory latency**: Real-time control requires low-latency sensory feedback loops
- **Parameter tuning**: Manifold geometry parameters require careful calibration for stable dynamics

## Related Work

- Neural manifold analysis in motor cortex
- Reservoir computing on neuromorphic hardware
- Biologically-plausible learning rules for spiking networks

## References

- Paper: arXiv:2607.07373 (July 8, 2026)
- SpiNNaker 2 neuromorphic platform
- Neural manifold theory in computational neuroscience
