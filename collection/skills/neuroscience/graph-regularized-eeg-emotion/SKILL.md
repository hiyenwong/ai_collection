---
name: graph-regularized-eeg-emotion
description: "Graph-regularized deep learning framework for EEG-based emotion recognition with psychologically-grounded label structure. Introduces Graph Label Smoothing, Graph Laplacian Commuting Distance, and Sliced Wasserstein Distance regularization strategies. Use when working with EEG emotion classification, affective BCI, SEED datasets, emotion topology, or graph-regularized neural networks for affective computing."
metadata:
  arxiv_id: "2607.07773"
  published: "2026-07-08"
  authors: "Dongyang Kuang, Zizheng Ma, Yushan Zhang, Xiaocong Zeng"
  tags: [EEG, emotion-recognition, graph-regularization, affective-BCI, SEED, label-structure, sliced-wasserstein]
---

# Graph-Regularized EEG Emotion Recognition

## Overview

EEG-based emotion recognition framework that conceptualizes emotions as nodes in a graph where edges encode proximity based on dimensional emotion theories (e.g., valence-arousal space). Instead of treating emotion classes as isolated labels, it penalizes predictions that deviate from established emotion topology.

## Three Regularization Strategies

### 1. Graph Label Smoothing (GLS)
- **Mechanism**: Intuitive soft labeling based on emotion graph proximity
- **Complexity**: Lowest — simple label distribution smoothing
- **Effect**: Reduces overconfident wrong predictions to psychologically distant classes

### 2. Commuting Distance via Graph Laplacian (CDGL)
- **Mechanism**: Spectral graph theory — commute time distance on emotion graph
- **Complexity**: Medium — requires eigendecomposition of graph Laplacian
- **Effect**: Enforces that prediction errors respect graph topology (closer emotions = smaller penalty)

### 3. Sliced Wasserstein Distance (SWD)
- **Mechanism**: Optimal transport on emotion graph structure
- **Complexity**: Highest — projection-based Wasserstein computation
- **Effect**: Most principled — directly minimizes transport cost between prediction and ground truth distributions

## Architecture-Agnostic Application

Framework tested with three backbones:
- **AudioTransformer** (pure transformer)
- **Conformer** (CNN-transformer hybrid)
- **DCGNN** (causal graph neural network)

All show consistent improvement — the regularization is orthogonal to architecture choice.

## Results

- **SEED-IV** (4-class): Up to +5.42% accuracy, 39% reduction in psychologically implausible misclassifications
- **SEED-V** (5-class): Consistent gains across all backbone architectures
- Key benefit: Not just better accuracy — fewer *meaningfully wrong* errors (e.g., confusing joy with sadness vs. joy with neutral)

## Implementation Pattern

```python
# 1. Build emotion graph based on dimensional theory
emotion_graph = build_emotion_graph(dimensions=['valence', 'arousal', 'dominance'])

# 2. Choose regularization (trade-off: speed vs. principled)
if compute_budget == 'low':
    reg = GraphLabelSmoothing(emotion_graph)
elif compute_budget == 'medium':
    reg = CommutingDistanceRegularization(emotion_graph)
else:
    reg = SlicedWassersteinRegularization(emotion_graph)

# 3. Add to training loop
loss = task_loss(prediction, targets) + lambda_reg * reg(prediction, targets)
```

## Application Domains

- Affective brain-computer interfaces
- Mental health monitoring from EEG
- Emotion-aware HCI systems
- Multimodal emotion recognition (can extend to other modalities)
- Psychologically-grounded ML for any classification with structured labels

## Activation Keywords

`EEG emotion recognition`, `graph regularization`, `affective BCI`, `SEED dataset`, `emotion topology`, `Sliced Wasserstein`, `Graph Label Smoothing`, `psychologically-grounded labels`, `commuting distance`, `emotion classification`, `mental health monitoring`

## Pitfalls

- **Emotion graph construction**: Quality depends on accurate dimensional emotion theory — valence-arousal-dominance dimensions are most established
- **Lambda tuning**: Regularization strength needs careful tuning; too high can suppress task-specific learning
- **Computational overhead**: SWD regularization is most principled but adds training cost; GLS is recommended as baseline
- **Not limited to EEG**: Framework generalizes to any modality with structured label spaces (fMRI, facial expressions, audio)
- **Class imbalance**: Graph regularization may need adjustment if emotion classes are severely imbalanced
