---
name: quantum-economic-action-constant
description: "Quantum economics methodology using economic action constant (hbar_E) as structural analogue to Planck's constant for modeling macroeconomic regime transitions under radical uncertainty."
---

# Quantum Economic Action Constant

## Description
Methodology for modeling macroeconomic dynamics using an economic action constant (hbar_E) as the fundamental scale of irreducible uncertainty, derived through canonical quantization with non-commuting observables. Enables analysis of regime transitions between deterministic, probabilistic, and highly unstable economic dynamics.

## Activation Keywords
- quantum economics
- 量子经济学
- economic action constant
- hbar_E quantum economics
- macroeconomic regime transitions
- canonical quantization economics
- economic uncertainty modeling
- 经济作用量常数

## Tools Used
- terminal: Run numerical simulations, solve differential equations
- write_file: Create economic potential models
- read_file: Read economic time series data
- search_files: Locate economic datasets

## Usage Patterns

### Pattern 1: Regime Transition Analysis
When analyzing macroeconomic stability under uncertainty:
1. Define economic observables (X, P_X) as non-commuting operators
2. Estimate hbar_E from historical volatility and institutional stability metrics
3. Solve the economic Schrödinger equation for regime probabilities
4. Identify bifurcation points where dynamics become unstable

### Pattern 2: Double-Well Economic Potential
When modeling economies with two stable states (e.g., growth vs recession):
1. Construct double-well potential V(x) representing two economic equilibria
2. Compute tunneling rates between wells as function of hbar_E
3. Analyze spectral properties for early warning signals
4. Simulate harmonic modulation effects on regime stability

### Pattern 3: Semi-Classical Economic Analysis
When hbar_E → 0 (low uncertainty environment):
1. Apply WKB approximation for semi-classical solutions
2. Identify classical trajectories (deterministic economic paths)
3. Calculate quantum corrections for small but non-zero uncertainty
4. Derive policy implications for uncertainty reduction

## Instructions for Agents

### Step 1: Define Economic Observables
Identify the economic quantities to quantize:
```
X = economic state variable (GDP growth, inflation, etc.)
P_X = conjugate momentum (rate of change, policy response)
[X, P_X] = i * hbar_E  (non-commutation relation)
```

### Step 2: Construct Economic Hamiltonian
```
H = P_X²/(2m) + V(X)
```
where:
- m = economic inertia (resistance to change)
- V(X) = economic potential (stability landscape)
  - Single well: stable equilibrium
  - Double well: bistable regime (boom/bust)
  - Multi-well: complex economic dynamics

### Step 3: Derive Uncertainty Relations
```
ΔX · ΔP_X ≥ hbar_E/2
```
This bounds the precision of simultaneous economic measurement.

### Step 4: Estimate hbar_E from Data
1. Collect macroeconomic time series
2. Compute realized volatility and institutional stability indices
3. Fit the uncertainty relation to historical data
4. Calibrate hbar_E as function of policy environment

### Step 5: Numerical Simulation
1. Discretize the economic Schrödinger equation
2. Solve for eigenstates and eigenvalues
3. Simulate time evolution under parameter changes
4. Identify critical hbar_E values where regime transitions occur

## Error Handling

### Data Quality Issues
If economic data is noisy or incomplete:
- Apply Kalman filtering for state estimation
- Use Bayesian inference for hbar_E estimation
- Incorporate agent-based simulation priors

### Model Complexity
If full quantum treatment is computationally infeasible:
- Use semi-classical approximation (WKB)
- Apply mean-field theory for multi-agent systems
- Reduce dimensionality via principal component analysis

### Interpretation Ambiguity
When mapping quantum formalism to economics:
- Ensure economic observables have clear operational definitions
- Validate against established economic theory
- Cross-check with classical economic models as limiting case

## Examples

### Example 1: Post-War Reconstruction Dynamics
```python
import numpy as np
from scipy.linalg import eigh

# Double-well economic potential
def V(x, a=1.0, b=0.5):
    return a * x**4 - b * x**2  # Growth vs recession equilibria

# Hamiltonian matrix in position basis
N = 100  # grid points
x = np.linspace(-2, 2, N)
dx = x[1] - x[0]
hbar_E = 0.1  # low uncertainty (post-war institutional stability)

# Kinetic energy (discrete Laplacian)
T = -hbar_E**2 / (2 * dx**2) * (np.diag(-2*np.ones(N)) + np.diag(np.ones(N-1), 1) + np.diag(np.ones(N-1), -1))
V_diag = np.diag(V(x))
H = T + V_diag

# Solve for eigenstates
eigenvalues, eigenvectors = eigh(H)
print(f"Ground state energy: {eigenvalues[0]:.4f}")
print(f"First excited state: {eigenvalues[1]:.4f}")
print(f"Energy gap (tunneling rate): {eigenvalues[1] - eigenvalues[0]:.4f}")
```

## Resources
- arXiv: 2509.02647 - hbar_E: an action constant for quantum economics
- arXiv: 2505.08917 - When Recall Fails, Discord Remembers: A Quantum Analogue of Kuhn's Theorem
- Journal of Quantum Economics and Finance

## Related Skills
- quantum-cognition
- quantum-game-theory-economics
- quantum-finance-analysis
- quantum-probability-statistics
