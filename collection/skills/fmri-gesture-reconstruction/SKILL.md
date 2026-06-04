---
name: fmri-gesture-reconstruction
description: "fMRI2GES: Dual brain decoding alignment framework for co-speech gesture reconstruction from fMRI signals. Maps brain responses to external stimuli and decodes gestural behavior through dual-alignment brain decoding. Activation: fMRI gesture reconstruction, brain-to-gesture decoding, fMRI2GES, co-speech gesture brain decoding, dual brain decoding alignment."
---

# fMRI Gesture Reconstruction (fMRI2GES)

> Dual brain decoding alignment framework for reconstructing co-speech gestures from fMRI signals, advancing brain-to-behavior decoding beyond traditional speech/motor paradigms.

## Metadata
- **Source**: arXiv:2512.01189
- **Authors**: Chunzheng Zhu, Jialin Shao, Jianxin Lin, Yijun Wang, Jing Wang, Jinhui Tang
- **Published**: 2025-11-30
- **Categories**: Not specified in abstract

## Core Methodology

### Key Innovation
Extends brain decoding beyond speech/text reconstruction to **gesture reconstruction** — decoding the physical gestural behavior that accompanies speech from fMRI signals. Uses dual alignment strategy to improve decoding fidelity.

### Technical Framework

1. **Dual Brain Decoding Alignment**
   - Aligns fMRI signals to both gesture kinematics and speech features
   - Two-stage alignment: brain-to-gesture + brain-to-speech cross-modal mapping
   - Leverages shared neural representations between speech and gesture production

2. **Gesture Reconstruction Pipeline**
   - Input: fMRI time series during speech-with-gesture tasks
   - Intermediate: Aligned latent representations
   - Output: Reconstructed gesture sequences (motion trajectories)

3. **Cross-Modal Learning**
   - Joint training on gesture and speech decoding objectives
   - Shared encoder captures multimodal neural representations
   - Separate decoders for gesture kinematics and speech features

## Applications
- Brain-computer interfaces for gesture communication
- Understanding neural basis of co-speech gesture production
- Neurorehabilitation for speech-gesture coordination deficits
- Multimodal brain decoding research

## Implementation Guide

### Prerequisites
- fMRI data with gesture annotation
- Motion capture or gesture tracking data
- Deep learning framework for sequence modeling

### Step-by-Step
1. Collect fMRI data during natural speech-with-gesture tasks
2. Annotate gesture sequences (kinematics, timing, type)
3. Build dual-alignment encoder for fMRI-to-gesture mapping
4. Train with joint gesture + speech decoding objectives
5. Evaluate gesture reconstruction quality against ground truth
6. Analyze neural regions contributing to gesture decoding

### Pitfalls
- fMRI temporal resolution limits gesture reconstruction precision
- Requires synchronized fMRI and motion capture data
- Gesture annotation is labor-intensive
- Cross-modal alignment may be sensitive to individual variability
- Limited generalizability across subjects without adaptation

## Related Skills
- brain-dit-fmri-foundation-model
- brain-to-speech-prosody-feature-engineering
- eeg2vision-multimodal-eeg-framework-2d-visual
- visual-imagery-decoding-fmri
