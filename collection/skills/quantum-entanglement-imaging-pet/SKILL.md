---
name: quantum-entanglement-imaging-pet
category: quantum-medicine
description: Methodology for quantum entanglement imaging using PET scanners exploiting polarization entanglement of annihilation photons
created: 2026-07-01
trigger_words: quantum entanglement imaging, PET, J-PET, annihilation photons, polarization imaging, quantum medical diagnostics
---

# Quantum Entanglement Imaging with PET (arXiv:2606.29421)

## Overview

This methodology enables simultaneous imaging of radiopharmaceutical uptake AND quantum entanglement degree of annihilation photons in human subjects, exploiting the polarization entanglement that has not been previously utilized in medical diagnostics.

## Core Methodology

### 1. Detector Technology
- Use **plastic scintillator** PET scanner (J-PET architecture) instead of traditional crystal scintillators
- In plastics, annihilation photons interact primarily via **Compton effect**
- Compton scattering provides simultaneous information on:
  - Photon interaction position
  - Photon interaction time
  - Photon polarization plane

### 2. Quantum Entanglement Measurement
- Annihilation photons from positron-electron annihilation are **quantum-entangled in polarization**
- Measure degree of entanglement from the **relative angle between polarization planes** of the two annihilation photons
- The entanglement degree image is reconstructed simultaneously with the standard PET uptake image

### 3. Clinical Protocol
1. Inject patient with radiopharmaceutical (e.g., DOTA-TATE labeled with ⁶⁸Ga)
2. Use plastic scintillator PET scanner to detect coincidence events
3. For each coincidence: record position, time, and polarization plane for both photons
4. Reconstruct two images simultaneously:
   - Standard PET uptake image
   - Quantum entanglement degree image

### 4. Diagnostic Advantages
- **Dual imaging modality**: metabolic activity + quantum correlation information
- **Enhanced tissue characterization**: entanglement degree may reveal tissue properties not visible in standard PET
- **No additional radiation**: uses same annihilation photons, no extra dose
- **Room temperature operation**: plastic scintillators don't require cryogenic cooling

## Implementation Steps

1. **Scanner Setup**: Configure plastic scintillator PET scanner with polarization-sensitive readout
2. **Coincidence Detection**: Implement time-coincidence window with polarization measurement
3. **Compton Kinematics**: Reconstruct photon polarization from Compton scattering angle distributions
4. **Entanglement Reconstruction**: Calculate entanglement degree from polarization correlation statistics
5. **Image Reconstruction**: Apply iterative reconstruction algorithms for both uptake and entanglement images

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Radiopharmaceutical | ⁶⁸Ga-DOTA-TATE |
| Scanner Type | J-PET (plastic scintillators) |
| Interaction Mechanism | Compton effect |
| Entanglement Type | Polarization entanglement |
| Detection | Dual: position + time + polarization |

## Activation

Keywords: quantum entanglement imaging, PET scanner, J-PET, annihilation photons, polarization entanglement, Compton effect, quantum medical diagnostics, in vivo quantum imaging, entanglement degree imaging, radiopharmaceutical imaging

## Related Papers

- arXiv:2606.28252 - CV-QNN for oral cancer detection
- arXiv:2606.27411 - Quantum autoencoder for brain MRI anomaly detection
- arXiv:2606.30551 - Generative-ML-assisted quantum selected CI for molecular simulations
