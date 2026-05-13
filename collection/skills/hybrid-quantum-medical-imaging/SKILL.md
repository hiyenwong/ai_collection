---
name: hybrid-quantum-medical-imaging
description: >
  Hybrid Quantum-Classical Neural Network methodology for medical image analysis,
  specifically thermographic breast cancer classification. Combines quantum variational
  circuits with classical CNN backbones to leverage quantum advantage in complex thermal
  pattern discrimination. Use when building quantum-enhanced medical imaging classifiers,
  HQNN architectures, thermographic cancer detection systems, or quantum-classical
  feature fusion for healthcare AI. Activation: hybrid quantum neural network, quantum
  medical imaging, thermographic cancer detection, HQNN breast cancer, quantum healthcare AI.
---

# Hybrid Quantum Medical Imaging

## Architecture Pattern

Combine quantum variational circuits with classical CNN backbones for medical image classification:

```
Input Image -> Classical CNN Backbone -> Feature Vector
                                           |
                                    Quantum Encoding
                                           |
                               Variational Quantum Circuit
                                           |
                              Quantum Measurement -> Classification
```

## Key Design Decisions

### Classical Backbone Selection
- Use lightweight CNNs (ResNet18, EfficientNet-B0) for feature extraction
- Freeze backbone layers during quantum circuit training
- Extract mid-level features (before final FC layer) for quantum encoding

### Quantum Circuit Design
- Use parameterized rotation gates (RY, RZ) for encoding
- Implement entangling layers (CNOT, CZ) for quantum advantage
- Keep circuit depth ≤ 4 for NISQ-era hardware compatibility
- Use amplitude or angle encoding based on feature dimensionality

### Training Strategy
- Two-phase training: freeze quantum while training classical, then joint fine-tuning
- Use hybrid loss: classical cross-entropy + quantum measurement expectation
- Apply gradient clipping to prevent quantum gradient explosion
- Use parameter-shift rule for quantum gradient computation

## Implementation Example

```python
import pennylane as qml
from pennylane import numpy as pnp
import torch

def create_quantum_layer(n_qubits, n_layers):
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(inputs, weights):
        # Encoding
        for i in range(n_qubits):
            qml.RY(inputs[i], wires=i)
        
        # Variational layers
        for layer in range(n_layers):
            for i in range(n_qubits):
                qml.Rot(*weights[layer, i], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i+1])
        
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
    
    weight_shapes = {"weights": (n_layers, n_qubits, 3)}
    return qml.qnn.TorchLayer(circuit, weight_shapes)

# Integration with classical backbone
class HQNNClassifier(torch.nn.Module):
    def __init__(self, backbone, n_qubits=4, n_layers=3):
        super().__init__()
        self.backbone = backbone
        self.feature_extractor = torch.nn.Sequential(*list(backbone.children())[:-1])
        self.quantum_layer = create_quantum_layer(n_qubits, n_layers)
        self.classifier = torch.nn.Linear(n_qubits, 2)
    
    def forward(self, x):
        features = self.feature_extractor(x).squeeze()
        quantum_output = self.quantum_layer(features[:n_qubits])
        return self.classifier(quantum_output)
```

## Medical Imaging Applications

- Thermographic breast cancer classification
- X-ray pneumonia detection
- MRI tumor segmentation
- Histopathology image analysis
- Dermatology lesion classification

## Pitfalls

- Quantum circuits add significant computational overhead; only use when classical approaches plateau
- Shot noise in quantum measurements can destabilize training; use shot=1024 minimum
- NISQ hardware limitations restrict practical qubit counts to ~20-50
- Quantum advantage is dataset-dependent; benchmark against classical baselines first
