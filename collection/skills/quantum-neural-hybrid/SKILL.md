---
name: quantum-neural-hybrid
version: v1.0.0
last_updated: 2026-04-06
description: Hybrid classical-quantum neural network development skill. Provides workflows for transfer learning, quantum error mitigation, and noise-resistant quantum neural networks. Use when working with quantum machine learning (QML), variational quantum circuits (VQC), quantum-classical hybrid architectures, or implementing quantum neural networks on NISQ devices. Supports PennyLane, Qiskit, and other quantum ML frameworks.
---

# Quantum Neural Hybrid

## Overview

Enables development of hybrid classical-quantum neural networks for quantum machine learning on NISQ (Noisy Intermediate-Scale Quantum) devices. Combines classical deep learning with variational quantum circuits for enhanced computational capabilities.

## Workflow Decision Tree

```
User Request → Identify QML Task Type
├── Transfer Learning → Hybrid Transfer Workflow
├── Error Mitigation → Quantum Error Mitigation Workflow
├── Noise-Robust Training → Robust QNN Training Workflow
└── General QNN → Standard QNN Development Workflow
```

## 1. Hybrid Transfer Learning Workflow

**When to use**: Pre-trained classical network + quantum circuit augmentation

### Step 1: Prepare Classical Network
```python
# Load pre-trained classical model
import torch
import pennylane as qml

class ClassicalNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )
    
    def forward(self, x):
        return self.features(x)

# Load pre-trained weights
model = ClassicalNetwork()
model.load_state_dict(torch.load('pretrained_weights.pth'))
```

### Step 2: Design Quantum Circuit
```python
n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    # Encoding layer
    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)
    
    # Variational layers
    for layer in range(n_layers):
        for i in range(n_qubits):
            qml.Rot(weights[layer, i, 0],
                   weights[layer, i, 1],
                   weights[layer, i, 2], wires=i)
        # Entangling
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i+1])
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### Step 3: Create Hybrid Architecture
```python
class HybridModel(nn.Module):
    def __init__(self, classical_model, quantum_circuit):
        super().__init__()
        self.classical = classical_model
        self.quantum = quantum_circuit
        self.q_weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))
    
    def forward(self, x):
        classical_out = self.classical(x)
        quantum_out = self.quantum(classical_out, self.q_weights)
        return quantum_out

hybrid_model = HybridModel(model, quantum_circuit)
```

### Step 4: Fine-tune with Transfer Learning
```python
# Freeze classical layers
for param in hybrid_model.classical.parameters():
    param.requires_grad = False

# Train quantum layers only
optimizer = torch.optim.Adam([hybrid_model.q_weights], lr=0.01)

for epoch in range(epochs):
    loss = train_step(hybrid_model, data)
    optimizer.step()
```

**Reference**: Transfer learning in hybrid classical-quantum neural networks (arXiv:1912.08278)

## 2. Quantum Error Mitigation Workflow

**When to use**: Noisy quantum simulations requiring error correction

### Step 1: Generate Training Data via Echo Evolution
```python
def echo_evolution_data(circuit, time_steps):
    """Generate noise-free reference using echo evolution"""
    # Forward evolution
    forward_data = run_circuit(circuit, time_steps)
    # Echo evolution (reverse)
    echo_data = run_circuit(circuit.reverse(), time_steps)
    # Average for error mitigation baseline
    return (forward_data + echo_data) / 2
```

### Step 2: Train Neural Network Error Mitigator
```python
class ErrorMitigator(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(noisy_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, clean_dim)
        )
    
    def forward(self, noisy_data):
        return self.network(noisy_data)

# Training
mitigator = ErrorMitigator()
noisy_data = run_noisy_circuit(circuit)
clean_data = echo_evolution_data(circuit, time_steps)

loss = F.mse_loss(mitigator(noisy_data), clean_data)
```

**Reference**: Echo-evolution data generation for quantum error mitigation (arXiv:2311.00487)

## 3. Robust QNN Training Workflow

**When to use**: Training quantum neural networks under noise and decoherence

### Key Techniques

1. **Noise-Aware Loss Function**
```python
def robust_loss(model_output, target, noise_level):
    # Standard loss
    base_loss = F.mse_loss(model_output, target)
    # Noise penalty
    noise_penalty = noise_level * variance(model_output)
    return base_loss + noise_penalty
```

2. **Dropout in Quantum Circuits**
```python
@qml.qnode(dev)
def dropout_qnn(inputs, weights, dropout_rate):
    # Regular encoding
    encode_inputs(inputs)
    
    # Dropout gates (randomly disable)
    for i in range(n_qubits):
        if random() > dropout_rate:
            apply_rotation(weights[i], wires=i)
    
    return measurements
```

**References**: 
- Quantum Learning with Noise and Decoherence (arXiv:1612.07593)
- A General Approach to Dropout in Quantum Neural Networks (arXiv:2310.04120)

## 4. Noise Handling Strategies

### Types of Quantum Noise

1. **Decoherence**: Loss of quantum coherence
   - Solution: Use noise-aware loss functions
   - Monitor: Track variance in quantum outputs

2. **Sampling Noise**: Finite measurement statistics
   - Solution: Increase measurement shots
   - Mitigation: Use error mitigation networks

3. **Gate Errors**: Imperfect quantum operations
   - Solution: Circuit optimization
   - Compensation: Calibration-aware parameters

### Noise-Robust Training Tips

- Start with high noise levels, gradually reduce
- Use batch averaging to reduce sampling noise
- Implement noise injection during training
- Validate on real quantum hardware if available

## Common Use Cases

### Use Case 1: Quantum Image Classification
```
Classical CNN → Feature Extraction → Quantum Circuit → Classification
```

### Use Case 2: Quantum Financial Modeling
```
Time Series Encoder → Quantum Embedding → Variational Layer → Prediction
```

### Use Case 3: Quantum Drug Discovery
```
Molecular Encoder → Quantum Similarity Circuit → Property Prediction
```

## Resources

This skill includes resources for quantum-classical hybrid neural network development:

### scripts/
- `hybrid_transfer_example.py`: Complete transfer learning example
- `error_mitigation_nn.py`: Neural network-based error mitigation
- `noise_robust_training.py`: Training scripts for noisy QNNs

### references/
- `quantum_ml_frameworks.md`: PennyLane, Qiskit, TensorFlow Quantum usage guide
- `noise_models.md`: Quantum noise types and mitigation strategies
- `nisq_best_practices.md`: Best practices for NISQ device development

### assets/
- `hybrid_model_template.py`: Boilerplate for hybrid architectures
- `quantum_circuit_templates/`: Pre-designed quantum circuit architectures

**Note**: Delete example files and replace with actual implementations.

## Frameworks

### PennyLane
```python
import pennylane as qml

# Most recommended for research
dev = qml.device("default.qubit", wires=4)
```

### Qiskit
```python
from qiskit import QuantumCircuit
from qiskit_machine_learning import QNN

# Good for IBM hardware integration
```

### TensorFlow Quantum
```python
import tensorflow_quantum as tfq

# Best for hybrid classical-quantum models
```

## Error Handling

### Common Errors

1. **Dimension Mismatch**
   - Check classical output matches quantum input dimensions
   - Solution: Add dimension adapter layer

2. **Noise Overwhelming Signal**
   - Reduce noise level in training
   - Increase measurement shots

3. **Training Convergence Issues**
   - Adjust learning rates
   - Use classical optimizer warm-start

### Recovery Steps

- Validate quantum circuit on simulator first
- Test classical network separately
- Use gradient clipping for stability
- Monitor loss curves for both components

## Examples

### Example 1: Basic Hybrid Model

**User Request**: "Create a hybrid quantum-classical network for image classification"

**Workflow**:
1. Load pre-trained CNN (ResNet, VGG)
2. Design 4-qubit variational circuit
3. Connect via hybrid architecture
4. Fine-tune on quantum layers

### Example 2: Error Mitigation

**User Request**: "Reduce noise in quantum circuit simulations"

**Workflow**:
1. Generate echo evolution data
2. Train neural network mitigator
3. Apply to noisy circuit outputs
4. Validate error reduction

### Example 3: Robust Training

**User Request**: "Train QNN that works on noisy hardware"

**Workflow**:
1. Inject noise during training
2. Use noise-aware loss function
3. Implement dropout in quantum layers
4. Test on real/simulated noisy hardware

## Related Skills

- `quantum-finance-analysis`: Quantum applications in finance
- `spikingjelly-framework`: Spiking neural networks (alternative neuromorphic approach)
- `neural-dynamics-universal-translator`: Neural dynamics modeling

## References

1. **Transfer Learning**: Mari et al., "Transfer learning in hybrid classical-quantum neural networks" (arXiv:1912.08278)
2. **Error Mitigation**: Babukhin, "Echo-evolution data generation for quantum error mitigation via neural networks" (arXiv:2311.00487)
3. **Noise Robustness**: Nguyen et al., "Quantum Learning with Noise and Decoherence" (arXiv:1612.07593)
4. **Dropout**: Scala et al., "A General Approach to Dropout in Quantum Neural Networks" (arXiv:2310.04120)

---

*This skill enables quantum machine learning development on NISQ devices, combining classical deep learning advantages with quantum computational capabilities.*
