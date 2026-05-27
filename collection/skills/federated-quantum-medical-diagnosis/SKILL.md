---
name: federated-quantum-medical-diagnosis
description: "Federated Quantum Neural Network methodology for privacy-preserving medical image diagnosis. Combines federated learning with quantum neural networks for distributed medical imaging analysis without sharing raw patient data. Use when: federated quantum learning, privacy-preserving medical AI, distributed quantum ML for healthcare, FQPDR pattern."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.08324"
  published: "2026-05-08"
  tags: [quantum, federated-learning, medical-diagnosis, privacy, qnn]
---

# Federated Quantum Medical Diagnosis

## Overview

Combine federated learning (FL) with quantum neural networks (QNNs) for privacy-preserving medical image analysis. Each site trains a local QNN on private medical data, and only model parameters (not data) are aggregated.

## When to Use

- Multi-institutional medical image analysis without data sharing
- Early detection of subtle medical features (microaneurysms, small lesions)
- Privacy-preserving quantum ML for healthcare
- Distributed quantum neural network training across hospitals

## Architecture

### Step 1: Local QNN Design

```python
import pennylane as qml
import torch

def create_qnn(n_qubits, n_layers):
    dev = qml.device('default.qubit', wires=n_qubits)
    
    @qml.qnode(dev, interface='torch')
    def circuit(inputs, weights):
        # Data encoding (amplitude encoding for medical features)
        qml.AmplitudeEmbedding(inputs, wires=range(n_qubits), normalize=True)
        
        # Variational layers
        for layer in range(n_layers):
            for i in range(n_qubits):
                qml.Rot(weights[layer, i, 0], weights[layer, i, 1], 
                       weights[layer, i, 2], wires=i)
            for i in range(n_qubits - 1):
                qml.CNOT(wires=[i, i + 1])
        
        return qml.expval(qml.PauliZ(0))
    
    return circuit
```

### Step 2: Federated Aggregation

```python
def federated_aggregate(local_models, weights=None):
    """FedAvg for quantum neural networks"""
    if weights is None:
        weights = [1.0 / len(local_models)] * len(local_models)
    
    global_model = {}
    for key in local_models[0].keys():
        global_model[key] = sum(
            w * local_models[i][key] 
            for i, w in enumerate(weights)
        )
    return global_model
```

### Step 3: Training Loop

```python
for round in range(n_rounds):
    local_models = []
    for site in sites:
        # Train local QNN on private medical data
        model = train_local_qnn(site.data, site.labels)
        local_models.append(model.get_parameters())
    
    # Aggregate
    global_params = federated_aggregate(local_models)
    
    # Distribute global model back to sites
    for site in sites:
        site.set_parameters(global_params)
```

## Key Patterns

### Pattern 1: Quantum Feature Encoding for Medical Images

Use amplitude or angle encoding for medical image patches:
- Small image regions (patches) → quantum state preparation
- Pre-process with classical CNN for feature extraction
- Quantum circuit for fine-grained classification

### Pattern 2: Privacy Preservation Guarantees

FL ensures raw patient data never leaves local site:
- Only model gradients/parameters are shared
- Optional: add differential privacy noise to gradients
- Quantum circuits add additional obfuscation

### Pattern 3: Handling Class Imbalance

For rare disease detection (e.g., early DR):
- Use weighted loss functions in local training
- Oversample minority class with quantum data augmentation
- F1-score as primary metric (not accuracy)

## Error Handling

### Quantum Communication Overhead

QNNs require more classical communication than classical NNs:
- Compress quantum circuit parameters before transmission
- Use parameter-efficient ansatz (fewer variational parameters)
- Consider gradient compression techniques

### Non-IID Data Across Sites

Medical data distribution varies by hospital:
- Use personalized FL (partial model sharing)
- Site-specific fine-tuning after global aggregation
- Monitor per-site performance separately

## Related Skills

- quantum-medical-ai: General quantum medical AI patterns
- quantum-neural-network-designer: QNN architecture design
- medical-domain-adaptation: Medical image domain adaptation
