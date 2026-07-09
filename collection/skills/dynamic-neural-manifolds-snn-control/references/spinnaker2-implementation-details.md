# SpiNNaker 2 Implementation Details

## Circuit Mechanisms → Manifold Geometry Mapping

| Circuit Mechanism | Manifold Property | Behavioral Function |
|-------------------|-------------------|---------------------|
| **Heterogeneous Inhibition** | Subspace orientation (rotation angle = arccos(1-p_inh)) | Behavior state switching |
| **Gain Modulation** | Trajectory speed | Movement timing control |
| **Transient Currents** | Trajectory shape/radius | Movement parameter adjustment |

## SpiNNaker 2 Architecture

### Ring Network Model
- **Neurons**: Rate-based (original) → Spike-based (SpiNNaker 2)
- **Connectivity**: Asymmetric recurrent weights (circulant structure)
- **Activity bump**: Stable packet of neural activity propagates around ring
- **Control neurons**: Three populations (speed, shape, selection) modulate ring dynamics

### Hardware Optimizations
- Spike-based communication (probabilistic rate-to-spike conversion)
- Circulant weight matrix with sparsity mask
- Streaming I/O for closed-loop control
- 128kB SRAM per core constraint → streaming architecture required

### Performance Metrics
- 500 neurons, 20% connectivity → <1ms real-time timestep
- Runtime scales **linearly** with mean spike count per timestep
- Larger bumps (more active neurons) → higher computational cost
- More inhibition (fewer spikes) → lower runtime

## Validation Results

### Parameter Control Accuracy
- **Shape control (current I)**: Bump size changes match rate-based model
- **Speed control (gain S)**: Trajectory velocity scales linearly with S
- **Subspace rotation (inhibition p_inh)**: Angles follow arccos(1-p_inh) prediction

### Closed-Loop Robotic Control
**Task**: Two-wheeled agent navigates virtual maze
- **Actions**: Forward movement, turning in place, jumping
- **Network**: 500 neurons, 3 subspaces (40% neurons each)
- **Training**: Random exploration (200 actions × 250ms) → learn readout weights
- **Sensory feedback**: Wall distances, ground type → modulate control parameters

**Control flow**:
```
High-level plan + Sensory input → Control parameters → Manifold geometry → Motor output
```

## Biological Relevance

### Cross-Species Evidence
Oscillatory sequences on low-dimensional manifolds observed in:
- Rat spinal cord (motor control)
- Drosophila larvae ganglia (calcium waves)
- Turtle spinal cord (locomotion)
- Mouse medial entorhinal cortex (spatial navigation)

## Limitations

- **Memory constraints**: Limited on-chip storage (128kB SRAM) restricts recording duration
- **Spike noise**: Probabilistic rate-to-spike conversion adds variability vs. rate-based models
- **Scalability trade-off**: Larger networks → higher runtime, may exceed real-time threshold
- **Training cost**: Readout requires extensive random exploration (200 actions)
- **Hardware specificity**: Optimizations tied to SpiNNaker 2 architecture
