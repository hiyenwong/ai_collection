---
name: hebbian-incremental-audio-learning
version: 1.0.0
description: "Incremental learning for audio classification using Hebbian Deep Neural Networks. Proposes kernel plasticity approach that selectively modulates network kernels during incremental learning — acting on selected kernels to learn new information while others retain previous knowledge. Based on ESC-50 dataset validation. arXiv:2604.18270."
date: 2026-04-23
arxiv_id: "2604.18270"
authors: "Riccardo Casciotti, Francesco De Santis, Alberto Antonietti, Annamaria Mesaros"
categories: "eess.AS, cs.LG"
activation:
  - Hebbian learning
  - incremental learning
  - continual learning audio
  - kernel plasticity
  - sound classification
  - catastrophic forgetting
  - biologically inspired learning
  - ESC-50
---

# Incremental Learning for Audio Classification with Hebbian Deep Neural Networks

## Overview
Applies biologically inspired **Hebbian learning** to continual/incremental audio classification. Proposes a **kernel plasticity approach** that selectively modulates convolutional kernels — some kernels learn new classes while others remain frozen to retain prior knowledge, mitigating catastrophic forgetting.

## Key Methodology

### Hebbian Learning Rules
- **Classic Hebb**: Δw = η · x · y (co-activation strengthens synapses)
- **Oja's rule**: Adds normalization to prevent unbounded growth
- **Modulated Hebbian**: Combines with top-down modulatory signals

### Kernel Plasticity Approach
1. **Initialize** DNN with convolutional layers for audio spectrogram input
2. **Phase 1 training**: Train base task using standard backprop
3. **Incremental phases**:
   - **Freeze** kernels most important for previous tasks (measured by gradient magnitude)
   - **Allow plasticity** in remaining kernels for new task learning
   - Apply Hebbian update rules to plastic kernels
4. **Readout update**: Only update classification head for new classes

### Selective Modulation Strategy
- Rank kernels by importance to previous tasks
- High-importance kernels → frozen (preserves old knowledge)
- Low-importance kernels → plastic (learns new information)
- Importance metric: gradient-based saliency or activation statistics

### Audio-Specific Design
- Input: Mel spectrograms or log-mel features
- Architecture: CNN backbone + classification head
- Incremental scenarios: Class-incremental, task-incremental

## Implementation Steps
1. Prepare audio dataset as Mel spectrograms
2. Build CNN with separable plastic/frozen kernel groups
3. Train initial task with backprop
4. For each new task: compute kernel importance, freeze top-k, apply Hebbian updates to rest
5. Evaluate on all seen classes (class-incremental setting)

## Advantages
- Biologically plausible learning mechanism
- Mitigates catastrophic forgetting without replay buffers
- Competitive performance on ESC-50 benchmark
- Lower memory footprint than replay-based methods

## Pitfalls
- Kernel selection threshold requires tuning
- Performance degrades with many incremental steps
- Hebbian rules may not capture complex feature hierarchies
- Audio domain specificity may limit generalization

## References
- arXiv: [2604.18270](https://arxiv.org/abs/2604.18270)
- Key terms: Hebbian learning, continual learning, audio classification, catastrophic forgetting, kernel plasticity, ESC-50
