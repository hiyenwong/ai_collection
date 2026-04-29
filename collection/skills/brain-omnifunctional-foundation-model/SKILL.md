---
title: Omnifunctional Foundation Model for Brain Signals (Brain-OF)
description: Universal multi-state foundation model processing fMRI, EEG, MEG, and ECoG in a single architecture with cross-modal representation learning and shared latent space for multi-modal brain decoding.
activation: brain foundation model, omnifunctional brain model, multi-modal neuroimaging, cross-modal brain decoding
categories: ["neuroscience", "foundation-model", "multimodal", "fMRI", "EEG", "MEG", "ECoG"]
trigger_keywords: ["Brain-OF", "omnifunctional foundation model", "multi-modal brain model", "cross-modal neuroimaging", "fMRI EEG MEG", "unified brain foundation", "brain signal foundation", "multi-state brain decoding", "shared latent brain", "cross-modal brain representation"]
related_skills: 
source_paper: Brain-OF: Omnifunctional Foundation Model for Brain Signals
source_url: https://arxiv.org/abs/2604.14940
created: 2026-04-19
version: 1.0
name: brain-omnifunctional-foundation-model
---


# Brain-OF: Omnifunctional Foundation Model for Brain Signals

## Overview

Brain-OF is a universal multi-state foundation model that processes multiple brain signal modalities (fMRI, EEG, MEG, ECoG) within a single architecture. It learns cross-modal representations in a shared latent space, enabling transfer learning between modalities and unified brain state decoding.

## When to Use

- Multi-modal brain disorder diagnosis (Alzheimer's, schizophrenia, epilepsy)
- Cross-modal brain state decoding and prediction
- Unified neuroimaging analysis pipelines
- Transfer learning from data-rich to data-poor modalities
- Large-scale brain atlas construction
- Multi-modal biomarker discovery

## Core Architecture

```
Input Modalities              Shared Backbone              Task Heads
┌─────────────┐              ┌─────────────┐              ┌─────────────┐
│   fMRI      │ ──┐          │             │    ┌────────→│ Classification│
│   (4D)      │   │          │             │    │         └─────────────┘
├─────────────┤   │ Adapter  │   Shared    │    │         ┌─────────────┐
│   EEG       │ ──┼─────────→│  Transformer│ ───┼────────→│  Regression  │
│   (2D+time) │   │ Layer    │   Backbone  │    │         └─────────────┘
├─────────────┤   │          │             │    │         ┌─────────────┐
│   MEG       │ ──┤          │             │    └────────→│  Decoding    │
│   (2D+time) │   │          │             │              └─────────────┘
├─────────────┤   │          │             │              ┌─────────────┐
│   ECoG      │ ──┘          │             │    ┌────────→│ Generation  │
│   (2D+time) │              └─────────────┘    │         └─────────────┘
└─────────────┘                                 │         ┌─────────────┐
                                                └────────→│  Retrieval   │
                                                          └─────────────┘
```

## Technical Components

### Modality-Specific Input Adapters

Each modality is converted to a unified token space:

**fMRI Adapter:**
- 4D volumes → spatial patches + temporal segments
- 3D CNN encoder → patch tokens
- Temporal positional encoding

**EEG/MEG Adapter:**
- Multi-channel time series → temporal windows
- 1D CNN or linear projection → token sequence
- Channel and temporal positional encoding

**ECoG Adapter:**
- Grid-based time series → spatial-temporal tokens
- Local connectivity-aware tokenization
- High-frequency band feature extraction

### Shared Transformer Backbone

- Multi-head self-attention for cross-modal interaction
- Layer normalization and residual connections
- Scalable depth (12-24 layers depending on model size)
- Cross-attention for modality-to-modality alignment

### Pre-training Objectives

1. **Masked Signal Modeling:**
   - Randomly mask portions of input signals
   - Predict masked regions from context
   - Applied independently per modality and jointly

2. **Contrastive Cross-Modal Learning:**
   - Pull representations of same subject's different modalities together
   - Push different subjects' representations apart
   - Temperature-scaled InfoNCE loss

3. **Multi-State Prediction:**
   - Predict cognitive states from brain signals
   - Multi-task learning across states
   - Shared representations benefit all tasks

### Fine-tuning Strategies

1. **Full Fine-tuning:**
   - Update all parameters for target task
   - Best when target dataset is large

2. **Adapter Fine-tuning:**
   - Freeze backbone, add task-specific adapters
   - Efficient for multiple downstream tasks
   - Prevents catastrophic forgetting

3. **Linear Probing:**
   - Freeze backbone, train linear classifier
   - Quick evaluation of representation quality
   - Minimal compute requirements

## Implementation Guidelines

### Data Preparation
```python
# Unified data format for all modalities
class BrainSample:
    def __init__(self, signal, modality, metadata):
        self.signal = signal  # Raw signal array
        self.modality = modality  # 'fmri', 'eeg', 'meg', 'ecog'
        self.metadata = metadata  # Subject info, task labels, etc.

# Preprocessing pipeline
def preprocess(sample):
    if sample.modality == 'fmri':
        return normalize_fMRI(sample.signal)
    elif sample.modality == 'eeg':
        return filter_and_rereference(sample.signal)
    # ... other modalities
```

### Training Pipeline
```python
# Pre-training loop
for batch in dataloader:
    # Forward through modality adapter
    tokens = adapter(batch.signal, batch.modality)

    # Forward through shared backbone
    representations = transformer(tokens)

    # Compute pre-training losses
    masked_loss = masked_modeling_loss(representations, batch.signal)
    contrastive_loss = cross_modal_contrastive(representations, batch.subject_id)

    # Combined loss
    total_loss = masked_loss + lambda_c * contrastive_loss
    total_loss.backward()
```

### Fine-tuning Example
```python
# Task-specific fine-tuning
class BrainTaskModel(nn.Module):
    def __init__(self, foundation_model, num_classes):
        super().__init__()
        self.backbone = foundation_model
        self.adapter = TaskAdapter()  # Lightweight adapter
        self.classifier = nn.Linear(hidden_dim, num_classes)

    def forward(self, signal, modality):
        # Freeze backbone, only train adapter
        with torch.no_grad():
            reps = self.backbone.encode(signal, modality)
        reps = self.adapter(reps)
        return self.classifier(reps)
```

## Applications

- **Multi-modal Diagnosis:** Combine fMRI + EEG for better Alzheimer's detection
- **Cross-modal Prediction:** Predict fMRI patterns from EEG (cost-effective screening)
- **Unified Brain Atlas:** Common representation space for all modalities
- **Transfer Learning:** Pre-train on large fMRI, fine-tune on small ECoG dataset
- **Biomarker Discovery:** Identify multi-modal biomarkers for disorders
- **Brain-Computer Interfaces:** Robust decoding using multi-modal signals

## Pitfalls

1. **Modality Imbalance:** fMRI datasets are much larger than ECoG. Use balanced sampling or modality-specific learning rates.
2. **Temporal Alignment:** Different modalities have different temporal resolutions. Use appropriate temporal windows.
3. **Spatial Alignment:** fMRI and EEG have different spatial characteristics. Use co-registration when possible.
4. **Batch Effects:** Multi-site data introduces batch effects. Apply harmonization (ComBat) before training.
5. **Computational Cost:** Training on all modalities simultaneously requires significant resources. Consider progressive training.
6. **Overfitting to Dominant Modality:** The model may favor the most common modality. Use modality-balanced loss weighting.

## Evaluation Metrics

- **Classification Accuracy:** For diagnostic tasks
- **Cross-modal Retrieval:** Recall@K for matching same subject across modalities
- **Representation Similarity:** CKA between modalities
- **Transfer Efficiency:** Performance gain from pre-training vs. training from scratch
- **Calibration:** Expected Calibration Error (ECE) for confidence estimation

## Future Directions

- Incorporate structural MRI (sMRI, DTI) as additional modalities
- Generative capabilities for missing modality imputation
- Continual learning for incremental modality addition
- Federated learning across institutions
- Clinical validation in multi-center trials


## Activation Keywords

- brain-omnifunctional-foundation-model
- brain omnifunctional foundation
- brain omnifunctional foundation model


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Brain Omnifunctional Foundation Model

**Agent:** Brain Omnifunctional Foundation Model 是关于...
