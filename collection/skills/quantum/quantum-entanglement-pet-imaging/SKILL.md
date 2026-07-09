---
name: quantum-entanglement-pet-imaging
description: "First-in-human quantum entanglement imaging using J-PET plastic scintillator scanner for PET + entanglement degree tomography. Exploits polarization correlations of annihilation photons for enhanced diagnostics. Use when building quantum-enhanced PET imaging systems, polarization-correlated tomography, or entanglement-based biomarker analysis. Activation: quantum entanglement imaging, J-PET, plastic scintillator PET, polarization-correlated tomography, entanglement degree biomarker, 68Ga quantum imaging, quantum PET"
category: quantum
created: 2026-07-08
source: arXiv:2606.29421
---

# First-in-Human Quantum Entanglement Imaging for PET

## Source

arXiv:2606.29421 — "First-in-human quantum entanglement imaging" by multiple authors (2026-06-28)

## Overview

Presents the first in vivo imaging of the degree of quantum entanglement of photons originating from positron-electron annihilation within a human subject. Uses the **Jagiellonian Positron Emission Tomography (J-PET)** scanner, constructed from plastic scintillators.

## Core Methodology

### Quantum Entanglement in PET

- Annihilation photons from positron-electron annihilation are **quantum-entangled in polarization**
- Plastic scintillators detect photons via **Compton scattering**, providing:
  - Photon interaction position
  - Interaction time
  - Photon polarization plane
- The **relative angle between polarization planes** of annihilation photons encodes the entanglement degree

### Pipeline Architecture

```
Patient injected with 68Ga-DOTA-TATE radiopharmaceutical
    │
    ▼
Positron-electron annihilation → Entangled photon pairs
    │
    ▼
J-PET Plastic Scintillator Detection (Compton scattering)
    │
    ├──→ Standard PET image (radiopharmaceutical uptake)
    │
    └──→ Quantum entanglement degree image (polarization correlation)
    │
    ▼
Clinical analysis of entanglement degree in organs
    ├── Liver: entanglement < maximally entangled, > separable
    └── Spleen: entanglement < maximally entangled, > separable
```

## Key Results

- **First in vivo demonstration** of quantum entanglement degree imaging in humans
- Patient injected with 68Ga-DOTA-TATE radiopharmaceutical
- Entanglement degree values measured in liver and spleen:
  - **Smaller than maximally entangled** two-photon states
  - **Larger than separable** photons
- Opens new biomarker channel for clinical diagnostics

## Applications

1. **Enhanced PET Imaging**: Combining standard uptake imaging with entanglement degree as additional diagnostic channel
2. **Tumor Characterization**: Entanglement degree may correlate with tissue properties
3. **Radiopharmaceutical Development**: Understanding how different isotopes affect entanglement
4. **Quantum Biology**: Studying quantum effects in biological systems

## Technical Details

### J-PET Scanner Architecture
- Built from **plastic scintillators** (not traditional crystal scintillators)
- Plastics enable Compton scattering detection → polarization information
- Provides 4D information: 3D position + time + polarization

### Entanglement Degree Measurement
- Determined from relative angle between polarization planes
- Values between 0 (separable) and 1 (maximally entangled)
- Tissue-dependent variation suggests potential diagnostic value

## Pitfalls

### Signal-to-Noise Challenges
- Entanglement signal is weak compared to standard PET signal
- Requires high-statistics measurements for reliable entanglement estimation
- Compton scattering cross-section in plastics is lower than photoelectric absorption in crystals

### Interpretation Complexity
- Entanglement degree affected by multiple factors:
  - Tissue scattering properties
  - Detector geometry and efficiency
  - Radiopharmaceutical biodistribution
- Must disentangle physical entanglement from measurement artifacts

## Future Directions

1. **Correlation Studies**: Link entanglement degree to pathological states
2. **Multi-isotope Studies**: Compare entanglement across different radiopharmaceuticals
3. **Real-time Entanglement Imaging**: Enable dynamic entanglement monitoring
4. **Quantum-Enhanced Reconstruction**: Use entanglement information for better image reconstruction

## Activation Keywords

- quantum entanglement imaging
- J-PET scanner
- plastic scintillator PET
- polarization-correlated tomography
- entanglement degree biomarker
- 68Ga quantum imaging
- quantum PET
- annihilation photon entanglement
