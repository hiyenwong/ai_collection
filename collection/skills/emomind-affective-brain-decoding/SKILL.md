---
name: emomind-affective-brain-decoding
description: "End-to-end pipeline for decoding affective captions directly from fMRI signals using continuous emotion vectors and classifier-free guidance rewriting. Use when: brain-to-text with emotion/affect, fMRI affective decoding, continuous emotion representation from brain signals, individualized affective caption generation, classifier-free guidance for neural decoding. Activation: emomind, affective brain decoding, emotion fMRI, brain-to-text emotion, affective caption, continuous emotion vector, classifier-free guidance neural."
---

# EmoMind: Decoding Affective Captions from Brain fMRI

> First end-to-end pipeline for decoding affective captions directly from fMRI signals using continuous 34D emotion vectors, outperforming label-prompted GPT-4 across subject-specificity, structural geometry, and causal control axes.

## Metadata
- **Source**: arXiv:2605.16739
- **Authors**: Bilal A. Mohammed, Lin Gu, Ruogo Fang
- **Published**: 2026-05-16

## Core Problem

Brain-to-text systems recover semantic content but discard affect. Language models can generate emotional text from categorical labels, but labels collapse rich inter-subject variability into coarse discrete bins.

## Key Innovation

**Continuous emotion representation** vs discrete labels:
- Decode a 34-dimensional continuous emotion vector from fMRI
- Avoids information loss from categorization
- Preserves individual affective structure

## Methodology: Two-Stage Pipeline

### Stage 1: Neutral Scene Description Retrieval
- Brain-decoded visual features → semantically grounded neutral scene description
- Standard brain-to-text for content (no affect)

### Stage 2: Affective Rewriting with Classifier-Free Guidance
- Rewrite neutral description using decoded continuous emotion vector
- **Classifier-free guidance** trained against identity-preserving null branch
- Enables smooth interpolation between semantic fidelity and affective expressivity

### Three-Axis Validation Framework
1. **Subject-specificity**: Does the model capture person-specific affective structure?
2. **Structural geometry**: Does the emotion space geometry match neural representations?
3. **Causal control**: Can we causally manipulate affect while preserving content?

### Synthetic-Brain Substitution Test
- Probes robustness to measurement apparatus
- Tests generalization beyond specific fMRI acquisition

## Applications
- Personalized emotion-aware neural interfaces
- Individualized affective brain organization research
- Brain-computer interfaces with emotional state decoding
- Affective neuroscience with continuous emotion measurement

## Pitfalls
- **Emotion dimensionality**: 34D vector may be dataset-specific; validate dimensionality for new datasets
- **Cross-subject generalization**: Largest gains are on person-specific metrics — population-level aggregation loses value
- **fMRI temporal resolution**: Affective states may evolve faster than fMRI sampling rate
- **Semantic-affect balance**: Classifier-free guidance parameter critically controls the trade-off

## Related Skills
- brain-dit-fmri-foundation-model
- brain-to-speech-prosody-feature-engineering
- neural-encoding-evaluation-ground-truth
