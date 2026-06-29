---
name: diameter-truncated-operator-evolution
description: "Diameter-based operator truncation methodology for simulating out-of-equilibrium quantum systems, enabling efficient extraction of local correlation functions and transport properties"
---

# Diameter Truncated Operator Evolution

## Description
A method for simulating operator dynamics in out-of-equilibrium quantum systems using diameter-based truncation. Extends low-weight Pauli string truncation to diameter-based truncation, where operators are truncated based on the spatial region size they are supported on rather than the number of non-trivial Pauli terms. This leaner truncation protocol is physically well-motivated and allows efficient, accurate extraction of local correlation functions and transport properties.

## Activation Keywords
- diameter truncated operator evolution
- quantum operator dynamics simulation
- operator truncation protocol
- quantum correlation functions
- 直径截断算符演化
- out-of-equilibrium quantum simulation
- transport properties quantum
- 量子系统算符动力学模拟
- kicked Ising model simulation
- Heisenberg XXZ simulation

## Tools Used
- coding: Implement operator evolution and truncation algorithms in Python/Julia
- terminal: Run numerical simulations on quantum models

## Usage Patterns

### Pattern 1: Local Correlation Function Extraction
For computing two-point infinite-temperature correlation functions:
1. Initialize local operators on the lattice
2. Evolve under Hamiltonian dynamics
3. Truncate operators by diameter (spatial support size)
4. Extract correlation functions from truncated operator expansion

### Pattern 2: Transport Property Computation
For analyzing transport in quantum many-body systems:
1. Define current operators at lattice sites
2. Evolve using diameter-truncated protocol
3. Compute transport coefficients from time-dependent correlations
4. Validate against known limits (ballistic, diffusive)

### Pattern 3: Generic Circuit Analysis
For analyzing dynamics of generic quantum circuits:
1. Map circuit to operator evolution problem
2. Apply diameter truncation at each timestep
3. Track operator growth via diameter distribution
4. Extract dynamical quantities of interest

## Instructions for Agents

### Step 1: System Setup
Define the quantum system:
- Lattice geometry (1D chain, 2D grid, etc.)
- Hamiltonian (kicked Ising, Heisenberg XXZ, etc.)
- Initial operator (local observable, current operator, etc.)

### Step 2: Operator Expansion
Represent operators in Pauli string basis:
```
O(t) = Σ_P c_P(t) · P
```
where P are Pauli strings and c_P(t) are time-dependent coefficients.

### Step 3: Diameter-Based Truncation
At each timestep:
1. Compute diameter of each Pauli string (size of non-trivial support region)
2. Keep strings with diameter ≤ D_max
3. Discard strings with diameter > D_max
4. Renormalize remaining coefficients if needed

**Diameter definition**: The diameter of a Pauli string is the size of the minimal contiguous region containing all non-identity terms.

### Step 4: Time Evolution
Evolve using Trotter decomposition or exact exponentiation:
```
O(t + dt) = e^{iH·dt} O(t) e^{-iH·dt}
```
Apply diameter truncation after each evolution step.

### Step 5: Observable Extraction
Compute quantities of interest:
- Two-point correlations: ⟨O_A(t) O_B(0)⟩
- Transport coefficients from current-current correlations
- Out-of-time-order correlators (OTOCs) for scrambling analysis

## Mathematical Framework

### Diameter vs Weight Truncation
Traditional weight truncation keeps Pauli strings with ≤ k non-trivial terms. Diameter truncation keeps strings supported on regions of size ≤ D.

**Advantage of diameter truncation:**
- More physically motivated (locality of interactions)
- Leaner protocol (fewer strings to track for same accuracy)
- Better scaling for lattice models with local Hamiltonians

### Error Bounds
For generic circuits with local interactions, the truncation error scales as:
```
ε(D_max) ≤ C · exp(-α · D_max)
```
where α depends on the interaction range and C on the initial operator.

### Kicked Ising Model
```
H = Σ_i J Z_i Z_{i+1} + h Σ_i X_i
```
with periodic kicks. Diameter truncation efficiently captures correlation spreading.

### Heisenberg XXZ Model
```
H = Σ_i [J (X_i X_{i+1} + Y_i Y_{i+1}) + Δ Z_i Z_{i+1}]
```
Diameter truncation captures spin transport properties accurately.

## Error Handling

### Truncation Error Accumulation
If error accumulates over long evolution times:
- Increase D_max adaptively based on error estimates
- Use extrapolation from multiple D_max values
- Monitor conservation laws (energy, magnetization)

### Operator Growth
If operators grow beyond truncation threshold too quickly:
- Reduce timestep dt for finer resolution
- Use adaptive D_max based on operator diameter distribution
- Switch to weight-based truncation for comparison

### Numerical Stability
If coefficients become numerically unstable:
- Use higher precision arithmetic (float128)
- Implement coefficient thresholding (discard |c_P| < ε)
- Apply QR decomposition for orthogonalization

## Examples

### Example 1: Kicked Ising Correlation Function
```python
# Initialize Z_0 operator on 1D chain
# Evolve under kicked Ising Hamiltonian
# Truncate at diameter D_max = 10
# Compute ⟨Z_0(t) Z_r(0)⟩ for various r
```

### Example 2: Heisenberg XXZ Transport
```python
# Initialize current operator J = Σ_i (X_i Y_{i+1} - Y_i X_{i+1})
# Evolve under XXZ Hamiltonian
# Truncate at diameter D_max = 15
# Extract Drude weight from long-time current autocorrelation
```

## Resources
- arXiv: 2606.28313 - Diameter truncated operator evolution
- Low-weight operator truncation literature
- Quantum many-body dynamics simulation methods
