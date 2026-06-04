---
name: dual-memory-pathway-snn
description: "Dual Memory Pathway (DMP) neuromorphic network co-design methodology. Inspired by cortical fast-slow organization, combines explicit slow memory with fast spiking activity for long-timescale context. Applies to: neuromorphic computing, event-driven sensing, energy-efficient SNN deployment. Activation: dual memory pathway, neuromorphic co-design, fast-slow SNN, near-memory compute, cortical memory."
---

# Dual Memory Pathway (DMP) Neuromorphic Networks

> Algorithm-hardware co-design combining biological fast-slow cortical organization with neuromorphic hardware optimization for energy-efficient long-timescale computation.

## Metadata
- **Source**: arXiv:2512.07602
- **Authors**: Pengfei Sun, Zhe Su, Jascha Achterberg, Giacomo Indiveri, Dan F.M. Goodman, Danyal Akarca
- **Published**: 2025-12-08 (v2: 2025-12-11)

## Core Methodology

### Key Innovation
The DMP architecture introduces an explicit **slow memory pathway** alongside fast spiking activity, inspired by cortical fast-slow organization. Each layer maintains a compact low-dimensional state summarizing recent activity that modulates spiking dynamics.

### Algorithm Level
1. **Dual Memory Structure**: Each layer has two pathways:
   - **Fast pathway**: Standard spiking activity (event-driven, sparse)
   - **Slow pathway**: Compact state vector tracking long-timescale context
2. **Memory Modulation**: Slow pathway state modulates fast spiking dynamics
3. **Learning Stabilization**: Explicit memory stabilizes training while preserving sparsity
4. **Parameter Efficiency**: 40-60% fewer parameters than equivalent SOTA SNNs

### Hardware Level
1. **Near-Memory-Compute Architecture**: Retains compact shared state while optimizing dataflow
2. **Heterogeneous Dataflow**: Optimized for both sparse-spike and dense-memory pathways
3. **Throughput Improvement**: 4x increase over state-of-the-art implementations
4. **Energy Efficiency**: 5x improvement in energy efficiency

## Technical Framework

### DMP Layer Structure
```
For each layer l:
  Fast state: s_l(t) = spike_activation(input, weights, slow_state)
  Slow state: m_l(t+1) = α·m_l(t) + (1-α)·aggregate(s_l(t))
  Output: modulated_spike(s_l(t), m_l(t))
```

Where:
- α is the memory decay factor (slow timescale)
- aggregate() summarizes fast activity into slow state
- modulation() combines fast and slow pathways

### Implementation Steps
1. Define DMP layer with dual pathway structure
2. Implement slow state update with configurable timescale
3. Design modulation mechanism (multiplicative, additive, or gating)
4. Co-design hardware dataflow for heterogeneous pathways
5. Train with standard SNN surrogate gradient + memory regularization

## Applications
- Event-based vision sensors with long-timescale context
- Neuromorphic edge computing for autonomous systems
- Low-power IoT sensing with temporal memory
- Real-time neuromorphic computation and learning

## Pitfalls
- Memory decay factor α must be tuned per task
- Hardware co-design requires specialized architecture knowledge
- Slow pathway introduces additional compute overhead
- Not suitable for purely feedforward, single-pass inference

## Related Skills
- dual-timescale-memory-spiking-neuron-astrocyte
- snn-universal-approximation-theory
- snn-edge-intelligence-survey
- physical-foundation-models
