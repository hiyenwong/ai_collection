---
name: eccentricity-confound-eeg-visual-attention-decoding
description: "EEG-based visual attention decoding methodology addressing the eccentricity confound. Uses spatial attention tasks with controlled stimulus eccentricity and phase-scrambling controls to demonstrate that decodable EEG signals reflect genuine attention modulation, not visual processing confounds. Use when building EEG-based BCI attention decoders, visual attention research, or addressing confounds in neural decoding."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Decoding Visual Attention from EEG while Controlling for Visual Confounds (arXiv:2604.14890)"
    tags: [neuroscience, eeg, visual-attention, decoding, bci, confound-control]
---

# EEG Visual Attention Decoding with Eccentricity Control

## Overview

Addresses the fundamental confound in EEG-based visual attention decoding: whether signals reflect genuine attentional modulation or low-level visual processing differences. Demonstrates that spatial attention can be decoded from EEG above chance, and that the decoded signal is primarily driven by attentional modulation rather than stimulus eccentricity.

## Core Contribution

Shows that when controlling for stimulus eccentricity and using phase-scrambled stimuli, the decoded EEG signal reflects genuine spatial attention modulation. This validates EEG-based attention decoding as a reliable BCI paradigm.

## Key Findings

| Metric | Value |
|--------|-------|
| Attention decoding accuracy | 76% |
| Eccentricity decoding | 55% |
| Phase-scrambled control | Attention signal preserved |
| Conclusion | Attention > eccentricity as driver |

## Methodology

```python
# Experimental design controls:
# 1. Spatial attention task (attend left vs right)
# 2. Controlled stimulus eccentricity
# 3. Phase-scrambled stimuli (no recognizable content)
# 4. Compare decoding accuracy across conditions

def decode_attention(eeg_data, condition):
    """Decode spatial attention from EEG signals."""
    # Conditions: spatial_attention, eccentricity_control, 
    #              phase_scrambled
    pass

# Key finding: attention decoding works even with phase-scrambled
# stimuli, proving signal is attention-driven, not visual
```

## Applications

- **BCI attention control**: Reliable spatial attention-based interfaces
- **Visual neuroscience**: Disentangling attention from visual processing
- **Neurofeedback**: Attention-based training systems
- **Experimental design**: Proper confound control in neural decoding

## References

- Original paper: arXiv:2604.14890v1
- Authors: Not specified in abstract
- Published: 2026-04-16
