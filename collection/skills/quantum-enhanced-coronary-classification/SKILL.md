---
name: quantum-enhanced-coronary-classification
description: "Lightweight quantum-enhanced ResNet for coronary angiography (CAG) classification. Combines classical CNN backbones with variational quantum circuits for medical image classification. Use when: coronary angiography analysis, cardiac image classification, lightweight QML models, quantum-enhanced CNNs, operator-dependency reduction in CAG interpretation, or hybrid quantum-classical medical imaging."
metadata:
  arxiv_ids: "1809"
  published: "2026-01-22"
  tags: [quantum, medical-imaging, coronary, resnet, cnn, lightweight, vqc]
---

# Quantum-Enhanced Coronary Angiography Classification

## Description

Lightweight quantum-enhanced ResNet framework combining classical CNN feature extractors with variational quantum circuits for coronary angiography (CAG) classification. Addresses operator-dependency in CAG interpretation by providing consistent, quantum-enhanced analysis of coronary vessel images.

**Key insight**: Classical CNN handles most feature extraction; quantum circuit acts as a lightweight classifier head, leveraging Hilbert space expressivity for complex decision boundaries with minimal qubits.

## Architecture

### Hybrid Pipeline

```
Input Image → CNN Backbone (ResNet) → Feature Vector → Quantum Circuit → Classification
```

1. **CNN Backbone**: Standard ResNet (pretrained on ImageNet or medical data)
2. **Feature Compression**: Reduce to N dimensions (N = number of qubits)
3. **Quantum Classifier Head**: VQC with N qubits, parameterized layers
4. **Measurement**: Readout yields class probabilities

### Quantum Circuit Design

- **Encoding**: Angle encoding of compressed features
- **Ansatz**: Hardware-efficient (RY/RZ + CZ entanglement layers)
- **Layers**: 2-4 layers (shallow to reduce noise impact)
- **Readout**: Pauli-Z expectation values per qubit

### Why Lightweight?

- Only classifier head is quantum (1-4 qubits vs full image encoding)
- Classical CNN handles the computationally heavy feature extraction
- Quantum part focuses on high-dimensional decision boundaries
- Compatible with current NISQ hardware

## When to Use

- Coronary angiography image classification
- Reducing operator dependency in CAG interpretation
- Lightweight quantum enhancement of existing CNN models
- Medical imaging where quantum advantage is plausible in classification layer
- Resource-constrained quantum hardware (few qubits available)

## Implementation Steps

1. **Prepare dataset**: CAG images with stenosis/severity labels
2. **Train/freeze CNN**: Use pretrained ResNet, freeze early layers
3. **Design VQC**: Match qubit count to compressed feature dimension
4. **Hybrid training**: Backprop through CNN, parameter-shift for VQC
5. **Evaluate**: Compare against CNN-only baseline and clinical expert performance

## Error Handling

### Feature Dimension Mismatch
- Use PCA/autoencoder to compress CNN features to exact qubit count
- Ensure compressed features retain discriminative information

### Quantum Circuit Barren Plateaus
- Initialize with identity or classically-informed parameters
- Use local observables instead of global measurements
- Limit circuit depth to avoid vanishing gradients

### Clinical Validation Gap
- Validate against expert cardiologist annotations
- Report both accuracy and clinical relevance metrics (sensitivity, specificity)
- Consider regulatory requirements for clinical deployment

## Resources

- Paper: Entity ID 1809 in kg.db
- Related: Hybrid quantum-classical patterns from quantum-medical-diagnosis skill
- Related: VQC design from quantum-neural-architecture skill
