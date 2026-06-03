---
name: distributed-quantum-cnn-medical
description: "Distributed hybrid quantum convolutional neural network with quantum circuit splitting for medical image classification. Reduces qubit requirements by splitting quantum circuits across distributed nodes. Use when building quantum CNNs for medical image classification under resource constraints, implementing quantum circuit splitting/distribution, or training QCNN models with fewer qubits than the full circuit requires."
---

# Distributed Hybrid QCNN for Medical Image Classification

Build distributed quantum convolutional neural networks using quantum circuit splitting to reduce qubit requirements for medical image classification.

## Core Technique: Quantum Circuit Splitting

Split an N-qubit QCNN into M smaller sub-circuits (M < N qubits each), run in parallel or sequentially, then aggregate results.

### Architecture

```
Medical Image → Classical Preprocessing → Feature Map
    ↓
[Sub-circuit 1: qubits 0-4] → Results_1
[Sub-circuit 2: qubits 5-9] → Results_2
[Sub-circuit 3: qubits 10-14] → Results_3
    ↓
Classical Aggregation → Classification
```

### Implementation Pattern

```python
import pennylane as qml

def split_qcnn(image_features, n_qubits_per_split=5):
    """Split 8-qubit QCNN into 5-qubit sub-circuits."""
    
    # Split features across sub-circuits
    splits = split_features(image_features, n_qubits_per_split)
    
    results = []
    for split_features in splits:
        sub_result = run_subcircuit(split_features, n_qubits_per_split)
        results.append(sub_result)
    
    # Classical aggregation
    return aggregate_results(results)

def run_subcircuit(features, n_qubits):
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(f, params):
        # Encoding
        for i in range(n_qubits):
            qml.RY(f[i], wires=i)
        
        # Quantum convolution layers
        for layer in range(2):
            # Convolution via entangling gates
            for i in range(n_qubits - 1):
                qml.CRY(params[layer, i], wires=[i, i+1])
            # Pooling via measurement
            qml.measure(0)
        
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
    
    return circuit(features, trainable_params())
```

## Benefits

- **Reduced qubit count**: 8-qubit QCNN runs on 5-qubit hardware
- **Distributed training**: Sub-circuits can train in parallel
- **Resource-constrained deployment**: Works on current NISQ devices
- **Fewer parameters**: Achieves strong performance with reduced model size

## Evaluation

- Test on medical image datasets (binary and multiclass classification)
- Compare against full-circuit QCNN and classical baselines
- Measure performance vs. qubit count tradeoff
- Evaluate scaling with circuit split size

## Related Papers

- arXiv:2501.06225 — Distributed Hybrid QCNN for Medical Image Classification
- arXiv:2605.08324 — Federated Quantum Medical Diagnosis

## Activation

Keywords: distributed quantum CNN, quantum circuit splitting, split QCNN, resource-constrained quantum medical, quantum medical image classification
