---
name: metabolic-quantum-meg
description: Metabolic quantum limit methodology for magnetoencephalography - deriving technology-independent bound on brain information capacity using energy resolution and Planck's constant
---

# Metabolic Quantum Limit to MEG Information Capacity

## Source
arXiv: 2511.06401 - "Metabolic quantum limit to the information capacity of magnetoencephalography" (E. Gkoudinakis et al., Physical Review RESEARCH 2026)

## Core Methodology
Derives a fundamental, technology-independent bound on the information capacity of MEG by combining the energy resolution limit of magnetic sensing with the metabolic power available to neural currents.

### Key Formula
- Information rate bound factorizes into: **Geometry × Metabolism × Planck's Constant**
- Estimated maximum: **2.2 Mbit/s** for representative human-brain parameters

### Findings
1. **Angular Bandwidth Limit**: Externally measurable magnetic field has finite angular bandwidth; high multipole components are geometrically attenuated below quantum-limited noise floor.
2. **Spatial Scale**: Information-limited spatial scale of order ~1 cm. Denser sampling beyond this provides redundant measurements.
3. **Nyquist Scale**: Energy resolution limit defines an information-theoretic Nyquist scale for MEG.
4. **Trade-off**: Noise variance grows linearly with bandwidth, creating a fundamental spatio-temporal trade-off.

### Implications
- Quantum-limited measurements constrain observable complexity of noninvasive brain imaging.
- Provides quantitative link between fundamental physics and neuroscience.
- Sets hard limits on what future MEG sensors can recover, regardless of engineering improvements.

### When to Use
- Designing next-gen MEG sensor arrays
- Evaluating theoretical limits of noninvasive brain imaging
- Neuroscience studies requiring fundamental bounds on information extraction
- Quantum sensing applications in biology
