---
name: cv-photonic-qnn-edge-medical
description: "Parameter-efficient continuous-variable photonic quantum neural networks for edge medical AI. Simplified Phi-D-U1 CV-QNN architecture cuts trainable parameters 40-45%, mitigates barren plateaus, achieves 100% calibrated test accuracy with 18 parameters for oral cancer detection. Use when: CV quantum neural network design, photonic quantum ML, medical image classification on edge devices, barren plateau mitigation, parameter-efficient quantum classifiers, room-temperature quantum computing."
metadata:
  arxiv_id: "2606.28252"
  published: "2026-06-26"
  authors: "Akshay Bhagwan Sonawane, Sophie Choe, Lakshman Tamil"
  tags: [CV-QNN, photonic-quantum, medical-AI, edge-computing, oral-cancer, barren-plateau]
---

# CV Photonic QNN for Edge Medical AI

## Core Concept

Hybrid classical-continuous-variable quantum neural network for parameter-efficient medical image classification at the edge. Uses room-temperature photonic quantum computing (vs. cryogenic qubit hardware) combined with MobileNetV1 feature extraction and PCA dimensionality reduction to achieve medical-grade accuracy with minimal trainable quantum parameters.

## Architecture

### Pipeline
1. **Feature extraction**: MobileNetV1 pretrained classical backbone → smartphone image features
2. **Dimensionality reduction**: PCA to 16 dimensions
3. **Quantum encoding**: Angle encoding into CV quantum states
4. **CV-QNN layers**: Displacement (D), interferometric (U1), and Kerr nonlinear gates on photonic backend

### Simplified Layer Design
- **Standard CV-QNN** (Killoran et al. 2019): Full D → S → R → U → K gate sequence
- **Simplified Phi-D-U1**: Reduced Phi ∘ D ∘ U1 sequence cutting trainable parameters by 40-45%
- **Width-dependent performance**: Full layer wins at 2 qumodes; simplified layer wins at 4 qumodes with 44% fewer parameters

## Key Results

| Metric | Value |
|--------|-------|
| Best model | 4-qumode simplified CV-QNN |
| Trainable parameters | 18 |
| Validation AUC | Highest among all models |
| Test accuracy | 100% calibrated (all seeds) |
| Parameter savings vs classical baseline | 67% fewer than 55-parameter classical |
| Gradient variance improvement | ~58 orders of magnitude (barren plateau mitigation) |

## Barren Plateau Mitigation Strategies

1. **Dimensionality reduction**: PCA before quantum encoding reduces input dimension, preventing exponential gradient vanishing
2. **Encoding restriction**: Limited angle encoding scope maintains gradient signal
3. **Layer simplification**: Phi-D-U1 reduces circuit depth, preserving trainability
4. **Qumode scaling**: 4-qumode configuration optimal for simplified architecture

## Implementation Pattern

```python
# Conceptual pipeline
class CVCancerClassifier:
    def __init__(self, n_qumodes=4):
        self.classical = MobileNetV1(weights='imagenet')
        self.pca = PCA(n_components=16)
        self.cv_qnn = SimplifiedCVQNN(n_qumodes=n_qumodes)  # Phi-D-U1 architecture
    
    def forward(self, image):
        features = self.classical(image)
        reduced = self.pca.fit_transform(features)
        quantum_output = self.cv_qnn.encode_and_process(reduced)
        return quantum_output.classify()
```

## Edge Deployment Advantages

- **Room temperature operation**: Photonic hardware eliminates cryogenic infrastructure
- **Minimal parameters**: 18 trainable parameters vs. thousands in classical equivalents
- **Smartphone-compatible**: Designed for smartphone-based screening in low-resource settings

## Pitfalls

- **Photonic backend availability**: Requires access to photonic quantum computing platforms (e.g., Xanadu Strawberry Fields)
- **Width-dependent optimization**: Must empirically test qumode count — simplified layer not universally superior
- **Classical feature dependency**: Performance relies on quality of MobileNetV1 features — domain mismatch affects results

## Activation Keywords

- CV-QNN, photonic quantum neural network, continuous-variable quantum, edge quantum AI, oral cancer detection, MobileNet quantum hybrid, barren plateau mitigation, parameter-efficient QML, room-temperature quantum computing, smartphone medical screening
