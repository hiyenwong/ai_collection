---
name: amplitude-encoding-qrnn
description: "Amplitude encoding methodology for Quantum Recurrent Neural Networks (QRNNs) — EnQode approximate amplitude encoding + magnitude augmentation + circuit depth reduction for time series forecasting. Activation: qrnn, quantum recurrent, amplitude encoding, quantum time series, EnQode, quantum sequence model."
---

# Amplitude Encoding for Quantum Recurrent Neural Networks (QRNNs)

**Source**: arXiv:2508.16784v3 (2026-06-02 revision)
**Authors**: Jack Morgan, Hamed Mohammadbagherpoor, Eric Ghysels

## Problem

Quantum Recurrent Neural Networks (QRNNs) encode temporal data into quantum states that are periodically fed into a quantum circuit. Prior QRNN work predominantly used **angle encoding**, leaving **amplitude encoding** underexplored due to:

1. **High computational complexity** of amplitude encoding preparation
2. **Information loss** — amplitude encoding loses magnitude information during normalization
3. **Circuit depth overhead** — original QRNN architectures have unnecessary depth

## Methodology

### 1. EnQode Approximate Amplitude Encoding

Replace exact amplitude encoding (O(2^n) gates) with **EnQode** — a recently introduced method for approximate amplitude encoding that:
- Uses polynomial-depth circuits instead of exponential
- Achieves near-exact state preparation with bounded error
- Enables scaling to larger input dimensions

### 2. Magnitude Augmentation Pre-processing

**Key insight**: amplitude encoding normalizes input vectors to unit norm, losing magnitude information. The paper proposes augmenting amplitude-encoded inputs with their pre-normalized magnitudes:

```
x_raw → [amplitude_encode(x_raw), ||x_raw||] → QRNN circuit
```

This simple pre-processing technique:
- Restores lost magnitude information
- Improves generalization on real-world datasets
- Adds minimal overhead (single scalar per input)

### 3. Circuit Depth Reduction Architecture

The paper introduces a **mathematically equivalent circuit architecture** that achieves substantial reduction in circuit depth:

- Original QRNN: sequential application of unitary transformations
- Reduced QRNN: equivalent transformation with parallelized gate structure
- Result: fewer quantum gates → lower noise accumulation → better results on NISQ hardware

## Implementation Pattern

```python
import numpy as np

def prepare_amplitude_encoded_input(x):
    """Augment amplitude-encoded input with magnitude."""
    magnitude = np.linalg.norm(x)
    # EnQode approximate amplitude encoding
    normalized = x / (magnitude + 1e-10)
    return normalized, magnitude

def qrnn_step(hidden_state, input_augmented, params):
    """QRNN recurrent step with augmented amplitude input."""
    encoded_input, magnitude = input_augmented
    # Apply reduced-depth QRNN circuit
    # [circuit implementation depends on quantum framework]
    return new_hidden_state, output
```

## When to Use

- **Time series forecasting** with quantum circuits
- **Sequential data** where angle encoding is suboptimal
- **NISQ-era quantum hardware** where circuit depth matters
- **Medical/financial time series** (validated on real-world datasets)
- Any QRNN application where encoding strategy is a bottleneck

## Key Findings

| Aspect | Angle Encoding | Amplitude Encoding (this work) |
|--------|---------------|-------------------------------|
| State capacity | O(n) qubits for n features | O(log n) qubits for n features |
| Circuit depth | Moderate | Reduced with new architecture |
| Magnitude info | Preserved | Recovered via augmentation |
| NISQ suitability | Good | Improved with depth reduction |

## Pitfalls

- **Amplitude encoding is approximate** — EnQode introduces bounded error; verify error tolerance for your use case
- **Magnitude augmentation adds one scalar** — must be handled separately in the quantum circuit
- **Not a drop-in replacement** — requires re-architecture of the QRNN circuit
- **Validation needed** — the paper tested on 2 real-world datasets; performance may vary on other domains

## Cross-References

- `quantum-reservoir-computing` — alternative quantum approach for time series
- `qlif-cast-quantum-spiking-forecasting` — quantum spiking approach for forecasting
- `quantum-time-series-finance` — quantum time series for financial applications
- `spiking-bandpass-wavelet-encoding` — encoding strategies for spiking networks (analogous encoding challenge)
