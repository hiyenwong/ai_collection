# NMPC Formulation for Autonomous Drifting

## Optimization Problem

### Standard NMPC Formulation

**Objective:**
```
minimize J(x, u) = Σ[k=0 to N-1] l(x_k, u_k) + l_f(x_N)

where:
  l(x, u) = ||x - x_ref||²_Q + ||u - u_ref||²_R
  l_f(x) = ||x - x_ref||²_Q_f  (terminal cost)
  
x_ref = reference trajectory (drift steady-state)
u_ref = reference control (steady-state control)
```

**Constraints:**
```
Subject to:
  x_0 = x(t)                    (initial condition)
  x_{k+1} = f(x_k, u_k)        (dynamics)
  u_k ∈ U                      (control constraints)
  x_N ∈ X_f                    (terminal constraint)
  
Additional envelope constraints:
  x_k ∈ Ω_outer                (stay in recoverable region)
  optional: x_k ∈ Ω_inner      (smooth transition)
```

### Dual Envelope NMPC

**Enhanced formulation:**

```python
def nmpc_envelope_formulation():
    """
    NMPC with dual envelope constraints.
    """
    # Cost function
    J = 0
    for k in range(N):
        # Tracking error
        e_k = x_k - x_ref
        J += e_k.T @ Q @ e_k
        
        # Control effort
        delta_u_k = u_k - u_ref
        J += delta_u_k.T @ R @ delta_u_k
    
    # Terminal cost
    J += (x_N - x_ref).T @ Q_f @ (x_N - x_ref)
    
    # Constraints
    constraints = [
        # Dynamics
        x_{k+1} == f(x_k, u_k),
        
        # Control bounds
        delta_f_min <= u_k[0] <= delta_f_max,
        Mz_min <= u_k[1] <= Mz_max,
        
        # Outer envelope constraint (safety)
        in_outer_envelope(x_k),  # x_k ∈ Ω_outer
        
        # Optional: Inner envelope constraint (transition)
        # in_inner_envelope(x_k),  # x_k ∈ Ω_inner
        
        # Terminal constraint
        x_N near saddle_point,  # End near drift equilibrium
    ]
    
    return minimize(J, constraints)
```

## Discrete-Time Vehicle Model

### State Equations

**Continuous-time model:**
```
dx/dt = f(x, u)

where:
  x = [Vx, β, r]^T
  
  dVx/dt = -(F_yf*sin(δf) + F_yr*sin(β))/m + ...  (longitudinal)
  dβ/dt = (F_yf + F_yr)/(m*Vx) - r  (sideslip dynamics)
  dr/dt = (a*F_yf - b*F_yr + Mz)/I_z  (yaw dynamics)
```

**Discrete-time (Euler integration):**
```
x_{k+1} = x_k + dt * f(x_k, u_k)

or Runge-Kutta 4:
  x_{k+1} = x_k + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
  where:
    k1 = f(x_k, u_k)
    k2 = f(x_k + dt/2*k1, u_k)
    k3 = f(x_k + dt/2*k2, u_k)
    k4 = f(x_k + dt*k3, u_k)
```

### Tire Force Model

```python
def compute_tire_force(alpha, mu, F_z, tire_params):
    """
    Compute lateral tire force using Pacejka formula.
    
    alpha: slip angle (radians)
    mu: road adhesion coefficient
    F_z: vertical load
    tire_params: {B, C, D, E}
    """
    B, C, D, E = tire_params['B'], tire_params['C'], tire_params['D'], tire_params['E']
    
    # Pacejka magic formula
    alpha_rad = alpha * np.pi / 180  # degrees to radians
    F_y = D * np.sin(C * np.arctan(B * alpha_rad - E * (B * alpha_rad - np.arctan(B * alpha_rad))))
    
    # Saturation limit
    F_y_max = mu * F_z
    
    # Apply saturation
    F_y = np.clip(F_y, -F_y_max, F_y_max)
    
    return F_y
```

## Envelope Constraint Formulation

### Implicit Representation

**Method 1: Signed distance function**
```python
def in_outer_envelope(x):
    """
    Check if state x is in outer envelope.
    
    Use signed distance: d(x) < 0 means inside envelope
    """
    beta, r = x[1], x[2]
    
    # Compute signed distance to envelope boundary
    d = signed_distance_to_envelope(beta, r, outer_envelope_params)
    
    return d < 0  # constraint: inside envelope
```

**Method 2: Half-plane constraints**
```python
def in_outer_envelope(x):
    """
    Represent envelope as intersection of half-planes.
    
    Each boundary segment: a*β + b*r + c ≤ 0
    """
    beta, r = x[1], x[2]
    
    constraints = []
    for segment in envelope_boundary_segments:
        a, b, c = segment['a'], segment['b'], segment['c']
        constraints.append(a*beta + b*r + c <= 0)
    
    return all(constraints)
```

### Explicit Representation (Precomputed)

```python
def load_envelope_lookup(mu, Vx):
    """
    Load precomputed envelope boundaries from lookup table.
    
    For given (μ, Vx), return envelope boundary points.
    """
    # Interpolate between precomputed envelopes
    envelope = interpolate_envelope(mu, Vx, envelope_database)
    
    return envelope
```

## Reference Trajectory

### Saddle Point Reference

```python
def compute_drift_reference(saddle_point, Vx_ref):
    """
    Compute reference trajectory for drifting at saddle point.
    """
    beta_saddle, r_saddle = saddle_point
    
    # Steady-state reference
    x_ref = np.array([Vx_ref, beta_saddle, r_saddle])
    
    # Steady-state control (computed from equilibrium conditions)
    delta_f_eq, Mz_eq = solve_steady_state_control(beta_saddle, r_saddle, Vx_ref)
    u_ref = np.array([delta_f_eq, Mz_eq])
    
    return x_ref, u_ref
```

### Dynamic Reference (Entry/Exit)

```python
def compute_transition_reference(x_current, saddle_point):
    """
    Compute reference trajectory for transition to/from drift.
    """
    # Generate smooth trajectory from current state to saddle point
    # Could use: spline interpolation, optimal trajectory, etc.
    
    trajectory = generate_smooth_trajectory(x_current, saddle_point)
    
    return trajectory
```

## Solver Configuration

### Sequential Quadratic Programming (SQP)

```python
def configure_sqp_solver():
    """
    Configure SQP solver for NMPC.
    """
    solver_config = {
        'method': 'sqp',
        'max_iterations': 100,
        'tolerance': 1e-4,
        'line_search': 'backtracking',
        'hessian': 'bfgs',  # approximate Hessian
    }
    return solver_config
```

### Interior Point Method

```python
def configure_ip_solver():
    """
    Configure interior point solver.
    """
    solver_config = {
        'method': 'ipopt',
        'max_iterations': 200,
        'tolerance': 1e-6,
        'barrier_parameter': 0.1,
        'mu_strategy': 'adaptive',
    }
    return solver_config
```

## Real-Time Implementation

### Solver Warm-Start

```python
def warm_start_solver(previous_solution, current_state):
    """
    Use previous solution to warm-start current optimization.
    
    Shift previous solution by one step:
      u_opt_prev[1:] → initial guess for u_opt_current[:-1]
    """
    # Shift previous solution
    u_init_guess = np.roll(previous_solution['u'], -1)
    u_init_guess[-1] = previous_solution['u'][-1]  # repeat last control
    
    # Adjust for new initial state
    x_init = current_state
    
    return {'u_init': u_init_guess, 'x_init': x_init}
```

### Computation Time Budget

```python
def enforce_time_budget(max_solve_time):
    """
    Limit solver time for real-time execution.
    """
    # Typical: 10-50 ms solve time
    # Horizon: 20-50 steps
    # dt: 10-20 ms
    
    if solve_time > max_solve_time:
        # Return last successful solution or fallback
        return fallback_solution
    
    return optimal_solution
```

## Parameter Tuning

### Weight Matrices

```python
def tune_cost_weights():
    """
    Tune Q, R, Q_f weight matrices.
    """
    # State tracking weights
    Q = np.diag([
        1.0,   # Vx weight
        10.0,  # β weight (important for drift)
        5.0,   # r weight (important for yaw control)
    ])
    
    # Control effort weights
    R = np.diag([
        0.1,   # δf weight (steering effort)
        0.5,   # Mz weight (yaw moment effort)
    ])
    
    # Terminal cost weight
    Q_f = 2.0 * Q  # larger terminal cost
    
    return Q, R, Q_f
```

### Prediction Horizon

```
N = prediction horizon (number of steps)

Trade-off:
  - Larger N: Better prediction, longer solve time
  - Smaller N: Faster solve, shorter prediction
  
Recommended: N = 20-50 steps

horizon_time = N * dt
dt: sampling time (10-20 ms typical)
```

## Performance Metrics

### Tracking Accuracy

```python
def compute_tracking_error(x_actual, x_ref):
    """
    Compute RMS tracking error.
    """
    e = x_actual - x_ref
    
    rms_error = np.sqrt(np.mean(e**2))
    
    # Weighted by importance
    weighted_error = np.sqrt(np.mean((Q @ e)**2))
    
    return rms_error, weighted_error
```

### Convergence to Saddle

```python
def check_saddle_convergence(x_actual, saddle_point):
    """
    Check convergence to drift equilibrium.
    """
    beta_saddle, r_saddle = saddle_point
    beta_actual, r_actual = x_actual[1], x_actual[2]
    
    # Distance to saddle
    distance = np.sqrt((beta_actual - beta_saddle)**2 + (r_actual - r_saddle)**2)
    
    # Convergence rate
    convergence_rate = -d_distance/dt
    
    return distance, convergence_rate
```

## References

1. Rawlings, J.B. "Model Predictive Control: Theory and Design"
2. Borrelli, F. "Predictive Control for Linear and Hybrid Systems"
3. Kong, J. "Kinematic and dynamic vehicle models for autonomous driving control"