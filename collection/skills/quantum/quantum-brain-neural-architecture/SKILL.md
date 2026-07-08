---
name: quantum-brain-neural-architecture
description: >
  Design and implement brain-inspired quantum neural architectures combining
  Quantum Spiking Neural Networks (QSNN) and Quantum Long Short-Term Memory
  (QLSTM) for pattern recognition, anomaly detection, and temporal sequence
  modeling. Use when the user asks about quantum neural networks, quantum-spiking
  hybrids, brain-inspired quantum models, QSNN, QLSTM, quantum anomaly detection,
  or quantum memory architectures for ML tasks.
---

# Quantum-Brain Neural Architecture

## Overview

Combine Quantum Spiking Neural Networks (QSNN) and Quantum Long Short-Term Memory
(QLSTM) into a two-stage architecture inspired by brain information processing:

- **Stage 1 (Hypothalamus-like)**: QSNN performs sensory-level filtering — removes
  noisy/infrequent events while strengthening spatio-temporal correlations.
- **Stage 2 (Hippocampus-like)**: QLSTM processes filtered information, captures
  correlated patterns, and converts short-term to long-term memory storage.

This architecture excels at anomaly detection on imbalanced or low-quality data,
where classical models and standard QNNs struggle.

## Architecture Components

### Stage 1: QSNN (Sensory Filtering)

```
Input data → QSNN encoder → Spike encoding → Quantum variational circuit → Filtered features
```

- Encode input features as spike trains (temporal encoding)
- Apply parameterized quantum gates for spike propagation
- QSNN naturally filters noise: infrequent spikes have low firing probability
- Output: strengthened signals with high space-time correlation

### Stage 2: QLSTM (Memory Processing)

```
Filtered features → QLSTM cell → Gate operations (forget/input/output) → Memory state → Prediction
```

- QLSTM gates implemented via parameterized quantum circuits
- Cell state acts as quantum memory register
- Preserves both temporal and spatial information
- Handles long-range dependencies better than classical LSTM

### Full Pipeline

```
Raw Data → QSNN (filter) → QLSTM (memorize) → Quantum measurement → Classical post-processing → Output
```

## Implementation Guidelines

### Key Design Principles

1. **Two-stage separation**: Keep QSNN and QLSTM as distinct modules — the filtering
   stage improves QLSTM input quality significantly
2. **Temporal encoding**: Use time-to-first-spike or rank-order encoding for QSNN
3. **Variational circuits**: Use hardware-efficient ansatz (RY/RZ rotations + CZ entangling)
4. **Hybrid training**: Classical optimizer (Adam/COBYLA) with quantum circuit evaluation
5. **Measurement strategy**: Use Pauli-Z expectation values as output features

### Quantum Circuit Design

```python
# QSNN variational layer pattern
for layer in range(depth):
    RY(params[0], qubit) for each qubit
    RZ(params[1], qubit) for each qubit
    CZ entangling (linear or all-to-all topology)

# QLSTM gate circuits (one per gate: forget, input, cell, output)
def qlstm_gate(input_state, hidden_state, params):
    # Concatenate inputs
    # Apply variational circuit
    # Measure expectation values
    # Apply classical activation (sigmoid/tanh)
    return gate_output
```

### Training Strategy

1. Pre-train QSNN on feature extraction task
2. Freeze QSNN, train QLSTM on memorization
3. Fine-tune both stages jointly
4. Use cross-entropy + focal loss for imbalanced datasets

## When to Use

| Scenario | Why this architecture |
|----------|----------------------|
| Fraud/anomaly detection | QSNN filters noise, QLSTM captures rare patterns |
| Imbalanced datasets | Quantum models find patterns classical models miss |
| Low-quality/limited data | Quantum advantage with fewer parameters |
| Temporal sequence tasks | QLSTM preserves long-range temporal dependencies |
| Brain-inspired AI research | Directly models hypothalamus-hippocampus pathway |

## Related Papers in Knowledge Graph

- `[25]` Brain-Inspired Quantum Neural Architectures (QSNN+QLSTM)
- `[26]` Quantum-Brain: Vision-Brain Understanding with Entanglement
- `[28]` Brain-Inspired Paradigm for Scalable Quantum Vision
- `[32]` Transforming NNs into Neuromorphic Quantum Models
- `[23]` Digital Quantum Magnetism on Trapped-Ion Computer
- `[1]` Early Fault Tolerant Neutral Atoms Systems

## Pitfalls

- **Barren plateaus**: Use shallow circuits (<10 layers) and layer-wise training
- **Shot noise**: Increase measurement shots (1024+) for stable gradients
- **Data encoding**: Poor encoding negates quantum advantage — use amplitude or
  angle encoding appropriate to data structure
- **Classical baseline**: Always compare against classical LSTM/QNN baselines
  to verify quantum benefit

## Tools & Frameworks

- **PennyLane**: Quantum circuit differentiation and training
- **Qiskit**: IBM quantum hardware access
- **SpikingJelly**: Classical SNN simulation for hybrid comparison
- **PyTorch**: Classical post-processing and training loop integration

## Key Papers

See [references/key-papers-2026-05.md](references/key-papers-2026-05.md) for
detailed summaries of 8 papers at the quantum × neuroscience intersection.
