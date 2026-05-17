---
name: gksl-quantum-cognition
description: "GKSL (Gorini-Kossakowski-Sudarshan-Lindblad) master equation methodology for quantum-like modeling of cognition and decision-making (QCDM). Models mental state evolution as dissipative process in open quantum systems framework. Identifies cognitive beats as spectral signature of internal deliberation between competing flows of mind. Use when: quantum-like cognition, decision-making modeling, cognitive agency analysis, dissipative quantum models, GKSL/Lindblad dynamics, cognitive beats detection, Prisoner's Dilemma quantum analysis, non-classical decision theory, open quantum systems in psychology."
---

# GKSL Quantum Cognition

## Overview

Apply GKSL master equation to model cognitive processes as open quantum systems.
Mental states evolve as density matrices under dissipative dynamics influenced
by informational environment — not physical quantum processes in the brain,
but Hilbert space formalism applied to cognition.

## Core Framework

### GKSL Master Equation

```
dρ/dt = -i[H, ρ] + Σ_k γ_k (L_k ρ L_k† - ½{L_k†L_k, ρ})
```

Where:
- `ρ` = density matrix representing cognitive state
- `H` = Hamiltonian (internal deliberation dynamics)
- `L_k` = Lindblad operators (environmental decoherence channels)
- `γ_k` = decoherence rates

### Dynamical Regimes

| Regime | Condition | Cognitive Meaning |
|--------|-----------|-------------------|
| **Passive** | H commutes with decision basis | Classical rational agent |
| **Active** | H does NOT commute with decision basis | Cognitive agency, quantum escape from equilibria |
| **Decohered** | γ_k dominates | Collapse to classical probabilities |
| **Coherent** | Hamiltonian dominates | Quantum-like interference in decisions |

### Cognitive Beats

When two competing deliberation flows have similar frequencies:
- **Beat frequency** = |ω₁ - ω₂| where ω are eigenvalues of effective Liouvillian
- Beat envelope marks timing of peak readiness and hesitation
- Detectable via spectral analysis of Liouvillian superoperator
- Provides diagnostic for depth of cognitive agency

## Implementation Steps

### 1. Define Decision Basis

```python
import numpy as np

# Two-choice decision: basis |0>, |1>
n = 2  # number of options

# Initial cognitive state (equal preference)
rho_0 = np.eye(n) / n  # maximally mixed
```

### 2. Construct Hamiltonian

```python
# Non-commuting Hamiltonian for cognitive agency
H = np.array([[E0, J],
              [J, E1]])  # J != 0 creates non-classical transitions

# Active regime: H does not commute with projection operators
P0 = np.diag([1, 0])  # projection onto choice 0
non_commute = np.linalg.norm(H @ P0 - P0 @ H) > 0  # True = active
```

### 3. Define Lindblad Operators

```python
# Environmental decoherence (e.g., information overload, time pressure)
L1 = np.array([[1, 0], [0, 0]])  # decoherence in choice 0
L2 = np.array([[0, 0], [0, 1]])  # decoherence in choice 1
gamma = 0.1  # decoherence rate
```

### 4. Simulate Evolution

```python
from scipy.linalg import expm

def lindblad_step(rho, H, L_ops, gammas, dt):
    """Single step of GKSL evolution."""
    # Unitary part
    d_rho = -1j * (H @ rho - rho @ H)
    
    # Dissipative part
    for L, gamma in zip(L_ops, gammas):
        d_rho += gamma * (L @ rho @ L.conj().T - 0.5 * (L.conj().T @ L @ rho + rho @ L.conj().T @ L))
    
    return rho + d_rho * dt

# Time evolution
times = np.linspace(0, 10, 100)
trajectory = [rho_0]
for t in times[1:]:
    rho_next = lindblad_step(trajectory[-1], H, [L1, L2], [gamma, gamma], dt=0.1)
    trajectory.append(rho_next)

# Extract choice probabilities
prob_0 = [np.real(np.trace(rho @ P0)) for rho in trajectory]
```

### 5. Detect Cognitive Beats

```python
# Build Liouvillian superoperator in vectorized form
def build_liouvillian(H, L_ops, gammas, dim):
    """Construct Liouvillian matrix for spectral analysis."""
    d2 = dim * dim
    L = np.zeros((d2, d2), dtype=complex)
    
    # Hamiltonian part: -i(H ⊗ I - I ⊗ H^T)
    H_term = -1j * (np.kron(H, np.eye(dim)) - np.kron(np.eye(dim), H.T))
    
    # Dissipative part
    for L_op, gamma in zip(L_ops, gammas):
        L += gamma * (np.kron(L_op.conj(), L_op) 
                     - 0.5 * np.kron(np.eye(dim), L_op.conj().T @ L_op)
                     - 0.5 * np.kron(L_op.conj().T @ L_op, np.eye(dim)))
    
    return H_term + L

# Eigenvalue analysis
L_super = build_liouvillian(H, [L1, L2], [gamma, gamma], n)
eigenvalues = np.linalg.eigvals(L_super)

# Find oscillatory modes (imaginary eigenvalue pairs)
oscillatory = eigenvalues[np.abs(eigenvalues.imag) > 0.01]
if len(oscillatory) >= 2:
    # Beat frequency from two closest oscillatory modes
    freqs = np.sort(np.abs(oscillatory.imag))
    beat_freq = freqs[1] - freqs[0]
    print(f"Cognitive beat frequency: {beat_freq}")
```

## Applications

### Non-Nash Equilibria in Games

GKSL dynamics can stabilize outcomes that are not Nash equilibria:
- Prisoner's Dilemma: quantum-like model supports cooperation as steady state
- Active Hamiltonian creates persistent deviation from classical best response

### Decision Making Under Uncertainty

- Models hesitation, contextuality, and order effects in surveys
- Captures violations of sure-thing principle
- Predicts interference patterns in sequential decisions

### Cognitive Agency Measurement

- Active Hamiltonian strength → degree of cognitive agency
- Cognitive beat frequency → depth of deliberation
- Decoherence rate → vulnerability to information overload

## Key Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| H coupling (J) | 0-1 | ↑ J → ↑ quantum-like interference |
| Decoherence (γ) | 0-10 | ↑ γ → faster collapse to classical |
| H non-commutation | 0+ | >0 → active cognitive agency |
| Time scale | arbitrary | Determines beat period |

## Activation

Keywords: `gksl dynamics`, `quantum-like cognition`, `Lindblad equation`, `cognitive beats`,
`dissipative quantum models`, `cognitive agency`, `open quantum systems psychology`,
`quantum decision theory`, `quantum escape`, `non-Nash game theory`,
`quantum cognition modeling`, `density matrix cognition`

arXiv: 2604.18643
