---
name: combining-convolution-delay-learning-recurrent-spiking
description: "Combining convolutional recurrent connections with DelRec delay learning in spiking neural networks for resource-constrained edge deployment - arXiv:2604.15997 (April 2026). Covers convolutional recurrent SNNs, axonal delay learning, ~99% parameter reduction, 52x inference speedup on audio classification."
---

# Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

**arXiv:** [2604.15997](https://arxiv.org/abs/2604.15997)
**Date:** April 17, 2026
**Authors:** Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi
**Categories:** cs.NE, cs.LG, q-bio.NC

## Summary

Spiking Neural Networks (SNNs) are gaining momentum for resource-constrained edge systems due to their event-driven, energy-efficient computation. This work extends the **DelRec** approach — a recurrent SNN framework where axonal delays are learned at runtime — by advocating **convolutional recurrent connections** in conjunction with the DelRec delay learning mechanism. The key insight is that replacing dense recurrent weight matrices with convolutional kernels drastically reduces the number of trainable parameters while preserving the temporal modeling capability enabled by learned axonal delays.

On audio classification tasks, this combined approach achieves:
- **~99% savings** in recurrent parameters
- **52x faster inference time**
- **Accuracy comparable** to the original DelRec architecture

## Key Methodology

### DelRec Background

DelRec is a recurrent SNN approach where each recurrent connection is parameterized by a learnable **axonal delay** value rather than (or in addition to) a synaptic weight. These delays are optimized at runtime via gradient descent, allowing the network to discover useful temporal processing structures without manual delay tuning.

### Convolutional Recurrent Connections

Instead of using a dense (fully connected) recurrent weight matrix — which scales quadratically with the number of neurons — this work proposes using **convolutional kernels** for the recurrent connections. Key advantages:

1. **Parameter sharing** across spatial locations reduces parameter count dramatically
2. **Local connectivity patterns** are enforced naturally by the convolution kernel
3. **Spatial structure** in spike patterns is exploited rather than flattened

### Delay Learning Integration

The convolutional recurrent connections are combined with DelRec-style delay learning:
- Axonal delays remain **learnable** during training
- Delays modulate **when** recurrent spikes arrive, enabling precise temporal processing
- The convolution structure constrains **where** recurrent connections exist
- Together, the spatial efficiency of convolutions and the temporal expressiveness of learned delays create a compact yet powerful architecture

## Core Architecture

```
Convolutional Recurrent SNN with Delay Learning (Conv-DelRec):
+-- Input Layer
|   +-- Spike encoding (e.g., rate coding or latency coding)
|   +-- Feeds into convolutional SNN backbone
+-- Convolutional SNN Layers
|   +-- Standard Conv2D-SNN blocks (stride, padding as needed)
|   +-- Leaky Integrate-and-Fire (LIF) neurons
|   +-- Surrogate gradient for backpropagation through spikes
+-- Convolutional Recurrent Block
|   +-- Conv2D recurrent kernel (shared weights)
|   +-- Learnable axonal delays (per-channel or per-filter)
|   +-- LIF neuron membrane dynamics
|   +-- Spike generation and delayed feedback
+-- Readout Layer
|   +-- Global pooling (e.g., average over spatial dimensions)
|   +-- Fully connected classification head
+-- Training
    +-- Surrogate gradient backpropagation (BPTT through time)
    +-- Delay parameters updated via gradient descent
    +-- Standard loss (e.g., cross-entropy with rate decoding)
```

### Parameter Comparison

| Component | DelRec (Dense) | Conv-DelRec (Proposed) |
|-----------|---------------|----------------------|
| Recurrent weights | O(N^2) | O(K^2 x C^2) where K=kernel, C=channels |
| Axonal delays | O(N^2) | O(C) or O(K^2 x C) |
| Total recurrent params | Very large | ~1% of dense |
| Inference speed | Baseline | **52x faster** |

## Implementation Notes

### Framework Considerations

- Implement using **PyTorch** with custom spiking neuron modules
- Surrogate gradient functions needed (e.g., ATen-based or sigmoid-derived)
- Delayed spike transmission requires custom **buffer/queue mechanisms** for storing spikes across timesteps
- Convolutional recurrence can be implemented via `nn.Conv2d` applied to the previous timestep's spike map

### Key Implementation Steps

1. **Define LIF neuron** with membrane potential decay, threshold, and reset mechanism
2. **Implement delay buffer** — circular buffer that holds spike traces for the required delay timesteps
3. **Create ConvRNN cell** — applies Conv2d to delayed spike input from previous timestep
4. **Make delays learnable** — register as `nn.Parameter` with positive constraint (e.g., softplus)
5. **Training loop** — unroll SNN over T timesteps; accumulate surrogate gradients through both weights and delays

### Delay Parameterization

```python
# Example: learnable delays with positive constraint
import torch
import torch.nn as nn

class LearnableDelays(nn.Module):
    def __init__(self, num_channels, max_delay=20):
        super().__init__()
        self.max_delay = max_delay
        # Raw delay logits (positive via softplus)
        self.delay_logits = nn.Parameter(torch.randn(num_channels))

    def forward(self, spike_tensor, delay_buffer):
        # Compute actual delays
        delays = torch.softplus(self.delay_logits).int().clamp(1, self.max_delay)
        # Retrieve delayed spikes from buffer
        delayed_spikes = delay_buffer.get(delays)
        return delayed_spikes
```

### Training Tips

- Use **small learning rates for delay parameters** (e.g., 10x smaller than weight LR)
- Apply **delay regularization** to prevent degenerate solutions
- **Gradient clipping** recommended due to surrogate gradient instabilities
- Typical training: 100-300 epochs with cosine annealing scheduler

## Results

### Audio Classification Performance

| Metric | DelRec (Dense Recurrent) | Conv-DelRec (Proposed) |
|--------|-------------------------|----------------------|
| Accuracy | Baseline DelRec accuracy | Comparable (retained) |
| Recurrent parameters | Full dense matrix | **~99% reduction** |
| Inference time | 1x (baseline) | **52x faster** |
| Model size | Larger | Significantly smaller |

### Key Findings

1. **Parameter efficiency**: Convolutional weight sharing reduces recurrent parameters by approximately 99%, making the architecture viable for edge devices with limited memory
2. **Inference speedup**: The sparse, structured nature of convolutional recurrent connections enables 52x faster inference compared to dense recurrent counterparts
3. **Accuracy preservation**: Despite massive parameter reduction, the learned delays compensate for the reduced expressiveness, maintaining competitive accuracy
4. **Scalability**: The convolutional approach scales more favorably with increasing channel counts compared to dense recurrent connections

### Suitability for Edge Deployment

- Low memory footprint (few parameters to store)
- Fast inference (structured operations amenable to hardware acceleration)
- Event-driven computation (SNNs naturally sparse)
- Compatible with neuromorphic hardware (e.g., Intel Loihi, SpiNNaker)

## Activation Triggers

This skill is relevant when:
- Building **spiking neural network (SNN)** architectures for edge/embedded deployment
- Optimizing **recurrent connections in SNNs** for parameter efficiency
- Implementing **delay learning** mechanisms in neuromorphic systems
- Designing **audio classification** systems with low-latency requirements
- Exploring **convolutional recurrence** as an alternative to dense RNN connections
- Reducing **inference latency** in recurrent spiking models
- Working with **DelRec** or similar delay-based recurrent SNN frameworks
- Deploying SNNs on **resource-constrained hardware** (microcontrollers, neuromorphic chips)
- Combining **spatial (convolution) and temporal (delay)** processing in neural networks

## Citations

```bibtex
@article{zebendo2026combining,
  title={Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks},
  author={Zebendo, L\'ucio Folly Sanches and Cicciarella, Eleonora and Rossi, Michele},
  journal={arXiv preprint arXiv:2604.15997},
  year={2026}
}
```
