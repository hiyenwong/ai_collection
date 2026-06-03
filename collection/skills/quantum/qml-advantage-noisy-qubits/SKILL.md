---
name: qml-advantage-noisy-qubits
description: >
  Methodology for demonstrating quantum ML advantage with tens of noisy qubits.
  Use when: (1) evaluating quantum advantage in machine learning tasks, (2) comparing
  coherent quantum processing vs fixed-measurement schemes, (3) designing near-term
  quantum ML experiments on NISQ devices, (4) analyzing data acquisition bottlenecks
  in quantum learning, (5) hardware-aware quantum algorithm design.
  Keywords: quantum ML advantage, noisy qubits, coherent processing, fixed-measurement,
  quantum learning, data acquisition bottleneck, NISQ, quantum simulation.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Quantum ML Advantage with Noisy Qubits

Methodology from arXiv:2605.21346 (Danaci, Patel, Molteni, van Nieuwenburg, Dunjko, Krzywda, May 2026).

## Core Finding

**Coherent quantum processing** of quantum data outperforms **fixed-measurement + classical
processing** schemes even at the scale of just 30-40 noisy qubits.

### Key Results

- Performance separation persists under realistic noise
- At 30-40 qubits, bottleneck shifts from classical computation to **data acquisition**
- Matching coherent protocol with measure-first would require **months to years** of measurements

## Experimental Evaluation Framework

### Hardware Constraints to Evaluate

1. **State preparation fidelity** — initial state quality
2. **Gate errors** — two-qubit gate error rates
3. **Readout errors** — measurement fidelity
4. **Connectivity** — qubit coupling topology
5. **Coherence times** — T1, T2 limits

### Comparison Protocol

```
Coherent Protocol:
  quantum_data → coherent_processing → quantum_output → measurement

Fixed-Measurement Protocol:
  quantum_data → measurement → classical_data → classical_processing → output
```

## When Quantum Advantage Emerges

| Factor | Favors Coherent | Favors Incoherent |
|--------|----------------|-------------------|
| Data cost | High (coherent wins) | Low |
| Qubit count | > 30 | < 30 |
| Noise level | Moderate (advantage persists) | Extreme |
| Problem type | Quantum data learning | Classical data |

## Practical Implications

- Near-term quantum advantage is **accessible on current devices**
- Focus on **data acquisition efficiency** rather than just gate fidelity
- Coherent processing advantage is **statistical** — measurable with fewer samples

## Related Work

- Coherent quantum inference: arXiv:2605.21457 (sample complexity theory)
- Device-independent randomness: arXiv:2605.21293 (noise robustness)

## Activation Keywords

quantum ML advantage, noisy qubits, coherent vs measurement, quantum learning advantage,
NISQ quantum advantage, data acquisition bottleneck, quantum simulation, quantum data processing
