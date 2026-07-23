---
name: input-constrained-spatiotemporal-tubes
description: >
  Input-constrained spatiotemporal tube (STT) control framework for safe
  navigation of unknown Euler-Lagrange systems in dynamic environments.
  Provides finite-time reach-avoid-stay guarantees with explicit actuator
  constraint handling. Approximation-free and computationally efficient.
---

# Input-Constrained Spatiotemporal Tubes

## Context

Safe navigation in dynamic environments for autonomous systems (robots,
drones, spacecraft) where:
- System dynamics are unknown or partially known (Euler-Lagrange form)
- Actuator inputs are physically constrained (force, torque limits)
- Environment contains dynamic obstacles
- Formal safety guarantees are required

Existing methods (MPC, CBFs) either need accurate models, require online
optimization, or fail to explicitly handle input constraints.

Based on: Upadhyay, Das, Jagtap, "Input-Constrained Spatiotemporal Tubes
for Safe Navigation of Unknown Euler-Lagrange Systems in Dynamic Environments"
(arXiv:2607.08189, 2026)

## Core Methodology

### Spatiotemporal Tube (STT) Framework Extension

The STT framework creates a tube-shaped region in state space that the
system trajectory is guaranteed to stay within. This paper extends STT by:

1. **Incorporating input constraints** into controller design
2. **Offline-verifiable feasibility conditions** relating control authority
   to tube design and uncertainty bounds
3. **Approximation-free** design -- no linearization or discretization needed
4. **Computationally efficient** -- suitable for real-time implementation

### System Model

Unknown Euler-Lagrange system:
```
M(q)q_ddot + C(q,q_dot)q_dot + G(q) + d(t) = tau
```
where M is inertia matrix, C is Coriolis, G is gravity, d(t) is disturbance,
tau is control input subject to ||tau|| <= tau_max.

### Key Results

- **Finite-Time Reach-Avoid-Stay (FT-RAS)**: System reaches target,
  avoids obstacles, and stays in target set within finite time
- **Offline feasibility check**: Before deployment, verify that available
  control authority suffices for the tube design given uncertainty bounds
- **No online optimization**: Unlike MPC, all computations are closed-form

## Implementation Patterns

### Pattern 1: STT Controller Design

```python
class SpatiotemporalTubeController:
    def __init__(self, tube_params, uncertainty_bounds, input_limits):
        self.tube_center = tube_params['center_trajectory']
        self.tube_radius = tube_params['radius_function']
        self.uncertainty = uncertainty_bounds  # ||d(t)|| <= d_max
        self.tau_max = input_limits

    def verify_feasibility(self):
        """Offline check: control authority sufficient for tube design."""
        required_authority = self.tube_radius.derivative_max() + self.uncertainty
        return required_authority <= self.tau_max

    def compute_control(self, q, q_dot, t):
        """Closed-form control -- no optimization needed."""
        q_ref, q_dot_ref, q_ddot_ref = self.tube_center(t)
        e = q - q_ref
        e_dot = q_dot - q_dot_ref
        tau = self.control_law(e, e_dot, t)
        return saturate(tau, self.tau_max)
```

### Pattern 2: Dynamic Obstacle Avoidance

```python
def compute_avoidance_tube(obstacles, tube_radius):
    """Modify tube to avoid dynamic obstacles."""
    for obs in obstacles:
        safe_margin = obs.radius + safety_buffer
        if distance(tube_center, obs.center) < safe_margin + tube_radius:
            tube_center = repel(tube_center, obs.center)
    return tube_center, tube_radius
```

### Pattern 3: Uncertainty Compensation

```python
class AdaptiveCompensator:
    """Neural network compensator for unknown Euler-Lagrange dynamics."""
    def __init__(self, input_dim):
        self.nn = NeuralNetwork(input_dim)
        self.adaptation_rate = 0.1

    def update(self, tracking_error):
        transformed = bounded_transform(tracking_error)
        approximation = self.nn(transformed)
        self.nn.update(approximation, rate=self.adaptation_rate)
```

## Deployment Checklist

- [ ] Model system as Euler-Lagrange (or verify EL form applicability)
- [ ] Characterize actuator input limits (tau_max)
- [ ] Bound disturbance magnitude (||d(t)|| <= d_max)
- [ ] Design tube trajectory (center + radius functions)
- [ ] Verify offline feasibility: control authority > required authority
- [ ] Implement approximation-free control law with bounded transformation
- [ ] Test on simulation (mobile robot, quadrotor, or spacecraft)
- [ ] Validate hardware experiments with real sensor data

## Pitfalls

- **Ignoring input constraints**: Leads to infeasible commands, saturation,
  safety violations -- always verify offline feasibility first
- **Overly tight tube radius**: May not be achievable with available control
  authority -- balance precision vs. feasibility
- **Unbounded disturbance estimates**: If d_max is underestimated, guarantees
  fail -- use conservative bounds from physical analysis
- **Online optimization temptation**: The advantage of STT is being
  approximation-free and closed-form -- resist adding MPC layers

## Verification

- System must satisfy FT-RAS: reach target T, avoid obstacles O, stay in S
- Control input must never exceed tau_max (verify via saturation logging)
- Tracking error must remain within tube radius at all times
- Offline feasibility check must pass before deployment

## Activation

**Keywords**: spatiotemporal tube, safe navigation, euler-lagrange, input
constraints, reach-avoid-stay, unknown dynamics, approximation-free control,
real-time control, dynamic obstacles, actuator limits, mobile robot, quadrotor,
spacecraft, control barrier function alternative

**When to use**: When designing safe navigation controllers for robots/drones
with unknown dynamics and hard actuator limits, when MPC is too slow for
real-time, or when formal reach-avoid-stay guarantees are needed.
