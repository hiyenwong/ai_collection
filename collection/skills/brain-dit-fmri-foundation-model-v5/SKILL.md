---
name: brain-dit-fmri-foundation-model-v5
description: Brain-DiT v5 universal multi-state fMRI foundation model with pre-training and fine-tuning for zero-shot and few-shot brain decoding across multiple states. Supports cross-task, cross-subject, and cross-dataset fMRI analysis using diffusion transformer architecture. Use when: fMRI foundation models, brain decoding, diffusion transformers for neuroimaging, cross-subject fMRI analysis, zero-shot brain state prediction, multi-task fMRI modeling, neural state decoding, fMRI pre-training. Activation: Brain-DiT, fMRI foundation model, diffusion transformer brain, multi-state fMRI, brain decoding, cross-subject fMRI, fMRI pre-training, neural state prediction, zero-shot brain analysis.
version: 1.0.0
metadata:
  hermes:
    tags: [fMRI, foundation-model, diffusion-transformer, brain-decoding, multi-state, zero-shot, cross-subject, neuroimaging]
    source_paper: "Brain-DiT v5: Universal Multi-State fMRI Foundation Model (arXiv:2505.00936)"
    date: 2025-05-01
---

# Brain-DiT v5: Universal Multi-State fMRI Foundation Model

## Overview

Brain-DiT is a diffusion transformer-based foundation model for fMRI data that supports:
- Pre-training on large-scale fMRI datasets
- Zero-shot and few-shot fine-tuning for downstream tasks
- Cross-subject, cross-task, and cross-dataset generalization
- Multi-state brain activity modeling

**Source Paper**: Brain-DiT v5 (arXiv:2505.00936, 2025-05-01)

## Core Architecture

```
┌──────────────────────────────────────────────┐
│              Brain-DiT Architecture           │
├──────────────────────────────────────────────┤
│  fMRI Input → Patch Embedding                 │
│       ↓                                       │
│  DiT Blocks (diffusion transformer layers)    │
│       ↓                                       │
│  State Conditioning (task/stimulus labels)    │
│       ↓                                       │
│  Output: Brain state reconstruction/prediction │
└──────────────────────────────────────────────┘
```

## Key Innovations

1. **Universal Multi-State Modeling**: Single model handles multiple brain states/tasks
2. **Diffusion-Based Generation**: Uses diffusion process for robust fMRI prediction
3. **Cross-Subject Generalization**: Learns subject-invariant representations
4. **Foundation Model Pre-training**: Scales to large fMRI corpora

## Usage Pattern

```python
# Fine-tuning for new task
model = BrainDiT(pretrained="base")
model.fine_tune(
    dataset=new_fMRI_dataset,
    task="classification",  # or "reconstruction", "prediction"
    n_shots=5,  # few-shot learning
    epochs=50
)

# Zero-shot inference
predictions = model.predict(new_fMRI_data, task="unknown_task")
```

## Applications

- **Brain-computer interfaces**: Decode intent from fMRI signals
- **Clinical diagnosis**: Detect neurological disorders from brain activity patterns
- **Cognitive neuroscience**: Understand multi-task brain organization
- **Cross-study analysis**: Harmonize fMRI data across different studies

## Related Skills

- brain-dit-fmri-foundation-model — Brain-DiT overview
- brain-dit-universal-multi-state — Brain-DiT multi-state modeling
- meta-learning-in-context-brain-decoding — Cross-subject brain decoding
