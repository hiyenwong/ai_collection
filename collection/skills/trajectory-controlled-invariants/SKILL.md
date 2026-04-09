---
name: trajectory-controlled-invariants
description: "Trajectory-based computation of controlled invariant sets for linear discrete-time systems and MPC. Use when computing maximal controlled invariant sets, designing MPC without terminal sets, or needing recursive feasibility guarantees. Keywords: controlled invariants, MPC, trajectory-based, convex feasible points, recursive feasibility, terminal sets."
---

# Trajectory-Based Controlled Invariants for MPC

New approach to computing controlled invariant sets using trajectory-based characterization, enabling MPC without precomputed terminal sets.

## Core Innovation

**Convex Feasible Points (CFPs)**: New characterization of controlled invariance using finitely long state trajectories, not geometric set computation.

## Key Concepts

### Controlled Invariant Set

Set $S$ where: if $x \in S$, exists control $u$ such that next state $x' \in S$

Traditional approach: Backward fixed-point iteration (computationally expensive)

### Convex Feasible Point

A point $x$ is CFP if exists trajectory $x_0, x_1, ..., x_n$ where:
- $x_0 = x$
- All $x_k$ satisfy constraints
- Trajectory length $n$ finite

**Key insight**: CFPs characterize controlled invariance without computing full set.

## Algorithm

### 1. CFP Identification

```
Given: System Ax + Bu, constraints Cx ≤ d
Find: Trajectory from x satisfying constraints throughout
```

### 2. Maximal Controlled Invariant

Combine CFP notion with backward fixed-point algorithm:
- More efficient than pure geometric computation
- Produces maximal controlled invariant set

### 3. MPC Design

Two schemes with recursive feasibility guarantee:
- **No terminal set required**
- CFPs provide implicit terminal constraint

## MPC Without Terminal Sets

Traditional MPC requires:
- Terminal set (precomputed)
- Terminal cost
- Complex offline computation

This approach:
- Uses CFPs as implicit terminal constraint
- Recursive feasibility guaranteed
- Less offline computation

## Optimization Formulation

Search for CFPs as optimization problem:

$$\min_{u_0,...,u_{n-1}} \|x_n - x_0\|$$
$$\text{s.t. } x_k \in \mathcal{X}, u_k \in \mathcal{U}, x_{k+1} = Ax_k + Bu_k$$

## Practical Benefits

1. **Reduced offline computation**: No terminal set computation
2. **Guaranteed feasibility**: Recursive feasibility from CFP structure
3. **Flexible MPC**: Can adjust horizon online
4. **Scalable**: Trajectory-based approach scales better than set computation

## Design Procedure

1. Identify system dynamics $Ax + Bu$
2. Define constraint sets $\mathcal{X}, \mathcal{U}$
3. Solve optimization for CFPs
4. Design MPC using CFP structure
5. Verify recursive feasibility

## Applications

- Constrained linear systems
- Autonomous vehicle control
- Process control
- Robotics
- Power systems

## Comparison

| Aspect | Traditional | Trajectory-Based |
|--------|-------------|------------------|
| Terminal set | Required | Not required |
| Offline computation | Heavy | Light |
| Feasibility guarantee | Via terminal set | Via CFPs |
| Flexibility | Limited | High |

## Key Result

Controlled invariant sets computed through trajectory characterization:
- More efficient than geometric methods
- Enables MPC without terminal sets
- Practical for online implementation

## References

- arXiv:2604.07225v1 - "A Trajectory-based Approach to the Computation of Controlled Invariants with application to MPC"
- Accepted at European Control Conference 2026
- Blanchini (1999) - Survey on invariant sets

## Activation Keywords

- controlled invariants
- MPC
- trajectory-based
- convex feasible points
- recursive feasibility
- terminal sets

## Tools Used

- exec
- read
- write

## Instructions for Agents

Use this skill for computing maximal controlled invariant sets for linear discrete-time systems. Apply the trajectory-based approach to enable MPC without explicit terminal set computation.

## Examples

User: Help me with Trajectory Controlled Invariants
Agent: [Activates trajectory-controlled-invariants skill and follows the instructions above]
