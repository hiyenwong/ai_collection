---
name: brain-inspired-capture-visual-decoding
description: >
  Brain-Inspired Capture (BI-Cap) methodology for visual decoding from neurophysiological signals.
  Neuromimetic perceptual simulation paradigm emulating Human Visual System (HVS) processing pipeline
  to align neural and visual modalities for brain-computer interfaces.
  Trigger: brain-inspired capture, bi-cap, visual decoding, 视觉解码, brain-computer interface,
  neural-to-visual, neurophysiological signal decoding, neuromimetic simulation, HVS emulation.
version: 1.0.0
metadata:
  hermes:
    tags: [bci, visual-decoding, neuroscience, neuromimetic, hvs]
    source_paper: "Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding (arXiv:2604.17927)"
    paper_date: "2026-04-20"
    score: 33
---

# Brain-Inspired Capture (BI-Cap) for Visual Decoding

## Overview

BI-Cap addresses the systematic and stochastic gaps between neural signals and visual representations in BCIs by emulating the Human Visual System's (HVS) computational mechanisms rather than directly mapping neural activity to pixel space.

## Core Paradigm

Instead of direct neural→image mapping, BI-Cap constructs a neuromimetic pipeline that mirrors biological visual processing stages, creating an intermediate representation space that both modalities can bridge naturally.

## Neuromimetic Pipeline Stages

### Stage 1: Low-Level Feature Extraction

Mimics retinal and LGN processing:

```python
def retinal_processing(neural_signal):
    """Simulate early visual pathway processing."""
    # Edge detection (retinal ganglion cells)
    edges = apply_gabor_filters(neural_signal)
    # Contrast normalization (lateral geniculate)
    contrast = normalize_contrast(edges)
    return contrast
```

### Stage 2: Intermediate Representation

Mimics V1-V4 cortical processing:

```python
def cortical_processing(signal):
    """Simulate V1-V4 hierarchical processing."""
    # Orientation selectivity
    orientations = extract_orientations(signal)
    # Color processing
    color_channels = process_color_channels(signal)
    # Motion detection
    motion = detect_motion_patterns(signal)
    return combine_features(orientations, color_channels, motion)
```

### Stage 3: Perceptual Simulation

Generate visual content that matches the neuromimetic intermediate representation:

```python
def perceptual_synthesis(intermediate_rep, diffusion_model):
    """Use diffusion model to synthesize visual output."""
    # Condition diffusion model on neuromimetic features
    synthesized = diffusion_model.sample(
        condition=intermediate_rep,
        guidance_strength=7.5
    )
    return synthesized
```

## Key Design Principles

1. **Biological plausibility**: Each stage maps to known HVS mechanisms
2. **Modality bridging**: Intermediate space reduces neural-visual gap
3. **Evidence-driven**: Grounded in neurophysiological evidence
4. **Hierarchical processing**: Respects the feedforward hierarchy of visual cortex

## Architecture Overview

```
Neural Signal → [Retinal Model] → [LGN Model] → [V1-V4 Models] → [IT Cortex]
                                                                    ↓
                    Image ← [Diffusion Generator] ← [Perceptual Space]
```

## Comparison with Direct Mapping

| Aspect | Direct Mapping | BI-Cap |
|--------|---------------|--------|
| Modality gap | Large | Reduced via intermediate space |
| Biological grounding | None | HVS-inspired |
| Interpretability | Low | High (each stage maps to biology) |
| Generalization | Poor | Better (shared biological priors) |

## Applications

- Brain-computer interfaces for communication
- Visual prosthetics
- Neuroimaging-based content reconstruction
- Cognitive neuroscience research tools

## References

- BI-Cap paper: arXiv:2604.17927 (2026-04-20)
- HVS processing: Hubel & Wiesel (1962), receptive fields
- Neural decoding: Naselaris et al. (2011), encoding/decoding models