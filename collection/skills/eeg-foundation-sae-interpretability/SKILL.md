---
name: eeg-foundation-sae-interpretability
description: "Mechanistic interpretability of EEG foundation models using Sparse Autoencoders (SAEs). Use when: interpreting EEG foundation model internals, extracting clinically-meaningful features from neural networks, applying mechanistic interpretability to neuroimaging models, understanding what EEG models learn, SAE feature analysis for clinical trust. Trigger: EEG interpretability, sparse autoencoder EEG, EEG foundation model analysis, mechanistic interpretability neuroimaging, clinical trust EEG models, TopK SAE neural signals, brain model features. arXiv: 2605.13930 (May 2026)"
---

# Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders

## Overview

This paper (arXiv:2605.13930, May 2026) applies TopK Sparse Autoencoders (SAEs) to decode the internal representations of EEG foundation models, bridging the gap between high clinical performance and clinical trust.

## Key Contributions

### Methodology

- Applied TopK SAEs across three architecturally distinct EEG foundation models
- Discovered interpretable features corresponding to known clinical EEG patterns
- MSAE (Multi-Scale SAE) captures both temporal and frequency-domain features
- Features map to clinically-relevant phenomena: sleep spindles, K-complexes, epileptiform discharges

### Key Findings

1. **Feature Decomposition**: SAEs decompose black-box representations into human-interpretable components
2. **Cross-Architecture Consistency**: Similar features emerge across different model architectures
3. **Clinical Alignment**: Discovered features correlate with expert-annotated clinical markers
4. **Downstream Utility**: SAE features can be used for feature-based classification with improved interpretability

### Technical Approach

- **TopK Sparsity**: Enforces sparse activation (K active features per input)
- **Multi-Scale Analysis**: Captures both fine-grained and coarse neural patterns
- **Cross-Model Comparison**: Validates features are model-agnostic, not architecture artifacts

### Clinical Impact

- Provides transparency for clinical adoption of EEG foundation models
- Enables feature-based quality control and failure mode analysis
- Supports regulatory compliance for medical AI systems

## Implementation Notes

### SAE Configuration

- Sparsity parameter: TopK with K=32-128 (task-dependent)
- Dictionary size: 4x-16x expansion of hidden dimension
- Training: Reconstruction loss + L0 sparsity penalty
- Normalization: LayerNorm before SAE input

### Feature Analysis Pipeline

1. Train SAE on frozen foundation model activations
2. Extract feature dictionaries across layers
3. Map features to clinical concepts via correlation analysis
4. Validate with expert neurologist annotations

## Related Work

- Extends SAE interpretability from language models to neuroimaging
- Complements LRP (Layer-wise Relevance Propagation) for EEG
- Builds on EEG foundation model adapter methods

## Activation Keywords

- EEG interpretability
- sparse autoencoder EEG
- EEG foundation model analysis
- mechanistic interpretability neuroimaging
- clinical trust EEG models
- TopK SAE neural signals
- brain model features
- EEG black box interpretation
