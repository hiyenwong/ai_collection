---
name: quantum-ml-data-loading
description: "Quantum machine learning data loading optimization - efficient quantum state preparation, amplitude encoding, and data embedding techniques for QML. Use when: (1) Loading classical data into quantum circuits for QML, (2) Optimizing quantum feature maps and kernels, (3) Implementing efficient amplitude encoding, (4) Reducing circuit depth for data embedding, (5) Designing quantum data loaders for NISQ devices."
---

# Quantum ML Data Loading

Efficient techniques for loading classical data into quantum circuits for quantum machine learning applications.

## The Data Loading Problem

### Challenge

Classical data must be encoded into quantum states for QML algorithms:
- **n** classical data points → **log(n)** qubits (exponential compression)
- But encoding requires **O(n)** gates (circuit depth bottleneck)

### Key Metrics

| Metric | Classical | Quantum Target |
|--------|-----------|----------------|
| Data points | n | n amplitudes |
| Qubits | - | log₂(n) |
| Gates needed | - | O(poly(log n)) ideal |
| Current NISQ | - | O(n) practical |

## Encoding Strategies

### 1. Basis Encoding

**Concept**: Classical bitstring → Computational basis state

```
Classical: x = [0, 1, 0, 1]
Quantum: |x⟩ = |0101⟩
```

**Implementation**:
```python
def basis_encoding(data: list[int]) -> QuantumCircuit:
    """
    Encode binary data as computational basis state.
    
    Args:
        data: List of binary values (0 or 1)
    
    Returns:
        QuantumCircuit with X gates for each |1⟩
    """
    n_qubits = len(data)
    qc = QuantumCircuit(n_qubits)
    
    for i, bit in enumerate(data):
        if bit == 1:
            qc.x(i)
    
    return qc
```

**Pros**: Simple, deterministic
**Cons**: No superposition, limited expressivity

### 2. Amplitude Encoding

**Concept**: Classical vector → Amplitudes of quantum state

```
Classical: x = [x₁, x₂, ..., xₙ] with Σ|xᵢ|² = 1
Quantum: |ψ⟩ = Σ xᵢ |i⟩
```

**Efficient Implementation**:

```python
def amplitude_encoding(vector: np.ndarray) -> QuantumCircuit:
    """
    Encode normalized vector into quantum amplitudes.
    Uses state preparation with O(n) gates.
    
    Args:
        vector: Normalized classical vector (Σ|vᵢ|² = 1)
    
    Returns:
        QuantumCircuit preparing the state
    """
    n = len(vector)
    n_qubits = int(np.ceil(np.log2(n)))
    
    qc = QuantumCircuit(n_qubits)
    
    # Use Qiskit's StatePreparation for efficiency
    from qiskit.circuit.library import StatePreparation
    
    # Pad vector to power of 2
    padded = np.zeros(2**n_qubits)
    padded[:n] = vector
    padded = padded / np.linalg.norm(padded)
    
    qc.append(StatePreparation(padded), range(n_qubits))
    
    return qc
```

**Circuit Depth Optimization**:
- Standard: O(n) depth
- Optimized (Möttönen et al.): O(n) with reduced constant
- Approximate: O(poly(log n)) with error tolerance

### 3. Angle Encoding

**Concept**: Classical values → Rotation angles

```
Classical: x = [x₁, x₂, ..., xₙ] ∈ [0, 1]
Quantum: |ψ⟩ = ⊗ᵢ Rᵧ(πxᵢ)|0⟩
```

**Implementation**:

```python
def angle_encoding(data: np.ndarray, rotation: str = 'RY') -> QuantumCircuit:
    """
    Encode data as rotation angles.
    
    Args:
        data: Array of values in [0, 1]
        rotation: 'RX', 'RY', or 'RZ'
    
    Returns:
        QuantumCircuit with rotation gates
    """
    n_qubits = len(data)
    qc = QuantumCircuit(n_qubits)
    
    for i, val in enumerate(data):
        angle = np.pi * val  # Scale to [0, π]
        
        if rotation == 'RX':
            qc.rx(angle, i)
        elif rotation == 'RY':
            qc.ry(angle, i)
        elif rotation == 'RZ':
            qc.rz(angle, i)
    
    return qc
```

**Pros**: Shallow circuits (depth 1), hardware-friendly
**Cons**: Limited entanglement, may need feature maps

### 4. Quantum Feature Maps

**Concept**: Encode data into quantum Hilbert space with kernel properties

**Common Feature Maps**:

| Feature Map | Structure | Use Case |
|-------------|-----------|----------|
| ZZFeatureMap | ZZ interactions | Binary classification |
| PauliFeatureMap | Pauli strings | General kernels |
| Custom | Problem-specific | Domain applications |

```python
def zz_feature_map(n_qubits: int, reps: int = 2) -> QuantumCircuit:
    """
    ZZ feature map for quantum kernel methods.
    
    Creates entanglement through ZZ interactions:
    U(x) = exp(i Σ φᵢ(x) Zᵢ + Σ φᵢⱼ(x) ZᵢZⱼ)
    
    Args:
        n_qubits: Number of qubits
        reps: Number of repetitions
    
    Returns:
        Parameterized quantum circuit
    """
    from qiskit.circuit.library import ZZFeatureMap
    
    feature_map = ZZFeatureMap(
        feature_dimension=n_qubits,
        reps=reps,
        entanglement='linear'
    )
    
    return feature_map
```

## NISQ-Era Optimizations

### 1. Approximate State Preparation

**Trade-off**: Accuracy vs Circuit Depth

```python
def approximate_amplitude_encoding(
    vector: np.ndarray,
    max_depth: int,
    tolerance: float = 0.01
) -> QuantumCircuit:
    """
    Approximate amplitude encoding within depth budget.
    
    Strategy:
    1. Use low-rank approximation
    2. Truncate small amplitudes
    3. Iterative refinement
    
    Args:
        vector: Target normalized vector
        max_depth: Maximum allowed circuit depth
        tolerance: Acceptable fidelity loss
    
    Returns:
        Optimized circuit
    """
    n = len(vector)
    
    # Low-rank approximation via SVD
    # Keep only significant components
    threshold = tolerance / n
    significant = np.abs(vector) > threshold
    
    # Construct approximate state
    approx = vector.copy()
    approx[~significant] = 0
    approx = approx / np.linalg.norm(approx)
    
    # Build circuit with depth constraint
    return build_low_depth_circuit(approx, max_depth)
```

### 2. Hardware-Aware Encoding

**Considerations**:
- Native gate set
- Connectivity graph
- Gate fidelities

```python
def hardware_aware_encoding(
    data: np.ndarray,
    backend: Backend
) -> QuantumCircuit:
    """
    Optimize encoding for specific hardware.
    
    Args:
        data: Classical data to encode
        backend: Target quantum backend
    
    Returns:
        Hardware-optimized circuit
    """
    # Get hardware constraints
    coupling_map = backend.configuration().coupling_map
    basis_gates = backend.configuration().basis_gates
    
    # Build circuit
    qc = amplitude_encoding(data)
    
    # Transpile for hardware
    from qiskit import transpile
    optimized = transpile(
        qc,
        backend=backend,
        optimization_level=3,
        layout_method='sabre'
    )
    
    return optimized
```

### 3. Hybrid Approaches

**Classical Preprocessing + Quantum Encoding**:

```python
def hybrid_data_loading(
    raw_data: np.ndarray,
    reduction_dim: int
) -> QuantumCircuit:
    """
    Classical dimensionality reduction + quantum encoding.
    
    Pipeline:
    1. PCA to reduce dimensionality
    2. Normalize to quantum-ready format
    3. Amplitude encode reduced data
    
    Args:
        raw_data: High-dimensional classical data
        reduction_dim: Target dimension (determines qubits)
    
    Returns:
        Quantum circuit encoding
    """
    from sklearn.decomposition import PCA
    
    # Classical preprocessing
    pca = PCA(n_components=reduction_dim)
    reduced = pca.fit_transform(raw_data.reshape(1, -1))[0]
    
    # Normalize for quantum encoding
    normalized = reduced / np.linalg.norm(reduced)
    
    # Quantum encoding
    return amplitude_encoding(normalized)
```

## Performance Analysis

### Circuit Depth Comparison

| Method | Depth | Qubits | Expressivity |
|--------|-------|--------|--------------|
| Basis | O(n) | n | Low |
| Amplitude | O(n) | log(n) | High |
| Angle | O(1) | n | Medium |
| Feature Map | O(reps × n) | n | High |

### Fidelity Considerations

```python
def calculate_encoding_fidelity(
    target_state: np.ndarray,
    actual_circuit: QuantumCircuit,
    backend: Backend
) -> float:
    """
    Calculate fidelity of encoding process.
    
    Fidelity = |⟨target|actual⟩|²
    
    Args:
        target_state: Ideal quantum state
        actual_circuit: Implemented circuit
        backend: Execution backend
    
    Returns:
        Fidelity value [0, 1]
    """
    from qiskit.quantum_info import state_fidelity, Statevector
    
    # Simulate actual circuit
    actual_state = Statevector.from_instruction(actual_circuit)
    target_sv = Statevector(target_state)
    
    return state_fidelity(target_sv, actual_state)
```

## Research Directions

### Active Areas

1. **Quantum Random Access Memory (QRAM)**
   - Theoretical: O(log n) query complexity
   - Practical: Hardware implementations emerging

2. **Sparse State Preparation**
   - Exploit sparsity for sublinear depth
   - Applications: Sparse data, compressed sensing

3. **Learned Encodings**
   - Train encoding circuits end-to-end
   - Optimize for downstream tasks

4. **Error Mitigation**
   - Zero-noise extrapolation for encodings
   - Probabilistic error cancellation

## Implementation Patterns

### Pattern 1: Data Pipeline

```python
class QuantumDataLoader:
    """
    End-to-end quantum data loading pipeline.
    """
    
    def __init__(self, encoding_method: str = 'amplitude'):
        self.encoding_method = encoding_method
        self.scaler = StandardScaler()
    
    def preprocess(self, classical_data: np.ndarray) -> np.ndarray:
        """Classical preprocessing."""
        normalized = self.scaler.fit_transform(
            classical_data.reshape(-1, 1)
        ).flatten()
        return normalized / np.linalg.norm(normalized)
    
    def encode(self, data: np.ndarray) -> QuantumCircuit:
        """Encode to quantum circuit."""
        if self.encoding_method == 'amplitude':
            return amplitude_encoding(data)
        elif self.encoding_method == 'angle':
            return angle_encoding(data)
        else:
            raise ValueError(f"Unknown method: {self.encoding_method}")
    
    def load(self, classical_data: np.ndarray) -> QuantumCircuit:
        """Full pipeline."""
        preprocessed = self.preprocess(classical_data)
        return self.encode(preprocessed)
```

### Pattern 2: Batch Loading

```python
def batch_amplitude_encoding(
    data_batch: list[np.ndarray]
) -> list[QuantumCircuit]:
    """
    Encode multiple data points efficiently.
    
    Optimization: Share common subcircuits
    """
    circuits = []
    
    for data in data_batch:
        qc = amplitude_encoding(data)
        circuits.append(qc)
    
    return circuits
```

## Key Papers

- **Quantum state preparation with optimal circuit depth** (arxiv:2004.08469)
- **Efficient quantum circuits for state preparation** (arxiv:1807.03206)
- **Quantum feature maps for machine learning** (arxiv:1804.11326)
- **Supervised learning with quantum computers** (arxiv:1707.05391)

## Related Skills

- `quantum-neural-network-data-loading` - Shot-Based Quantum Encoding
- `quantum-ml-research` - General QML research
- `quantum-neural-architecture` - QNN design patterns

## Tools Used

- `exec`: Run Qiskit/Pennylane encoding scripts
- `read`: Load research papers on state preparation
- `write`: Create encoding circuit implementations

## Activation Keywords

- quantum data loading
- amplitude encoding
- quantum state preparation
- quantum feature map
- QML data encoding
- quantum embedding
- basis encoding
- angle encoding
- 量子数据加载
- 量子态制备
- 振幅编码
