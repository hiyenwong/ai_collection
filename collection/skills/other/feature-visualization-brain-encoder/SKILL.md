---
name: feature-visualization-brain-encoder
description: "Feature visualization as interpretability technique for brain encoder models. Uses gradient ascent on predicted activation for target ROIs to qualitatively evaluate whether encoders have internalized functional brain organization. Activation: feature visualization brain encoder, cortical selectivity validation, brain encoder interpretability, ROI feature visualization."
---

# Feature Visualization for Brain Encoder Interpretability

> Proposes feature visualization as a complementary interpretability technique for brain encoder models, going beyond held-out prediction accuracy to assess whether encoders have internalized the functional organization of the brain.

## Metadata
- **Source**: arXiv:2605.13904
- **Authors**: Stuart Bladon, Brinnae Bent
- **Published**: 2026-05-13
- **Paper**: "Feature Visualization Recovers Known Cortical Selectivity from TRIBE v2"

## Core Methodology

### Problem
Brain encoder models are typically evaluated by held-out prediction accuracy -- useful for training but poor for interpretation. High prediction scores don't reveal whether the model has internalized the brain's functional organization.

### Key Innovation
**Feature Visualization for Brain Encoders**: Gradient ascent on the encoder's predicted activation for a target region of interest (ROI), synthesizing images that maximally activate each brain region.

### Technical Framework
1. **Compose** brain encoder with differentiable backbone (e.g., TRIBE v2 + V-JEPA 2 ViT-G)
2. **Hold both frozen** during optimization
3. **Gradient ascent** on input image pixels to maximize predicted activation for target ROI
4. **Evaluate** synthesized images against known cortical selectivity patterns

### Results
- **V1-V4 progression**: Recovered visible hierarchy of increasing spatial scale and feature complexity
- **MT (middle temporal)**: Radial "frozen-motion" streaks despite static-only optimization
- **FFA (fusiform face area)**: Face-like features, optimized stimuli drive ~4x more than natural faces (adversarial super-stimuli)
- **PPA (parahippocampal place area)**: Consistent rectilinear line patterns

### Applications
- Qualitative evaluation of brain encoders
- Validation of in-silico neuroscience models
- Discovery of unexpected selectivity patterns
- Applicable to any brain encoder with differentiable backbone

## Pitfalls
- Optimized stimuli are super-stimuli, not canonical exemplars
- Requires differentiable encoder backbone
- Static optimization may miss temporal selectivity (e.g., MT's motion preference only partially recovered)

## Related Skills
- tribe-v2-foundation-model
- tribe-v2-trimodal-foundation-model
- decoding-encoding-alignment-critique
- lpact-brain-lm-alignment-evaluation
