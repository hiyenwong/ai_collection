---
name: quantum-neural-architecture-search
description: "Quantum Neural Network Architecture Search (QNAS) skill for designing efficient quantum neural networks on NISQ hardware. Uses multi-objective optimization (NSGA-II) to balance accuracy, runtime efficiency, and circuit cutting overhead. Apply when designing quantum neural networks, optimizing hybrid quantum-classical architectures, or searching for Pareto-optimal quantum circuit configurations. Keywords: quantum neural network, QNN, quantum architecture search, variational quantum circuit, ansatz design, quantum optimization, NISQ, quantum computing."
---

# Quantum Neural Architecture Search

## Overview

Automated quantum neural network architecture search framework for designing efficient, deployable quantum circuits on NISQ (Noisy Intermediate-Scale Quantum) hardware. Balances three key objectives: validation accuracy, runtime efficiency, and circuit cutting overhead.

## Core Methodology

### 1. Multi-Objective Optimization Framework

QNAS optimizes three objectives jointly using NSGA-II (Non-dominated Sorting Genetic Algorithm II):

| Objective | Description | Metric |
|-----------|-------------|--------|
| Validation Error | Classification/ regression accuracy | Cross-validation loss |
| Runtime Cost | Wall-clock evaluation time | Parameter count × depth |
| Cutting Overhead | Circuit cutting complexity | Number of subcircuits |

**Pareto Front Analysis**: Reveals trade-offs between accuracy, efficiency, and deployability.

### 2. Hardware-Aware Evaluation

Consider NISQ hardware constraints:

- **Qubit Budget**: Maximum available qubits (e.g., 8-20 qubits)
- **Gate Fidelity**: CNOT error rates, single-qubit gate errors
- **Coherence Time**: T1/T2 times affecting circuit depth limits
- **Connectivity**: Hardware-specific coupling maps

### 3. SuperCircuit Training Strategy

Train a shared-parameter SuperCircuit that encodes all candidate architectures:

```
SuperCircuit Design:
├── Embedding Layer (variable: angle-y, angle, amplitude)
├── Entangling Layer (variable: sparse, full, linear CNOT patterns)
├── Variational Layer (variable: depth 1-5)
└── Measurement Layer
```

**Benefits**:
- Single training pass evaluates multiple architectures
- Shared weights reduce search cost
- Weight inheritance for sampled architectures

### 4. Architecture Search Space

**Key Search Dimensions**:

| Component | Options | Impact |
|-----------|---------|--------|
| Embedding Type | angle-y, angle, amplitude | Data encoding efficiency |
| CNOT Mode | sparse, full, linear | Entanglement overhead |
| Circuit Depth | 1-5 layers | Expressivity vs. noise |
| Qubit Count | 4-8 qubits | Resource constraints |

**Key Findings** (from benchmarks):
- **angle-y embedding** + **sparse entangling** → best for image data (MNIST, Fashion-MNIST)
- **amplitude embedding** → optimal for tabular data (Iris)

## Workflow

### Step 1: Define Search Space

```python
search_space = {
    'embedding': ['angle-y', 'angle', 'amplitude'],
    'cnot_pattern': ['sparse', 'full', 'linear'],
    'depth': [1, 2, 3, 4, 5],
    'qubits': [4, 6, 8]
}
```

### Step 2: Initialize SuperCircuit

```python
# Train shared-parameter SuperCircuit
supercircuit = SuperCircuit(
    max_qubits=8,
    max_depth=5,
    embedding_types=search_space['embedding'],
    cnot_patterns=search_space['cnot_pattern']
)

# Train on target dataset
supercircuit.train(dataset, epochs=50)
```

### Step 3: Run NSGA-II Optimization

```python
from nsga2 import NSGA2

optimizer = NSGA2(
    objectives=['validation_error', 'runtime_cost', 'cutting_overhead'],
    population_size=100,
    generations=50
)

# Evaluate population
pareto_front = optimizer.optimize(
    evaluate_fn=lambda arch: evaluate_architecture(arch, supercircuit),
    search_space=search_space
)
```

### Step 4: Evaluate Architecture

```python
def evaluate_architecture(architecture, supercircuit):
    """
    Three-objective evaluation:
    1. Validation error (accuracy)
    2. Runtime cost proxy (param_count × depth)
    3. Cutting overhead (estimated subcircuits)
    """
    # Sample weights from SuperCircuit
    weights = supercircuit.sample_weights(architecture)
    
    # Build candidate circuit
    circuit = build_circuit(architecture, weights)
    
    # Evaluate on validation set
    val_error = evaluate(circuit, validation_data)
    
    # Runtime cost proxy
    runtime_cost = count_parameters(architecture) * get_depth(architecture)
    
    # Cutting overhead (if circuit exceeds qubit budget)
    cutting_overhead = estimate_cutting_overhead(
        circuit, 
        target_qubits=architecture['qubits']
    )
    
    return [val_error, runtime_cost, cutting_overhead]
```

### Step 5: Analyze Pareto Front

```python
# Visualize Pareto front
plot_pareto_front(pareto_front)

# Select best architecture based on constraints
best_arch = select_from_pareto(
    pareto_front,
    constraints={'qubits': 8, 'min_accuracy': 95}
)
```

## Benchmark Results

| Dataset | Best Accuracy | Qubits | Depth | Configuration |
|---------|--------------|--------|-------|---------------|
| MNIST | 97.16% | 8 | 2 | angle-y + sparse |
| Fashion-MNIST | 87.38% | 5 | 2 | angle-y + sparse |
| Iris | 100% | 4 | 2 | amplitude |

## Implementation Components

### Required Libraries

```bash
pip install pennylane qiskit deap numpy scikit-learn
```

### Key Classes

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| SuperCircuit | Shared-parameter circuit | PennyLane/Qiskit |
| ArchitectureSampler | Sample candidate architectures | Random + mutation |
| MultiObjectiveEvaluator | Three-objective evaluation | Custom scoring |
| ParetoAnalyzer | Pareto front analysis | DEAP NSGA-II |

## Best Practices

### 0. HQNN-Specific: Expressibility-Trainability Trade-off (arXiv: 2605.25768)

When designing Hybrid Quantum Neural Networks (HQNNs), **the presumed expressibility-trainability trade-off may not hold**:

- **Pure PQC training**: Shows only a weak, regime-dependent trade-off
- **Quantum-only training in hybrid**: Trade-off increasingly disrupted by classical components
- **Full end-to-end hybrid training**: Trade-off can be **completely eliminated** — classical layers reshape the optimization landscape, decoupling trainability from PQC expressibility

**Practical implication**: Do NOT avoid expressive circuits in HQNNs out of fear of barren plateaus. Use multi-objective NAS that jointly optimizes expressibility, trainability, and task performance. Pareto-optimal architectures differ between quantum-only and full end-to-end training — always analyze under full end-to-end training for realistic results.

**Expressibility metrics**: Frame potential, KL divergence to Haar-random distribution
**Trainability metrics**: Gradient variance, Fisher information

### 1. Embedding Selection

- **angle-y embedding**: Best for normalized image features
- **amplitude embedding**: Optimal for dense vectors (requires 2^n qubits)
- **angle embedding**: General-purpose, moderate efficiency

### 2. Entangling Patterns

- **sparse CNOT**: Reduces gate count, maintains expressivity
- **full CNOT**: Maximum entanglement, higher noise sensitivity
- **linear CNOT**: Minimal overhead, suitable for shallow circuits

### 3. Circuit Cutting Strategy

When circuit exceeds qubit budget:
- Estimate cutting overhead: `O(2^k)` where k = number of cuts
- Use sparse patterns to minimize cuts
- Balance accuracy loss vs. cutting cost

### 4. Hardware Constraints

- Limit depth based on T1/T2 coherence times
- Account for gate error rates in runtime cost
- Use hardware-native gates when possible

## Common Issues

### Issue 1: Barren Plateaus

**Problem**: Gradients vanish in deep/highly-entangled circuits.

**Solution**:
- Use local cost functions
- Limit circuit depth (≤ 3 layers initial search)
- Prefer sparse entangling patterns

### Issue 2: Cutting Overhead Explosion

**Problem**: Circuit cutting leads to exponential overhead.

**Solution**:
- Set strict cutting overhead constraint in NSGA-II
- Use sparse patterns to minimize cuts
- Consider hybrid quantum-classical split earlier

### Issue 3: Noise Dominance

**Problem**: Hardware noise overwhelms signal in deep circuits.

**Solution**:
- Include noise model in evaluation
- Reduce depth for NISQ hardware (≤ 5 layers)
- Use error mitigation techniques

## Extensions

### Hybrid Quantum-Classical Networks

Extend QNAS to HQNN (Hybrid Quantum Neural Networks):

```python
hqnn_architecture = {
    'quantum_layer': {
        'type': 'qnn',
        'architecture': best_quantum_arch
    },
    'classical_layers': [
        {'type': 'dense', 'units': 128},
        {'type': 'dense', 'units': 10}
    ]
}
```

### Multi-Dataset Transfer

Transfer learned architectures across datasets:

- Pre-train SuperCircuit on large dataset
- Fine-tune search space for new dataset
- Reduce search generations via warm start

## Resources

### References

- `references/qnas_paper.md`: Original QNAS paper (2604.07013v1)
- `references/nsga2_algorithm.md`: NSGA-II algorithm details
- `references/circuit_cutting.md`: Circuit cutting techniques

### Scripts

- `scripts/build_supercircuit.py`: SuperCircuit construction
- `scripts/nsga2_optimizer.py`: NSGA-II optimization loop
- `scripts/evaluate_architecture.py`: Three-objective evaluation

## Related Skills

- **quantum-computing**: General quantum computing workflows
- **multi-objective-optimization**: NSGA-II and Pareto analysis
- **neural-architecture-search**: Classical NAS methods

---

*Extracted from arxiv:2604.07013v1 - "QNAS: A Neural Architecture Search Framework for Accurate and Efficient Quantum Neural Networks"*