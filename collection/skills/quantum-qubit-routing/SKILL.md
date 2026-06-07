---
name: quantum-qubit-routing
description: >
  Qubit mapping and routing methodology for quantum compilation.
  Uses position graph abstraction and memoized heuristic evaluation to scale
  SABRE-based routing on TI-QCCD and other heterogeneous quantum architectures.
  Covers position graph abstraction, relative move scoring, memoized congestion resolution,
  and architecture-aware compilation. Use when: designing quantum compilers, implementing
  qubit routing/mapping, optimizing TI-QCCD shuttling, scaling SABRE algorithms,
  or building architecture-aware quantum compilation frameworks.
  Activation: qubit routing, qubit mapping, quantum compiler, SABRE, position graph,
  TI-QCCD, 量子比特路由, 量子编译
---

# Qubit Mapping and Routing with Position Graph Abstraction

## Core Problem

Scalable qubit mapping and routing are major bottlenecks in quantum compilation,
especially for Trapped-Ion Quantum Charge-Coupled device (TI-QCCD) architectures
where qubit interactions require physically shuttling ions under strict movement,
congestion, and trap-capacity constraints.

## Position Graph Abstraction

A unified representation of executable locations, movement paths, and routing
constraints that enables heuristic mappers to operate directly on
shuttling-based hardware.

### Graph Construction

1. **Nodes**: Executable trap locations (interaction zones, storage zones)
2. **Edges**: Valid movement paths between locations
3. **Weights**: Movement cost (distance, time, congestion)
4. **Constraints**: Trap capacity, exclusion zones, connectivity limits

### Key Operations

```python
class PositionGraph:
    def __init__(self, architecture_spec):
        # Build graph from hardware topology
        self.nodes = self._parse_locations(architecture_spec)
        self.edges = self._parse_connections(architecture_spec)
        self.constraints = self._parse_constraints(architecture_spec)

    def find_path(self, source, target, constraints):
        """Find valid movement path respecting all hardware constraints."""
        # Use A* or Dijkstra with constraint-aware cost function
        return self._shortest_path(source, target, constraints)

    def check_feasibility(self, qubit_assignment, gates):
        """Check if gate sequence is executable under current mapping."""
        return all(self._can_execute(g, qubit_assignment) for g in gates)
```

## Memoized SABRE Optimization

Two key memoization techniques to accelerate SABRE-based routing:

### 1. Relative Move Scoring

Caches repeated heuristic move evaluations that arise during search.
Many gate ordering decisions produce identical relative position changes,
making memoization highly effective.

```python
class MemoizedSABRE:
    def __init__(self, position_graph):
        self.graph = position_graph
        self.move_cache = {}  # (gate, layout) -> score

    def score_move(self, gate, current_layout):
        key = self._canonical_key(gate, current_layout)
        if key in self.move_cache:
            return self.move_cache[key]
        score = self._compute_heuristic(gate, current_layout)
        self.move_cache[key] = score
        return score
```

### 2. Memoized Congestion Resolution

Speeds up resolution of repeated congestion patterns by caching
previous successful resolutions and their outcomes.

```python
    def resolve_congestion(self, blocked_paths, current_layout):
        key = self._congestion_key(blocked_paths, current_layout)
        if key in self.congestion_cache:
            return self.congestion_cache[key]
        resolution = self._solve_congestion(blocked_paths, current_layout)
        self.congestion_cache[key] = resolution
        return resolution
```

## Architecture-Aware Compilation Pipeline

```
Circuit → Gate Decomposition → Position Graph Construction
    → SABRE with Memoization → Routing Plan → Hardware-Specific Scheduling
    → Pulse-Level Instructions
```

### Pipeline Stages

1. **Gate decomposition**: Convert high-level gates to native gate set
2. **Position graph**: Build hardware topology graph from device spec
3. **Mapping**: Assign logical qubits to physical trap locations
4. **Routing**: Insert SWAP/shuttle operations for non-adjacent interactions
5. **Scheduling**: Order operations respecting timing and capacity constraints
6. **Pulse generation**: Convert to hardware-specific pulse sequences

## TI-QCCD Specific Considerations

- **Movement constraints**: Ion shuttling requires voltage waveform sequences
- **Congestion**: Multiple ions cannot occupy same trap zone simultaneously
- **Trap capacity**: Each trap zone has maximum ion count limits
- **Crosstalk**: Adjacent operations may interfere; schedule accordingly
- **Reordering**: Ion chain reordering requires split-merge operations

## Generalization to Other Architectures

The position graph abstraction generalizes beyond TI-QCCD:

- **Superconducting**: Nodes = qubits, edges = couplers
- **Photonic**: Nodes = optical components, edges = waveguide paths
- **Neutral atoms**: Nodes = trap sites, edges = rearrangement paths
- **Ion trap (linear)**: Nodes = ion positions, edges = SWAP operations

## Pitfalls

- **Graph size explosion**: Large architectures create huge position graphs;
  use hierarchical abstraction to manage complexity
- **Cache invalidation**: Memoization assumes deterministic hardware;
  recalibrate when device parameters change
- **Over-caching**: Too many cache entries consume memory; use LRU eviction
- **Constraint coupling**: Movement and capacity constraints are interdependent;
  solve jointly, not sequentially
- **Heuristic drift**: Hardware drift changes optimal routing; periodic
  recalibration required

## Verification

1. Verify all gates in routed circuit are executable under final mapping
2. Check no constraint violations (capacity, movement, timing)
3. Compare gate count and depth against baseline (no routing)
4. Validate on simulator before hardware execution
