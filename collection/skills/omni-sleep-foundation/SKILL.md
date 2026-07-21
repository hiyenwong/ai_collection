---
name: omni-sleep-foundation
description: "Omni-Sleep sleep foundation model methodology using CNS/ANS hierarchical contrastive learning for topology-constrained multimodal PSG representation learning. Use when working with sleep staging, affective BCI, polysomnography analysis, CNS-ANS dynamics, multimodal biosignal foundation models, or physiological hierarchy in representation learning."
metadata:
  arxiv_id: "2607.07720"
  published: "2026-07-04"
  authors: "Zhoujie Hou, Song Wang, Kexin Lou, Mo Wang, Chen Wei, Quanying Liu"
  tags: [sleep-foundation-model, CNS-ANS, polysomnography, contrastive-learning, EEG, multimodal]
---

# Omni-Sleep: Sleep Foundation Model via Hierarchical Contrastive Learning

## Overview

Omni-Sleep is a sleep foundation model that uses the CNS/ANS (Central/Autonomic Nervous System) partition as a physiological prior for topology-constrained representation learning. Pre-trained on 100,000+ hours of multi-center multimodal PSG data, it addresses the gap where existing sleep models fuse heterogeneous biosignals in a topology-agnostic manner.

## Core Architecture

### Three Learning Objectives

1. **Intra-System Consistency**: Captures shared subsystem-level factors within neural (EEG, EOG, EMG) and cardio-respiratory (ECG, respiration) signals separately
2. **Inter-System Synchronization**: Aligns CNS and ANS subsystem trajectories to model brain-body dynamics cross-correlations
3. **Latent-Space Masked Temporal Modeling**: Captures long-horizon sleep dynamics through masked token prediction in the latent space

### Physiological Prior Structure

```
CNS Branch: EEG + EOG + EMG → Neural subsystem encoder
ANS Branch: ECG + Respiration → Cardio-respiratory encoder
                ↓
    Cross-system synchronization module
                ↓
    Unified sleep representation → Sleep staging / Disease classification
```

## Key Innovations

- **Topology-constrained fusion**: Uses known physiological organization (CNS vs ANS) rather than treating all modalities equally
- **100K+ hours pre-training**: Multi-center multimodal PSG dataset, significantly larger than prior work
- **Modality robustness**: Graceful degradation when modalities are missing during inference
- **Cross-dataset generalization**: Strong transfer across different sleep labs and recording protocols

## Application Domains

- Sleep stage classification (AASM standard)
- Multi-disease sleep disorder classification (apnea, insomnia, narcolepsy, etc.)
- Brain-computer interface for sleep-state monitoring
- Multimodal biosignal representation learning
- Physiological hierarchy in AI models

## Activation Keywords

`omni-sleep`, `sleep foundation model`, `CNS-ANS dynamics`, `polysomnography`, `PSG`, `sleep staging`, `brain-body dynamics`, `physiological hierarchy`, `topology-constrained learning`, `multimodal biosignal`, `affective computing`, `sleep physiology`

## Pitfalls

- **Modality availability**: Requires at least one CNS and one ANS modality for full inter-system synchronization objective
- **Data requirements**: 100K+ hours pre-training is a significant compute investment; fine-tuning on smaller datasets is more practical
- **Code availability**: Repository at https://github.com/AutoBrain-sleep/OmniSleep — check for latest release before implementation
- **Generalization limits**: While showing cross-dataset generalization, the model may still require domain adaptation for very different recording setups
- **Not a replacement for clinical judgment**: Foundation model outputs should be validated against clinical ground truth
