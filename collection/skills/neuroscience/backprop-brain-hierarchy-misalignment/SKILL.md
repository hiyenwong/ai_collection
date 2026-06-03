---
name: backprop-brain-hierarchy-misalignment
description: "Methodology for analyzing the misalignment between backpropagation algorithms in deep neural networks and the hierarchical organization of brain responses. Extends encoding analyses from forward activations to backpropagated gradients, revealing fundamental differences in learning mechanisms. Use when studying brain-DNN alignment, computational neuroscience, or investigating whether backpropagation is biologically plausible."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.28693"
  published: "2026-05-27"
  authors: "Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, Huy V. Vo, Jérémy Rapin, Patrick Labatut, Piotr Bojanowski, Valentin Wyart, Jean-Rémi King"
  tags: [neuroscience, deep-learning, backpropagation, brain-alignment, fMRI, MEG, visual-processing, predictive-coding]
---

# Backpropagation-Brain Hierarchy Misalignment

## Overview

This methodology extends standard encoding analyses to map backpropagated gradients onto neural data (fMRI and MEG), revealing that while deep networks and the brain share similar representational content, they likely rely on fundamentally different learning mechanisms.

## Core Discovery

**Key finding**: Backpropagated gradients can predict brain signals (fMRI/MEG), but their spatial and temporal organization diverges from expected patterns under biologically plausible backpropagation.

## Methodology

### 1. Extended Encoding Analysis

Standard encoding analysis maps forward activations to neural responses. This framework extends to:

- **Forward activations**: Already known to map onto cortical hierarchy reliably
- **Backpropagated gradients**: NEW - maps to higher-level visual cortex and later latencies

**Implementation**:
```python
# Extract gradients from vision model (e.g., DINOv3)
model.backward(input_image)  # Compute gradients
gradient_features = extract_gradient_representations(model)
# Map to neural data via encoding analysis
encoding_score = correlate(gradient_features, neural_data)
```

### 2. Spatial Hierarchy Analysis

**Expected pattern (biologically plausible BP)**:
- Gradients computed in reverse order: high-level → low-level
- Spatial organization: parietal → occipital progression

**Observed pattern**:
- Diverges from expected temporal hierarchy
- Diverges from expected spatial hierarchy

### 3. Temporal Hierarchy Analysis

**Expected**: Gradients arrive at low-level cortex after high-level cortex (reverse temporal order)

**Observed**: Temporal organization does not match expected pattern

## Key Results

### Brain Prediction Performance

- **fMRI**: Backpropagated gradients predict signals in higher-level visual cortex
- **MEG**: Gradients predict later latency responses (post-stimulus period)
- **Model**: DINOv3 (self-supervised) + 8 vision models for validation

### Misalignment Evidence

1. **Order divergence**: Gradient computation order ≠ brain temporal hierarchy
2. **Spatial divergence**: Gradient spatial organization ≠ brain spatial hierarchy
3. **Representational similarity**: Forward activations align with brain hierarchy, but gradients misalign

## Implications

### For Neuroscience

- Brain and deep networks share representational content
- But learning mechanisms are fundamentally different
- Backpropagation unlikely to be implemented in brain as-is

### For AI Research

- Forward activations are reliable brain models
- Gradient-based learning differs from biological learning
- Alternative learning algorithms may better match brain mechanisms

## Experimental Setup

### Data Sources
- **fMRI**: Human brain responses to natural images
- **MEG**: Temporal dynamics of visual processing

### Models Tested
- DINOv3 (primary self-supervised model)
- 8 additional vision models (reproducibility check)

### Analysis Pipeline

1. Extract forward activations from pretrained model
2. Compute backpropagated gradients for input images
3. Correlate both with fMRI voxel responses and MEG sensor signals
4. Compare spatial/temporal organization patterns
5. Assess alignment with cortical hierarchy

## Use Cases

### When to Apply This Methodology

1. **Brain-DNN alignment studies**: Investigating correspondence between AI and brain learning
2. **Biological plausibility research**: Testing whether backpropagation is neurally implementable
3. **Encoding analysis extensions**: Moving beyond forward activations to gradient-based mapping
4. **Visual neuroscience**: Understanding brain responses to natural images

### Research Applications

- Compare learning algorithms to biological learning
- Identify brain-like vs non-brain-like AI mechanisms
- Guide development of biologically plausible learning rules
- Validate representational alignment in self-supervised models

## Technical Details

### Gradient Extraction

- Standard backpropagation through vision model
- Extract layer-wise gradient representations
- Normalize and prepare for encoding analysis

### Encoding Analysis

- Linear regression: gradient features → neural responses
- Cross-validation for prediction accuracy
- ROI-based spatial analysis
- Time-window-based temporal analysis

## Pitfalls

### Common Issues

1. **Gradient instability**: Small changes in input → large gradient changes
2. **Layer selection**: Which layer gradients best predict brain responses
3. **Temporal alignment**: MEG latency windows must match gradient computation timing

### Mitigation Strategies

- Use self-supervised models (more stable gradients)
- Validate across multiple models
- Apply regularization in encoding regression
- Use appropriate temporal windows based on model architecture

## Related Work

- Predictive coding frameworks
- Brain-DNN representational alignment
- Self-supervised learning in vision models
- Biological plausibility of deep learning

## Future Directions

- Test alternative learning algorithms (predictive coding, Hebbian)
- Compare different model architectures
- Extend to other sensory modalities
- Develop gradient-based brain mapping standards

## Activation Keywords

- `backpropagation`, `brain hierarchy`, `gradient encoding`
- `fMRI MEG`, `visual cortex`, `brain-DNN alignment`
- `biological plausibility`, `self-supervised vision`