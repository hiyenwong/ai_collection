# Quantum Circuit Patterns for QNNs

This document provides common circuit patterns for quantum neural networks with analysis of their properties.

## Pattern Catalog

### Pattern 1: Angle Encoding + Rotation Layers

**Use Case**: Classification with moderate dimensionality (4-16 features)

**Structure**:
```
Encoding: RX(θ_i) for each feature i
Layers: 
  - Layer 1: RZ-RY on each qubit + CNOT chain
  - Layer 2: RX-RZ + CNOT ring
  - Measurement: Local observables (Z_i)
```

**Properties**:
- Qubits: n (matches feature count)
- Parameters: 2n × depth + n (encoding)
- Expressivity: Moderate (rank ~2n^2)
- Trainability: Good for depth ≤ 5
- Barren plateau risk: LOW

**Example**:
```python
# 8 features, 4 qubits (amplitude encoding alternative)
circuit = {
    'encoding': 'angle',
    'qubits': 8,
    'layers': [
        {'gates': ['RZ', 'RY', 'CNOT'], 'entanglement': 'chain'},
        {'gates': ['RX', 'RZ', 'CNOT'], 'entanglement': 'ring'}
    ],
    'depth': 3
}
```

### Pattern 2: Amplitude Encoding + Variational Layers

**Use Case**: High-dimensional data (image, audio, large feature sets)

**Structure**:
```
Encoding: Amplitude encoding (2^n features → n qubits)
Layers: 
  - Strongly entangling layers: RX-RY-RZ + CZ/CNOT
  - Multiple measurement zones
```

**Properties**:
- Qubits: log2(features) (efficient)
- Parameters: 3n × depth
- Expressivity: High for deep circuits
- Trainability: Moderate (risk increases with depth)
- Barren plateau risk: MODERATE for depth > 5

**Example**:
```python
# 256 features → 8 qubits
circuit = {
    'encoding': 'amplitude',
    'qubits': 8,  # log2(256)
    'layers': [
        {'gates': ['RX', 'RY', 'RZ'], 'entanglement': 'full'},
        {'gates': ['RX', 'RY', 'RZ'], 'entanglement': 'ring'}
    ],
    'depth': 5
}
```

### Pattern 3: Basis Encoding + Grover-style

**Use Case**: Discrete/classical data, search problems

**Structure**:
```
Encoding: Basis states (binary data)
Layers: 
  - Grover iterations: Oracle + diffusion
  - Optional: Variational refinement
```

**Properties**:
- Qubits: n (matches data bits)
- Parameters: 0 (Grover) or few (variational)
- Expressivity: Task-specific
- Trainability: Excellent (deterministic algorithm)
- Barren plateau risk: LOW (fixed structure)

### Pattern 4: Hardware-Efficient Ansatz

**Use Case**: Near-term hardware with limited connectivity

**Structure**:
```
Layers:
  - Single-qubit rotations: RX-RZ or RX-RY-RZ
  - Entangling: Hardware-native (CNOT, CZ, iSWAP)
  - Repeat with different parameters
```

**Properties**:
- Qubits: Flexible
- Parameters: 2-3 per qubit × depth
- Expressivity: Moderate to high
- Trainability: Good (native gates)
- Barren plateau risk: Depends on depth

**Hardware-specific variants**:
- **Superconducting**: CNOT/CZ entanglement
- **Trapped ions**: Mølmer-Sørensen gates
- **Photonics**: Linear optics + measurements

### Pattern 5: Problem-Inspired Ansatz

**Use Case**: Task-specific optimization (VQE, QAOA, chemistry)

**Structure**:
```
Layers:
  - Task-specific unitaries (Hamiltonian evolution)
  - Mixing operators (parameterized rotations)
  - Cost function measurement
```

**Properties**:
- Qubits: Problem-determined
- Parameters: Problem-dependent
- Expressivity: Targeted
- Trainability: Excellent (built-in structure)
- Barren plateau risk: LOW

**Examples**:
- **VQE**: Hartree-Fock + unitary coupled cluster
- **QAOA**: Cost + mixer layers
- **Quantum chemistry**: UCCSD ansatz

### Pattern 6: Tensor Network Ansatz

**Use Case**: Systems with specific correlation structure

**Structure**:
```
Layers:
  - Matrix product state (MPS) structure
  - Tree tensor network (TTN)
  - Projected entangled pair states (PEPS)
```

**Properties**:
- Qubits: Flexible
- Parameters: Reduced (few per bond)
- Expressivity: Structured (correlation-aware)
- Trainability: Good (limited parameter space)
- Barren plateau risk: LOW-MODERATE

## Pattern Selection Guide

| Task | Recommended Pattern | Reason |
|------|---------------------|--------|
| Image classification | Amplitude + Entangling | High dimensionality |
| Text features | Angle + Rotation | Moderate dimensionality |
| Binary classification | Basis + Variational | Discrete data |
| Optimization (VQE) | Problem-inspired | Built-in structure |
| Hardware-constrained | Hardware-efficient | Native gates |
| Strongly correlated | Tensor network | Correlation structure |

## Depth Recommendations

Based on barren plateau analysis:

| Qubits | Max Depth | Expressivity Range |
|--------|-----------|-------------------|
| 4 | 10 | 0.1 - 0.6 |
| 8 | 6 | 0.1 - 0.4 |
| 16 | 4 | 0.05 - 0.2 |
| 32+ | 2-3 | 0.02 - 0.1 |

## Measurement Strategies

### Global vs Local Measurements

**Global**: Measure all qubits
- Cost: ⨍(U(θ), Z⊗n)
- Risk: Higher barren plateau risk
- Use: When full state information needed

**Local**: Measure subsets
- Cost: Σ_i ⨍(U(θ), Z_i)
- Risk: Lower barren plateau risk
- Use: Recommended for most tasks

**Semi-local**: Measure k-qubit subsets
- Cost: Σ_{|S|=k} ⨍(U(θ), Z_S)
- Risk: Intermediate
- Use: Balance coverage vs trainability

## Noise Considerations

### Error Rates vs Depth

| Error Rate | Max Depth | Strategy |
|------------|-----------|----------|
| 1e-3 | 10 | Standard training |
| 1e-2 | 5 | Error mitigation |
| 1e-1 | 2-3 | Noise adaptive |

### Noise-Resilient Patterns

- Shallow circuits (depth < 5)
- Error mitigation techniques
- Noise-aware training
- Hardware-efficient gates

## References

- "Expressibility and entangling capability" - Sim et al. (2019)
- "Hardware-efficient variational quantum eigensolver" - Kandala et al. (2017)
- "Quantum circuit learning" - Mitarai et al. (2018)