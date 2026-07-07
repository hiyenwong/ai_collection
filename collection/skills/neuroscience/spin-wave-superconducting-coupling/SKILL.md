---
name: spin-wave-superconducting-coupling
description: Strong coupling between propagating spin waves and microwave photons in superconducting resonator-magnetic thin film hybrid circuits. Design methodology for hybrid magnonic quantum systems using YIG-on-substrate integration.
tags: [quantum, magnonics, spin-wave, superconducting-resonator, hybrid-systems, YIG, microwave-photon, cavity-magnonics, nonreciprocity, Damon-Eshbach, quantum-information]
trigger_words: spin wave coupling, superconducting magnon, YIG resonator, propagating spin wave, microwave photon coupling, Damon-Eshbach mode, backward-volume spin wave, hybrid magnonic system, cavity magnonics, nonreciprocal spin wave, rare-earth-free substrate
---

# Spin Wave–Superconducting Coupling

## Description

Design methodology for achieving strong coupling between propagating spin wave (magnon) modes and microwave photons in superconducting resonator-magnetic thin film hybrid circuits. Enables integration of spin-wave magnonics with cavity magnonics for quantum information science applications.

Based on: "Strong coupling between propagating spin wave and microwave photons in a superconducting resonator" (arXiv:2606.27279)

## Strong Coupling Criterion

The system achieves **strong coupling** when:

```
g > κ_m, κ_c, γ
```

Where:
- **g**: magnon-photon coupling strength
- **κ_m**: magnon damping rate
- **κ_c**: cavity (photon) damping rate  
- **γ**: spin wave propagation loss

Strong coupling enables:
- Coherent magnon-photon state exchange
- Magnon-based quantum memory
- Nonreciprocal quantum signal routing

## Key Architecture

### 1. Substrate + Film Stack
```
┌─────────────────────────────────┐
│    Superconducting Resonator     │  ← Nb/Al superconducting film
├─────────────────────────────────┤
│   YIG Thin Film (Y₃Fe₅O₁₂)     │  ← Magnetically active layer
├─────────────────────────────────┤
│  Y₃Sc₂Ga₃O₁₂ (YSGO) Substrate  │  ← Rare-earth-free, lattice-matched
└─────────────────────────────────┘
```

- **YSGO substrate**: Rare-earth-free alternative to GGG, reduces cost and supply chain constraints
- **YIG thin film**: Ultra-low magnetic damping (α < 10⁻⁴), high spin wave coherence
- **Superconducting resonator**: High-Q microwave cavity (Q > 10⁵ at mK temperatures)

### 2. Spin Wave Modes

| Mode Type | Propagation | Coupling Characteristics |
|-----------|-------------|-------------------------|
| **Damon-Eshbach (DE)** | Surface wave, unidirectional | Strongest coupling, exhibits nonreciprocity |
| **Backward-Volume (BV)** | Volume wave, bidirectional | Weaker coupling but broader bandwidth |
| **Magnetostatic Forward Volume** | Bulk propagation | Intermediate characteristics |

### 3. Nonreciprocal Radiation

In the Damon-Eshbach configuration:
- Spin wave radiation is **nonreciprocal** (direction-dependent)
- Enables one-way magnon-photon conversion
- Useful for quantum isolators and circulators without magnetic bias field

## Design Parameters

### Coupling Strength Optimization
```
g ∝ √(N_magnons) × γ_magnon-photon × √(ω_cavity)
```
- Maximize magnon density N via film thickness optimization
- Optimize mode overlap integral between spin wave and cavity field
- Higher cavity frequency → stronger single-photon coupling

### Damping Minimization
| Loss Channel | Typical Value | Mitigation |
|-------------|---------------|------------|
| Magnon damping (κ_m/2π) | ~1 MHz | High-quality YIG, surface passivation |
| Cavity loss (κ_c/2π) | ~0.1 MHz | Superconducting materials, geometric optimization |
| Spin wave propagation loss | ~1 dB/mm | Film thickness, surface roughness control |
| Two-level system (TLS) loss | ~0.01-0.1 MHz | Substrate cleaning, interface optimization |

### Fabrication Guidelines
1. **YIG film growth**: Pulsed laser deposition or sputtering on YSGO
2. **Film thickness**: 50-200 nm (optimize for DE mode coupling)
3. **Resonator design**: Coplanar waveguide or lumped element resonator
4. **Temperature**: mK regime for superconducting operation
5. **Magnetic bias**: External field for mode tuning (0-0.3 T)

## Applications

| Application | Configuration | Key Metric |
|-------------|--------------|------------|
| Quantum memory | DE mode coupling | Coherence time > 1 μs |
| Quantum transducer | BV mode + optical conversion | Conversion efficiency > 1% |
| Quantum isolator | DE nonreciprocity | Isolation > 20 dB |
| Magnonic quantum processor | Multi-mode coupling | Mode count > 10, g/2π > 10 MHz |
| Hybrid quantum network | Spin wave bus | Propagation distance > 1 mm |

## Related Skills

- `quantum-network-transduction` - Quantum signal conversion
- `non-hermitian-cv-quantum-control` - Non-Hermitian control methods
- `quantum-hybrid-neural-computing` - Hybrid quantum systems

## Activation

**Keywords**: spin wave coupling, superconducting magnon, YIG resonator, propagating spin wave, microwave photon coupling, Damon-Eshbach mode, backward-volume spin wave, hybrid magnonic system, cavity magnonics, nonreciprocal spin wave, rare-earth-free substrate, YSGO substrate

## References

- arXiv:2606.27279 - "Strong coupling between propagating spin wave and microwave photons in a superconducting resonator" (June 2026)
- Damon-Eshbach spin wave theory (1961)
- Cavity magnonics review literature
