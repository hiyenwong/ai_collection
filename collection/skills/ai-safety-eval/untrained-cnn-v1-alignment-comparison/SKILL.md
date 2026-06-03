---
name: untrained-cnn-v1-alignment-comparison
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained networks at V1 visual cortex representations. Activation: brain model, neural scaling, multimodal brain, fMRI, EEG, neural encoding."
---

# Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI

> Systematic RSA comparison showing untrained CNNs match backpropagation-trained networks at V1 visual cortex representations

## Metadata
- **Source**: arXiv:2604.16875
- **Authors**: Nils Leutenegger
- **Published**: 2026-04-18

## Core Methodology

### Key Innovation
A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules -- backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) -- applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (

### Technical Framework
Based on the paper arXiv:2604.16875, this methodology introduces novel approaches to computational neuroscience and brain network analysis. The framework integrates data-driven methods with theoretical neuroscience principles.

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
# Reference: arXiv:2604.16875
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
- arXiv: 2604.16875 — [Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI](https://arxiv.org/abs/2604.16875)
- PDF: [Download](https://arxiv.org/pdf/2604.16875)
