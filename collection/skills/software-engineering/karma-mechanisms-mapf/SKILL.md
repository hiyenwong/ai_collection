---
name: karma-mechanisms-mapf
description: Karma Mechanisms for Decentralised Cooperative Multi-Agent Path Finding (MAPF). Novel coordination framework using artificial non-tradeable credits (Karma) to account for past cooperative behavior and regulate conflict resolution. Bilateral negotiation enables pairwise replanning without global priority structures. Promotes long-term fairness under limited communication. Use for: (1) Decentralized multi-agent coordination, (2) fair resource allocation, (3) path planning without centralization, (4) cooperative conflict resolution.
---

# Karma Mechanisms for Decentralized MAPF

## Overview

Multi-Agent Path Finding (MAPF) requires coordination among multiple agents computing conflict-free trajectories. Centralized solvers are optimal but computationally expensive, while decentralized heuristics are fast but suboptimal and unfair.

**Karma Mechanism**: Decentralized coordination using artificial credits that account for past cooperation and regulate future decisions. Enables pairwise conflict resolution with long-term fairness without global priority structures.

## Key Concepts

### Karma Credits

**Definition**: Artificial, non-tradeable credits representing cooperative behavior history.

**Properties**:
- Non-tradeable: Cannot be exchanged between agents
- History-dependent: Accumulated from past cooperation
- Fairness-regulating: Used in conflict resolution

**Mechanism**:
```
Agent i has Karma_i(t) = history of cooperation
Higher Karma → higher priority in conflicts
Karma decreases when winning conflicts
Karma increases when yielding to others
```

### Bilateral Negotiation

**Conflict Resolution Process**:
1. Detect conflict between agents i and j
2. Compare Karma values: `Karma_i vs Karma_j`
3. Higher Karma agent wins priority
4. Winning agent: Karma decreases
5. Yielding agent: Karma increases
6. Both agents replan locally

**No Global Priority**:
- Pairwise negotiation only
- No central coordinator
- Limited communication required

### Long-Term Fairness

**Fairness Properties**:
- **Harsanyian**: Total utility maximization
- **Rawlsian**: Minimize worst outcome
- **Utilitarian**: Average utility
- **Egalitarian**: Equal distribution

**Karma Mechanism Effects**:
- Balances replanning effort across agents
- Reduces disparity in service times
- Maintains overall efficiency

## Mathematical Framework

### Karma Dynamics

**Update Rule**:
```
Karma_i(t+1) = Karma_i(t) - α (if win)
Karma_i(t+1) = Karma_i(t) + β (if yield)
```

Where:
- `α`: penalty for winning
- `β`: reward for yielding
- `α, β > 0` and balanced

### Conflict Resolution

**Decision Rule**:
```
Agent i wins if: Karma_i > Karma_j
Agent j wins if: Karma_j > Karma_i
Random tie-breaking if equal
```

**Replanning**:
```
Winning agent: Replan path
Yielding agent: Adjust path around winner
```

### Performance Metrics

**Efficiency**:
```
Total time = sum_i completion_time_i
Average time = mean(completion_times)
```

**Fairness**:
```
Disparity = max(time) - min(time)
Standard deviation of completion times
```

## Applications

### 1. Robotic Warehouses

**Scenario**: Lifelong pickup-and-delivery
- Agents: warehouse robots
- Tasks: continuously assigned
- Constraints: kinematic orientation

**Benefits**:
- Balanced replanning effort
- Fair service times
- Real-time applicability

### 2. Autonomous Vehicles

**Scenario**: Multi-vehicle coordination
- Agents: autonomous cars
- Tasks: navigation to destinations
- Constraints: traffic rules

**Benefits**:
- Decentralized decision-making
- Fair priority allocation
- No central server needed

### 3. Drone Swarms

**Scenario**: Multi-drone task allocation
- Agents: drones
- Tasks: area coverage
- Constraints: battery limits

**Benefits**:
- Efficient coordination
- Fair workload distribution
- Limited communication

## Implementation Guidelines

### Karma Initialization

1. Set initial Karma values (equal or weighted)
2. Define update parameters (α, β)
3. Set Karma bounds (min, max)

### Conflict Detection

1. Check for path overlaps
2. Identify collision times
3. Detect conflicting agents

### Negotiation Protocol

1. Exchange Karma values
2. Compare and decide winner
3. Update Karma accordingly
4. Replan paths locally

### Fairness Monitoring

1. Track service times per agent
2. Compute fairness metrics
3. Validate long-term balance

## Advantages

1. **Decentralized**: No central coordinator
2. **Fair**: Long-term fairness guaranteed
3. **Efficient**: Near-optimal solutions
4. **Scalable**: Limited communication overhead
5. **Real-time**: Fast pairwise replanning

## Experimental Results

**Testbed**: Lifelong robotic warehouse
- Kinematic orientation constraints
- Multi-agent pickup-and-delivery
- Large-scale simulation

**Findings**:
- Karma balances replanning effort
- Reduces service time disparity
- Maintains overall efficiency
- No sacrifice in performance

## Code Repository

- GitHub: https://github.com/DerKevinRiehl/karma_dmapf
- Implementation: Karma mechanism for MAPF
- Language: Python/C++

## References

- Paper: "Karma Mechanisms for Decentralised, Cooperative Multi Agent Path Finding" (arxiv:2604.07970)
- Authors: Kevin Riehl, Julius Schlapbach, Anastasios Kouvelas, Michail A. Makridis
- PDF: ~/.openclaw/workspace/papers/karma-mechanisms-mapf.pdf

## Related Skills

- `cognitive-flexibility-bayesian-estimation`: Adaptive belief systems
- `resilience-dynamics-cpsos`: Multi-agent resilience
- `safe-rl-forward-invariant`: Safety in multi-agent systems

## Description

This skill provides specialized capabilities for its domain.

## Activation Keywords

- keyword1
- keyword2
- keyword3

## Tools Used

- read: Read files
- write: Write files
- exec: Execute commands

## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance

## Examples

```
User: How do I use this skill?
Agent: I'll help you with this skill...
```