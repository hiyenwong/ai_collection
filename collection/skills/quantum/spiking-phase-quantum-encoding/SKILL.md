---
name: spiking-phase-quantum-encoding
description: >
  SPATE methodology for quantum machine learning — spiking-phase adaptive temporal encoding.
  Converts real-valued features into leaky integrate-and-fire spike trains and maps spike statistics
  to quantum rotations, augmented with temporal qubits via controlled phase operations.
  Use when: (1) designing QML pipelines for temporal data, (2) encoding time-series/tabular data
  into quantum feature spaces, (3) comparing spike-based vs angle/amplitude encoding quality,
  (4) building hybrid quantum neural networks under constrained qubit budgets, (5) evaluating
  quantum feature representation quality. Triggers: SPATE, spiking encoding quantum, temporal
  quantum encoding, spike-to-phase, quantum feature encoding, LIF quantum.
---

# SPATE: Spiking-Phase Adaptive Temporal Encoding for QML

## Overview

SPATE (arXiv:2604.11022) addresses a key limitation of QML: static encodings (angle, amplitude)
cannot handle temporal information. SPATE uses spike-based data representation to incorporate
temporal structure into quantum feature preparation.

## Core Pipeline

```
Real-valued features → LIF spike trains → Spike statistics → Quantum rotations + Temporal qubits → Quantum classifier
```

### Step 1: LIF Spike Train Generation

```python
def lif_spike_train(x, tau=1.0, threshold=1.0, dt=0.01, T=1.0):
    """Generate spike train from input using Leaky Integrate-and-Fire model."""
    spikes = []
    v = 0.0
    for t in range(int(T/dt)):
        v += (dt/tau) * (x - v)  # leaky integration
        if v >= threshold:
            spikes.append(t * dt)
            v = 0.0  # reset
    return spikes
```

### Step 2: Spike Statistics → Quantum Rotations

Extract spike count, inter-spike intervals, and phase information. Map to quantum rotations:

- **Spike count** → RY rotation angle: `θ = π × count / max_count`
- **Inter-spike interval** → RZ phase: `φ = 2π × ISI / T`
- **Phase locking** → RX rotation for temporal qubits

### Step 3: Temporal Qubits

Add controlled phase operations on dedicated temporal qubits:

```python
# For each temporal feature dimension
for i, (spike_times, phase) in enumerate(zip(spike_trains, phases)):
    circuit.ry(phase, qubit[i])
    if len(spike_times) > 1:
        circuit.cp(phase * 0.5, qubit[i], qubit[i+1])  # temporal entanglement
```

## Encoding Quality Evaluation Protocol

Use these metrics to compare encodings independently of the classifier:

| Metric | What it measures | Good range |
|--------|-----------------|------------|
| **CKTA** (Centered Kernel Target Alignment) | Feature alignment with labels | > 0.5 |
| **Fisher score** | Inter/intra-class separability | > 1.0 |
| **Silhouette score** | Cluster cohesion | > 0.3 |
| **Normalized entropy** | Feature informativeness | Low |
| **TV-pair collapse** | Representation collapse detection | < 0.1 |

## Performance Benchmarks

SPATE vs Angle encoding (from paper):

| Dataset | SPATE CKTA | Angle CKTA | SPATE Fisher | Angle Fisher |
|---------|-----------|-----------|-------------|-------------|
| Blobs | 0.966 | 0.632 | 7.37 | 0.70 |
| Moons | 0.506 | 0.015 | — | — |

Hybrid QNN results (fixed qubit budget):
- **Wine**: Accuracy 0.826, AUC 0.978
- **Moons**: Accuracy 0.840, AUC 0.923

## When to Use

- Time-series classification with quantum circuits
- Tabular data where temporal ordering matters
- Low qubit budget scenarios requiring efficient encoding
- When static encodings (angle/amplitude) underperform

## Pitfalls

- LIF parameters (tau, threshold) need tuning per dataset
- Spike train length trades off temporal resolution vs circuit depth
- Always evaluate encoding quality BEFORE training the classifier
