---
name: eventqueues-autodifferentiable-snn
description: "Autodifferentiable spike event queues for efficient SNN simulation on AI accelerators (CPU, GPU, TPU, LPU). Enables gradient-based training of spiking neural networks with memory-efficient event-driven computation. Activation: spiking neural network, SNN, event queue, autodifferentiable, neuromorphic simulation, AI accelerator."
---

# EventQueues: Autodifferentiable Spike Event Queues for Brain Simulation

> Memory-efficient, gradient-enabled event queue structures for scalable spiking neural network simulation across CPU, GPU, TPU, and LPU platforms.

## Metadata
- **Source**: arXiv:2512.05906v1
- **Authors**: Lennart P. L. Landsmeer, Amirreza Movahedin, Said Hamdioui, Christos Strydis
- **Published**: 2025-12-05
- **Categories**: cs.NE (Neural and Evolutionary Computing)

## Core Methodology

### Key Innovation
Traditional gradient-based SNNs implement sparse spike events using dense, memory-heavy data structures. EventQueues introduces:
1. **Exact gradient computation through spike event queues** - including delayed spikes
2. **Memory-efficient event queue structures** - optimized for gradient-enabled simulation
3. **Cross-platform benchmarking** - CPU, GPU, TPU, and LPU performance analysis

### Technical Framework

#### 1. Event Queue Design Patterns
- **Tree-based/FIFO**: Optimal for CPU implementations
- **Ring buffers**: Best for GPU with smaller simulations
- **Sparse data structures**: Preferred under high memory pressure on GPUs
- **Sorting intrinsics**: Favored by TPU architectures

#### 2. Delayed Spike Handling
Addresses a critical gap in current simulators that often omit or inefficiently handle delayed spikes.

#### 3. Performance-Accuracy Trade-offs
Selective spike dropping provides configurable performance-accuracy trade-offs.

## Implementation Guide

### Prerequisites
- PyTorch or JAX for automatic differentiation
- Access to target accelerators (GPU/TPU/LPU)
- SNN framework (e.g., SpikingJelly, snnTorch)

### Platform-Specific Optimizations

#### CPU
```python
# Tree-based or FIFO queue implementation
from collections import deque

class CPUEventQueue:
    def __init__(self, max_delay):
        self.queues = [deque() for _ in range(max_delay)]
    
    def push(self, spike_time, neuron_id, delay):
        self.queues[delay].append((spike_time + delay, neuron_id))
    
    def pop_due(self, current_time):
        # Return spikes with timestamp <= current_time
        pass
```

#### GPU
```python
# Ring buffer for small simulations
# Sparse data structures for large simulations
class GPURingBuffer:
    def __init__(self, capacity, max_neurons):
        self.buffer = torch.zeros(capacity, max_neurons)
        self.head = 0
        self.tail = 0
```

#### TPU
```python
# Sorting-based implementation leveraging TPU intrinsics
class TPUSortQueue:
    def process_events(self, events):
        # Use TPU-optimized sorting for event scheduling
        sorted_events = torch.sort(events)
        return sorted_events
```

## Applications
- **Large-scale brain simulation**: Efficient SNN training on commodity hardware
- **Neuromorphic ML**: Gradient-based learning for event-driven models
- **Cross-platform deployment**: Single codebase targeting multiple accelerators
- **Delayed synapse modeling**: Accurate temporal dynamics in recurrent networks

## Pitfalls
- **Memory pressure**: GPU performance degrades without sparse structures at scale
- **Queue design matters**: Wrong choice can negate accelerator benefits
- **Autograd framework limitations**: Current frameworks don't adapt primal/tangent structures

## Related Skills
- spikingjelly-framework
- snn-learning-survey
- snn-microcontroller-simulation
- yana-neuromorphic-simulation
