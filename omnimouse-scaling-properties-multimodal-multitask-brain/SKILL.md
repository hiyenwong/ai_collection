---
name: omnimouse-scaling-properties-multimodal-multitask-brain
description: "OmniMouse scaling properties of multi-modal multi-task brain models trained on 150B neural tokens from 3.1M neurons across 73 mice. Activation: brain model, neural scaling, multimodal brain, fMRI, EEG, neural encoding."
---

# OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens

> OmniMouse scaling properties of multi-modal multi-task brain models trained on 150B neural tokens from 3.1M neurons across 73 mice

## Metadata
- **Source**: arXiv:2604.18827
- **Authors**: Konstantin F. Willeke, Polina Turishcheva, Alex Gilbert, Goirik Chakrabarty, Hasan A. Bedel et al. (21 authors)
- **Published**: 2026-04-20

## Core Methodology

### Key Innovation
Scaling data and artificial neural networks has transformed AI, driving breakthroughs in language and vision. Whether similar principles apply to modeling brain activity remains unclear. Here we leveraged a dataset of 3.1 million neurons from the visual cortex of 73 mice across 323 sessions, totaling more than 150 billion neural tokens recorded during natural movies, images and parametric stimuli, and behavior. We train multi-modal, multi-task models that support three regimes flexibly at test t

### Technical Framework
Based on the paper arXiv:2604.18827, this methodology introduces novel approaches to computational neuroscience and brain network analysis. The framework integrates data-driven methods with theoretical neuroscience principles.

## Implementation Guide

### Prerequisites
- Python 3.9+
- PyTorch / JAX
- NumPy, SciPy

### Step-by-Step
1. **Data Preparation**: Load neural data (fMRI volumes / EEG signals / spike trains)
2. **Preprocessing**: Apply standard neuroimaging preprocessing pipelines
3. **Model Configuration**: Set up the architecture following paper specifications
4. **Training**: Train with recommended hyperparameters from the paper
5. **Evaluation**: Use cross-validation with appropriate brain parcellations

### Code Example
```python
# Reference: arXiv:2604.18827
import numpy as np

# Placeholder for core algorithm
# See paper for detailed implementation
```

## Applications
- Brain network analysis and connectomics
- Neural signal decoding and encoding
- Clinical neuroimaging biomarker discovery
- Neuromorphic computing and brain-inspired AI

## Pitfalls
- Batch effects and site-related confounds in multi-site neuroimaging data
- Individual variability in brain anatomy requires careful alignment
- Temporal autocorrelation in fMRI violates independence assumptions

## Related Skills
- [[brain-dit-fmri-foundation-model]]
- [[snn-learning-survey]]
- [[neural-population-decoding]]
- [[brain-network-controllability]]

## References
- arXiv: 2604.18827 — [OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens](https://arxiv.org/abs/2604.18827)
- PDF: [Download](https://arxiv.org/pdf/2604.18827)
