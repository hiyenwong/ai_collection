---
name: face-perception-inverse-generative
description: >
  Human face perception methodology using controversial stimulus pairs to distinguish
  between theoretically distinct DNN models. Shows that human face perception is shaped
  by inverse-generative mechanisms that infer latent causes of facial appearance and
  discount nuisance variation, tuned by natural image statistics. arXiv:2605.12619.
category: neuroscience
tags: [face-perception, inverse-rendering, neural-representations, DNN-neuroscience,
       representational-similarity, controversial-stimuli, ventral-stream]
related_skills:
  - neuroscience-of-transformers
  - vlm-visual-cortex-alignment-robustness
  - neural-encoding-evaluation-ground-truth
activation_keywords:
  - face perception inverse generative
  - inverse rendering face perception
  - controversial face pairs
  - human face dissimilarity judgments
  - natural image statistics face perception
  - neural representations face recognition
  - DNN face perception models
---

# Face Perception via Inverse-Generative and Naturalistic Discriminative Objectives

**Paper**: *Human face perception reflects inverse-generative and naturalistic discriminative objectives*
**Authors**: Wenxuan Guo, Heiko H. Schutt, Kamila Maria Jozwik, Katherine R. Storrs, Nikolaus Kriegeskorte, Tal Golan
**arXiv**: 2605.12619 (May 12, 2026)
**Category**: q-bio.NC, cs.CV

## Overview

This paper addresses what computational objectives shape human face perception. By comparing
six DNN models trained on distinct tasks using **controversial face pairs** (optimized to elicit
contrasting model predictions) rather than randomly sampled faces, the study reveals that
human face perception is shaped by inverse-generative mechanisms that infer latent causes of
facial appearance.

## Core Problem

Theoretically distinct DNN models often make indistinguishable representational predictions
for randomly sampled faces. Standard RSA with random stimuli cannot expose diagnostic
differences among competing computational hypotheses about face perception.

## Key Innovation: Controversial Stimuli

**Controversial pairs** are face pairs specifically optimized to maximize disagreement between
model predictions. This diagnostic approach reveals which computational objectives best
match human perceptual judgments.

## Methodology

### Models Compared (6 models, shared architecture, different objectives)
1. **Inverse rendering** - infers latent 3D causes of facial appearance
2. **Face identification** - identity classification
3. **Object classification** - general object categorization
4. **Self-supervised** - contrastive learning
5. **Pixel reconstruction** - autoencoder-style
6. **Random/naive** - baseline

### Experimental Design
- 864 human participants for face-dissimilarity judgments
- Stimulus sets varying in realism and pose variation
- Controversial pairs + random pairs for comparison
- RSA between model representations and human judgments

## Key Findings

1. **Inverse-generative models win**: Models trained on inverse rendering, face ID, or object
   classification most robustly matched human judgments
2. **Natural image advantage**: Models trained on natural images outperformed synthetic-trained
3. **Controversial pairs are diagnostic**: Random pairs cannot distinguish competing models
4. **Latent cause inference**: Face perception infers underlying 3D structure, discounts nuisance
5. **Natural statistics tuning**: Face perception is tuned by natural image statistics

## Core Principle

Human face perception reflects **inverse problem solving** - the brain infers latent causal
structure (identity, 3D shape) from appearance, rather than mere pattern matching.

## Workflow for Agents

### Controversial Stimuli Design Pattern
```
1. Train multiple models with different objectives
2. Find input pairs that maximize disagreement between models
3. Collect human perceptual judgments on these diagnostic pairs
4. Compare model RSA matrices against human judgments
5. The model that best predicts human dissimilarity wins
```

## Applications

1. Visual neuroscience - understanding ventral stream computation
2. Computer vision - designing human-aligned vision systems
3. AI safety - understanding AI vs human perception divergence
4. Computational psychiatry - modeling face perception deficits

## Pitfalls

1. **Random stimuli are non-diagnostic** - cannot distinguish competing hypotheses
2. **Natural vs synthetic gap** - natural image training consistently outperforms synthetic
3. **Inverse rendering is computationally expensive** - winning model type is most costly

## References

- arXiv:2605.12619 (Guo et al., 2026)
- Kriegeskorte et al. (2008): Representational Similarity Analysis
