---
name: gqml-graph-models-toolbox
description: "Geometric Quantum Machine Learning (GQML) toolbox for graph problems — comprehensive characterization of constituents for n-node graphs encoded in n-qubit states. Provides design patterns for quantum graph models including natural classical integration, expressivity extension, and classical pre-training strategies. arXiv:2607.00698"
tags: ["geometric-qml", "quantum-graph-learning", "equivariant-quantum", "graph-encoding", "classical-pretraining", "GQML"]
---

# GQML Graph Models Toolbox

## Description

Geometric Quantum Machine Learning (GQML) design toolbox for graph-structured problems. Provides comprehensive characterization of quantum graph model constituents when n-node graphs are encoded in n-qubit states, with patterns for classical integration, expressivity extension at minimal cost, and classical pre-training strategies. arXiv:2607.00698

## Activation Keywords
- quantum graph learning
- GQML graph models
- geometric quantum ML graphs
- equivariant quantum graph
- quantum graph neural network
- n-qubit graph encoding
- classical pretraining quantum

## Core Contributions

### Toolbox Components
1. **Graph Encoding Strategies**: How to map n-node graphs to n-qubit states
2. **Equivariant Layer Design**: Quantum layers respecting graph symmetries
3. **Classical Integration**: Natural hybrid classical-quantum architecture patterns
4. **Expressivity Extension**: Methods to extend known GQML models at virtually no cost
5. **Classical Pre-training**: Strategies for pre-training quantum graph models classically

### Key Insights
- GQML models for graphs lack the detailed understanding that classical GML has
- n-node graphs → n-qubit states provides natural encoding with structure preservation
- Classical pre-training enables effective initialization of quantum graph models

## Instructions for Agents

### Step 1: Choose Graph Encoding
For n-node graphs encoded in n-qubit states:

```python
# Graph-to-quantum encoding patterns

# Pattern A: Adjacency matrix encoding
# Each qubit represents a node, entanglement encodes edges
def adjacency_encoding(adj_matrix):
    n = len(adj_matrix)
    circuit = QuantumCircuit(n)
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j] == 1:
                circuit.cz(i, j)  # Entangle connected nodes
    return circuit

# Pattern B: Node feature encoding
# Classical node features → quantum amplitudes
def feature_encoding(node_features):
    # Amplitude encoding: features → state amplitudes
    state = normalize(node_features)
    return state_prepare_circuit(state)
```

### Step 2: Design Equivariant Layers
Quantum layers that respect graph symmetries:

```python
# Equivariant quantum graph layer
class EquivariantQuantumGraphLayer:
    def __init__(self, n_qubits, symmetry_group):
        # Generators must commute with symmetry group action
        self.generators = self._equivariant_generators(symmetry_group)
        self.circuit = ParameterizedQuantumCircuit(
            n_qubits=n_qubits,
            generators=self.generators
        )
    
    def _equivariant_generators(self, group):
        # Find generators that respect graph automorphisms
        # Only include terms invariant under group action
        return [g for g in all_generators if commutes_with(g, group)]
```

### Step 3: Apply Classical Pre-training
```python
# Classical pre-training → Quantum fine-tuning

# Phase 1: Train classical graph model
classical_model = GraphNeuralNetwork(...)
classical_model.train(graph_dataset)

# Phase 2: Transfer to quantum model
# Initialize quantum parameters from classical weights
quantum_model = QuantumGraphModel(...)
quantum_model.initialize_from(classical_model)

# Phase 3: Fine-tune quantum model
quantum_model.fine_tune(graph_dataset, lr=1e-3)
```

### Step 4: Extend Expressivity
Extend existing GQML models at minimal cost:

```python
# Expressivity extension patterns

# 1. Add symmetry-preserving entanglement
extended_circuit = base_circuit + equivariant_entanglement_layer()

# 2. Multi-scale processing
for scale in [coarse, medium, fine]:
    circuit.add_layer(pool_to_scale(scale), equivariant_layer(scale))

# 3. Classical-quantum fusion
output = fuse(classical_gnn(graph), quantum_gnn(graph))
```

## Design Patterns

### Pattern 1: Graph Classification
```
Input Graph → Encode (n nodes → n qubits)
            → Equivariant Quantum Layers
            → Measurement → Classical Classifier
            → Graph Label
```

### Pattern 2: Node Property Prediction
```
Input Graph → Node-wise quantum encoding
            → Local quantum message passing
            → Node-wise measurement
            → Per-node predictions
```

### Pattern 3: Link Prediction
```
Input Graph + Node Pair → Quantum similarity encoding
                        → Entanglement-based similarity measure
                        → Link probability
```

## Pitfalls

1. **Encoding overhead**: Naive graph encoding may require O(n²) gates
   - Solution: Use sparse encoding or approximate methods
   
2. **Symmetry violation**: Incorrect equivariant design breaks guarantees
   - Solution: Verify commutation with symmetry group algebraically
   
3. **Classical pre-training gap**: Classical weights may not map well to quantum
   - Solution: Use structured initialization that respects quantum constraints
   
4. **Scalability**: n-qubit encoding limits to small graphs on NISQ
   - Solution: Use graph coarsening or subgraph sampling

## Related Skills
- `qml-graph-models-geometric-toolbox` - Existing GQML design toolbox
- `dla-trainability-by-design` - Trainability-by-Design for QML
- `quantum-ml-patterns` - General QML patterns

## Resources
- `scripts/graph_encoding.py` - Graph-to-quantum encoding utilities
- `references/gqml_theory.md` - Geometric QML theory primer
