---
name: quantum-medical-feature-fusion
description: "Adaptive hybrid quantum-classical feature fusion for medical image classification. Combines classical deep learning backbones (ResNet, ViT) with quantum circuits via three progressive fusion strategies: Static Hybrid Fusion (SHF), Dynamic Hybrid Fusion (DHF), and Temperature-Scaled Hybrid Fusion (TSHF). TSHF uses a learnable scalar to dynamically balance hybrid gradient dynamics, achieving 87.82% accuracy on BreastMNIST. Activation: quantum feature fusion, hybrid quantum medical imaging, temperature-scaled fusion, quantum breast cancer, quantum medical classification, quantum-classical fusion."
---

# Quantum Medical Feature Fusion

## Overview

Unified framework for combining classical neural network features with quantum circuit embeddings for medical image classification. Three fusion strategies provide trade-offs between simplicity, adaptivity, and performance.

## When to Use

- Medical image classification with limited labeled data
- When classical models plateau and quantum enhancement is desired
- Breast cancer, lung nodule, or dermatology image classification
- When optimizing for threshold reliability (F1, AUC-ROC) alongside accuracy
- When deploying hybrid quantum-classical architectures in clinical settings

## Three Fusion Strategies

### 1. Static Hybrid Fusion (SHF)

Offline extraction of classical and quantum features, then concatenation.

**Pros**: Simple, stable, no training interference
**Cons**: No co-adaptation between modalities
**Use when**: Quick prototyping, baseline comparison

```python
def static_hybrid_fusion(classical_features, quantum_features):
    """Concatenate pre-extracted classical and quantum features."""
    return torch.cat([classical_features, quantum_features], dim=-1)
```

### 2. Dynamic Hybrid Fusion (DHF)

End-to-end co-adaptation where both classical and quantum branches are trained jointly.

**Pros**: Full co-adaptation, potentially optimal
**Cons**: Optimization asymmetry can cause instability (quantum gradients << classical)
**Use when**: Sufficient training data, stable quantum-classical gradient dynamics

```python
class DynamicHybridFusion(nn.Module):
    def __init__(self, classical_dim, quantum_dim, hidden_dim):
        super().__init__()
        self.fusion = nn.Sequential(
            nn.Linear(classical_dim + quantum_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
    
    def forward(self, classical_features, quantum_features):
        combined = torch.cat([classical_features, quantum_features], dim=-1)
        return self.fusion(combined)
```

### 3. Temperature-Scaled Hybrid Fusion (TSHF) — Recommended

Learnable scalar (temperature) dynamically balances hybrid gradient dynamics.

**Pros**: Resolves optimization bottlenecks, achieves best performance
**Cons**: One additional hyperparameter to tune
**Use when**: Best accuracy required, gradient imbalance between classical and quantum branches

```python
class TemperatureScaledHybridFusion(nn.Module):
    def __init__(self, classical_dim, quantum_dim, init_temp=1.0):
        super().__init__()
        self.temperature = nn.Parameter(torch.tensor(init_temp))
        self.classical_proj = nn.Linear(classical_dim, quantum_dim)
    
    def forward(self, classical_features, quantum_features):
        # Project classical to quantum dimension
        c_proj = self.classical_proj(classical_features)
        
        # Temperature-scaled combination
        # Higher temperature = more classical influence
        # Lower temperature = more quantum influence
        alpha = torch.sigmoid(self.temperature)
        fused = alpha * c_proj + (1 - alpha) * quantum_features
        
        return fused, alpha  # Return alpha for monitoring
```

## Implementation Pipeline

### Step 1: Feature Extraction

```python
import torch
import torch.nn as nn
import pennylane as qml

class ClassicalBackbone(nn.Module):
    """Classical feature extractor (e.g., ResNet18)."""
    def __init__(self):
        super().__init__()
        self.backbone = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True)
        self.backbone.fc = nn.Identity()  # Remove classification head
    
    def forward(self, x):
        return self.backbone(x)  # Shape: [B, 512]

class QuantumCircuit(nn.Module):
    """Parameterized quantum circuit for feature encoding."""
    def __init__(self, n_qubits=4, n_layers=2):
        super().__init__()
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))
    
    def forward(self, x):
        """x: classical features projected to n_qubits dimensions"""
        # Encode input as rotation angles
        # Apply parameterized layers
        # Measure expectation values as output features
        features = []
        for i in range(self.n_qubits):
            # Rx, Ry, Rz with trainable weights
            pass  # PennyLane implementation
        return torch.stack(features)  # Shape: [B, n_qubits]
```

### Step 2: Full Hybrid Model

```python
class HybridQuantumMedicalClassifier(nn.Module):
    def __init__(self, strategy='tshf'):
        super().__init__()
        self.classical = ClassicalBackbone()
        self.quantum = QuantumCircuit(n_qubits=4, n_layers=2)
        self.input_proj = nn.Linear(512, 4)  # Project to qubit count
        
        if strategy == 'shf':
            self.fusion = StaticHybridFusion(512, 4)
            self.classifier = nn.Linear(516, 2)
        elif strategy == 'dhf':
            self.fusion = DynamicHybridFusion(512, 4, 128)
            self.classifier = nn.Linear(1, 2)
        elif strategy == 'tshf':
            self.fusion = TemperatureScaledHybridFusion(512, 4, init_temp=1.0)
            self.classifier = nn.Linear(4, 2)
    
    def forward(self, x):
        classical_features = self.classical(x)
        quantum_input = self.input_proj(classical_features)
        quantum_features = self.quantum(quantum_input)
        fused, alpha = self.fusion(classical_features, quantum_features)
        return self.classifier(fused), alpha
```

### Step 3: Training Loop

```python
def train_hybrid_model(model, dataloader, epochs=50, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        for images, labels in dataloader:
            outputs, alpha = model(images)
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()
            
            # Gradient clipping prevents quantum gradient explosion
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
        
        # Monitor fusion balance
        with torch.no_grad():
            if hasattr(model.fusion, 'temperature'):
                alpha_val = torch.sigmoid(model.fusion.temperature).item()
                print(f"Epoch {epoch}: alpha={alpha_val:.4f} (higher=more classical)")
```

## Key Results (BreastMNIST)

| Strategy | Accuracy | F1-Score | AUC-ROC |
|----------|----------|----------|---------|
| Classical (ResNet) | 84.2% | 88.1% | 85.6% |
| SHF | 85.1% | 89.3% | 86.8% |
| DHF | 86.5% | 90.4% | 88.1% |
| **TSHF** | **87.82%** | **91.77%** | **89.08%** |

## Pitfalls

- **Gradient asymmetry**: Quantum gradients can be orders of magnitude smaller than classical. TSHF directly addresses this.
- **Barren plateaus**: Deep quantum circuits suffer from vanishing gradients. Keep circuits shallow (2-4 layers).
- **Noisy quantum simulation**: Use shot-based simulation with sufficient shots (1000+) for stable gradients.
- **Medical data preprocessing**: Ensure images are properly normalized and resized to model input dimensions.

## References

- Paper: "On the Complementarity of Quantum and Classical Features: Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification" (arXiv: 2604.22903v1)
- Authors: Yasmin Rodrigues Sobrinho, Joao Renato Ribeiro Manesco, Joao Paulo Papa
- Dataset: BreastMNIST
