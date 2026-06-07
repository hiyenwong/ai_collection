---
name: eeg-sae-interpretability
description: "Mechanistic interpretability of EEG foundation models via sparse autoencoders. Extracting interpretable features from EEG foundation model internal representations using sparse autoencoder decomposition. Use when: interpreting EEG foundation models, extracting clinically meaningful features from EEG, understanding neural network representations of EEG signals, mechanistic analysis of neural signal processing."
---

# EEG Foundation Model Interpretability via Sparse Autoencoders

**arXiv**: 2605.13930
**Authors**: William Lehn-Schiøler, Magnus Ruud Kjær, Rahul Thapa
**Published**: 2026-05-13
**Categories**: q-bio.NC, cs.LG, eess.SP

## Overview

EEG foundation models achieve state-of-the-art clinical performance, yet their internal computations remain opaque. This paper applies sparse autoencoder (SAE) decomposition to extract interpretable features from EEG foundation model activations, bridging the gap between performance and interpretability in clinical neural signal processing.

## Core Concepts

### Sparse Autoencoder Decomposition
- **SAE Architecture**: Overcomplete dictionary learning that decomposes model activations into sparse, interpretable features
- **Feature Discovery**: Automatic identification of clinically meaningful patterns in EEG representations
- **Activation Analysis**: Understanding how EEG foundation models encode neural signal characteristics

### Key Innovation
- First application of SAE-based interpretability to EEG foundation models
- Discovers human-interpretable features corresponding to known EEG phenomena
- Enables mechanistic understanding of model predictions in clinical contexts
- Provides auditability for medical AI systems

## Methodology

### SAE Training Pipeline
1. **Activation Collection**: Extract internal activations from EEG foundation model on diverse dataset
2. **Dictionary Learning**: Train overcomplete autoencoder with sparsity constraints on activations
3. **Feature Interpretation**: Analyze learned dictionary elements for clinical correspondence
4. **Feature Attribution**: Map discovered features to model predictions and clinical outcomes

### Feature Types Discovered
- **Physiological patterns**: Sleep spindles, K-complexes, epileptiform discharges
- **Frequency-band features**: Alpha, beta, delta, theta oscillation encodings
- **Artifact features**: Eye movement, muscle activity, line noise representations
- **Clinical markers**: Seizure precursors, sleep stage indicators, pathological patterns

## Applications

### Clinical Interpretability
- Understanding EEG model decisions in seizure detection
- Explaining sleep staging predictions
- Auditing model behavior across patient populations

### Feature Discovery
- Automated identification of clinically relevant EEG patterns
- Discovery of novel biomarkers from model representations
- Validation against expert-labeled EEG annotations

### Model Debugging
- Identifying failure modes through feature activation analysis
- Detecting bias in EEG model predictions
- Understanding cross-dataset generalization through feature consistency

## Implementation Considerations

### SAE Configuration
- Dictionary size relative to activation dimensionality
- Sparsity penalty tuning for feature interpretability
- Training data diversity for comprehensive feature discovery

### EEG Model Compatibility
- Works with transformer-based EEG foundation models
- Applicable to any model with accessible internal activations
- Feature discovery quality depends on model representational capacity

### Clinical Validation
- Cross-reference discovered features with expert EEG annotations
- Validate feature-clinical outcome relationships
- Assess feature stability across recording protocols

## Activation Keywords

- EEG foundation model interpretability
- sparse autoencoder EEG
- mechanistic interpretability EEG
- EEG feature extraction
- clinical EEG model auditing
- EEG representation analysis
- sparse dictionary EEG features
- neural signal interpretability

## Related Skills

- eeg-foundation-sae-interpretability: Mechanistic interpretability of EEG foundation models via SAE
- eeg-foundation-model-adapters: EEG foundation models with domain adaptation
- neural-encoding-evaluation-ground-truth: Evaluation framework for neural encoding models

## References

- arXiv: 2605.13930
- Sparse Autoencoders: Bricken et al. (2023)

## Pitfalls

- **Feature entanglement**: SAE features may still be entangled; use additional analysis techniques
- **Clinical validation required**: Discovered features need expert verification before clinical use
- **Dataset bias**: Features reflect training data distribution; may not generalize to all populations
- **Computational cost**: SAE training on large EEG foundation models requires significant resources
- **Activation sampling**: Ensure diverse activation coverage for comprehensive feature discovery
