---
name: hybrid-quantum-medical-classification
description: Hybrid quantum-classical machine learning pipelines for medical diagnosis and healthcare classification. Integrates parameterized quantum circuits (PQC/VQC) with classical CNNs, QSVM, or PCA for disease detection from medical imaging (thermography, X-ray, MRI) and clinical data. Use when: designing quantum-enhanced medical AI systems, building hybrid quantum-classical diagnostic pipelines, selecting quantum feature maps for healthcare data, handling class imbalance in medical classification with quantum models, or applying variational quantum circuits to clinical datasets.
---

# Hybrid Quantum-Classical Medical Classification

Design hybrid quantum-classical pipelines for medical diagnosis combining classical preprocessing/feature extraction with quantum machine learning (QML) models.

## Core Architecture Pattern

```
Medical Data → Classical Preprocessing → Quantum Encoding → VQC/QSVM → Classical Postprocessing → Diagnosis
```

### Step 1: Classical Preprocessing

- Apply **PCA** or **CNN feature extraction** to reduce dimensionality before quantum encoding
- For imaging: use pretrained CNN backbone (ResNet, EfficientNet) → flatten features → quantum encoding
- For tabular clinical data: standardize, normalize, then amplitude/angle encoding
- Handle class imbalance: SMOTE, class weights, or ensemble approaches

### Step 2: Quantum Encoding Strategies

Select encoding based on data type and qubit budget:

| Encoding | Best For | Qubits Needed |
|----------|----------|---------------|
| Angle Encoding | Normalized features | n = features |
| Amplitude Encoding | High-dimensional data | n = log₂(features) |
| IQP Feature Map | Non-linear separable | n = features |
| ZZFeatureMap | Entangled classification | n = features |

### Step 3: Variational Quantum Circuit (VQC) Design

- Use **hardware-efficient ansatz** for NISQ devices: layers of single-qubit rotations + CNOT entanglers
- **Multi-head quantum attention**: embed attention within parameterized circuits for medical imaging
- **Ensemble Multi-VQC**: train multiple VQCs with different initializations, aggregate predictions for imbalanced data
- Barren plateau mitigation: layer-wise training, localized cost functions

### Step 4: Hybrid Training Loop

```python
def hybrid_loss(params, X_classical, X_quantum, y):
    # Classical feature extraction
    features = cnn_backbone(X_classical)
    # Quantum encoding + VQC
    quantum_output = vqc.forward(features, params)
    # Classical post-processing
    logits = classifier(quantum_output)
    return cross_entropy(logits, y) + class_weight_penalty(y)
```

### Step 5: Key Pitfalls

- **Qubit budget**: NISQ devices limited to ~100 qubits; always use dimensionality reduction first
- **Shot noise**: use sufficient shots (≥1024) for reliable gradient estimation
- **Class imbalance**: quantum models amplify imbalance; use weighted loss or ensemble
- **Data loading bottleneck**: quantum state preparation is O(N); prefer amplitude encoding for large datasets
- **Barren plateaus**: deep circuits → vanishing gradients; use shallow circuits or layer-wise training

## QSVM for Medical Classification

Alternative to VQC when training stability is priority:

1. Choose quantum kernel (RBF-inspired, ZZFeatureMap-based)
2. Compute kernel matrix K[i,j] = |⟨φ(x_i)|φ(x_j)⟩|²
3. Train classical SVM on quantum kernel matrix
4. Best for: small-to-medium datasets (<10K samples), binary classification

## Activation

- hybrid quantum medical, quantum healthcare AI, QML diagnosis
- quantum neural network cancer detection, QSVM healthcare
- variational quantum circuit medical imaging, quantum X-ray diagnosis
- quantum thermographic classification, hybrid quantum-classical pipeline
