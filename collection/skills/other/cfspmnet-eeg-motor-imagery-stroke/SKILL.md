---
name: cfspmnet-eeg-motor-imagery-stroke
description: "CFSPMNet - Cross-subject Fourier-guided Spatial-Patch Mamba Network for EEG Motor Imagery Decoding in Stroke Patients. Use when working with MI-EEG decoding, cross-subject BCI for stroke rehabilitation, Mamba-based EEG models, or Fourier-domain token reorganization for neural decoding."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.10111"
  published: "2026-05-11"
  authors: "Xiangkai Wang, Yun Zhao, Dongyi He, Qingling Xia, Gen Li, Xinlai Xing, Yuchi Pan, Bin Jiang"
  tags: [eeg, motor-imagery, mamba, stroke-rehabilitation, bci, cross-subject]
---

# CFSPMNet: Cross-subject Fourier-guided Spatial-Patch Mamba Network for EEG Motor Imagery Decoding in Stroke Patients

**arXiv:2605.10111** | Submitted 11 May 2026 | cs.LG, cs.AI, cs.CV

## Core Concept

CFSPMNet addresses the challenge of cross-patient MI-EEG decoding for stroke rehabilitation. Pathological neural reorganization makes source-learned MI representations unreliable for unseen patients. CFSPMNet models post-stroke MI-EEG as latent neural-state organization, combining a **Fourier-Reorganized State Mamba Network (FRSM)** with **Shared-Private Prototype Matching (SPPM)** for robust cross-subject adaptation.

## Key Insights

1. **Fourier-Reorganized State Mamba Network (FRSM)**: Represents each trial as a latent physiological token sequence, reorganizes token states in the Fourier domain, and uses Fourier-derived trial context to guide Mamba state-space propagation. This captures both band-specific spectral patterns and cross-frequency interactions.

2. **Shared-Private Prototype Matching (SPPM)**: Improves target-domain pseudo-label updating by combining semantic confidence with shared-private physiological consistency, filtering confident but physiologically inconsistent target predictions.

3. **Leave-One-Subject-Out Results**: Achieves 68.23% on XW-Stroke and 73.33% on 2019-Stroke datasets, outperforming CNN, Transformer, Mamba, and adaptation-based baselines with improvements of 5.63 and 8.25 percentage points.

4. **Neurophysiological Interpretability**: Ablation, sensitivity, feature-alignment, pseudo-label selection, and neurophysiological visualization analyses confirm that Fourier-domain token-state reorganization and calibrated pseudo-label updating contribute to the performance gains.

## Method Components

### Fourier-Reorganized State Mamba Network
- Encodes EEG trials as latent physiological token sequences
- Reorganizes token states in the Fourier domain to capture spectral structure
- Fourier-derived trial context guides Mamba state-space propagation
- Captures both band-specific and cross-frequency interactions

### Shared-Private Prototype Matching
- Maintains shared prototypes (common across subjects) and private prototypes (subject-specific)
- Pseudo-label selection filters based on both semantic confidence and physiological consistency
- Prevents propagation of confident but neurophysiologically implausible predictions

## Applications

- **Stroke rehabilitation BCI** with MI-EEG decoding
- **Cross-subject EEG decoding** where training data comes from different patients
- **Mamba-based neural signal processing** for time-series EEG
- **Domain adaptation for pathological EEG** affected by neural reorganization
- **Fourier-domain EEG feature extraction** for spectral representation learning

## Activation Keywords

- CFSPMNet
- EEG motor imagery decoding
- Mamba EEG network
- Fourier-guided EEG
- cross-subject BCI stroke
- shared-private prototype matching
- stroke rehabilitation EEG
- Fourier domain token reorganization
- Mamba state space EEG
- MI-EEG cross-patient

## References

- Wang et al. (2026). CFSPMNet: Cross-subject Fourier-guided Spatial-Patch Mamba Network for EEG Motor Imagery Decoding in Stroke Patients. arXiv:2605.10111
