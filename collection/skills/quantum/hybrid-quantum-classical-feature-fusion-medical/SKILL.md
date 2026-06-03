---
name: hybrid-quantum-classical-feature-fusion-medical
description: "Hybrid quantum-classical feature fusion methodology for medical image classification. Uses three progressive fusion strategies (SHF, DHF, TSHF) to unify quantum and classical representations for enhanced diagnostic accuracy. Use when building quantum-enhanced medical diagnostic systems, hybrid QNN-classical pipelines, or medical image classification with quantum circuits. Activation: hybrid quantum classical feature fusion, temperature scaled fusion, quantum medical diagnosis, quantum breast cancer classification, hybrid quantum medical, TSHF"
---

# Hybrid Quantum-Classical Feature Fusion for Medical Diagnosis

## Overview

Combines quantum machine learning with classical deep learning for medical image analysis by mapping data into high-dimensional Hilbert spaces and fusing complementary representations from both paradigms.

## Core Methodology

### Three Progressive Fusion Strategies

1. **Static Hybrid Fusion (SHF)**: Offline extraction of classical + quantum features, then concatenate for downstream classifier. Simple but inflexible.

2. **Dynamic Hybrid Fusion (DHF)**: End-to-end co-adaptation where classical backbone and quantum circuit train jointly. Gradient flows through both branches simultaneously.

3. **Temperature-Scaled Hybrid Fusion (TSHF)**: Novel approach using a learnable scalar parameter (inspired by multimodal learning) to dynamically balance gradient dynamics between quantum and classical branches. Resolves optimization asymmetries.

### Architecture Pipeline

```
Input Medical Image
    │
    ├──→ Classical Backbone (ResNet/ViT) → Classical Embedding
    │
    └──→ Quantum Circuit (trainable or deterministic) → Quantum Embedding
    │
    ▼
Temperature-Scaled Hybrid Fusion (TSHF)
    │
    ▼
Unified Representation → Classifier Head → Diagnosis
```

### Key Results

On BreastMNIST with ResNet + trainable quantum circuit:
- **Accuracy**: 87.82%
- **F1-Score**: 91.77%
- **AUC-ROC**: 89.08%
- Outperforms purely classical baselines

## Implementation Guide

### Step 1: Classical Feature Extraction

```python
import torch
import torch.nn as nn
from torchvision.models import resnet18

class ClassicalBranch(nn.Module):
    def __init__(self, embedding_dim=128):
        super().__init__()
        backbone = resnet18(pretrained=True)
        backbone.fc = nn.Linear(backbone.fc.in_features, embedding_dim)
        self.backbone = backbone
    
    def forward(self, x):
        return self.backbone(x)
```

### Step 2: Quantum Circuit Feature Extraction

```python
import pennylane as qml

n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    # Amplitude encoding
    qml.AmplitudeEmbedding(inputs, wires=range(n_qubits), normalize=True)
    
    # Variational layers
    for i in range(n_qubits):
        qml.Rot(weights[i, 0], weights[i, 1], weights[i, 2], wires=i)
    
    # Entangling layers
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    
    # Measurement
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Step 3: Temperature-Scaled Hybrid Fusion

```python
class TSHF(nn.Module):
    def __init__(self, classical_dim, quantum_dim):
        super().__init__()
        # Learnable temperature scalars
        self.t_classical = nn.Parameter(torch.tensor(1.0))
        self.t_quantum = nn.Parameter(torch.tensor(1.0))
        # Projection to unified space
        self.projection = nn.Linear(classical_dim + quantum_dim, classical_dim)
    
    def forward(self, classical_feat, quantum_feat):
        # Scale by learnable temperatures
        c_scaled = classical_feat / self.t_classical.clamp(min=0.1)
        q_scaled = quantum_feat / self.t_quantum.clamp(min=0.1)
        
        # Concatenate and project
        combined = torch.cat([c_scaled, q_scaled], dim=-1)
        return self.projection(combined)
```

### Step 4: Complete Hybrid Model

```python
class HybridQuantumMedicalClassifier(nn.Module):
    def __init__(self, classical_dim=128, quantum_dim=4, n_classes=2):
        super().__init__()
        self.classical = ClassicalBranch(classical_dim)
        self.fusion = TSHF(classical_dim, quantum_dim)
        self.classifier = nn.Linear(classical_dim, n_classes)
    
    def forward(self, x, quantum_inputs, quantum_weights):
        c_feat = self.classical(x)
        q_feat = quantum_circuit(quantum_inputs, quantum_weights)
        q_feat = torch.stack(q_feat).T  # [batch, n_qubits]
        
        unified = self.fusion(c_feat, q_feat)
        return self.classifier(unified)
```

## Pitfalls

### Optimization Asymmetries
- Quantum and classical branches often have different gradient scales
- **Solution**: Use TSHF with learnable temperature scalars to balance gradients
- Monitor gradient norms of both branches during training

### Qubit Count Mismatch
- Too few qubits → insufficient representational power
- Too many qubits → noise dominates on NISQ hardware
- **Solution**: Match qubit count to compressed latent dimension

### Data Encoding Bottleneck
- Classical medical images are high-dimensional (224x224x3)
- Direct amplitude encoding is infeasible for large images
- **Solution**: Use classical backbone for dimensionality reduction first, then encode the embedding into quantum circuit

## Activation Keywords
- hybrid quantum classical feature fusion
- temperature scaled fusion
- quantum medical diagnosis
- TSHF
- quantum breast cancer classification
- hybrid quantum medical image
- quantum classical fusion medical

## Related Patterns
- Tensor-network quantum federated learning (see `tensor-network-quantum-federated` skill)
- Quantum neural network architecture design
- Medical image domain adaptation
