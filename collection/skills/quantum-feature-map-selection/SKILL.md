---
name: quantum-feature-map-selection
description: Methodology for selecting and evaluating quantum feature maps in Quantum Support Vector Machines (QSVM) for classification tasks. Covers angle encoding, amplitude encoding, ZZFeatureMap, IQPFeatureMap, and their trade-offs for different data types (medical imaging, clinical data, financial data). Use when: choosing quantum encoding strategies, designing quantum kernels for SVM, comparing feature map effectiveness, or optimizing quantum-classical data encoding pipelines.
---

# Quantum Feature Map Selection for QSVM

Systematic methodology for selecting quantum feature maps that maximize classification performance.

## Feature Map Taxonomy

### 1. Angle Encoding
- Map each feature x_i → RY(x_i) rotation on qubit i
- **Qubits**: n = number of features
- **Depth**: O(1) — single layer
- **Best for**: Normalized features, low-dimensional data (<20 features)
- **Pros**: Simple, shallow, NISQ-friendly
- **Cons**: No entanglement by default; add CNOT layers for expressivity

### 2. Amplitude Encoding
- Encode N features into amplitudes of log₂(N) qubits state |ψ⟩ = Σ x_i |i⟩
- **Qubits**: n = log₂(N) — exponentially compact
- **Depth**: O(N) for state preparation
- **Best for**: High-dimensional data (images, gene expression)
- **Pros**: Exponential compression
- **Cons**: State preparation overhead, requires normalization

### 3. ZZFeatureMap
- Alternating H-layer + ZZ entangling + RZ(φ(x_i)) rotations
- **Qubits**: n = number of features (or subset via PCA)
- **Depth**: O(reps × n²) — configurable via reps parameter
- **Best for**: Non-linearly separable data, when entanglement is beneficial
- **Pros**: Proven expressivity, widely used in Qiskit
- **Cons**: Deep circuits for many features

### 4. IQPFeatureMap (Instantaneous Quantum Polynomial)
- Diagonal gates with feature-dependent phases
- **Qubits**: n = number of features
- **Best for**: Theoretical quantum advantage studies

## Selection Decision Tree

```
Data dimensionality?
├── Low (<20 features) → Angle Encoding or ZZFeatureMap
├── Medium (20-100) → PCA → Angle Encoding, or ZZFeatureMap on top components
└── High (>100) → Amplitude Encoding or CNN features → Angle Encoding

Non-linearity needed?
├── Yes → ZZFeatureMap (reps=2) or IQPFeatureMap
└── No → Angle Encoding (sufficient)

NISQ device constraints?
├── Limited coherence → Angle Encoding (shallowest)
├── Moderate → ZZFeatureMap (reps=1)
└── Simulator → Full expressivity
```

## Evaluation Protocol

1. **Expressivity test**: Measure kernel target alignment KTA = Tr(K_target K_quantum) / (||K_target|| ||K_quantum||)
2. **Generalization bound**: Compute quantum kernel condition number κ(K) — lower is better
3. **Classification accuracy**: Cross-validate on train set
4. **Quantum advantage indicator**: Compare quantum kernel SVM vs classical RBF kernel SVM

## Medical Domain Specifics

- **Thermographic images**: CNN features (512-d) → PCA (16-d) → ZZFeatureMap(reps=2)
- **X-ray images**: PCA (8-d) → Angle Encoding — fracture detection
- **Clinical tabular**: Standardize → Amplitude Encoding — heart failure, diabetes
- **Class imbalance**: Use weighted QSVM or ensemble of feature maps

## Pitfalls

- Feature map choice has larger impact than circuit ansatz — always benchmark multiple encodings
- ZZFeatureMap on >20 features → too deep for NISQ; always reduce dimension first
- Quantum kernels don't automatically outperform classical RBF — verify KTA > classical baseline

## Activation

- quantum feature map, QSVM encoding, quantum kernel selection
- angle encoding, amplitude encoding, ZZFeatureMap, IQPFeatureMap
- quantum SVM medical, quantum kernel classification
