---
name: snn-working-memory-heterogeneous-delays-v3
description: "Working memory implementation in recurrent spiking neural networks (HD-SNN) with heterogeneous synaptic delays. Stores and recalls precise temporal patterns of neural activity using Spiking Motifs and sequential spike prediction. Activation: HD-SNN, working memory, heterogeneous delays, spiking motifs, recurrent SNN memory, sequential spike prediction, delay tensor, surrogate gradient, neuromorphic memory, synaptic delay lines, temporal pattern storage."
source_paper:
  title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
  author: "Laurent U. Perrinet"
  arxiv: "2604.14096v1"
  published: "2026-04-15"
  category: "q-bio.NC"
  url: "https://arxiv.org/abs/2604.14096"
  pdf: "https://arxiv.org/pdf/2604.14096v1"
version: "3.0"
updated: "2026-04-20"
---

# Working Memory in Recurrent Spiking Neural Networks with Heterogeneous Synaptic Delays

## Overview

This skill implements **Working Memory in a Heterogeneous Delay Spiking Neural Network (HD-SNN)** — a recurrent SNN architecture where each synapse is modeled as a three-dimensional weight tensor with learnable heterogeneous delays. The network achieves working memory by predicting future spikes, representing each target pattern as a chain of overlapping **Spiking Motifs** that propagate recall forward in time.

Based on Perrinet (2026), arXiv:2604.14096v1.

## Architecture: D=41 Heterogeneous Delay Tensor

### Core Structure

The HD-SNN architecture departs from traditional SNNs by replacing point-to-point synaptic weights with a **three-dimensional delay tensor**:

```
W ∈ R^(N×N×D)
```

Where:
- **N** = number of neurons in the recurrent network
- **N×N** = all-to-all recurrent connectivity matrix  
- **D = 41** = number of discrete heterogeneous delays per synapse

Each element `W[i, j, d]` represents the synaptic weight from presynaptic neuron `j` to postsynaptic neuron `i` with delay `d` time steps.

### Why D=41?

The specific choice of **D=41 delays** is a key design parameter that:
1. **Captures motif windows**: Each Spiking Motif is a contiguous window of length D, so D=41 provides sufficient temporal context for pattern prediction
2. **Enables overlapping motifs**: Adjacent motifs overlap within the D-step window, enabling recall propagation from one motif to the next
3. **Balances capacity and complexity**: Larger D increases representational capacity but also training complexity; D=41 was found to be an effective trade-off
4. **Covers relevant biological timescales**: Synaptic delays in biological neural systems span similar ranges (~1-40ms)

### Delay Tensor Properties

- **Sparse activation**: Only a subset of the D delay channels per synapse carry significant weight after training
- **Heterogeneous**: Different synapses learn different delay distributions — not uniform across the network
- **Learnable**: All delay channels are jointly optimized end-to-end
- **Temporal receptive field**: The D delays effectively give each neuron a temporal receptive field of D time steps

## End-to-End Training Methodology

### Surrogate-Gradient Backpropagation Through Time (BPTT)

The HD-SNN is trained end-to-end using **surrogate-gradient BPTT**, which addresses the non-differentiability of the spiking operation:

1. **Surrogate gradients**: Replace the non-differentiable Heaviside step function of spike generation with a smooth approximation (e.g., sigmoid, exponential, or piecewise-linear surrogate)
2. **BPTT**: Gradients flow backward through time across the full temporal sequence
3. **Delay tensor optimization**: All elements of W ∈ R^(N×N×D) are updated simultaneously via gradient descent

### Training Pipeline

```
Target Spike Patterns → Spiking Motif Decomposition → Network Initialization → 
Forward Pass (spike simulation with delays) → Loss Computation → 
Surrogate-gradient BPTT → Weight Tensor Update → Iterate
```

### Loss Function

The loss function measures the discrepancy between **predicted spikes** and **target spike patterns**:
- **Spike timing prediction loss**: Quantifies how well the network's output spikes match the target temporal pattern
- **Pattern completion objective**: Network learns to fill in missing spike events from partial cues

### Training Characteristics

- **Clamped initialization**: A short initialization window where the target pattern is clamped (forced) to bootstrap recall
- **Free recall phase**: After initialization, the network autonomously continues generating the pattern from its recurrent dynamics
- **Convergence**: The delay tensor converges to weights that implement sequential spike prediction via overlapping motifs

## How Working Memory Emerges from Delay Structure

### Spiking Motifs

A **Spiking Motif** is defined as a **contiguous window of length D** in the spike train that uniquely predicts the spike pattern at the next time step.

```
Motif at time t: S[t-D:t] → predicts S[t]
```

Where S is the spike pattern and D is the delay window size.

### Sequential Chain Mechanism

1. **Pattern Decomposition**: Each target spike pattern of length T is decomposed into overlapping Spiking Motifs
2. **Motif-to-Motif Transition**: The delay tensor learns to map each motif to its successor motif
3. **Chain Formation**: Overlapping motifs form a sequential chain: Motif₁ → Motif₂ → Motif₃ → ...
4. **Recall Propagation**: Once a motif is activated (by clamped initialization or partial cue), the network's recurrent dynamics automatically propagate through the chain, recalling the full pattern

### Memory Storage as Weight Encoding

Memory is stored **implicitly** in the delay tensor weights:
- Strong weights at specific delays encode the transitions between motifs
- The heterogeneous delay structure allows different motifs to be active at different temporal scales
- Overlapping motifs share weight structure, enabling efficient storage of multiple patterns

### Recall Dynamics

1. **Cue presentation**: A partial or clamped initialization activates the first motif(s)
2. **Forward propagation**: Each activated motif, through its learned delay connections, triggers the next motif in the chain
3. **Full pattern reconstruction**: The cascade of motif activations reconstructs the complete stored temporal pattern
4. **Robustness**: Overlapping motif structure provides fault tolerance — partial cues can still trigger full recall

## Performance Metrics

### Benchmark Configuration

| Parameter | Symbol | Value | Description |
|-----------|--------|-------|-------------|
| Neurons | N | 512 | Network size |
| Delay channels | D | 41 | Heterogeneous delays per synapse |
| Stored patterns | M | 16 | Number of arbitrary spike patterns |
| Time steps | T | 1000 | Pattern duration |
| Motif length | L | D=41 | Contiguous prediction window |

### Results

| Metric | Value | Notes |
|--------|-------|-------|
| **Mean F1 Score** | **1.0** | Perfect recall on synthetic benchmark |
| **Pattern Capacity** | M=16 | Stored patterns in N=512 neurons |
| **Recall Fidelity** | Perfect | Exact spike timing reconstruction |
| **Energy Efficiency** | High | Sparse event-driven computation |
| **Training** | End-to-end | Surrogate-gradient BPTT |

### Scaling Properties

- **Memory capacity** scales with both N (neurons) and D (delay channels)
- **Pattern length** scales with D (longer delay windows support longer motifs)
- **Number of patterns** M is limited by the combinatorial capacity of the delay tensor

## Comparison to Previous Approaches

### vs. Traditional SNN Working Memory

| Aspect | Traditional SNNs | HD-SNN (This Work) |
|--------|-----------------|-------------------|
| Synaptic model | Single weight per connection | D-dimensional delay tensor |
| Temporal coding | Rate-based or fixed delays | Heterogeneous learnable delays |
| Memory mechanism | Persistent activity / synaptic plasticity | Spiking Motif chains |
| Training | Often heuristic or local rules | End-to-end surrogate-gradient BPTT |
| Temporal precision | Limited | Exact spike timing |

### vs. Continuous RNNs (LSTM/GRU)

| Aspect | LSTM/GRU | HD-SNN |
|--------|----------|--------|
| Computation | Dense, continuous | Sparse, event-driven |
| Energy | High (continuous activation) | Low (only active during spikes) |
| Temporal resolution | Fixed time steps | Event-driven, microsecond precision |
| Biological plausibility | Low | High (inspired by synaptic delay lines) |
| Hardware deployment | Standard processors | Neuromorphic chips |

### vs. Other SNN Memory Architectures

| Architecture | Mechanism | HD-SNN Advantage |
|-------------|-----------|-----------------|
| Reservoir Computing | Fixed random recurrent weights | Fully trainable, optimal delay structure |
| Liquid State Machines | Fixed reservoir + readout training | End-to-end trainable |
| STDP-based SNNs | Local Hebbian plasticity | Global optimization via BPTT |
| Delay-based SNNs (uniform delays) | Single delay per synapse | Heterogeneous delays (D=41 channels) |

## Implementation Parameters

### Network Configuration

| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| N | Number of neurons | 512 |
| D | Number of delays per synapse | 41 |
| M | Number of stored patterns | 16 |
| T | Time steps per pattern | 1000 |
| W shape | Delay tensor dimensions | (N, N, D) = (512, 512, 41) |
| Motif length | Prediction window | D = 41 |

### Training Specifications

| Parameter | Description |
|-----------|-------------|
| Algorithm | Surrogate-gradient Backpropagation Through Time |
| Loss | Spike timing prediction loss |
| Initialization | Clamped window at pattern start |
| Recall | Autonomous propagation after initialization |
| Surrogate | Smooth approximation of spike threshold function |
| Optimizer | Gradient-based (Adam/SGD) |

### Memory Specifications

- **Pattern encoding**: M arbitrary target spike patterns → overlapping Spiking Motifs
- **Storage capacity**: Scales with N×N×D parameter count
- **Recall mode**: Forward propagation from clamped/seed initialization
- **Robustness**: Overlapping motifs provide pattern completion from partial cues

## Applications

### Primary Use Cases

1. **Neuromorphic Edge Deployment**: Energy-efficient working memory on specialized hardware (Loihi, SpiNNaker, DYNAP-SE)
2. **Temporal Pattern Storage**: Precise spike timing sequence storage and recall
3. **Sequence Completion**: Pattern recall from partial or noisy cues
4. **Memory-Augmented SNNs**: Add working memory modules to larger spiking network architectures
5. **Temporal Signal Processing**: Time-series prediction and filtering in spike domain

### Domains

- Brain-computer interfaces (BCI)
- Neuromorphic computing
- Temporal sequence modeling
- Cognitive computing architectures
- Event-based vision and audio processing
- Robotic control with temporal memory

## Implementation Notes

### Key Implementation Steps

1. **Initialize delay tensor**: `W = torch.randn(N, N, D)` 
2. **Define neuron model**: LIF or similar spiking neuron with surrogate gradient
3. **Implement delay-aware recurrence**: For each time step, sum delayed presynaptic spikes across all D delay channels
4. **Define loss**: Compare network output spikes to target pattern
5. **Train with surrogate BPTT**: Standard PyTorch autograd with surrogate gradient wrapper
6. **Evaluate**: Measure F1 score between predicted and target spike trains

### Delay-Aware Recurrence Formula

At each time step t, the input current to neuron i:

```
I_i(t) = Σ_j Σ_d W[i,j,d] · S_j(t-d)
```

Where S_j(t-d) is the spike output of neuron j at time t-d, and the sum over d runs across all D delay channels.

### Memory Capacity Formula

Maximum patterns M scales approximately as:

```
M ∝ (N × D) / L
```

Where L is the motif length (typically D).

## Activation Keywords

- HD-SNN
- heterogeneous delays
- working memory
- spiking motifs
- recurrent SNN memory
- sequential spike prediction
- delay tensor
- surrogate gradient
- BPTT
- neuromorphic memory
- spike timing memory
- temporal pattern storage
- synaptic delay lines
- pattern completion
- event-driven memory
- SpikingJelly
- Loihi
- neuromorphic computing
- temporal sequence modeling

## Tools Used

- **Python/PyTorch**: Implementation framework
- **SpikingJelly**: SNN training library
- **Surrogate gradients**: Backpropagation through non-differentiable spike function
- **Neuromorphic hardware**: Loihi, SpiNNaker, DYNAP-SE (for deployment)

## Related Papers

- Perrinet 2026: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays" (arXiv:2604.14096v1)

## References

```bibtex
@article{perrinet2026working,
  title={Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays},
  author={Perrinet, Laurent U.},
  journal={arXiv preprint arXiv:2604.14096},
  year={2026},
  month={April},
  eprint={2604.14096},
  primaryClass={q-bio.NC}
}
```

---

_Last updated: 2026-04-20_
_v3: Enhanced with detailed D=41 delay tensor architecture analysis, end-to-end training methodology, working memory emergence mechanism, performance metrics, and comparison to previous approaches._

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Snn Working Memory Heterogeneous Delays V3 usage
```
User: "Help me with snn working memory heterogeneous delays v3"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed snn working memory heterogeneous delays v3 assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
