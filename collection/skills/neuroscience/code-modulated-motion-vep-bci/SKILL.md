---
name: code-modulated-motion-vep-bci
description: "Code-Modulated Motion Visual Evoked Potential (c-MVEP) methodology for brain-computer interfacing using motion stimulation instead of flickering. Use when: designing BCI paradigms, visual evoked potential stimulation, motion-based BCI, reducing visual fatigue in SSVEP/c-VEP systems, EEG-based BCI with pseudo-random sequences. Activation: c-MVEP, motion VEP BCI, code-modulated motion, visual evoked potential BCI, flicker-free BCI, SSVEP alternative, c-VEP alternative."
---

# c-MVEP: Code-Modulated Motion Visual Evoked Potentials for BCI

Motion-based BCI paradigm using pseudo-random sequences instead of flickering.

## Paradigm

Uses pseudo-random sequences to visually stimulate objects via **motion** instead of **flickering**.

## Comparison with Existing Paradigms

| Paradigm | Stimulus Type | SNR | Accuracy | Speed | Subjective Preference |
|----------|--------------|-----|----------|-------|----------------------|
| c-MVEP | Motion + code | Moderate | 85.67% | 2.61s | No clear preference |
| c-VEP | Flicker + code | Moderate-high | 97.81% | 1.15s | No clear preference |
| SSVEP | Steady flicker | High | 93.42% | 1.94s | No clear preference |
| SSMVEP | Steady motion | Lower | 64.91% | 4.18s | No clear preference |

## Key Findings

- c-MVEP shows similar time-domain characteristics as c-VEP
- Broadband frequency response comparable to c-VEP, more focused in lower frequencies
- Spatial distribution: main activation at Oz, spreads across electrodes
- Outperforms SSMVEP significantly in accuracy and speed
- Provides viable alternative to flicker-based paradigms

## BCI Implementation

- 4-class BCI evaluation
- Offline comparison of 4 stimulation conditions
- Mean accuracy: 85.67% with 2.61s average selection time
- Suitable for applications where flickering is undesirable (e.g., photosensitive users)

## Activation Keywords

- c-MVEP
- Motion VEP
- BCI paradigm
- Flicker-free BCI
- Visual evoked potential
- Code-modulated motion
- EEG BCI stimulation
