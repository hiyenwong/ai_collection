---
name: coherent-quantum-inference
description: >
  Methodology for coherent quantum inference — preserving quantum coherence during
  data processing to achieve exponentially lower sample complexity than incoherent
  (measurement-mediated) protocols. Use when: (1) designing quantum data processing
  pipelines, (2) comparing coherent vs incoherent quantum learning, (3) optimizing
  sample complexity in quantum ML, (4) implementing quantum purity amplification (QPA),
  mixed-state purification, or density matrix exponentiation, (5) analyzing
  coherent-incoherent separations in quantum algorithms.
  Keywords: quantum inference, sample complexity, coherent processing, purity amplification,
  entanglement-breaking limit, quantum learning, quantum statistics.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Coherent Quantum Inference

Methodology from arXiv:2605.21457 (Li, Theil, Harrow, Chuang, May 2026).

## Core Insight

**Coherent quantum inference** — where the desired output remains quantum (preserving
coherence) — achieves exponentially lower sample complexity than incoherent protocols
that first measure quantum data then process classically.

### Sample Complexity Separation

For quantum purity amplification (QPA) with principal eigenstate targets and d-dimensional inputs:

- **Coherent processing**: O(d/ε) copies for error ε
- **Incoherent processing**: O(d²/ε²) copies
- **Separation**: exponential in sample complexity

## Key Concepts

### 1. Coherent vs Incoherent Protocols

| Property | Coherent | Incoherent |
|----------|----------|------------|
| Output type | Quantum | Classical |
| Measurement | None before output | Immediate |
| Sample complexity | Lower (e.g., O(d/ε)) | Higher (e.g., O(d²/ε²)) |
| Coherence preserved | Yes | No |

### 2. Applications

- **Quantum Purity Amplification (QPA)**: Amplify dominant eigenstate of mixed state
- **Mixed-state Approximate Purification/Cloning**
- **Density Matrix Exponentiation**: e^{iρt} from copies of ρ
- **Quantum State Tomography** (coherent variant)

### 3. Entanglement-Breaking Limit

Each coherent protocol has an optimal incoherent counterpart defined by the
entanglement-breaking limit. Use this to:
- Benchmark coherent advantage
- Identify when coherence is necessary
- Design hybrid protocols

## When to Use Coherent Inference

1. **Sample-limited regime**: When quantum data is expensive to prepare
2. **High-dimensional states**: Advantage scales with dimension d
3. **Precision-critical tasks**: Error ε matters for both protocols
4. **Downstream quantum processing**: Output feeds into quantum circuit

## Decision Framework

```
Is the downstream task quantum?
├── Yes → Use coherent processing
│   ├── Need exact output? → Full coherent pipeline
│   └── Approximate ok? → Coherent with early truncation
└── No → Incoherent may suffice
    ├── High-dimensional input? → Check if coherent→measure helps
    └── Low-dimensional? → Incoherent is optimal
```

## Practical Considerations

- **Coherence time**: Coherent protocols require longer quantum memory
- **Error accumulation**: Coherent processing propagates errors differently
- **Hardware constraints**: Near-term devices may force incoherent trade-offs
- **Noise sensitivity**: See arXiv:2605.21346 for noisy-qubit performance analysis

## Related Work

- **Quantum ML advantage with noisy qubits**: arXiv:2605.21346 (30-40 qubits,
  coherent vs fixed-measurement comparison)
- **Device-independent randomness**: arXiv:2605.21293 (robustness to noisy signaling)

## Activation Keywords

coherent quantum inference, sample complexity, quantum purity amplification,
quantum cloning, density matrix exponentiation, entanglement-breaking,
quantum data processing, quantum advantage, quantum statistics
