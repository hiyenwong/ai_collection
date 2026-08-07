---
name: layered-surprise-cascades-predictive-coding
title: Layered Surprise Cascades Predictive Coding
version: 1.0.0
description: Biologically plausible framework for hierarchical predictive coding using local contrastive learning and activity cancellation, based on the Forward-Forward algorithm with inverted objective.
author: Andrew L. Smith, Linxing Preston Jiang, Jason K. Eshraghian, Matthew S. Bull, Stefano Recanatesi
arxiv_id: 2608.05481
date: 2026-08-07
tags:
  - predictive coding
  - surprise cascades
  - forward-forward algorithm
  - contrastive learning
  - neural dynamics
  - cortical computation
  - three-factor Hebbian learning
---

# Layered Surprise Cascades Predictive Coding

## Overview

This methodology presents a biologically plausible framework for hierarchical predictive coding that emerges from local contrastive learning and simple activity cancellation. Building on the Forward-Forward (FF) algorithm, it uses an inverted objective that increases activity for negative data, yielding predictive representations across layers that capture hallmark features of cortical computation.

## Key Contributions

### Biological Plausibility
- **No error-coding neurons required**: Unlike classical predictive coding models that rely on dedicated error neurons
- **No weight symmetry**: Eliminates the need for symmetric feed-forward and feedback weights
- **Local synaptic learning**: Uses only local synaptic updates with a simple global signal
- **Three-factor Hebbian rule**: Mathematically equivalent to established principles of synaptic plasticity where updates depend on pre-synaptic activity, post-synaptic activity, and global gating

### Emergent Properties
- **Bottom-up surprise cascade**: Despite top-down label delivery, the model learns bottom-up cancellation of predictable activity
- **Top-down modulation**: Captures cortical top-down modulation effects
- **Surprise signaling**: Amplifies responses to unexpected inputs while suppressing expected ones
- **Hierarchical prediction**: Builds layered predictions that minimize surprise across the hierarchy

### Mathematical Foundation
The local contrastive objective is proven to be mathematically equivalent to a three-factor Hebbian learning rule:
```
Δw_ij ∝ x_i * y_j * g
```
Where:
- `x_i` = pre-synaptic activity
- `y_j` = post-synaptic activity  
- `g` = global gating signal (positive for negative data, negative for positive data)

## Implementation Guidelines

### Architecture
- Use recurrent Forward-Forward networks with inverted objective
- Implement local contrastive learning at each layer
- Apply activity cancellation mechanisms between layers
- Ensure global signal can modulate learning based on data positivity/negativity

### Training Procedure
1. **Positive phase**: Present real data, apply negative global signal to decrease activity
2. **Negative phase**: Present corrupted/noisy data, apply positive global signal to increase activity  
3. **Local updates**: Perform synaptic updates using three-factor Hebbian rule at each layer
4. **Hierarchical propagation**: Allow cancellation signals to propagate bottom-up while predictions flow top-down

### Validation Metrics
- Measure surprise amplification across layers for unexpected inputs
- Verify suppression of predictable features in early layers
- Test top-down modulation effects on lower layer responses
- Evaluate reconstruction quality and prediction accuracy

## Applications

### Neuroscience Research
- Model cortical predictive processing without biologically implausible assumptions
- Generate testable hypotheses about neural surprise signaling
- Bridge machine learning advances with neuroscientific observations

### Machine Learning
- Develop more biologically plausible deep learning architectures
- Create efficient predictive models for time-series forecasting
- Build robust anomaly detection systems based on surprise cascades

## Experimental Predictions

1. **Neural recordings should show**: Bottom-up waves of activity suppression followed by surprise amplification
2. **Synaptic plasticity experiments**: Should reveal three-factor learning rules with global neuromodulatory signals
3. **Perturbation studies**: Disrupting global signals should impair hierarchical prediction without affecting local learning

## References

- Smith, A. L., Jiang, L. P., Eshraghian, J. K., Bull, M. S., & Recanatesi, S. (2026). From Local Learning to Global Prediction Through Layered Surprise Cascades. arXiv:2608.05481 [q-bio.NC].
- Hinton, G. E. (2022). The Forward-Forward Algorithm: Some Preliminary Investigations. arXiv:2212.13345.
- Rao, R. P., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. Nature neuroscience, 2(1), 79-87.

## Activation Keywords

Use when: implementing biologically plausible predictive coding, studying surprise cascades in neural networks, developing contrastive learning with hierarchical structure, modeling cortical top-down modulation, or exploring three-factor Hebbian learning rules.