---
name: trajectory-based-controlled-invariants
description: "Compute controlled invariant sets for linear discrete-time systems using trajectory-based approach with convex feasible points. Use for MPC design, control invariant set computation, feasibility guarantees, and discrete-time system analysis. Keywords: controlled invariant, MPC, trajectory-based, convex feasible points, discrete-time systems, recursive feasibility."
---

# Trajectory-Based Controlled Invariants

## Description

A trajectory-based approach to computing controlled invariant sets for linear discrete-time systems. Introduces convex feasible points concept for invariant set characterization and provides MPC schemes with recursive feasibility guarantees without precomputed terminal sets.

## Activation Keywords

- controlled invariant
- controlled invariant set
- trajectory-based invariants
- convex feasible points
- MPC recursive feasibility
- discrete-time system invariance
- 控制不变集
- MPC 可行性
- 轨迹方法不变集

## Tools Used

- exec: Run Python scripts for system analysis
- read: Load system models, reference papers
- write: Save invariant set computations

## Core Concepts

### 1. Convex Feisible Points

Definition: A finitely long state trajectory that provides new characterization of controlled invariance.

**Key Properties:**
- Provides necessary condition for control invariance
- Can be verified with finite trajectory length
- Combines with backward fixed-point algorithm

### 2. Controlled Invariant Sets

Sets where system state can remain indefinitely under proper control.

**Traditional Methods:**
- Backward reachability
- Fixed-point iteration

**Trajectory-Based Innovation:**
- Uses finite trajectories instead of infinite analysis
- Reduces computational complexity
- Enables practical MPC design

### 3. MPC without Terminal Sets

Two proposed MPC schemes:
1. Direct feasibility guarantee via trajectory constraints
2. Recursive feasibility through convex feasible points

**Advantages:**
- No need for precomputed terminal sets
- Online feasibility verification
- Reduced offline computation burden

## Instructions for Agents

### Step 1: System Modeling

Given discrete-time linear system:
```
x(k+1) = Ax(k) + Bu(k)
```

Identify:
- State matrix A
- Input matrix B
- State constraints X
- Input constraints U

### Step 2: Trajectory Analysis

1. Generate candidate trajectories
2. Verify convex feasible point conditions
3. Check trajectory constraints satisfaction

**Verification criterion:**
- Trajectory must remain in X for all steps
- Control inputs must satisfy U constraints
- Must provide convex hull feasible for continuation

### Step 3: Invariant Set Computation

Use backward fixed-point algorithm:
```python
def compute_maximal_invariant(A, B, X, U, iterations=100):
    """Compute maximal controlled invariant set."""
    current_set = X
    for i in range(iterations):
        # Backward reachable set
        predecessor = backward_reach(A, B, current_set, U)
        # Intersection with constraints
        current_set = predecessor ∩ X
        if current_set.is_empty():
            break
    return current_set
```

### Step 4: MPC Design

Construct MPC scheme:
```python
def mpc_trajectory_based(x_current, horizon, A, B, X, U, convex_feasible_point):
    """MPC with trajectory-based feasibility guarantee."""
    # Optimization problem
    # Variables: x(0:N), u(0:N-1)
    # Constraints:
    #   - Dynamics: x(k+1) = Ax(k) + Bu(k)
    #   - State: x(k) ∈ X
    #   - Input: u(k) ∈ U
    #   - Feasibility: convex_feasible_point condition
    # Objective: minimize cost function
    
    return optimal_sequence
```

### Step 5: Feasibility Verification

Check recursive feasibility:
- Verify convex feasible point at each iteration
- Ensure existence of feasible continuation
- Validate constraint satisfaction

## Use Cases

### Use Case 1: Safety-Critical Control

**Scenario:** Robot navigation with obstacle avoidance

**Application:**
- Define safety constraints (avoid obstacles)
- Compute controlled invariant safe set
- Design MPC guaranteeing perpetual safety
- No precomputation of terminal safe set needed

### Use Case 2: Resource Management

**Scenario:** Tank level control with limits

**Application:**
- State constraints: tank level bounds
- Input constraints: pump capacity
- Compute invariant operating region
- MPC maintains feasibility indefinitely

### Use Case 3: Power System Control

**Scenario:** Generator scheduling with stability constraints

**Application:**
- State: power output, frequency
- Input: control signals
- Invariant set ensures stability
- Trajectory-based simplifies computation

## Mathematical Formulation

### Convex Feisible Point Definition

A trajectory {x(0), x(1), ..., x(N)} is a convex feasible point if:

1. **State constraints:** x(k) ∈ X for all k
2. **Input constraints:** u(k) ∈ U satisfies x(k+1) = Ax(k) + Bu(k)
3. **Convexity:** There exists convex combination enabling continuation

### Optimization Problem

```
minimize   Σ J(x(k), u(k))
subject to x(k+1) = Ax(k) + Bu(k), k = 0, ..., N-1
           x(k) ∈ X, k = 0, ..., N
           u(k) ∈ U, k = 0, ..., N-1
           convex_feasible_point(x(N)) = true
```

## Error Handling

### Infeasible Initial State

**Problem:** Current state outside invariant set

**Solution:**
- Check feasibility before MPC execution
- If infeasible, use recovery maneuver
- Plan trajectory to invariant set boundary

### Invariant Set Computation Failure

**Problem:** Algorithm doesn't converge

**Solution:**
- Increase iteration limit
- Check constraint compatibility
- Verify system controllability
- Adjust numerical precision

### Numerical Issues

**Problem:** Convex hull computation unstable

**Solution:**
- Use robust convex hull algorithms
- Increase trajectory length
- Apply regularization techniques

## Examples

### Example 1: Double Integrator

**System:**
```
A = [[1, 1], [0, 1]]
B = [[0], [1]]
X = {x: |x₁| ≤ 10, |x₂| ≤ 2}
U = {u: |u| ≤ 1}
```

**Process:**
1. Generate trajectories with N=10
2. Identify convex feasible points
3. Compute maximal invariant set
4. Design MPC with horizon 5

### Example 2: Room Temperature Control

**System:**
```
A = 0.95  # Decay rate
B = 1.0   # Heating effect
X = [18°C, 25°C]
U = [0kW, 5kW]
```

**Application:**
- Compute temperature invariant interval
- MPC maintains comfortable temperature
- No terminal set precomputation

## Resources

- **Paper:** arXiv:2604.07225 - "A Trajectory-based Approach to Controlled Invariants"
- **Code:** scripts/compute_invariant_set.py
- **References:** references/discrete_time_control.md

## Related Skills

- kuramoto-control-theory: Synchronization control
- robust-regret-control: Robust MPC design
- ml-complexity-management: Complexity analysis for control

## Notes

- Applicable to linear discrete-time systems only
- Numerical stability depends on trajectory length
- Convexity assumption required
- MPC horizon affects computational load