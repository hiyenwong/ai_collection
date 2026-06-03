---
name: mirage-fmri-mental-imagery
description: "MIRAGE methodology — robust multi-modal architecture for translating fMRI-to-image models from vision decoding to mental image reconstruction. Uses linear backbone + multi-modal text/image features with diffusion model; achieves SOTA on NSD-Imagery benchmark. Activation: fMRI mental imagery, MIRAGE, brain decoding, image reconstruction, cross-decoding, NSD-Imagery"
arxiv_id: "2605.17198"
published: "2026-05-16"
authors: "Reese Kneeland, Cesar Kadir Torrico Villanueva, Jordyn Ojeda, Shuhb Khanna, Jonathan Xu, Paul S. Scotti, Thomas Naselaris"
tags: [fmri-decoding, mental-imagery, image-reconstruction, multi-modal, diffusion-model, brain-computer-interface]
---

# MIRAGE: Robust Multi-Modal Architectures Translate fMRI-to-Image Models from Vision to Mental Imagery

> MIRAGE (Multi-modal Imagery Reconstruction via Augmented Generative Encoding) is a method explicitly designed to train on vision datasets (external stimuli) and cross-decode mental images from brain activity. It uses a linear backbone with multi-modal text and image features as input to a diffusion model.

**Source**: arXiv: [2605.17198](https://arxiv.org/abs/2605.17198)

## Core Innovation

While modern vision decoders can reconstruct seen images from human brain activity, they fail to generalize to internally generated visual representations (mental images). MIRAGE is the first method explicitly designed to bridge this gap.

### Key Technical Framework

1. **Linear Backbone**: Maps fMRI brain activity to a shared embedding space without overfitting to specific visual stimulus
2. **Multi-Modal Feature Fusion**: Combines text-based (semantic) and image-based (high- and low-level visual) features
3. **Diffusion Model**: Generates reconstructed images conditioned on the fused feature representation
4. **Classifier-Free Guidance**: Balances content preservation vs. reconstruction fidelity

### Critical Findings

- **SOTA on mental imagery**: MIRAGE achieves state-of-the-art performance on the NSD-Imagery benchmark
- **Vision decoder gap**: SOTA performance on seen image reconstruction ≠ SOTA on mental image reconstruction
- **Feature dimensionality matters**: Mental image reconstruction works best with relatively few dimensional image features
- **Multi-modal guidance essential**: Both text-based and image-based features (high + low level) are required

## Applications

- **Clinical brain-computer interfaces**: Decoding imagined content from locked-in patients
- **Neuroscience research**: Probing the nature of mental imagery representations
- **Creativity and communication**: New paradigms for expressing imagined content

## Related Skills

- visual-imagery-decoding-fmri
- brain-dit-universal-multi-state
- eeg-diffusion-visual-reconstruction
