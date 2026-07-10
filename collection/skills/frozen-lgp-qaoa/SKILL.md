---
name: frozen-lgp-qaoa
description: "FrozenLGP adaptive decomposition framework for divide-and-conquer QAOA. Transforms partitionability from an assumption into an enforceable property by freezing obstructing vertices and folding their energy into linear bias terms. Enables 100% decomposition coverage on graphs up to 10,000 vertices including dense/high-connectivity instances. Activation: FrozenLGP, divide-and-conquer QAOA, qubit freezing, graph partitioning QAOA, adaptive decomposition, max-flow vertex cut, dense graph QAOA"
metadata:
  arxiv_id: "2607.08138"
  published: "2026-07-09"
  authors: "Sokea Sang, Leanghok Hour, Dongmin Kim, Youngsun Han"
  tags: [quantum, qaoa, optimization, graph-partitioning, divide-and-conquer]
---

# FrozenLGP: Adaptive Qubit Freezing for Divide-and-Conquer QAOA

## Description

Adaptive decomposition framework that makes any graph partitionable for divide-and-conquer QAOA. When standard partitioning fails (no small vertex separator exists), FrozenLGP identifies minimum obstructing vertices via max-flow min-cut, classically freezes their spin assignments, and folds removed interaction energies into linear bias terms of neighboring active qubits.

## Activation Keywords

- FrozenLGP
- divide-and-conquer QAOA
- qubit freezing
- graph partitioning QAOA
- adaptive decomposition
- max-flow vertex cut
- dense graph QAOA
- QAOA scalability

## Core Concepts

### The Partitionability Problem

Standard divide-and-conquer QAOA requires small vertex separators — it fails entirely on dense or highly connected graphs where no such decomposition exists (only ~4.6% coverage on high-connectivity instances).

### FrozenLGP Solution

1. **Detect failure**: Standard graph partitioning fails → no small vertex separator
2. **Find minimum vertex cut**: Max-flow min-cut computation identifies the smallest set of vertices preventing partition
3. **Freeze obstructing vertices**: Classically assign spin values to these vertices
4. **Fold energy**: Removed interaction energies become linear bias terms in the Ising Hamiltonian of neighboring active qubits
5. **Solve subproblems**: Each partition now fits on available qubits
6. **Combine solutions**: Frozen values + subproblem solutions = full solution

### Energy Preservation

The key mathematical insight: when a vertex v with spin s_v is removed, all terms involving v in the Ising Hamiltonian H = Σᵢⱼ Jᵢⱼzᵢzⱼ + Σᵢ hᵢzᵢ become:
- Quadratic terms Jᵥᵢ·sᵥ·zᵢ → absorbed into linear bias hᵢ' = hᵢ + Jᵥᵢ·sᵥ
- The energy contribution is rigorously preserved, not approximated

### Performance

- **100% decomposition coverage** vs 4.6% for standard approach on high-connectivity graphs
- Tested on graphs up to 10,000 vertices across multiple topology families
- Preserves approximation quality on already-solvable instances
- Noise simulations show improved robustness from reduced entangling-gate requirements

## Usage Patterns

### Pattern 1: Pre-processing Pipeline

```
Input graph → Try standard partitioning
  ├─ Success → Use standard D&C QAOA
  └─ Fail → Run FrozenLGP:
       1. Compute min vertex cut (max-flow)
       2. Classically freeze cut vertices
       3. Fold energies into neighbor biases
       4. Partition remaining graph
       5. Solve each subproblem with QAOA
       6. Combine with frozen values
```

### Pattern 2: Vertex Cut Selection

- Use max-flow min-cut algorithm (Edmonds-Karp, Dinic's, or push-relabel)
- Trade-off: fewer frozen vertices → more quantum resources needed per subproblem
- Trade-off: more frozen vertices → smaller subproblems but more classical approximation

### Pattern 3: Noise-Robust Operation

FrozenLGP reduces entangling gate requirements (fewer qubits per subproblem) → inherently more robust to noise on NISQ devices.

## Pitfalls

- **Frozen value selection matters**: Poor classical assignments of frozen spins degrade overall solution quality. Consider trying multiple assignments and picking the best.
- **Not a quantum advantage proof**: The freezing step is classical — the quantum part only solves smaller subproblems. Overall speedup depends on subproblem solving efficiency.
- **Dense graphs still hard**: While FrozenLGP achieves 100% coverage, the number of frozen vertices may be large for very dense graphs, requiring many classical sub-routines.
- **Approximation quality**: Guaranteed to match standard D&C quality on solvable instances, but optimal frozen value selection for unsolved instances is heuristic.

## Related Skills

- `quantum-optimization-qaoa` (QAOA methodology)
- `quantum-annealing-xai` (annealing-based optimization)
- `quantum-inspired-optimization` (quantum-inspired classical optimization)
- `quantum-hypergraph-partitioning` (quantum hypergraph partitioning)
