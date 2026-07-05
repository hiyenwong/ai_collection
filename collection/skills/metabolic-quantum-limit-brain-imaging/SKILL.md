---
name: metabolic-quantum-limit-brain-imaging
description: Quantum-metabolic bounds on information capacity of noninvasive brain imaging (arXiv:2511.06401)
category: quantum-neuroscience
---

# Metabolic Quantum Limit to Brain Imaging Information Capacity

Methodology from arXiv:2511.06401 (Physical Review RESEARCH 8, 023267, 2026). Technology-independent bound on MEG information capacity.

## Core Pattern

Combines **quantum sensing limits** with **metabolic constraints** to derive fundamental bounds:
- Energy resolution limit of magnetic sensing × metabolic power available to neural currents
- Bound factorizes into: **geometry × metabolism × Planck's constant**
- Maximum information rate: **~2.2 Mbit/s** for human brain parameters
- External magnetic field has **finite angular bandwidth** — high multipole components fall below quantum noise floor
- Information-limited spatial scale: **~1 cm**
- Measurement space is effectively **finite-dimensional**

## Key Findings

- Quantum-limited noise floor defines **information-theoretic Nyquist scale**
- Denser spatial sampling beyond Nyquist provides redundant, not additional, information
- Noise variance grows linearly with measurement bandwidth
- **Temporal and spatial bandwidths compete** — fundamental spatio-temporal trade-off
- Links fundamental physics to neuroscience quantitatively

## Implementation Steps

1. Model neural currents and their magnetic field generation
2. Apply quantum energy resolution limit to sensing geometry
3. Incorporate metabolic power constraints on neural currents
4. Derive information capacity bound (geometry × metabolism × ℏ)
5. Compute angular bandwidth cutoff from geometric attenuation
6. Determine spatial Nyquist scale from quantum noise floor
7. Analyze spatio-temporal trade-off from bandwidth competition

## When to Use

- Evaluating maximum information capacity of brain imaging modalities
- Designing optimal sensor arrays for MEG/EEG
- Understanding fundamental limits of noninvasive brain measurement
- Quantifying link between physics and neuroscience

## References

- arXiv: 2511.06401v3 (Physical Review RESEARCH 8, 023267, 2026)
- Authors: E. Gkoudinakis, S. Li, I. K. Kominis
