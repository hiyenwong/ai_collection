---
name: computational-auditory-periphery-models
description: Cross-species computational modeling of the auditory periphery using 1-D nonlinear cochlear transmission-line models adapted across human, mouse, and gerbil. Covers species-specific anatomical/physiological parameterization, BM mechanics, OHC deficits, and cochlear synaptopathy simulation.
source: "arXiv: 2605.19070v2"
arxiv_id: "2605.19070"
authors: "Morgan Thienpont, F. Deloche, S. Keshishzadeh, D. Kiselev, J. Bourien, J.-L. Puel, B. N. Buran, N. Bramhall, S. Verhulst"
published: "2026-05-18 (v2: 2026-05-20)"
category: "q-bio.NC"
---

# Computational Auditory Periphery Models: the Return of the Rodent

## Overview

Cross-species computational models of the auditory periphery bridge the gap between non-invasive human diagnostics and experimental evidence from animal studies. This work adapts a 1-D nonlinear cochlear transmission-line (TL) model originally designed for the human auditory periphery to mouse and gerbil, enabling a single computational framework for cross-species research on sensorineural hearing loss (SNHL).

## Key Contributions

1. **Species-Specific Parameterization**: Adapted anatomical and physiological parameters — including basilar membrane (BM) length and width, stapes area, middle-ear transfer functions, and frequency range — to match each species' auditory periphery and hearing range.

2. **Cross-Species Validation**: Validated against experimental BM velocity level-growth characteristics, auditory-nerve (AN) tuning curves, and DPOAEs (distortion product otoacoustic emissions).

3. **Cochlear Synaptopathy Simulation**: Reproduced observed differences in recorded auditory brainstem responses (ABR) and envelope following responses (EFR) from mice and gerbils with SNHL.

4. **Model Limitations Identified**: OHC individualization based on DPOAEs failed to faithfully reproduce individual measurements, though intergroup differences in OHC damage were captured.

## Core Methodology

### Transmission-Line (TL) Model

The TL model is based on a time-domain implementation of Zweig's description of cochlear admittance, grounded in local scaling symmetry. Key equations:

- **Series impedance**: Z_{s_n}(s) = ω_n M_{s0} s
- **Shunt admittance (BM admittance)**: Y_{p_n}(s) = 1/Z_{p_n}(s) = s[ω_n M_{p0}(s² + δn + 1 + ρ_n e^{-μ_n s})]⁻¹

where `s = iω/ω_c` is normalized by CF, `n` is the cochlear section number (1–1000), and δ, ρ, μ specify damping, stiffness, and delay.

### Cochlear Nonlinearity

Zweig's TL linear equations are extended to a nonlinear version by dynamically shifting the double-pole α* in the s-plane. This shift broadens filters in response to increasing stimulus intensity while maintaining BM velocity zero-crossings. Key parameters per CF:

1. **Active pole α*_A**: Sharpest filters at low stimulation
2. **Passive pole α*_P**: Broader filters at high stimulation or post-mortem
3. **Compression slope C**: 0.31 dB/dB for human model
4. **Compression threshold**: Level at which BM velocity begins compressive growth

### Species Translation

Species-specific adjustments include:

| Parameter | Human | Gerbil | Mouse |
|-----------|-------|--------|-------|
| BM Length | ~35 mm | ~11 mm | ~7 mm |
| BM Width | Variable | Narrower | Narrowest |
| Frequency Range | 20–20,000 Hz | 0.1–50 kHz | 1–80 kHz |
| Stapes Area | ~3.2 mm² | ~0.8 mm² | ~0.5 mm² |
| AN Fiber Count | ~30,000 | ~24,000 | ~12,000 |

### Auditory Nerve and Brainstem Modeling

AN synapse model computes vesicle release and firing probability → single-fiber firing rate. ANFs divided into three subtypes by spontaneous rate (LSR=1, MSR=10, HSR=68.5 spikes/s). Responses summed across CFs and passed to ABR generators (cochlear nucleus, inferior colliculus) to model EFRs.

### Hearing Loss Simulation

- **OHC Loss**: Reduce mechanical cochlear gain in TL model
- **Cochlear Synaptopathy**: Remove subtypes of ANFs

## Key Results

1. Simulated AN outputs reasonably matched empirical AN thresholds and frequency selectivity
2. Discrepancy larger for cochlear sections near base or apex
3. Cochlear synaptopathy simulations reproduced species-specific ABR/EFR differences
4. OHC individualization via DPOAEs limited in reproducing individual measurements but effective for intergroup differences

## When to Use

Use this skill when:
- Building or adapting computational models of the auditory periphery
- Conducting cross-species hearing research (human ↔ rodent translation)
- Simulating sensorineural hearing loss or cochlear synaptopathy
- Validating auditory models against physiological data (BM velocity, AN tuning, DPOAEs, ABR)

## Related Skills

- [[computational-neuroscience-in-llm-era]] - General computational neuroscience
- [[multi-scale-info-geometry-neural]] - Information geometry approaches

## References

- Thienpont, M. et al. (2026). Computational Auditory Periphery Models: the Return of the Rodent. arXiv:2605.19070v2 [q-bio.NC]
- Zweig, G. (1991). Finding the impedance of the organ of Corti. JASA.
- Verhulst, S. et al. (2012, 2018). Nonlinear time-domain cochlear model. Hearing Research.
- Shera, C.A. (2001). Frequency glides in click-evoked otoacoustic emissions. JASA.
- Altoè, A. et al. (2014, 2018). Cochlear transmission-line models. JASA.
