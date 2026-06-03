---
name: scalable-snn-without-backprop
description: "Scalable learning in structured recurrent SNNs without backpropagation or surrogate gradients. Uses local plasticity, WTA teaching signals, and random broadcast alignment. Trigger words: SNN without backprop, local plasticity, structured recurrent SNN, WTA teaching signal, broadcast alignment."
category: neuroscience
---

# Scalable Learning in Structured Recurrent SNNs Without Backpropagation

Skill based on arXiv:2605.00402v1 - Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation.

## Core Methodology

### Architecture
- **Structured multi-layer recurrent SNN**: Locally dense recurrent layers
- **Sparse small-world long-range projections**: To readout population
- **Fixed long-range connectivity**: Preserves routing efficiency and hardware scalability
- **Synaptic adaptation**: Performed using strictly local plasticity mechanisms

### Learning Framework (No Backpropagation, No Surrogate Gradients)

#### Component 1: WTA Teaching Signals
- **Population-based Winner-Take-All (WTA)** at output layer
- Provides supervised teaching signals without global error backpropagation
- Biologically plausible competition mechanism

#### Component 2: Fixed Random Broadcast Alignment
- **Fixed random broadcast feedback pathways**
- Aligns local learning with global objective
- Eliminates need for weight transport problem solution

#### Component 3: Local Plasticity Mechanisms
- **Strictly local synaptic updates**
- Compatible with neuromorphic hardware
- Biologically motivated learning rules

### Key Design Principles
1. **No backpropagation**: Eliminates need for differentiable spike models
2. **No surrogate gradients**: Avoids gradient approximation artifacts
3. **Local plasticity only**: Each synapse updates based on local information
4. **Fixed long-range connections**: Hardware-friendly routing
5. **Scalable**: Works with large recurrent architectures

## Implementation

### Network Structure
```
Input → [Dense Recurrent Layer 1] → [Dense Recurrent Layer 2] → ... → Readout
              ↑                          ↑
    Sparse long-range           Sparse long-range
    projections (fixed)         projections (fixed)
```

### Learning Algorithm
```python
# Pseudocode for learning step
for each time_step:
    # Forward pass through recurrent layers
    spikes = propagate_spikes(inputs, recurrent_weights)
    
    # WTA competition at output
    winners = winner_take_all(output_layer_activity)
    
    # Local plasticity update
    for synapse in local_connections:
        pre_activity = synapse.pre_spike_history
        post_activity = synapse.post_spike_history
        teaching_signal = broadcast_feedback(winners)
        delta_w = local_plasticity_rule(pre_activity, post_activity, teaching_signal)
        synapse.weight += delta_w
```

### Hardware Compatibility
- **FPGA/ASIC friendly**: Fixed routing patterns
- **Event-driven**: Spike-based computation
- **Local memory**: Each synapse stores only local state
- **Scalable**: Multi-chip deployment via ring topology

## Applications

### Neuromorphic Computing
- Energy-efficient inference on edge devices
- Event-based sensor processing
- Low-power autonomous systems

### Brain-Inspired AI
- Biologically plausible learning
- Continual learning without catastrophic forgetting
- Real-time adaptive systems

### Scalable SNN Training
- Deep recurrent SNN architectures
- Temporal pattern recognition
- Sequence modeling

## Advantages Over Traditional SNN Training

| Aspect | Surrogate Gradient | This Method |
|--------|-------------------|-------------|
| Backpropagation | Required | Not needed |
| Gradient Approximation | Required | Not needed |
| Hardware Compatibility | Limited | High |
| Biological Plausibility | Low | High |
| Scalability | Moderate | High |
| Memory Requirements | High (global gradients) | Low (local only) |

## Key Parameters

- **Recurrent layer size**: Number of neurons per layer
- **Small-world connectivity**: Sparsity and topology of long-range links
- **WTA capacity**: Number of winners at output layer
- **Plasticity rate**: Learning rate for local updates
- **Broadcast dimensionality**: Size of alignment feedback

## Validation Results
- Scalable to large recurrent architectures
- Competitive performance on temporal tasks
- Hardware-efficient implementation
- Biologically plausible learning dynamics

## References

- **Paper**: Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation
- **Authors**: Bo Tang, Weiwei Xie
- **arXiv**: 2605.00402v1 [cs.NE]
- **Categories**: Neural and Evolutionary Computing (cs.NE)
- **Date**: May 1, 2026

## Related Skills

- spiking-neural-network-analysis
- snn-learning-survey
- multi-plasticity-snn-training
- snn-performance-analysis
