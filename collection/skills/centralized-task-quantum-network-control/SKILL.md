---
name: centralized-task-quantum-network-control
description: >
  Resource-centric, task-based centralized control architecture for quantum networks. Replaces layered
  protocol stacks with a centralized controller that tracks quantum memory availability across all nodes
  and schedules objectives using priority-based scheduling. Validated on bottleneck, grid, star, and
  caveman topologies using SeQUeNCe simulator. Reduces latency compared to layered architectures.
  Use when designing quantum network control architectures, evaluating layered vs centralized approaches,
  priority-based quantum resource scheduling, or scaling quantum network simulators.
metadata:
  arxiv_id: "2605.03336"
  published: "2026-05-05"
  authors: "Alexander Pirker, Robert J. Hayek, Alexander Kolar, Igor Kadota, Joaquin Chung, Rajkumar Kettimuthu"
  tags: [quantum-networks, centralized-control, resource-scheduling, SeQUeNCe, layered-vs-task-based, topology-evaluation, systems-engineering]
---

# Centralized Task-Based Quantum Network Control

## Overview

For a decade, layered protocol stacks dominated quantum network architecture design. However, layered architectures
impose stringent design and timing constraints that add latency to entanglement generation requests and cause
state degradation that minimizes achievable fidelities.

This methodology replaces the layered approach with a **resource-centric, task-based centralized controller**
that directly tracks quantum memory availability and schedules objectives with priority-based scheduling.

## Core Architecture

### Centralized Controller Components

```
┌─────────────────────────────────────────────┐
│           Centralized Controller             │
│  ┌───────────────────────────────────────┐  │
│  │    Global Memory State Tracker         │  │
│  │  (tracks qubit availability per node)  │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │    Priority-Based Objective Scheduler  │  │
│  │  (offline scheduling of entanglement   │  │
│  │   requests by priority and resources)  │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │    Topology-Aware Path Planner         │  │
│  │  (maps requests to physical paths)     │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Design Principles

1. **Resource-Centric**: Schedule based on actual qubit/memory availability, not protocol layer abstraction
2. **Task-Based**: Handle entanglement generation requests as tasks with priorities, not as layered protocol events
3. **Centralized**: Global view enables optimal resource allocation across the entire network
4. **Offline Scheduling**: Pre-compute schedules to minimize online decision latency

## Topology Performance Analysis

Evaluation across four topologies reveals critical trade-offs:

| Topology | Low-Delay Delivery | High-Delay Tail | Saturation Behavior |
|----------|-------------------|-----------------|---------------------|
| **Caveman** | High | Higher than star | Graceful degradation |
| **Grid** | High | Higher than star | Graceful degradation |
| **Star** | Lower | Lower | Fast saturation at high load |
| **Bottleneck** | Variable | Variable | Depends on bottleneck capacity |

### Key Findings

1. **Caveman and Grid topologies**: Higher fraction of requests delivered with low delay, but also higher fraction of highly delayed requests (bimodal distribution)
2. **Star topology**: CDFs of priority queues converge fast into saturation for increasing request arrival rates
3. **Reservation delay**: Linear shift of CDFs in terms of queue size for all topologies
4. **High-load robustness**: Framework remains robust under high load, with predictable degradation patterns

## Implementation Steps

### Step 1: Deploy SeQUeNCe Simulator
```python
# Use SeQUeNCe quantum network simulator
# https://github.com/sequence-toolbox/central_scheduler/
```

### Step 2: Define Network Topology
Configure node positions, link fidelities, memory sizes, and decoherence times.

### Step 3: Implement Centralized Controller
- **Memory Tracker**: Poll all nodes for qubit availability state
- **Priority Scheduler**: Sort requests by priority, deadline, and resource requirements
- **Path Planner**: Map each request to a feasible path given current memory state

### Step 4: Set Reservation Patterns
Define varying reservation delays and request arrival rates to stress-test the controller.

### Step 5: Evaluate Performance Metrics
- Fraction of requests delivered within latency threshold
- CDF of delivery delays
- Queue size distributions
- Saturation points for different topologies

## Advantages Over Layered Architecture

| Aspect | Layered Approach | Task-Based Centralized |
|--------|-----------------|----------------------|
| Latency | High (layer processing overhead) | Low (direct scheduling) |
| State Degradation | Significant (timing delays) | Minimized |
| Resource Visibility | Local (per-layer) | Global |
| Scalability | Limited by layer boundaries | Scales with controller capacity |

## Pitfalls

- **Central controller bottleneck**: The centralized controller itself can become a bottleneck — ensure controller processing capacity exceeds peak request rate
- **Memory state staleness**: Quantum memory decoheres rapidly — the global memory tracker must update frequently enough to reflect current state
- **Single point of failure**: Centralized architecture has inherent single-point-of-failure risk — consider redundant controllers
- **Topology dependence**: Performance varies significantly by topology — caveman/grid perform better than star for this approach
- **Reservation delay tuning**: Queue size scales linearly with reservation delay — optimize this parameter per topology

## Related Skills

- `scope-syndrome-control-plane` — QEC-aware routing (complementary network-layer approach)
- `quantum-network-task-control` — Existing quantum network control framework
- `quantum-network-routing-hamiltonian` — QKD network routing
- `quantum-network-osi-stack` — Layered quantum network architecture (contrasting approach)

Activation: quantum network control, centralized quantum controller, task-based scheduling, SeQUeNCe simulator, quantum network topology, entanglement generation, priority scheduling, resource-centric quantum network, layered vs task-based quantum architecture
