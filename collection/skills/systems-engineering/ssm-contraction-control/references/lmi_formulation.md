# LMI Formulation for SSM Controller Design

## Contraction Theory Preliminaries

### Incremental Stability
System `dx/dt = f(x, u)` is contracting if:
```
∂f/∂x + (∂f/∂x)^T ≤ -λ I  (λ > 0)
```

implies exponential convergence of all trajectories.

### Discrete-Time Extension
For discrete-time system `x_{t+1} = f(x_t)`, contraction condition:
```
f(x) - f(y) ≤ α |x - y|  (α < 1)
```

equivalent to:
```
∂f/∂x^T M ∂f/∂x - M < 0
```

## SSM Structure

### Linear Time-Invariant SSM
```
h_{t+1} = A h_t + B x_t + K (y_t - C h_t)
y_t = C h_t
```

with continuous-time hidden dynamics:
```
dh/dt = A_c h + B_c x
```

### Controllability Matrix
```
C_ctrb = [B, AB, A²B, ..., A^{n-1}B]
```

Controllable iff rank(C_ctrb) = n (full state dimension).

### Observability Matrix
```
C_obs = [C^T, A^T C^T, ..., (A^T)^{n-1} C^T]
```

Observable iff rank(C_obs) = n.

## Controller LMI

### Problem Formulation
Find K such that closed-loop system is contracting:
```
h_{t+1} = (A + BK) h_t
```

### Contraction Condition
```
(A + BK)^T M (A + BK) - M ≤ -Q
```

where:
- M > 0: contraction metric
- Q > 0: convergence rate matrix

### LMI Variables
- M (n × n, symmetric positive definite)
- K (m × n, feedback gain)
- Y (m × n, Y = KM)

### LMI Constraints
```
[ M            (A M + B Y)^T ]
[ A M + B Y    M            ] > 0
```

and:
```
M > ε I  (ε > 0)
```

### Solver Implementation
```python
import cvxpy as cp

# Variables
M = cp.Variable((n, n), symmetric=True)
Y = cp.Variable((m, n))

# Constraints
constraints = [
    M >> eps * np.eye(n),  # M > 0
    cp.bmat([[M, (A @ M + B @ Y).T],
             [A @ M + B @ Y, M]]) >> 0
]

# Objective: minimize contraction rate (optional)
objective = cp.Minimize(cp.trace(Q @ M))

# Solve
problem = cp.Problem(objective, constraints)
problem.solve()

# Extract K
K = Y.value @ np.linalg.inv(M.value)
```

## Observer LMI

### Problem Formulation
Find L such that observer is contracting:
```
ĥ_{t+1} = A ĥ_t + B x_t + L (y_t - C ĥ_t)
```

### Observer Dynamics
```
ĥ_{t+1} = (A - LC) ĥ_t + B x_t + L y_t
```

estimation error:
```
e_{t+1} = (A - LC) e_t
```

### Contraction Condition
```
(A - LC)^T M (A - LC) - M ≤ -Q
```

### LMI Formulation
```
[ M            (A M - Y C)^T ]
[ A M - Y C    M            ] > 0
```

where Y = LM.

### Solver Implementation
```python
# Variables
M_obs = cp.Variable((n, n), symmetric=True)
Y_obs = cp.Variable((n, p))

# Constraints
constraints = [
    M_obs >> eps * np.eye(n),
    cp.bmat([[M_obs, (A @ M_obs - Y_obs @ C).T],
             [A @ M_obs - Y_obs @ C, M_obs]]) >> 0
]

# Solve
problem = cp.Problem(objective, constraints)
problem.solve()

# Extract L
L = np.linalg.inv(M_obs.value) @ Y_obs.value
```

## Separation Principle

### Combined System
State + estimation error dynamics:
```
[x_{t+1}    ] = [A + BK     0     ] [x_t    ] + [B  ] u_t
[e_{t+1}    ]   [0          A - LC] [e_t    ]   [0  ]
```

### Stability Condition
Both A+BK and A-LC contracting → combined system contracting.

**Proof:**
Block-diagonal contraction metric:
```
M_comb = [M_ctrb   0    ]
         [0        M_obs]
```

satisfies contraction condition:
```
(A_comb)^T M_comb A_comb - M_comb = [
  (A+BK)^T M_ctrb (A+BK) - M_ctrb,  0
  0,                                (A-LC)^T M_obs (A-LC) - M_obs
] < 0
```

### Output Feedback Law
```
u_t = K ĥ_t = K (x_t - e_t)
```

Closed-loop dynamics:
```
x_{t+1} = (A + BK) x_t - BK e_t
```

Estimation error converges exponentially → asymptotic tracking.

## Scalable Decomposition

### Large-Scale SSM
Decompose into subsystems:
```
h_i ∈ ℝ^{n_i},  Σ n_i = n
```

### Interconnection Structure
```
h_{i,t+1} = A_i h_{i,t} + Σ_{j≠i} A_ij h_{j,t} + B_i u_i
```

### Local LMI
For each subsystem i:
```
(A_i + B_i K_i)^T M_i (A_i + B_i K_i) - M_i ≤ -Q_i
```

+ interconnection condition:
```
Σ_{j≠i} ||A_ij|| ≤ γ_i  (small-gain)
```

### Aggregate Contraction
If all subsystems contracting + small-gain condition:
```
Σ γ_i < 1
```

→ overall system contracting.

## Implementation Notes

### Solver Selection
- CVXPY with SCS or MOSEK backend
- SDP solvers for large n: use decomposition
- Guaranteed convergence for convex LMIs

### Numerical Issues
- Scale M: normalize to trace(M) = n
- Regularize: add εI to avoid singularity
- Check rank conditions before solving

### Validation
1. Verify M > 0 (check eigenvalues)
2. Compute contraction rate: λ = min(eig(Q))/max(eig(M))
3. Simulate: test closed-loop response
4. Robustness: perturb parameters, verify stability