---
name: cortico-cerebellar-modular-rnn
description: "Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning — CB-RNN architecture showing cerebellar-inspired feedforward modules drive learning efficiency while cortical recurrent cores act as fixed reservoirs."
---

# Cortico-Cerebellar Modular RNN (CB-RNN)

Based on: Voce, Giannakakis & Clopath (2026) "Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning" — arXiv:2605.10356v1

## Core Problem

How do the cerebellum and cerebral cortex interact to support flexible and efficient temporal processing? Can this biological architecture benefit artificial systems?

## Key Discovery

**Heterogeneous modular architectures** (cortical recurrent core + cerebellar feedforward module) act as powerful structural inductive biases, enabling:
- Faster learning convergence
- Higher maximum performance
- Efficient knowledge transfer

## CB-RNN Architecture

### Cortical Core (Recurrent Network)

- **Role**: Fixed reservoir for temporal feature extraction
- **Property**: Can be frozen after minimal training
- **Function**: Provides rich temporal representations
- **Biological basis**: Cerebral cortex dynamics

### Cerebellar Module (Feedforward)

- **Role**: Primary driver of learning efficiency
- **Property**: Adapts rapidly to new tasks
- **Function**: Fine-tunes outputs from cortical features
- **Biological basis**: Cerebellar supervised learning

### Key Finding: Freezing Strategy

```
Phase 1: Train both core + module (minimal training)
Phase 2: Freeze cortical core
Phase 3: Delegate all learning to cerebellar module
Result: Superior efficiency + performance preserved
```

## Mechanisms

### 1. Division of Labor

- **Cortex**: Slow, stable temporal representations
- **Cerebellum**: Fast, adaptive output refinement
- **Together**: Efficient learning with stable foundations

### 2. Inductive Bias Benefits

- **Faster convergence**: Cerebellar module learns quickly
- **Higher performance**: Outperforms parameter-matched baselines
- **Robustness**: Frozen core prevents catastrophic forgetting

### 3. Architectural Efficiency

- **Parameter efficiency**: Same parameter count, better performance
- **Training efficiency**: Faster convergence across task difficulties
- **Transfer efficiency**: Frozen core enables rapid task switching

## Comparison with Standard RNNs

| Property | Standard RNN | CB-RNN |
|----------|--------------|--------|
| Learning speed | Baseline | **Faster** |
| Max performance | Baseline | **Higher** |
| Parameter efficiency | Standard | **Superior** |
| Task transfer | Poor | **Excellent** |
| Biological plausibility | Low | **High** |

## Applications

1. **Temporal sequence learning**: Speech, music, time series
2. **Motor control**: Robotics, prosthetics
3. **Continuous learning**: Sequential task domains
4. **Neuromorphic computing**: Brain-inspired hardware

## Design Principles

1. **Heterogeneous modularity**: Different modules for different functions
2. **Core-periphery architecture**: Stable core + adaptive periphery
3. **Biological inspiration**: Architecture grounded in brain organization
4. **Freezing strategy**: Strategic parameter freezing for efficiency

## Implementation Hints

```python
class CB_RNN:
    def __init__(self, core_size, module_size):
        # Cortical core: recurrent, can be frozen
        self.cortical_core = RNNCell(core_size)
        # Cerebellar module: feedforward, adapts rapidly
        self.cerebellar_module = FeedforwardNet(module_size)
    
    def train_phase1(self, data, epochs=5):
        # Train both together briefly
        train(self.cortical_core, self.cerebellar_module, data, epochs)
    
    def train_phase2(self, data):
        # Freeze core, only train module
        freeze(self.cortical_core)
        train(self.cerebellar_module, data)
    
    def forward(self, x):
        core_features = self.cortical_core(x)
        output = self.cerebellar_module(core_features)
        return output
```

## Research Gaps

1. Optimal core-to-module size ratios for different tasks
2. Extension to multi-layer cerebellar architectures
3. Integration with attention mechanisms
4. Application to large-scale language models
5. Hardware implementation efficiency

## Related Skills

- hierarchical-control-abstraction
- modular-memristor-synaptic-plasticity
- dual-timescale-memory-astrocyte
- working-memory-heterogeneous-delays
- mpcs-neuroplastic-continual-learning

## Activation Keywords

cortico-cerebellar, CB-RNN, cerebellar module, cortical core, temporal learning, modular architecture, inductive bias, recurrent neural network, feedforward module, freezing strategy, reservoir computing, biological architecture