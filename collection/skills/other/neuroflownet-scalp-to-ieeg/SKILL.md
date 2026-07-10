---
name: neuroflownet-scalp-to-ieeg
title: "Non-Invasive Reconstruction of Intracranial EEG Across the Deep Temporal Lobe from Scalp EEG based on Conditional Normalizing Flow"
description: NeuroFlowNet — cross-modal generative framework using Conditional Normalizing Flow for reconstructing high-fidelity iEEG signals from non-invasive scalp EEG
tags:
  - eeg
  - ieeg
  - normalizing-flow
  - deep-brain-activity
  - cross-modal-reconstruction
  - temporal-lobe
  - computational-neuroscience
created: 2026-05-26
---

# NeuroFlowNet: Non-Invasive iEEG Reconstruction from Scalp EEG

**arXiv**: [2603.03354](https://arxiv.org/abs/2603.03354)
**Authors**: Dongyi He, Bin Jiang, Kecheng Feng, Luyin Zhang, Ling Liu, Yuxuan Li, Yun Zhao, He Yan
**Subjects**: Neurons and Cognition (q-bio.NC); Artificial Intelligence (cs.AI)

## Summary

This paper introduces NeuroFlowNet, the first framework to reconstruct high-fidelity intracranial EEG (iEEG) signals from the entire deep temporal lobe region using non-invasive scalp EEG (sEEG). Built on Conditional Normalizing Flow (CNF), the model directly learns complex conditional probability distributions through reversible transformations, explicitly capturing the inherent randomness of brain signals while avoiding pattern collapse issues common in generative models.

## Key Contributions

1. **First-ever iEEG Reconstruction**: Successfully reconstructs iEEG signals from the entire deep temporal lobe region using scalp EEG — a previously unexplored capability

2. **Conditional Normalizing Flow (CNF) Core**: Uses reversible transformations to model complex conditional probability distributions, explicitly capturing brain signal randomness

3. **Multi-Scale Architecture + Self-Attention**: Robustly captures fine-grained temporal details and long-range dependencies

4. **Pattern Collapse Avoidance**: CNF architecture fundamentally avoids pattern collapse issues common in existing generative models (e.g., GANs, VAEs)

## Methodology

- **Base Architecture**: Conditional Normalizing Flow (CNF)
- **Enhancements**: Multi-scale architecture + self-attention mechanisms
- **Training**: Supervised cross-modal generation from sEEG to iEEG
- **Validation Metrics**:
  - Temporal waveform fidelity
  - Spectral feature reproduction
  - Functional connectivity restoration

## Validation Results

- Validated on publicly available synchronized sEEG-iEEG dataset
- Demonstrates effectiveness across all three validation dimensions (waveform, spectrum, connectivity)
- Establishes more reliable and scalable paradigm for non-invasive deep brain analysis

## Implications

- Enables non-invasive access to deep brain dynamics without surgical implantation
- Potential clinical applications: epilepsy monitoring, deep brain stimulation targeting, psychiatric diagnosis
- Provides scalable alternative to invasive iEEG for neuroscience research
- Opens new possibilities for studying deep temporal lobe function non-invasively

## Activation Keywords

neuroflownet, scalp-to-ieeg, normalizing-flow-eeg, deep-brain-reconstruction, ieeg-reconstruction, cross-modal-eeg, temporal-lobe-ieeg, non-invasive-deep-brain, conditional-normalizing-flow-eeg
