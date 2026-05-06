---
name: quantum-eeg-foundation
description: Quantum-enhanced EEG signal analysis and neural network foundation model skill. Implements quantum-classical hybrid architectures for brain signal processing, combining quantum encoding layers with classical EEGNet for improved feature extraction from high-dimensional EEG data. Use when developing BCI systems, EEG analysis pipelines, quantum-neuroscience applications, or quantum machine learning for brain signal processing.
---

# Quantum EEG Foundation

## Overview

Enables quantum-enhanced EEG signal analysis through hybrid quantum-classical neural networks. Combines quantum computing advantages with established EEGNet architectures for improved encoding of complex, high-dimensional brain signals. Based on QEEGNet (arXiv:2407.19214) research pattern.

## Workflow Decision Tree

```
EEG Analysis Request → Identify Task Type
├── BCI System Development → QEEGNet Hybrid Architecture
├── Signal Classification → Quantum Feature Extraction Workflow
├── Real-time Processing → Optimized Quantum Encoding
└── Research/Exploration → Full QEEGNet Implementation
```

## 1. QEEGNet Hybrid Architecture

**Core Pattern**: Integrate quantum encoding layer with classical EEGNet

### Architecture Overview
```
Raw EEG Signal → Temporal Filter → Spatial Filter → Quantum Encoding Layer → Classification
                      ↓                ↓                    ↓                    ↓
                 EEGNet Core    EEGNet Core        Variational Circuit    Output Layer
```

### Step 1: Prepare EEGNet Backbone
```python
import torch
import pennylane as qml

class EEGNetBackbone(nn.Module):
    """Classical EEGNet architecture for EEG processing"""
    def __init__(self, n_channels, n_samples, n_classes):
        super().__init__()
        # Temporal convolution
        self.temporal_conv = nn.Conv2d(1, 8, (1, 64), padding=(0, 32))
        # Spatial convolution
        self.spatial_conv = nn.Conv2d(8, 16, (n_channels, 1))
        # Separable convolution
        self.separable_conv = nn.Conv2d(16, 16, (1, 16), padding=(0, 8))
        
    def forward(self, x):
        x = self.temporal_conv(x)
        x = self.spatial_conv(x)
        x = self.separable_conv(x)
        return x.view(x.size(0), -1)  # Flatten for quantum layer
```

### Step 2: Design Quantum Encoding Layer
```python
n_qubits = 4  # Adjust based on feature dimension
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_eeg_layer(features, weights):
    """Quantum encoding for EEG features"""
    # Angle encoding - map EEG features to rotation angles
    for i in range(n_qubits):
        qml.RY(features[i] * np.pi, wires=i)  # Scale features to [0, π]
    
    # Variational layers for quantum feature extraction
    for layer in range(n_layers):
        # Rotation gates
        for i in range(n_qubits):
            qml.Rot(weights[layer, i, 0],
                    weights[layer, i, 1],
                    weights[layer, i, 2], wires=i)
        # Entangling gates (create quantum correlations)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i+1])
        qml.CNOT(wires=[n_qubits-1, 0])  # Circular entanglement
    
    # Measurement - extract quantum features
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Step 3: Create QEEGNet Hybrid Model
```python
class QEEGNet(nn.Module):
    """Quantum-enhanced EEGNet"""
    def __init__(self, backbone, quantum_layer, n_classes):
        super().__init__()
        self.backbone = backbone
        self.quantum = quantum_layer
        self.q_weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3) * 0.1)
        self.classifier = nn.Linear(n_qubits, n_classes)
        
    def forward(self, x):
        # Classical EEGNet feature extraction
        features = self.backbone(x)
        # Reduce dimension for quantum layer (n_qubits features)
        features = features[:, :n_qubits]
        # Quantum enhancement
        quantum_features = self.quantum(features, self.q_weights)
        # Classification
        return self.classifier(torch.stack(quantum_features).T)
```

### Step 4: Train QEEGNet
```python
def train_qeegnet(model, train_data, epochs=100):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        for batch_x, batch_y in train_data:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
    return model
```

## 2. Quantum Feature Extraction

**Key Advantage**: Quantum circuits can capture complex correlations in EEG signals

### Quantum Encoding Strategies

1. **Angle Encoding**: Direct feature → rotation angle mapping
2. **Amplitude Encoding**: Normalize features as quantum state amplitudes
3. **Basis Encoding**: Binary encoding for discrete features

### Feature Dimension Handling
```python
def dimension_adapter(features, target_dim=n_qubits):
    """Adapt high-dimensional EEG features to quantum layer"""
    # Option 1: PCA reduction
    pca = PCA(n_components=target_dim)
    return pca.fit_transform(features)
    
    # Option 2: Feature selection
    return features[:, :target_dim]
    
    # Option 3: Learned projection
    projection = nn.Linear(features.shape[1], target_dim)
    return projection(features)
```

## 3. BCI Applications

### Motor Imagery Classification
```python
# QEEGNet for motor imagery BCI
model = QEEGNet(
    backbone=EEGNetBackbone(n_channels=64, n_samples=512),
    quantum_layer=quantum_eeg_layer,
    n_classes=4  # Left hand, right hand, feet, tongue
)
```

### Emotion Recognition
```python
# QEEGNet for emotion recognition
model = QEEGNet(
    backbone=EEGNetBackbone(n_channels=32, n_samples=256),
    quantum_layer=quantum_eeg_layer,
    n_classes=2  # Positive, negative
)
```

## 4. Optimization Strategies

### Noise Handling
```python
# Increase measurement shots for better statistics
dev = qml.device("default.qubit", wires=n_qubits, shots=1000)

# Use error mitigation
@qml.qnode(dev)
def quantum_eeg_layer_robust(features, weights):
    # ... circuit ...
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Batch Processing
```python
def batch_quantum_processing(model, eeg_batch):
    """Process multiple EEG samples efficiently"""
    results = []
    for sample in eeg_batch:
        quantum_out = model.quantum(sample, model.q_weights)
        results.append(quantum_out)
    return torch.stack(results)
```

## Key Research Findings

From QEEGNet paper (arXiv:2407.19214):
- Quantum encoding improves EEG feature extraction efficiency
- Hybrid architecture outperforms pure classical on complex EEG tasks
- Quantum layer reduces computational overhead for high-dimensional data
- Suitable for BCI systems requiring real-time processing

## Framework Compatibility

### PennyLane (Recommended)
```python
import pennylane as qml
# Best for research and flexibility
```

### Qiskit Machine Learning
```python
from qiskit_machine_learning import QNN
# Good for IBM hardware integration
```

### TensorFlow Quantum
```python
import tensorflow_quantum as tfq
# Best for hybrid classical-quantum models
```

## Resources

### references/
- `qeegnet_paper.md`: QEEGNet paper summary (arXiv:2407.19214)
- `eeg_encoding.md`: Quantum encoding strategies for EEG
- `bci_applications.md`: BCI use cases and implementations

### assets/
- `qeegnet_template.py`: QEEGNet boilerplate code

## Related Skills

- `quantum-neural-hybrid`: General quantum-classical hybrid architectures
- `quantum-neuroscience-analysis`: Quantum neuroscience research patterns
- `spikingjelly-framework`: Alternative neuromorphic approach (spiking neural networks)

## References

1. QEEGNet: Quantum Machine Learning for Enhanced Electroencephalography Encoding (arXiv:2407.19214)
2. EEGNet: A Compact Convolutional Neural Network for EEG-based BCIs
3. Transfer learning in hybrid classical-quantum neural networks (arXiv:1912.08278)

---

*This skill enables quantum-enhanced EEG analysis for neuroscience and BCI applications.*