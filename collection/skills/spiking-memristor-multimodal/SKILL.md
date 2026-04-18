---
name: spiking-memristor-multimodal
description: "Rapid progress of artificial neural network applications in recent years has led to the issue of an unprecedented energy consumption. It can be solved by the implementation of ener... Activation: spiking neural network, neuromorphic, memristor"
---

# Multiple spiking functionalities in annealing-optimized Ag/Hf$_{0.5}$Zr$_{0.5}$O$_2$-based memristive neurons

## Overview

Rapid progress of artificial neural network applications in recent years has led to the issue of an unprecedented energy consumption. It can be solved by the implementation of energy efficient hardware based on non-von-Neumann architectures, which requires the development of electronic components emulating the behavior of synapses and neurons. While research of synaptic elements is vast, the technology for fabrication of scalable and highly reproducible neuronal elements is far less developed. In this paper, we demonstrate an artificial neuron with multiple functionalities based on filamentary switching Ag/Hf$_{0.5}$Zr$_{0.5}$O$_2$ (HZO) memristors. To improve the parameters of memristors, we propose a two-step annealing method, which allows for better control of the crystallization of the

## Source Paper

- **Title**: Multiple spiking functionalities in annealing-optimized Ag/Hf$_{0.5}$Zr$_{0.5}$O$_2$-based memristive neurons
- **Authors**: Nikita Zhidkov, Andrei Zenkevich, Anton Khanas
- **arXiv**: [2604.11780v1](https://arxiv.org/pdf/2604.11780v1)
- **Published**: 2026-04-13
- **Categories**: cond-mat.mtrl-sci, physics.app-ph
- **PDF**: [2604.11780v1](https://arxiv.org/pdf/2604.11780v1)

## Core Concepts

### Key Contributions

1. Rapid progress of artificial neural network applications in recent years has led to the issue of an unprecedented energy consumption.

2. It can be solved by the implementation of energy efficient hardware based on non-von-Neumann architectures, which requires the development of electronic components emulating the behavior of synapses and neurons.

3. While research of synaptic elements is vast, the technology for fabrication of scalable and highly reproducible neuronal elements is far less developed.

4. In this paper, we demonstrate an artificial neuron with multiple functionalities based on filamentary switching Ag/Hf$_{0.5}$Zr$_{0.5}$O$_2$ (HZO) memristors.

## Practical Applications

### Neuromorphic Hardware
- Implement multi-functionality spiking neurons on memristive devices
- Use annealing optimization for device parameter tuning
- Support multiple encoding modes: TTFS, spike count, firing rate

### Memristive Neuron Design

```python
class MemristiveNeuron:
    def __init__(self):
        self.threshold = 1.0
        self.refractory = 0
    
    def encode_ttfs(self, current_input):
        # Time-to-first-spike encoding
        for t in range(1000):
            if self._membrane_potential(current_input) > self.threshold:
                return t * 0.001  # seconds
        return None
    
    def encode_spike_count(self, current_input, duration=1.0):
        # Spike count encoding
        count = 0
        for t in range(int(duration / 0.001)):
            if self._membrane_potential(current_input) > self.threshold:
                count += 1
        return count
    
    def _membrane_potential(self, current_input):
        return current_input * 0.1  # simplified
```

## Implementation Steps

1. **Understand the core methodology** - Read the paper's method section carefully
2. **Reproduce baseline results** - Start with the paper's reported experiments
3. **Adapt to your domain** - Modify parameters for your specific use case
4. **Evaluate and iterate** - Compare against baselines, measure improvement

## Limitations

- Paper-specific limitations should be verified against full text
- Implementation details may require access to supplementary materials
- Hardware requirements vary by application scale

## Related Work


## Activation Keywords

- spiking neural network, neuromorphic, memristor
