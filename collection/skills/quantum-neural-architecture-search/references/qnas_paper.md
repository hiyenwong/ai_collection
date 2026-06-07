# QNAS: A Neural Architecture Search Framework for Accurate and Efficient Quantum Neural Networks

**arXiv ID**: 2604.07013v1
**Published**: 2026-04-08
**Authors**: Kooshan Maleki, Alberto Marchisio, Muhammad Shafique

## Abstract

Designing quantum neural networks (QNNs) that are both accurate and deployable on NISQ hardware is challenging. Handcrafted ansatze must balance expressivity, trainability, and resource use, while limited qubits often necessitate circuit cutting. Existing quantum architecture search methods primarily optimize accuracy while only heuristically controlling quantum and mostly ignore the exponential overhead of circuit cutting. We introduce QNAS, a neural architecture search framework that unifies hardware aware evaluation, multi objective optimization, and cutting overhead awareness for hybrid quantum classical neural networks (HQNNs). QNAS trains a shared parameter SuperCircuit and uses NSGA-II to optimize three objectives jointly: (i) validation error, (ii) a runtime cost proxy measuring wall clock evaluation time, and (iii) the estimated number of subcircuits under a target qubit budget. QNAS evaluates candidate HQNNs under a few epochs of training and discovers clear Pareto fronts that reveal tradeoffs between accuracy, efficiency, and cutting overhead. Across MNIST, Fashion-MNIST, and Iris benchmarks, we observe that embedding type and CNOT mode selection significantly impact both accuracy and efficiency, with angle-y embedding and sparse entangling patterns outperforming other configurations on image datasets, and amplitude embedding excelling on tabular data (Iris). On MNIST, the best architecture achieves 97.16% test accuracy with a compact 8 qubit, 2 layer circuit; on the more challenging Fashion-MNIST, 87.38% with a 5 qubit, 2 layer circuit; and on Iris, 100% validation accuracy with a 4 qubit, 2 layer circuit. QNAS surfaces these design insights automatically during search, guiding practitioners toward architectures that balance accuracy, resource efficiency, and practical deployability on current hardware.

## Key Contributions

### 1. Three-Objective Optimization

QNAS is the first quantum NAS framework to jointly optimize:
- **Validation error** (accuracy)
- **Runtime cost** (efficiency)
- **Cutting overhead** (deployability)

### 2. SuperCircuit Training

Shared-parameter SuperCircuit enables efficient architecture evaluation without re-training each candidate from scratch.

### 3. Hardware-Aware Evaluation

Considers NISQ hardware constraints: qubit budget, gate fidelity, coherence time.

### 4. Cutting Overhead Awareness

First NAS framework to explicitly account for exponential overhead of circuit cutting.

## Methodology Details

### SuperCircuit Architecture

```
SuperCircuit Components:
├── Data Embedding Layer
│   ├── angle-y embedding
│   ├── angle embedding
│   └── amplitude embedding
├── Entangling Layer
│   ├── sparse CNOT pattern
│   ├── full CNOT pattern
│   └── linear CNOT pattern
├── Variational Layer
│   ├── rotation gates (Rx, Ry, Rz)
│   ├── depth: 1-5 layers
└── Measurement Layer
```

### NSGA-II Optimization

**Algorithm Steps**:
1. Initialize population of candidate architectures
2. Evaluate each architecture on three objectives
3. Perform non-dominated sorting
4. Calculate crowding distance
5. Select parents via tournament selection
6. Create offspring via crossover + mutation
7. Combine parent + offspring populations
8. Select next generation via elitism
9. Repeat for N generations

### Architecture Evaluation

```python
def evaluate_hqnn(architecture):
    # Objective 1: Validation Error
    val_error = cross_validate(architecture, validation_set)
    
    # Objective 2: Runtime Cost
    runtime_cost = count_params(architecture) * circuit_depth(architecture)
    
    # Objective 3: Cutting Overhead
    if circuit_width(architecture) > qubit_budget:
        cutting_overhead = estimate_subcircuits(architecture, qubit_budget)
    else:
        cutting_overhead = 1
    
    return [val_error, runtime_cost, cutting_overhead]
```

## Experimental Results

### Benchmark Datasets

| Dataset | Type | Features | Classes |
|---------|------|----------|---------|
| MNIST | Image | 784 (28×28) | 10 |
| Fashion-MNIST | Image | 784 (28×28) | 10 |
| Iris | Tabular | 4 | 3 |

### Best Architectures Found

**MNIST**:
- Configuration: angle-y embedding, sparse CNOT, 8 qubits, 2 layers
- Accuracy: 97.16%
- Parameters: 32

**Fashion-MNIST**:
- Configuration: angle-y embedding, sparse CNOT, 5 qubits, 2 layers
- Accuracy: 87.38%
- Parameters: 20

**Iris**:
- Configuration: amplitude embedding, 4 qubits, 2 layers
- Accuracy: 100%
- Parameters: 8

### Pareto Front Analysis

QNAS discovers clear Pareto fronts showing trade-offs:

- **Accuracy vs. Efficiency**: Higher accuracy requires more qubits/depth
- **Accuracy vs. Cutting Overhead**: Limited qubits force circuit cutting
- **Efficiency vs. Cutting Overhead**: Sparse patterns reduce both

## Key Insights

### 1. Embedding Type Matters

**angle-y embedding**:
- Best for normalized features (images)
- Rotates each feature along Y-axis
- Efficient for 784-dim inputs → 8 qubits

**amplitude embedding**:
- Best for dense vectors (tabular)
- Requires 2^n qubits for n features
- Optimal for Iris (4 features → 4 qubits)

### 2. Sparse Entangling Patterns

Sparse CNOT patterns:
- Reduce gate count by 50-70%
- Maintain expressivity
- Lower noise sensitivity
- Enable deeper circuits on NISQ hardware

### 3. Circuit Cutting Trade-offs

Circuit cutting overhead:
- Exponential in number of cuts: O(2^k)
- Sparse patterns minimize cuts needed
- Balance: accept slightly lower accuracy to avoid cutting

## Limitations

### 1. Barren Plateaus
Deep/highly-entangled circuits may suffer from vanishing gradients.

### 2. Hardware Noise
Noise models not fully integrated in evaluation.

### 3. Limited Benchmark Scope
Only tested on MNIST, Fashion-MNIST, Iris.

## Future Directions

1. **Noise-aware evaluation**: Integrate realistic noise models
2. **Transfer learning**: Pre-train SuperCircuit, fine-tune for new tasks
3. **Multi-task optimization**: Optimize for multiple datasets simultaneously
4. **Real hardware deployment**: Validate on actual quantum hardware

## Reproducibility

**Code**: Will be released upon publication
**Datasets**: Publicly available (MNIST, Fashion-MNIST, Iris)
**Hyperparameters**:
- Population size: 100
- Generations: 50
- SuperCircuit epochs: 50
- Cross-validation: 5-fold

## Related Work

### Quantum Architecture Search
- **QAS** (2023): Single-objective (accuracy only)
- **Q-NAS** (2024): Hardware-aware but ignores cutting overhead

### Classical Neural Architecture Search
- **NAS** (2017): RL-based search
- **DARTS** (2018): Differentiable architecture search
- **ENAS** (2018): Shared-weight approach

QNAS combines classical NAS techniques with quantum-specific considerations.

---

*Source: arxiv:2604.07013v1*