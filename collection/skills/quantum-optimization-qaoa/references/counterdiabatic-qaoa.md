# Counterdiabatic QAOA (CCD-QAOA)

## Source
- arXiv:2605.06858 - "Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization" (Falla & Safro, 2026)
- arXiv:2605.02465 - "Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution" (Awasthi et al., 2026)

## What is Counterdiabatic Driving?

Counterdiabatic (CD) driving adds gauge potential terms to the QAOA ansatz to suppress non-adiabatic transitions, enabling better performance at fixed circuit depth.

### Standard QAOA vs CCD-QAOA

**Standard QAOA:**
```
|γ,β⟩ = Π_{k=1}^{p} e^{-iβ_k H_M} e^{-iγ_k H_C} |+⟩^{⊗n}
```

**CCD-QAOA:**
```
|γ,β,α⟩ = Π_{k=1}^{p} e^{-iα_k H_{CD}} e^{-iβ_k H_M} e^{-iγ_k H_C} |+⟩^{⊗n}
```

Where H_{CD} is the approximate adiabatic gauge potential.

### Approximate Gauge Potentials

The adiabatic gauge potential A_λ satisfies:
```
∂_λ H(λ) + i[A_λ, H(λ)] = 0
```

Approximated via nested commutators:
```
A_λ ≈ Σ_k c_k [H_C, [H_C, ...[H_C, H_M]...]]  (k nested commutators)
```

First-order approximation: A_λ ≈ c_1 [H_C, H_M]

For Ising-type portfolio Hamiltonian with XY-mixer:
```
[H_C, H_XY] = [Σ μ_i Z_i + Σ Σ_ij Z_i Z_j, Σ_{a<b} (X_a X_b + Y_a Y_b)]
```

The commutator generates terms like Y_i Z_j and X_i Z_j that push the state along the adiabatic path.

## Portfolio Optimization Application

### Problem Formulation

Minimize: `-Σ μ_i z_i + λ Σ Σ_ij z_i z_j`
Subject to: `Σ z_i = K` (budget/cardinality constraint)

### Why CCD-QAOA for Portfolio?

1. **Budget constraint naturally enforced** by XY-mixer (preserves Hamming weight)
2. **CD terms improve convergence** at fixed QAOA depth
3. **No penalty distortion** — avoids energy landscape warping from penalty methods
4. **Better approximation ratios** vs standard XY-mixer QAOA, Grover-mixer QAOA, penalty-based QAOA

## Implementation Pattern

```python
from qiskit import QuantumCircuit
import numpy as np

def commutator_term_qaoa_layer(qc, n, gamma, beta, alpha, layer):
    """Single QAOA layer with CD term."""
    # Cost Hamiltonian
    for i in range(n):
        qc.rz(2 * gamma[layer], i)
    
    # XY-Mixer
    for i in range(n):
        for j in range(i+1, n):
            qc.rxx(2 * beta[layer], i, j)
            qc.ryy(2 * beta[layer], i, j)
    
    # Counterdiabatic term (simplified)
    for i in range(n):
        qc.rx(2 * alpha[layer], i)
```

## Trotterization Tradeoffs (from arXiv:2605.02465)

| Trotter Steps | Constraint Fidelity | Gate Count | Recommended When |
|---------------|---------------------|------------|-------------------|
| 1 | ~90% | O(n²) | Hardware-limited |
| 2-4 | ~95-98% | O(2-4 n²) | Balanced |
| 8+ | ~99%+ | O(8+ n²) | Simulation |

- More Trotter steps → better constraint preservation but deeper circuits
- Optimal tradeoff depends on hardware coherence time
- Higher-order Suzuki formulas can achieve better accuracy with fewer steps

## Key Findings

1. CCD-QAOA consistently outperforms standard QAOA at fixed depth
2. XY-mixer + CD terms is superior to penalty-based constraint handling
3. First-order gauge potential [H_C, H_M] provides most improvement; higher-order terms add diminishing returns
4. For portfolio optimization with cardinality constraint, XY-mixer is the natural choice (preserves Hamming weight)
5. Trotterization errors in XY-mixer implementation are systematic and bounded
