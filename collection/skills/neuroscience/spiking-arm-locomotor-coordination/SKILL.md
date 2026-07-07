---
name: spiking-arm-locomotor-coordination
description: Spiking Neural Network architecture coordinating bipedal locomotion and arm control via NEF/SPA with biologically grounded basal ganglia for humanoid robots
tags: [spiking neural network, neuromorphic, humanoid control, basal ganglia, locomotion, arm control, NEF, SPA]
version: 1.0
arxiv_id: 2606.11034v1
created: 2026-06-10
---

# A Spiking Neural Architecture for Coordinating Arm and Locomotor Control

## Paper Information
- **arXiv ID**: 2606.11034v1
- **Authors**: Lea Steffen, Kathryn Simone, Graeme Damberger, Travis DeWolf, Hudson Ly, Chris Eliasmith
- **Published**: 2026-06-09
- **Categories**: cs.RO, cs.NE
- **URL**: https://arxiv.org/abs/2606.11034v1

## Summary

This paper presents the first integrated spiking controller combining bipedal locomotion and arm control on a full-scale humanoid platform. Using the Neural Engineering Framework (NEF) and Semantic Pointer Architecture (SPA), the system coordinates force-based arm control and locomotion mediated by a biologically grounded spiking basal ganglia model, enabling future deployment on low-power neuromorphic hardware.

## Key Contributions

### 1. Integrated Spiking Architecture
- **First full-scale humanoid**: Combines both locomotor and arm control in single spiking system
- **Action selection**: Basal ganglia mediates switching between walking and arm control
- **Force-based arm control**: Novel approach using force feedback for manipulation
- **Bipedal locomotion**: Path-following walking with stability

### 2. Biological Grounding
- **Basal ganglia model**: Spiking implementation of disinhibition-based action selection
- **Cortical circuits**: Motor cortex regions for arm and locomotion control
- **Sensorimotor integration**: Tactile and proprioceptive feedback in spiking circuits

### 3. Neuromorphic Implementation
- **Nengo framework**: Neural Engineering Framework for spiking network construction
- **Isaac Sim validation**: Co-simulation of neural control with physics engine
- **Energy efficiency**: Designed for low-power neuromorphic hardware deployment

## Methodology Details

### Neural Engineering Framework (NEF)
- **Representation**: Neural populations encode vectors via distributed firing rates
- **Transformation**: Computations via weighted connections between populations
- **Dynamics**: Temporal processing via recurrent connections and synaptic filters

### Semantic Pointer Architecture (SPA)
- **High-level control**: Symbolic action representations in neural substrate
- **Bind/unbind operations**: Associative memory for action sequencing
- **Routing**: Basal ganglia disinhibition controls information flow

### Basal Ganglia Action Selection
```
Cortex → Striatum (Go/NoGo pathways)
  ↓
GPi/SNr (Output nucleus)
  ↓
Thalamus (Disinhibition)
  ↓
Motor cortex (Selected action execution)
```

## System Components

### 1. Locomotion Controller
- **Bipedal walking**: Dynamic balance and path-following
- **Foot placement**: Adaptive stepping based on terrain
- **Gait generation**: Central pattern generator + sensory modulation

### 2. Arm Controller
- **Force-based control**: Target reaching via force feedback
- **Digit drawing**: Continuous trajectory generation
- **Manipulation**: Object interaction with tactile sensing

### 3. Action Selection System
- **Basal ganglia**: Spiking model with striatum, GPi/SNr, thalamus
- **Cortical routing**: Motor cortex regions for selected action
- **Switching mechanism**: Disinhibition enables rapid action transitions

## Experimental Validation

### Demonstrated Tasks
1. **Target reaching**: Arm reaches to specified locations
2. **Digit drawing**: Continuous drawing of digits (0-9)
3. **Path-following locomotion**: Walking along predefined paths
4. **Action switching**: Transitioning between walking and arm control

### Co-Simulation Platform
- **Nengo**: Neural network simulation (spiking dynamics)
- **Isaac Sim**: Physics simulation (humanoid robot dynamics)
- **Integration**: Real-time communication between neural controller and physics engine

## Technical Details

### Spiking Implementation
- **Neuron model**: LIF (Leaky Integrate-and-Fire) neurons
- **Encoding**: Rate coding with tuning curves
- **Synaptic filters**: Exponential post-synaptic currents
- **Time steps**: 1ms simulation resolution

### Force-Based Arm Control
- **Force feedback**: Simulated tactile sensors on fingertips
- **Target specification**: Desired force profile for reaching
- **Error correction**: Online adaptation via sensory feedback
- **Joint control**: Force-to-joint-torque transformation

### SPA Operations
- **Bind**: Circular convolution for associative memory
- **Unbind**: Inverse operation for memory retrieval
- **Cleanup**: Similarity-based memory selection
- **Routing**: Disinhibition-based pathway selection

## Applications

### Primary Use Cases
- **Humanoid robots**: Full-body control with coordinated locomotion and manipulation
- **Neuromorphic platforms**: Energy-efficient deployment on specialized hardware
- **Prosthetics**: Bio-inspired control for assistive devices
- **Assistive robotics**: Adaptive systems for human-robot collaboration

### Advantages vs. Traditional Approaches
- **Energy efficiency**: Spiking networks consume less power than ANN
- **Biological plausibility**: Grounded in neuroscience principles
- **Integrated control**: Single unified framework for multiple actions
- **Online adaptation**: Learning through sensory feedback

## Future Directions

### Hardware Deployment
- **Intel Loihi**: Neuromorphic chip implementation
- **SpiNNaker**: Massively parallel spiking simulation
- **Braindrops**: Analog neuromorphic processors

### Extensions
- **Multi-modal sensing**: Vision, auditory, proprioceptive integration
- **Learning**: On-chip plasticity for skill acquisition
- **Social interaction**: Human-robot collaborative tasks
- **Terrain adaptation**: Outdoor walking on uneven surfaces

## Implementation Notes

### Key Innovations
- **First integrated control**: Previous SNN systems addressed locomotion or arm separately
- **Basal ganglia mediation**: Biologically grounded action selection mechanism
- **Force-based approach**: Novel arm control paradigm using force feedback

### Challenges Addressed
- **Action coordination**: Switching between locomotor and manipulator modes
- **Real-time control**: Low-latency spiking processing for dynamic tasks
- **Stability**: Balance during locomotion and manipulation

## Related Skills
- `snn-learning-survey`: Overview of SNN training methods
- `neuromorphic-supremacy-hybrid-astrocytic-spiking`: Advanced neuromorphic architectures
- `robotic-locomotion-dynamics`: Locomotion biomechanics
- `bci-motor-decoding`: Motor cortex decoding for prosthetics

## References
- Paper: https://arxiv.org/pdf/2606.11034v1
- Nengo: https://www.nengo.ai/
- Isaac Sim: https://developer.nvidia.com/isaac-sim
- SPA: Eliasmith & Anderson (2003), "Neural Engineering"

---

**Activation**: Use when designing spiking controllers for humanoid robots, implementing integrated locomotion-manipulation systems, building biologically grounded basal ganglia models, or deploying neural control on neuromorphic hardware. Keywords: spiking humanoid, basal ganglia, locomotion arm coordination, NEF SPA, force-based control, Nengo Isaac Sim, neuromorphic robotics.