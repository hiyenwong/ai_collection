# Physics-Informed Discrete-Event Simulation

## Jones Calculus Components

Optical component modeling using 2×2 Jones matrices:

### Wave Plates
```
λ/4 (quarter wave): 
  J_qwp(θ) = exp(-iπ/4) [cos(θ)+i·sin(θ), -sin(θ)+i·cos(θ)
                         sin(θ)+i·cos(θ),   cos(θ)-i·sin(θ)]

λ/2 (half wave):
  J_hwp(θ) = [cos(2θ), sin(2θ)
              sin(2θ), -cos(2θ)]
```

### Polarizing Beam Splitter
```
PBS: separates |H⟩ and |V⟩ modes
  H-mode transmission: T_H
  V-mode reflection: R_V
```

## SPDC Bell-State Source

Spontaneous parametric down-conversion generates:
```
|Φ^+⟩ = |H⟩|H⟩ + |V⟩|V⟩ (type-I)
|Φ^-⟩ = |H⟩|V⟩ + |V⟩|H⟩ (type-II)
```

Generation rate: R = η · P_pump
- η: conversion efficiency
- P_pump: pump power

## Multi-Section Fiber Model

Fiber sections with:
- Length: L_i
- Loss: α_i
- PMD: τ_i
- Dispersion: D_i

Combined effect:
```
H_fiber = exp(-Σ α_i L_i) · exp(i Σ D_i L_i ω^2)
```

## Timing Parameters

- Gate time: T_gate
- Detection window: T_det
- Coincidence window: T_coinc
- Photon arrival variance: σ_t

Typical values:
- T_gate = 100 ns
- T_det = 10 ns
- T_coinc = 1 μs
- σ_t = 100 ps