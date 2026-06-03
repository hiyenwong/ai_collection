---
name: covert-quantum-computing
description: >
  Covert quantum computing methodology for multi-tenant quantum cloud platforms.
  Ensures computation privacy against adversaries sharing the same quantum processing unit
  using information-theoretic covertness analysis. Use when: designing secure quantum cloud
  architectures, analyzing multi-tenant QCU privacy, studying quantum crosstalk side channels,
  implementing covert quantum communication, evaluating spatial isolation for quantum processors,
  or analyzing qubit layout security properties.
  Activation: covert quantum computing, quantum cloud security, quantum privacy,
  multi-tenant quantum, quantum crosstalk, quantum side channel, quantum covertness,
  QCU security, quantum isolation.
---

# Covert Quantum Computing

Methodology from arXiv:2605.14325 — "Toward Covert Quantum Computing" (Anderson, Datta, Bash, 2026).

## Core Concept

Covert quantum computing ensures that an adversary with access to all other quantum computational
units (QCUs) of a shared quantum computer **cannot detect** computation on the subset they cannot
access. Unlike covert communication (where the adversary observes a shared channel), here the
adversary controls the systems used for detection.

## Analysis Framework

### Quantum-Strategy Framework

Use the quantum-strategy framework from quantum game theory and memory channel discrimination:

1. Model adversary as having quantum memory and adaptive operations
2. Analyze detection probability using quantum hypothesis testing
3. Account for adaptive measurements across multiple rounds

### Discrete Isoperimetric Inequalities

For planar graph circuit layouts with nearest-neighbor crosstalk model:

- **n-qubit circuit**: Only O(√n) border qubits provide detection information to adversary
- **Scaling law**: Covertness improves as √n / n → 0 for large circuits
- **Implication**: Larger quantum processors naturally provide better covertness

### Crosstalk Analysis

Two types of crosstalk channels to analyze:

1. **Nearest-neighbor crosstalk**: Expected, border-limited — consistent with isoperimetric bound
2. **Long-range coupling**: Induced by leakage from drive/control lines — reveals side channel
   beyond border qubits, degrading covertness and co-tenant circuit fidelity

## Verification Steps

### Ramsey Experiment Protocol

To detect crosstalk on qubits not used in computation:

```python
# 1. Initialize border qubits in |+⟩ state
# 2. Run computation on interior qubits
# 3. Measure border qubits for phase shifts
# 4. Repeat to statistically detect deviations
```

### Covertness Metrics

- **Detection probability**: P_detect < ε for chosen covertness parameter ε
- **Crosstalk magnitude**: Measure Ramsey fringe shifts on idle qubits
- **Spatial decay**: Verify crosstalk falls off with distance from compute qubits

## Key Findings

- IBM Heron 2 (156-qubit) and IQM Emerald (54-qubit) show both nearest-neighbor AND
  long-range crosstalk — long-range coupling is the practical bottleneck for covertness
- Drive/control line leakage hypothesis: spatial isolation alone is insufficient
- Co-tenants exposed to both adversarial AND unintended crosstalk degradation

## When to Apply

- Designing quantum cloud platform security architecture
- Evaluating multi-tenant quantum computing isolation guarantees
- Analyzing spatial layout optimization for quantum processors
- Assessing crosstalk as a security vulnerability in quantum hardware
- Building quantum information-theoretic security protocols
