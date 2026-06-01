---
name: metabolic-quantum-limit-meg
description: "Metabolic quantum limit methodology for magnetoencephalography (MEG). Combines energy resolution limits of quantum sensing with brain metabolic power to derive fundamental information capacity bounds."
category: neuroscience
trigger: "metabolic quantum limit, MEG information capacity, quantum sensors brain, SQUID brain imaging, atomic magnetometer MEG"
---

# Metabolic Quantum Limit to MEG Information Capacity

## Description

Methodology from arXiv:2511.06401 (Gkoudinakis, Li, Kominis, 2025). Derives fundamental limits on the information capacity of magnetoencephalography (MEG) by combining the energy resolution limit of magnetic sensing (using quantum sensors such as SQUIDs and atomic magnetometers) with the brain's metabolic power budget. Establishes the physical upper bound on how much information can be extracted from brain activity measurements.

## Core Framework

### 1. Quantum Sensing Limits

**SQUID Sensors:**
- Superconducting Quantum Interference Devices
- Flux quantization provides fundamental sensitivity
- Limited by thermal noise and quantum back-action

**Atomic Magnetometers:**
- Optically pumped magnetometers (OPMs)
- Spin-projection noise sets fundamental limit
- Approaching SQUID sensitivity without cryogenics

### 2. Metabolic Power Constraint

The brain's information processing is bounded by:
- **Energy budget**: ~20W total brain power consumption
- **Neuronal efficiency**: Energy per action potential (~10^9 ATP molecules)
- **Signal-to-noce ratio**: Metabolic noise floor constrains detectable signals

### 3. Information Capacity Derivation

```
C_max = (P_brain / (k_B * T)) * log2(SNR_max)
```

Where:
- P_brain: Available metabolic power for measurable activity
- k_B: Boltzmann constant
- T: Temperature
- SNR_max: Maximum achievable signal-to-noise ratio given quantum sensor limits

### 4. Key Results

- MEG information capacity is fundamentally limited by both quantum sensing AND metabolic constraints
- Current MEG systems operate far below theoretical capacity
- Atomic magnetometers may approach quantum limits more closely than SQUIDs
- Spatial resolution vs information capacity trade-off follows fundamental bounds

## When to Use

- Designing next-generation MEG systems
- Evaluating whether sensor improvements will yield meaningful gains
- Understanding fundamental limits of non-invasive brain imaging
- Comparing MEG with other neuroimaging modalities (fMRI, EEG)
- Planning experiments requiring maximum information extraction

## Pitfalls

- **Theoretical vs practical**: Real systems face additional engineering constraints
- **Model assumptions**: Simplified metabolic models may not capture all neural dynamics
- **Sensor-specific limits**: Different sensor technologies have different limiting factors
- **Temperature dependence**: Quantum sensor performance varies significantly with temperature
- **Cross-talk**: Multi-sensor arrays face mutual interference not captured by single-sensor analysis

## References

- arXiv:2511.06401 — "Metabolic quantum limit to the information capacity of magnetoencephalography" (Gkoudinakis, Li, Kominis, 2025)
- Related: Quantum sensing limits, Landauer bound, neural energy efficiency
