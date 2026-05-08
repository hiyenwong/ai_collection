---
name: pulse-level-quantum-fourier-models
description: "Pulse-level Quantum Fourier Models (QFMs) methodology for quantum machine learning. Goes beyond gate-based VQAs by operating at the pulse level, enabling richer Fourier feature spaces for quantum ML. Covers: (1) QFM mathematical structure via quantum Fourier series, (2) pulse-level control vs gate decomposition trade-offs, (3) scalability and trainability analysis, (4) frequency spectrum control for expressive quantum models. Use when: designing quantum ML models, analyzing QFM trainability, comparing pulse-level vs gate-based approaches, or optimizing quantum feature spaces for machine learning tasks. Activation: quantum Fourier model, QFM, pulse-level quantum ML, quantum machine learning Fourier, 脉冲级量子傅里叶模型, quantum feature space"
---

# Pulse-Level Quantum Fourier Models (QFMs)

## Overview

Quantum Fourier Models (QFMs) provide a mathematically well-defined structure for quantum machine learning based on quantum Fourier series. Unlike gate-based variational quantum algorithms (VQAs) that decompose circuits into discrete gates, pulse-level QFMs operate directly on quantum hardware control pulses, enabling richer frequency spectra and more expressive models.

**Source**: arXiv:2605.04945 - "Beyond Gates: Pulse Level Quantum Fourier Models"

## Mathematical Foundation

### Quantum Fourier Series

A QFM represents a function as a quantum Fourier series:

```
f(x) = Σ_k c_k * e^(i * ω_k * x)
```

where frequencies ω_k are determined by the Hamiltonian eigenvalue differences, and coefficients c_k depend on the observable and state preparation.

### Key Components

1. **Data Encoding**: Input x mapped via unitary U(x) = exp(-i * H_data * x)
2. **Trainable Unitary**: Parameterized quantum circuit U(θ)
3. **Measurement**: Observable expectation ⟨O⟩ as output
4. **Frequency Spectrum**: Determined by Hamiltonian eigenvalue differences

## Workflow

### Step 1: Define QFM Architecture

```python
# QFM components
# 1. Data Hamiltonian H_data - encodes input x
# 2. Ansatz U(θ) - trainable quantum circuit
# 3. Observable O - measurement operator

def qfm_circuit(x, theta, H_data, ansatz, observable):
    # Prepare initial state
    state = |0⟩^n
    # Encode data
    state = exp(-i * H_data * x) @ state
    # Apply trainable ansatz
    state = ansatz(theta) @ state
    # Measure observable
    return ⟨state| observable |state⟩
```

### Step 2: Analyze Frequency Spectrum

The expressivity of a QFM is determined by its accessible frequency set:

```python
def compute_frequencies(H_data):
    """Compute accessible frequencies from data Hamiltonian eigenvalues."""
    eigenvalues = np.linalg.eigvalsh(H_data)
    # Frequencies are pairwise differences
    freqs = set()
    for i in range(len(eigenvalues)):
        for j in range(len(eigenvalues)):
            freqs.add(eigenvalues[i] - eigenvalues[j])
    return sorted(freqs)
```

### Step 3: Pulse-Level vs Gate-Based Trade-offs

| Aspect | Gate-Based VQA | Pulse-Level QFM |
|--------|---------------|-----------------|
| Expressivity | Limited by gate set | Richer frequency spectrum |
| Compilation | Gate decomposition overhead | Direct hardware control |
| Noise | Accumulated gate errors | Shorter circuits, less noise |
| Trainability | Well-studied | Emerging, potential advantages |

### Step 4: Trainability Considerations

- **Barren Plateaus**: Check gradient variance scaling
- **Frequency Control**: More frequencies → higher expressivity but harder training
- **Ansatz Design**: Balance expressivity with trainability

## Key Insights from Paper

1. **Pulse-level QFMs** bypass gate decomposition, accessing richer frequency sets
2. **Scalability analysis** shows potential advantages over gate-based approaches
3. **Trainability limits** exist but pulse-level control offers new optimization landscapes
4. **Mathematical structure** of QFMs provides rigorous foundation for QML model design

## When to Use

- Designing quantum ML models where expressivity matters
- Comparing pulse-level vs gate-based quantum approaches
- Analyzing QFM frequency spectra for specific Hamiltonians
- Optimizing quantum feature spaces for regression/classification
- Researching trainability properties of quantum models

## Activation Keywords

- quantum Fourier model
- QFM quantum machine learning
- pulse-level quantum ML
- quantum Fourier series ML
- 脉冲级量子傅里叶模型
- quantum feature space design
- quantum model expressivity
- QFM trainability

## Related Skills

- `quantum-neural-architecture`: Quantum neural network design
- `hybrid-qml-pipeline-design`: Hybrid QML pipeline patterns
- `composite-quantum-gates-error-cancellation`: Pulse shaping for gates
- `drl-quantum-optimal-control`: RL for quantum pulse control

## References

- arXiv:2605.04945 - "Beyond Gates: Pulse Level Quantum Fourier Models"
- Categories: quant-ph
