---
name: equivariant-rl-clifford
description: "Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis. Synthesizes optimal Clifford quantum circuits using RL with qubit-permutation-equivariant neural networks. Use when: synthesizing quantum circuits, Clifford gate optimization, quantum circuit compilation, equivariant neural networks for quantum computing, RL for quantum tasks, or qubit relabeling invariance."
---

# Equivariant RL for Clifford Circuit Synthesis

Synthesize Clifford quantum circuits using RL with qubit-permutation-equivariant neural networks (arXiv: 2605.10910).

## Core Problem

Synthesizing Clifford circuits for all-to-all qubit connectivity devices. The key challenge: the search space grows factorially with qubit count, but the underlying problem is invariant to qubit relabeling.

## Key Insight

A neural network policy that is **equivariant to qubit permutations** can learn a single policy that works across all qubit counts, rather than training separate policies per qubit count.

## Architecture

### Equivariant Policy Network

- **Input**: Clifford state representation (stabilizer tableau or symplectic matrix)
- **Equivariance**: Permutations of qubit labels in input produce corresponding permutations in output
- **Size-agnostic**: Single trained policy works for any qubit count
- **Output**: Distribution over valid Clifford gate actions (H, S, CNOT)

### RL Training

- **Environment**: Clifford circuit synthesis task
- **State**: Current unitary (represented as stabilizer tableau)
- **Action**: Apply Clifford gate (H, S, CNOT on any qubit pair)
- **Reward**: Negative circuit depth / gate count (minimize gates)
- **Termination**: Target unitary reached

## Results

- Finds circuits within **one two-qubit gate of optimality** in milliseconds per instance
- **99.2% optimal** circuit discovery rate
- Single policy generalizes across qubit counts

## Workflow for Agents

### Step 1: Define Target Unitary

Express the target Clifford operation as:
- Stabilizer tableau (binary symplectic matrix)
- Or as a composition of known Clifford gates

### Step 2: Run Synthesis

```python
# Pseudocode for synthesis
def synthesize_clifford(target_unitary, max_steps=1000):
    state = identity_tableau(target_unitary.n_qubits)
    circuit = []
    for step in range(max_steps):
        action = equivariant_policy(state)  # (gate_type, qubit_indices)
        state = apply_gate(state, action)
        circuit.append(action)
        if state == target_unitary:
            break
    return circuit
```

### Step 3: Optimize Circuit

Post-process to merge adjacent gates and remove identities.

## Design Principles

1. **Equivariance over invariance**: The policy output must permute consistently with input qubit permutations, not stay fixed
2. **Size-agnostic training**: Train on mixed qubit counts to enable generalization
3. **Symplectic representation**: Use binary symplectic matrices (tableaux) for efficient Clifford state representation
4. **Reward shaping**: Penalize two-qubit gates more heavily than single-qubit gates

## When to Use

- Clifford circuit synthesis for NISQ devices
- Quantum compiler optimization
- Any task requiring minimal-depth Clifford circuits
- When circuit synthesis must generalize across qubit counts

## Related Skills

- quantum-neural-network-designer
- quantum-error-correction-methods
- quantum-circuit-synthesis-gst
