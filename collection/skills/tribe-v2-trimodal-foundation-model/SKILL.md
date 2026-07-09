---
name: tribe-v2-trimodal-foundation-model
description: >
  TRIBE v2 tri-modal foundation model methodology for in-silico neuroscience.
  Uses video, audio, and language modalities to predict human brain activity across
  naturalistic and experimental conditions. Supersedes linear encoding models with
  several-fold accuracy improvements. Enables in-silico experimentation and reveals
  multisensory integration topography. Activation: TRIBE v2, brain foundation model,
  in-silico neuroscience, multi-modal brain prediction, fMRI encoding model,
  multisensory integration, tri-modal neural model, neural encoding foundation.
---

# TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience

**Paper**: arXiv:2605.04326 (2026-05-05)
**Authors**: Stéphane d\'Ascoli, Jérémy Rapin, Yohann Benchetrit, Teon Brooks, Katelyn Begany
**Categories**: q-bio.NC, cs.LG

## Core Contribution

TRIBE v2 is a tri-modal (video, audio, language) foundation model that predicts
human brain activity across diverse experimental conditions, using a unified dataset
of 1000+ hours of fMRI across 720 subjects. It supersedes traditional linear
encoding models and enables in-silico experimentation.

## Key Findings

1. **Unified Multi-Modal Prediction**: Single model handles video, audio, and text
   stimuli, predicting high-resolution brain responses for novel stimuli, tasks,
   and subjects
2. **Several-Fold Accuracy Improvement**: Outperforms traditional linear encoding
   models by multiple factors
3. **In-Silico Experimentation**: Recovers established results from decades of
   empirical visual and neuro-linguistic research
4. **Interpretable Latent Features**: Extracts fine-grained topography of
   multisensory integration

## Architecture Principles

- **Tri-Modal Input**: Video, audio, and language encoders unified into shared
  latent space
- **Brain Mapping Layer**: Maps latent features to voxel-wise fMRI predictions
- **Subject Generalization**: Handles 720 subjects with cross-subject transfer
- **Naturalistic Stimuli**: Trained on naturalistic paradigms, not just controlled
  experiments

## Applications

1. **Encoding Model Replacement**: Use instead of traditional GLM/linear encoding
   for fMRI prediction tasks
2. **In-Silico Experiments**: Test hypotheses about brain responses without
   running new fMRI studies
3. **Multisensory Integration Analysis**: Extract latent features to study how
   brain integrates across sensory modalities
4. **Cross-Subject Transfer**: Predict brain activity for new subjects using
   learned subject embeddings

## Relationship to Prior Work

- Builds on original TRIBE (arXiv:2601.xxxx) single-modality approach
- Extends brain foundation model lineage (Brain-DiT series, neuroSTORM, etc.)
- Competes with other multi-modal brain models (M3D-BFS, MV-BrainFM)

## Testable Predictions

- Model should recover known visual hierarchy (V1→V4→IT) from video stimuli
- Language areas (Broca\'s, Wernicke\'s) should respond selectively to linguistic input
- Multisensory integration areas (STS, pSTS) should show enhanced responses
  to cross-modal stimuli

## Implementation Considerations

- Requires large-scale fMRI dataset (1000+ hours) for training
- Video/audio/language encoders need pre-training on naturalistic data
- Subject-specific adaptation layers may improve cross-subject generalization
- Validation on held-out subjects and novel stimuli is critical

## Related Skills

- `brain-dit-fmri-foundation-model` - fMRI foundation model series
- `eeg-foundation-model-adapters` - EEG foundation models
- `neuro-grounded-foundation-models` - neuroscience-grounded models
- `multimodal-brain-connectivity-gnn` - multi-modal brain analysis
