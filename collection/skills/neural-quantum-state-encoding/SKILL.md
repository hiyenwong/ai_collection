---
name: neural-quantum-state-encoding
description: Quantum state preparation via neural network encoding methodology. Maps classical data to quantum circuit parameters using a trained neural network, avoiding iterative variational optimization for each data instance. Achieves high-fidelity state preparation (up to 0.992) with 5000x speedup over per-instance optimization. Use when designing quantum machine learning pipelines that need efficient data loading, amplitude encoding, or scalable quantum state preparation on NISQ devices. Applies to quantum image processing, quantum classification, and hybrid quantum-classical models where data encoding is a bottleneck.
---

# Neural Quantum State Encoding

Methodology from Aoun & Kiwit (arXiv:2605.31006, May 2026).

## Problem

State preparation is the bottleneck in quantum machine learning. Amplitude encoding represents 2^n-dimensional data with n qubits, but preparing arbitrary states requires variational optimization of a parameterized quantum circuit for each data instance — computationally prohibitive at scale.

## Solution

Train a classical neural network to map input data directly to the continuous parameters of a **fixed** quantum circuit. All optimization is performed once during training; new inputs are encoded in a single inference step.

## Core Architecture

```
Input Data → Neural Network → Circuit Parameters → Fixed Quantum Circuit → Quantum State
```

### Key Design Choices

1. **Fixed circuit topology** — only parameters vary, not structure
2. **Neural network** learns the mapping x → θ(x) where θ are circuit parameters
3. **Single inference** per new data point — no iterative optimization at inference time
4. **Generalizes** to unseen data with high fidelity

## Results (validated on MNIST, Fashion-MNIST)

- Fidelity up to **0.992** on unseen images
- **5000x+ speedup** in per-data-instance runtime vs. variational optimization
- Generalizes well beyond training distribution

## Implementation Workflow

### 1. Design the Parameterized Circuit

```python
# Choose a fixed ansatz with tunable parameters
# Example: hardware-efficient ansatz with rotation gates
def create_ansatz(n_qubits, n_layers):
    """Fixed circuit topology with n_layers * n_qubits parameters"""
    # Alternating layers of single-qubit rotations + entangling gates
    pass
```

### 2. Train the Encoder Network

```python
# Neural network: input_dim → hidden → output_dim (circuit parameters)
class QuantumEncoder(nn.Module):
    def __init__(self, input_dim, n_qubits, n_layers):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, n_qubits * n_layers * 3)  # 3 rotation angles per qubit per layer
        )
    
    def forward(self, x):
        return self.net(x)

# Training loop: optimize for state fidelity
# Loss: 1 - |⟨ψ_target|ψ_predicted⟩|²
def fidelity_loss(predicted_params, target_state, circuit):
    predicted_state = circuit(predicted_params)
    return 1.0 - torch.abs(torch.dot(predicted_state, target_state.conj())) ** 2
```

### 3. Inference (Data Loading)

```python
# Once trained, encode any new data point in a single forward pass
def encode_data(encoder, data_point, circuit):
    params = encoder(data_point)  # Single inference, no optimization
    return circuit(params)  # Prepare quantum state
```

## When to Use

- QML pipeline with high-dimensional classical data
- Need to load many data points into quantum states
- Variational per-instance optimization is too slow
- Working with NISQ devices with limited coherence time

## Comparison with Alternatives

| Method | Per-instance cost | Generalization | Fidelity |
|--------|------------------|----------------|----------|
| Variational opt | O(iterations × circuit_depth) | N/A | High |
| Amplitude encoding | O(2^n gates) | N/A | Exact |
| **Neural encoding (this)** | **O(1 forward pass)** | **Generalizes** | **~0.99** |

## Pitfalls

- Circuit must be expressive enough to represent target state manifold
- Training requires representative data distribution
- Fidelity degrades on out-of-distribution inputs — monitor generalization
- Not suitable when exact state preparation is required (fidelity < 1.0)

## Activation

neural quantum state encoding, quantum data loading, QML state preparation, amplitude encoding optimization, quantum circuit parameterization, quantum image states
