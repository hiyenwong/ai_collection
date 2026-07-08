# Quantum Neural Network Papers Reference

Key papers that inform the quantum-neural-architecture skill patterns.

## Paper List

### 1. LieTrunc-QNN (arxiv:2604.02697)

**Title**: LieTrunc-QNN: Lie Algebra Truncation and Quantum Expressivity Phase Transition

**Authors**: Haijian Shao, Dalong Zhao, Xing Deng

**Published**: 2026-04-03

**Abstract**: Quantum Machine Learning (QML) is fundamentally limited by two challenges: barren plateaus (exponentially vanishing gradients) and the fragility of parameter perturbation.

**Key Patterns**:
- Lie algebra truncation controls QNN expressivity
- Expressivity phase transition at critical generator threshold
- Below threshold: stable gradients, limited expressivity
- Above threshold: full expressivity, barren plateau risk

**Citation Pattern**:
```python
# Use when designing QNNs
from qiskit.circuit import QuantumCircuit
ansatz = build_truncated_ansatz(n_qubits, max_generators)
```

---

### 2. Topological Neural Network Field Theory (arxiv:2604.02313)

**Title**: Topological Effects in Neural Network Field Theory

**Authors**: Christian Ferko, James Halverson, Vishnu Jejjala

**Published**: 2026-04-02

**Abstract**: Neural network field theory formulates field theory as a statistical ensemble of fields defined by a network architecture.

**Key Patterns**:
- Neural networks as statistical field ensembles
- Network topology affects field properties
- Topological invariants constrain network design
- Connection to physical field theories

**Citation Pattern**:
```python
# Use when analyzing network topology effects
topological_invariant = compute_network_topology(network)
```

---

### 3. Physics-Guided Neural Networks (arxiv:2604.02906)

**Title**: Probing Proton Structure via Physics-Guided Neural Networks in Holographic QCD

**Authors**: Wei Kou, Xurong Chen

**Published**: 2026-04-03

**Abstract**: Describing the proton structure function F2 in the non-perturbative regime of QCD.

**Key Patterns**:
- Embed physical laws into neural architecture
- Physics-based loss terms
- Symmetry-preserving architectures
- Domain knowledge integration

**Citation Pattern**:
```python
# Use when neural network must respect physics
loss = data_loss + physics_constraint_loss
network = symmetry_preserving_architecture()
```

---

### 4. Belief Propagation Tensor Networks (arxiv:2604.03228)

**Title**: Belief Propagation and Tensor Network Expansions for Many-Body Quantum Systems

**Authors**: Siddhant Midha, Grace M. Sommers, Joseph Tindall

**Published**: 2026-04-03

**Abstract**: Belief propagation provides scalable heuristic for contracting tensor networks on loopy graphs.

**Key Patterns**:
- Tensor network encoding for quantum states
- Belief propagation contraction on loopy graphs
- Rigorous bounds for quantum systems
- MPS/Tree tensor network structures

**Citation Pattern**:
```python
# Use for efficient quantum state encoding
tensors = initialize_mps(n_qubits, bond_dimension)
contracted = belief_propagation_contract(tensors)
```

---

### 5. Gradient Boosting in Attention (arxiv:2604.03190)

**Title**: Gradient Boosting within a Single Attention Layer

**Authors**: Saleh Sargolzaei

**Published**: 2026-04-03

**Abstract**: Transformer attention computes a single softmax-weighted average over values.

**Key Patterns**:
- Attention as one-pass estimate (no error correction)
- Gradient boosting enables iterative refinement
- Single-layer attention enhancement
- Combining classical ML with transformer architecture

**Citation Pattern**:
```python
# Use when enhancing attention mechanisms
attention_output = gradient_boosted_attention(values, queries, keys)
```

---

## Cross-Reference Patterns

| Paper | Primary Pattern | Related Skill |
|-------|-----------------|---------------|
| LieTrunc-QNN | Barren plateau mitigation | quantum-neural-architecture |
| Topological NFT | Network topology | neural-dynamics-analysis |
| Physics-Guided | Physics constraints | physics-informed-ml |
| Tensor BP | Quantum encoding | quantum-state-representation |
| Gradient Attention | Attention enhancement | transformer-optimization |

## Future Papers to Monitor

- Quantum natural gradient methods
- Variational quantum eigensolvers (VQE)
- Quantum error mitigation techniques
- Quantum-classical hybrid benchmarks