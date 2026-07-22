---
name: spiking-neural-networks-fmri-visual-decoding
title: Spiking Neural Networks for fMRI-Based Visual Semantic Decoding
version: 1.0.0
description: Methodology for using Spiking Neural Network (SNN)-derived visual features as targets for fMRI-based visual semantic decoding, showing superior alignment with brain activity compared to traditional ANN features.
trigger_words:
  - "snn fmri decoding"
  - "spiking neural network brain decoding"
  - "fMRI visual semantic decoding"
  - "brain-decodable visual representations"
domain: neuroscience/computational-neuroscience
authors:
  - Jiahong Zhang
  - Jinning Zhao
  - Sijun Shen
  - Siyuan Xu
  - Bo Xu
  - Guoqi Li
paper_id: arXiv:2607.19170
date: 2026-07-21
---

# Spiking Neural Networks for fMRI-Based Visual Semantic Decoding

## Overview

This methodology investigates **Spiking Neural Network (SNN)-derived visual features** as alternative targets for fMRI-based visual semantic decoding. The research demonstrates that SNN-derived features exhibit stronger alignment with fMRI responses and significantly improve visual semantic decoding performance compared to traditional Artificial Neural Network (ANN) baseline features.

## Key Findings

### Performance Improvements
- **Feature-prediction error reduced** from 0.7707 (ANN) to 0.0282 (SNN)
- **Top-1 semantic decoding accuracy improved** from 0.1800 (ANN) to 0.4400 (SNN) on the GoD dataset
- Both **spiking neural dynamics** and **temporal simulation steps** contribute to the observed advantage

### Methodological Approach
- Uses the **same L2-regularized linear fMRI-to-feature decoder** across all models
- Only varies the **feature vectors used as regression targets**
- Compares ANN baseline with **four SNN variants** from the same architectural family
- SNN variants differ in their **spiking dynamics** while maintaining architectural consistency

## Implementation Steps

### 1. Model Selection and Training
- Select SNN architecture from the same family as your ANN baseline
- Ensure SNN variants have different spiking dynamics (e.g., different neuron models, time constants)
- Train SNN models on the same visual dataset as the ANN baseline

### 2. Feature Extraction
- Extract visual features from SNN models at the appropriate layer(s)
- For temporal SNNs, consider features across multiple time steps or aggregate temporal information
- Normalize features consistently with ANN baseline for fair comparison

### 3. fMRI-to-Feature Mapping
- Use **L2-regularized linear regression** to map fMRI responses to feature vectors
- Apply the same regularization parameters across ANN and SNN targets
- Validate mapping performance using cross-validation

### 4. Semantic Decoding Evaluation
- Evaluate downstream semantic decoding performance using standard metrics
- Compare against ANN baseline using identical evaluation protocols
- Perform ablation studies to isolate contributions of spiking dynamics vs. temporal simulation

## Best Practices

### Target Feature Design
- **Target feature design is crucial** for fMRI-based visual decoding success
- SNN-derived features provide more **brain-decodable visual representations**
- Consider the **biological plausibility** of SNN dynamics when selecting architectures

### Ablation Analysis
- Systematically test the contribution of:
  - Spiking neural dynamics
  - Temporal simulation steps  
  - Architectural differences
- This helps identify which aspects drive the performance improvement

### Dataset Considerations
- Results demonstrated on the **GoD dataset**
- Methodology should generalize to other fMRI visual decoding datasets
- Consider dataset-specific characteristics when applying this approach

## Applications

- **Brain-computer interfaces** for visual reconstruction
- **Neural decoding** of complex visual scenes
- **Computational neuroscience** studies of visual representation alignment
- **AI-neuroscience integration** for developing brain-inspired AI systems

## Activation Keywords

Use this skill when working with:
- fMRI-based visual semantic decoding
- Spiking Neural Networks for brain decoding
- Brain-AI alignment studies
- Visual representation learning with biological constraints
- Neural decoding target feature optimization

## References

- Zhang, J., Zhao, J., Shen, S., Xu, S., Xu, B., & Li, G. (2026). Spiking Neural Networks for fMRI-Based Visual Semantic Decoding. arXiv:2607.19170
- Related work on SNN biological plausibility and computational efficiency
- fMRI encoding/decoding methodologies and benchmarks