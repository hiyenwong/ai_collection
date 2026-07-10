---
name: self-initiated-attention-shifts-eeg
description: Subject-specific analysis of self-initiated attention shifts from EEG with controlled internal and external attention conditions. Machine learning + SHAP feature attribution reveals that higher-frequency bands and frontal regions carry subject-specific discriminative information for distinguishing self-initiated vs externally-cued attention shifts (arXiv:2605.18251). Use for EEG attention decoding, self-initiated attention research, voluntary attention neural correlates, SHAP-based EEG interpretation.
---

# Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG

Research methodology from paper: Zeng, Hou, Zhang, Sun, Huang, Tseng, Shioiri (May 2026). arXiv:2605.18251

## Overview

Self-initiated attention shifts are critical for voluntary behavior but difficult to study due to absence of explicit temporal markers. This study investigates whether preparatory EEG activity can distinguish self-initiated shifts from externally instructed shifts under identical visual stimulation.

## Key Contributions

### Experimental Paradigm
- Controlled comparison between task-constrained self-initiated shifts and externally instructed shifts
- Identical visual stimulation for both conditions
- Enables isolation of neural correlates of self-initiation

### Analytical Approach
- **Performance-oriented assessment**: Frequency-specific topographic patterns across multi-dimensional EEG features
- **Model-based feature attribution**: SHAP (SHapley Additive exPlanations) analysis for interpretable feature importance
- Structured view of how spectral features across regions of interest contribute to model behavior

### Key Findings
- **Reliable within-subject classification**: Preparatory EEG contains subject-specific discriminative information
- **Higher-frequency bands** (beta, gamma) contribute strongly to model decisions
- **Frontal regions** show strongest discriminative power
- Subject-specific patterns require individualized models

## Methodology

1. EEG recording during attention shift task (self-initiated vs externally-cued)
2. Spectral feature extraction across frequency bands and regions
3. Within-subject classification pipeline
4. SHAP-based feature attribution analysis

## Activation
- self-initiated attention, EEG attention decoding, voluntary attention, SHAP EEG, frontal EEG attention, preparatory EEG, attention shift classification, subject-specific EEG, frequency-specific topography, EEG feature attribution

## References
- arXiv:2605.18251 - https://arxiv.org/abs/2605.18251
