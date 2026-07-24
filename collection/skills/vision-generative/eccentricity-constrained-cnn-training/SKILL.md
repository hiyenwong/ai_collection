---
name: eccentricity-constrained-cnn-training
title: Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field
version: 1.0.0
description: Methodology for training CNNs with eccentricity-constrained egocentric video data to reveal adaptive information coding that mirrors primate visual system organization, showing differential task-relevance between foveal and peripheral vision.
trigger_words:
  - "eccentricity-constrained cnn"
  - "fovea-periphery vision coding"
  - "egocentric visual experience"
  - "adaptive information coding visual field"
domain: neuroscience/computational-neuroscience
authors:
  - Dylan M. Diaz
  - Margaret M. Henderson
paper_id: arXiv:2607.19316
date: 2026-07-21
---

# Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field

## Overview

This methodology investigates how **eccentricity-dependent visual coding** can emerge from natural egocentric experience by training CNNs on gaze-contingent video data that isolates different regions of the visual field. The research demonstrates that models trained on fovea-only vs. periphery-only data develop systematic differences in their representations that align with known properties of the primate visual system.

## Key Findings

### Biological Alignment
- **Center-preferring cortical populations** have higher spatial resolution and overlap face/word-selective regions
- **Periphery-preferring populations** have lower spatial resolution and overlap scene-selective regions  
- This "eccentricity bias" reflects differential task-relevance across the visual field

### Model Performance Differences
- **Fovea-only models** stronger on both face recognition (VGGFace2) and scene categorization (Places365)
- **VEDB-pretrained models** generalized better to scene categorization than face recognition overall
- **Periphery-only models** held small but consistent advantage in scene-selective cortex (PPA, RSC)

### Neural Predictivity
- VEDB-pretrained models matched neural predictivity of ImageNet-100 models across visual cortex
- Egocentric data supports emergence of cortically-aligned representations
- Scene-selective cortex shows alignment with peripheral statistics

## Implementation Steps

### 1. Data Preparation
- Use **egocentric video and eye-tracking data** from Visual Experience Dataset (VEDB)
- Create **gaze-contingent crops** to isolate different eccentricities:
  - Fovea-only crops (central vision)
  - Periphery-only crops (surrounding vision)  
  - Periphery-only crops with NeuroFovea transform applied

### 2. Model Training
- Train **ResNet-18 models** using contrastive learning (SimCLR)
- Apply the same training protocol across all eccentricity conditions
- Ensure consistent preprocessing and augmentation strategies

### 3. Downstream Evaluation
- Evaluate on **in-domain VEDB frame classification** to assess differential informativeness
- Test **downstream transfer performance** on standard benchmarks:
  - Face recognition: VGGFace2
  - Scene categorization: Places365
- Compare performance systematically across fovea vs. periphery conditions

### 4. Neural Alignment Analysis
- Build **encoding models** using Natural Scenes Dataset (NSD) fMRI data
- Calculate **explained variance** across different visual cortex regions
- Specifically analyze scene-selective regions (PPA, RSC) for peripheral advantage

## Best Practices

### Egocentric Data Utilization
- **Egocentric experience adaptively constrains** cortical information processing
- Natural viewing behavior provides implicit supervision for visual representation learning
- Gaze-contingent cropping preserves ecological validity while enabling controlled experiments

### Eccentricity Isolation Techniques
- Use **NeuroFovea transform** for more biologically plausible periphery processing
- Ensure crops are properly aligned with gaze position from eye-tracking data
- Consider temporal consistency when processing video sequences

### Comparative Analysis Framework
- Always include **both fovea-only and periphery-only conditions** for comparison
- Use **identical architectures and training protocols** across conditions
- Include **non-egocentric baselines** (e.g., ImageNet-trained models) for reference

## Applications

- **Computational models of visual development** from natural experience
- **Brain-inspired computer vision** systems with foveated processing
- **Neural decoding studies** of visual field organization
- **AI-neuroscience integration** for understanding cortical information processing
- **Egocentric AI systems** that leverage natural viewing patterns

## Activation Keywords

Use this skill when working with:
- Eccentricity-dependent visual representation learning
- Foveated computer vision systems
- Egocentric video analysis with eye-tracking
- Neural alignment studies of visual cortex organization
- Computational models of primate visual system development

## References

- Diaz, D. M., & Henderson, M. M. (2026). Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field. arXiv:2607.19316
- Visual Experience Dataset (VEDB) - egocentric video with eye-tracking
- Natural Scenes Dataset (NSD) - human fMRI for neural alignment validation
- Related work on foveated vision and cortical eccentricity organization