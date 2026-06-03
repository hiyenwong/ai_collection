---
name: qtl-fair-benchmarking
description: >
  Quantum Transfer Learning (QTL) fair benchmarking methodology for visual and medical image
  classification. Uses pretrained classical backbone networks (ResNet, ViT) to extract high-level
  features, then applies compact quantum modules (VQC, QNN) as trainable classification heads.
  Establishes fair comparison protocols between quantum and classical ML by controlling for
  parameter count, training data, and evaluation metrics. Addresses the critical problem that
  many quantum ML papers claim advantages without fair baselines. Use when: (1) benchmarking
  quantum ML against classical baselines, (2) quantum transfer learning for visual classification,
  (3) medical image classification with quantum-enhanced heads, (4) evaluating whether quantum
  advantages are genuine or artifacts of unfair comparison, (5) near-term quantum ML under qubit
  constraints. Based on arXiv:2605.19417.
---

# QTL Fair Benchmarking

## Core Pattern

Use pretrained classical backbones for feature extraction, then apply compact quantum circuits
as trainable classification heads. This hybrid approach leverages classical representational
power while testing quantum classification capabilities under near-term qubit constraints.

## Key Paper

**Towards Fair Benchmarking of Quantum Transfer Learning for Visual Classification**
arXiv:2605.19417

## Architecture

```
Input → [Classical Backbone (frozen)] → Features → [Quantum Module (trainable)] → Output
```

### Classical Backbone (Frozen)
- ResNet-18, ResNet-50, or ViT pretrained on ImageNet
- Extract features from penultimate layer
- No fine-tuning during quantum training (frozen weights)
- Produces high-dimensional feature vectors

### Quantum Classification Head (Trainable)
- Data re-uploading circuit or variational quantum classifier
- Typically 4-8 qubits on NISQ hardware
- Amplitude or angle encoding of classical features
- Parameters trained via classical optimizer (SPSA, Adam)

## Fair Comparison Protocol

Many quantum ML papers claim advantages over classical baselines without ensuring fair comparison:

1. **Equal parameter budget**: Classical baseline should have similar trainable parameter count
2. **Equal feature representation**: Both models receive identical extracted features
3. **Equal training data**: Same train/val/test splits
4. **Equal optimization budget**: Same number of training steps, same optimizer type
5. **Report variance**: Run multiple random seeds, report mean ± std

### Unfair Comparison Examples to Avoid
- Comparing QTL to shallow classical networks (unfair — classical should be strong)
- Using different feature extractors for quantum vs classical
- Not reporting classical baseline variance
- Cherry-picking hyperparameters for quantum model only

## Implementation

```python
import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights

class QTLModel(nn.Module):
    def __init__(self, feature_dim=512, n_qubits=4):
        super().__init__()
        # Frozen classical backbone
        backbone = resnet18(weights=ResNet18_Weights.DEFAULT)
        self.backbone = nn.Sequential(*list(backbone.children())[:-1])
        for p in self.backbone.parameters():
            p.requires_grad = False

        # PCA to reduce to n_qubits dimensions
        self.pca = nn.Linear(feature_dim, n_qubits)

        # Quantum circuit (simulated via Pennylane/TorchQuantum)
        self.quantum_head = QuantumClassifier(n_qubits)

    def forward(self, x):
        features = self.backbone(x).squeeze()
        reduced = self.pca(features)
        return self.quantum_head(reduced)
```

## When to Use

- **Medical image classification** with limited labeled data
- **Visual classification** tasks where quantum advantage is suspected
- **Benchmarking studies** comparing quantum vs classical ML
- **Near-term quantum ML** under qubit constraints

## Pitfalls

- Quantum advantage claims are often artifacts of weak classical baselines
- Feature dimensionality must match qubit count (use PCA/feature selection)
- Quantum training is slow — limit to proof-of-concept scale
- Real hardware noise can erase any theoretical quantum advantage
- Always report both quantum and classical results with variance

## Related Skills

- `quantum-kernel-advantage`: QSVM with medical foundation model embeddings
- `quantum-ml-patterns`: General QML research patterns
- `hybrid-quantum-medical-classification`: HQNN for medical imaging
- `vqc-architecture-comparison`: VQC architecture design patterns
