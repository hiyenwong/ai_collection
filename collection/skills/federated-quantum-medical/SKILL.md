---
name: federated-quantum-medical
description: >
  Federated quantum learning methodology for privacy-preserving medical diagnosis.
  Combines federated learning (FL) with quantum neural networks (QNN) for early disease
  detection without sharing sensitive patient data across institutions.
  Use when: building privacy-preserving medical AI, federated quantum learning,
  cross-institutional medical data collaboration, early disease detection with quantum models,
  diabetic retinopathy detection, medical image privacy, FQPDR methodology,
  quantum federated learning, healthcare data privacy, distributed quantum medical AI.
---

# Federated Quantum Medical Diagnosis

## Core Pattern

Combine federated learning with quantum neural networks for privacy-preserving medical diagnosis across multiple institutions without sharing raw patient data.

## Key Paper

**FQPDR** (arXiv:2605.08324v1): Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy

## Architecture

```
Hospital A ──┐
Hospital B ──┼── Federated Aggregator ── QNN ── Diagnosis
Hospital C ──┘
```

## Implementation Steps

1. Each institution trains QNN on local medical images
2. Only model weights sent to central aggregator (no raw data)
3. Combine weights using FedAvg or quantum-aware aggregation
4. Distribute updated global model back to all institutions
5. Iterate until convergence

## Key Technical Decisions

- **Quantum Encoder**: Amplitude or angle encoding for medical images
- **Variational Layer**: Parameterized quantum circuit with trainable rotation gates
- **Measurement**: Pauli-Z expectation values as classical output
- **Privacy**: Add differential privacy via noise injection during weight sharing

## Pitfalls

- Communication overhead: Quantum model parameters can be large
- Non-IID data: Medical data across hospitals has different distributions
- Quantum noise: NISQ-era noise affects local training
- Barren plateaus: Use layer-wise training for QNN convergence
