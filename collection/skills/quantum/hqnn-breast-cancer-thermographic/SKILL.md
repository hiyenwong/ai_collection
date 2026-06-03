---
name: hqnn-breast-cancer-thermographic
description: "Hybrid Quantum Neural Network (HQNN) architecture for breast cancer thermographic classification. Integrates parameterized quantum circuits with multi-head attention and classical CNN layers for enhanced medical thermal pattern recognition."
---

# HQNN Breast Cancer Thermographic Classification (HQNN-BCT)

## Core Concept

Hybrid Quantum Neural Network architecture that integrates **parameterized quantum circuits (PQC)** with **classical convolutional neural networks** and **multi-head attention mechanisms** for breast cancer classification from thermographic (thermal) images. Demonstrates quantum-classical synergy where quantum layers enhance feature representation beyond classical CNN capabilities alone.

**Paper**: "Hybrid Quantum Neural Networks for Enhanced Breast Cancer Thermographic Classification: A Novel Quantum-Classical Integration Approach" (arXiv:2604.16953)
**Authors**: Riza Alaudin Syah, Irwan Alnarus Kautsar, Gunawan Witjaksono, Haza Nuzly bin Abdull Hamed
**Published**: 2025 IEEE IBITeC

## Architecture

```
Thermal Image → Classical CNN → Feature Maps
                                      │
                              Multi-Head Attention
                                      │
                          Quantum-Aware Feature Encoding
                          (4-qubit variational circuit)
                          ┌─────────────────────────────┐
                          │ Strongly Entangling Layers   │
                          │ ├─ RY rotations (params)     │
                          │ ├─ CNOT entanglement chain   │
                          │ └─ Observable measurement    │
                          └─────────────────────────────┘
                                      │
                              Feature Fusion
                                      │
                              Classification Output
```

## Key Design Elements

### 1. Quantum Circuit Design
- **4-qubit variational circuit** with strongly entangling layers
- RY rotation gates for parameterized feature encoding
- CNOT chains for entanglement across qubits
- Observable-based measurement (Pauli-Z expectation values)

### 2. Multi-Head Attention for Quantum Encoding
- Attention mechanism before quantum encoding selects most relevant features
- Reduces dimensionality to match qubit count (4 features → 4 qubits)
- Prevents information loss from naive dimensionality reduction

### 3. Classical-Quantum Integration
- Classical CNN extracts spatial thermal patterns
- Quantum layer captures non-linear correlations classical layers miss
- Feature fusion combines both representations for final classification

## Implementation Pattern

```python
import torch
import torch.nn as nn
import pennylane as qml

class HQNNBreastCancer(nn.Module):
    def __init__(self, n_qubits=4, n_layers=2):
        super().__init__()
        # Classical CNN backbone
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten()
        )
        
        # Multi-head attention
        self.attention = nn.MultiheadAttention(64, num_heads=4)
        self.feature_selector = nn.Linear(64, n_qubits)
        
        # Quantum circuit
        self.n_qubits = n_qubits
        self.dev = qml.device("default.qubit", wires=n_qubits)
        
        @qml.qnode(self.dev)
        def quantum_circuit(inputs, weights):
            for i in range(n_qubits):
                qml.RY(inputs[i], wires=i)
            for layer in range(n_layers):
                for i in range(n_qubits):
                    qml.Rot(*weights[layer, i], wires=i)
                for i in range(n_qubits - 1):
                    qml.CNOT(wires=[i, i + 1])
            return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
        
        self.q_weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))
        self.quantum_layer = lambda x: torch.stack(quantum_circuit(x, self.q_weights))
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(64 + n_qubits, 32),
            nn.ReLU(),
            nn.Linear(32, 2)  # binary classification
        )
    
    def forward(self, x):
        cnn_features = self.cnn(x)
        attended, _ = self.attention(cnn_features.unsqueeze(0), 
                                      cnn_features.unsqueeze(0), 
                                      cnn_features.unsqueeze(0))
        quantum_input = torch.tanh(self.feature_selector(attended.squeeze(0)))
        quantum_output = self.quantum_layer(quantum_input)
        combined = torch.cat([cnn_features, quantum_output], dim=-1)
        return self.classifier(combined)
```

## Best Practices

1. **Attention before quantum**: Use multi-head attention to select the most discriminative features before quantum encoding — don't use random PCA
2. **Strongly entangling layers**: Alternate single-qubit rotations with CNOT chains for maximum expressivity
3. **Thermal-specific preprocessing**: Normalize thermographic images to [0,1] temperature range; thermal patterns are subtle
4. **Hybrid training**: Freeze CNN initially, train quantum + attention layers, then fine-tune end-to-end
5. **Observable design**: Pauli-Z measurements are sufficient for binary classification; consider more complex observables for multi-class

## Pitfalls

1. **Barren plateaus**: Deep quantum circuits (>6 layers) with random initialization suffer from vanishing gradients
2. **Dimension mismatch**: CNN output must match attention input dim; quantum input must match qubit count
3. **Simulation vs hardware**: Paper uses classical simulation — real quantum hardware noise may reduce advantage
4. **Thermographic data scarcity**: Limited public datasets; consider data augmentation specific to thermal patterns
5. **No quantum advantage proof**: Paper demonstrates performance improvement but doesn't establish provable quantum advantage

## Activation

Keywords: HQNN breast cancer, quantum thermographic, hybrid quantum CNN, quantum attention medical, parameterized quantum circuit medical, thermal image quantum, variational quantum classification

## Related Skills

- `quantum-neural-hybrid` - General hybrid quantum-classical neural networks
- `quantum-kernel-medical-embeddings` - Quantum kernel methods for medical AI
- `hqnn-neural-architecture-search` - HQNN architecture search
