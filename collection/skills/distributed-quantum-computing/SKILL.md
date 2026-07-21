---
name: distributed-quantum-computing
description: 'Distributed Quantum Computing architecture and patterns. Apply when designing multi-QPU systems, quantum communication protocols, or scaling quantum computing beyond single device limitations.'
metadata:
  {
    "openclaw":
      {
        "emoji": "⏛",
        "source": "arxiv:2212.10609,arxiv:2404.01265",
        "authors": ["Caleffi et al.", "Barral et al."],
        "year": 2024,
      },
  }
---

# Distributed Quantum Computing

Framework from arxiv:2212.10609 & arxiv:2404.01265 - scaling quantum computing via distributed paradigm.

## Core Problem

**Single QPU Limitation:**
- Current: ~100-1000 noisy qubits
- Need: ~10,000-1,000,000 noise-free qubits for practical quantum advantage
- Solution: **Distributed quantum computing** - multiple QPUs communicating and cooperating

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 Distributed Quantum Computing System         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│   │  QPU-1   │    │  QPU-2   │    │  QPU-3   │              │
│   │ 100 qubits│    │ 100 qubits│    │ 100 qubits│             │
│   └──────────┘    ┌──────────┘    └──────────┘              │
│        │              │              │                       │
│        └──────────────┼──────────────┘                       │
│                       │                                      │
│               ┌───────▼───────┐                              │
│               │ Quantum Network│                              │
│               │  (Entanglement │                              │
│               │   Distribution)│                              │
│               └───────┬───────┘                              │
│                       │                                      │
│               ┌───────▼───────┐                              │
│               │  Distributed  │                              │
│               │  Quantum Gates│                              │
│               └───────┬───────┘                              │
│                       │                                      │
│               ┌───────▼───────┐                              │
│               │   Scheduler   │                              │
│               │  (Task Distribution)│                         │
│               └───────┴───────┘                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Key Components

### 1. Quantum Communication Protocols

| Protocol | Purpose |
|----------|---------|
| **Teleportation** | Transfer quantum state between QPUs |
| **Entanglement swapping** | Create entanglement across non-directly connected QPUs |
| **Quantum routing** | Route qubits through quantum network |

### 2. Distributed Quantum Gates

- **Non-local gates:** Gates acting on qubits across different QPUs
- **CAT gates:** Communication-Assisted Teleportation gates
- **Telegate protocol:** Teleport gate execution to remote QPU

### 3. Scheduler

- Task decomposition across QPUs
- Minimize communication overhead
- Balance QPU workload

## Challenges

| Challenge | Description | Current Solutions |
|-----------|-------------|-------------------|
| **Entanglement distribution** | Create/maintain entanglement across QPUs | Quantum repeaters, entanglement swapping |
| **Noise propagation** | Errors spread across distributed system | Distributed error correction |
| **Communication overhead** | Teleportation requires classical communication | Minimize non-local gates |
| **Synchronization** | QPUs must be synchronized | Distributed quantum clock |
| **Scalability** | Network topology limits scaling | Hierarchical architecture |

## Design Patterns

### Pattern 1: Quantum Circuit Partitioning

```python
def partition_circuit(circuit, n_qpus):
    """Partition quantum circuit across multiple QPUs."""
    partitions = []
    for i in range(n_qpus):
        partition = extract_local_gates(circuit, qpu_range=i)
        non_local_gates = extract_non_local_gates(circuit, qpu_range=i)
        partitions.append({
            'local': partition,
            'non_local': non_local_gates,
            'communication': estimate_teleportation_cost(non_local_gates)
        })
    return optimize_partition(partitions)
```

**Optimal Gate-Packing (arXiv:2606.18494):** The primary cost metric for multi-QPU partitioning is **e-bit count** (maximally entangled qubit pairs between QPUs). 
1. Build interaction graph from two-qubit gates (nodes=qubits, edges=gates)
2. Apply gate-packing: group commuting gates before partitioning to reduce cross-QPU edges
3. Use graph partitioning (METIS, spectral, ILP) to assign qubits to QPUs
4. Rewrite cross-QPU gates via teleportation, preserving unitary equivalence
5. Validate with unitary matrix comparison and hardware execution

**Pitfall**: Always optimize the circuit *before* partitioning. Partitioning an unoptimized circuit wastes e-bits on gates that could be eliminated. For QFT circuits, exploit the hierarchical structure of controlled-phase gates to reduce e-bit cost beyond generic partitioning.

### Pattern 2: Entanglement Distribution Network

```
QPUs connected via quantum network:
- Direct links: High-fidelity entanglement
- Indirect links: Entanglement swapping via repeaters
- Topology: Minimize shortest path between any two QPUs
```

### Federated Quantum Learning
- See `q-anchor-federated-quantum-learning` skill for QFL with ZNE-guided correction addressing double-drift (client drift + hardware bias)

### Key Pattern: Distributed Quantum Error Correction

- Surface code adapted for distributed QPUs
- Parity checks across QPU boundaries
- Requires entangled ancilla qubits

## Metrics

| Metric | Target |
|--------|--------|
| Entanglement fidelity | > 0.99 for distributed gates |
| Communication latency | < 1ms for teleportation |
| QPU utilization | > 80% parallel execution |
| Error rate | < 0.001 per distributed operation |

## Applications

- **Distributed Shor's algorithm:** Factor large numbers across QPUs
- **Distributed QAOA:** Optimize large-scale optimization problems
  - DQAOA simulator (arxiv:2606.26297): Qiskit-compatible simulator for multi-QPU QUBO. Canonicalizes QUBO → cost Hamiltonian → variable allocation → circuit construction. Runtime optimizations: circuit reuse, batched eval, parallel multi-start. Power unit commitment case: distributed recovers same optimal as monolithic. Cross-QPU couplings require remote operations → more demanding. See `distributed-qaoa-simulator` skill.
- **Quantum simulation:** Simulate larger quantum systems
- **Quantum machine learning:** Train larger quantum models

## Relation to OpenClaw

OpenClaw's distributed agent architecture parallels DQC:

- Multiple QPUs → Multiple agent instances
- Quantum communication → Agent communication protocols
- Distributed gates → Cross-agent tool calls
- Scheduler → Agent orchestrator

---

*Sources: arxiv:2212.10609 (Caleffi et al., 2024), arxiv:2404.01265 (Barral et al., 2024)*