---
name: quantum-neural-architecture
description: "Quantum Neural Network (QNN) architecture design and optimization patterns. Covers quantum-classical hybrid learning, Lie algebra truncation, barren plateau mitigation, quantum expressivity, and tensor network approaches. Activates for: QNN design, quantum neural network, quantum machine learning, quantum-classical hybrid, quantum expressivity phase transition, LieTrunc, quantum gradient descent."
---

# Quantum Neural Architecture

Patterns for designing and optimizing Quantum Neural Networks (QNN) that bridge quantum computing and classical deep learning.

## Activation Keywords

- quantum neural network
- QNN design
- quantum machine learning
- quantum-classical hybrid
- quantum expressivity
- barren plateau
- LieTrunc
- quantum gradient descent
- 量子神经网络
- 量子机器学习

## Key Patterns

### 1. Lie Algebra Truncation (LieTrunc)

**Problem**: QNNs suffer from barren plateaus (exponentially vanishing gradients)

**Solution**: Truncate the Lie algebra of QNN generators to control expressivity

```python
# Pattern from: LieTrunc-QNN paper (arxiv:2604.02697)
def compute_lie_algebra_generators(ansatz, n_qubits):
    """
    Compute generators of the dynamical Lie algebra.
    
    Key insight: Expressivity phase transition occurs when
    generator count crosses critical threshold.
    """
    generators = []
    for layer in ansatz:
        # Each parametrized gate contributes to Lie algebra
        g = compute_generator(layer)
        generators.append(g)
    
    # Truncate to subspace avoiding barren plateaus
    truncated = truncate_generators(generators, threshold)
    return truncated
```

**Threshold formula**: 
- Below threshold: Stable gradients, limited expressivity
- Above threshold: Expressive but barren plateau risk

### 2. Quantum Expressivity Phase Transition

**Concept**: QNN expressivity undergoes phase transition similar to physical systems

| Region | Generator Count | Expressivity | Trainability |
|--------|-----------------|--------------|--------------|
| Low | < threshold | Limited | Stable gradients |
| Critical | ~ threshold | Balanced | Moderate |
| High | > threshold | Full | Barren plateaus |

**Application**: Design QNNs to operate in "critical" region for optimal performance

### 3. Tensor Network Quantum States

**Pattern from**: Belief Propagation paper (arxiv:2604.03228)

```python
def tensor_network_encoding(n_qubits, bond_dimension):
    """
    Encode quantum states as tensor networks for efficient contraction.
    
    Uses Matrix Product States (MPS) or Tree Tensor Networks.
    """
    # MPS encoding: psi = A1 ⊗ A2 ⊗ ... ⊗ An
    tensors = initialize_mps(n_qubits, bond_dimension)
    
    # Contract via belief propagation on loopy graphs
    contracted = belief_propagation_contract(tensors)
    return contracted
```

**Key insight**: BP contraction on loopy tensor networks has rigorous bounds for quantum systems

### 4. Physics-Guided Neural Networks

**Pattern from**: Holographic QCD paper (arxiv:2604.02906)

```python
def physics_guided_network(physical_constraints):
    """
    Embed physical laws into neural network architecture.
    
    Example: Holographic QCD for proton structure.
    """
    # Add physics-based loss terms
    loss = data_loss + physics_constraint_loss
    
    # Use symmetries from physical system
    network = symmetry_preserving_architecture()
    return network
```

**When to use**: When neural network must respect physical laws (quantum mechanics, relativity)

### 5. Topological Neural Network Field Theory

**Pattern from**: arxiv:2604.02313

**Concept**: Neural networks as statistical ensembles of fields

- **Neural network field theory**: Formulate field theory from network architecture
- **Topological effects**: Network topology affects field properties
- **Application**: Use topological invariants to constrain network design

## QNN Architecture Templates

### Basic Parameterized Quantum Circuit (PQC)

```python
def pqc_layer(n_qubits, params):
    """
    Basic PQC layer for QNN.
    
    Structure:
    1. Rotation gates (Rz, Ry, Rx)
    2. Entangling gates (CNOT, CZ)
    3. Measurement
    """
    circuit = QuantumCircuit(n_qubits)
    
    # Rotations
    for i in range(n_qubits):
        circuit.ry(params[3*i], i)
        circuit.rz(params[3*i+1], i)
        circuit.rx(params[3*i+2], i)
    
    # Entangling (alternating pattern)
    for i in range(n_qubits-1):
        circuit.cnot(i, i+1)
    
    return circuit
```

### Expressivity-Controlled QNN

```python
def expressivity_controlled_qnn(n_qubits, target_expressivity):
    """
    Design QNN with controlled expressivity to avoid barren plateaus.
    
    Key: Limit number of generators in Lie algebra.
    """
    # Compute generator budget from target expressivity
    max_generators = expressivity_to_generator_budget(target_expressivity)
    
    # Build ansatz respecting generator budget
    ansatz = build_truncated_ansatz(n_qubits, max_generators)
    
    return ansatz
```

## Gradient Descent Strategies

### 1. Quantum Natural Gradient

```python
def quantum_natural_gradient(params, circuit, cost_function):
    """
    Use quantum Fisher information matrix for natural gradient.
    
    Advantages: Better convergence, respects quantum geometry.
    """
    # Compute Fubini-Study metric (quantum Fisher)
    fisher = compute_quantum_fisher(circuit, params)
    
    # Natural gradient: F^{-1} ∇C
    gradient = compute_gradient(cost_function, params)
    natural_grad = np.linalg.solve(fisher, gradient)
    
    return natural_grad
```

### 2. Layerwise Training

```python
def layerwise_qnn_training(circuit, data, epochs):
    """
    Train QNN layer-by-layer to avoid barren plateaus.
    
    Pattern: Gradually increase expressivity during training.
    """
    n_layers = len(circuit.layers)
    
    for layer_idx in range(n_layers):
        # Freeze previous layers, train current layer
        for epoch in range(epochs):
            train_single_layer(circuit, layer_idx, data)
        
        # Unfreeze all for final fine-tuning
        if layer_idx == n_layers - 1:
            finetune_all_layers(circuit, data)
```

## Integration Patterns

### Quantum-Classical Hybrid Learning

```python
def quantum_classical_hybrid(n_qubits, classical_features):
    """
    Hybrid architecture: Classical preprocessing + Quantum layer.
    
    Workflow:
    1. Classical encoder: Extract features
    2. Quantum layer: Process quantum-encoded features
    3. Classical decoder: Interpret quantum output
    """
    # Classical encoder
    features = classical_encoder(classical_features)
    
    # Quantum encoding (angle encoding)
    quantum_state = angle_encoding(features, n_qubits)
    
    # Quantum layer
    processed = pqc_layer(n_qubits, params)
    
    # Measurement
    output = measure_expectation(processed)
    
    # Classical decoder
    result = classical_decoder(output)
    
    return result
```

### Attention-Enhanced QNN

```python
def attention_qnn(n_qubits, attention_params):
    """
    Incorporate attention mechanism into quantum circuit.
    
    Pattern: Quantum gates modulated by attention weights.
    """
    # Classical attention computation
    attention_weights = compute_attention(classical_input)
    
    # Modulate quantum gates
    for i in range(n_qubits):
        # Gate strength proportional to attention
        gate_strength = attention_weights[i] * params[i]
        circuit.ry(gate_strength, i)
    
    return circuit
```

## Error Handling

### Barren Plateau Detection

```python
def detect_barren_plateau(gradient_variance):
    """
    Detect if QNN is in barren plateau regime.
    
    Threshold: Gradient variance < 1/n^2 (n = qubit count)
    """
    threshold = 1 / (n_qubits ** 2)
    
    if gradient_variance < threshold:
        print("Warning: Barren plateau detected!")
        print("Suggestions:")
        print("  1. Reduce circuit depth")
        print("  2. Use local cost functions")
        print("  3. Apply layerwise training")
        print("  4. Try Lie algebra truncation")
        return True
    return False
```

### Hardware Noise Mitigation

```python
def mitigate_noise(circuit, noise_model):
    """
    Mitigate quantum hardware noise in QNN.
    
    Strategies:
    1. Error mitigation techniques
    2. Robust circuit design
    3. Noise-aware training
    """
    # Zero-noise extrapolation
    results = []
    for scale in [1, 3, 5]:
        scaled_circuit = scale_noise(circuit, scale)
        results.append(execute(scaled_circuit))
    
    extrapolated = extrapolate_to_zero(results)
    return extrapolated
```

## Resources

- **LieTrunc-QNN**: arxiv:2604.02697 - Lie algebra truncation for stable QNNs
- **Tensor Networks**: arxiv:2604.03228 - BP for quantum tensor networks
- **Physics-Guided NN**: arxiv:2604.02906 - Physics constraints in neural networks
- **Topological NFT**: arxiv:2604.02313 - Neural network field theory

## Related Skills

- **spiking-mode-neural-networks**: Spiking neural network patterns
- **multi-plasticity-snn-training**: Multi-plasticity training
- **neural-emulator-theory**: Neural emulator theory
- **quantum-computing**: General quantum computing patterns

## Notes

- QNNs require careful balance of expressivity and trainability

### Scalable Training (June 2026)
- **Gradient bottleneck**: Parameter-shift scales O(n²) → use QUIVER forward gradients (arXiv: 2606.09734) or Butterfly architecture (arXiv: 2606.03517) to scale to 60+ qubits
- **Quantum-SNN fusion**: QDS-SNN combines SNNs with quantum supervision for 55%+ energy reduction (arXiv: 2606.07657)
- See `quantum-neuromorphic-computing` skill for cross-domain SNN+QNN methodology
- Barren plateaus are the main challenge for deep QNNs
- Lie algebra truncation provides principled approach to avoid barren plateaus
- Tensor networks offer efficient quantum state representation
- Hybrid quantum-classical architectures often perform best