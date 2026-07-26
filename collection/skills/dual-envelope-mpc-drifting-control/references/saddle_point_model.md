# Saddle Point Coordinate Model

## Mathematical Framework

### Vehicle Dynamics Model

**State variables:**
```
x = [Vx, Vy, r]^T  (or equivalently [Vx, β, r]^T)
where:
  Vx = longitudinal velocity
  Vy = lateral velocity  
  r = yaw rate
  β = atan(Vy/Vx) = sideslip angle
```

**Control variables:**
```
u = [δf, Mz]^T
where:
  δf = front wheel steering angle
  Mz = additional yaw moment (from distributed drive)
```

### Nonlinear Tire Model

**Pacejka Magic Formula:**
```
F_y = D * sin(C * atan(B * α - E * (B * α - atan(B * α))))
where:
  F_y = lateral force
  α = slip angle = atan(Vy_wheel / Vx_wheel)
  B, C, D, E = tire parameters
```

**Combined slip (longitudinal + lateral):**
```
When |α| > α_sat, tire force saturates
F_y_max = μ * F_z  (road adhesion limit)
```

### Handling Diagram

**Saddle point conditions:**
```
Equilibrium equations:
  m * Vx * (dβ/dt + r) = F_yf + F_yr  (lateral force balance)
  I_z * (dr/dt) = a * F_yf - b * F_yr + Mz  (yaw moment balance)

At saddle point:
  dβ/dt = 0, dr/dt = 0
  
This gives:
  Vx * r = (F_yf + F_yr) / m
  a * F_yf - b * F_yr + Mz = I_z * 0
```

**Saddle point location depends on:**
1. Road adhesion coefficient μ
2. Longitudinal velocity Vx
3. Front steering angle δf
4. Additional yaw moment Mz

### Phase Plane Analysis

**Phase plane coordinates: (β, r)**

```
Characteristic regions:
  - Stable equilibria: β and r converge to steady state
  - Unstable equilibria (saddle): Trajectories diverge
  - Saddle point: Junction between stable and unstable manifolds
```

**Stability boundaries:**
```
Stable manifold: Trajectories that converge to saddle
Unstable manifold: Trajectories that diverge from saddle

The saddle point is surrounded by:
  - Basins of attraction (stable regions)
  - Divergent regions (unstable regions)
```

## Saddle Point Computation

### Algorithm

```python
def find_saddle_point(mu, Vx, delta_f_range, Mz_range):
    """
    Find saddle point location for given parameters.
    
    Returns: (β_saddle, r_saddle, delta_f_eq, Mz_eq)
    """
    # 1. Compute handling diagram for given μ and Vx
    equilibria = compute_handling_diagram(mu, Vx)
    
    # 2. Identify saddle points (unstable equilibria)
    saddle_points = []
    for eq in equilibria:
        if is_unstable_equilibrium(eq):
            saddle_points.append(eq)
    
    # 3. Find saddle point reachable with bounded controls
    for saddle in saddle_points:
        # Check if saddle can be maintained with δf ∈ [min, max], Mz ∈ [min, max]
        delta_f_req = compute_required_steering(saddle)
        Mz_req = compute_required_yaw_moment(saddle)
        
        if delta_f_min <= delta_f_req <= delta_f_max and \
           Mz_min <= Mz_req <= Mz_max:
            return saddle
    
    return None  # No reachable saddle point
```

### Handling Diagram Construction

```python
def compute_handling_diagram(mu, Vx):
    """
    Compute handling diagram showing all equilibria.
    
    Handling diagram plots:
      - Yaw rate r vs sideslip angle β for steady-state conditions
      - Shows stable and unstable branches
      - Saddle points at junction points
    """
    equilibria = []
    
    # Sweep through possible β values
    for beta in np.linspace(-30, 30, 100):  # degrees
        for delta_f in np.linspace(-30, 30, 100):
            # Compute steady-state r for given β and δf
            r_ss = compute_steady_state_yaw_rate(mu, Vx, beta, delta_f)
            
            # Check stability (eigenvalues of linearized system)
            eig = compute_linearized_eigenvalues(mu, Vx, beta, r_ss, delta_f)
            
            stability = classify_stability(eig)
            
            equilibria.append({
                'beta': beta,
                'r': r_ss,
                'delta_f': delta_f,
                'stability': stability
            })
    
    return equilibria
```

## Key Equations

### Equilibrium Conditions

**Lateral force balance:**
```
m * Vx * r = F_yf(αf, μ) + F_yr(αr, μ)

Slip angles:
  αf = β + a*r/Vx - δf
  αr = β - b*r/Vx
```

**Yaw moment balance:**
```
I_z * 0 = a * F_yf - b * F_yr + Mz
```

### Tire Force Saturation

**Saturation condition:**
```
|F_y| > μ * F_z  → saturated

When saturated:
  F_y = sign(α) * μ * F_z
```

**Saturation boundaries:**
```
Front tire saturation: αf_sat = F_zf / (μ * C_f)
Rear tire saturation: αr_sat = F_zr / (μ * C_r)

where C_f, C_r are cornering stiffnesses
```

## Parameter Dependence

### Road Adhesion (μ)

- Higher μ → larger stable region, higher achievable drift angles
- Lower μ → smaller envelope, reduced control authority
- Saddle point shifts with μ

### Velocity (Vx)

- Higher Vx → larger achievable drift angles
- Lower Vx → smaller envelope, reduced stability margins
- Critical velocity exists where drift becomes impossible

### Steering Angle (δf)

- Limited steering range constrains reachable equilibria
- Steering saturation defines envelope boundary
- δf bounds affect recoverable region

### Yaw Moment (Mz)

- Additional yaw moment extends control authority
- Enables reaching otherwise unreachable equilibria
- Mz bounds define envelope boundary

## References

1. Pacejka, H.B. "Tire and Vehicle Dynamics" (3rd ed.)
2. Hindiyeh, R.Y. "Dynamics and Control of Drifting Automobiles"
3. Velenis, E. "Drift Control in Autonomous Vehicles"