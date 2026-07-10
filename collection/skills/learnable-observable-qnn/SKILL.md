---
name: learnable-observable-qnn
description: "Learnable Observable Quantum Neural Network methodology. Makes quantum measurement observables (Hermitian matrices) trainable parameters alongside circuit parameters. Reduces expert dependency in QML. Activation: quantum observable, QNN measurement, learnable observable, quantum neural network training, QML optimization."
---

# Learnable Observable QNN (LO-QNN)

Making quantum measurement observables trainable parameters in Quantum Neural Networks (QNNs). Eliminates the need for expert-crafted Hermitian measurement operators by learning them end-to-end alongside circuit parameters.

## Core Concept

Traditional QNNs require manually designed measurement observables (Hermitian matrices) to extract classical outputs from quantum states. LO-QNN parameterizes the observable and trains it jointly with the quantum circuit via gradient descent.

### Mathematical Formulation

The QNN output is:
```
f(x) = ⟨ψ(x, θ)| O(φ) |ψ(x, θ)⟩
```

Where:
- `|ψ(x, θ)⟩` is the quantum state from parameterized circuit with parameters θ
- `O(φ)` is the parameterized observable with trainable parameters φ
- Both θ and φ are optimized simultaneously via backpropagation

### Observable Parameterization

The observable O(φ) is parameterized as:
```
O(φ) = Σᵢ φᵢ Pᵢ
```
Where Pᵢ are Pauli string basis operators and φᵢ are trainable coefficients.

Alternatively, parameterize via unitary rotation:
```
O(φ) = U(φ)† Z U(φ)
```
Where U(φ) is a parameterized unitary and Z is a fixed measurement operator.

## Implementation Steps

### Step 1: Parameterize the Observable

```python
import torch
import numpy as np

class LearnableObservable:
    def __init__(self, num_qubits):
        # Learnable coefficients for Pauli basis decomposition
        self.coefficients = torch.nn.Parameter(
            torch.randn(4**num_qubits) * 0.01
        )
        self.num_qubits = num_qubits
    
    def forward(self):
        # Reconstruct observable from learned coefficients
        return self.build_pauli_observable(self.coefficients)
    
    def build_pauli_observable(self, coeffs):
        """Build Hermitian observable from Pauli basis."""
        # Implementation depends on quantum framework (PennyLane, Qiskit)
        pass
```

### Step 2: Joint Training Loop

```python
def train_qnn_with_learnable_observable(qnn_circuit, observable, 
                                          data, labels, epochs, lr=0.01):
    optimizer = torch.optim.Adam([
        *qnn_circuit.parameters(),
        *observable.parameters()
    ], lr=lr)
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        
        # Forward: quantum circuit + learnable measurement
        outputs = []
        for x in data:
            state = qnn_circuit(x)  # Prepare quantum state
            obs_matrix = observable()  # Get current observable
            pred = torch.expectation(state, obs_matrix)
            outputs.append(pred)
        
        loss = torch.nn.MSELoss()(torch.stack(outputs), labels)
        loss.backward()
        optimizer.step()
    
    return qnn_circuit, observable
```

### Step 3: PennyLane Implementation

```python
import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def lo_qnn_circuit(inputs, circuit_params, obs_params, wires):
    # Encoding
    for i, w in enumerate(wires):
        qml.RY(inputs[i], wires=w)
    
    # Parameterized quantum circuit
    for i, w in enumerate(wires):
        qml.Rot(*circuit_params[i], wires=w)
    qml.CNOT(wires=[0, 1])
    
    # Measurement with learnable coefficients
    coeffs = obs_params
    paulis = [qml.PauliX, qml.PauliY, qml.PauliZ]
    hamiltonian = coeffs[0] * qml.PauliZ(0) + coeffs[1] * qml.PauliZ(1) + coeffs[2] * qml.PauliZ(0) @ qml.PauliZ(1)
    return qml.expval(hamiltonian)
```

## When to Use

- QML model design without measurement expertise
- Quantum circuits where optimal measurement basis is unknown
- Hybrid quantum-classical training pipelines
- NISQ-era variational quantum algorithms
- Tasks requiring adaptive quantum measurements

## Advantages

1. **Reduced Expert Dependency**: No need to hand-craft measurement operators
2. **Adaptive Measurements**: Observable evolves during training to match the task
3. **End-to-End Differentiability**: Full gradient flow from loss to both circuit and observable
4. **Better Convergence**: Joint optimization can find better optima than fixed observables
5. **Framework Agnostic**: Works with PennyLane, Qiskit, Cirq

## Key Pitfalls

1. **Observable Norm**: Without constraints, learned observables can grow unbounded. Add regularization: `λ * ||O(φ)||²`
2. **Barren Plateaus**: Parameterized observables may worsen gradient vanishing. Use layerwise training.
3. **Measurement Complexity**: Full Pauli decomposition scales as 4^n. Use truncated basis for large systems.
4. **Overparameterization**: Observable params + circuit params = more parameters than data points. Use weight decay.
5. **Hardware Constraints**: On real quantum devices, decompose learned observable into measurable terms.

## Verification

```python
# Verify Hermiticity of learned observable
def verify_observable(O):
    import torch
    assert torch.allclose(O, O.conj().T), "Observable not Hermitian!"
    eigenvalues = torch.linalg.eigvalsh(O)
    print(f"Eigenvalue range: [{eigenvalues.min():.4f}, {eigenvalues.max():.4f}]")
    
# Training convergence check
def check_convergence(loss_history, window=10, threshold=1e-4):
    recent = loss_history[-window:]
    return max(recent) - min(recent) < threshold
```

## Activation Keywords

- learnable observable
- quantum measurement training
- QNN observable optimization
- differentiable quantum measurement
- quantum neural network measurement
- parameterized observable
- quantum ML measurement design
- QML training without expert knowledge