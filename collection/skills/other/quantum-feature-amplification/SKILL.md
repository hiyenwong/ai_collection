---
name: quantum-feature-amplification
description: >
  Quantum Feature Amplification Network (QFAN) methodology for autoregressive quantum generative modeling.
  Decouples quantum register size from output dimension using fixed-size quantum circuits combined with
  classical autoregressive decoding. Use when designing scalable quantum generative models for high-dimensional
  data, quantum ML for scientific simulations, or hybrid quantum-classical generative architectures.
  arXiv: 2605.16044
---

# Quantum Feature Amplification Network (QFAN)

## Overview
QFAN is an autoregressive quantum generative model that solves the scaling bottleneck of direct-register
quantum generative models, where output dimension is tied to quantum register size.

## Core Insight
Traditional quantum generative models require the quantum register to scale with the full image/data dimension,
making large-scale demonstrations infeasible. QFAN breaks this coupling by using:
1. A **fixed-size quantum circuit** that processes local feature patches
2. **Classical autoregressive decoding** that stitches patches into full outputs
3. **Quantum-classical handoff** at the feature level, not the pixel level

## Architecture

```
Input → Fixed Quantum Circuit (small register) → Feature Patch → Autoregressive Classical Decoder → Full Output
```

### Key Design Choices
- **Quantum register size**: Independent of output dimension
- **Autoregressive structure**: Each step conditions on previous outputs
- **Hybrid quantum-classical**: Quantum for feature extraction, classical for generation

## Advantages
1. **Scalability**: Handles high-dimensional data without proportional qubit increase
2. **Hardware-friendly**: Works on near-term quantum devices (NISQ)
3. **Scientific applications**: Suitable for detector-scale geometries in high-energy physics
4. **Generative quality**: Autoregressive structure captures complex correlations

## Application Domains
- Calorimeter shower simulation (high-energy physics)
- Medical image generation
- Molecular structure generation
- Scientific data synthesis

## Implementation Pattern
```python
# Conceptual architecture
class QFAN:
    def __init__(self, quantum_circuit_size, autoregressive_steps):
        self.quantum_circuit = FixedSizeQuantumCircuit(quantum_circuit_size)
        self.decoder = AutoregressiveDecoder(autoregressive_steps)

    def generate(self, latent):
        features = self.quantum_circuit.encode(latent)
        return self.decoder.autoregressive_decode(features)
```

## Comparison with Alternatives
| Approach | Register Scaling | Output Dimension | Hardware Demand |
|----------|-----------------|------------------|-----------------|
| Direct-register | Linear with output | Limited | High |
| Latent-variable hybrid | Partial reduction | Medium | Medium |
| **QFAN** | **Fixed** | **Unbounded** | **Low** |

## Pitfalls
- Autoregressive decoding introduces sequential bottleneck
- Quality depends on feature patch size and overlap
- Quantum circuit still needs sufficient expressivity per patch

## References
- arXiv: 2605.16044
- Related: [[qml-spiking-encoding]], [[quantum-neural-network-data-loading]]
