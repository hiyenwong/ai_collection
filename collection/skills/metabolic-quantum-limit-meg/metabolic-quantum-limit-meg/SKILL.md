---
name: metabolic-quantum-limit-meg
description: "Metabolic quantum limit methodology for magnetoencephalography (MEG) — derives technology-independent bounds on brain information capacity from quantum sensing limits + neural metabolism. Use when: studying quantum limits on brain imaging, MEG sensor resolution, neuro-metabolic information bounds, spatio-temporal trade-offs in neural measurement, quantum sensor design for neuroscience, fundamental limits of noninvasive brain recording, Planck-scale constraints on neural data."
---

# Metabolic Quantum Limit to MEG Information Capacity

## Overview

arXiv: 2511.06401 — Gkoudinakis, Li, Kominis (2025)

Combines energy resolution limit of magnetic sensing with brain metabolic power to derive a technology-independent bound on MEG information capacity.

## Core Results

### Maximum Information Rate

- **2.2 Mbit/s** upper bound for human brain MEG
- Derived from three fundamentals: geometry, neural metabolism, Planck's constant (h)
- Technology-independent — applies to any magnetic sensing approach

### Spatio-Temporal Trade-off

- Energy resolution limit → noise variance ∝ bandwidth
- Temporal and spatial bandwidths compete
- Higher multipole components geometrically suppressed below quantum-limited noise floor
- Finite angular bandwidth limits spatial complexity of neural current patterns

## Methodology

### Step 1: Energy Resolution Limit

For magnetic sensors (SQUIDs, atomic magnetometers):
```
ΔE · Δt ≥ ℏ/2
```
Noise variance grows linearly with measurement bandwidth.

### Step 2: Metabolic Power Budget

Brain metabolic power constrains total neural current energy available for measurement:
```
P_metabolic → maximum measurable signal power
```

### Step 3: Channel Capacity Bound

Apply Shannon-like capacity with quantum-limited SNR:
```
C = B · log₂(1 + SNR_quantum)
```
where SNR is bounded by metabolic power / quantum noise.

### Step 4: Multipole Suppression

External magnetic field multipole expansion:
- Dipole terms dominant
- Quadrupole and higher suppressed by geometry
- Higher orders fall below quantum noise floor
- Establishes finite angular bandwidth

## Key Equations

| Quantity | Scaling |
|----------|---------|
| Max info rate | ~2.2 Mbit/s |
| Noise variance | ∝ bandwidth |
| Multipole suppression | geometric (r⁻⁽ˡ⁺²⁾) |
| Angular bandwidth | finite |

## Applications

- Design of optimal MEG sensor arrays (spatio-temporal allocation)
- Fundamental limits for BCI information throughput
- Quantum sensor specification for neuroimaging
- Benchmark for neural recording technology claims
- Synthesis of neuroscience with quantum technology

## Activation Keywords

metabolic quantum limit, MEG, magnetoencephalography, information capacity, brain imaging bounds, quantum sensors, SQUID, atomic magnetometer, neural metabolism, Planck constant, spatio-temporal trade-off, multipole suppression, BCI throughput, noninvasive brain recording, quantum neuroimaging
