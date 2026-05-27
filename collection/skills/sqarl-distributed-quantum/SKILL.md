---
name: sqarl-distributed-quantum
description: "Size-Agnostic Reinforcement Learning (SQARL) methodology for circuit allocation in distributed quantum computing networks. Use when: allocating quantum circuits across heterogeneous quantum processors, optimizing distributed quantum computing resource allocation, designing quantum network schedulers, mapping quantum circuits to multi-processor systems, RL-based quantum resource management. Activation: SQARL, distributed quantum computing, circuit allocation, quantum resource scheduling, quantum network optimization, RL quantum scheduling, size-agnostic quantum allocation."
---

# SQARL: Distributed Quantum Circuit Allocation

## Description
Reinforcement Learning methodology for efficient circuit allocation in distributed quantum computing networks. Enables size-agnostic mapping of quantum circuits across heterogeneous quantum processors.

Source: arXiv:2605.27027v1 - "SQARL: A Size-Agnostic Reinforcement Learning approach for Circuit Allocation in Distributed Quantum Computing Networks"

## Core Methodology

### 1. Size-Agnostic Representation
- Encode quantum circuits in a hardware-independent format
- Use graph-based representations that generalize across circuit sizes
- Abstract qubit connectivity and gate operations into allocation-friendly features

### 2. RL-Based Allocation Policy
- State: Available quantum processors (qubit counts, connectivity, error rates, availability)
- Action: Circuit-to-processor mapping and routing decisions
- Reward: Execution fidelity, latency minimization, resource utilization efficiency
- Policy: Neural network that generalizes across different circuit and hardware sizes

### 3. Heterogeneous Hardware Support
- Model processor heterogeneity: different qubit counts, topologies, gate sets, noise profiles
- Support dynamic hardware availability and time-varying resource constraints
- Enable allocation across hybrid classical-quantum infrastructure

### 4. Distributed Network Optimization
- Optimize for inter-processor communication overhead
- Minimize qubit teleportation and SWAP gate requirements
- Balance load across the quantum computing network

## Application Steps

1. **Characterize hardware**: Build profiles for each quantum processor (qubits, topology, fidelity)
2. **Encode circuit**: Convert quantum circuit to size-agnostic graph representation
3. **Query RL policy**: Get allocation decision for circuit-to-processor mapping
4. **Execute allocation**: Deploy circuit segments to assigned processors
5. **Monitor and update**: Track execution metrics and update RL policy

## Key Design Patterns

### Pattern 1: Graph-Based Circuit Encoding
```
Quantum Circuit → Dependency Graph → Feature Vector → RL Policy
```

### Pattern 2: Multi-Objective Optimization
```
Maximize: Fidelity × Throughput × Utilization
Minimize: Latency × Communication Overhead × SWAP Count
```

### Pattern 3: Dynamic Rescheduling
```
Hardware State Change → Re-evaluate Allocation → Optimal Remapping
```

## Integration with Other Systems

- **QKD Networks**: Combine with MBSE-designed quantum network architectures (qkd-network-mbse)
- **Entanglement Distillation**: Use high-fidelity entanglement links for inter-processor communication
- **Quantum Error Correction**: Account for error correction overhead in allocation decisions

## Verification
- Allocation decisions should respect hardware constraints (qubit count, connectivity)
- Circuit fidelity should meet threshold requirements after allocation
- Network utilization should be balanced across processors
- RL policy should generalize to unseen circuit sizes and hardware configurations
