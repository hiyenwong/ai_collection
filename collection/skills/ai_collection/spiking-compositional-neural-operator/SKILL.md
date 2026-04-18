---
name: spiking-compositional-neural-operator
description: >
  Spiking Compositional Neural Operator (SCNO) - modular neural operator framework
  combining spiking neural networks with compositional architecture for PDE solving
  and dynamical system modeling. Uses event-driven computation for energy-efficient
  operator learning with modular composition of sub-operators.
  Activation: neural operator, spiking neural network, PDE solver, compositional model,
  energy-efficient ML, dynamical systems, 脉冲神经算子, 组合神经算子
version: 1.0.0
metadata:
  hermes:
    source_paper: "SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic PDE Solver"
    arxiv_id: "2604.11625"
    tags: [snn, neural-operator, pde, compositional, energy-efficient, neuromorphic]
---

# Spiking Compositional Neural Operator (SCNO)

## Overview

Combines spiking neural networks with compositional neural operators for energy-efficient PDE solving. SCNO decomposes complex operators into modular sub-operators, each implemented as an SNN, enabling both compositionality and event-driven computation.

## Architecture

### Compositional Decomposition
```
F(u) = F_n ∘ F_{n-1} ∘ ... ∘ F_1(u)
```
Each sub-operator F_i handles a specific transformation:
- Fourier Neural Operator block (frequency domain)
- Graph Neural Operator block (spatial relationships)
- Local operator block (pointwise nonlinearities)

### Spiking Implementation
```python
class SpikingNeuralOperator:
    def __init__(self, sub_operators):
        self.sub_ops = nn.ModuleList(sub_operators)
    
    def forward(self, x):
        # Each sub-op is a spiking module
        spikes = x
        for op in self.sub_ops:
            spikes = op(spikes)  # event-driven computation
        return spikes
```

## Key Innovations

1. **Modular Composition**: Sub-operators can be reused across different PDEs
2. **Event-Driven Computation**: SNN neurons only fire when needed → energy savings
3. **Resolution Invariance**: Works on different spatial/temporal discretizations
4. **Neuromorphic Deployment**: Compatible with Loihi, SpiNNaker, BrainChip

## Training Strategy

- Train sub-operators independently on simple PDEs
- Compose for complex PDEs (transfer learning)
- Surrogate gradient descent for spiking backprop

## Performance Characteristics

- 10-100x energy reduction vs. dense neural operators
- Comparable accuracy to FNO/GeoFNO
- Scales to high-dimensional PDEs
- Real-time inference on neuromorphic hardware

## Applications

- Fluid dynamics simulation
- Weather prediction
- Real-time physics engines
- Scientific computing on edge devices

## Related Skills

- spiking-neural-network-analysis, physics-guided-neural-networks
