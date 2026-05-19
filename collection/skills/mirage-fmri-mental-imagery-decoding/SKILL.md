---
name: mirage-fmri-mental-imagery-decoding
description: "MIRAGE methodology — robust multi-modal architecture for translating fMRI-to-image models from visual perception to mental imagery reconstruction. Use when: (1) decoding mental imagery from brain activity, (2) building fMRI-to-image decoders, (3) cross-decoding from perception to imagination, (4) designing multi-modal brain-computer interfaces, (5) analyzing NSD-Imagery dataset, (6) studying generalization of vision decoders to internally generated representations. Activation: MIRAGE, fMRI mental imagery, brain-to-image decoding, mental image reconstruction, NSD-Imagery, vision decoder generalization, fMRI diffusion model, neuroimaging decoding, internal representation decoding"
---

# MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding

**Paper**: Kneeland et al. (2026). *MIRAGE: Robust multi-modal architectures translate fMRI-to-image models from vision to mental imagery*. arXiv:2605.17198.

## Core Insight

State-of-the-art performance on seen image reconstruction does NOT guarantee SOTA on mental image reconstruction. MIRAGE explicitly designs for cross-decoding generalization from external perception to internally generated visual representations.

## Architecture

MIRAGE = **linear backbone** + **multi-modal features** → **diffusion model**

### Key Design Choices

1. **Linear backbone**: Simple linear mapping from fMRI to feature space (avoiding complex nonlinear encoders that overfit to perception)
2. **Multi-modal feature input**:
   - Image features (relatively low-dimensional)
   - Text-based features (semantic guidance)
   - Both high-level and low-level image features
3. **Diffusion model generation**: Uses decoded features as conditioning for image synthesis

### Why It Works

- **Feature dimensionality matters**: Mental image reconstruction works best with fewer-dimensional image features
- **Text guidance critical**: Including text-based features provides semantic grounding absent in low-level visual features alone
- **Multi-level features**: Both high-level (semantic) and low-level (textural) image features needed

## Key Findings

### SOTA Performance
- MIRAGE achieves state-of-the-art mental image reconstruction on NSD-Imagery benchmark
- Validated by both feature metrics and human raters

### Architecture Comparison
- Some modern vision decoders perform well on mental imagery, others fail completely
- SOTA on seen images ≠ SOTA on mental images (architectural sensitivity)
- Simple linear backbone + rich multi-modal features outperforms complex nonlinear architectures

### Ablation Results
- Best performance requires: low-dim image features + text guidance + high+low-level features
- Removing any component degrades mental image quality significantly

## Methodology

1. **Train on vision datasets**: Use external stimulus data (NSD) as training source
2. **Linear fMRI-to-feature mapping**: Avoid overfitting nonlinear encoders
3. **Multi-modal feature concatenation**: Combine text, high-level, and low-level features
4. **Diffusion model decoding**: Generate images from decoded features
5. **Cross-decode to mental imagery**: Evaluate on internally generated representations

## Applications

- **Mental image reconstruction**: Decode imagined content from fMRI
- **Brain-computer interfaces**: Communication via imagined content
- **Clinical neuroscience**: Studying imagination deficits in neurological conditions
- **Consciousness research**: Probing the neural basis of internally generated representations

## Pitfalls

- **Do not assume visual decoder generalizes to mental imagery**: Architecture must be explicitly designed for cross-decoding
- **High-dimensional features hurt**: Low-dimensional image features generalize better to mental imagery
- **Text features are essential**: Semantic grounding from text features critical for mental image quality
- **Simple > complex**: Linear backbone outperforms complex nonlinear encoders for this task
- **NSD-Imagery is the benchmark**: Use this dataset for standardized evaluation

## Activation Keywords

- MIRAGE mental imagery
- fMRI mental image reconstruction
- brain-to-image decoding
- NSD-Imagery
- vision decoder generalization
- mental imagery fMRI
- cross-decoding brain activity
- fMRI diffusion model
