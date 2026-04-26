---
name: untrained-cnns-match-backprop-v1
description: "Representational Similarity Analysis (RSA) showing untrained CNNs can match backpropagation-trained models in early visual cortex (V1) alignment. Activation: Understanding neural coding in V1, Model selection for brain alignment."
---

# Untrained CNNs Match Backpropagation at V1: RSA Analysis

> Representational Similarity Analysis (RSA) showing untrained CNNs can match backpropagation-trained models in early visual cortex (V1) alignment.

## Metadata
- **Source**: arXiv:2604.16875v1
- **Authors**: Nils Leutenegger
- **Published**: 2026-04-18
- **Categories**: cs.LG, q-bio.NC

## Core Methodology

### Key Innovation
### Core Method
Systematic RSA comparison revealing:

1. **V1 Alignment**: Untrained CNNs achieve comparable V1 alignment to trained models
2. **Hierarchical Progression**: Deeper layers show increasing training dependence
3. **Random Feature Hypothesis**: Early visual representations may rely on generic Gabor-like filters
4. **Backpropagation Role**: Training primarily improves higher-level representations

### Technical Framework
- **Models**: VGG, ResNet, AlexNet (trained vs. random weights)
- **Brain Data**: fMRI or ECoG recordings from human V1 during visual stimulation
- **RSA**: Correlation between model and neural RDMs (Representational Dissimilarity Matrices)
- **Stimuli**: Natural images with controlled visual properties

## Implementation Guide

### Prerequisites
### Prerequisites
- Pre-trained CNN models (PyTorch/TensorFlow)
- fMRI or ECoG data from V1
- Representational Similarity Analysis tools (rsatoolbox, nilearn)
- Statistical testing framework

### Step-by-Step
1. **Load Models**: Load pre-trained and randomly initialized CNNs
2. **Extract Activations**: From multiple layers for stimulus set
3. **Compute RDMs**: For each model layer
4. **Neural RDMs**: Compute from brain data
5. **Compare**: Correlate model and neural RDMs
6. **Statistical Testing**: Test significance of alignment differences

### Applications
- Understanding neural coding in V1
- Model selection for brain alignment
- Theoretical neuroscience
- Computational modeling

## Pitfalls
- Results specific to V1 (not generalizable to higher areas)
- Stimulus set dependent
- May not hold for all CNN architectures

## Related Skills
- neuroscience-research-method
- brain-connectivity-analysis
- eeg-decoding-brain-computer-interface

## References
- arXiv: https://arxiv.org/abs/2604.16875v1
