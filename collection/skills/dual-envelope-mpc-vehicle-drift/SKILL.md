---
name: dual-envelope-mpc-vehicle-drift
description: "Dual-envelope constrained nonlinear MPC for autonomous vehicle drifting control. Methods for constructing stability envelopes in phase plane, model predictive control with envelope constraints, and handling bounded steering/yaw-moment control for distributed drive EVs. Triggers: vehicle drifting control, MPC envelope constraint, autonomous drifting, distributed drive EV, yaw moment control, saddle point stability, phase plane envelope."
---

# Dual-Envelope Constrained NMPC for Vehicle Drifting

Model predictive control framework for autonomous drifting with stability envelope constraints.

## Overview

Paper: "Dual-Envelope Constrained Nonlinear MPC for Distributed Drive Electric Vehicles Drifting Under Bounded Steering and Direct Yaw-Moment Control" (arXiv: 2604.07342v1, April 2026)

Key contribution: Extended dual envelope framework that accounts for control input coupling, enabling smoother drift convergence and improved tracking.

## Vehicle Dynamics Model

### Distributed Drive Configuration

- Independent torque control for each wheel
- Direct yaw moment generation via torque distribution
- Superior yaw control compared to conventional vehicles

### Drift State Variables

| Variable | Description |
|----------|-------------|
| Slip angle (β) | Vehicle side slip angle |
| Yaw rate (r) | Rotational velocity around vertical axis |
| Velocity (v) | Longitudinal velocity |
| Steering angle (δ) | Front wheel steering |

### Tire Model

Nonlinear tire model captures:
- Force saturation at high slip angles
- Road adhesion coefficient effects
- Combined slip effects

## Saddle Point Analysis

### Phase Plane Construction

Build stability boundaries in (β, r) phase plane:
1. Identify drift equilibrium (saddle point)
2. Construct stability boundaries from equilibrium analysis
3. Account for control input effects on saddle location

### Control Input Coupling Effects

Critical insight: Control inputs reshape phase plane:
- Steering angle shifts saddle point location
- Yaw moment modifies stability boundaries
- Open-loop envelopes may be invalid for closed-loop control

### Saddle Point Coordinate Model

```python
# Account for all relevant parameters
saddle_point = {
    'road_adhesion': μ,       # Road friction coefficient
    'velocity': v,            # Longitudinal velocity
    'steering': δ_f,          # Front wheel steering angle
    'yaw_moment': M_z,        # Additional yaw moment
}
```

## Dual Envelope Framework

### Outer Envelope

**Purpose**: Define recoverable set under bounded control inputs

Characteristics:
- States reachable from drift equilibrium
- Constrained by steering angle limits
- Constrained by yaw moment limits
- Defines maximum drift extent

### Inner Envelope

**Purpose**: Characterize non-drifting stability region

Characteristics:
- States with unsaturated tire forces
- Normal driving stability region
- Transition boundary to drift regime

### Envelope Construction

```
Phase Plane → Envelope Boundaries:
1. Analyze convergence tendency toward saddle points
2. Apply steering angle bounds
3. Apply yaw moment bounds
4. Compute reachable state sets
5. Define inner/outer envelope boundaries
```

## NMPC Controller Design

### Control Objective

Track reference trajectory while maintaining drift stability:
- Maintain desired drift angle
- Track velocity reference
- Control yaw rate
- Respect envelope boundaries

### Constraint Implementation

```python
# NMPC constraints
constraints = {
    'state_envelope': inner < β < outer,  # Slip angle bounds
    'yaw_envelope': r_min < r < r_max,    # Yaw rate bounds
    'steering_limit': |δ_f| < δ_max,      # Steering angle limit
    'yaw_moment_limit': |M_z| < M_z_max,  # Yaw moment limit
}
```

### Optimization Problem

```
minimize: tracking_error + control_effort
subject to: envelope_constraints + input_limits + dynamics
```

## Performance Results

### Hardware-in-the-Loop Experiments

Compared NMPC with envelope constraints vs. unconstrained NMPC:

| Metric | Improvement |
|--------|-------------|
| Steady-state speed error | -33.07% |
| Steady-state sideslip error | -71.18% |
| Steady-state yaw rate error | -31.27% |
| Peak tracking error (friction mismatch) | -63.66% |

### Benefits

- **Smaller convergence** toward drift saddle point
- **Reduced tracking errors** across all state variables
- **Robust to friction mismatch** - Handles road condition changes

## Implementation Guidance

### Controller Tuning

Key parameters:
1. Envelope boundary margins
2. Control horizon length
3. Prediction step size
4. Weighting matrices for cost function

### Real-time Considerations

- Optimize solver for real-time execution
- Use warm-starting for successive solves
- Pre-compute envelope boundaries offline

## Reference

- Paper: arXiv:2604.07342v1
- PDF: https://arxiv.org/pdf/2604.07342v1
- Category: eess.SY (Systems and Control)