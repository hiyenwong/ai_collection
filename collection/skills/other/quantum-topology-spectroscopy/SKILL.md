---
name: quantum-topology-spectroscopy
description: >
  Quantum topology spectroscopy methodology for detecting band topology via quantum
  optical signatures in high-harmonic generation (HHG). Use when: (1) analyzing
  topological phases via optical spectroscopy, (2) computing high-harmonic generation
  in solid-state systems, (3) studying quantum light signatures of band topology,
  (4) implementing density-matrix evolution for light-matter dynamics, (5) designing
  topology-sensitive quantum light sources. Based on arXiv:2604.20388 (Ilin, Solntsev, Iorsh).
  Activation: band topology, high-harmonic generation, quantum light, SSH model,
  cavity QED, photon statistics, topological phase, squeezed light, current fluctuations
---

# Quantum Topology Spectroscopy via High-Harmonic Generation

## Core Insight

Topological phases of matter imprint directly on the quantum statistics of emitted
high-harmonic light — enabling topology detection via photon statistics rather than
traditional transport measurements.

## Key Results

1. **Topological phase → stronger HHG response**: The topological phase of the SSH
   model exhibits stronger high-harmonic generation than the trivial phase.

2. **Topological phase → stronger quantum signatures**: Non-classical light properties
   (squeezing, photon statistics) are enhanced in the topological phase.

3. **Squeezing from current fluctuations**: Cavity-matter interaction generates
   squeezed HHG light governed by current-current fluctuations, NOT by Kerr nonlinearity.

4. **Density-matrix approach essential**: Standard Schrödinger-equation HHG theories
   miss the mixed-state character critical for complex band structures.

## Theoretical Framework

### Density-Matrix Evolution

Instead of Schrödinger equation, use Liouville-von Neumann:

```
dρ/dt = -i/ℏ [H, ρ] + L_diss[ρ]
```

This captures both field and matter mixed states simultaneously.

### Weak-Correlation Expansion

Expand in photonic and matter degrees of freedom:

```
ρ = ρ_field ⊗ ρ_matter + δρ_corr
```

The correction term δρ_corr encodes the quantum statistics imprint of topology.

### SSH Model in Cavity

The Su-Schrieffer-Heeger (SSH) model coupled to a one-sided optical cavity:

- **Topological phase** (v < w): Edge states, non-trivial winding number
- **Trivial phase** (v > w): No edge states, trivial winding
- **HHG response**: Stronger in topological phase due to interband coherence

## Measurement Protocol

1. **Prepare system**: SSH model (or equivalent two-band topological insulator)
2. **Couple to cavity**: One-sided optical cavity with coupling strength g
3. **Drive with laser**: Intense mid-IR pump pulse
4. **Measure HHG spectrum**: Record harmonic intensities I_n for harmonics n = 1..N
5. **Measure photon statistics**: Compute g^(2)(τ) and squeezing parameter
6. **Compare phases**: Contrast topological vs trivial phase signatures

## Quantum Light Signatures

### Squeezing Parameter

```
r = ½ arctanh(2|⟨a²⟩ - ⟨a⟩²| / (2⟨a†a⟩ - |⟨a⟩|² + 1))
```

- Topological phase → larger r → more squeezing
- Origin: current-current fluctuations Im[χ(ω)] in material susceptibility

### Photon Statistics

```
g^(2)(0) = ⟨a†a†aa⟩ / ⟨a†a⟩²
```

- g^(2)(0) < 1: antibunching (non-classical)
- g^(2)(0) > 1: bunching
- Topological phase shifts g^(2)(0) further from 1

## Implementation Notes

- The genuine quantum Kerr term is higher order in light-matter coupling
- In mesoscopic regime, Kerr is negligible; current fluctuations dominate
- This establishes HHG as a topology probe without needing separate Kerr media
- Applicable to any system with non-trivial band topology (Chern insulators, topological superconductors)

## Applications

- Topological phase detection without transport measurements
- Quantum light source engineering via topology
- Photon-statistics-based spectroscopy of solid-state systems
- Benchmarking topological quantum materials

## Pitfalls

- Do NOT use Schrödinger-equation-based HHG theories for this analysis
- The Kerr nonlinearity is NOT the source of squeezing in this regime
- Cavity boundary conditions matter: one-sided cavity required for output coupling
- Weak-correlation expansion valid only for moderate light-matter coupling
