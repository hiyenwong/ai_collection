---
name: prism-cross-subject-eeg-emotion
description: "PRISM framework for cross-subject EEG emotion recognition using prioritized channel importance and semi-supervised domain adaptation. Differentiable channel weighting via lightweight expert ensemble plus confidence-filtered pseudo-labels for label-efficient generalization across subjects. Activation: EEG emotion recognition, cross-subject BCI, channel selection, domain adaptation, PRISM, semi-supervised EEG"
metadata:
  arxiv_id: "2607.00358"
  published: "2026-07-01"
  authors: ["Xin Zhou", "Xiang Zhang", "Hao Deng", "Lijun Yin"]
  tags: [eeg, emotion-recognition, cross-subject, domain-adaptation, channel-selection, bci, semi-supervised]
license: Complete terms in LICENSE.txt
---

# PRISM: Prioritized Channel Importance with Semi-supervised Domain Adaptation for Cross-Subject EEG Emotion Recognition

## Core Contribution

A novel framework combining **differentiable channel importance weighting** with **semi-supervised domain adaptation** to solve two key obstacles in EEG emotion recognition: channel redundancy and inter-subject variability. Achieves state-of-the-art on DEAP, DREAMER, and SEED datasets with limited annotations.

## Architecture: Two-Pillar Design

### Pillar 1: Prioritized Channel Importance (Channel Side)

**Problem**: Standard EEG uses fixed channel sets with equal weighting. Many channels are redundant or subject-specific noise sources.

**Solution**: PRISM assigns differentiable, data-dependent channel weights via a lightweight expert ensemble:
- Multiple lightweight "expert" modules each specialize on different channel subsets
- Channel weights learned end-to-end via gradient descent
- Amplifies reliable electrodes while suppressing distractors
- Differentiable: weights adapt during training, not a fixed selection

**Key advantage over prior channel selection methods**: Most methods use discrete selection (keep/drop channels). PRISM uses continuous, differentiable weighting, allowing fine-grained importance scoring.

### Pillar 2: Semi-supervised Domain Adaptation (Domain Side)

**Problem**: Inter-subject variability means models trained on one subject perform poorly on others. Labeling EEG data is expensive.

**Solution**: Leverages unlabeled data through confidence-filtered pseudo-labels:
1. Generate pseudo-labels on unlabeled target-subject data using current model
2. **Confidence filtering**: Only retain pseudo-labels with prediction confidence above threshold
3. Use retained pseudo-labels for consistency regularization
4. Domain alignment via adversarial or MMD-based loss between source and target distributions
5. Iteratively refine as model improves

## Methodology Workflow

1. **Preprocessing**: Standard EEG preprocessing (bandpass filter, artifact removal, epoching)
2. **Feature extraction**: Time-frequency decomposition or raw signal input
3. **Channel weighting**: Forward pass through expert ensemble to get per-channel importance scores
4. **Supervised loss**: Cross-entropy on labeled source-subject data
5. **Pseudo-label generation**: Forward pass on unlabeled target data
6. **Confidence filtering**: Retain predictions with confidence > threshold tau
7. **Consistency regularization**: Enforce consistent predictions under input perturbations
8. **Domain alignment**: Minimize distribution discrepancy between source and target
9. **Joint optimization**: Total loss = L_sup + lambda1 * L_consistency + lambda2 * L_domain

## Datasets and Results

| Dataset | Subjects | Channels | Emotions | Improvement over SOTA |
|---------|----------|----------|----------|----------------------|
| DEAP | 32 | 32 | Valence/Arousal | Significant cross-subject gains |
| DREAMER | 23 | 14 | Valence/Arousal/Dominance | Robust with limited labels |
| SEED | 15 | 62 | 3 classes | State-of-the-art generalization |

**Key result**: PRISM achieves robust cross-subject generalization given limited annotations (as few as 10-20% labeled target data).

## Pitfalls

### Confidence threshold sensitivity
The pseudo-label confidence threshold tau is critical: too low introduces noisy labels, too high wastes unlabeled data. Recommend warmup schedule: start high (0.9) and gradually decrease.

### Expert ensemble overhead
Multiple expert modules increase parameter count. Use lightweight experts (1-2 layer MLPs) to keep overhead minimal. Number of experts should match expected number of distinct channel importance patterns.

### Channel importance not transferable across emotions
Optimal channel subsets differ between valence vs arousal decoding. Train separate channel weights per emotion dimension or use multi-task learning.

### Pseudo-label confirmation bias
Early in training, model may generate systematically biased pseudo-labels that reinforce errors. Use exponential moving average (EMA) teacher model for more stable pseudo-labels.

## Related Skills

- [[eeg-channel-adaptation-benchmark]] - Channel adaptation methods for EEG
- [[cross-subject-eeg-decoding]] - Comprehensive survey of cross-subject EEG decoding
- [[eeg-test-time-adaptation-benchmark]] - Test-time adaptation for EEG models
- [[eeg-biomarker-robustness-cross-population]] - Cross-population robustness
