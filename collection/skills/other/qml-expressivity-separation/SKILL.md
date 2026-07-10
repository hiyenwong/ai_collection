---
name: qml-expressivity-separation
description: >
  Quantum Machine Learning expressivity separation methodology. Based on
  Anschuetz & Gao (Quantum 10, 1976, 2026). Provides framework for constructing
  efficiently trainable QNNs with provable polynomial memory separations over
  classical neural networks. Use when: (1) designing QNN architectures with
  provable quantum advantage, (2) analyzing expressivity vs trainability trade-offs,
  (3) implementing quantum contextuality as computational resource, (4) comparing
  quantum vs classical sequence modeling capabilities. Keywords: quantum machine
  learning, QNN, expressivity, contextuality, polynomial separation, trainable.
---

# QML Expressivity Separation

Based on Anschuetz & Gao, "Arbitrary Polynomial Separations in Trainable Quantum Machine Learning" (Quantum 10, 1976, 2026).

## Core Result

Constructed hierarchy of **efficiently trainable QNNs** that exhibit **unconditionally provable polynomial memory separations** of arbitrary constant degree over classical neural networks (including Transformers) for classical sequence modeling tasks.

## Key Concepts

### Expressivity-Trainability Trade-off

Previous work showed a fundamental tension:
- High expressivity QNNs → exponential training time
- Trainable QNNs → limited expressivity advantage

This work **circumvents** the trade-off by:
1. Constructing QNNs with constant gate complexity per unit cell
2. Achieving polynomial (not exponential) but **arbitrary degree** separations
3. Using quantum contextuality as the resource

### Quantum Contextuality

**Definition**: Quantitative notion of semantic ambiguity — the inability to assign consistent classical values to all measurement outcomes simultaneously.

**Role in QML**: Contextuality in the quantum model's latent space is the **source** of expressivity separation. Tasks with semantic ambiguity are natural candidates for quantum advantage.

## Architecture Design

### Unit Cell Structure

```
Input → [Quantum Gate Layer] → [Measurement] → Output
              ↓
        Constant gate complexity (O(1))
```

### Key Properties

1. **Efficient Trainability**: Gradient-based optimization converges in polynomial time
2. **Polynomial Separation**: Memory advantage of degree d for any constant d
3. **Constant Gate Complexity**: Each unit cell uses O(1) gates
4. **Sequence Modeling**: Applicable to classical sequential data tasks

## Implementation Framework

### Step 1: Define the Task

```python
# Sequence modeling task with semantic ambiguity
# Example: Natural language understanding, temporal patterns
# where context changes meaning (contextuality-friendly)
def task(x_sequence):
    # Input: sequence of symbols
    # Output: classification/prediction
    return model(x_sequence)
```

### Step 2: Construct the QNN

```python
import pennylane as qml
import numpy as np

def qnn_unit_cell(wires, params):
    """Single unit cell with constant gate complexity."""
    n_wires = len(wires)
    
    # Ansatz with O(1) gates per cell
    for i, w in enumerate(wires):
        qml.Rot(params[i, 0], params[i, 1], params[i, 2], wires=w)
    
    # Entangling layer
    for i in range(len(wires) - 1):
        qml.CZ(wires=[wires[i], wires[i+1]])
    
    return qml.state()

def qnn_circuit(inputs, params, n_layers):
    """Full QNN with multiple unit cells."""
    n_qubits = len(inputs)
    wires = range(n_qubits)
    
    # Encode input
    for i, x in enumerate(inputs):
        qml.RY(x, wires=i)
    
    # Apply unit cells
    for layer in range(n_layers):
        qnn_unit_cell(wires, params[layer])
    
    # Measure observables
    return [qml.expval(qml.PauliZ(i)) for i in wires]
```

### Step 3: Training Loop

```python
def train_qnn(qnn, data, labels, n_steps, lr=0.01):
    """Gradient-based training (efficiently trainable by construction)."""
    params = initialize_params()
    
    for step in range(n_steps):
        # Forward pass
        predictions = qnn(data, params)
        
        # Compute loss
        loss = compute_loss(predictions, labels)
        
        # Compute gradients (efficient due to structure)
        grads = qml.grad(loss_fn)(params)
        
        # Update
        params -= lr * grads
    
    return params
```

## When to Use This Approach

### Suitable Tasks
- **Sequence modeling** with contextual/ambiguous semantics
- **Natural language** understanding tasks
- **Temporal pattern** recognition
- Tasks where classical models need large context windows

### Unsuitable Tasks
- Tasks already efficiently solvable classically
- Problems without inherent ambiguity/complexity
- Tasks where polynomial separation is insufficient

## Theoretical Guarantees

| Property | Guarantee |
|----------|-----------|
| Trainability | Polynomial time convergence |
| Expressivity | Degree-d polynomial separation |
| Gate Complexity | O(1) per unit cell |
| Classical Hardness | Unconditional proof |

## Relationship to Other Work

- **Complements** Google's RL-QEC work: This paper addresses algorithmic expressivity, RL-QEC addresses hardware control
- **Contrasts** with exponential separation claims: Focuses on **trainable** models with realistic advantages
- **Connects** to contextuality literature: Formalizes contextuality as ML resource

## References

- Quantum 10, 1976 (2026) - Main paper
- arXiv:2402.08606v4 - Preprint version
- "Does provable absence of barren plateaus imply classical simulability?" (Nature Communications, 2025)
