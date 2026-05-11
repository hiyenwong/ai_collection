---
name: compositional-quantum-heuristics
description: "Design compositional quantum models that avoid barren plateaus by assembling smaller trainable subcomponents. Use when building quantum neural networks, quantum graph algorithms, or combinatorial optimization solvers. Triggers: barren plateau, quantum composition, compositional QML, quantum graph neural network, max-clique, group-invariant loss, symmetry-induced bias, permutation-equivariant, recursive quantum heuristic, quantum subcircuit assembly"
---

# Compositional Quantum Heuristics

## Overview

This skill provides patterns for building quantum machine learning models compositionally — assembling larger quantum models from smaller, independently trainable subcomponents. This approach directly addresses the **barren plateau** problem in QML, where deep quantum circuits have vanishing gradients that prevent effective training.

Based on: *Compositional Quantum Heuristics for Max-Clique Detection* (arxiv:2605.07611, May 2026).

## Core Problem: Barren Plateaus

In deep variational quantum circuits, the gradient magnitude decreases exponentially with circuit depth:

```
|∇L(θ)|² ≈ O(1/2ⁿ)  where n = number of qubits
```

This makes gradient-based training impossible for circuits beyond ~20 qubits without special structure.

## Technique 1: Compositional Model Assembly

Instead of training one large circuit, decompose the problem:

```
Large Circuit C(θ) → Compose[C₁(θ₁), C₂(θ₂), ..., Cₖ(θₖ)]
```

Each subcircuit Cᵢ is small enough to remain trainable (avoids barren plateaus), and the composition preserves expressivity.

**When to use:** Any quantum circuit with >10 qubits where gradient vanishing is observed.

**Steps:**
1. Identify problem structure that allows decomposition (e.g., graph subproblems)
2. Design subcircuits C₁...Cₖ, each with ≤10 qubits
3. Train each subcircuit independently
4. Compose outputs via classical post-processing or light entanglement

## Technique 2: Group-Invariant Loss Functions

Design loss functions invariant under symmetry groups of the problem:

```python
# Symmetry-induced inductive bias
def group_invariant_loss(predictions, targets, symmetry_group):
    """Loss invariant under problem symmetry group action."""
    # Average loss over group orbit
    total_loss = 0
    for g in symmetry_group:
        transformed_preds = g.apply(predictions)
        total_loss += standard_loss(transformed_preds, targets)
    return total_loss / len(symmetry_group)
```

**Benefits:**
- Reduces effective parameter search space
- Enforces problem-specific constraints
- Improves sample complexity by |G| factor (group order)

## Technique 3: Permutation-Equivariant Quantum GNNs

For graph problems (max-clique, TSP, graph isomorphism), use permutation-equivariant architectures:

```python
# Permutation-equivariant quantum graph neural network
def perm_equivariant_qgnn(graph_state, adjacency):
    """
    Quantum GNN that respects graph permutation symmetry:
    f(P·A·P⁻¹, P·x) = P·f(A, x)
    """
    # Message passing via quantum gates conditioned on adjacency
    for layer in range(depth):
        for edge in adjacency.edges():
            apply_controlled_gate(qubit_i=edge.u, qubit_j=edge.v, gate=RYY)
        # Node update via variational layer
        for node in adjacency.nodes():
            apply_variational_layer(qubit=node, params=θ[layer])
    return measure()
```

**Applicable problems:** Max-clique detection, graph coloring, community detection, molecular property prediction.

## Technique 4: Recursive Hybrid Quantum-Classical Heuristic

Combine quantum subroutines with classical recursive decomposition:

```
function Solve(problem):
    if size(problem) ≤ threshold:
        return QuantumSubroutine(problem)
    
    subproblems = ClassicalDecompose(problem)
    partial_solutions = [Solve(sp) for sp in subproblems]
    return ClassicalMerge(partial_solutions)
```

**Key insight:** Each recursive call operates on smaller instances that are easier for quantum circuits to handle, while the classical layer manages the global structure.

## Activation Scenarios

Use this skill when:
- Designing quantum circuits for combinatorial optimization
- Encountering barren plateaus in QML training
- Building quantum models for graph-structured data
- Need to scale quantum algorithms beyond ~10-20 qubits
- Working on max-clique, TSP, graph partitioning, or similar problems

## Anti-Patterns to Avoid

1. **Monolithic deep circuits** — Don't build one 50-qubit circuit; decompose into 5×10-qubit circuits
2. **Ignoring symmetry** — Don't use generic loss functions when problem has known symmetries
3. **Pure quantum** — Don't try to solve everything quantum; use hybrid recursive approach
4. **Random initialization** — Initialize subcircuits near identity to stay in trainable regime
