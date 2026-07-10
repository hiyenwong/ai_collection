---
name: moving-mri-brain-imaging
description: Moving MRI (mMRI) methodology for imaging during large-scale motion. Core idea: Move subject and scanner (magnet, gradients, RF coil) as a single unit to minimize relative motion, enabling neuroimaging during movement. Demonstrates cryogen-free superconducting magnet on pneumatically actuated tilt platform. Enables vestibular function studies during natural head motion. Activation: moving MRI, mMRI, motion MRI, vestibular imaging, motion artifact MRI, naturalistic neuroimaging, superconducting magnet mobile, head motion fMRI, brain imaging during movement.
---

# Moving MRI (mMRI) Brain Imaging

## Paper

- **Title**: Moving MRI: Imaging a moving body with a moving magnet
- **Authors**: Jingting Yao, Artan Kaso, Nikhil Patel, Yin-Ching Iris Chen, Andre van der Kouwe, Daniel M. Merfeld, Jerome L. Ackerman
- **arXiv**: 2605.09267v1 (2026-05-10)
- **Categories**: physics.med-ph, eess.SY

## Core Methodology

### Problem

Standard MRI requires subjects to remain stationary, preventing studies of brain networks during natural movement (e.g., vestibular function, locomotion).

### Key Innovation: mMRI System

Move the **entire imaging system** (magnet + gradients + RF coil) together with the subject:
- **Compact cryogen-free superconducting magnet** — no liquid helium dependency
- **Pneumatically actuated tilt mechanism** — moves the entire system as a unit
- **Minimizes relative motion** between subject and scanner during movement
- Maintains imaging during repetitive tilting motion

### Experimental Validation

- Phantom scans during motion — characterized tilt-induced field shifts
- In vivo rat brain scans during repetitive tilting
- Partially reduced motion and field-shift artifacts

### Applications

- **Vestibular function studies**: Image brain networks that sense head motion
- **Naturalistic paradigms**: Study neural correlates of movement
- **Broadening access**: Lower barrier to naturalistic neuroscience

## Technical Challenges

1. **Tilt-induced field shifts**: Gravity affects superconducting magnet homogeneity
2. **Residual subject-scanner motion**: Imperfect coupling introduces artifacts
3. **Pneumatic actuation**: Vibration and acceleration noise

## Future Directions

- Human-scale mMRI systems
- Integration with functional imaging (fMRI) during movement
- Combined with EEG/MEG for multi-modal moving neuroimaging

## Related Skills

- brain-digital-twins-execution-semantics-v3: Brain digital twin frameworks
- eeg-foundation-model-adapters: EEG foundation models
