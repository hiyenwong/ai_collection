---
name: snn-working-memory-heterogeneous-delays-v3
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Enables energy-efficient neuromorphic storage and recall of precise temporal spike patterns through weight tensor modeling and surrogate-gradient backpropagation. Activation: SNN working memory, heterogeneous synaptic delays, spike pattern storage, recurrent SNN memory, temporal pattern recall."
version: v1.0.0
last_updated: 2026-04-16
arxiv_source: "2604.14096v1"
---

# SNN Working Memory with Heterogeneous Synaptic Delays

Working memory implementation in recurrent spiking neural networks (SNNs) using heterogeneous synaptic delays modeled as weight tensors. Enables storage and recall of precise temporal patterns of neural activity.

## Core Innovation

This methodology addresses the challenge of implementing working memory in SNNs by:
- **Heterogeneous delays**: Each synapse equipped with D=41 delays
- **Weight tensor representation**: Synaptic weights modeled as $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$
- **Fixed-point dynamics**: Patterns stored as fixed points of network dynamics
- **Surrogate-gradient training**: End-to-end backpropagation through time with spike-compatible gradients

## Technical Details

### Network Architecture
- **Recurrent SNN** with N neurons
- **Delay dimension**: D = 41 delays per synapse
- **Pattern storage**: M arbitrary target spike patterns
- **Recall mechanism**: Brief external cue triggers pattern retrieval

### Training Methodology

1. **Surrogate-Gradient Backpropagation**
   - Replace non-differentiable spikes with smooth surrogate functions
   - Enable end-to-end gradient flow through temporal dynamics
   - Train with backpropagation through time (BPTT)

2. **Pattern Storage as Fixed Points**
   - Encode target patterns as stable attractor states
   - Network dynamics converge to stored patterns upon cue presentation
   - Fixed-point stability ensures robust pattern maintenance

3. **Temporal Precision**
   - Heterogeneous delays enable precise spike timing
   - Weight tensor captures temporal dependencies across multiple time scales
   - Supports 64-dimensional spike patterns with high fidelity

## Implementation Guidelines

### Network Configuration
```python
N = 256  # Number of neurons
D = 41   # Delays per synapse
M = 16   # Number of stored patterns
pattern_dim = 64  # Spike pattern dimensionality
```

### Weight Tensor Structure
```
W[i, j, d] = synaptic weight from neuron j to neuron i with delay d
where i, j ∈ [0, N-1], d ∈ [0, D-1]
```

### Training Loop
1. Initialize weight tensor with small random values
2. For each training epoch:
   - Present target patterns
   - Compute surrogate gradients through spike dynamics
   - Update weights via gradient descent
3. Validate pattern recall with brief cues

## Activation Keywords

- SNN working memory
- heterogeneous synaptic delays
- spike pattern storage
- recurrent SNN memory
- temporal pattern recall
- neuromorphic memory
- spike-based working memory
- delay-based SNN

## Use Cases

1. **Neuromorphic Computing**: Energy-efficient memory for edge devices
2. **Brain-Computer Interfaces**: Pattern storage for neural decoding
3. **Temporal Pattern Recognition**: Sequence learning and prediction
4. **Robotics**: Sensorimotor memory for autonomous agents

## Performance Metrics

- Successfully stores M=16 distinct 64-dimensional spike patterns
- High temporal precision in pattern recall
- Energy-efficient compared to rate-based neural networks

## References

- Paper: arXiv:2604.14096v1 (April 2026)
- Title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
- Author: Laurent U Perrinet
- PDF: https://arxiv.org/pdf/2604.14096v1

## Related Skills

- snn-heterogeneous-delay-working-memory
- spiking-neural-network-training
- neuromorphic-computing

## Notes

- Surrogate-gradient selection affects training stability
- Delay range should match pattern temporal characteristics
- Network size scales with pattern complexity and capacity requirements
