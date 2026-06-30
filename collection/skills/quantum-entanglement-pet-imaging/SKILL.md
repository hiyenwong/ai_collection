---
name: quantum-entanglement-pet-imaging
description: "Positron Emission Tomography using quantum-entangled Compton events — methodology for exploiting annihilation photon polarization correlations to enhance PET sensitivity and signal-to-background ratio."
---

# Quantum Entanglement PET Imaging

## Description

Methodology for exploiting quantum entanglement of annihilation photons in Positron Emission Tomography (PET) to improve imaging quality. By measuring polarization correlations of annihilation quanta via Compton scattering, this approach achieves up to 10% sensitivity increase and 20% higher signal-to-random-background ratio compared to conventional single-pixel events.

## Activation Keywords

- quantum entanglement PET
- quantum-entangled Compton PET
- polarization-correlated PET imaging
- 量子纠缠PET成像
- quantum PET
- entangled annihilation photons
- J-PET scanner
- quantum-enhanced medical imaging

## Core Methodology

### Principle

Annihilation photons from positron-electron annihilation are quantum-entangled in polarization. In plastic scintillators (unlike crystal scintillators), photons interact primarily via the Compton effect, which provides:
1. Photon interaction position
2. Interaction time
3. Photon polarization plane

By selecting events based on the relative angle between polarization planes of annihilation photons, one can isolate polarization-correlated Compton events with higher signal-to-noise properties.

### Key Results (arXiv: 2606.25804)

| Metric | Single-Pixel Events | Polarization-Correlated Events |
|--------|--------------------|-------------------------------|
| Spatial Resolution | 2.5 ± 0.1 mm | 3.6–4.9 ± 0.3 mm |
| Signal-to-Random Background | Baseline | +20% higher |
| Estimated Sensitivity Gain | — | Up to 10% |
| Phantom Tested | NEMA NU-4 (378 MBq ⁶⁸Ga) | Same |

### Workflow

1. **Setup**: Use plastic scintillator-based PET scanner (e.g., J-PET)
2. **Detection**: Capture annihilation photon Compton scattering events
3. **Polarization Extraction**: Measure polarization planes from Compton scattering angles
4. **Event Selection**: Select events based on relative angle between polarization planes
5. **Image Reconstruction**: Combine polarization-correlated events with conventional events
6. **Quality Assessment**: Evaluate spatial resolution, signal-to-background, contrast-to-noise ratio

## Tools Used

- PET scanner with plastic scintillators (J-PET or similar)
- Compton polarimetry for polarization correlation measurement
- Statistical analysis for signal-to-background ratio comparison

## Usage Patterns

### Pattern 1: Enhanced Sensitivity PET Imaging
When standard PET resolution is insufficient and sensitivity is the bottleneck, use polarization-correlated Compton event selection to gain up to 10% sensitivity improvement.

### Pattern 2: Quality-Tradeoff Optimization
When spatial resolution is less critical than signal quality, select polarization-correlated events to improve signal-to-background ratio by ~20%.

### Pattern 3: Hybrid Event Reconstruction
Combine polarization-correlated Compton events with conventional single-pixel events for optimal overall image quality.

## Instructions for Agents

1. Identify if the clinical use case prioritizes sensitivity over spatial resolution
2. If yes → recommend polarization-correlated event selection
3. If spatial resolution is critical → use single-pixel events (2.5mm resolution)
4. For best overall performance → hybrid approach combining both event types
5. Note that this methodology requires plastic scintillator detectors (not crystal scintillators)

## Error Handling

### Plastic Scintillator Requirement
This methodology **requires** plastic scintillator detectors where Compton scattering dominates. Crystal scintillators (where photoelectric effect dominates) cannot measure polarization correlations this way.

### Resolution Tradeoff
Polarization-correlated events have slightly worse spatial resolution (3.6–4.9mm) vs single-pixel events (2.5mm). Select based on clinical priority.

## Related Skills

- `quantum-entanglement-imaging` (2606.29421) — First-in-human quantum entanglement imaging via J-PET
- `cv-photonic-qnn-edge-ai` (2606.28252) — CV photonic QNN for medical image classification
- `quantum-autoencoder-anomaly-detection` (2606.27411) — Quantum autoencoder for brain MRI anomaly detection
- `quantum-medical-imaging` — Umbrella skill for quantum-enhanced medical imaging

## Resources

- arXiv: 2606.25804 — "Positron Emission Tomography with quantum-entangled Compton events: first imaging results at clinically relevant activities"
- J-PET (Jagiellonian Positron Emission Tomography) scanner
