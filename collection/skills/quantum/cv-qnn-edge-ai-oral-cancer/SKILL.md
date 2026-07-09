---
name: cv-qnn-edge-ai-oral-cancer
description: "Parameter-efficient Continuous-Variable Photonic Quantum Neural Networks for Edge AI — simplified Φ∘D∘U₁ CV-QNN architecture achieving 100% calibrated test accuracy on oral cancer detection with only 18 parameters (44% fewer than standard CV-QNN layer). Use when building room-temperature quantum ML for medical classification, edge quantum AI, or optimizing CV-QNN parameter efficiency."
category: quantum
created: 2026-07-08
source: arXiv:2606.28252
---

# Parameter-Efficient CV-QNN for Edge AI Medical Classification

## Source

arXiv:2606.28252 — "Parameter-Efficient Continuous-Variable Photonic Quantum Neural Networks for Edge Quantum AI: Demonstration in Oral Cancer Detection" by Akshay Bhagwan Sonawane, Sophie Choe, Lakshman Tamil (2026-06-26)

## Overview

Demonstrates that **Continuous-Variable (CV) photonic quantum computing** — which operates at **room temperature** — can deliver parameter-efficient medical image classification suitable for edge deployment. A simplified **Φ∘D∘U₁** CV-QNN architecture cuts trainable parameters by 40-45% relative to the standard CV-QNN layer, and achieves 100% calibrated test accuracy with only 18 parameters.

## Why CV Over Qubit-Based for Edge?

| Property | Qubit-Based (Superconducting) | CV Photonic |
|----------|-------------------------------|-------------|
| Operating Temperature | ~10 mK (cryogenic) | Room temperature |
| Edge Deployment | Not feasible | Feasible |
| Parameter Efficiency | Moderate | High (with simplified layers) |

## Core Methodology

### Pipeline Architecture

```
Smartphone Image
    │
    ▼
MobileNetV1 Feature Extractor
    │
    ▼
PCA Dimensionality Reduction → 16 dimensions
    │
    ▼
CV-QNN (Displacement + Interferometric + Kerr gates)
    │
    ▼
Classification (Oral Cancer Detection)
```

### Simplified CV-QNN Layer Architecture: Φ∘D∘U₁

The standard CV-QNN layer (Killoran et al., 2019) uses: **Displacement → Squeezing → Rotation → Interferometer**

The **simplified** version: **Φ (Kerr nonlinearity) → D (Displacement) → U₁ (single-mode interferometer)**

```python
# Standard CV-QNN layer
# D(α) → S(r,φ) → R(θ) → Interferometer → Kerr(κ)

# Simplified CV-QNN layer (proposed)
# Kerr(κ) → D(α) → U₁ (single-mode)

# Parameter reduction: 40-45% fewer trainable parameters
```

### Key Insight: Dimensionality Reduction + Encoding Restriction

Combining **PCA dimensionality reduction** with **encoding restriction strategies** mitigates barren plateaus, raising loss-gradient variance by approximately **58 orders of magnitude**.

### Width-Dependent Performance

| Qumodes | Standard Layer | Simplified Layer | Winner |
|---------|---------------|------------------|--------|
| 2 | Small edge | Slightly worse | Standard |
| 4 | Worse | **Better (44% fewer params)** | **Simplified** |

## Key Results

- **Best Model**: 4-qumode simplified CV-QNN with only **18 parameters**
- **Validation AUC**: Highest among all models tested
- **Test Accuracy**: 100% calibrated accuracy across all seeds
- **Parameter Efficiency**: 67% fewer parameters than 55-parameter classical baseline
- **Loss-Gradient Variance**: ~58 orders of magnitude improvement over unrestricted encoding

## Implementation Guide

### Step 1: Classical Preprocessing

```python
import torch
import torch.nn as nn
from torchvision.models import mobilenet_v1

class ClassicalPreprocessor(nn.Module):
    def __init__(self, output_dim=16):
        super().__init__()
        backbone = mobilenet_v1(pretrained=True)
        backbone.classifier = nn.Linear(backbone.classifier[0].in_features, output_dim)
        self.backbone = backbone
    
    def forward(self, x):
        features = self.backbone(x)
        # PCA to final dimension
        return features  # Shape: [batch, 16]
```

### Step 2: Simplified CV-QNN Layer

```python
import pennylane as qml
from pennylane import numpy as np

n_qumodes = 4
cutoff_dim = 5  # Fock basis truncation

dev = qml.device("strawberryfields.fock", wires=n_qumodes, cutoff_dim=cutoff_dim)

@qml.qnode(dev)
def simplified_cv_qnn(inputs, weights):
    """Simplified Φ∘D∘U₁ CV-QNN layer."""
    
    # Encode classical features as displacement amplitudes
    for i in range(n_qumodes):
        qml.Displacement(inputs[i], 0.0, wires=i)
    
    # Φ: Kerr nonlinearity
    for i in range(n_qumodes):
        qml.Kerr(weights[i, 0], wires=i)
    
    # D: Additional displacement (trainable)
    for i in range(n_qumodes):
        qml.Displacement(weights[i, 1], weights[i, 2], wires=i)
    
    # U₁: Single-mode interferometer (rotation)
    for i in range(n_qumodes):
        qml.Rotation(weights[i, 3], wires=i)
    
    # Measure photon number expectation
    return [qml.expval(qml.NumberOperator(i)) for i in range(n_qumodes)]
```

### Step 3: Hybrid Model

```python
class CVQNNOralCancerClassifier(nn.Module):
    def __init__(self, n_qumodes=4, cutoff_dim=5):
        super().__init__()
        self.preprocessor = ClassicalPreprocessor(output_dim=16)
        self.n_qumodes = n_qumodes
        self.qnn_weights = nn.Parameter(torch.randn(n_qumodes, 4))
        self.classifier = nn.Linear(n_qumodes, 2)  # Binary classification
    
    def forward(self, x):
        # Classical feature extraction
        features = self.preprocessor(x)  # [batch, 16]
        
        # PCA / dimensionality reduction
        features = features[:, :self.n_qumodes]  # Take first n_qumodes
        
        # CV-QNN
        qnn_outputs = []
        for i in range(x.shape[0]):
            out = simplified_cv_qnn(features[i].detach().numpy(), 
                                     self.qnn_weights.detach().numpy())
            qnn_outputs.append(out)
        
        qnn_tensor = torch.tensor(qnn_outputs)
        return self.classifier(qnn_tensor)
```

## Pitfalls

### Barren Plateaus in CV-QNN
- **Problem**: Standard CV-QNN layers suffer from vanishing gradients
- **Solution**: Use PCA dimensionality reduction + encoding restriction (raises gradient variance by ~58 orders of magnitude)

### Qumode Count Selection
- **2 qumodes**: Standard layer has small edge over simplified
- **4 qumodes**: Simplified layer is significantly better with 44% fewer parameters
- **Rule**: Use 4 qumodes with simplified layer for best parameter efficiency

### Encoding Restriction
- Full amplitude encoding of high-dimensional features causes training instability
- **Solution**: Restrict encoding to displacement-only or phase-only, combined with PCA

### MobileNetV1 vs MobileNetV2/V3
- MobileNetV1 chosen for parameter efficiency on edge devices
- MobileNetV2/V3 add complexity that may negate quantum advantage on constrained hardware

## Edge Deployment Considerations

1. **Photonic Hardware**: CV-QNN runs on photonic quantum processors (Xanadu, etc.)
2. **Classical Simulation**: Can simulate on CPU for development, but true edge deployment requires photonic co-processor
3. **Parameter Count**: 18 parameters fit easily in edge device memory
4. **Latency**: Room-temperature operation eliminates cryogenic cooling latency

## Activation Keywords

- CV-QNN, continuous-variable quantum neural network
- edge quantum AI, edge AI medical
- oral cancer detection
- photonic quantum computing
- parameter-efficient quantum ML
- simplified CV-QNN layer
- Φ∘D∘U₁ architecture
- room-temperature quantum ML
- MobileNet quantum hybrid
- barren plateau mitigation

## Related Skills

- `hybrid-quantum-classical-feature-fusion-medical` — TSHF for breast cancer
- `qae-mri-anomaly-detection` — Quantum autoencoder for brain MRI
- `cv-photonic-qnn-edge-ai` — General CV-QNN edge AI patterns
- `qbalance-quantum-workflow-optimization` — Multi-objective quantum workflow optimization
