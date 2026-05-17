---
name: quantum-hybrid-neural-computing
description: "Quantum-hybrid neural computing framework for designing and implementing hybrid quantum-classical neural networks. Covers variational quantum circuits (VQC), parameterized quantum circuits (PQC), quantum neural networks (QNN), and hybrid training strategies. Use when implementing quantum-classical ML models, optimizing quantum circuits for neural tasks, or analyzing quantum advantage in deep learning."
---

# Quantum-Hybrid Neural Computing

Framework for designing, training, and deploying hybrid quantum-classical neural networks for machine learning tasks.

## Activation Keywords

- hybrid quantum neural network
- quantum-classical ML
- variational quantum circuit
- parameterized quantum circuit
- quantum neural network
- VQC training
- quantum machine learning
- hybrid QNN
- 量子混合神经网络
- 量子经典混合

## Tools Used

- `exec`: Run Python with Qiskit/Pennylane
- `web_search`: Find latest quantum ML papers
- `write`: Save quantum circuit designs, training scripts
- `read`: Load quantum circuit configurations

## Core Concepts

### Variational Quantum Circuits (VQC)

```
VQC Structure:
  1. Data Encoding Layer: |ψ(x)⟩ = U_encode(x)|0⟩
  2. Variational Layer: U(θ) = ∏ U(θ_i)
  3. Measurement: ⟨Z⟩ or Pauli expectation values
```

**Encoding Methods**:
- **Basis Encoding**: Binary to computational basis
- **Amplitude Encoding**: Features to state amplitudes
- **Angle Encoding**: Rotation angles from features
- **Dense Angle Encoding**: Efficient qubit utilization

### Hybrid Quantum-Classical Architecture

```
Hybrid Model:
  Input (Classical)
    ↓
  Classical Preprocessing (Feature extraction)
    ↓
  Quantum Encoder (State preparation)
    ↓
  Variational Quantum Circuit (Processing)
    ↓
  Measurement (Expectation values)
    ↓
  Classical Postprocessing (Decision)
    ↓
  Output (Classical)
```

## Implementation Workflow

### Step 1: Problem Analysis

Determine quantum suitability:
- **Classification**: Quantum advantage with high-dimensional feature spaces
- **Regression**: Parameterized quantum regression
- **Generative**: Quantum GANs, Born machines
- **Reinforcement**: Quantum policy gradients

### Step 2: Circuit Design

**Circuit Depth Guidelines**:
- NISQ devices: Depth < 100 gates
- Error rates: Keep below hardware thresholds
- Ansatz selection: Hardware-efficient vs. problem-inspired

**Common Ansätze**:
```python
# Hardware Efficient Ansatz (HEA)
def hea_circuit(n_qubits, n_layers):
    for layer in range(n_layers):
        for q in range(n_qubits):
            ry(theta[q, layer], q)
            rz(phi[q, layer], q)
        for q in range(n_qubits - 1):
            cx(q, q + 1)

# Alternating Layered Ansatz
def ala_circuit(n_qubits, n_layers):
    for layer in range(n_layers):
        # Entangling layer
        for q in range(0, n_qubits - 1, 2):
            cx(q, q + 1)
        for q in range(1, n_qubits - 1, 2):
            cx(q, q + 1)
        # Rotation layer
        for q in range(n_qubits):
            rx(theta[q, layer], q)
```

### Step 3: Training Strategy

**Gradient Computation**:
- **Parameter-Shift Rule**: Exact gradients for quantum circuits
- **Finite Differences**: Approximate gradients
- **Simultaneous Perturbation**: SPSA for large parameter spaces

```python
# Parameter-Shift Rule
def quantum_gradient(params, circuit, observable):
    grad = []
    for i in range(len(params)):
        # Positive shift
        params_plus = params.copy()
        params_plus[i] += np.pi / 2
        f_plus = circuit(params_plus, observable)
        
        # Negative shift
        params_minus = params.copy()
        params_minus[i] -= np.pi / 2
        f_minus = circuit(params_minus, observable)
        
        grad.append(0.5 * (f_plus - f_minus))
    return np.array(grad)
```

### Step 4: Optimization

**Optimizer Selection**:
- **COBYLA**: Gradient-free, robust
- **SPSA**: Stochastic approximation, noise-tolerant
- **Adam**: Adaptive learning rate (classical)
- **L-BFGS-B**: Quasi-Newton for smooth landscapes

**Training Loop**:
```python
def train_hybrid_model(X, y, n_epochs=100):
    params = initialize_parameters()
    optimizer = AdamOptimizer(learning_rate=0.01)
    
    for epoch in range(n_epochs):
        for batch_x, batch_y in batches(X, y):
            # Forward pass through hybrid model
            predictions = hybrid_forward(batch_x, params)
            loss = compute_loss(predictions, batch_y)
            
            # Backward pass with quantum gradients
            gradients = compute_quantum_gradients(loss, params)
            params = optimizer.step(gradients, params)
    
    return params
```

## Quantum-Classical Integration Patterns

### Pattern 1: Quantum Feature Map

```
Classical Input → Quantum Feature Map → Classical Classifier

Use when: High-dimensional classical features
Benefit: Quantum kernel methods for non-linear separation
```

### Pattern 2: Quantum Layer in Deep Network

```
Input → Classical Layers → Quantum Layer → Classical Layers → Output

Use when: Quantum processing of intermediate representations
Benefit: Quantum advantage in specific subspaces
```

### Pattern 3: Quantum Embedding

```
Input → Quantum Encoder → Quantum Latent Space → Quantum Decoder → Output

Use when: Quantum generative models
Benefit: Quantum-enhanced representation learning
```

## Error Mitigation Strategies

### Zero-Noise Extrapolation

```python
def zne_mitigation(circuit, observable, scale_factors=[1, 2, 3]):
    results = []
    for scale in scale_factors:
        # Scale circuit by adding CNOT pairs
        scaled_circuit = scale_noise(circuit, scale)
        result = execute(scaled_circuit, observable)
        results.append(result)
    
    # Extrapolate to zero noise
    return richardson_extrapolate(results, scale_factors)
```

### Probabilistic Error Cancellation

```python
def pec_mitigation(circuit, observable, noise_model):
    # Learn quasi-probability representation
    gamma, operations = learn_representation(noise_model)
    
    # Sample and execute
    results = []
    for _ in range(n_samples):
        sampled_circuit = sample_circuit(operations, gamma)
        result = execute(sampled_circuit, observable)
        results.append(result * gamma)
    
    return np.mean(results)
```

## Best Practices

### Circuit Design

1. **Keep depth minimal**: Reduces decoherence
2. **Use hardware-efficient gates**: Match native gate set
3. **Exploit symmetry**: Reduce parameter count
4. **Validate expressibility**: Check state coverage

### Training

1. **Warm start**: Initialize with classical pre-training
2. **Batch size**: Small batches for quantum simulation
3. **Learning rate**: Conservative for quantum landscapes
4. **Regularization**: Prevent barren plateaus

### Hardware Considerations

1. **Qubit mapping**: Minimize SWAP operations
2. **Gate scheduling**: Optimize parallel execution
3. **Readout correction**: Calibrate measurement errors
4. **Dynamic decoupling**: Extend coherence times

## Applications

### Binary Classification

```python
def quantum_classifier(X_train, y_train, n_qubits):
    # Define quantum feature map
    feature_map = ZZFeatureMap(n_qubits, reps=2)
    
    # Variational circuit
    ansatz = EfficientSU2(n_qubits, reps=1)
    
    # VQC
    vqc = VQC(
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=SPSA(maxiter=100)
    )
    
    vqc.fit(X_train, y_train)
    return vqc
```

### Quantum Autoencoder

```python
def quantum_autoencoder(n_qubits, n_latent):
    # Encoder: n_qubits → n_latent
    encoder = QuantumCircuit(n_qubits)
    for layer in range(3):
        for q in range(n_qubits):
            encoder.ry(Parameter(f'θ_{q}_{layer}'), q)
        for q in range(n_qubits - 1):
            encoder.cx(q, q + 1)
    
    # Latent state extraction
    # Decoder: n_latent → n_qubits (via inverse)
    
    return encoder
```

## Evaluation Metrics

### Quantum Advantage Assessment

1. **Accuracy**: Classification/regression performance
2. **Expressibility**: State space coverage
3. **Entangling Capability**: Meyer-Wallach measure
4. **Gradient Magnitude**: Avoid barren plateaus
5. **Classical Simulability**: Tensor network contraction

### Benchmarking

```python
def benchmark_vqc(vqc, X_test, y_test):
    metrics = {
        'accuracy': accuracy_score(y_test, vqc.predict(X_test)),
        'inference_time': measure_time(vqc, X_test),
        'circuit_depth': vqc.circuit_depth(),
        'parameter_count': vqc.num_parameters,
        'expressibility': compute_expressibility(vqc),
        'entangling': compute_entangling(vqc)
    }
    return metrics
```

## Limitations

- **NISQ constraints**: Limited qubits, gate fidelity
- **Barren plateaus**: Gradient vanishing in deep circuits
- **Classical simulation**: Quantum advantage hard to prove
- **Training time**: Quantum simulation overhead
- **Noise**: Decoherence and gate errors

## Related Skills

- **quantum-neuroscience-fusion**: Quantum spiking neural networks
- **quantum-computing**: General quantum computing
- **spikingjelly-framework**: Classical SNN implementation

## References

- Benedetti et al. "Parameterized quantum circuits as machine learning models"
- Cerezo et al. "Variational quantum algorithms"
- McClean et al. "Barren plateaus in quantum neural networks"
- Schuld & Petruccione "Machine Learning with Quantum Computers"

## Examples

### Example 1: Using this skill
```
User: [Request related to this skill's domain]
Agent: [Applies skill knowledge to help user]
```
