---
name: hqnn-neural-architecture-search
description: "Hybrid Quantum-Classical Neural Architecture Search methodology. FLOPs-aware NAS for HQNN design combining parameterized quantum circuits with classical neural networks. Covers encoding strategies, circuit topology selection, measurement design, and hardware-constrained optimization."
---

# Hybrid Quantum-Classical Neural Architecture Search (HQNN-NAS)

## Description

Hybrid quantum-classical neural networks (HQNNs) combine classical learning components with parameterized quantum circuits (PQCs) in an end-to-end trainable framework for quantum machine learning in the NISQ era. This methodology provides systematic approaches for neural architecture search over HQNN designs, with FLOPs-aware optimization to balance accuracy and computational efficiency.

## Activation Keywords

- hybrid quantum neural architecture search
- HQNN NAS
- quantum-classical neural network design
- 混合量子经典神经网络架构搜索
- quantum NAS
- hardware-aware quantum ML
- FLOPs-aware quantum search
- hqnn design
- quantum architecture search

## Tools Used

- **terminal**: Run quantum simulation (Qiskit, Pennylane, TorchQuantum)
- **file**: Create HQNN architecture configurations
- **browser**: Access quantum computing platforms (IBM Quantum, Rigetti)

## Core Methodology

### Step 1: HQNN Architecture Definition

Define the search space with these dimensions:

| Dimension | Options | Impact |
|-----------|---------|--------|
| **Data Encoding** | Angle, Amplitude, Basis, IQP, Hamiltonian | Determines quantum feature map expressivity |
| **Circuit Structure** | Layered, Hardware-Efficient, Entangling, Problem-Inspired | Affects trainability and expressiveness |
| **Circuit Depth** | 1-10+ layers (hardware-limited) | Trade-off: expressivity vs. noise accumulation |
| **Measurement** | Pauli-Z, Pauli-X/Y, Expectation values, Samples | Information extraction strategy |
| **Classical Coupling** | Pre-processing, Post-processing, Interleaved | Integration pattern between quantum and classical |
| **Classical Backbone** | MLP, CNN, RNN, Transformer | Classical component architecture |

### Step 2: FLOPs-Aware Search Space

```python
# FLOPs estimation for hybrid quantum-classical networks
def estimate_hqnn_flops(config):
    """Estimate computational complexity of HQNN configuration."""
    # Classical component FLOPs
    classical_flops = sum(
        layer['input_dim'] * layer['output_dim'] 
        for layer in config['classical_layers']
    )
    
    # Quantum component FLOPs (approximation)
    # Each gate ~ O(2^n) for n qubits, simplified as gate count
    quantum_flops = (
        config['num_qubits'] * 
        config['circuit_depth'] * 
        config['shots'] *
        config['num_layers']
    )
    
    # Measurement overhead
    measurement_flops = config['num_qubits'] * config['shots']
    
    return {
        'classical': classical_flops,
        'quantum': quantum_flops,
        'measurement': measurement_flops,
        'total': classical_flops + quantum_flops + measurement_flops
    }
```

### Step 3: Search Strategy Selection

| Strategy | Use Case | Pros | Cons |
|----------|----------|------|------|
| **Random Search** | Baseline, initial exploration | Simple, parallelizable | Inefficient for large spaces |
| **Bayesian Optimization** | Moderate search spaces | Sample efficient | Struggles with discrete variables |
| **Reinforcement Learning** | Large, structured spaces | Learns search policy | Requires many evaluations |
| **Evolutionary Search** | Complex fitness landscapes | Good exploration | Computationally expensive |
| **Differentiable NAS** | End-to-end optimization | Gradient-based efficiency | Relaxation artifacts |
| **MCTS** (see mcts-quantum-encoding-discovery) | Encoding-specific optimization | Balanced exploration-exploitation | Tree depth limited |

### Step 4: Hardware-Aware Constraints

```python
# Hardware constraint checks for NISQ devices
def check_hardware_constraints(config, backend_info):
    """Verify HQNN design is executable on target quantum hardware."""
    constraints = {
        'max_qubits': backend_info.get('num_qubits', 127),
        'max_depth': backend_info.get('max_circuit_depth', 100),
        'coupling_map': backend_info.get('coupling_map', None),
        'gate_set': backend_info.get('supported_gates', ['rx', 'ry', 'rz', 'cx']),
        'noise_model': backend_info.get('noise_model', None)
    }
    
    violations = []
    if config['num_qubits'] > constraints['max_qubits']:
        violations.append(f"Exceeds max qubits: {config['num_qubits']} > {constraints['max_qubits']}")
    if config['circuit_depth'] > constraints['max_depth']:
        violations.append(f"Exceeds max depth: {config['circuit_depth']} > {constraints['max_depth']}")
    for gate in config['gate_set']:
        if gate not in constraints['gate_set']:
            violations.append(f"Unsupported gate: {gate}")
    
    return violations
```

### Step 5: Training Pipeline

```
1. Initialize HQNN architecture from search space
2. Encode classical data → quantum feature map
3. Apply parameterized quantum circuit
4. Measure quantum outputs → classical features
5. Feed to classical neural network
6. Compute loss and backpropagate through both components
7. Evaluate FLOPs budget constraint
8. Update architecture via search algorithm
9. Repeat until convergence or FLOPs budget exhausted
```

## Implementation Example

```python
import torch
import pennylane as qml

class HQNNLayer(torch.nn.Module):
    """Single hybrid quantum-classical layer."""
    
    def __init__(self, num_qubits, num_classical, circuit_depth=3):
        super().__init__()
        self.num_qubits = num_qubits
        self.circuit_depth = circuit_depth
        
        # Classical pre-processing
        self.preprocess = torch.nn.Linear(num_classical, num_qubits)
        
        # Quantum circuit parameters
        self.phi_weights = torch.nn.Parameter(
            torch.randn(circuit_depth, num_qubits) * 0.1
        )
        self.theta_weights = torch.nn.Parameter(
            torch.randn(circuit_depth, num_qubits) * 0.1
        )
        
        # Classical post-processing
        self.postprocess = torch.nn.Linear(num_qubits, num_classical)
    
    def quantum_circuit(self, inputs, phi, theta):
        """Parameterized quantum circuit."""
        @qml.qnode(qml.device('default.qubit', wires=self.num_qubits))
        def circuit(x, ph, th):
            # Encoding
            for i in range(self.num_qubits):
                qml.RY(x[i], wires=i)
            
            # Variational layers
            for layer in range(self.circuit_depth):
                for i in range(self.num_qubits):
                    qml.RY(phi[layer, i], wires=i)
                    qml.RZ(th[layer, i], wires=i)
                # Entanglement
                for i in range(self.num_qubits - 1):
                    qml.CNOT(wires=[i, i + 1])
            
            return [qml.expval(qml.PauliZ(i)) for i in range(self.num_qubits)]
        
        return torch.tensor(circuit(inputs, phi, theta))
    
    def forward(self, x):
        # Classical → Quantum
        x_q = torch.tanh(self.preprocess(x))
        # Quantum circuit
        x_m = self.quantum_circuit(x_q, self.phi_weights, self.theta_weights)
        # Quantum → Classical
        return self.postprocess(x_m)
```

## Error Handling

### Barren Plateaus
- **Symptom**: Gradients vanish exponentially with qubit count
- **Solution**: Use local cost functions, layer-wise training, or problem-inspired ansatz

### Hardware Noise
- **Symptom**: Performance degrades on real hardware vs. simulation
- **Solution**: Include noise model in search fitness function, use error mitigation

### FLOPs Budget Violation
- **Symptom**: Architecture exceeds computational budget
- **Solution**: Penalize over-budget architectures in search, use Pareto optimization

## Key References

- arXiv:2605.18345 - Hybrid Quantum-Classical Neural Architecture Search
- Marchisio et al. (2026) - FLOPs-aware HQNN design
- Pennylane documentation for quantum circuit implementation
- Qiskit documentation for hardware-aware compilation

## Related Skills

- mcts-quantum-encoding-discovery: MCTS-based encoding optimization
- quantum-neural-architecture: General QNN design patterns
- qml-framework-agnostic-design: Framework-agnostic QML design
