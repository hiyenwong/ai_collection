---
name: hqnn-medical-image-classification
category: quantum-healthcare
description: Hybrid Quantum Neural Network (HQNN) methodology for medical image classification. Combines pre-trained CNN backbones with variational quantum circuits for enhanced feature representation. Use when building quantum-enhanced medical imaging classifiers, comparing quantum vs classical feature transformations, or evaluating VQC robustness on real quantum hardware.
---

# HQNN Medical Image Classification

## Overview

Hybrid Quantum-Classical Neural Networks (HQNNs) combine classical deep learning feature extractors with variational quantum circuits (VQCs) for enhanced discriminative representations in medical imaging tasks. Validated on blood cell classification with measurable improvements over classical baselines.

**Source**: arXiv:2605.23324v1 (May 2026) — "Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks"

## Core Architecture

```
Input Image → Pre-trained CNN (ResNet-50) → Latent Bottleneck → VQC → Classifier → Output
```

### Key Design Decisions

1. **Backbone Selection**: Use pre-trained ResNet-50 (or equivalent) as fixed feature extractor
2. **Dimensionality Reduction**: Bottleneck layer compresses features to match qubit count (typically 4-8 qubits)
3. **Variational Quantum Circuit**: Parameterized quantum gates for non-linear feature transformation
4. **Classical Classifier**: Standard fully-connected layers on top of quantum output

## Three-Model Comparison Methodology

To isolate the quantum contribution, always evaluate three architectures:

| Model | Description | Purpose |
|-------|-------------|---------|
| **HQNN** | CNN + VQC | Full quantum-enhanced model |
| **Classical Matched** | CNN + extra nonlinear layer (same capacity as VQC) | Controls for parameter count |
| **Baseline** | CNN only (no intermediate layer) | Establishes baseline performance |

### Why Three Models?

- **Classical Matched** proves the improvement comes from quantum effects, not just more parameters
- **Baseline** shows the absolute improvement needed
- Only when HQNN > Classical Matched > Baseline can you claim quantum advantage

## Training Protocol

1. **Freeze Backbone**: Keep pre-trained CNN weights frozen during VQC training
2. **Train VQC + Classifier**: Only train variational parameters and final classifier
3. **Optimizer**: Use gradient-based optimizer (Adam/AdamW) with learning rate scheduling
4. **Batch Size**: Small batches (8-32) for stable VQC gradient estimation
5. **Epochs**: Typically 20-50 epochs (VQC training converges faster than full CNN)

## Implementation Pattern

```python
import torch
import torch.nn as nn
from torchvision import models

class HQNN(nn.Module):
    def __init__(self, num_classes, num_qubits=6):
        super().__init__()
        # Pre-trained backbone
        backbone = models.resnet50(weights='IMAGENET1K_V1')
        self.backbone = nn.Sequential(*list(backbone.children())[:-1])
        
        # Bottleneck to match qubit count
        self.bottleneck = nn.Linear(2048, num_qubits)
        
        # VQC (use PennyLane/Qiskit)
        self.vqc = VariationalQuantumCircuit(num_qubits)
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(num_qubits, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )
    
    def forward(self, x):
        features = self.backbone(x).squeeze()
        encoded = self.bottleneck(features)
        quantum_output = self.vqc(encoded)
        return self.classifier(quantum_output)
```

## Performance Benchmarks

From the paper (blood cell classification):
- **Blood Cell Images Dataset**: HQNN improves macro F1-score by up to 3.7% over classical baselines
- **PBC Dataset (8-class)**: F1-score from 98.54% → 98.69% (near-saturated performance)
- **IBM Quantum Hardware**: Modest degradation vs simulation, proving noise robustness

## Noise Robustness

- Test on **real quantum hardware** (IBM Quantum) alongside simulator
- Expect 1-3% performance drop on real hardware vs simulation
- This validates the model's resilience to NISQ-era noise

## When to Use

- Medical image classification with limited data
- Tasks where classical performance is near-saturation and small gains matter
- Research comparing quantum vs classical feature representations
- Binary or multi-class classification of microscopic/medical images

## Activation

hybrid quantum neural network, HQNN, medical image classification, blood cell, variational quantum circuit, quantum-classical hybrid, ResNet, feature representation, noise robustness
