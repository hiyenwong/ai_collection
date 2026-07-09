---
name: dual-envelope-mpc
description: Nonlinear Model Predictive Control with dual-envelope constraints for distributed drive systems. Use when: vehicle dynamics control, MPC implementation, envelope-based stability analysis, autonomous drifting, distributed drive electric vehicles, phase plane analysis, saddle point modeling, or constrained nonlinear control systems.
---

# Dual-Envelope Constrained Nonlinear MPC

## Overview

This skill provides methodology for implementing dual-envelope constrained Nonlinear Model Predictive Control (NMPC) for distributed drive electric vehicles. The approach uses phase plane analysis with saddle point modeling to define stability envelopes that guide controller design for extreme maneuvers like autonomous drifting.

**Key Innovation**: Addresses the issue where control input coupling reshapes phase plane topology and shifts saddle point location, invalidating open-loop equilibrium-based envelope structures when used for closed-loop control.

## Core Concepts

### 1. Saddle Point Coordinate Model

Combines nonlinear tire model with handling diagram to establish saddle point coordinates that explicitly account for:
- Road adhesion coefficient (μ)
- Longitudinal velocity (vx)
- Front wheel steering angle (δf)
- Additional yaw moment (Mz)

**Key Insight**: Saddle points define the transition between stable and unstable regions in the phase plane (slip angle β vs yaw rate ωz).

### 2. Dual Envelope Framework

**Outer Envelope**:
- Defines recoverable set under bounded control inputs
- Based on convergence tendency toward saddle points
- Constraints: front wheel steering angle + additional yaw moment
- Purpose: Ensures state remains recoverable during drifting maneuvers

**Inner Envelope**:
- Characterizes non-drifting stability region
- Associated with unsaturated tire forces
- Normal vehicle operation stability boundary
- Purpose: Defines normal driving stability region

### 3. Nonlinear Tire Model

Essential for capturing:
- Tire force saturation
- Coupling between longitudinal and lateral forces
- Relationship between slip angle and tire forces

### 4. Phase Plane Analysis

Phase plane (β, ωz) topology:
- Saddle points mark stability transition
- Control input coupling reshapes topology
- Envelope boundaries define operational regions
- Closed-loop vs open-loop dynamics differ

## Implementation Workflow

### Step 1: Establish Tire Model

Use nonlinear tire model capturing:
- Combined slip (longitudinal + lateral)
- Force saturation behavior
- Road adhesion effects

Common models:
- Pacejka tire model
- Dugoff tire model
- Brush tire model

### Step 2: Construct Handling Diagram

Plot tire force characteristics:
- Lateral force vs slip angle
- Account for longitudinal force coupling
- Identify saturation regions

### Step 3: Calculate Saddle Point Coordinates

Solve for equilibrium points considering:
- Current road adhesion coefficient μ
- Vehicle velocity vx
- Control inputs (δf, Mz)
- Tire force balance equations

Mathematical formulation:
```
β* = saddle point slip angle coordinate
ωz* = saddle point yaw rate coordinate

Depends on: μ, vx, δf, Mz
```

### Step 4: Build Dual Envelope

**Outer Envelope Construction**:
1. Simulate state trajectories under bounded control inputs
2. Identify convergence regions toward saddle points
3. Define envelope boundary from recoverable state set
4. Ensure envelope respects control constraints

**Inner Envelope Construction**:
1. Identify tire saturation boundaries
2. Define region where tire forces remain unsaturated
3. Characterize normal stability region
4. Set boundary at transition to drifting regime

### Step 5: Implement NMPC Controller

Formulate optimization problem:
```
minimize: tracking error + control effort
subject to:
  - Vehicle dynamics constraints
  - Outer envelope constraint (recoverability)
  - Inner envelope constraint (if needed)
  - Control input bounds (δf, Mz)
  - State constraints
```

Use sequential quadratic programming (SQP) or other NMPC solvers.

### Step 6: Hardware-in-the-Loop Validation

Validate controller performance:
- Compare with NMPC without envelope constraints
- Measure tracking errors: speed, sideslip angle, yaw rate
- Verify smoother convergence toward drift saddle point
- Test under varying road adhesion conditions

## Key Benefits

| Metric | Improvement vs NMPC without envelopes |
|--------|----------------------------------------|
| Steady-state speed tracking error | -33.07% |
| Steady-state sideslip angle error | -71.18% |
| Steady-state yaw rate error | -31.27% |
| Peak tracking error | -63% |
| Convergence smoothness | Improved |

## Control Input Coupling Effects

**Critical Issue**: Open-loop envelopes derived from equilibrium analysis become invalid for closed-loop control because:

1. Control input coupling reshapes phase plane topology
2. Saddle point location shifts under closed-loop dynamics
3. Envelope structure changes with active control
4. Boundaries must account for control constraints

**Solution**: Extended dual envelope framework explicitly accounts for:
- Bounded steering angle constraints
- Bounded yaw moment constraints
- Control-induced topology changes
- Closed-loop convergence behavior

## Distributed Drive Advantages

Distributed drive electric vehicles provide:
- Superior yaw moment control (individual wheel torque)
- Faster response than traditional steering-based control
- Additional yaw moment Mz as control input
- Suitable for extreme maneuvers (drifting)

## Phase Plane Topology

### State Variables
- β: vehicle sideslip angle
- ωz: yaw rate

### Equilibrium Points
- Stable equilibria: attract nearby states
- Saddle points: bifurcation points between stability regimes
- Unstable equilibria: repel nearby states

### Envelope Boundaries
- Outer envelope: recoverability boundary
- Inner envelope: normal stability boundary
- Saddle points: transition markers

## Applications

### Autonomous Drifting
- Controlled extreme maneuvers
- Stable drift state maintenance
- Smooth transition to/from drift

### Vehicle Stability Control
- Active safety systems
- Envelope-based intervention triggers
- Prevention of unrecoverable states

### Advanced Driver Assistance
- Performance driving assistance
- Stability margin monitoring
- Predictive control intervention

## Mathematical Framework

### Vehicle Dynamics

Simplified 2-DOF model:
```
dβ/dt = -(vx/lf+lr)[lf*Cf*cos(δf) + lr*Cr + Mz/vx]
       / (m*vx) + ωz
       
dωz/dt = [lf*Cf*cos(δf) - lr*Cr - Mz] / Iz
```

Where:
- lf, lr: front/rear axle distances
- Cf, Cr: front/rear tire cornering stiffnesses
- m: vehicle mass
- Iz: yaw moment of inertia
- vx: longitudinal velocity

### Envelope Constraint Formulation

Outer envelope: `g_outer(β, ωz, δf, Mz) ≤ 0`
Inner envelope: `g_inner(β, ωz) ≤ 0`

Constraints in NMPC optimization:
```python
# Check recoverability
if g_outer(current_state, control_inputs) > 0:
    # State outside recoverable envelope
    # Need to steer back toward saddle point
    
# Check normal stability (optional)
if g_inner(current_state) > 0:
    # Operating in drifting regime
    # Ensure outer envelope constraint active
```

## Implementation Considerations

### Computational Requirements
- NMPC requires real-time optimization
- Envelope checking adds computational overhead
- Hardware-in-the-loop testing essential
- Suitable solvers: qpOASES, ACADO, HPIPM

### Tuning Parameters
- Envelope boundary margins
- Control weight vs tracking weight
- Prediction horizon length
- Sample time for discretization

### Safety Margins
- Conservative envelope boundaries recommended
- Account for sensor noise and delays
- Consider model uncertainty
- Validate across operating conditions

## Research Paper Reference

**Paper**: "Dual-Envelope Constrained Nonlinear MPC for Distributed Drive Electric Vehicles Drifting Under Bounded Steering and Direct Yaw-Moment Control"
- **Authors**: Yurun Gan, Ziyu Song, Jing Yang, et al.
- **arXiv ID**: 2604.07342
- **Published**: April 8, 2026
- **Categories**: eess.SY (Systems and Control)
- **Link**: https://arxiv.org/abs/2604.07342

## Related Skills

- **control-systems**: General control systems theory
- **vehicle-dynamics**: Vehicle dynamics modeling
- **mpc-basics**: Fundamentals of MPC implementation
- **phase-plane-analysis**: Stability analysis techniques

## See Also

- Vehicle dynamics textbooks
- MPC implementation guides
- Tire modeling references
- Phase plane analysis tutorials