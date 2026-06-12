---
name: reduced-basis-quantum-ode-solver
description: Reduced Basis Algorithm (RBA) methodology for solving polynomial nonlinear ODEs and spatially discretized PDEs on quantum computers. Uses monomial basis composition to lift nonlinear dynamics into linear quantum-accessible operators with logarithmic qubit scaling in grid size. arXiv: 2606.13457
category: quantum/mathematics
metadata:
  arxiv_id: "2606.13457"
  authors: "Monica Lăcătuş, Matthias Möller, Sauro Succi"
  subjects: "math.NA, quant-ph"
  published_date: "2026-06-11"
---

## Context

Quantum computing excels at linear evolution (Schrödinger equation) but struggles with nonlinear differential equations since quantum evolution is intrinsically linear. The Reduced Basis Algorithm (RBA) bridges this gap by lifting polynomial nonlinear ODEs/PDEs into linear operators acting on an expanded monomial basis, enabling exact recovery of discrete-time nonlinear dynamics on quantum hardware.

## Core Methodology

1. **Time Discretization**: Discretize the polynomial nonlinear ODE/PDE system with a chosen time-stepping scheme (e.g., forward Euler, Runge-Kutta). The discrete update map becomes a polynomial function of the state variables.

2. **Monomial Basis Composition**: Compose the polynomial update map over `m` timesteps. This produces a higher-degree polynomial in the original variables.

3. **Reduced Monomial Basis Identification**: Identify the minimal set of monomials that appear in the composed map. This is the "reduced basis" — a subset of the full monomial basis that actually contributes to the dynamics.

4. **Linear RBA Operator Construction**: Construct a linear operator `A_RBA` acting on the vector of reduced monomials. The action of `A_RBA` on the monomial vector exactly reproduces the `m`-step nonlinear dynamics.

5. **Quantum Encoding**: Encode the linear RBA operator into a quantum-accessible format (block-encoding or Pauli decomposition). The qubit requirement is governed by the reduced monomial basis size.

6. **Classical Preprocessing + Quantum Execution**: Move the computational burden of basis construction and operator assembly to a classical preprocessing step. The quantum computer executes the linear evolution on the encoded state.

## Implementation Steps

### Step 1: System Representation
For an `n`-dimensional polynomial ODE system of degree `d`:
```
dx/dt = f(x) where f is polynomial of degree d
```
After time discretization with step `Δt`:
```
x_{k+1} = g(x_k) where g is a polynomial map
```

### Step 2: Monomial Basis Construction
- Full monomial basis for degree `d` in `n` dimensions has size `C(n+d, d)`
- Composing `m` timesteps increases effective degree to `d^m`
- Reduced basis size: `|B_reduced| ≤ C(n+d^m, d^m)` (often much smaller due to sparsity)

### Step 3: RBA Operator Assembly
```python
# Pseudocode for RBA operator construction
def construct_rba_operator(f, m, delta_t):
    # f: polynomial vector field
    # m: number of timesteps to compose
    # delta_t: time step size
    
    # 1. Compose polynomial map m times
    g = compose_polynomial(f, m, delta_t)
    
    # 2. Identify monomials in composed map
    monomial_basis = identify_reduced_monomials(g)
    
    # 3. Build linear operator on monomial basis
    A_RBA = build_linear_operator(g, monomial_basis)
    
    return A_RBA, monomial_basis
```

### Step 4: Qubit Complexity Analysis
- **Full basis scenario**: `(n+d^m)`-dimensional lifted register
- **PDE on N grid points** (locality-based): `O(N^d_local * log N)` qubits where `d_local` is local interaction degree
- **Key insight**: Grid size dependence remains **logarithmic**, nonlinear overhead controlled by local reduced basis size

### Step 5: Trade-off Management
- **Timestep composition (m)**: Larger `m` → fewer quantum calls but exponential basis growth
- **Locality**: For spatially discretized PDEs, exploit local interaction structure to limit basis expansion
- **Accuracy**: No additional approximation error beyond time discretization error

## Pitfalls

- **Basis Explosion**: Composing many timesteps (`m` large) causes exponential growth in reduced monomial basis size. **Fix**: Use moderate `m` and compose iteratively.
- **Non-Polynomial Systems**: RBA applies only to polynomial nonlinearities. For non-polynomial systems, use polynomial approximation (Taylor series, spectral methods) first.
- **Classical Bottleneck**: The preprocessing step (basis identification, operator construction) can dominate total runtime for large systems. **Fix**: Exploit sparsity and locality patterns.
- **Condition Number**: The RBA operator may be ill-conditioned for stiff systems. **Fix**: Combine with preconditioning techniques (see `pauli-structured-preconditioning-qls` skill).
- **Verification**: Always verify RBA output against classical nonlinear solver on small test cases before deploying on quantum hardware.

## Verification

1. **Lorenz System Test**: Reproduce known chaotic dynamics of the Lorenz system using RBA. Compare trajectory against classical RK4 solver.
2. **Burgers Equation Test**: Solve 1D Burgers equation with RBA. Verify shock formation and propagation match analytical/numerical benchmarks.
3. **Basis Size Validation**: Check that the reduced monomial basis size is significantly smaller than the full basis `C(n+d^m, d^m)` for sparse systems.
4. **Error Bound**: Verify that the only error source is time discretization — RBA should reproduce the discrete-time map exactly.

## Activation

reduced basis algorithm, quantum ODE solver, quantum PDE solver, nonlinear differential equations quantum, monomial basis lifting, polynomial nonlinear quantum, RBA quantum computing, Lorenz system quantum, Burgers equation quantum
