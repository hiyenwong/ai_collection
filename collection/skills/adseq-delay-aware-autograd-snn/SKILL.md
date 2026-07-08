---
name: adseq-delay-aware-autograd-snn
description: "ADSEQ: delay-aware autograd-compatible framework for spike-event delivery in SNNs — memory-efficient autodifferentiable spike event queues with delay support, benchmarked across CPU/GPU/TPU/LPU platforms. arXiv:2512.05906v2"
tags: ["spiking-neural-networks", "autograd", "spike-delivery", "delay", "memory-efficient", "hardware-benchmark", "SNN-simulation", "queue-design"]
activation_words: [ADSEQ, spike event queue, delay-aware SNN, autograd SNN, spike delivery, ring buffer SNN, SNN accelerator benchmark, CPU GPU TPU LPU, selective spike dropping]
arxiv_id: "2512.05906"
---

# ADSEQ: Delay-Aware Autograd-Compatible Framework for Spike-Event Delivery in SNNs

## Paper Info
- **Title**: ADSEQ: A delay-aware autograd-compatible framework for spike-event delivery in SNNs
- **arXiv**: 2512.05906v2 (updated July 7, 2026)
- **Authors**: Lennart P. L. Landsmeer, Amirreza Movahedin, Said Hamdioui, Christos Strydis
- **Categories**: cs.NE

## Core Problem

Spiking Neural Networks (SNNs) require:
1. **Efficient simulation** — sparse spike events, not dense activations
2. **Gradient-based training** — backpropagation through spike times
3. **Spike delays** — biologically realistic and computationally important

**Gap**: Current SNN frameworks either:
- Use dense, memory-heavy data structures (defeating spike sparsity)
- Lack exact gradient methods with generality
- Omit or inefficiently handle delayed spikes

## Key Innovation

**Gradient computation through spike event queues** — including delays — implemented as memory-efficient, autodifferentiable data structures (ADSEQ).

### Queue Design Findings (Platform-Specific)

| Platform | Best Data Structure | Notes |
|----------|-------------------|-------|
| **CPU** | Tree-based or FIFO | Traditional implementations work well |
| **GPU** (small sim) | Ring buffers | Excel with contiguous memory access |
| **GPU** (high memory pressure) | Sparse data structures | Prefer sparsity under pressure |
| **TPU** | Sorting intrinsics | Leverage TPU's sorting hardware |
| **LPU** | (benchmarked) | Novel neuromorphic platform |

### Key Insight
> Queue design strongly shapes performance — there is no one-size-fits-all solution.

## Methodology

### 1. Spike Event Queue Formulation
- Represent spikes as events in a queue (not dense tensors)
- Each event: (timestamp, neuron_id, delay)
- Queue operations: insert, pop, delay propagation

### 2. Autodifferentiable Implementation
- Derive gradient computation through queue operations
- Make queue operations compatible with autograd (PyTorch/JAX)
- Handle delays explicitly in forward and backward passes

### 3. Memory Efficiency
- Sparse representation: only store actual spikes
- Avoid dense time × neuron matrices
- Scale to large networks without memory explosion

### 4. Selective Spike Dropping
- Trade-off: drop low-importance spikes for speed
- Provides simple performance-accuracy knob
- Future work: adaptive dropping based on gradient magnitude

## Design Principles

1. **Event-driven, not time-stepped** — process only when spikes occur
2. **Delay-aware** — synaptic and axonal delays are first-class citizens
3. **Platform-adaptive** — different data structures for different hardware
4. **Autograd-native** — gradients flow through queue operations naturally

## Applications

1. **Large-scale SNN simulation** — memory-efficient training of networks with millions of neurons
2. **Neuromorphic hardware compilation** — queue-based representation maps to neuromorphic cores
3. **Biologically realistic modeling** — delays are essential for realistic neural dynamics
4. **Multi-platform deployment** — same code runs on CPU/GPU/TPU/LPU with optimal data structures

## Implementation Notes

- Built on top of existing autograd frameworks (PyTorch-compatible)
- Queue operations are differentiable — gradients flow through insert/pop/delay
- Selective spike dropping is a runtime knob, not a training-time approximation
- Platform detection can auto-select optimal data structure

## Limitations

- Selective spike dropping is a heuristic — optimal dropping strategy unknown
- Platform-specific optimizations require separate implementations
- Delay handling adds complexity to gradient computation
- Not yet validated on very large-scale (>1M neuron) networks

## Related Work

- **SNN simulators**: BindsNET, Norse, SpikingJelly, Brian2
- **Event-driven simulation**: NEST, Neuron
- **Gradient methods**: surrogate gradients, e-prop, backprop through time
- **Hardware**: SpiNNaker, Loihi, TrueNorth

## Future Directions

The paper suggests:
> Future autograd frameworks could adapt diverging primal/tangent data-structures — using different representations for forward pass (speed) vs backward pass (gradient accuracy).

This is a profound insight: the forward simulation might benefit from one data structure (e.g., ring buffer for GPU), while the backward pass might need another (e.g., sparse for memory efficiency).

## Activation Keywords
ADSEQ, spike event queue, delay-aware SNN, autograd SNN, spike delivery, ring buffer SNN, SNN accelerator benchmark, CPU GPU TPU LPU, selective spike dropping, memory-efficient SNN, differentiable queue
