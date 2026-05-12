---
name: federated-quantum-medical-diagnosis
description: >
  Federated Quantum Neural Network (FQNN) methodology for privacy-preserving medical diagnosis.
  Combines federated learning with quantum neural networks to train medical image classifiers
  without centralizing patient data. Use when designing privacy-preserving quantum ML systems
  for healthcare, federated quantum learning, distributed medical AI, or lightweight QNN deployment.
  Triggers: federated quantum, privacy-preserving medical AI, federated QNN, distributed quantum diagnosis,
  FQNN, quantum federated learning, medical data privacy quantum.
---

# Federated Quantum Medical Diagnosis

## Core Methodology

Integrate federated learning with quantum neural networks for medical image classification:

1. **Classical feature extraction**: Use lightweight CNN to extract features from medical images
2. **Quantum encoding**: Map classical features to quantum states via angle/data encoding
3. **Federated training**: Each client trains local QNN, sends only model parameters to server
4. **Parameter aggregation**: Server averages quantum circuit parameters (not raw data)
5. **Global model distribution**: Aggregated parameters distributed back to clients

## Architecture

```
Client 1: [Medical Images] -> [CNN Features] -> [QNN(local)] -> [params] ──┐
Client 2: [Medical Images] -> [CNN Features] -> [QNN(local)] -> [params] ──┤→ [Server: Aggregate]
Client 3: [Medical Images] -> [CNN Features] -> [QNN(local)] -> [params] ──┘
```

## Key Design Principles

- **Minimal qubits**: Use 4-6 qubits for medical classification tasks
- **Few trainable parameters**: 10-20 parameters sufficient for lightweight FQNN
- **Privacy by design**: Only model weights shared, patient data never leaves client
- **Cross-evaluation**: Test each client's model on other clients' data for robustness

## Implementation Pattern (PennyLane + PyTorch)

```python
import pennylane as qml
import torch

def quantum_layer(n_qubits=4):
    dev = qml.device('default.qubit', wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(inputs, weights):
        # Data encoding
        for i in range(n_qubits):
            qml.RY(inputs[i], wires=i)
        
        # Variational layers
        for layer in range(2):
            for i in range(n_qubits):
                qml.Rot(*weights[layer, i], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i + 1])
        
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
    
    return circuit

# Federated aggregation
def federated_aggregate(client_params, weights=None):
    if weights is None:
        weights = torch.ones(len(client_params)) / len(client_params)
    return sum(w * p for w, p in zip(weights, client_params))
```

## Datasets for Validation

- E-Ophtha (diabetic retinopathy microaneurysm detection)
- Retina MNIST (retinal image classification)
- Kaggle DR datasets

## Activation Keywords
- federated quantum neural network
- privacy-preserving quantum diagnosis
- FQNN medical
- federated QNN
- quantum federated learning
- distributed quantum medical AI
- patient data privacy quantum
- cross-evaluation quantum model
