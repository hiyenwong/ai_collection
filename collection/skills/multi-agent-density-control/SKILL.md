---
name: multi-agent-density-control
description: "Stochastic Density-Driven Optimal Control (D²OC) for multi-agent coverage and distribution matching. Uses Wasserstein distance as running cost with convergence guarantees for stochastic LTI systems. Use when designing decentralized multi-agent coverage, area coverage, distribution matching, or swarm control systems."
---

# Density-Driven Optimal Control for Stochastic Multi-Agent Systems

## Core Problem

**Non-uniform area coverage** for multi-agent systems:
- Spatial priority variations
- Resource constraints
- Decentralized coordination
- Stochastic dynamics

Traditional approaches rely on:
- Eulerian PDE solvers (computationally heavy)
- Heuristic planning (no guarantees)

## Key Innovation: Stochastic D²OC

**Density-Driven Optimal Control (D²OC)**: A Lagrangian framework bridging individual agent dynamics with collective distribution matching.

### Core Idea

Minimize the difference between:
1. **Empirical distribution** of agent positions (time-averaged)
2. **Target density** (non-parametric spatial priority)

Using **Wasserstein distance** as the cost function.

## Mathematical Formulation

### Agent Dynamics (Stochastic LTI)

```
x_{k+1} = A x_k + B u_k + w_k
y_k = C x_k + v_k
```

Where:
- `x_k`: Agent state (position + velocity)
- `u_k`: Control input
- `w_k`: Process noise
- `v_k`: Measurement noise

### Empirical Distribution

For N agents over time window T:
```
μ_empirical = (1/NT) Σ_{i=1}^N Σ_{k=1}^T δ(x_i(k))
```

### Control Objective

```
min_u Σ_{k=0}^H W_2(μ_k, μ_target) + R(u_k)²
```

Where:
- `W_2`: 2-Wasserstein distance
- `μ_target`: Desired spatial density
- `R(u)`: Control effort penalty

## Convergence Guarantee

**Theorem**: Under stochastic LTI dynamics with bounded noise, the time-averaged empirical distribution converges to the target density with bounded tracking error.

### Key Conditions

1. **Reachability**: Target density support reachable from initial positions
2. **Noise bounded**: Process and measurement noise have bounded covariance
3. **Persistence of excitation**: Sufficient exploration of state space

## Algorithm Structure

### MPC-like Formulation

```
At each time step t:
  1. Measure current states {x_i}
  2. Solve finite-horizon optimization:
     min_{u_0:H} Σ_{k=0}^H W_2(μ_k, μ_target) + R(u_k)²
     subject to: dynamics, constraints
  3. Apply first control u_0
  4. Repeat
```

### Decentralized Implementation

Each agent solves local optimization:
- Local objective: Contribution to global distribution
- Communication: Share planned trajectories
- Consensus: Coordinate density contributions

## Applications

### 1. Environmental Monitoring
- Non-uniform sensor placement
- Priority-based coverage
- Adaptive patrolling

### 2. Search and Rescue
- Probability-based area coverage
- Resource allocation
- Dynamic priority updates

### 3. Agricultural Robotics
- Variable-rate application
- Field coverage optimization
- Precision agriculture

### 4. Surveillance
- Priority-based monitoring
- Intruder detection
- Dynamic redeployment

## Comparison with Existing Methods

| Method | Optimality | Decentralized | Guarantees | Complexity |
|--------|------------|---------------|------------|------------|
| D²OC | High | Yes | Convergence | Moderate |
| Voronoi coverage | Medium | Yes | Local optima | Low |
| PDE-based | High | No | Convergence | High |
| Heuristic | Low | Varies | None | Low |

## Implementation Considerations

### Wasserstein Distance Computation

- **Exact**: Linear programming (expensive for large N)
- **Approximate**: Sliced Wasserstein, Sinkhorn divergence
- **Discretization**: Grid-based approximation

### Communication Requirements

- Trajectory sharing: O(N × H) per iteration
- Density estimation: Distributed averaging
- Consensus: Iterative protocols

### Computational Complexity

Per-agent optimization: O(H × dim) with H horizon, dim state dimension

## Design Parameters

| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| Horizon H | Plan quality | 10-50 steps |
| Control penalty R | Smoothness | [0.01, 1.0] |
| Communication rate | Coordination | 1-10 Hz |

## Paper Reference

**Title**: Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems
**Author**: Kooktae Lee
**arXiv**: 2604.08495
**Category**: math.OC, cs.MA, cs.RO, eess.SY
**Published**: 2026-04-09

## Key Equations

### Wasserstein Distance (2-Wasserstein)
```
W_2(μ, ν) = (inf_{γ∈Γ(μ,ν)} ∫||x-y||² dγ(x,y))^{1/2}
```

### Convergence Bound
```
E[||μ_T - μ_target||] ≤ C/√T + O(σ²)
```

Where σ is noise magnitude.

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