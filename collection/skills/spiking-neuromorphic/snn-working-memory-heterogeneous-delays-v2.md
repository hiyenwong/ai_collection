---
name: snn-working-memory-heterogeneous-delays-v2
description: "Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays. Stores and recalls precise temporal patterns of neural activity using Spiking Motifs. Activation: SNN working memory, heterogeneous delays, spiking motifs, recurrent SNN memory."
---

# Working Memory in Recurrent Spiking Neural Networks with Heterogeneous Synaptic Delays

## Description
Working memory -- the ability to store and recall precise temporal patterns of neural activity -- implemented in recurrent spiking neural networks (SNNs) using heterogeneous synaptic delays. Based on Perrinet 2026 (arXiv:2604.14096v1).

Each synapse is equipped with D delays (e.g., D=41), modeled as a weight tensor W ∈ R^(N×N×D) and trained end-to-end with surrogate-gradient backpropagation through time.

## Methodology

### Core Architecture
- **Recurrent SNN**: N neurons with all-to-all recurrent connections
- **Heterogeneous Delays**: Each synapse has D discrete delays (e.g., D=41)
- **Weight Tensor**: W ∈ R^(N×N×D) representing synaptic weights across delays
- **Training**: Surrogate-gradient backpropagation through time (BPTT)

### Spiking Motifs Representation
- Target spike patterns stored as sequential chains
- **Spiking Motifs**: Contiguous windows of length D that uniquely predict spikes at the next time step
- Overlapping motifs enable pattern completion and recall propagation

### Memory Storage Mechanism
1. **Pattern Encoding**: M arbitrary target spike patterns encoded
2. **Sequential Chains**: Each pattern represented as overlapping Spiking Motifs
3. **Predictive Coding**: Motif windows predict next time step spikes
4. **Recall Propagation**: Recall emerges near clamped initialization, propagates forward

## Implementation Parameters

### Network Configuration
| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| N | Number of neurons | 512 |
| D | Number of delays per synapse | 41 |
| M | Number of stored patterns | 16 |
| T | Time steps | 1000 |

### Training Specifications
- **Algorithm**: Surrogate-gradient backpropagation through time
- **Loss**: Spike timing prediction loss
- **Performance**: Mean F1 score = 1.0 on synthetic benchmark

## Applications

### Primary Use Cases
1. **Neuromorphic Edge Deployment**: Energy-efficient working memory
2. **Temporal Pattern Storage**: Precise spike timing sequences
3. **Sequence Completion**: Pattern recall from partial cues
4. **Memory-Augmented Networks**: Add working memory to SNNs

### Domains
- Brain-computer interfaces
- Neuromorphic computing
- Temporal sequence modeling
- Cognitive computing architectures

## Technical Specifications

### Memory Capacity
- Stores M=16 arbitrary patterns with N=512 neurons
- Each pattern: T=1000 time steps
- Pattern length scales with D (delay count)

### Performance Metrics
- **F1 Score**: 1.0 (perfect recall)
- **Energy Efficiency**: Sparse event-driven computation
- **Recall Dynamics**: Forward propagation from initialization window

### Advantages
- **Energy Efficient**: Sparse spiking activity
- **End-to-End Trainable**: Gradient-based optimization
- **Scalable**: Memory capacity scales with N and D
- **Biologically Plausible**: Inspired by synaptic delay lines

## Activation Keywords
- SNN working memory
- heterogeneous delays
- spiking motifs
- recurrent SNN memory
- temporal pattern storage
- surrogate gradient BPTT
- neuromorphic memory
- spike timing memory

## Tools Used
- **Python/PyTorch**: Implementation framework
- **SpikingJelly**: SNN training library
- ** surrogate_gradient**: Backpropagation through time

## Related Papers
- Perrinet 2026: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays" (arXiv:2604.14096v1)

## References
```bibtex
@article{perrinet2026working,
  title={Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays},
  author={Perrinet, Laurent U},
  journal={arXiv preprint arXiv:2604.14096},
  year={2026}
}
```

---

_Last updated: 2026-04-17_
