---
name: hopper-entanglement-distribution
description: "Hop-by-hop entanglement distribution protocol for asynchronous quantum networks. Enables multiplexed concurrent ebit requests with autonomous node decisions. Activation: quantum network protocol, entanglement distribution, hop-by-hop, async quantum, quantum internet, HOPPER protocol."
---

# HOPPER: Hop-by-hop Entanglement Distribution Protocol for Asynchronous Quantum Networks

> A novel protocol for quantum internet entanglement distribution that enables intermediate nodes to make autonomous, hop-by-hop decisions for parallel ebit establishment, overcoming the serial bottleneck of existing approaches.

## Metadata
- **Source**: arXiv:2605.15869
- **Authors**: Claudio Cicconetti
- **Published**: 2026-05-15
- **Venue**: Accepted at IEEE ICCCN 2026
- **Cross-domain**: Quantum Physics (quant-ph) + Networking (cs.NI)

## Core Methodology

### Key Innovation
The HOPPER protocol introduces **multiplexed concurrent ebit requests** on the same quantum path, where intermediate nodes make **autonomous hop-by-hop decisions** about resource allocation when establishing entanglement. This overcomes the serial bottleneck where traditional approaches must complete one ebit before starting the next.

### Technical Framework

1. **Asynchronous Operation Model**
   - Unlike synchronous time-slotted approaches, nodes operate independently
   - Each node makes local decisions without global synchronization
   - Enables better utilization of multi-qubit memory resources

2. **Multiplexed Concurrent Requests**
   - Multiple ebit requests can be in-flight simultaneously on the same path
   - Nodes manage concurrent state without serial waiting
   - Significantly improves throughput in long-range networks with high latency

3. **Hop-by-hop Autonomous Decisions**
   - Intermediate nodes use local resource state to decide ebit allocation
   - No central coordinator required
   - Self-organizing entanglement distribution

4. **Memory Qubit Parallelism**
   - Leverages multiple memory qubits at intermediate nodes
   - Parallel ebit establishment reduces end-to-end latency
   - Critical advantage grows with network distance

## Implementation Guide

### Prerequisites
- Quantum network simulator (e.g., SeQUeNCe, NetSquid)
- Knowledge of quantum repeater protocols
- Entanglement swapping and purification techniques

### Protocol Steps
1. **Request Initiation**: End nodes send entanglement requests
2. **Hop-by-hop Propagation**: Requests propagate through intermediate nodes
3. **Local Resource Allocation**: Each node allocates memory qubits independently
4. **Parallel EBIT Generation**: Multiple ebits generated concurrently
5. **Entanglement Swapping**: Intermediate nodes perform Bell measurements
6. **Confirmation**: End nodes verify established entanglement

### Performance Characteristics
- Better than synchronous alternatives in high-latency networks
- Scales well with increasing memory qubit count per node
- Effective for multi-request scenarios

## Applications
- Quantum internet infrastructure
- Distributed quantum computing
- Blind quantum computing
- Quantum key distribution networks

## Pitfalls
- Requires nodes with multiple memory qubits
- Decoherence limits effective multiplexing window
- Complex state management for concurrent requests
- Simulation results may not capture all hardware constraints

## Related Skills
- quantum-data-centers-entanglement
- quantum-network-control
- asynchronous-quantum-distributed-computing
- quantum-protocol-designer
