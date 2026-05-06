---
name: finite-time-reachability-partial-control
description: Finite-time reachability control for constrained nonlinear systems with partial loss of control authority. Addresses driving system to target state in finite time despite partial actuator failures. Use when designing fault-tolerant control, handling actuator failures, reachability under constraints, or nonlinear control with reduced control authority.
---

# Finite-Time Reachability Under Partial Control Loss

## Overview

Techniques for driving constrained nonlinear systems to target states in finite time when the system suffers partial loss of control authority (actuator failures, reduced control inputs).

**Key Problem**: Can we still reach target states when some actuators fail?

**Answer**: Yes, under appropriate conditions and using time partitioning strategies.

## Core Concepts

### Partial Loss of Control Authority

**Definition**: System loses ability to control one or more inputs:
- Actuator failure: Input becomes uncontrolled
- Reduced control range: Input magnitude limited
- Unavailable inputs: Control inputs disabled

**Impact**: Available control inputs must compensate for lost inputs.

### Constrained Nonlinear Systems

**System Model**:
```
dx/dt = f(x, u_c, u_u)

where:
- x: state vector
- u_c: controlled inputs (available)
- u_u: uncontrolled inputs (lost/failed)
- f: nonlinear dynamics
```

**Constraints**:
- State constraints: x ∈ X (e.g., position, velocity bounds)
- Control constraints: u_c ∈ U_c (e.g., magnitude limits)
- Uncontrolled input: u_u ∈ U_u (bounded disturbance)

### Finite-Time Reachability

**Goal**: Drive state x(t0) to target state x_target in finite time T, despite:
- Partial control loss
- Nonlinear dynamics
- State/control constraints
- Uncontrolled input effects

**Challenge**: Uncontrolled inputs can push state away from target.

## Solution Approach

### Linear Driftless Approximation

**Key Insight**: Approximate nonlinear dynamics near initial state with simple linear model.

**Approximation**:
```
dx/dt ≈ g(x0) + ∑_{i∈controlled} B_i u_i

where:
- g(x0): drift term at initial state
- B_i: control direction vectors
- u_i: controlled inputs
```

**Driftless Property**: Linear approximation without uncontrolled dynamics (compensated by control design).

### Time Partitioning Strategy

**Core Algorithm**:

1. **Partition time horizon**: T → T1 + T2 + ... + Tk (successively smaller intervals)

2. **Design control inputs**: Based on approximate dynamics in each partition

3. **Bound error**: Show that total error remains bounded despite uncontrolled inputs

4. **Reduce error**: As partitions become shorter, error → 0

### Mathematical Framework

```python
def finite_time_reachability(x0, x_target, T, dynamics, uncontrolled_bounds):
    """
    Design control inputs to reach target in finite time.
    
    Strategy:
    1. Partition time horizon into smaller intervals
    2. Design control for each interval based on approximation
    3. Bound cumulative error from uncontrolled inputs
    4. Refine partition to reduce error to zero
    """
    
    # Time partitions
    partitions = create_partitions(T)
    
    # Current state
    x_current = x0
    
    # Control sequence
    u_sequence = []
    
    for delta_t in partitions:
        # Compute linear approximation at current state
        drift, B_controlled = approximate_dynamics(x_current, dynamics)
        
        # Design control to compensate drift and move toward target
        u_design = solve_reachability_subproblem(
            x_current, x_target, drift, B_controlled, delta_t, 
            uncontrolled_bounds
        )
        
        u_sequence.append(u_design)
        
        # Predict next state (with worst-case uncontrolled input)
        x_next = predict_state(x_current, u_design, uncontrolled_bounds, delta_t)
        x_current = x_next
    
    return u_sequence

def create_partitions(T):
    """
    Create successively smaller time partitions.
    
    Example: T/2, T/4, T/8, ..., T/2^k
    """
    partitions = []
    t_remaining = T
    k = 1
    
    while t_remaining > epsilon:
        delta_t = T / (2 ** k)
        partitions.append(delta_t)
        t_remaining -= delta_t
        k += 1
    
    return partitions
```

## Reachability Analysis

### Error Bounds

**Key Result**: Under appropriate conditions, designed control inputs achieve:

```
‖x(T) - x_target‖ ≤ ε

where ε → 0 as partitions become finer
```

**Conditions**:
1. Linear approximation valid near initial state
2. Controlled inputs can compensate drift
3. Uncontrolled input bounds known
4. Time horizon sufficiently long

### Convergence Proof

**Step 1**: Show error bounded in each partition

**Step 2**: Show cumulative error bounded by sum of partition errors

**Step 3**: Show partition errors → 0 as partitions → smaller

**Result**: Total error → 0, reaching target state.

## Practical Implementation

### Algorithm Steps

**Phase 1: System Analysis**
```python
# 1. Identify controlled vs. uncontrolled inputs
controlled_inputs = [u1, u2]  # Available
uncontrolled_inputs = [u3]     # Failed/unavailable

# 2. Compute control authority
# Can controlled inputs reach all directions?
control_reachability = analyze_control_space(dynamics, controlled_inputs)

# 3. Estimate uncontrolled input bounds
u_bounds = estimate_uncontrolled_bounds(system_data)
```

**Phase 2: Control Design**
```python
# 1. Choose time horizon
T = compute_minimum_time(x0, x_target, dynamics, control_reachability)

# 2. Create time partitions
partitions = create_partitions(T)

# 3. Design control sequence
u_sequence = []
for delta_t in partitions:
    u_i = design_partition_control(x_current, x_target, delta_t, dynamics)
    u_sequence.append(u_i)
```

**Phase 3: Execution**
```python
# Execute control sequence
for u, delta_t in zip(u_sequence, partitions):
    apply_control(u, delta_t)
    x_current = measure_state()
    
    # Adapt if state drifts significantly
    if deviation(x_current, expected_state) > threshold:
        u_sequence = adapt_control_sequence(x_current, x_target, remaining_time)
```

### Implementation Code Pattern

```python
class FiniteTimeReachabilityController:
    def __init__(self, dynamics, controlled_indices, uncontrolled_bounds):
        self.f = dynamics
        self.u_c_idx = controlled_indices
        self.u_u_bounds = uncontrolled_bounds
    
    def compute_control(self, x0, x_target, T):
        """Design control to reach target in finite time."""
        
        # Check feasibility
        if not self.check_reachable(x0, x_target, T):
            raise ValueError("Target not reachable with available controls")
        
        # Partition time horizon
        partitions = self.create_partitions(T)
        
        # Design control sequence
        controls = []
        x = x0
        
        for delta_t in partitions:
            # Approximate dynamics at current state
            g, B = self.linear_approximation(x)
            
            # Solve subproblem
            u_c = self.solve_reachability_subproblem(
                x, x_target, g, B, delta_t
            )
            
            controls.append((u_c, delta_t))
            
            # Predict next state (worst-case uncontrolled)
            x = self.predict_worst_case(x, u_c, delta_t)
        
        return controls
    
    def linear_approximation(self, x):
        """Linear driftless approximation at state x."""
        
        # Drift term (compensated by control)
        g = compute_drift(x, self.f)
        
        # Control directions (controlled inputs only)
        B = []
        for i in self.u_c_idx:
            B_i = compute_control_direction(x, i, self.f)
            B.append(B_i)
        
        return g, B
    
    def solve_reachability_subproblem(self, x, x_target, g, B, delta_t):
        """Solve finite-time reachability subproblem."""
        
        # Desired motion toward target
        motion_needed = (x_target - x) / delta_t
        
        # Compensate drift
        motion_controlled = motion_needed - g
        
        # Solve for control inputs
        u_c = solve_linear_system(B, motion_controlled)
        
        # Enforce control constraints
        u_c = project_to_constraints(u_c, self.control_bounds)
        
        return u_c
```

## Applications

### Aircraft Control

**Scenario**: Fighter jet with actuator failure
**Problem**: One control surface fails mid-flight
**Solution**: Use remaining control surfaces to maintain control and reach landing state

**Example from Paper**: Simulation on fighter jet model demonstrates reaching target state despite loss of one control input.

### Autonomous Vehicles

**Scenario**: Vehicle with steering failure
**Problem**: Steering actuator fails, only throttle available
**Solution**: Use differential braking or throttle modulation to reach safe state

### Robotics

**Scenario**: Robot arm with joint failure
**Problem**: One joint motor fails
**Solution**: Use remaining joints to compensate and reach desired end-effector position

### Spacecraft

**Scenario**: Satellite with thruster failure
**Problem**: One thruster unavailable
**Solution**: Use remaining thrusters to achieve attitude and position control

## Design Considerations

### Time Horizon Selection

**Minimum Time**: Depends on:
- Control authority (how many inputs available)
- Distance to target
- Uncontrolled input bounds

**Heuristic**:
```
T_min ∝ (‖x0 - x_target‖) / (‖u_c‖_max * control_efficiency)
```

### Partition Granularity

**Tradeoff**:
- Finer partitions → Smaller error → More computation
- Coarser partitions → Larger error → Less computation

**Guideline**: Start with T/2, T/4, ..., until error < threshold

### Control Constraints

**Handling**:
- Magnitude limits: Project control to feasible region
- Rate limits: Limit control changes between partitions
- Energy limits: Optimize total control energy

## Theoretical Results

### Reachability Condition

**Theorem**: Target state reachable in finite time if:
1. Controlled inputs span sufficient directions
2. Time horizon T ≥ T_min
3. Uncontrolled input bounds finite

### Error Bound

**Lemma**: Designed control achieves bounded error:
```
‖x(T) - x_target‖ ≤ C * (sum of partition errors)

where C depends on system properties
```

### Convergence

**Result**: As partition size → 0:
- Partition errors → 0
- Total error → 0
- Target state reached exactly

## Related Work

### Control Theory
- **Reachability theory**: What states can be reached?
- **Fault-tolerant control**: Handle actuator failures
- **Constrained control**: State/control constraints

### Comparison with Other Methods

| Method | Approach | Pros | Cons |
|--------|----------|------|------|
| **This method** | Time partitioning + linear approximation | Works for nonlinear + constraints | Requires sufficient control authority |
| **Robust MPC** | Model predictive with uncertainty | Handles uncertainty | Computationally heavy |
| **Sliding mode** | Robust control law | Simple implementation | Chattering, not optimal |

## References

- Paper: arXiv:2604.08327v1 - "Finite-time Reachability for Constrained, Partially Uncontrolled Nonlinear Systems"
- PDF: https://arxiv.org/pdf/2604.08327v1
- Authors: Ram Padmanabhan, Melkior Ornik
- Categories: math.OC, eess.SY
- Published: 2026-04-09

## Related Skills

- `mpc-stability-suboptimality`: MPC under model mismatch
- `fault-tolerant-control`: General fault tolerance
- `nonlinear-control-design`: Nonlinear control methods

## Further Reading

For detailed proofs:
- Paper Section 2: Linear approximation method
- Paper Section 3: Time partitioning algorithm
- Paper Section 4: Error analysis
- Paper Section 5: Fighter jet simulation example

---

**Date Created**: 2026-04-10
**Paper Source**: arxiv weekly systems engineering search