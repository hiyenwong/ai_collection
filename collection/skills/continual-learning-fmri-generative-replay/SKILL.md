---
name: continual-learning-fmri-generative-replay
description: "Functional connectivity-aware generative replay framework for continual learning of brain disorder diagnosis from fMRI data without catastrophic forgetting. Activation: Multi-disorder diagnosis, Adaptive BCI systems."
---

# Continual Learning for fMRI Brain Disorder Diagnosis via Generative Replay

> Functional connectivity-aware generative replay framework for continual learning of brain disorder diagnosis from fMRI data without catastrophic forgetting.

## Metadata
- **Source**: arXiv:2604.14259v1
- **Authors**: Qianyu Chen, Shujian Yu
- **Published**: 2026-04-15
- **Categories**: q-bio.TO, cs.LG, eess.IV

## Core Methodology

### Key Innovation
### Core Method
Generative replay with functional connectivity awareness:

1. **FC-Aware Generator**: Generates synthetic fMRI data preserving functional connectivity patterns
2. **Experience Replay**: Stores and replays representative examples from previous tasks
3. **Modular Architecture**: Task-specific adapters that don't interfere
4. **Regularization**: EWC or similar regularization preventing weight drift

### Technical Framework
- **Generator**: VAE or GAN conditioned on functional connectivity matrices
- **Feature Extractor**: Graph neural network for FC representation
- **Classifier**: Task-specific classification heads
- **Memory Buffer**: Experience replay buffer with importance sampling

## Implementation Guide

### Prerequisites
### Prerequisites
- PyTorch or TensorFlow
- Nilearn for fMRI processing
- PyTorch Geometric for GNNs
- fMRI datasets for multiple disorders

### Step-by-Step
1. **Preprocess fMRI**: Compute FC matrices
2. **Build Generator**: Train VAE/GAN on FC patterns
3. **Initialize Model**: Set up modular classification architecture
4. **Continual Training**: 
   - Train on Task 1
   - Generate synthetic data for Task 1 while training Task 2
   - Combine real and synthetic data
5. **Evaluate**: Test on all tasks sequentially

### Applications
- Multi-disorder diagnosis
- Adaptive BCI systems
- Longitudinal studies
- Rare disease learning

## Pitfalls
- Generator quality limits performance
- Computational cost increases with tasks
- May suffer from mode collapse

## Related Skills
- neuroscience-research-method
- brain-connectivity-analysis
- spiking-neural-networks

## References
- arXiv: https://arxiv.org/abs/2604.14259v1
