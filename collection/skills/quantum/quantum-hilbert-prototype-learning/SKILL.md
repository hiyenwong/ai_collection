---
name: quantum-hilbert-prototype-learning
description: "Quantum Hilbert Space prototype learning methodology using Matrix Product States (MPS). Encodes class prototypes as generative MPS in quantum Hilbert space for classification and clustering via geometric quantum state measures. Covers quantum attraction effect and prototype-based dimensionality reduction."
---

# Quantum Hilbert Space Prototype Learning (QHPL)

## Description

Prototype learning is a fundamental ML paradigm where each class is represented by a prototype (representative example). This methodology lifts prototype learning from classical feature space to **quantum Hilbert space** by encoding class prototypes as generative Matrix Product States (MPS). Classification and clustering are performed through geometric measures between quantum states, enabling explainable, quantum-probabilistic learning that outperforms classical prototype approaches.

## Activation Keywords

- quantum prototype learning
- quantum Hilbert space learning
- matrix product state classification
- 量子原型学习
- quantum geometric learning
- MPS machine learning
- quantum prototype classification
- quantum Hilbert ML
- 量子希尔伯特空间学习
- quantum state geometric measure

## Tools Used

- **terminal**: Run MPS simulations (TeNPy, ITensor, PennyLane)
- **file**: Create MPS-based model implementations
- **browser**: Access quantum simulation platforms

## Core Methodology

### Step 1: Quantum Probability Framework

Classical ML operates on feature vectors. Quantum ML operates on **quantum states** in Hilbert space:

| Concept | Classical | Quantum (Hilbert Space) |
|---------|-----------|------------------------|
| Data point | Vector x ∈ R^d | State |ψ⟩ ∈ H |
| Class prototype | Centroid μ | MPS |φ_c⟩ |
| Similarity | Euclidean distance | Fidelity F = |⟨ψ|φ_c⟩|² |
| Probability | Softmax | Born rule: P(c) = |⟨ψ|φ_c⟩|² |
| Decision boundary | Hyperplane | Quantum interference |

### Step 2: MPS Prototype Construction

```python
import numpy as np
from numpy.linalg import svd

class MPSPrototype:
    """Matrix Product State prototype for a class."""
    
    def __init__(self, num_sites, bond_dim, physical_dim=2):
        self.num_sites = num_sites  # Number of qubits/features
        self.bond_dim = bond_dim    # MPS bond dimension
        self.physical_dim = physical_dim
        # MPS tensors: A[i] has shape (bond_dim, physical_dim, bond_dim)
        self.tensors = [
            np.random.randn(bond_dim, physical_dim, bond_dim) 
            for _ in range(num_sites)
        ]
        # Boundary conditions
        self.tensors[0] = np.random.randn(physical_dim, bond_dim)
        self.tensors[-1] = np.random.randn(bond_dim, physical_dim)
    
    def normalize(self):
        """Normalize MPS to unit norm."""
        norm = self.compute_norm()
        for i in range(self.num_sites):
            self.tensors[i] /= norm ** (1.0 / self.num_sites)
    
    def compute_overlap(self, other):
        """Compute |⟨ψ|φ⟩|² between two MPS states (fidelity)."""
        # Contract MPS tensors efficiently
        overlap = 1.0
        for i in range(self.num_sites):
            # Tensor contraction: ⟨A_i|B_i⟩
            overlap *= np.einsum('...a,...a->...', 
                                np.conj(self.tensors[i]), 
                                other.tensors[i])
        return np.abs(overlap) ** 2
```

### Step 3: Training with Quantum Prototype Optimization

```
Training Algorithm:
1. Encode data samples as quantum states |ψ_i⟩
2. Initialize class prototypes as random MPS |φ_c⟩
3. For each training step:
   a. Compute fidelity F_i,c = |⟨ψ_i|φ_c⟩|² for all classes
   b. Calculate quantum probability P(c|i) = F_i,c / Σ_c' F_i,c'
   c. Compute cross-entropy loss
   d. Update MPS tensors via gradient descent
4. The quantum "attraction" effect emerges naturally:
   - Similar data points attract prototype toward their region
   - Distant points have diminishing influence via Born rule
```

### Step 4: Quantum Attraction Effect

A key discovery: quantum-probabilistic prototypes exhibit an **"attraction" effect**:

- Classical prototypes: mean of assigned points (arithmetic average)
- Quantum prototypes: **coherent superposition** of assigned states
- The attraction is governed by quantum interference, not just averaging
- This enables prototypes to capture **multi-modal** class distributions

```python
def quantum_prototype_update(prototype, data_states, assignments, lr=0.01):
    """Update quantum prototype with attraction effect."""
    for state, assigned in zip(data_states, assignments):
        if not assigned:
            continue
        
        # Quantum attraction: gradient of fidelity
        overlap = prototype.compute_overlap(state)
        gradient = (state.tensors - prototype.tensors) * overlap
        
        for i in range(prototype.num_sites):
            prototype.tensors[i] += lr * gradient[i]
    
    prototype.normalize()
```

### Step 5: Dimensionality Reduction via Prototype Distances

```python
def prototype_distance_reduction(prototypes, data_states):
    """Reduce dimensionality by projecting onto prototype distance space.
    
    Each data point is represented by its distances to all prototypes,
    reducing from 2^n dimensions to k (number of classes) dimensions.
    """
    n_classes = len(prototypes)
    reduced = np.zeros((len(data_states), n_classes))
    
    for i, state in enumerate(data_states):
        for j, proto in enumerate(prototypes):
            reduced[i, j] = 1.0 - state.compute_overlap(proto)
    
    return reduced
```

## Implementation Example

```python
class QuantumPrototypeClassifier:
    """Prototype-based classifier in quantum Hilbert space."""
    
    def __init__(self, n_classes, n_qubits, bond_dim=4):
        self.n_classes = n_classes
        self.n_qubits = n_qubits
        self.bond_dim = bond_dim
        self.prototypes = [
            MPSPrototype(n_qubits, bond_dim) 
            for _ in range(n_classes)
        ]
    
    def encode_data(self, x):
        """Encode classical data as quantum state (amplitude encoding)."""
        # Normalize and pad to 2^n
        x_norm = x / np.linalg.norm(x)
        padded = np.zeros(2 ** self.n_qubits)
        padded[:len(x_norm)] = x_norm
        return padded / np.linalg.norm(padded)
    
    def predict(self, x):
        """Predict class via quantum fidelity."""
        state = self.encode_data(x)
        fidelities = []
        for proto in self.prototypes:
            fidelity = proto.compute_fidelity(state)
            fidelities.append(fidelity)
        return np.argmax(fidelities)
    
    def fit(self, X, y, epochs=100, lr=0.01):
        """Train prototypes via quantum attraction."""
        for epoch in range(epochs):
            for x, label in zip(X, y):
                state = self.encode_data(x)
                # Update only the assigned prototype
                self.prototypes[label].attract(state, lr)
```

## Error Handling

### Bond Dimension Too Small
- **Symptom**: Low classification accuracy, poor prototype quality
- **Solution**: Increase bond_dim; start with 4 and scale up to 16+

### MPS Normalization Instability
- **Symptom**: Overlaps diverge during training
- **Solution**: Apply canonical form after each update, or use left/right canonicalization

### State Encoding Bottleneck
- **Symptom**: Encoding classical data requires exponential resources
- **Solution**: Use approximate encoding (TTN, tensor train) for high-dimensional data

## Key References

- arXiv:2605.17895 - Geometric Prototype Learning in Quantum Hilbert Space with MPS
- Zhang et al. (2026) - Fashion-MNIST and ECG dataset benchmarks
- Matrix Product State (MPS) / Tensor Train decompositions

## Related Skills

- quantum-tensor-network-ml: Tensor network methods for QML
- quantum-neural-network-designer: General QNN design
- hqnn-neural-architecture-search: Hybrid quantum-classical architecture
