---
name: hybrid-quantum-medical-thermographic
description: "Hybrid Quantum Neural Networks (HQNN) for medical thermographic classification. Integrates quantum circuits within classical neural network layers for enhanced breast cancer detection using thermographic imaging. Use when building quantum-enhanced medical imaging classifiers, HQNN architectures, or thermographic diagnosis systems. Activation: hybrid quantum neural network medical, HQNN thermographic, quantum breast cancer thermography, quantum thermal imaging diagnosis"
---

# Hybrid Quantum Neural Networks for Thermographic Medical Diagnosis

## Overview

Combines quantum circuits with classical neural network layers to enhance medical image classification, specifically for breast cancer detection using thermographic (thermal imaging) data.

## Architecture

### HQNN Layer Integration

```
Thermal Image → Conv Layers → [Quantum Layer] → Dense Layers → Classification
                              │
                    Variational Quantum Circuit
                    (parameterized gates)
```

### Key Components

1. **Classical Preprocessing**: CNN feature extraction from thermographic images
2. **Quantum Encoding**: Classical features → quantum state (amplitude/angle encoding)
3. **Variational Quantum Layer**: Parameterized gates for quantum feature transformation
4. **Measurement + Classical Post-processing**: Observable measurement → final classification

### Quantum Layer Design

```python
import pennylane as qml
import torch

class HQNNLayer(torch.nn.Module):
    """Hybrid Quantum Neural Network layer for thermographic features."""
    
    def __init__(self, n_qubits, n_layers=2):
        super().__init__()
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.dev = qml.device("default.qubit", wires=n_qubits)
        
        # Trainable weights for each layer
        self.weights = torch.nn.Parameter(
            torch.randn(n_layers, n_qubits, 3) * 0.1
        )
    
    @qml.qnode
    def _circuit(self, features, weights):
        n_qubits = len(features)
        
        # Encode classical features
        for i in range(n_qubits):
            qml.RY(features[i], wires=i)
        
        # Variational layers
        for layer in range(len(weights)):
            for i in range(n_qubits):
                qml.Rot(weights[layer, i, 0], 
                       weights[layer, i, 1], 
                       weights[layer, i, 2], wires=i)
            # Entanglement
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i + 1])
        
        # Measurement
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
    
    def forward(self, x):
        results = []
        for features in x:
            r = self._circuit(features, self.weights)
            results.append(r)
        return torch.stack(results)
```

## Thermographic Imaging Pipeline

### Data Preprocessing
- Thermal images capture temperature distribution patterns
- Key features: temperature asymmetry, hot spot detection, vascular patterns
- Normalize temperature values to [0, 1] range
- Extract ROI (Region of Interest) for analysis

### Feature Encoding Strategy
- **Angle encoding**: Map pixel intensities to rotation angles
- **Amplitude encoding**: For high-dimensional compressed features
- **Basis encoding**: For binary thermal patterns

### Classification Output
- Binary: Benign vs Malignant
- Multi-class: BI-RADS categories
- Confidence scores with uncertainty quantification

## Pitfalls

### Feature Dimensionality
- Quantum circuits limited by available qubits
- **Solution**: Classical CNN bottleneck → small feature vector → quantum layer

### Noise on NISQ Hardware
- Thermographic classification sensitive to quantum noise
- **Solution**: Simulate with noise models during training

### Gradient Computation
- Parameter-shift rule for quantum gradients
- **Solution**: PennyLane auto-differentiation handles this

## Activation Keywords
- hybrid quantum neural network medical
- HQNN thermographic classification
- quantum breast cancer thermography
- quantum thermal imaging
- hybrid quantum medical diagnosis
- quantum layer neural network medical

## Related Patterns
- Hybrid quantum-classical feature fusion
- Tensor-network quantum federated learning
