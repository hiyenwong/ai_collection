---
name: eeg-foundation-model-adapters
description: "EEG foundation models with domain adaptation using lightweight adapters. Covers pre-trained EEG encoders, task-specific fine-tuning with adapters, cross-dataset generalization, and efficient deployment. Use when working with EEG foundation models, neural signal pre-training, adapter-based fine-tuning, or cross-dataset EEG classification."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [eeg, foundation-model, adapters, neural-signals, transfer-learning]
    source_paper: "EEG Foundation Models with Domain Adaptation (arXiv:2604.xxxxx)"
    citations: 0
---

# EEG Foundation Models with Adapters

## Overview

Leveraging pre-trained EEG foundation models with lightweight adapter modules for efficient domain adaptation across different EEG tasks, datasets, and recording conditions.

## Core Concepts

### Foundation Model Architecture
- Self-supervised pre-training on large EEG corpora
- Multi-channel temporal encoding
- Cross-subject representation learning
- Contrastive learning for neural patterns

### Adapter-Based Fine-Tuning
- Lightweight adapter modules (1-5% of parameters)
- Task-specific adaptation without full model retraining
- Domain shift mitigation across datasets
- Efficient deployment with frozen backbone

## Implementation Patterns

```python
# Adapter-based EEG classification
class EEGAdapterModel:
    def __init__(self, foundation_model, num_tasks):
        self.backbone = foundation_model  # Frozen pre-trained EEG encoder
        self.adapters = nn.ModuleList([
            AdapterLayer(dim=768) for _ in range(num_tasks)
        ])
        self.classifiers = nn.ModuleList([
            nn.Linear(768, num_classes) for _ in range(num_tasks)
        ])
    
    def forward(self, eeg_signal, task_id):
        features = self.backbone(eeg_signal)  # Frozen encoder
        adapted = self.adapters[task_id](features)
        return self.classifiers[task_id](adapted)
```

## Key Benefits

1. **Data Efficiency**: 10-100x less task-specific data needed
2. **Cross-Dataset Generalization**: Adapt to new EEG systems
3. **Computational Efficiency**: Train only 1-5% of parameters
4. **Multi-Task Learning**: Single backbone, multiple adapters

## Use Cases

- Motor imagery classification across subjects
- Sleep stage scoring across labs
- Epileptic seizure detection across hospitals
- Cognitive load estimation across tasks

## Activation Keywords
- EEG foundation model
- neural signal pre-training
- adapter fine-tuning EEG
- cross-dataset EEG classification
- self-supervised EEG learning
- efficient EEG model deployment

## References
- Related: eeg2vision-multimodal-reconstruction, meta-learning-in-context-brain-decoding
