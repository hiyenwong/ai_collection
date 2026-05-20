---
name: equivariant-rl-clifford
description: Equivariant reinforcement learning methodology for Clifford quantum circuit synthesis — using group-equivariant policies to learn optimal Clifford gate sequences. Use when designing quantum circuit compilers, optimizing Clifford circuits, or applying RL to quantum compilation.
---

# Equivariant RL for Clifford Circuit Synthesis

## Core Concept

Use equivariant reinforcement learning to synthesize Clifford circuits by exploiting the group structure of the Clifford group. The policy is designed to be equivariant under Clifford group symmetries, dramatically reducing the search space and improving generalization.

## Technical Approach

1. **Clifford Group Symmetry**: The Clifford group C_n forms a finite group with known structure
2. **Equivariant Policy**: π(g·s) = g·π(s) ensures policy respects group symmetries
3. **State Representation**: Stabilizer tableau or symplectic matrix representation
4. **Action Space**: Clifford gate set {H, S, CNOT}

## Key Advantages

- **Sample Efficiency**: Equivariance reduces effective state space by |C_n| factor
- **Generalization**: Policies trained on subset of states generalize to symmetry-related states
- **Optimality**: Converges to shorter circuits than non-equivariant approaches

## Usage Patterns

### Pattern 1: Clifford Circuit Synthesis
1. Represent target unitary as stabilizer tableau
2. Define equivariant policy over Clifford group actions
3. Train RL agent with reward = -circuit_depth
4. Extract optimal gate sequence from trained policy

### Pattern 2: Circuit Optimization
1. Start with initial (possibly suboptimal) Clifford circuit
2. Apply equivariant RL to find shorter equivalent circuit
3. Exploit stabilizer formalism for efficient equivalence checking
4. Achieve depth reduction while preserving functionality

## Activation Keywords
- equivariant RL Clifford synthesis
- Clifford circuit optimization RL
- group-equivariant quantum compilation
- RL quantum circuit design
- Clifford group symmetry learning
- stabilizer circuit synthesis
