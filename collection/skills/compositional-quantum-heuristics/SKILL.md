---
name: compositional-quantum-heuristics
description: >
  Compositional Quantum Heuristics methodology for mitigating barren plateaus
  in quantum machine learning. Assembles larger quantum models from smaller
  trainable subcomponents using group-invariant loss functions and symmetry-
  induced inductive bias. Use when building quantum ML models, designing
  parameterized quantum circuits, or addressing gradient vanishing in QML.
  arXiv:2605.07611
---

# Compositional Quantum Heuristics for QML

## Description

Addresses the barren plateau problem in quantum machine learning by
composing larger quantum models from smaller, trainable subcomponents.
Uses group-invariant loss functions to introduce symmetry-induced inductive
bias, improving gradient behavior and generalization.

## Activation Keywords
- compositional quantum heuristics
- barren plateau mitigation
- quantum ML composition
- group-invariant loss function
- permutation-equivariant QGNN
- quantum graph neural network
- symmetry-induced bias quantum
- QIRO quantum-informed recursive

## Core Methodology

### Step 1: Decompose into Subcomponents

Break the target quantum circuit into smaller sub-circuits that are:
- Classically simulable (few qubits each)
- Trainable (no barren plateaus at small scale)
- Composable (output of one feeds into next)

### Step 2: Construct Group-Invariant Loss

```python
import numpy as np

def group_invariant_loss(predictions, targets, symmetry_group):
    """Loss invariant under symmetry group transformations."""
    loss = 0.0
    for g in symmetry_group:
        # Apply group transformation to predictions
        g_preds = apply_symmetry(predictions, g)
        g_targets = apply_symmetry(targets, g)
        loss += np.mean((g_preds - g_targets) ** 2)
    return loss / len(symmetry_group)

def apply_symmetry(x, permutation):
    """Apply permutation symmetry to data."""
    return x[permutation]
```

### Step 3: Build Permutation-Equivariant QGNN

For graph problems (e.g., max-clique):
1. Encode graph structure as quantum state
2. Apply permutation-equivariant quantum layers
3. Read out invariant predictions

```python
# Pseudocode for permutation-equivariant QGNN
def qgnn_layer(adjacency, node_states, num_qubits):
    """One layer of permutation-equivariant quantum GNN."""
    # Aggregate neighbor information (equivariant)
    aggregated = adjacency @ node_states
    
    # Apply quantum circuit to each node (equivariant)
    updated = apply_parametric_circuit(aggregated, node_states)
    
    # Normalize
    return updated / np.linalg.norm(updated)
```

### Step 4: Recursive Hybrid Heuristic (QIRO-inspired)

Use trained quantum model to guide classical search:
1. Train small quantum model on subproblems
2. Use model predictions to prioritize classical search branches
3. Recurse on promising subproblems
4. Combine solutions compositionally

## Applications

- **Max-Clique Detection**: Identifying maximal cliques in graphs
- **Combinatorial Optimization**: Graph problems with symmetry
- **Graph Classification**: With permutation-invariant pooling
- **Any QML task** where circuit expressivity vs trainability trade-off exists

## Key Insights

1. **Composition beats monolith**: Smaller circuits are trainable; compose them
2. **Symmetry is free bias**: Group invariance provides inductive bias without data
3. **Recursive guidance**: Quantum models guide classical search, not replace it
4. **Generalization**: Compositional models generalize to larger instances

## Pitfalls

- Group symmetry must match problem structure (wrong group = no benefit)
- Subcomponent boundaries need careful design
- Recursive depth limited by accumulated errors
- Classical simulation of subcomponents still exponential in subcircuit size

## References
- arXiv:2605.07611 - "Compositional Quantum Heuristics for Max-Clique Detection"
- arXiv:2308.13607 - QIRO (Quantum-Informed Recursive Optimization)
