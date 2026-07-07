---
name: krylov-complexity-analog-simulator
description: "Bridging Krylov complexity theory with universal analog quantum simulation — using Lanczos algorithm and Krylov subspace growth to characterize computational power of analog quantum simulators. Activation: Krylov complexity, analog quantum simulator, Lanczos algorithm quantum, operator growth complexity."
---

# Krylov Complexity for Analog Quantum Simulation

## Description
Methodology connecting Krylov complexity theory with universal analog quantum simulation. Uses Lanczos algorithm to track operator growth in Krylov space as a measure of computational complexity in analog quantum simulators. Applicable to quantum chaos characterization, simulator benchmarking, and complexity phase transitions.

## Activation Keywords
- Krylov complexity analog simulator
- Lanczos algorithm quantum complexity
- operator growth Krylov space
- quantum simulator benchmarking complexity
- Krylov basis quantum dynamics
- analog quantum simulation complexity
- Krylov复杂性量子模拟

## Tools Used
- **terminal**: Run Krylov subspace calculations
- **execute_code**: Implement Lanczos algorithm and Krylov complexity measures
- **web_search**: Research Krylov complexity and analog quantum simulation

## Core Concepts

### Krylov Complexity
- **Operator Growth**: Heisenberg evolution of operators expands in operator space
- **Krylov Basis**: Lanczos algorithm generates orthonormal basis {O_n} from repeated commutation [H, O]
- **b_n Coefficients**: Lanczos coefficients determine growth rate of operator complexity
- **Krylov Complexity**: K(t) = Σ n |φ_n(t)|² measures spread in Krylov basis

### Lanczos Algorithm for Quantum Operators
```
Input: Hamiltonian H, initial operator O_0
1. b_1 O_1 = [H, O_0] - a_0 O_0    (a_0 = ⟨O_0|[H,O_0]|O_0⟩)
2. b_{n+1} O_{n+1} = [H, O_n] - a_n O_n - b_n O_{n-1}
3. Repeat until convergence or dimension limit
Output: Lanczos coefficients {b_n}, Krylov basis {O_n}
```

### Complexity Phases
- **Integrable Systems**: b_n saturates or grows slowly — low complexity
- **Chaotic Systems**: b_n ~ n (linear growth) — maximal complexity
- **Many-Body Localization**: b_n decays — complexity freezes

### Analog Quantum Simulator Benchmarking
1. **Map Simulator to Model**: Identify the effective Hamiltonian being simulated
2. **Compute Lanczos Coefficients**: Track b_n growth from experimentally accessible operators
3. **Compare to Theory**: Match measured b_n profile to expected complexity phase
4. **Validate Universality**: Check if simulator can access different complexity regimes

## Implementation Pattern

### Step 1: Lanczos Iteration
```python
import numpy as np
from scipy.linalg import commutator

def lanczos_operator_growth(H, O0, max_iter=50, tol=1e-10):
    """Compute Lanczos coefficients for operator growth."""
    # Normalize initial operator
    O0 = O0 / np.sqrt(np.trace(O0.conj().T @ O0))
    
    b_coeffs = []
    a_coeffs = []
    basis = [O0]
    
    for n in range(max_iter):
        # Compute commutator
        comm = 1j * (H @ basis[-1] - basis[-1] @ H)
        
        # Project onto previous basis elements
        a_n = np.real(np.trace(comm.conj().T @ basis[-1]))
        comm -= a_n * basis[-1]
        
        if n > 0:
            comm -= b_coeffs[-1] * basis[-2]
        
        # Norm gives next b coefficient
        b_n = np.sqrt(np.real(np.trace(comm.conj().T @ comm)))
        
        if b_n < tol:
            break
            
        b_coeffs.append(b_n)
        a_coeffs.append(a_n)
        basis.append(comm / b_n)
    
    return np.array(b_coeffs), np.array(a_coeffs), basis
```

### Step 2: Krylov Complexity Evolution
```python
def krylov_complexity(b_coeffs, t_values):
    """Compute Krylov complexity K(t) from Lanczos coefficients."""
    # Tridiagonal Hamiltonian in Krylov basis
    n = len(b_coeffs)
    H_krylov = np.zeros((n+1, n+1))
    for i in range(n):
        H_krylov[i, i+1] = b_coeffs[i]
        H_krylov[i+1, i] = b_coeffs[i]
    
    # Initial state: all weight in |0⟩
    psi_0 = np.zeros(n+1)
    psi_0[0] = 1.0
    
    complexities = []
    for t in t_values:
        # Time evolution
        U = scipy.linalg.expm(-1j * H_krylov * t)
        psi_t = U @ psi_0
        
        # K(t) = Σ n |φ_n(t)|²
        K_t = sum(n * abs(psi_t[n])**2 for n in range(n+1))
        complexities.append(K_t)
    
    return np.array(complexities)
```

### Step 3: Complexity Phase Classification
```python
def classify_complexity_phase(b_coeffs):
    """Classify complexity phase from Lanczos coefficient growth."""
    # Fit b_n to different models
    n_vals = np.arange(1, len(b_coeffs)+1)
    
    # Linear fit (chaotic): b_n ~ α*n
    lin_fit = np.polyfit(n_vals, b_coeffs, 1)
    lin_error = np.sum((b_coeffs - np.polyval(lin_fit, n_vals))**2)
    
    # Saturated fit (integrable): b_n → const
    const_fit = np.mean(b_coeffs)
    const_error = np.sum((b_coeffs - const_fit)**2)
    
    if lin_error < const_error:
        return "chaotic", lin_fit[0]  # slope
    else:
        return "integrable", const_fit
```

## Applications
- **Quantum Simulator Validation**: Verify simulator reaches expected complexity regime
- **Chaos Detection**: Identify quantum chaos through Lanczos coefficient growth
- **Benchmarking**: Compare different quantum simulator platforms
- **Resource Estimation**: Predict computational resources needed for simulation

## Pitfalls
- **Dimension Truncation**: Krylov space dimension is bounded by Hilbert space dimension — may saturate artificially
- **Numerical Stability**: Lanczos algorithm suffers from loss of orthogonality — use reorthogonalization for large spaces
- **Initial Operator Choice**: Different O_0 lead to different Krylov spaces — use physically relevant operators
- **Finite Size Effects**: Small systems may not show asymptotic b_n behavior

## Verification
- Check b_n growth rate matches theoretical prediction for known models (SYK, random matrix)
- Verify K(t) shows expected early-time exponential growth for chaotic systems
- Cross-validate with out-of-time-order correlators (OTOCs) for chaos detection

## References
- arXiv:2605.07668 — Bridging Krylov Complexity and Universal Analog Quantum Simulator
- Related: operator growth, quantum chaos, Lanczos algorithm, complexity geometry

## Related Skills
- `quantum-computational-sensing` — Quantum computational sensing methodology
- `quantum-reservoir-computing` — Quantum reservoir computing for chaotic time series
- `quantum-neural-dynamics` — Quantum neural network dynamics analysis
