---
name: "cv-quantum-biomedical-imaging"
description: "Continuous-variable quantum neural networks (CV-QCNN) for biomedical image classification methodology. Uses photonic circuit simulation with Gaussian gates (displacement, squeezing, rotation, beamsplitters) to emulate convolutional behavior for medical imaging tasks. Activation: continuous variable quantum, CV quantum neural network, photonic quantum imaging, biomedical image classification, CV-QCNN, MedMNIST quantum, quantum medical imaging, photonic circuit simulation, Gaussian gate convolution"
metadata:
  arxiv_id: "2511.02051"
  published: "2025-11-03"
  authors: "Daniel Alejandro Lopez, Oscar Montiel, Oscar Castillo, Miguel Lopez-Montiel"
  tags: [quantum, biomedical-imaging, continuous-variable, photonics, MedMNIST]
license: "Complete terms in LICENSE.txt"
---

## Context

Continuous-variable (CV) quantum computing offers scalable quantum machine learning via optical systems with infinite-dimensional Hilbert spaces. Unlike discrete-variable (DV) QNNs, CV models use Gaussian gates on continuous quadratures — more natural for image-like data but comparatively underexplored.

Paper: arXiv:2511.02051 — feasibility study of CV-QCNNs on MedMNIST for biomedical image classification.

## Core Methodology

### CV-QCNN Architecture

1. **Input Encoding**: Map biomedical image pixels to CV quantum modes via amplitude/phase encoding
2. **Gaussian Convolution Layers**: Compose displacement (D), squeezing (S), rotation (R), and beamsplitter (BS) gates to emulate spatial convolution
3. **Measurement Strategy**: Homodyne/heterodyne detection to extract classical features from quantum states
4. **Classification Head**: Classical post-processing of measurement outcomes for diagnostic prediction

### Gate Composition Pattern

```
CV-QCNN layer = BS ⊗ S ⊗ R ⊗ D (applied per image patch)
```

- **Beamsplitter (BS)**: Entangles adjacent modes → spatial feature mixing
- **Squeezing (S)**: Reduces uncertainty in one quadrature → feature amplification
- **Rotation (R)**: Phase-space rotation → feature transformation
- **Displacement (D)**: State translation → bias/offset

### Evaluation Metrics

- Classification accuracy, AUC, F1-score on MedMNIST benchmarks
- Model expressiveness (circuit depth vs performance trade-off)
- Gaussian noise resilience (critical for near-term hardware)

## Implementation Steps

1. Use photonic circuit simulation framework (e.g., Strawberry Fields, PennyLane)
2. Build CV circuit: Gaussian gates → non-Gaussian gates (for universality) → measurement
3. Train on MedMNIST dataset collection (annotated medical image benchmarks)
4. Compare against classical CNNs and equivalent DV quantum circuits
5. Evaluate noise resilience by injecting Gaussian noise into gate parameters

## Pitfalls

- **CV vs DV trade-off**: CV models have infinite-dimensional spaces but are harder to simulate classically → simulation cost grows rapidly with mode count
- **Non-Gaussian gates required**: Pure Gaussian circuits cannot achieve universal quantum computation → add Kerr/cubic phase gates for expressiveness
- **MedMNIST format**: Dataset uses small standardized images (28x28 or 64x64) — ensure encoding matches circuit mode capacity
- **Noise sensitivity**: CV states are highly sensitive to loss/decoherence — evaluate noise resilience early

## Verification

- Reproduce MedMNIST classification accuracy on at least 2 diagnostic tasks
- Verify CV circuit simulation converges within reasonable shot count
- Confirm noise resilience degrades gracefully (not catastrophically) with increasing Gaussian noise
