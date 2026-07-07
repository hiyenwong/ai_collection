---
name: metabolic-quantum-limit-meg
description: >
  Metabolic quantum limit methodology for magnetoencephalography (MEG) information capacity.
  Derives technology-independent bounds on MEG information capacity by combining quantum sensor
  energy resolution limits with metabolic power available to neural currents. The bound factorizes
  into geometry, metabolism, and Planck's constant. Use when: analyzing MEG information capacity
  limits, quantum sensing in neuroscience, fundamental limits of brain imaging, metabolic constraints
  on neural information processing, SQUID/OPM sensor analysis, information-theoretic bounds on
  neuroimaging, quantum-metabolic limits, brain sensor physics.
  Trigger words: MEG, magnetoencephalography, quantum limit, metabolic bound, information capacity,
  SQUID, atomic magnetometer, neural current, Planck constant bound, brain imaging limits.
---

# Metabolic Quantum Limit to MEG Information Capacity

Based on Gkoudinakis et al. (arXiv: 2511.06401).

## Core Framework

The information capacity of MEG is bounded by combining:
1. **Quantum sensing limit**: Energy resolution of magnetic sensors (SQUIDs, OPMs)
2. **Metabolic constraint**: Power available to neural currents from brain metabolism
3. **Geometric factor**: Distance and orientation of sensors relative to neural sources

### Bound Formula

The maximum information rate factorizes as:

```
I_max ∝ (geometry × metabolic_power) / ℏ
```

Where ℏ is Planck's constant, giving a fundamental physics-based bound independent of sensor technology.

## Key Findings

- Estimated maximum information rate: ~2.4 × 10^10 bits/sec for whole-brain MEG
- Bound is technology-independent — applies to any magnetic sensing approach
- Three factors: geometry (sensor-source configuration), metabolism (neural energy budget), Planck's constant
- SQUIDs and atomic magnetometers (OPMs) both approach this fundamental limit

## Application Workflow

1. **Identify the MEG system geometry** — sensor positions, orientations, distances to cortical sources
2. **Estimate metabolic power** — neural current power consumption (~10-20% of brain's ~20W budget)
3. **Apply the bound** — compute I_max using the factorized formula
4. **Compare with actual systems** — evaluate how close current MEG technology approaches the limit
5. **Optimize sensor placement** — use geometric factor to guide optimal sensor array design

## Cross-Domain Applications

- **fMRI limits**: Similar metabolic bounds may apply to BOLD signal information capacity
- **EEG**: Electrical sensing has analogous quantum-metabolic limits
- **Neural prosthetics**: Information bandwidth limits for brain-computer interfaces
- **Quantum sensing design**: Target information capacity when designing next-gen neural sensors

## Activation

- metabolic-quantum-limit-meg
- MEG information capacity
- quantum sensing neuroscience
- metabolic brain imaging limits
- neural current sensing bounds
