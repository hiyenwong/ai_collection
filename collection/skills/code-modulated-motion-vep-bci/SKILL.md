---
name: code-modulated-motion-vep-bci
description: "Code-Modulated Motion Visual Evoked Potential (c-MVEP) methodology for brain-computer interfacing. Uses pseudo-random motion sequences instead of flickering for visual stimulation. Covers EEG-based BCI paradigms comparing c-MVEP, c-VEP, SSMVEP, SSVEP. Based on Scheppink et al. (arXiv: 2605.15801). Use when designing motion-based BCI systems, developing flicker-free visual stimulation paradigms, or comparing VEP-based BCI approaches. Activation: c-MVEP, motion VEP, code-modulated VEP, brain-computer interface, visual evoked potential, flicker-free BCI, EEG BCI paradigm, arXiv:2605.15801"
---

# Code-Modulated Motion Visual Evoked Potential (c-MVEP) for BCI

> Novel BCI paradigm using pseudo-random motion sequences instead of flickering for visual object stimulation, offering a flicker-free alternative to c-VEP.

## Metadata
- **Source**: arXiv:2605.15801
- **Authors**: Hanneke Scheppink, Rainer Herpers, Jordy Thielen, Ivan Volosyak
- **Published**: 2026-05-15
- **Domain**: q-bio.NC (Neurons and Cognition)

## Core Methodology

### Key Innovation
Introduces **c-MVEP** (code-modulated motion visual evoked potential): a BCI paradigm that uses **pseudo-random binary sequences** to modulate **object motion** (rather than luminance flickering) for visual stimulation. This provides a more comfortable alternative to flicker-based SSVEP/c-VEP paradigms while maintaining comparable signal quality.

### Paradigm Comparison
The study compares four stimulation paradigms:

| Paradigm | Stimulation Type | Response Type | Key Characteristics |
|----------|-----------------|---------------|---------------------|
| **c-MVEP** | Code-modulated motion | Broadband, transient | Lower frequency focus, spread across multiple electrodes |
| **c-VEP** | Code-modulated flicker | Broadband, transient | Higher SNR, more focused at Oz |
| **SSMVEP** | Steady-state motion | Oscillatory at stim freq | Lower SNR than SSVEP |
| **SSVEP** | Steady-state flicker | Oscillatory at stim freq | Highest SNR |

### Signal Characteristics
- **c-MVEP time-domain**: Similar characteristics to c-VEP (broadband response)
- **c-MVEP frequency-domain**: Comparable SNR to c-VEP, but more concentrated in lower frequencies
- **Spatial distribution**: Main activation at Oz with spread across multiple electrodes
- **c-VEP comparison**: c-VEP shows less spreading, more focused at Oz

### Experimental Results

**Offline Experiment** (single object, 4 conditions):
- c-MVEP: Similar time-domain to c-VEP, comparable SNR in frequency domain
- SSVEP > SSMVEP for oscillatory response SNR
- Subjective ratings: No clear preference for motion-based over flicker-based

**Online Experiment** (4-class BCI):
| Paradigm | Accuracy | Selection Time |
|----------|----------|---------------|
| c-VEP | 97.81% | 1.15s |
| SSVEP | 93.42% | 1.94s |
| **c-MVEP** | **85.67%** | **2.61s** |
| SSMVEP | 64.91% | 4.18s |

### Pseudo-Random Sequence Coding
- Uses **Gold codes** or **m-sequences** for unique identification of each stimulus target
- Cross-correlation between EEG and reference sequences for target identification
- Same coding principle as c-VEP but applied to motion instead of luminance modulation

## Implementation Guide

### Prerequisites
- EEG acquisition system (minimum ~8 channels, recommended 16+)
- Stimulus presentation software capable of object motion control
- Electrode placement: Oz primary, surrounding occipital electrodes

### Step-by-Step
1. **Stimulus Design**: Create visual targets that move according to pseudo-random binary sequences
2. **Sequence Generation**: Use m-sequences or Gold codes with different shifts for each target
3. **EEG Recording**: Record EEG during stimulus presentation with synchronized markers
4. **Signal Processing**: Apply bandpass filtering, artifact removal
5. **Target Identification**: Cross-correlate EEG segments with reference sequences
6. **Classification**: Select target with highest correlation coefficient

### Code Example
```python
import numpy as np
from scipy.signal import correlate

def generate_m_sequence(degree=10):
    """Generate maximal-length sequence for BCI coding."""
    # Primitive polynomial for m-sequence generation
    # ... (standard LFSR implementation)
    pass

def c_mvep_classification(eeg_data, reference_sequences, fs=256):
    """Classify c-MVEP targets using template matching."""
    correlations = []
    for ref in reference_sequences:
        # Upsample reference to match EEG sampling rate
        ref_upsampled = np.repeat(ref, fs // 60)  # 60Hz refresh rate
        corr = correlate(eeg_data, ref_upsampled[:len(eeg_data)], mode='valid')
        correlations.append(np.max(corr))
    return np.argmax(correlations)
```

## Applications
- **Flicker-free BCI**: For users sensitive to flickering stimulation
- **Prolonged BCI sessions**: Reduced visual fatigue compared to SSVEP
- **Medical BCI**: Patients with photosensitive epilepsy
- **Consumer BCI**: More comfortable user experience for everyday use

## Pitfalls
- **Lower accuracy than c-VEP**: 85.67% vs 97.81% in the study
- **Slower selection time**: 2.61s vs 1.15s for c-VEP
- **Subjective comfort**: No clear user preference for motion over flicker in this study
- **Motion blur**: Fast motion may cause visual artifacts affecting signal quality

## Related Skills
- eeg-brain-connectivity-bci
- bci-rehabilitation-protocols
- unibci-invasive-foundation-model
- prm-explainable-rnn-p300-bci
