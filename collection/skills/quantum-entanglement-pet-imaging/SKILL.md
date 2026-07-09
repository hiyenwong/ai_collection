---
name: quantum-entanglement-pet-imaging
description: "Methodology for quantum entanglement degree imaging using PET scanners — extracting C_QE biomarkers from annihilation photon polarization correlations via Compton scattering. Use when researching quantum entanglement medical imaging, PET biomarker development, positronium imaging, or polarization-correlated photon diagnostics."
metadata:
  arxiv_id: "2606.29421"
  published: "2026-06-28"
  authors: "P. Moskal et al."
  tags: [quantum, medical-imaging, PET, entanglement, biomarker, J-PET]
---

# Quantum Entanglement PET Imaging

First-in-vivo measurement of quantum entanglement degree (C_QE) from positron-electron annihilation photons in human subjects using J-PET plastic scintillator scanner.

## Core Methodology

### Entanglement Degree Measurement

1. **Compton Scattering Plane Analysis**: Measure angle φ between scattering planes of two 511 keV annihilation photons
2. **Visibility Calculation**: V(θ₁,θ₂) = F_max(θ₁,θ₂) - F_min(θ₁,θ₂) / F_max(θ₁,θ₂) + F_min(θ₁,θ₂)
3. **Degree Extraction**: C_QE = R_QE / 1.56 - 0.77 where R_QE = F_max/F_min at θ₁=θ₂=82°
4. **Calibration**: C_QE=1 for maximally entangled, C_QE=0.5 for separable photons

### Clinical Applications

- **Positronium Lifetime Imaging**: Correlate C_QE with positronium lifetime and 3γ/2γ ratio
- **Tissue Molecular Environment**: Non-maximal C_QE indicates pick-off annihilation with uncorrelated electron spins
- **Hypoxia Biomarker**: C_QE varies with oxygen concentration at annihilation site
- **Nanostructure Sensing**: Tissue porosity and molecular architecture affect entanglement degree

### Scanner Requirements

- **Plastic Scintillators**: Required for Compton scattering detection (vs crystal scintillators that absorb directly)
- **Triggerless DAQ**: Continuous acquisition for simultaneous primary + secondary scattering registration
- **TOF Resolution**: ~500ps minimum for annihilation point reconstruction along LOR

### Data Processing Pipeline

1. **Hit Classification**: Identify annihilation candidates via energy+position+timing
2. **Kinematic Selection**: Δt<2.5ns, opening angle>60° between photon pairs
3. **Scatter Assignment**: Use scatter test ST_k,j = c(t_j-t_k) - |r_j-r_k| for correct photon-scatter pairing
4. **ROI Selection**: 3D ellipsoidal regions around annihilation density clusters
5. **Efficiency Correction**: Monte Carlo (Geant4) with full detector geometry for ε(θ₁,θ₂,φ)
6. **Fitting**: F(φ) = A(1 - B·cos(2φ)) to extract R_QE from efficiency-corrected φ distribution

## Key Results

- **Liver**: C_QE ≈ 0.85 (97% purity, non-maximal but above separable threshold)
- **Spleen**: C_QE ≈ 0.82 (94% purity)
- **Interpretation**: Non-maximal entanglement due to pick-off process where positron annihilates with uncorrelated environmental electron spin

## Activation Keywords

- `quantum entanglement imaging`
- `entanglement degree PET`
- `C_QE biomarker`
- `positronium imaging`
- `J-PET scanner`
- `Compton polarization correlation`
- `annihilation photon entanglement`
- `quantum medical diagnostics`
- `polarization PET`
- `entanglement biomarker`
- `positronium lifetime imaging`
