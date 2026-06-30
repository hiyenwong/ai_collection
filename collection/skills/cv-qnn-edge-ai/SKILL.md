---
name: cv-qnn-edge-ai
version: v1.0.0
last_updated: 2026-06-30
description: "Parameter-efficient Continuous-Variable (CV) Photonic Quantum Neural Networks for edge AI deployment. Applies Φ∘D∘U₁ simplified CV-QNN architecture that reduces trainable parameters by 40-45% vs standard CV-QNN. Key techniques: dimensionality reduction (PCA), encoding restriction, barren plateau mitigation. Demonstrated on medical image classification (oral cancer detection). Keywords: cv-qnn, photonic quantum, edge AI, parameter-efficient QML, barren plateau mitigation, CV-QNN, quantum edge deployment."
---

# CV Photonic QNN for Edge AI

## Description

Design and train parameter-efficient Continuous-Variable (CV) Photonic Quantum Neural Networks for resource-constrained edge deployment. Uses a simplified Φ∘D∘U₁ architecture that cuts trainable parameters 40-45% compared to the standard CV-QNN layer (Killoran et al., 2019), while maintaining or improving accuracy.

## Activation Keywords

- cv-qnn
- photonic quantum neural network
- edge quantum AI
- parameter-efficient QML
- barren plateau mitigation
- continuous-variable QNN
- quantum edge deployment
- 光子量子神经网络
- 边缘量子AI

## Core Architecture: Φ∘D∘U₁ Simplified CV-QNN Layer

The standard CV-QNN layer (Killoran et al.) consists of:
```
Interferometer → Squeezing → Interferometer → Displacement → Kerr
```

The **simplified** layer reduces this to:
```
Φ (single interferometer) → D (displacement) → U₁ (phase shift)
```

### Parameter Savings

| Configuration | Standard Params | Simplified Params | Reduction |
|--------------|-----------------|-------------------|-----------|
| 2 qumodes    | ~40             | ~22               | 45%       |
| 4 qumodes    | ~80             | ~44               | 45%       |
| 4 qumodes (strongest model) | 55 (classical baseline) | **18** | **67% fewer than classical** |

### Gate Sequence

1. **U₁ (Phase shift)**: Apply phase rotations R(φ) per qumode
2. **D (Displacement)**: Apply displacement D(α) per qumode  
3. **Φ (Interferometer)**: Apply MZI (Mach-Zehnder Interferometer) mesh

## Pipeline

### Step 1: Classical Feature Extraction

```python
# Use lightweight CNN for feature extraction (edge-compatible)
import torch
from torchvision.models import mobilenet_v1

# MobileNetV1 → PCA to 16 dimensions → CV-QNN input
feature_extractor = mobilenet_v1(weights='IMAGENET1K_V1')
# Freeze and use as feature extractor
for param in feature_extractor.parameters():
    param.requires_grad = False
```

### Step 2: Dimensionality Reduction

```python
from sklearn.decomposition import PCA

# PCA to reduce features to CV-QNN compatible dimensions (8-16)
pca = PCA(n_components=16)
reduced_features = pca.fit_transform(extracted_features)
```

### Step 3: Encoding

Use amplitude encoding for classical → quantum data mapping:

```python
import pennylane as qml

n_qumodes = 4  # Start with 4 for best parameter/accuracy trade-off

@qml.qnode(dev)
def cv_qnn(inputs, weights):
    # Amplitude encoding
    qml.AmplitudeEmbedding(inputs, wires=range(n_qumodes), normalize=True)
    
    # Simplified layer: Φ∘D∘U₁
    for i in range(n_qumodes):
        qml.Rotation(weights[i], wires=i)  # U₁ phase
    qml.DisplacementEmbedding(weights[n_qumodes:2*n_qumodes], wires=range(n_qumodes))  # D
    # Φ: MZI interferometer (simplified)
    for i in range(n_qumodes - 1):
        qml.Beamsplitter(weights[2*n_qumodes + i], 0, wires=[i, i+1])
    
    return [qml.expval(qml.X(i)) for i in range(n_qumodes)]
```

### Step 4: Barren Plateau Mitigation

Key strategies from the paper:

1. **Dimensionality Reduction**: PCA before encoding reduces input space
2. **Encoding Restriction**: Limit displacement gate range
3. **Layer Simplification**: Fewer gates → higher gradient variance

```python
# Restrict displacement amplitude to avoid saturation
max_displacement = 0.5  # Tune based on task

# Gradient variance boost: simplified layer raises it by ~58 orders of magnitude
# vs full layer, enabling effective training on NISQ devices
```

## Key Findings

| Width | Winner | Notes |
|-------|--------|-------|
| 2 qumodes | Full layer | Full layer has small but significant edge |
| 4 qumodes | **Simplified layer** | **44% fewer params, significantly better** |

### Optimal Configuration (Recommended)

- **4 qumodes** with simplified Φ∘D∘U₁ layer
- **18 trainable parameters** total
- **PCA to 16 dimensions** before encoding
- **MobileNetV1** as feature extractor (edge-compatible)
- Achieves 100% calibrated test accuracy (paper result on oral cancer)

## Applicable Domains

- Medical image classification on edge devices
- Low-resource diagnostic tools
- Room-temperature quantum computing (no cryogenics)
- Smartphone-based screening applications
- Parameter-efficient hybrid quantum-classical ML

## Comparison with Qubit-Based QNN

| Aspect | Qubit-Based | CV Photonic |
|--------|-------------|-------------|
| Operating Temp | Cryogenic (~mK) | **Room temperature** |
| Edge Viability | No | **Yes** |
| Parameter Efficiency | Moderate | **High (40-45% reduction possible)** |
| Hardware Access | IBM, Rigetti | Xanadu, PsiQuantum |

## Implementation Notes

- Use PennyLane's `default.gaussian` or `strawberryfields` device
- For edge deployment, consider classical simulation of CV-QNN (small qumode counts)
- The simplified layer works best at ≥4 qumodes; at 2 qumodes the full layer is slightly better
- Always compare against classical baselines with matched parameter budgets

## Resources

- Paper: arXiv:2606.28252
- PennyLane CV QNN docs: https://pennylane.ai/qml/demos/tutorial_cvqnn
- Strawberry Fields: https://strawberryfields.ai/
