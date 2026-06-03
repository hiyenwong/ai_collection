---
name: grover-cvrptw-quantum
description: "Quantum algorithm for Capacitated Vehicle Routing Problem with Time Windows (CVRPTW) using Grover Search with qubit-efficient split-inspired modeling. Use when solving logistics optimization with quantum computing, vehicle routing, delivery optimization, or quantum combinatorial optimization with constraints."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.18393"
  published: "2026-05-18"
  tags: [quantum, optimization, vehicle-routing, grover, logistics, combinatorial]
---

# Grover-Based Quantum CVRPTW Solver

## Source
- arXiv: 2605.18393 (May 18, 2026)

## Core Problem
CVRPTW is NP-hard; classical route-first-cluster-second decompositions introduce suboptimality. Full quantum formulations need O(N^2) qubits — infeasible on NISQ devices.

## Key Innovation
Qubit-efficient split-inspired modeling:
- Inspired by classical route-first, cluster-second technique
- Overcomes suboptimality of classical decomposition via quantum search
- Adds only **linear** number of decision qubits vs standard TSP formulations

## Methodology

### 1. Split-Inspired Decomposition
- Phase 1: Giant tour construction (TSP-like ordering)
- Phase 2: Optimal split into feasible routes respecting capacity + time windows
- Quantum formulation searches over split points

### 2. Grover Search Framework
- Encodes feasible splits as marked states
- Oracle checks: capacity constraints + time window feasibility
- Quadratic speedup over classical enumeration of splits

### 3. Qubit-Efficient Encoding
- Standard TSP needs O(N^2) qubits for position encoding
- Split model needs O(N) decision qubits for split points only
- Linear scaling enables larger problem instances on near-term hardware

### 4. Constraint Handling
- Capacity: sum of demands per route <= vehicle capacity
- Time windows: arrival at each node within [a_i, b_i]
- Oracle rejects infeasible splits

## Systems Engineering Patterns
1. **Decomposition + Quantum Search**: classical decomposition + quantum refinement
2. **Qubit-Efficient Encoding**: minimize qubit count via problem structure exploitation
3. **Constraint-Oracle Design**: embed feasibility checks into quantum oracle

## Activation
- Keywords: quantum vehicle routing, CVRPTW, grover optimization, logistics quantum, delivery optimization, quantum combinatorial optimization
- Use when: solving vehicle routing with quantum computing, designing qubit-efficient formulations, postal/delivery route optimization

## Pitfalls
- Oracle complexity depends on constraint density
- Time window constraints increase oracle depth significantly
- Not viable on current NISQ hardware for realistic instance sizes
- Split decomposition assumes triangular inequality for cost matrix
