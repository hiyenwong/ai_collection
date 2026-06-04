---
name: neural-graph-embedding-qubo
description: "Neural-powered unit disk graph embedding for QUBO-to-quantum-annealer mapping. Uses neural network methods to solve the minor graph embedding problem for quantum annealers. Use when mapping QUBO problems to quantum hardware, solving graph embedding for D-Wave/quantum annealers, or optimizing qubit connectivity for optimization problems."
---

# Neural Graph Embedding for QUBO

Methodology from Vercellino, Viviani & Vitali (2026) "Neural-powered unit disk graph embedding: qubits connectivity for some QUBO problems" (arXiv:2605.04736).

## Problem

Quantum annealers have fixed hardware connectivity graphs. To run a QUBO problem, its interaction graph must be **minor-embedded** into the hardware graph — finding chains of physical qubits to represent each logical variable.

## Neural Embedding Approach

Instead of classical heuristic embedding (e.g., minorminer), use a **neural network** to learn the embedding:

1. **Represent** the problem graph and hardware graph as adjacency structures
2. **Train** a neural model to predict valid embeddings
3. **Optimize** embedding quality (chain length, chain strength) via gradient-based methods

## Key Advantages

- **Faster** than classical embedding for repeated problem types
- **Adaptive**: learns from previous embeddings
- **Quality**: can optimize for specific metrics (chain length, success rate)

## Embedding Pipeline

```
QUBO Problem Graph → Neural Encoder → Embedding Prediction → Hardware Mapping
     (logical)           (GNN/MLP)        (qubit assignment)   (physical)
```

### Step 1: Graph Representation

- Problem graph: nodes = variables, edges = QUBO couplings
- Hardware graph: fixed connectivity (e.g., Pegasus, Zephyr topology)

### Step 2: Neural Encoding

- Use GNN to encode structural features
- Positional encodings for spatial awareness
- Attention over hardware graph nodes

### Step 3: Embedding Prediction

- Output: assignment of logical variables to physical qubit chains
- Constraint satisfaction: embedding must be valid minor embedding

### Step 4: Validation & Refinement

- Verify embedding correctness
- Optimize chain strengths for annealing
- Iterate if embedding fails

## When to Use

| Scenario | Recommended |
|----------|-------------|
| Single QUBO, one-off | Classical minorminer |
| Many similar QUBOs | Neural embedding (learn once, apply many) |
| Large-scale QUBO | Neural + classical hybrid |
| Real-time embedding | Pre-trained neural model |

## Practical Tips

1. **Pre-training**: Train on a distribution of similar QUBO problems
2. **Chain length penalty**: Regularize to minimize chain lengths
3. **Hardware awareness**: Include hardware topology as input feature
4. **Fallback**: Always have classical embedding as backup

## Pitfalls

- Neural embedding may produce invalid embeddings — always validate
- Generalization to unseen problem structures may be poor
- Training data generation can be expensive
- Chain strength tuning still needed post-embedding

## Related Concepts

- QUBO: Quadratic Unconstrained Binary Optimization
- Minor embedding: Graph homomorphism with edge subdivision
- Quantum annealing: Adiabatic quantum optimization
- D-Wave: Commercial quantum annealer platform

## Activation Keywords

- QUBO embedding, quantum annealer mapping
- graph embedding, minor embedding
- neural embedding, D-Wave mapping
- qubit connectivity, quantum optimization
