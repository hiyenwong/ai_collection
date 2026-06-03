# QNAS Methodology

## Paper Information

- **Title**: QNAS: A Neural Architecture Search Framework for Accurate and Efficient Quantum Neural Networks
- **arXiv ID**: 2604.07013v1
- **Authors**: Kooshan Maleki, Alberto Marchisio, Muhammad Shafique
- **Date**: 2026-04-08

## Core Problem

Designing quantum neural networks (QNNs) for NISQ hardware faces three challenges:
1. **Expressivity vs. Trainability** - More gates ≠ better performance
2. **Resource Constraints** - Limited qubits require circuit cutting (exponential overhead)
3. **Hardware Compatibility** - Different hardware favors different architectures

Existing quantum architecture search methods optimize accuracy only, ignoring efficiency and cutting overhead.

## QNAS Solution

### Key Innovation

Multi-objective optimization with three objectives:
1. **Validation Error** - Accuracy measure
2. **Runtime Cost Proxy** - Wall-clock evaluation time
3. **Cutting Overhead** - Number of subcircuits needed

### SuperCircuit Approach

Instead of training each architecture independently:

1. **Parameterized SuperCircuit**: Single circuit with shared parameters
2. **Architecture Sampling**: Sample sub-architectures from SuperCircuit
3. **Few-Epoch Evaluation**: Quick evaluation (not full training)
4. **NSGA-II Optimization**: Evolutionary multi-objective search

### Algorithm Flow

```python
# QNAS Algorithm
def qnas_search(super_circuit, objectives, qubit_budget):
    # Initialize population
    population = random_architectures(super_circuit)
    
    for generation in range(max_gen):
        # Evaluate each architecture
        fitness = []
        for arch in population:
            # Three objectives
            acc = evaluate_accuracy(arch, few_epochs=True)
            runtime = runtime_proxy(arch)
            cuts = estimate_subcircuits(arch, qubit_budget)
            fitness.append([acc, runtime, cuts])
        
        # NSGA-II evolution
        population = nsga2_evolve(population, fitness)
    
    # Return Pareto front
    return pareto_front(population, fitness)
```

## Key Findings

### Embedding Type Impact

| Embedding | Best Use | Performance |
|-----------|----------|-------------|
| **Angle-Y** | Image data (MNIST, Fashion-MNIST) | Highest accuracy |
| **Amplitude** | Tabular data (Iris) | 100% validation accuracy |
| **Angle-X/Z** | Mixed data | Lower efficiency |

### Entangling Pattern Impact

| Pattern | Efficiency | Accuracy |
|---------|------------|----------|
| **Sparse (linear/ring)** | High | Good |
| **Dense (full CNOT)** | Low | Slightly better |

**Recommendation**: Sparse patterns win due to efficiency gains outweighing small accuracy loss.

### Results Summary

| Dataset | Best Architecture | Accuracy | Qubits | Layers |
|---------|-------------------|----------|--------|--------|
| MNIST | Angle-Y + Sparse | 97.16% | 8 | 2 |
| Fashion-MNIST | Angle-Y + Sparse | 87.38% | 5 | 2 |
| Iris | Amplitude | 100% | 4 | 2 |

## Implementation Guide

### Step 1: Define Search Space

```python
search_space = {
    'embedding': ['angle-y', 'angle-x', 'amplitude'],
    'entangling': ['linear', 'ring', 'full'],
    'layers': [1, 2, 3, 4],
    'gates_per_layer': [1, 2, 3]
}
```

### Step 2: Build SuperCircuit

```python
class SuperCircuit:
    def __init__(self, max_qubits=8, max_layers=4):
        self.shared_params = ParameterVector('θ', max_params)
        self.embedding_gates = {...}
        self.entangling_patterns = {...}
    
    def sample_architecture(self, config):
        """Sample specific architecture from SuperCircuit"""
        circuit = QuantumCircuit(config['qubits'])
        # Add embedding layer
        # Add entangling layers
        return circuit
```

### Step 3: Multi-objective Evaluation

```python
def evaluate_architecture(arch_config):
    # Objective 1: Accuracy (few epochs)
    acc = quick_train_and_eval(arch_config, epochs=5)
    
    # Objective 2: Runtime proxy
    depth = calculate_depth(arch_config)
    runtime = depth * gate_time + classical_overhead
    
    # Objective 3: Cutting overhead
    cuts = estimate_cuts(arch_config, target_qubits)
    overhead = cuts * classical_recombine_cost
    
    return [-acc, runtime, overhead]  # Negative for minimization
```

### Step 4: NSGA-II Search

```python
from pymoo.algorithms.moo.nsga2 import NSGA2

problem = QuantumNASProblem(search_space, qubit_budget)
algorithm = NSGA2(pop_size=50)
result = minimize(problem, algorithm, termination=('n_gen', 100))

# Extract Pareto front
pareto_solutions = result.X[result.F[:, 0] <= threshold]
```

## Design Principles

### 1. Hardware-Aware Evaluation

Always evaluate on target hardware constraints:
- Qubit count limits
- Gate fidelity
- Coherence time
- Classical communication latency

### 2. Trade-off Awareness

Understand three-way trade-off:
- More accuracy → More resources
- Fewer resources → Circuit cutting overhead
- Efficient design → Pareto-optimal choices

### 3. Quick Evaluation

Don't train fully during search:
- Use shared parameters from SuperCircuit
- Train 5-10 epochs only
- Full training only on final selected architecture

## Practical Recommendations

### For Image Classification
- Use **angle-Y embedding**
- Use **sparse entangling** (linear/ring)
- Start with 8 qubits, 2 layers
- Expect ~97% on MNIST, ~87% on Fashion-MNIST

### For Tabular Data
- Use **amplitude embedding**
- Start with 4 qubits, 2 layers
- Expect ~100% on simple datasets (Iris)

### For Complex Tasks
- Increase search space dimensions
- Increase NSGA-II generations
- Consider hybrid quantum-classical approaches

## Limitations

- SuperCircuit assumes parameter sharing validity
- Few-epoch evaluation may miss convergence issues
- Cutting overhead estimation is approximate
- Hardware simulation may not match real device

## Future Directions

- Hardware-specific optimization (IBM, Rigetti, IonQ)
- Noise-aware architecture search
- Dynamic architecture adaptation
- Quantum-classical co-design

## References

- Original paper: https://arxiv.org/abs/2604.07013
- NSGA-II algorithm: Deb et al., IEEE TEVC 2002
- Circuit cutting: Peng et al., arxiv:1904.00102