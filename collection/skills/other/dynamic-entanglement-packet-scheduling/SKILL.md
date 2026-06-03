---
name: dynamic-entanglement-packet-scheduling
description: Dynamic entanglement packet scheduling methodology for quantum networks. Online scheduler that dynamically schedules, defers, retries, or drops entanglement distribution reservations. Outperforms static TDMA baselines with lower completion time, higher completion ratio, and graceful degradation under overload.
category: quantum-networks
created: 2026-05-29
source: arXiv:2605.28795
tags: [quantum-networks, scheduling, entanglement, resource-allocation, control-theory, systems-engineering]
---

# Dynamic Entanglement Packet Scheduling for Quantum Networks

**Source**: arXiv:2605.28795 (IEEE QuNAP 2026 / INFOCOM 2026 workshop)
**Authors**: Quang-Phong Tran, Claudio Cicconetti, Marco Conti, Andrea Passarella

## Core Problem

Sharing entanglement among multiple users in scalable quantum networks requires efficient scheduling. Static TDMA-based schedules offer limited flexibility when outcomes are stochastic and arrivals are asynchronous.

## Key Innovation

**Online Dynamic Scheduler** — replaces static periodic scheduling with a real-time controller that can:
- **Schedule**: Assign entanglement distribution reservations dynamically
- **Defer**: Postpone reservations when network resources are temporarily unavailable
- **Retry**: Reattempt failed entanglement generation attempts
- **Drop**: Gracefully abandon reservations when deadlines cannot be met

## Methodology

### 1. Dynamic Scheduling Architecture
- Controller maintains a queue of pending entanglement requests
- Each request has a deadline and priority
- Scheduler evaluates network state in real-time
- Decisions made per-time-slot based on current conditions

### 2. Comparison with Static Baselines
- **Static**: EDF (Earliest Deadline First) recomputed periodically
- **Dynamic**: Per-slot online decision making
- Results: Lower completion time, higher completion ratio, higher throughput

### 3. Overload Behavior
- Dynamic scheduler continues to construct deadline-feasible schedules under overload
- Graceful degradation: drops lowest-priority requests rather than cascading failures
- Static baseline degrades catastrophically under overload

### 4. Systems Engineering Principles
- **Real-time control**: Online adaptation vs. periodic recomputation
- **Fault tolerance**: Retry mechanism for stochastic failures
- **Resource allocation**: Dynamic vs. static partitioning
- **Quality of Service**: Deadline-based prioritization

## Application Scenarios

### Quantum Network Resource Management
- Multi-user entanglement distribution
- Quantum internet backbone scheduling
- Distributed quantum computing resource allocation

### Hybrid Classical-Quantum Control
- Classical controller managing quantum resource allocation
- Real-time feedback from quantum hardware
- Integration with existing network protocols

## Implementation Guidelines

### Scheduler State Machine
```
Request Arrived → Evaluate Feasibility
                    ├── Feasible → Schedule → Execute
                    │               ├── Success → Complete
                    │               └── Failure → Retry (if time permits)
                    └── Infeasible → Defer (if deadline allows)
                                        └── Still infeasible → Drop
```

### Key Design Parameters
- Time slot duration (physical layer constraint)
- Deadline enforcement strictness
- Priority assignment policy
- Retry limit per request

## Pitfalls

- **Stochastic entanglement generation**: Success rates are probabilistic; scheduler must account for expected number of retries
- **Network heterogeneity**: Different links may have different success probabilities
- **Deadline propagation**: End-to-end deadlines must account for multi-hop distribution
- **Resource fragmentation**: Dynamic scheduling may fragment quantum memory resources

## Related Skills
- `quantum-network-scheduling` — existing quantum network scheduling
- `hopper-entanglement-distribution` — hop-by-hop entanglement distribution
- `entanglement-distillation-protocols` — entanglement distillation
