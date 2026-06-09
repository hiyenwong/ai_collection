# Phase Plane Envelope Theory

## Overview

Phase plane envelopes define boundaries in the (β, r) state space that characterize:
1. **Recoverable regions:** States that can be driven back to stability
2. **Unrecoverable regions:** States that inevitably diverge
3. **Drift stability regions:** States where sustained drift is possible

## Envelope Definitions

### Outer Envelope (Safety Envelope)

**Definition:** The set of states from which there exists at least one control trajectory that converges to a stable equilibrium.

**Construction principle:**
```
1. Start from saddle point
2. Simulate backward trajectories using all possible control combinations
3. Boundary = states that barely converge (edge of recoverability)
4. Outer envelope = union of all convergent initial states
```

**Mathematical characterization:**
```
Outer envelope boundary: ∂Ω_outer

For state (β, r) ∈ ∂Ω_outer:
  ∃ u(t) ∈ U_bounds such that trajectory converges to saddle point
  
where U_bounds = {δf ∈ [δf_min, δf_max], Mz ∈ [Mz_min, Mz_max]}
```

### Inner Envelope (Stability Envelope)

**Definition:** The region where tire forces remain unsaturated, representing normal driving stability.

**Construction principle:**
```
1. Determine tire saturation boundaries
2. Find states where |F_yf| < μ*F_zf and |F_yr| < μ*F_zr
3. Inner envelope = unsaturated tire force region
```

**Mathematical characterization:**
```
Inner envelope boundary: ∂Ω_inner

For state (β, r) ∈ Ω_inner:
  |F_yf(β, r)| < μ * F_zf
  |F_yr(β, r)| < μ * F_zr
  
This ensures:
  - Linear tire behavior
  - Predictable vehicle response
  - Normal driving stability
```

## Envelope Relationships

```
Ω_inner ⊂ Ω_outer

Drift region: Ω_drift = Ω_outer \ _inner
  - States in drift region: saturated tires, but recoverable
  - Requires deliberate control to maintain drift
  - Boundary crossing: transition from normal driving to drift
```

## Envelope Construction Algorithm

### Step 1: Boundary Control Inputs

```python
def get_boundary_controls():
    """
    Return control input combinations at bounds.
    
    For envelope construction, need extreme controls:
      δf ∈ {δf_min, δf_max}
      Mz ∈ {Mz_min, Mz_max}
    
    Total: 4 combinations
    """
    return [
        (delta_f_min, Mz_min),
        (delta_f_min, Mz_max),
        (delta_f_max, Mz_min),
        (delta_f_max, Mz_max)
    ]
```

### Step 2: Backward Simulation

```python
def simulate_backward(saddle_point, control_pair, time_horizon):
    """
    Simulate backward from saddle point to find envelope boundary.
    
    Backward integration: simulate forward but with reversed time
    Starting from saddle point, find states that converge to it.
    """
    # Initialize at saddle point
    beta_saddle, r_saddle = saddle_point
    delta_f, Mz = control_pair
    
    # Backward integration
    trajectory = []
    state = [beta_saddle, r_saddle]
    
    for t in reversed_time_steps:
        # Compute dynamics
        d_state = compute_dynamics(state, delta_f, Mz)
        
        # Backward step (reverse sign)
        state = state - dt * d_state
        
        trajectory.append(state)
        
        # Stop if trajectory diverges significantly
        if diverged(state):
            break
    
    return trajectory
```

### Step 3: Envelope Extraction

```python
def extract_envelope(trajectories):
    """
    Extract envelope boundary from simulated trajectories.
    
    The envelope boundary is the "outermost" trajectory
    that still converges to the saddle point.
    """
    envelope_boundary = []
    
    # Collect all trajectory endpoints
    endpoints = [traj[-1] for traj in trajectories]
    
    # Convex hull of endpoints gives envelope boundary
    envelope_boundary = convex_hull(endpoints)
    
    return envelope_boundary
```

## Convergence Analysis

### Convergence Criteria

```python
def check_convergence(trajectory, saddle_point, tolerance):
    """
    Check if trajectory converges to saddle point.
    """
    beta_saddle, r_saddle = saddle_point
    
    final_state = trajectory[-1]
    beta_final, r_final = final_state
    
    # Check distance to saddle
    distance = sqrt((beta_final - beta_saddle)**2 + (r_final - r_saddle)**2)
    
    return distance < tolerance
```

### Divergence Detection

```python
def diverged(state, threshold):
    """
    Check if state has diverged beyond reasonable bounds.
    """
    beta, r = state
    
    # Thresholds for divergence
    beta_threshold = 45  # degrees (extreme sideslip)
    r_threshold = 90     # deg/s (extreme yaw rate)
    
    return abs(beta) > beta_threshold or abs(r) > r_threshold
```

## Envelope Properties

### Invariance

The outer envelope is a **controlled invariant set**:
```
If state x(t) ∈ Ω_outer, 
then ∃ control sequence u(t) such that x(t+1) ∈ Ω_outer

This ensures: Once inside envelope, can stay inside (safety guarantee)
```

### Reachability

The outer envelope defines the **reachable set** from saddle point:
```
Ω_outer = {x : saddle point reachable from x}

This defines: All states that can be recovered to stable drift
```

## Phase Plane Visualization

```
     r (yaw rate)
     ↑
     |    Unstable region
     |    (divergent)
     |  
     |    ────── Outer envelope
     |    
     |    ===== Inner envelope
     |    
     |    Saddle point (β_s, r_s)
     |       * ←
     |    
     |    ===== Inner envelope
     |    
     |    ────── Outer envelope
     |    
     |    Unstable region
     |
─────+──────────→ β (sideslip angle)
     |
```

## Coupling Effects

### Steering-Yaw Moment Coupling

When both δf and Mz are bounded, their coupling affects envelope shape:

```
δf and Mz act together to control:
  - Lateral force distribution (front/rear)
  - Yaw moment generation
  - Drift equilibrium location

Coupling can:
  - Extend envelope (reach more states)
  - Compress envelope (control authority limits)
```

### Extended Dual Envelope Framework

**Paper contribution: Accounts for coupling explicitly**

```
Instead of treating δf and Mz independently,
the extended framework considers:
  - How δf affects tire saturation
  - How Mz shifts saddle point location
  - Combined effect on envelope boundaries
```

## Practical Considerations

### Real-Time Construction

Envelopes can be computed offline for:
- Different μ values (friction conditions)
- Different Vx values (speed ranges)
- Different control bounds (actuator limits)

Store as lookup tables for real-time use.

### Adaptive Envelopes

For varying conditions:
```
μ estimation → update envelope
Vx tracking → interpolate between precomputed envelopes
Control bound changes → reconstruct envelope online
```

## References

1. Blanchini, F. "Set invariance in control"
2. Kolmanovsky, I. "Safety envelopes for vehicle control"
3. Bobba, K. "Reachability-based safety verification"