---
name: metabolic-quantum-limit-meg
description: "Metabolic quantum limit methodology for magnetoencephalography (MEG) — derives fundamental technology-independent bounds on brain information capacity using quantum sensing limits and metabolic power constraints."
activation_keywords:
  - metabolic quantum limit
  - MEG information capacity
  - brain information bound
  - magnetoencephalography quantum
  - quantum sensing brain
  - 脑信息容量量子极限
  - MEG量子极限
  - quantum-limited brain imaging
  - metabolic power brain
  - spatio-temporal bandwidth trade-off
categories:
  - neuroscience
  - quantum-physics
  - medical-imaging
arxiv_id: "2511.06401"
arxiv_url: "https://arxiv.org/abs/2511.06401"
authors: "E. Gkoudinakis, S. Li, I. K. Kominis"
created: "2026-06-08"
---

# Metabolic Quantum Limit to MEG Information Capacity

## Description

Methodology for deriving fundamental, technology-independent bounds on the information capacity of magnetoencephalography (MEG) measurements. Combines the energy resolution limit of magnetic quantum sensors (SQUIDs, atomic magnetometers) with the brain's metabolic power to establish a maximum information rate bound based only on geometry, neural metabolism, and Planck's constant.

## Core Findings

- **Maximum information rate**: 2.2 Mbit/s for the human brain
- **Finite angular bandwidth**: The measurable magnetic field has limited angular resolution
- **Geometric suppression**: Higher multipole components fall below the quantum-limited noise floor
- **Spatio-temporal trade-off**: Temporal and spatial bandwidths compete because noise variance grows linearly with bandwidth

## Methodology Steps

### Step 1: Establish Energy Resolution Limit
The minimum detectable magnetic field energy is bounded by quantum uncertainty:
- SQUID and atomic magnetometer sensors are subject to fundamental quantum noise
- Energy resolution limit: ΔE · Δt ≥ ℏ/2

### Step 2: Relate to Brain Metabolic Power
- Neural activity consumes metabolic power P_met
- Magnetic fields produced by neural currents carry information proportional to power
- Information capacity C ≤ P_met / (ℏ · bandwidth_factor)

### Step 3: Geometric Constraints
- External magnetic field measured outside skull has finite multipole expansion
- Higher-order multipoles (quadrupole, octupole, etc.) are geometrically suppressed
- Only low-order multipoles contribute measurably above quantum noise floor

### Step 4: Spatio-Temporal Bandwidth Trade-off
- Noise variance σ² ∝ bandwidth B (white noise assumption)
- Signal-to-noise ratio decreases with increasing bandwidth
- Must choose between:
  - High temporal resolution (wide temporal bandwidth, coarse spatial)
  - High spatial resolution (narrow temporal bandwidth, fine spatial via multipoles)

## Key Equations

```
C_max ≈ P_met / (ℏ · ln(2))   [bits/s]

For human brain:
P_met ≈ 20W (total), neural fraction ~ few percent
C_max ≈ 2.2 Mbit/s

Angular bandwidth limit:
l_max ∝ (brain_radius / quantum_noise_floor)^(1/2)
```

## Applications

1. **MEG system design**: Optimal sensor placement and bandwidth allocation
2. **Neuroscience theory**: Fundamental limits on what can be known about brain activity noninvasively
3. **Quantum sensor development**: Benchmark for next-generation MEG sensors
4. **Brain-computer interfaces**: Information-theoretic upper bounds on BCI bandwidth
5. **Alzheimer's/disease detection**: Sensitivity limits for early-stage biomarkers

## Activation Conditions

Use this skill when:
- Designing or analyzing MEG/EEG systems
- Studying fundamental limits of brain imaging
- Evaluating quantum sensors for neuroscience
- Computing information-theoretic bounds on neural measurements
- Analyzing spatio-temporal resolution trade-offs in brain imaging

## Related Concepts

- Quantum-limited sensing (SQUID, atomic magnetometers)
- Bures distance and quantum state distinguishability
- Mahalanobis whitening for fMRI de-individualization
- Shannon channel capacity for biological systems
- Multipole expansion of magnetic fields

## Resources

- Paper: [arXiv:2511.06401](https://arxiv.org/abs/2511.06401)
- Related: De-Individualizing fMRI Signals via Mahalanobis Whitening and Bures Geometry (arXiv:2511.07313)
