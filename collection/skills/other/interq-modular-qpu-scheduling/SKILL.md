---
name: interq-modular-qpu-scheduling
description: "Communication-aware scheduling for modular QPU architectures with heterogeneous communication models (superconducting, trapped-ion, neutral-atom). InterQ jointly considers qubit capacity, placement, parallel execution, and communication-driven dependencies, with adaptive circuit cutting. Based on arXiv:2605.17769. Use when: modular quantum computing, QPU scheduling, distributed quantum systems, circuit cutting optimization, quantum cloud architecture, hybrid classical-quantum communication."
---

# InterQ: Communication-Aware Modular QPU Scheduling

## Core Concept

Future quantum systems will move beyond monolithic processors to **modular architectures** connecting multiple QPUs via classical or quantum links. Different platforms realize modularity differently:
- **Superconducting**: Real-time classical links, dynamic-circuit coordination
- **Trapped-ion**: Photonic interconnects for remote entanglement
- **Neutral-atom**: Strong intra-core connectivity, proposed optical inter-core links

**InterQ** is a communication-aware scheduler that jointly optimizes qubit capacity, placement, parallel execution, and communication-driven dependencies across distributed subcircuits.

## Key Problem

In shared modular quantum cloud environments, naive scheduling ignores:
1. Communication model heterogeneity across QPU types
2. Synchronization constraints from measurement and feedforward
3. Entanglement distribution costs for quantum links
4. Trade-off between circuit cutting depth and communication overhead

## InterQ Scheduling Framework

### Step 1: Model the Architecture

```python
class ModularQPU:
    """Represents a modular quantum processing unit"""
    def __init__(self, qpu_type, n_qubits, comm_model):
        self.qpu_type = qpu_type  # 'superconducting', 'trapped-ion', 'neutral-atom'
        self.n_qubits = n_qubits
        self.comm_model = comm_model  # 'classical-link' or 'quantum-link'
```

### Step 2: Adaptive Circuit Cutting

InterQ uses **adaptive circuit cutting** to decompose large circuits into subcircuits that fit within individual QPUs:
- Analyze circuit connectivity graph
- Identify optimal cut points that minimize inter-QPU communication
- Balance fidelity loss from cutting vs communication overhead
- Different cutting strategies for classical vs quantum links

### Step 3: Communication-Aware Scheduling

```
For each circuit/subcircuit:
  1. Identify communication dependencies
  2. Classify as classical-link or quantum-link execution
  3. Schedule based on:
     - Qubit availability on target QPU
     - Communication latency (classical vs quantum)
     - Synchronization constraints
     - Fidelity requirements
```

### Step 4: Cross-Architecture Tradeoff Analysis

| Architecture | Strength | Weakness |
|---|---|---|
| Neutral-atom modular | **Highest fidelity** | Higher communication cost |
| Superconducting modular | **Minimum runtime** | Lower fidelity on deep circuits |
| Trapped-ion modular | **Balanced** (fidelity + speed) | Intermediate on both metrics |

## Implementation Pattern

```python
# InterQ scheduling loop
def schedule_circuit(circuit, qpu_pool, constraints):
    # 1. Analyze circuit structure
    graph = build_circuit_graph(circuit)
    
    # 2. Adaptive circuit cutting
    subcircuits = adaptive_cut(graph, qpu_pool.qubit_capacities)
    
    # 3. Map subcircuits to QPUs
    mapping = qpu_assign(subcircuits, qpu_pool)
    
    # 4. Communication-aware scheduling
    schedule = build_schedule(
        mapping,
        classical_links=qpu_pool.classical_links,
        quantum_links=qpu_pool.quantum_links,
        sync_constraints=extract_sync(subcircuits)
    )
    
    return optimize_schedule(schedule, constraints.objective)  # min makespan / max fidelity
```

## Pitfalls

1. **Over-cutting**: Too many circuit cuts exponentially reduce fidelity
2. **Communication bottleneck**: Quantum entanglement distribution is slow and noisy
3. **Synchronization deadlock**: Classical feedforward can create circular dependencies
4. **QPU heterogeneity**: Different QPUs have different native gate sets → translation overhead

## Best Practices

1. **Profile communication costs** before scheduling — measure actual latency per link type
2. **Prefer quantum links** for high-fidelity requirements, classical links for throughput
3. **Use neutral-atom** when fidelity matters most (e.g., variational algorithms)
4. **Use superconducting** for speed-critical workloads (e.g., sampling tasks)
5. **Monitor fidelity degradation** from cutting and adjust cut depth dynamically

## Activation

Keywords: modular QPU, quantum scheduling, circuit cutting, quantum cloud, communication-aware quantum, inter-QPU communication, superconducting QPU, trapped-ion interconnect, neutral-atom modular, distributed quantum computing, quantum architecture scheduling

## Related Skills

- `distributed-quantum-computing` - General distributed quantum computing patterns
- `quantum-compiler-routing` - Qubit routing within a single QPU
- `quantum-network-control` - Quantum network entanglement distribution
