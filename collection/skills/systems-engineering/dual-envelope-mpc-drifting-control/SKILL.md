---
name: dual-envelope-mpc-drifting-control
description: "Dual-envelope constrained nonlinear MPC for autonomous drifting in distributed drive electric vehicles. Covers saddle point modeling, phase plane envelope construction, NMPC with envelope constraints, and extreme vehicle maneuver control. Use when working with: (1) vehicle dynamics control, (2) nonlinear MPC, (3) autonomous drifting, (4) distributed drive systems, (5) envelope-based safety constraints, or (6) yaw moment control for extreme maneuvers."
---

# Dual-Envelope Constrained NMPC for Autonomous Drifting

This skill provides methodology and implementation guidance for nonlinear model predictive control (NMPC) with dual-envelope constraints for autonomous drifting in distributed drive electric vehicles.

## Paper Reference

**Title:** Dual-Envelope Constrained Nonlinear MPC for Distributed Drive Electric Vehicles Drifting Under Bounded Steering and Direct Yaw-Moment Control

**Authors:** Yurun Gan, Ziyu Song, Jing Yang, Zheng Lin, Jianuo Zhang, Tongtong Gu, Haitao Ding, Nan Xu, Por Lip Yee, Wei Ni, Jun Luo

**arXiv:** 2604.07342 (April 8, 2026)

**PDF:** https://arxiv.org/pdf/2604.07342

## Core Concepts

### 1. Saddle Point Coordinate Model

The saddle point is the equilibrium in the phase plane where drift stability exists. Location depends on:
- Road adhesion coefficient (μ)
- Longitudinal velocity (Vx)
- Front wheel steering angle (δf)
- Additional yaw moment (Mz)

**Key equations:**

```
Phase plane coordinates: (β, r)
  β = sideslip angle
  r = yaw rate

Saddle point conditions:
  Fx = 0 (no longitudinal force at saddle)
  Saturation boundaries define reachable equilibria
```

### 2. Dual Envelope Framework

**Outer Envelope:** Recoverable set under bounded control inputs
- Defines states that can be driven back to stability
- Boundary: Convergence tendency toward saddle under max/min δf and Mz
- Accounts for coupling between steering and yaw moment

**Inner Envelope:** Non-drifting stability region
- States with unsaturated tire forces
- Normal driving stability region
- Smaller than outer envelope

**Envelope construction:**
```
1. Identify saddle point location for given parameters
2. Simulate state trajectories under bounded control inputs
3. Determine convergence/divergence boundaries
4. Construct outer envelope from recoverable state set
5. Inner envelope from unsaturated tire force region
```

### 3. NMPC Controller Design

**Objective function:**
```
J = Σ[k=0 to N] (||x_k - x_ref||²_Q + ||u_k - u_ref||²_R)
```

**Constraints:**
- Outer envelope: Safety constraint (keep within recoverable region)
- Inner envelope: Optional transition constraint (smooth entry to drift)
- Steering angle bounds: δf ∈ [δf_min, δf_max]
- Yaw moment bounds: Mz ∈ [Mz_min, Mz_max]

**State reference:**
```
x_ref = [Vx_ref, β_saddle, r_saddle, δf_ref, Mz_ref]
```

## Implementation Workflow

### Step 1: System Modeling

1. **Nonlinear tire model:** Pacejka magic formula or similar
2. **Vehicle dynamics:** 3-DOF bicycle model with yaw moment
3. **Handling diagram:** Construct for given μ and Vx
4. **Saddle point identification:** Solve equilibrium equations

See [references/saddle_point_model.md](references/saddle_point_model.md) for detailed equations.

### Step 2: Envelope Construction

```python
# Algorithm sketch
def construct_envelopes(mu, Vx, delta_f_range, Mz_range):
    # 1. Find saddle point
    saddle = find_saddle_point(mu, Vx)
    
    # 2. Simulate trajectories for boundary control inputs
    trajectories = []
    for delta_f in [delta_f_min, delta_f_max]:
        for Mz in [Mz_min, Mz_max]:
            traj = simulate_from_initial_states(delta_f, Mz)
            trajectories.append(traj)
    
    # 3. Determine outer envelope boundary
    outer_envelope = extract_convergence_boundary(trajectories)
    
    # 4. Determine inner envelope (unsaturated region)
    inner_envelope = find_unsaturated_boundary(mu, Vx)
    
    return outer_envelope, inner_envelope
```

See [scripts/envelope_construction.py](scripts/envelope_construction.py) for implementation.

### Step 3: NMPC Formulation

1. **Prediction horizon:** N steps (typically 20-50)
2. **State variables:** [Vx, β, r] or extended with controls
3. **Control variables:** [δf, Mz]
4. **Discretization:** Euler or Runge-Kutta integration
5. **Solver:** Sequential quadratic programming (SQP) or interior point

### Step 4: Hardware-in-the-Loop Testing

- Validate envelope boundaries
- Test controller tracking performance
- Evaluate robustness to friction mismatch
- Compare with unconstrained NMPC

## Performance Metrics

From the paper's HiL experiments:

**Tracking error reduction (compared to unconstrained NMPC):**
- Vehicle speed: 33.07%
- Sideslip angle: 71.18%
- Yaw rate: 31.27%

**Peak tracking error:** 63.66% reduction under friction mismatch

**Convergence:** Smoother convergence toward drift saddle point

## Applications

1. **Autonomous drifting:** Extreme vehicle maneuvers
2. **Emergency maneuvers:** Recoverable safety boundaries
3. **Racing applications:** High-speed vehicle control
4. **Drift training systems:** Guided drift entry/exit
5. **Vehicle stability systems:** Extended stability envelope

## Key Advantages

- **Safety guarantee:** Outer envelope ensures recoverability
- **Smooth transition:** Inner envelope guides drift entry
- **Robustness:** Handles friction mismatch effectively
- **Real-time capable:** NMPC with envelope constraints is computationally feasible

## Related Skills

- **physics-guided-neural-network:** For learning-based envelope approximation
- **control-systems-design:** General control system methodology
- **vehicle-dynamics:** Vehicle dynamics modeling

## References

- [saddle_point_model.md](references/saddle_point_model.md): Detailed mathematical model
- [envelope_theory.md](references/envelope_theory.md): Phase plane envelope theory
- [nmpc_formulation.md](references/nmpc_formulation.md): NMPC optimization formulation

## Tools Used

- **exec:** Run envelope construction scripts
- **read:** Load reference documentation
- **write:** Generate controller configuration files
- **edit:** Modify simulation parameters