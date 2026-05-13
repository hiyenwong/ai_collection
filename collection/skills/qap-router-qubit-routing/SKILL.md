---
name: qap-router-qubit-routing
description: Dynamic Quadratic Assignment Problem (QAP) formulation for qubit routing with reinforcement learning. Structure-aware Transformer with flow×distance attention, PPO training, and bidirectional refinement.
---

# QAP-Router: Qubit Routing via Dynamic QAP

## Description
Methodology for solving the NP-hard qubit routing problem by reformulating it as a dynamic Quadratic Assignment Problem (QAP) with reinforcement learning. Based on arXiv:2605.12365 "QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforcement Learning." Achieves 15.7–30.4% CNOT reduction vs industry compilers.

## Activation Keywords
- qubit routing, quadratic assignment problem, quantum compilation, SWAP optimization, structure-aware Transformer, reinforcement learning routing, flow matrix, distance matrix, dynamic assignment, PPO training, CNOT reduction, circuit mapping, lookahead planning, combinatorial optimization

## Core Methodology

### 1. Dynamic QAP Formulation
Model qubit routing as dynamic QAP:
- **Flow matrix F**: Logical qubit interactions (from circuit DAG)
- **Distance matrix D**: Hardware connectivity topology
- **Objective**: minimize Tr(F · X · D · X^T) over time, where X is the qubit mapping

### 2. Circuit Decomposition
Partition quantum circuit into time slices:
- Convert circuit to DAG
- Group parallel two-qubit gates into depthwise slices
- Each slice = one QAP sub-problem
- Solve sequentially with state carryover

### 3. Solution-Aware Transformer
Custom attention mechanism encoding problem structure:
- **Flow-distance attention**: Scale attention by F · D product
- **Interaction-distance coupling**: Directly encoded into attention scores
- **State encoding**: Current mapping X as positional information
- **Look-ahead embedding**: Future interaction sequence with decay

### 4. RL Environment Design
```
State: (X, F, F_lookahead, D)
Action: SWAP(u, v) on device edge
Reward: α · ΔQAP + β · SWAP_penalty + γ · gate_scheduling_bonus
```

### 5. Decay-Weighted Look-Ahead Reward
```
R_t = Σ_h γ^h · (QAP_improvement_h - SWAP_cost_h)
```
- Exponential decay factor γ balances immediate vs long-term gains
- Captures global optimization in local decisions

### 6. Training Protocol
- **Algorithm**: PPO (Proximal Policy Optimization)
- **Data**: 10M–50M timesteps on synthetic random circuits
- **Robustness**: Random initial mappings during training
- **Generalization**: No fine-tuning needed for real circuits

### 7. Bidirectional Refinement Pipeline
```
Forward Pass → Backward Pass (reversed order) → Forward Pass
```
- Forward: Solve slices in circuit order
- Backward: Propagate late-interaction information backward
- Final Forward: Combine global context from both directions

## Implementation Pattern

```python
import numpy as np
from scipy.sparse import csr_matrix

class QAPRouter:
    def __init__(self, hardware_topology, lookahead_depth=3, gamma=0.9):
        self.n_qubits = len(hardware_topology)
        self.distance_matrix = self._build_distance_matrix(hardware_topology)
        self.lookahead_depth = lookahead_depth
        self.gamma = gamma
    
    def _build_distance_matrix(self, topology):
        """Build shortest-path distance matrix from hardware graph."""
        n = len(topology)
        D = np.full((n, n), np.inf)
        np.fill_diagonal(D, 0)
        for u, v in topology:
            D[u][v] = D[v][u] = 1
        # Floyd-Warshall for all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        return D
    
    def compute_flow_matrix(self, circuit_slice):
        """Extract logical qubit interaction frequencies."""
        F = np.zeros((self.n_qubits, self.n_qubits))
        for gate in circuit_slice:
            q1, q2 = gate.qubits
            F[q1][q2] = F[q2][q1] = 1
        return F
    
    def qap_cost(self, F, X, D):
        """Compute Tr(F · X · D · X^T)."""
        return np.trace(F @ X @ D @ X.T)
    
    def reward(self, old_cost, new_cost, n_swaps):
        """Compute reward with decay-weighted lookahead."""
        qap_improvement = old_cost - new_cost
        swap_penalty = n_swaps * 2.0  # Penalize each SWAP
        return qap_improvement - swap_penalty
```

## Performance Results

| Benchmark | CNOT Reduction vs SOTA |
|-----------|----------------------|
| MQTBench (1,421 circuits) | 15.7% |
| AgentQ (204 circuits) | 30.4% |
| QUEKO (206 circuits) | 12.1% |

## Key Advantages
1. **Structure-aware**: Encodes problem coupling directly into attention
2. **Synthetic-to-real transfer**: Trained on random circuits, generalizes to real benchmarks
3. **Bidirectional refinement**: Forward-backward-forward captures global context
4. **Decay-weighted lookahead**: Balances immediate and long-term optimization
5. **Robust initialization**: Works with random initial mappings

## Application to Other Domains
This methodology generalizes beyond quantum:
- **Task scheduling**: Workers as locations, tasks as flows
- **Network routing**: Nodes as locations, traffic as flows
- **Facility layout**: Machines as locations, material flow as flows
- **VLSI placement**: Components as locations, wire connections as flows

## Related Papers
- arXiv:2605.12365 - QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment
- arXiv:2605.10768 - Unitaria: Quantum Linear Algebra via Block Encodings
