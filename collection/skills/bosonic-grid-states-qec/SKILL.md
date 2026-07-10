---
name: bosonic-grid-states-qec
description: "Bosonic quantum error correction using Gottesman-Kitaev-Preskill (GKP) grid states and programmable nonlinear bosonic circuits. Covers grid state preparation, logical qubit encoding in continuous-variable oscillators, Wigner function characterization, and fault-tolerant bosonic QEC architectures. Use when working on: bosonic codes, GKP states, cat/qubit encodings, continuous-variable QEC, nonlinear bosonic gates, or oscillator-based quantum computing. Triggers: bosonic QEC, GKP grid states, cat codes, binomial codes, continuous-variable quantum computing, oscillator qubit, bosonic circuits."
---

# Bosonic Grid States & Programmable Nonlinear Bosonic Circuits for QEC

## Overview

Bosonic quantum error correction encodes logical qubits into infinite-dimensional harmonic oscillators using discrete grid states (GKP), cat states, or binomial states. The key insight: a single physical mode with structured encoding can detect and correct errors without the overhead of multi-qubit repetition codes.

## Core Concepts

### GKP Grid States

GKP states encode logical information in the periodic structure of position (q) and momentum (p) quadratures:

```
|μ,ν⟩_GKP ∝ Σ_n |q = √π(2n+μ)⟩ · e^{i√π ν p}
```

- Logical |0⟩ and |1⟩ are displaced combs in phase space
- Grid spacing √π provides correctability against small shifts
- Errors appear as displacements: shift < √π/2 → correctable

### Error Model

Bosonic errors map to phase-space displacements:
- **Shift errors**: δq, δp displacements in quadrature space
- **Photon loss**: amplitude damping → biased shift errors
- **Dephasing**: random displacement in p-direction

Correction via Steane-type syndrome measurement: modular quadrature measurement reveals shift without collapsing logical information.

### Programmable Nonlinear Bosonic Circuits

Recent work (arXiv:2604.21824) demonstrates:
- Engineered Kerr nonlinearities for universal bosonic gates
- Programmable beam-splitter operations via parametric coupling
- SNAP (Selective Number-dependent Arbitrary Phase) gates for Fock-state control
- Cross-Kerr interactions for entangling logical bosonic modes

## Methodology

### Step 1: Choose Bosonic Code

| Code | Encoding | Best For |
|------|----------|----------|
| GKP | Periodic grid in phase space | General shift errors |
| Cat | Superposition of coherent states | Photon loss channels |
| Binomial | Number-state superpositions | Targeted loss+dephasing |
| Pair-cat | Two-mode entangled states | Biased noise |

### Step 2: State Preparation

GKP state preparation approaches:
1. **Circuit-based**: Oscillator-reset + sequence of conditional displacements
2. **Measurement-based**: Heralded preparation via ancilla coupling
3. **Autonomous**: Engineered dissipation stabilizing the grid manifold

### Step 3: Error Syndrome Extraction

```
1. Apply controlled-displacement with ancilla qubit
2. Measure ancilla → reveals mod(q, √π) or mod(p, √π)
3. Conditional displacement correction based on syndrome
4. Repeat for both quadratures
```

### Step 4: Logical Gate Implementation

| Gate | Physical Implementation |
|------|------------------------|
| X_L | Displacement by √π in q |
| Z_L | Displacement by √π in p |
| H_L | Phase-space rotation (π/4 shear) |
| CNOT | Entangling cross-Kerr + displacements |
| T_L | Magic state injection + distillation |

## Architecture Patterns

### Single-Oscillator QEC Cycle

```
Oscillator → Syndrome Extraction → Classical Decoding → Conditional Correction
     ↑                                                        |
     └────────────────────────────────────────────────────────┘
```

### Multi-Mode Architecture

```
[Mode 1] ──┬── [BS gate] ──┬── [Mode 2]
            │                │
        [SNAP]          [SNAP]
            │                │
        [Kerr]          [Kerr]
            └── [XK] ────────┘
```

## Implementation Guidance

### Wigner Function Analysis

```python
# Wigner function for GKP state characterization
import numpy as np

def wigner_gkp(q_grid, p_grid, mu=0, nu=0, delta=0.3, n_peaks=5):
    """Approximate Wigner function of finite-energy GKP state.
    
    Args:
        q_grid, p_grid: Phase space grids
        mu, nu: Logical encoding parameters (0 or 1)
        delta: Gaussian envelope width (finite energy)
        n_peaks: Number of grid peaks to include
    """
    W = np.zeros_like(q_grid)
    for n in range(-n_peaks, n_peaks+1):
        q0 = np.sqrt(np.pi) * (2*n + mu)
        envelope = np.exp(-(q_grid - q0)**2 / (2*delta**2))
        W += envelope * np.cos(np.sqrt(np.pi) * nu * p_grid)
    return W
```

### Syndrome Decoding

```python
def gkp_syndrome_decode(syndrome_q, syndrome_p, sqrt_pi=np.sqrt(np.pi)):
    """Decode GKP shift syndrome to correction displacement.
    
    Returns correction (dq, dp) to apply.
    """
    dq = syndrome_q % sqrt_pi
    dp = syndrome_p % sqrt_pi
    
    # Map to [-sqrt_pi/2, sqrt_pi/2)
    if dq > sqrt_pi / 2:
        dq -= sqrt_pi
    if dp > sqrt_pi / 2:
        dp -= sqrt_pi
    
    return -dq, -dp
```

## Key Metrics

| Metric | GKP Target | Cat Target |
|--------|-----------|------------|
| Threshold displacement | √π/2 ≈ 0.886 | Depends on α |
| Logical error rate | ~exp(-πΔ²) per cycle | ~exp(-2|α|²) |
| Overhead vs rep code | ~10x lower | ~5x lower |
| Gate fidelity target | >99.9% | >99.5% |

## Error Budget

1. **Finite-energy corrections**: Δ² ∝ 1/⟨n⟩ — higher photon count = better approximation
2. **Syndrome measurement errors**: Ancilla infidelity propagates as logical error
3. **Gate infidelity**: Nonlinear gate errors accumulate per QEC cycle
4. **Thermal noise**: Excitation drift between correction cycles

## Hardware Platforms

| Platform | Oscillator Mode | Nonlinearity Source |
|----------|----------------|---------------------|
| Superconducting | 3D/transmon cavity | JRM modulator, SNAIL |
| Trapped ions | Motional modes | Mølmer-Sørensen |
| Photonic | Temporal/freq modes | χ(2) crystals |
| Mechanical | MEMS resonators | Piezoelectric coupling |

## Pitfalls

- GKP states require high photon numbers; finite-energy envelope causes intrinsic error floor
- Cross-Kerr gates can be slow; gate times vs coherence time budget
- Syndrome measurement back-action on oscillator — use quantum non-demolition schemes
- Mode cross-talk in multi-oscillator architectures

## References

- arXiv:2604.21824 — Programmable nonlinear bosonic circuits for grid states
- Gottesman, Kitaev, Preskill (2001) — Original GKP encoding
- Terhal et al. (2020) — Bosonic QEC survey
- Albert et al. (2018) — Performance bounds for bosonic codes
