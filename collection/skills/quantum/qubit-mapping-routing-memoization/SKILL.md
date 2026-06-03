---
name: qubit-mapping-routing-memoization
description: "Scalable qubit mapping and routing using position graph abstraction and memoization for quantum compilation. Addresses TI-QCCD (Trapped-Ion Quantum Charge-Coupled Device) architectures and other systems requiring physical qubit movement. Use when: compiling quantum circuits for trapped-ion systems, optimizing qubit placement and routing, implementing position graph abstraction for quantum compilation, reducing compilation time through memoization patterns."
---

# Qubit Mapping and Routing with Position Graph Abstraction

## Core Problem

Qubit mapping and routing are major bottlenecks in quantum compilation, especially for:
- **TI-QCCD architectures**: Qubit interactions require physical ion shuttling
- **Movement constraints**: Strict limits on ion movement speed and paths
- **Congestion**: Multiple qubits competing for limited trap capacity
- **Trap capacity**: Physical limits on ions per trap zone

## Position Graph Abstraction (arXiv:2605.09237)

### Unified Representation
The position graph unifies three compilation concerns:
1. **Executable locations**: Where qubits can be placed
2. **Movement paths**: How qubits can travel between locations
3. **Routing constraints**: Capacity limits and movement rules

### Benefits
- Heuristic mappers operate on abstract graph instead of physical layout
- Enables memoization of routing decisions across compilation runs
- Reduces compilation time from exponential to near-linear for many circuits

## Compilation Framework

### Step 1: Build Position Graph
```python
# Position graph representation
position_graph = {
    'nodes': trap_zones,          # Executable locations
    'edges': movement_paths,      # Connectivity
    'capacity': zone_limits,      # Max ions per zone
    'constraints': movement_rules  # Speed, ordering limits
}
```

### Step 2: Graph-Based Mapping
1. Map logical qubits to position graph nodes
2. Identify required two-qubit interactions
3. Route qubits along edges to enable interactions
4. Track capacity constraints during routing

### Step 3: Memoization
Cache routing decisions for reuse:
```
key = (circuit_subgraph, position_subgraph)
value = optimal_mapping_and_routing
```
- Memoize at circuit-block level for composability
- Reuse across similar circuit structures
- Cache invalidation when hardware topology changes

### Step 4: SWAP Optimization
Minimize SWAP gate overhead:
- Prioritize interactions that don't require movement
- Batch movements for multiple qubits
- Use memoized solutions for common patterns

## Architecture-Specific Patterns

### TI-QCCD (Trapped-Ion)
- Ions shuttle between trap zones
- Movement is sequential (one at a time typically)
- Capacity: 10-100 ions per zone
- Key constraint: movement time dominates gate time

### Superconducting (for comparison)
- Fixed qubit positions, SWAP gates required
- Position graph maps to physical connectivity
- No movement, only gate-level routing

## Key Metrics
- **Compilation time**: Wall-clock time to map+route
- **SWAP overhead**: Additional gates from routing
- **Movement count**: Physical operations for TI-QCCD
- **Memoization hit rate**: % of routing decisions from cache

## Pitfalls
- Memoization cache grows with circuit diversity — implement LRU eviction
- Position graph must be rebuilt when hardware topology changes
- Congestion can cause deadlock — implement backtracking or randomized tie-breaking
- TI-QCCD movement scheduling is NP-hard in general — use greedy heuristics with memoization

## Related
- `quantum-compiler-routing`: General qubit routing methodology
- `quantum-compilation-workflow`: Multi-objective quantum compilation
- `distributed-quantum-computing`: Distributed quantum architectures
