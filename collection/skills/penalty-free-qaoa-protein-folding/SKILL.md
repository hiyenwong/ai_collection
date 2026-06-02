---
name: penalty-free-qaoa-protein-folding
description: "Penalty-free QAOA methodology for lattice protein folding using conflict graph independent set formulation. Use when: (1) quantum optimization for protein folding or molecular structure prediction, (2) QAOA without penalty terms, (3) conflict graph maximum independent set (MIS) mixer design, (4) quantum annealing approaches to biological optimization problems. Activation: penalty-free QAOA, protein folding, lattice protein, conflict graph, independent set mixer, QAOA bio-physics, quantum protein, molecular optimization, lattice model folding"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.02104"
  published: "2026-06-01"
  authors: "Leif Gellsersen, Anders Irbäck, Lucas Knuthson, Stefan Prestel"
  tags: [quantum, protein-folding, QAOA, optimization, bio-physics]
---

## Problem Statement

Lattice protein folding is a discrete optimization problem: find minimum-energy configurations of self-avoiding polymer chains on a lattice. Quantum approaches (QAOA, quantum annealing) require mapping to binary variables, typically using quadratic penalty terms to enforce chain connectivity constraints — which bloat qubit counts and degrade circuit performance.

## Core Methodology

### Conflict Graph Formulation

Instead of penalty terms, map the problem to **maximum independent set (MIS)** on a conflict graph:

1. **Nodes**: Each node represents a valid aminoacid-position assignment
2. **Edges**: Connect nodes that cannot simultaneously be true (steric clashes, chain breaks)
3. **Search space**: Restrict to independent sets — automatically satisfies all geometric constraints
4. **Objective**: Pure protein energy + linear bias (NO quadratic penalties)

### QAOA Mixer Design

Use the **MIS-preserving mixer** (Hen et al.) instead of the standard transverse-field mixer:

- Standard X-mixer explores full 2^n space (most states invalid)
- MIS mixer preserves the independent-set constraint throughout evolution
- Guarantees feasibility at every intermediate state

### Iterative Local Search

For large proteins (n > 25):

1. Decompose conflict graph into subgraphs (≤ 26 qubits)
2. Iteratively optimize subproblems
3. Converges to local minima with provable constraint satisfaction

## Key Results

- Validated via classical circuit simulation for proteins of lengths 15 and 18
- Heuristic scheme folds proteins up to length 60 with ≤ 26 qubits
- Objective function = protein energy + linear bias only (no penalties)

## Reusable Patterns

### Pattern 1: Constraint-Graph QAOA

When a discrete optimization problem has hard constraints:
1. Build a conflict graph where edges encode mutual exclusions
2. Use MIS-preserving mixer instead of penalty terms
3. Objective = problem energy only (linear + problem-specific)

**Applies to**: Scheduling, routing, portfolio selection, protein folding, molecular docking

### Pattern 2: Iterative Subgraph Decomposition

For problems exceeding available qubits:
1. Partition conflict graph into manageable subgraphs
2. Solve each subproblem with full QAOA circuit
3. Iterate until convergence

**Benefit**: Scales QAOA beyond native qubit limits

## Pitfalls

- **MIS mixer complexity**: The MIS-preserving mixer requires deeper circuits than transverse-field mixer — factor into coherence time budget
- **Conflict graph size**: For 2D lattice proteins, graph has O(n²) nodes — scales quadratically with chain length
- **No guarantee of global optimum**: Iterative local search finds local minima; use multiple random restarts
- **Classical simulation only**: This paper validates via classical simulation; hardware results pending

## References

- arXiv:2606.02104v1 — Penalty-free quantum optimization applied to lattice protein folding
- Related: q-bio.BM (biomolecules), physics.bio-ph (biological physics), physics.comp-ph (computational physics)
