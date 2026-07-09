---
name: dynamic-neural-manifolds-neuromorphic
description: Dynamic neural manifolds methodology for neuromorphic hardware implementation. Bridges computational neuroscience with SpiNNaker 2 chip for real-time closed-loop robotic control through parameterizable manifold geometry.
tags: [neuromorphic, neural-manifolds, spiking-neural-networks, spinnaker, closed-loop-control, robotics]
arxiv_id: "2607.07373v1"
date: 2026-07-08
---

# Dynamic Neural Manifolds for Neuromorphic Hardware

## Overview

This methodology implements dynamic neural manifolds on SpiNNaker 2 neuromorphic hardware for real-time, closed-loop control. The approach maps biological neural dynamics (sequential activity evolving along low-dimensional manifolds) to neuromorphic engineering, enabling explainable autonomous systems.

## Core Concepts

### Neural Manifolds
- Collective neural activity represented as trajectories in N-dimensional state space
- Biological activity constrained to low-dimensional manifolds capturing latent task variables
- Geometric features map to behavioral execution (subspace rotations for behavior switching, trajectory speed for timing control)

### Circuit Mechanisms as Control Knobs
Three key mechanisms enable dynamic manifold control:

1. **Heterogeneous Inhibition** → Subspace reorientation
   - Inhibitory ensembles silence random neuron subsets
   - Switching ensembles rotates neural subspace (angle = arccos(1-p_inh))
   - Enables behavior state switching

2. **Gain Modulation** → Trajectory speed control
   - Multiplicative gain S affects bump propagation speed
   - Controls neural trajectory velocity in state space

3. **Transient Currents** → Trajectory shape/radius
   - Additive current I changes active neuron count
   - Controls bump size and trajectory radius

### SpiNNaker 2 Implementation
- Ring network with asymmetric recurrent connectivity
- Activity bump propagates around ring (oscillatory sequences)
- Spike-based communication with probabilistic rate-to-spike conversion
- Circulant weight matrix with sparsity for memory efficiency
- Streaming architecture: control parameters in, spikes out for closed-loop

## Key Results

### Validation
- SpiNNaker 2 implementation matches rate-based CPU model across parameter ranges
- Subspace rotations follow theoretical scaling (arccos(1-p_inh))
- Speed control linear with gain parameter
- Shape control linear with current parameter

### Robotic Application
- Two-wheeled agent navigates virtual maze
- 500 neurons, 20% connectivity, 3 subspaces (40% neurons each)
- Subspaces encode: forward movement, turning, jumping
- Sensory feedback dynamically modulates control parameters
- Readout weights trained via random exploration (200 actions × 250ms)

### Efficiency
- Runtime scales linearly with spike count
- 500 neurons, 20% connectivity: well below 1ms real-time threshold
- Execution time ∝ mean spike count per timestep

## Methodology

### Implementation Steps
1. Design ring network with asymmetric recurrent weights
2. Implement control neuron populations (speed, shape, selection)
3. Map to SpiNNaker 2 with spike-based communication
4. Optimize: circulant weights, sparsity mask, streaming I/O
5. Train readout weights from network activity to motor commands
6. Close loop: sensory input → control parameters → network activity → action

### Control Parameter Mapping
```
Sensory Input → Control Parameters → Manifold Geometry → Motor Output
- Wall distance → Speed (S) → Trajectory velocity → Wheel speed
- Ground type → Shape (I) → Bump size → Movement mode
- Plan step → Selection (p_inh) → Subspace → Behavior type
```

## Applications

- **Explainable neuromorphic robotics**: Internal state mathematically interpretable
- **Biological neural dynamics research**: Testbed for circuit-manifold-behavior mappings
- **Energy-efficient adaptive control**: Low-latency, low-power edge deployment
- **Brain-inspired AI**: Geometrically parameterizable neural computation

## Pitfalls

- Limited on-chip memory constrains recording/storage (128kB SRAM)
- Spike-based conversion adds noise vs. rate-based models
- Trade-off between network size and real-time performance
- Readout training requires extensive random exploration

## Verification

- Compare spike counts to rate-based model across parameter ranges
- Validate subspace angles match arccos(1-p_inh) prediction
- Measure runtime vs. spike count (should be linear)
- Test closed-loop maze navigation success rate

## References

- von Seeler, Tetzlaff, Lehr (2026) arXiv:2607.07373v1
- Build on framework from [12, 13] (same authors, rate-based model)
- SpiNNaker 2 hardware: [8, 16]
