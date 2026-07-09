# Quantum Circuit Learning Patterns

## Overview

Quantum circuits as machine learning models - parameterized circuits, variational algorithms, and quantum neural networks.

## Key Papers

| Paper | Technique | Key Insight |
|-------|-----------|-------------|
| Quantum Circuit-Based Learning Models (2602.00048) | Overview survey | Bridges QC and ML |
| Quantum circuit optimization with deep RL (2103.07585) | RL optimization | Automated circuit design |
| Structure optimization for parameterized quantum circuits (1905.09692) | Structure+params | Simultaneous optimization |
| QTN-VQC: End-to-End Learning for QNNs (2110.03861) | Tensor network | QTN + VQC framework |
| Spectral Methods for ML: Natural for Quantum Computing (2603.24654) | Spectral methods | Fourier spectrum manipulation |

## Quantum Circuit Architecture

### Parameterized Quantum Circuits (PQC)

- **Gates**: Rotation gates (RX, RY, RZ), entangling gates (CNOT, CZ)
- **Parameters**: θ (learnable rotation angles)
- **Depth**: Number of gate layers
- **Structure**: Fixed or adaptive

### Quantum Neural Networks (QNN)

- **Input encoding**: Classical data → quantum states
- **Processing**: Parameterized circuit layers
- **Output**: Measurement (expectation values)

### Variational Quantum Eigensolver (VQE)

- **Purpose**: Find ground state energy
- **Workflow**: Circuit → measurement → classical optimizer → update params
- **Application**: Chemistry, optimization

## Learning Paradigms

### Variational Quantum Algorithms

1. **VQE** - Ground state finding
2. **QAOA** - Combinatorial optimization
3. **Quantum autoencoders** - Data compression

### Reinforcement Learning for Circuit Optimization

- **Agent**: RL policy network
- **Action**: Add/remove gates, adjust parameters
- **Reward**: Circuit fidelity, error rate
- **Result**: Automated circuit design

### Structure Optimization

- **Problem**: Finding optimal circuit topology
- **Approach**: Gradient-based structure search
- **Advantage**: Better than parameter-only optimization
- **Method**: Simultaneous structure + parameter updates

## Circuit Design Patterns

### Pattern 1: Hardware-Efficient Ansatz

```python
# Match hardware connectivity
def hardware_efficient_ansatz(n_qubits, depth):
    for d in range(depth):
        # Single-qubit rotations
        for q in range(n_qubits):
            qc.ry(params[d][q], q)
        
        # Entangling gates (hardware-specific)
        for (q1, q2) in hardware_coupling_map:
            qc.cx(q1, q2)
```

### Pattern 2: Strongly Entangling Layers

```python
# Pennylane strongly entangling layers
def strongly_entangling(n_qubits, depth):
    for d in range(depth):
        # Rotations
        for q in range(n_qubits):
            qc.rz(params[d][q][0], q)
            qc.rx(params[d][q][1], q)
            qc.rz(params[d][q][2], q)
        
        # Circular entanglement
        for q in range(n_qubits):
            qc.cx(q, (q+1) % n_qubits)
```

### Pattern 3: Tensor Network QNN

```python
# Quantum Tensor Network (QTN)
def qtn_circuit(n_qubits):
    # Tree tensor network structure
    for level in range(log2(n_qubits)):
        for block in range(n_qubits // 2**(level+1)):
            # Two-qubit unitary
            apply_unitary(qc, block, params[level][block])
```

## Spectral Methods Connection

### Quantum Fourier Transform

- Quantum computers naturally perform Fourier operations
- Spectral methods are "natural" for quantum computing
- Applications: Signal processing, pattern recognition

### Pattern: Quantum Spectral Learning

```python
# Quantum spectral filtering
def quantum_spectral_filter(data, kernel):
    # Encode data as quantum state
    state = encode(data)
    
    # Apply Fourier transform (natural in quantum)
    qc.append(QFT(n_qubits), range(n_qubits))
    
    # Apply filter in Fourier domain
    apply_filter(qc, kernel)
    
    # Inverse transform
    qc.append(QFT(n_qubits).inverse(), range(n_qubits))
```

## Framework-Agnostic Neural Networks

### Problem

- Vendor lock-in: IBM, Google, D-Wave各有不同API
- Solution: Framework-agnostic representation

### Approach

1. Abstract circuit representation
2. Automatic translation to target hardware
3. Vendor-independent training

## Key Metrics

| Metric | Description |
|--------|-------------|
| Circuit depth | Number of gate layers |
| Qubit count | Quantum resources needed |
| Entangling gates | Circuit expressibility |
| Trainability | Gradient-based optimization success |
| Expressibility | Representable function space |

## Research Challenges

1. **Barren plateaus** - Gradients vanish for deep circuits
2. **Noise resilience** - Performance under NISQ conditions
3. **Trainability** - Avoiding optimization traps
4. **Encoding efficiency** - Classical → quantum data mapping

## Keywords to Track

- `quantum circuit`
- `quantum neural network`
- `quantum spectral methods`
- `parameterized quantum circuits`
- `variational quantum algorithms`

## Resources

- PennyLane: https://pennylane.ai/
- Qiskit: https://qiskit.org/
- Cirq: https://quantumai.google/cirq
- arxiv: `ti:quantum+circuit+learning`

## Knowledge Graph Entities

- Paper: "2602.00048 - Quantum Circuit-Based Learning Models"
- Keyword: `quantum circuit`
- Keyword: `quantum neural network`
- Keyword: `quantum spectral methods`