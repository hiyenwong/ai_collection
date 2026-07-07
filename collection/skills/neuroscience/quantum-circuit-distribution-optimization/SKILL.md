---
name: quantum-circuit-distribution-optimization
description: "Joint qubit leasing and quantum circuit distribution optimization methodology. ILP formulation for multi-QC quantum network resource allocation, NP-completeness analysis, greedy algorithm with local search. Covers qubit allocation, gate execution placement, and inter-QC communication tradeoffs (migration vs teleportation). Activation: quantum circuit distribution, qubit leasing, quantum network optimization, JQLQCD, quantum resource allocation, distributed quantum computing."
arxiv_id: "2606.00501"
---

## Quantum Circuit Distribution Optimization (JQLQCD)

Methodology from arXiv:2606.00501 (May 2026). Joint Qubit Leasing and Quantum Circuit Distribution (JQLQCD) problem framework for optimizing quantum computation across networked quantum computers.

## Problem Formulation

Given a quantum circuit to execute across N quantum computers (QCs) connected by a quantum network, optimize four coupled decisions:

1. **Qubit Leasing**: How many qubits to lease from each QC
2. **Qubit Storage**: Where to store circuit qubits at each time slot
3. **Gate Execution**: Which QC executes each gate
4. **Qubit Movement**: How to move qubits between QCs (migration vs teleportation)

### Key Insight

These four decisions are **interdependent** — optimizing each independently leads to suboptimal solutions. The JQLQCD formulation captures the full coupling.

## ILP Formulation

### Decision Variables
- `x[q, t, c]`: qubit q stored at QC c at time t
- `y[g, c]`: gate g executed at QC c
- `l[c]`: number of qubits leased from QC c
- `m[q, t, c1, c2]`: qubit q migrated from c1 to c2 at time t
- `tele[q, t, c1, c2]`: qubit q teleported from c1 to c2 at time t

### Objective
Minimize total cost = leasing costs + communication costs (migration + teleportation)

### Constraints
1. **Storage**: Each qubit stored at exactly one location per time step
2. **Gate Proximity**: Qubits needed by a gate must be co-located at execution QC
3. **Capacity**: Leased qubits ≤ QC physical capacity
4. **Conservation**: Qubit movement preserves quantum state
5. **Temporal**: Gate ordering respects circuit dependencies

## Complexity Results

**NP-completeness**: JQLQCD is NP-complete (reduction from graph partitioning).

**Tractable special cases**:
1. **Single-QC**: Trivial — all gates execute locally
2. **Star topology with uniform costs**: Polynomial-time optimal solution
3. **Tree topology with linear costs**: Dynamic programming solution
4. **Fixed gate placement**: Reduces to min-cost flow (polynomial)

## Greedy Algorithm with Local Search

For general large instances:

### Phase 1: Greedy Initialization
1. Assign each gate to the QC with lowest leasing cost that has capacity
2. For each qubit, assign storage to minimize total movement
3. Choose migration vs teleportation based on cost comparison

### Phase 2: Local Search Refinement
1. **Gate Swap**: Try reassigning gates to different QCs
2. **Storage Redistribute**: Rebalance qubit storage across QCs
3. **Communication Optimize**: Switch migration ↔ teleportation where beneficial
4. Accept moves that reduce total cost

### Performance
- Near-optimal on small instances (within 5-15% of ILP optimum)
- Scales to circuits with 100+ qubits across 10+ QCs
- Runtime polynomial in circuit size × number of QCs

## Tradeoff: Migration vs Teleportation

| Aspect | Migration | Teleportation |
|--------|-----------|---------------|
| Cost | Linear in distance | Constant (entanglement pre-shared) |
| Fidelity | Preserved during transfer | Requires entanglement + classical comm |
| Latency | O(distance × transfer rate) | O(classical comm latency) |
| Resource | No entanglement needed | Consumes entanglement pairs |
| Best for | Nearby QCs, low bandwidth needs | Distant QCs, high-fidelity needs |

**Decision rule**: Use migration when `cost_migration < cost_teleportation`, i.e., when QCs are physically close and entanglement is expensive to maintain.

## Practical Applications

1. **Quantum Cloud Computing**: Users lease qubits from multiple quantum cloud providers
2. **Distributed Quantum Computing**: Multi-core quantum processors with interconnects
3. **Quantum Network Optimization**: Routing quantum computations across a quantum internet
4. **Hybrid Quantum-Classical Workflows**: Deciding which parts of a circuit run on which hardware

## Design Patterns

### Pattern 1: Cost-Aware Gate Placement
```
For each gate g:
  candidates = QCs with capacity for all g's qubits
  For each QC in candidates:
    cost = lease_cost + movement_cost(qubits_to_QC) + gate_cost(QC, g)
  Assign g to QC with minimum cost
```

### Pattern 2: Communication Mode Selection
```
For each qubit transfer (q, c1, c2):
  if distance(c1, c2) < threshold AND bandwidth(c1, c2) > min_bw:
    use migration
  else if entanglement_available(c1, c2):
    use teleportation
  else:
    establish entanglement + use teleportation
```

### Pattern 3: Temporal Qubit Scheduling
```
For each time step t in circuit:
  active_qubits = qubits needed by gates at t
  For each qubit q in active_qubits:
    target_QC = QC executing next gate on q
    if q.storage != target_QC:
      plan movement (migration or teleportation)
```

## Pitfalls

1. **Independent optimization is suboptimal**: Optimizing leasing, placement, and communication separately ignores their coupling
2. **Teleportation has hidden costs**: Entanglement generation and maintenance are expensive and not captured in simple models
3. **Gate fidelity varies by QC**: Different QCs have different error rates — incorporate into cost model
4. **Temporal dependencies**: Qubit movement takes time — must respect circuit timing constraints
5. **NP-hardness means heuristics are necessary**: For real-world instances (>50 qubits, >5 QCs), exact ILP is intractable

## Related Skills

- [[distributed-quantum-computing]] — DQC architecture and patterns
- [[quantum-qubit-routing]] — Qubit mapping and routing methodology
- [[asynchronous-quantum-distributed-computing]] — Asynchronous DQC patterns
- [[distributed-quantum-routing]] — Routing for distributed quantum networks
- [[quantum-network-control]] — Entanglement distribution optimization