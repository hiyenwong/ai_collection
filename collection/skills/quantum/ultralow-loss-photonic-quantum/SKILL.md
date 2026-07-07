---
name: ultralow-loss-photonic-quantum
description: Ultralow-loss integrated photonic platforms for discrete-variable quantum information processing using silicon nitride (Si3N4) technology. Design methodology for high-fidelity entanglement generation and multi-photon state synthesis on manufacturable chips.
tags: [quantum, photonics, silicon-nitride, integrated-circuits, discrete-variable, entanglement, GHZ, EPR, CMOS-compatible, quantum-information-processing]
trigger_words: ultralow-loss photonic, silicon nitride quantum, integrated photonics quantum, discrete-variable quantum information processing, EPR state generation, GHZ state synthesis, qubit fusion circuit, photonic integrated circuit quantum, Si3N4 quantum platform, heralded HOM interference
---

# Ultralow-Loss Photonic Quantum Platform

## Description

Design methodology for discrete-variable quantum information processing using monolithic ultralow-loss silicon nitride (Si₃N₄) integrated photonic platforms. Addresses the exponential rate-loss barrier that constrains silicon photonics scaling by achieving:

- **EPR state preparation** with fidelity ≥ 0.9875 and near-unity photon indistinguishability
- **Heralded Hong-Ou-Mandel (HOM) interference** visibility ≥ 0.990
- **Multi-photon GHZ synthesis** (4-photon fidelity ≥ 0.943) with count rates 100× higher than silicon-photonic implementations
- **CMOS-compatible fabrication** on 150mm wafers for manufacturable large-scale deployment

Based on: "An ultralow-loss integrated photonic platform for discrete-variable quantum information processing" (arXiv:2606.26910)

## Architecture Components

### 1. Photon Source Integration
- **Narrowband photon-pair sources** integrated monolithically on chip
- Type-II spontaneous four-wave mixing (SFWM) or SPDC in Si₃N₄ microring resonators
- Spectral filtering for near-transform-limited photon bandwidth
- Target: heralding efficiency > 80%, pair generation rate ~MHz

### 2. Qubit-Fusion Circuit
- **Low-loss directional couplers** and Mach-Zehnder interferometers
- Active phase tuning via thermal or electro-optic modulators
- Hong-Ou-Mandel interference for Bell-state projection
- Design rule: insertion loss < 0.1 dB per component

### 3. Reconfigurable State Analysis
- Programmable interferometer networks for arbitrary basis measurement
- On-chip single-photon detection integration (SNSPD coupling)
- Feed-forward control for adaptive measurement schemes

### 4. Multi-Photon State Synthesis Pipeline
```
EPR₁ ──┐
       ├── Fusion Gate ──┐
EPR₂ ──┘                 ├── GHZ₄ Analysis
EPR₃ ──┐                 │
       ├── Fusion Gate ──┘
EPR₄ ──┘
```
- Pair EPR states → fuse via Bell measurement → characterize output GHZ state
- Fidelity scales as: F_GHZ ≈ F_EPR^n × F_fusion^(n-1)
- For n=4: F ≈ 0.9875⁴ × 0.99² ≈ 0.943 (matching experimental results)

## Design Guidelines

### Loss Budget Analysis
- **Total on-chip loss** must be < 3 dB for viable multi-photon experiments
- Component budget per photon path:
  - Source coupling: < 0.5 dB
  - Waveguide propagation: < 0.1 dB/cm (target < 0.01 dB/cm)
  - Each coupler/interferometer: < 0.1 dB
  - Analysis interferometer: < 0.5 dB

### Scaling Law
- Multiphoton rate ∝ η^N where η is per-photon efficiency
- Si₃N₄ advantage: η_Si3N4 ≈ 0.95 vs η_Si ≈ 0.70
- For N=8 photons: rate ratio ≈ (0.95/0.70)^8 ≈ 10× improvement
- For N=12: rate ratio ≈ 100× improvement

### Fabrication Constraints
- 150mm wafer standard for CMOS foundry compatibility
- Film thickness: 400-800 nm Si₃N₄ on thermal SiO₂
- Minimum waveguide bend radius: ≥ 50 μm for low loss
- Coupler gap: 200-400 nm for controlled coupling length

## Applications

| Application | Required Photons | Platform Requirement |
|-------------|------------------|---------------------|
| Bell-state analysis | 2 | EPR source + HOM interferometer |
| GHZ state synthesis | 4+ | EPR sources + fusion gates + analysis |
| Boson sampling | 10+ | Single-photon sources + interferometer mesh |
| Quantum repeater nodes | 2-4 | Memory-compatible source + Bell measurement |
| CV-DV hybrid interfaces | 2+ | Frequency-conversion integration |

## Key Metrics to Track

1. **EPR state fidelity** (target: > 0.98)
2. **HOM interference visibility** (target: > 0.98)
3. **Fourfold coincidence rate** (target: > 10 Hz for GHZ₄)
4. **On-chip propagation loss** (target: < 0.1 dB/m)
5. **Phase stability** (target: < λ/100 over measurement time)

## Related Skills

- `quantum-photonic-neural-networks` - Time-bin QPNN architectures
- `bosonic-gkp-parity-encoding` - Bosonic QEC codes
- `quantum-error-correction-methods` - General QEC patterns
- `quantum-network-control` - Entanglement distribution

## Activation

**Keywords**: ultralow-loss photonic, silicon nitride quantum, Si3N4 quantum platform, discrete-variable quantum, EPR state fidelity, GHZ synthesis, qubit fusion circuit, heralded HOM, integrated photonics quantum, monolithic photonic quantum, CMOS-compatible quantum, multiphoton photonic

## References

- arXiv:2606.26910 - "An ultralow-loss integrated photonic platform for discrete-variable quantum information processing" (June 2026)
- Standard Si₃N₄ photonic foundry processes (LIGENTEC, IMEC)
- Hong-Ou-Mandel effect fundamentals
