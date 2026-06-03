---
name: quantum-compiler-routing
description: "Quantum compiler qubit mapping and routing methodology for scalable quantum circuit compilation. Covers position graph abstraction, heuristic mapper optimization (SABRE), memoized congestion resolution, and architecture-aware compilation for heterogeneous quantum hardware including TI-QCCD (Trapped-Ion Quantum Charge-Coupled Device) systems. Use when: implementing quantum compilers, designing qubit mapping and routing algorithms, optimizing quantum circuit compilation for specific hardware architectures, analyzing compilation scalability bottlenecks, or working with shuttling-based trapped-ion or superconducting quantum architectures. Activation: quantum compiler, qubit mapping, qubit routing, SABRE algorithm, quantum circuit compilation, TI-QCCD, trapped-ion compilation, position graph abstraction, quantum shuttling, compiler scalability, memoized heuristic evaluation."
---

# Quantum Compiler Qubit Mapping & Routing

Methodology for scalable qubit mapping and routing in quantum circuit compilation, based on position graph abstraction and memoized heuristic evaluation.

## Core Problem

Quantum circuit compilation requires mapping logical qubits to physical qubits and routing interactions under hardware connectivity constraints. For shuttling-based architectures (TI-QCCD), additional constraints include:
- Physical ion movement requirements
- Trap capacity limits
- Congestion resolution during multi-qubit operations

## Position Graph Abstraction

The **position graph** unifies three critical representations:

1. **Executable locations**: Where qubits can physically reside
2. **Movement paths**: Valid routes for qubit shuttling/swap operations
3. **Routing constraints**: Hardware-specific limitations (trap capacity, movement rules)

This abstraction enables heuristic mappers to operate directly on hardware-specific constraints without architecture-specific code changes.

## Optimizing SABRE-Based Compilation

### Relative Move Scoring (Memoization)

The SABRE (SWAP-based BidiREctional heuristic search) algorithm repeatedly evaluates the same heuristic moves during search. Cache these evaluations:

```python
move_cache = {}

def evaluate_move(state, swap):
    key = hash((state, swap))
    if key in move_cache:
        return move_cache[key]
    result = heuristic_compute(state, swap)
    move_cache[key] = result
    return result
```

This removes redundant computation **without changing routing decisions** — purely an acceleration.

### Memoized Congestion Resolution

Congestion resolution is the most expensive part of SABRE for large circuits:

```python
congestion_cache = {}

def resolve_congestion(state, blocked_qubits):
    key = hash((tuple(sorted(blocked_qubits)), state.occupancy_map))
    if key in congestion_cache:
        return congestion_cache[key]
    result = resolve_blocking(state, blocked_qubits)
    congestion_cache[key] = result
    return result
```

## Architecture-Aware Compilation Workflow

### Step 1: Hardware Characterization

Map hardware constraints to position graph:
- Define physical qubit/trap locations as graph nodes
- Define valid movement paths as graph edges
- Annotate with capacity, latency, and fidelity constraints

### Step 2: Circuit Analysis

- Build interaction graph from quantum circuit (nodes = logical qubits, edges = 2-qubit gates)
- Identify gate dependencies and parallelization opportunities
- Classify gates as native vs. requiring routing

### Step 3: Mapping + Routing

1. **Initial mapping**: Assign logical qubits to physical positions minimizing early gate distances
2. **Iterative scheduling**: For each gate:
   - If qubits are adjacent → execute
   - If not → use position graph to find shortest path
   - Apply memoized SABRE to find optimal swap/insert sequence
3. **Congestion resolution**: Use cached solutions for repeated blocking patterns

### Step 4: Optimization

- **Gate cancellation**: Remove adjacent inverse gates
- **Gate commutation**: Reorder independent gates for better parallelism
- **Depth minimization**: Parallelize independent operations

## Scalability Analysis

Key metrics to track:
- **Compilation time**: Wall-clock time for full circuit compilation
- **Circuit depth overhead**: Ratio of compiled depth to ideal depth
- **SWAP count**: Number of additional SWAP/insert operations
- **Fidelity estimate**: Product of gate fidelities along execution path
- **Memory usage**: Cache hit rate for memoized evaluations

## Pitfalls

- **Cache key collisions**: Ensure memoization keys uniquely capture state. Incorrect hashing leads to wrong routing decisions.
- **Architecture mismatch**: Position graph must accurately reflect hardware. Incomplete constraint modeling produces invalid schedules.
- **Over-optimization**: Memoization saves computation but increases memory. For very large circuits, consider bounded cache with LRU eviction.
- **Ignoring parallel gates**: Greedy sequential scheduling misses parallelization. Use dependency graph to identify concurrent operations.
- **Trapped-ion specifics**: TI-QCCD has unique constraints (trap capacity, shuttling time) not present in fixed-coupling architectures. Always model these explicitly.

## Related Methods

- **Qiskit transpiler**: IBM's default compiler (uses SABRE routing)
- **t|ket>**: Cambridge Quantum's compiler (architecture-aware)
- **Pytket extensions**: Custom routing passes
- **Classical routing**: SAT-based and ILP-based approaches (optimal but slow)
