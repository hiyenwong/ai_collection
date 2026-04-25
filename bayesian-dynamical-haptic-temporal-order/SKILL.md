---
name: bayesian-dynamical-haptic-temporal-order
description: "Bayesian dynamical framework for modeling time-order effects in haptic perception with temporal integration. Activation: brain model, neural scaling, multimodal brain, fMRI, EEG, neural encoding."
---

# Modelling time-order effects in haptic perception with a Bayesian dynamical framework

> Bayesian dynamical framework for modeling time-order effects in haptic perception with temporal integration

## Metadata
- **Source**: arXiv:2604.19662
- **Authors**: Gastón Avetta, Jose Lobera, Juan José Zárate, Inés Samengo, Damián G. Hernández
- **Published**: 2026-04-21

## Core Methodology

### Key Innovation
Perceptual judgments of sequential stimuli are systematically biased by prior expectations and by the temporal structure of sensory input. In haptic discrimination tasks, these effects often manifest as time-order asymmetries, whereby the perceived difference between two stimuli depends on their presentation order. Here, we introduce a dynamical Bayesian model that accounts for these biases by combining noisy sensory measurements with an evolving internal representation of stimulus intensity. Th

### Technical Framework
Based on the paper arXiv:2604.19662, this methodology introduces novel approaches to computational neuroscience and brain network analysis. The framework integrates data-driven methods with theoretical neuroscience principles.

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
# Reference: arXiv:2604.19662
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
- arXiv: 2604.19662 — [Modelling time-order effects in haptic perception with a Bayesian dynamical framework](https://arxiv.org/abs/2604.19662)
- PDF: [Download](https://arxiv.org/pdf/2604.19662)
