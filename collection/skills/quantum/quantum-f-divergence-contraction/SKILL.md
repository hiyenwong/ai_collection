---
name: quantum-f-divergence-contraction
description: "Quantum f-divergence contraction rate analysis methodology. Use when analyzing quantum channel convergence, strong data processing inequalities (SDPI), quantum information contraction bounds, or studying how quantum states approach equilibrium under noisy channels."
---

# Quantum f-Divergence Contraction Analysis

> Methodology for bounding asymptotic contraction rates of primitive quantum channels using quantum f-divergences and strong data processing inequality (SDPI) constants.

## Metadata
- **Source**: arXiv:2605.06452
- **Authors**: Matthew Simon Tan, Marco Tomamichel, Ian George
- **Published**: 2026-05-07
- **Categories**: quant-ph, cs.IT (Information Theory)

## Core Methodology

### Key Innovation
Establishes that quantum f-divergences satisfy a local reverse Pinsker inequality, which implies the asymptotic contraction rate of a primitive channel to its stationary state is upper bounded by the SDPI constant of any non-commutative f-divergence. Using quantum detailed balance, provides sufficient conditions for these bounds to be tight.

### Technical Framework

#### Step 1: Define Quantum f-Divergence
For a convex function f and quantum states ρ, σ:
```
D_f(ρ || σ) = Tr[σ^{1/2} f(σ^{-1/2} ρ σ^{-1/2}) σ^{1/2}]
```

#### Step 2: Strong Data Processing Inequality (SDPI)
For a quantum channel Φ with stationary state σ:
```
D_f(Φ(ρ) || σ) ≤ η · D_f(ρ || σ)
```
where η is the SDPI constant (0 ≤ η < 1 for primitive channels).

#### Step 3: Local Reverse Pinsker Inequality
Establish the local reverse Pinsker bound near the stationary state to relate contraction behavior to divergence measures.

#### Step 4: Contraction Rate Bound
The asymptotic contraction rate λ satisfies:
```
λ ≤ η_f
```
where η_f is the SDPI constant for the chosen f-divergence.

#### Step 5: Quantum Detailed Balance Condition
When the channel satisfies quantum detailed balance w.r.t. σ, the bounds become tight:
```
λ = η_f
```

### Applications to Specific Divergences
- **Petz f-divergences**: Standard quantum relative entropy family
- **Matsumoto f-divergences**: Maximal quantum divergences
- **Hirche-Tomamichel f-divergences**: Refined bounds for specific channel types

## Implementation Guide

### Prerequisites
- Python with NumPy/SciPy for matrix operations
- QuTiP or equivalent quantum computing library

### Step-by-Step
1. Implement the quantum channel as a superoperator (Kraus operators or Choi matrix)
2. Compute the stationary state σ (fixed point of the channel)
3. Choose an f-divergence family (Petz, Matsumoto, or Hirche-Tomamichel)
4. Compute the SDPI constant η via spectral analysis of the channel
5. Verify quantum detailed balance condition if tightness is needed
6. Apply bounds to analyze channel convergence behavior

### Code Example
```python
import numpy as np
from scipy.linalg import eig

def compute_sdpi_constant(kraus_ops, stationary_state, f_func):
    """Compute SDPI constant for a quantum channel."""
    # Construct the superoperator
    dim = stationary_state.shape[0]
    superop = np.zeros((dim**2, dim**2), dtype=complex)
    for K in kraus_ops:
        superop += np.kron(K, K.conj())
    
    # Analyze spectral gap
    eigenvalues = eig(superop, left=False, right=False)
    # Second largest eigenvalue modulus determines contraction rate
    sorted_eigs = np.sort(np.abs(eigenvalues))[::-1]
    sdpi = sorted_eigs[1]  # Spectral gap
    
    return sdpi

def verify_detailed_balance(kraus_ops, stationary_state):
    """Check if channel satisfies quantum detailed balance."""
    sigma_inv = np.linalg.inv(stationary_state)
    for K in kraus_ops:
        # Detailed balance: K_i = sqrt(σ) K_i† sqrt(σ^{-1})
        lhs = K
        rhs = np.sqrt(stationary_state) @ K.conj().T @ np.sqrt(sigma_inv)
        if not np.allclose(lhs, rhs, atol=1e-8):
            return False
    return True
```

## Applications
- **Quantum error correction**: Analyze how quickly errors contract under recovery channels
- **Quantum communication**: Bound information loss through noisy quantum channels
- **Quantum thermodynamics**: Study thermalization rates of open quantum systems
- **Quantum machine learning**: Understand convergence of quantum variational algorithms under noise

## Pitfalls
- SDPI constants depend on the reference state σ — bounds are state-dependent
- Quantum detailed balance is sufficient but not necessary for tight bounds
- Computing f-divergences for large systems requires efficient tensor network methods
- Non-commutativity makes quantum f-divergences fundamentally different from classical case

## Related Skills
- quantum-circuit-builder
- quantum-ml-patterns
