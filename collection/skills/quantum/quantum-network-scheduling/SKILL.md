---
name: quantum-network-scheduling
description: >
  Quantum network resource allocation and entanglement flow scheduling.
  Use when designing, optimizing, or analyzing quantum network architectures
  involving entanglement distribution, multi-channel resource allocation,
  queuing mechanisms for quantum requests, or classical allocation algorithms
  (Dynamic Efficient, Longest Queue First, Weighted LQF) applied to quantum networks.
  Also relevant for quantum-classical hybrid system scheduling and
  entanglement routing in distributed quantum computing.
---

# Quantum Network Scheduling

## Overview

Methodology for resource allocation in multi-channel quantum networks,
based on entanglement distribution optimization with heterogeneous link
characteristics and user-centric request handling.

## Core Concepts

### System Architecture

- **Multi-channel quantum network**: Heterogeneous links with varying
  fidelities, decoherence rates, and generation capacities
- **Entanglement requests**: User-centric queuing with retry mechanisms
- **Classical control plane**: Scheduling algorithms for channel/processor assignment

### Scheduling Algorithms

| Algorithm | Strategy | Best For |
|-----------|----------|----------|
| Dynamic Efficient | Optimizes channel assignment based on current state | High-fidelity requirements |
| Longest Queue First (LQF) | Prioritizes longest-waiting requests | Fairness across users |
| Weighted LQF (WLQF) | Priority-weighted queue management | QoS-differentiated networks |
| **TDMA Packet Scheduling** | Time-slot allocation with periodic recomputation | Scalable multi-user quantum networks |
| **Earliest Deadline First (EDF)** | Deadline-driven priority scheduling | Time-sensitive entanglement requests |

### Entanglement Packet Architecture (arXiv: 2605.28795)

New paradigm: **on-demand entanglement packets** where a central controller
uses TDMA to allocate network resources to quantum nodes on periodic schedules.

- **Periodic schedule**: Each node assigned fixed time slots for entanglement generation
- **Probabilistic fulfillment**: Accounts for quantum channel loss and decoherence
- **Dynamic recomputation**: Schedule rebuilt periodically to handle changing demands
- **Multi-application sharing**: Multiple quantum applications share network bandwidth

### Online Dynamic Scheduling (arXiv: 2605.28795, IEEE QuNAP 2026)

**Online dynamic scheduler** replaces static periodic TDMA with per-slot real-time control:

- **Four actions per slot**: Schedule, Defer, Retry, Drop — based on real-time network state
- **Stochastic awareness**: Entanglement generation is probabilistic; scheduler accounts for expected retries
- **Graceful degradation**: Under overload, drops lowest-priority requests rather than cascading failures
- **Performance gains**: Lower completion time, higher completion ratio, higher throughput vs static EDF baseline
- **Decision state machine**:
  ```
  Request Arrived → Evaluate Feasibility
    ├── Feasible → Schedule → Execute → Success/Retry
    └── Infeasible → Defer (if deadline allows) → Still infeasible → Drop
  ```

**When to use dynamic vs static**:
- Static TDMA/EDF: Stable, predictable workloads with low stochasticity
- Dynamic scheduler: Asynchronous arrivals, stochastic outcomes, variable network conditions

### Key Design Patterns

1. **Heterogeneous link modeling**: Characterize links by fidelity, latency, capacity
2. **Request queuing**: Implement retry mechanisms with exponential backoff
3. **Channel assignment**: Match request requirements to link capabilities
4. **Entanglement swapping**: Multi-hop distribution through intermediate nodes
5. **Resource contention resolution**: Handle competing requests for shared quantum processors
6. **TDMA slot allocation**: Assign periodic time slots for deterministic access
7. **Deadline tracking**: Monitor and enforce entanglement delivery deadlines

## Usage Workflow

### 1. Define Network Topology
```
nodes: [A, B, C, ...]
links: [(A,B): {fidelity, capacity, decoherence_rate}, ...]
processors: [P1, P2, ...]: {generation_rate, memory_size}
```

### 2. Model Request Queue
- Track pending entanglement requests with QoS requirements
- Implement retry logic with configurable backoff
- Monitor queue lengths per destination pair

### 3. Select Scheduling Algorithm
- **Dynamic Efficient**: When maximizing throughput is priority
- **LQF**: When fairness across all users matters
- **WLQF**: When some requests have higher priority (e.g., error correction)

### 4. Optimize Resource Allocation
- Assign channels to maximize successful entanglement generation
- Balance load across heterogeneous links
- Account for decoherence time windows

## Pitfalls

- **Decoherence deadline**: Entanglement must be distributed before qubit coherence expires
- **Fidelity degradation**: Each swap operation reduces fidelity exponentially
- **Classical coordination overhead**: Synchronization latency impacts quantum state validity
- **Resource starvation**: Simple LQF can starve low-demand destination pairs
- **Network fragmentation**: Dynamic scheduling may fragment quantum memory resources across time slots
- **Stochastic retry explosion**: Under high loss rates, retry queues can grow unbounded — set per-request retry limits
- **Deadline propagation in multi-hop**: End-to-end deadlines must account for sequential swapping at each hop, not just first-hop generation
- **Overload handling**: Static schedulers degrade catastrophically under overload; prefer dynamic schedulers that can gracefully drop low-priority requests

## Related Papers

- arXiv:2605.04767 — Scheduling Entanglement Flows in Multi-channel Quantum Networks
- arXiv:2605.04047 — Sequential vs. Simultaneous Entanglement Swapping under Optimal Link-Layer Control
- arXiv:2605.02389 — Action-Space Engineering for Quantum Circuit Routing in Distributed Quantum Computing

## Activation Keywords
- quantum network scheduling
- entanglement flow allocation
- quantum resource scheduling
- multi-channel quantum network
- entanglement distribution
- quantum network queuing
- 量子网络调度
- 纠缠分发
