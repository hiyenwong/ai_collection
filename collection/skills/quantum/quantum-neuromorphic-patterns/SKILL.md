---
name: quantum-neuromorphic-patterns
description: >
  Quantum neuromorphic computing patterns — combining quantum computing with brain-inspired neural architectures.
  Covers quantum brain modeling, quantum reservoir computing for neural dynamics, brain-inspired quantum neural architectures,
  spiking-phase quantum encoding, and quantum-inspired cognitive models.
  Use when designing quantum systems for neuroscience applications, brain-inspired quantum algorithms,
  or quantum-enhanced neural network architectures.
  Trigger: quantum neuromorphic, quantum brain, brain-inspired quantum, quantum reservoir computing neural,
  spiking quantum, quantum cognitive modeling, 量子神经形态, 量子脑模型.
---

# Quantum Neuromorphic Computing Patterns

## Overview

The intersection of quantum computing and neuroscience creates unique research patterns:
quantum systems modeling brain dynamics, brain-inspired quantum algorithms, and
neuromorphic architectures enhanced by quantum effects.

## Core Patterns

### Pattern 1: Brain-Inspired Quantum Neural Architectures

Map biological neural structures to quantum circuits:
- Use quantum entanglement to model neural synchronization
- Implement Hebbian-like learning through variational quantum circuits
- Model neural oscillations with quantum phase dynamics

### Pattern 2: Quantum Reservoir Computing for Neural Dynamics

Use quantum systems as reservoirs for processing temporal neural signals:
- Quantum reservoir states encode neural activity patterns
- Classical readout layer extracts predictions
- Suitable for EEG/MEG time-series analysis and brain-computer interfaces

### Pattern 3: Spiking-Phase Quantum Encoding (SPATE)

Encode spiking neural activity into quantum states via phase representation:
- Map spike timing to quantum phase angles
- Use quantum superposition for spike train compression
- Enable quantum machine learning on neuromorphic data

### Pattern 4: Quantum Cognitive Modeling

Model cognitive processes using quantum probability formalism:
- Contextuality captures order effects in decision making
- Quantum interference models cognitive biases
- Hilbert space representations for concept combination

## Implementation Guidelines

### Quantum Brain Model Construction

1. **Identify neural phenomenon** (synchronization, plasticity, oscillation)
2. **Map to quantum formalism** (qubits → neurons, entanglement → correlations)
3. **Choose ansatz** (hardware-efficient for NISQ, problem-inspired for simulation)
4. **Define cost function** (match observed neural statistics)
5. **Validate** against classical neural network baselines

### Quantum Reservoir for Neural Signals

```python
# Conceptual workflow
neural_signal → quantum_feature_map → quantum_reservoir → classical_readout → prediction
```

- Use parameterized quantum circuits as feature maps
- Quantum reservoir processes temporal correlations
- Classical linear readout is trained on reservoir outputs

## When to Use

- Modeling quantum effects in biological neural systems
- Quantum-enhanced analysis of neural time-series data
- Brain-inspired quantum algorithm design
- Quantum machine learning on neuromorphic hardware
- Cognitive science research with quantum probability models

## Key Findings from Literature

- Quantum-like dynamics observed in human brain activity patterns
- Brain-inspired quantum architectures improve pattern recognition
- Quantum reservoir computing efficiently processes neural time-series
- Spiking-phase encoding enables efficient quantum-neuromorphic data loading
- Three-layer quantum brain models show computational advantages

## Related Skills

- **quantum-neuroscience-analysis**: Quantum methods for neuroscience
- **spiking-neural-network-analysis**: SNN methodology
- **quantum-reservoir-computing**: QRC framework
- **quantum-cognition**: Quantum cognitive modeling

## Paper References

- Brain-Inspired Quantum Neural Architectures (arXiv: various)
- Quantum Reservoir Computing for neural dynamics
- SPATE: Spiking-Phase Adaptive Temporal Encoding (arXiv: 2605.xxxx)
- Dynamic Synaptic Modulation in Bio-Inspired Quantum Neural Networks
- Leggett-Garg Tests in Neural Dynamics (quant-ph)
