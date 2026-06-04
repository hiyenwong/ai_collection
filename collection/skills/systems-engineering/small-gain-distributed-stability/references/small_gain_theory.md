# Small-Gain Theory: Detailed Proofs and Computations

## Mathematical Foundations

### Input-to-State Stability (ISS)
System `dx/dt = f(x,u)` is ISS if:
``|x(t)| ≤ β(|x(0)|, t) + γ(|u|_∞)``

where:
- β: class KL function (decay)
- γ: class K function (gain)

### Incremental ISS (i-ISS)
Two trajectories x(t), x'(t) under inputs u, u':
``|x(t) - x'(t)| ≤ β(|x(0)-x'(0)|, t) + γ(|u-u'|_∞)``

### i-IOSS Extension
Include output differences:
``|x(t) - x'(t)| ≤ β(|x(0)-x'(0)|, t) + γ(|u-u'|_∞) + δ(|y-y'|_∞)``

**Detectability:** State differences bounded by output differences.

## Exponential i-IOSS

### Definition
System is exponentially i-IOSS if β is exponential:
``β(r,t) = K e^{-λt} r``

with λ > 0 (decay rate), K ≥ 1.

### Local Condition
For subsystem i with dynamics:
``x_i(t+1) = f_i(x_i, w_i, u_i)``
``y_i(t) = h_i(x_i)``

Exponential i-IOSS condition:
``|x_i(t) - x_i'(t)| ≤ K_i e^{-λ_i t} |x_i(0) - x_i'(0)| + γ_i |w_i - w_i'|_∞ + δ_i |u_i - u_i'|_∞ + ε_i |y_i - y_i'|_∞``

## Gain Computation

### Linear Subsystems
For linear system:
``x_i(t+1) = A_i x_i(t) + B_i w_i(t) + D_i u_i(t)``
``y_i(t) = C_i x_i(t)``

**i-IOSS gains:**
- γ_i = ||B_i|| · ||A_i^{-1}|| (interconnection gain)
- δ_i = ||D_i|| · ||A_i^{-1}|| (input gain)
- ε_i = ||C_i|| · ||A_i^{-1}|| (output gain)

provided A_i is stable (eigenvalues inside unit circle).

### Decay Rate
``λ_i = -ln(max |eig(A_i)|)``

### Nonlinear Subsystems
Use linearization or contraction theory:
``γ_i = sup ||∂f_i/∂w_i||``

computed via optimization.

## Interconnection Structure

### Network Topology
Let subsystems be nodes in graph G:
- Edges (i,j): subsystem i receives input from subsystem j
- w_i = Σ_{j∈N(i)} w_{ij}(x_j)

### Interconnection Gains
**Gain from j to i:**
``γ_{ij} = sup_{x_j} ||∂w_i/∂x_j||``

**Interconnection matrix:**
``Γ = [γ_{ij}]_{N×N}``

### Gain Composition
Signal flow: x_j → w_{ij} → x_i → w_{ki} → x_k

**Total gain from j to k:**
``γ_{kj} = Σ_{paths} γ_{k,i} γ_{i,j} ...``

## Small-Gain Theorem Proof

### Setup
Assume each subsystem i is exponentially i-IOSS:
``|x_i(t) - x_i'(t)| ≤ K_i e^{-λ_i t} |x_i(0) - x_i'(0)| + γ_i |w_i - w_i'|_∞ + δ_i |u_i - u_i'|_∞ + ε_i |y_i - y_i'|_∞``

### Interconnection Constraint
``|w_i - w_i'|_∞ ≤ Σ_j γ_{ij} |x_j - x_j'|_∞``

### Fixed-Point Argument
Define operator T on trajectory differences:
``T(Δx) = β(Δx(0), t) + γ(Γ Δx) + δ(Δu) + ε(Δy)``

where Δx = [|x_1 - x_1'|, ..., |x_N - x_N'|]^T.

### Contraction of T
Show T is contracting:
``||T(Δx) - T(Δx')|| ≤ α ||Δx - Δx'||``
with α < 1.

**Condition:**
``α = max_i (γ_i Σ_j γ_{ij}) < 1``
→ small-gain condition.

### Banach Fixed-Point
T has unique fixed-point Δx* (global trajectory difference).

**Stability:**
``||Δx(t)|| ≤ ||Δx*|| ≤ γ_global ||Δu|| + δ_global ||Δy||``

**Exponential decay:**
``||Δx(t)|| ≤ K_global e^{-λ_global t} ||Δx(0)|| + ...``

## Lyapunov Characterization

### Local Storage Functions
For subsystem i, define:
``V_i(x_i, x_i') = (x_i - x_i')^T P_i (x_i - x_i')``
``P_i > 0 (positive definite)``

**i-IOSS condition:**
``V_i(t+1) ≤ e^{-2λ_i} V_i(t) + γ_i^2 |w_i - w_i'|^2 + δ_i^2 |u_i - u_i'|^2 + ε_i^2 |y_i - y_i'|^2``

### LMI Equivalent
Linear case (A_i, B_i, C_i, D_i):
``[e^{-2λ_i} P_i - A_i^T P_i A_i,   A_i^T P_i B_i,  A_i^T P_i D_i,  A_i^T P_i C_i] ≥ 0``
``[B_i^T P_i A_i,                   γ_i^2 - B_i^T P_i B_i,  ...]``

Solve for P_i, λ_i, γ_i, δ_i, ε_i.

### Global Lyapunov
Weighted sum of local functions:
``V(x,x') = Σ_i α_i V_i(x_i, x_i')``
``α_i > 0 (weights)``

**Derivation:**
``dV/dt = Σ_i α_i dV_i/dt``
``≤ Σ_i α_i (-2λ_i V_i + γ_i^2 Σ_j γ_{ij}^2 V_j + δ_i^2 |Δu|^2 + ε_i^2 |Δy|^2)``

**Small-gain condition:**
Choose α_i such that:
``Σ_i α_i γ_i^2 γ_{ij}^2 < α_j λ_j``

(ensures overall decay)

### Gain Selection
From Perron-Frobenius theorem:
If Γ is irreducible and ρ(Γ) < 1, then positive eigenvector v exists:
``Γ v = ρ(Γ) v``

Set α_i = v_i (ensures positivity).

**Global decay rate:**
``λ_global = min_i (λ_i (1 - ρ(Γ)))``

## Quantitative Comparison

### Example: 3-Subsystem Network
Subsystems:
- A_1: stable, λ_1 = 0.1, γ_1 = 0.5
- A_2: stable, λ_2 = 0.15, γ_2 = 0.4
- A_3: stable, λ_3 = 0.12, γ_3 = 0.45

Interconnection matrix:
``Γ = [[0, 0.3, 0.2],
      [0.2, 0, 0.1],
      [0.15, 0.25, 0]]``

**Small-gain analysis:**
- ρ(Γ) = 0.28
- λ_global = 0.1 · (1 - 0.28) = 0.072
- γ_global = 0.5 / (1 - 0.28) = 0.69

**Centralized LMI:**
- Solve for P_global
- λ_centralized = 0.08
- γ_centralized = 0.55

**Comparison:**
Small-gain more conservative (lower λ, higher γ) but tractable for large N.

## Numerical Examples

### Example 1: Power Network
- 10 generators (subsystems)
- Local dynamics: swing equation
- Interconnection: transmission lines

**Small-gain:**
- Compute local γ_i from linearized dynamics
- Γ from line impedances
- ρ(Γ) = 0.72
- Verify: ρ(Γ) < 1 → global stability

**LMI:**
- Local P_i, λ_i, γ_i
- Global verification: 10×10 system tractable

### Example 2: Multi-Agent Formation
- 5 agents (subsystems)
- Dynamics: double integrator
- Interconnection: relative position feedback

**Small-gain:**
- γ_i = ||K_i|| (feedback gain)
- Γ from topology (chain: 1-2-3-4-5)
- ρ(Γ) = 0.85
- Stability verified

## Implementation Tips

### Gain Computation
- Linear: analytical formula
- Nonlinear: optimization (sup ||∂f/∂w||)
- Robust: worst-case gain over uncertainties

### Spectral Radius
- Use eigenvalue solver
- Perron-Frobenius: check irreducibility
- Numerical stability: normalize Γ

### LMI Solving
- CVXPY with SCS or MOSEK
- Decomposition: solve subsystem LMIs separately
- Validation: verify positive definiteness

### Verification
- Simulate perturbed trajectories
- Check convergence rate empirically
- Compare with theoretical predictions