---
name: equivariant-rl-quantum-circuit-synthesis
description: "Equivariant reinforcement learning for Clifford quantum circuit synthesis. Use when designing RL-based quantum circuit synthesis, leveraging group symmetries in quantum operations, or building equivariant architectures for quantum computing tasks."
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
---

# Equivariant RL for Quantum Circuit Synthesis

Methodology from arXiv:2605.10910 - "Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis" (Yeung, Kissinger, Cornish, 2026-05-12).

## Overview

This skill provides a framework for using equivariant reinforcement learning to synthesize Clifford quantum circuits. By leveraging the group symmetry properties of the Clifford group, the method achieves more efficient circuit synthesis compared to standard RL approaches.

## Core Concepts

### 1. Clifford Group Symmetries
- The Clifford group forms a unitary 2-design with rich symmetry structure
- Circuits are equivalent up to Clifford group transformations
- Symmetry-aware policies reduce the search space exponentially

### 2. Equivariant Architecture
- **Equivariant Policy Network**: Network outputs transform consistently under Clifford group actions
- **Group-equivariant layers**: Use steerable features that respect Clifford symmetries
- **Symmetry reduction**: Collapse equivalent states to canonical representatives

### 3. RL Formulation
- **State**: Current quantum circuit (gate sequence + qubit connectivity)
- **Action**: Add/remove/modify gates (H, S, CNOT, CZ, etc.)
- **Reward**: Negative circuit depth + correctness bonus
- **Episode**: Until target unitary is achieved within tolerance

## Implementation

### Step 1: State Representation
```python
import numpy as np
from stim import Tableau

class CliffordState:
    """Represent quantum circuit state via stabilizer tableau."""
    
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits
        self.tableau = Tableau(n_qubits)
        self.gates = []
        
    def apply_gate(self, gate_name, qubits):
        """Apply Clifford gate to tableau."""
        if gate_name == "H":
            self.tableau.append_H(qubits[0])
        elif gate_name == "S":
            self.tableau.append_S(qubits[0])
        elif gate_name == "CNOT":
            self.tableau.append_CX(qubits[0], qubits[1])
        elif gate_name == "CZ":
            self.tableau.append_CZ(qubits[0], qubits[1])
        
        self.gates.append((gate_name, qubits))
        
    def canonical_form(self):
        """Return canonical representative under Clifford equivalence."""
        # Use Gaussian elimination on stabilizer tableau
        return self.tableau.to_pauli_string()
        
    def circuit_depth(self):
        """Calculate circuit depth."""
        if not self.gates:
            return 0
        # Track qubit usage timeline
        timelines = {i: 0 for i in range(self.n_qubits)}
        depth = 0
        for gate, qubits in self.gates:
            max_time = max(timelines[q] for q in qubits) + 1
            for q in qubits:
                timelines[q] = max_time
            depth = max(depth, max_time)
        return depth
```

### Step 2: Equivariant Policy Network
```python
import torch
import torch.nn as nn

class EquivariantCliffordPolicy(nn.Module):
    """Equivariant policy for Clifford circuit synthesis."""
    
    def __init__(self, n_qubits, hidden_dim=128):
        super().__init__()
        self.n_qubits = n_qubits
        self.hidden_dim = hidden_dim
        
        # Equivariant layers
        self.state_encoder = nn.Sequential(
            nn.Linear(n_qubits * n_qubits, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        
        # Gate selection head (equivariant under qubit permutation)
        self.gate_selector = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 4)  # H, S, CNOT, CZ
        )
        
        # Qubit selection head
        self.qubit_selector = nn.Sequential(
            nn.Linear(hidden_dim, n_qubits)
        )
        
    def forward(self, state_tableau):
        """
        Args:
            state_tableau: Stabilizer tableau as binary matrix
        Returns:
            gate_probs: Distribution over gate types
            qubit_probs: Distribution over qubit choices
        """
        # Encode tableau
        tableau_flat = state_tableau.reshape(-1, self.n_qubits * self.n_qubits)
        features = self.state_encoder(tableau_flat.float())
        
        # Gate selection
        gate_probs = torch.softmax(self.gate_selector(features), dim=-1)
        
        # Qubit selection (permutation-equivariant)
        qubit_probs = torch.softmax(self.qubit_selector(features), dim=-1)
        
        return gate_probs, qubit_probs
```

### Step 3: Training Loop
```python
import torch
from torch.optim import Adam

def train_equivariant_rl(policy, target_unitary, n_episodes=1000, lr=1e-3):
    """Train equivariant policy for circuit synthesis."""
    optimizer = Adam(policy.parameters(), lr=lr)
    
    for episode in range(n_episodes):
        state = CliffordState(policy.n_qubits)
        done = False
        log_probs = []
        rewards = []
        
        while not done:
            # Get policy distribution
            tableau = state.tableau.to_numpy()
            gate_probs, qubit_probs = policy(tableau)
            
            # Sample action
            gate_idx = torch.multinomial(gate_probs[0], 1).item()
            qubit_idx = torch.multinomial(qubit_probs[0], 1).item()
            
            # Apply action
            gates = ["H", "S", "CNOT", "CZ"]
            gate = gates[gate_idx]
            qubits = [qubit_idx, (qubit_idx + 1) % policy.n_qubits]
            state.apply_gate(gate, qubits)
            
            # Calculate reward
            current = state.tableau.to_numpy()
            target = target_unitary.to_numpy()
            match = np.allclose(current, target, atol=1e-8)
            
            reward = -state.circuit_depth() * 0.1
            if match:
                reward += 100
                done = True
            
            if state.circuit_depth() > 50:
                done = True
                reward = -50
                
            log_probs.append(torch.log(gate_probs[0, gate_idx] * qubit_probs[0, qubit_idx]))
            rewards.append(reward)
        
        # REINFORCE update
        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + 0.99 * G
            returns.insert(0, G)
        
        returns = torch.tensor(returns)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
        loss = -sum(lp * ret for lp, ret in zip(log_probs, returns))
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if episode % 100 == 0:
            print(f"Episode {episode}, Return: {sum(rewards):.2f}, Depth: {state.circuit_depth()}")
```

### Step 4: Symmetry Reduction
```python
from itertools import permutations

def get_clifford_symmetries(n_qubits):
    """Get symmetry operations for n-qubit Clifford group."""
    # Qubit permutations
    qubit_perms = list(permutations(range(n_qubits)))
    
    # Pauli frame changes (2^2n possibilities for n qubits)
    pauli_frames = []
    for i in range(2**(2*n_qubits)):
        frame = [(i >> (2*j)) & 3 for j in range(n_qubits)]
        pauli_frames.append(frame)
        
    return qubit_perms, pauli_frames

def canonicalize_state(state, symmetries):
    """Find canonical representative under symmetry group."""
    qubit_perms, pauli_frames = symmetries
    
    best_state = None
    best_repr = None
    
    for perm in qubit_perms:
        for frame in pauli_frames:
            # Apply symmetry transformation
            transformed = apply_symmetry(state, perm, frame)
            repr_str = transformed.canonical_form()
            
            if best_repr is None or repr_str < best_repr:
                best_repr = repr_str
                best_state = transformed
                
    return best_state
```

## Key Patterns

### Pattern 1: Equivariant Design
- Design networks that respect physical symmetries
- Reduce search space by factoring out equivalent configurations
- Use steerable features for consistent transformations

### Pattern 2: Symmetry-Aware RL
- Canonicalize states before processing
- Augment experiences with symmetric equivalents
- Reward shaping that respects symmetry structure

### Pattern 3: Stabilizer-Based Representation
- Use stabilizer tableaux for efficient Clifford circuit simulation
- Gaussian elimination for canonical forms
- Binary matrix representation for neural network input

## Tools & Dependencies

```bash
pip install torch stim numpy
```

## Activation

- equivariant RL
- quantum circuit synthesis
- clifford group
- symmetry-aware reinforcement learning
- steerable neural networks
- 量子电路合成
- 等变强化学习

## Related Skills

- `quantum-neural-architecture`: For general QNN design
- `quantum-ml-patterns`: For quantum ML research patterns
- `rl-temporal-logic`: For RL with formal guarantees

## References

- Yeung, R., Kissinger, A., & Cornish, R. (2026). "Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis" arXiv:2605.10910
- Gottesman, D. (1998). "The Heisenberg Representation of Quantum Computers" arXiv:quant-ph/9807006
- Cohen, T. et al. (2019). "Gauge Equivariant Convolutional Networks" ICLR 2019

## Pitfalls

1. **State explosion**: Without symmetry reduction, Clifford circuit search space grows as O(4^n)
2. **Tableau updates**: stim library is fast but requires proper installation
3. **Canonical forms**: Gaussian elimination on stabilizer tableaux is O(n^3)
4. **Reward design**: Simple depth-based rewards may lead to suboptimal local minima
