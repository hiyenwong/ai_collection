---
name: metabolic-quantum-limit-meg
description: Metabolic quantum limit methodology for magnetoencephalography (MEG) — combining quantum sensor energy resolution with neural metabolic power to derive fundamental information capacity bounds for brain imaging.
category: neuroscience
trigger_words: ["quantum limit", "MEG", "magnetoencephalography", "metabolic bound", "information capacity", "quantum sensor", "Planck constant", "spatio-temporal trade-off", "Nyquist scale", "energy resolution limit"]
---

# Metabolic Quantum Limit to MEG Information Capacity

**Paper**: arXiv:2511.06401v3 (Physical Review RESEARCH 8, 023267, 2026)
**Authors**: E. Gkoudinakis, S. Li, I. K. Kominis

## Core Insight

Combines the energy resolution limit of magnetic sensing with the metabolic power available to neural currents to derive a **technology-independent bound** on the information capacity of MEG. The bound factorizes into **geometry**, **metabolism**, and **Planck's constant**.

## Key Results

1. **Maximum Information Rate**: ~2.2 Mbit/s for representative human-brain parameters
2. **Spatial Resolution Limit**: ~1 cm — beyond this, denser sampling provides redundant measurements (information-theoretic Nyquist scale)
3. **Angular Bandwidth**: High multipole components are geometrically attenuated below the quantum-limited noise floor
4. **Spatio-Temporal Trade-off**: Noise variance grows linearly with measurement bandwidth, creating a fundamental trade-off

## Methodology

### Energy Resolution Limit
The energy resolution limit of magnetic sensors defines a minimum detectable energy per unit bandwidth:
```
ε_min ∝ ℏ (Planck's constant)
```

### Information Capacity Bound
```
C_max ∝ (Geometry) × (Metabolism) / ℏ
```

### Nyquist Scale for MEG
The information-limited spatial scale (~1 cm) defines the **Nyquist scale** for MEG — denser spatial sampling beyond this scale yields redundant measurements rather than additional recoverable information.

### Spatio-Temporal Trade-off
- Temporal bandwidth ↑ → Noise variance ↑
- Spatial bandwidth ↑ → Signal attenuation ↑
- Optimal operating point balances both

## Applications

- **Brain Imaging**: Quantitative link between fundamental physics and neuroscience
- **Sensor Design**: Technology-independent bounds for MEG sensor development
- **Signal Processing**: Optimal sampling strategies respecting information limits
- **Clinical**: Improved accuracy for preclinical Alzheimer's diagnosis

## Trigger Patterns
Use when analyzing MEG systems, quantum sensors for brain imaging, fundamental limits of neural measurement, or spatio-temporal trade-offs in neuroimaging.
