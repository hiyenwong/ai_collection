---
name: mind-omni-brain-vision-language-unified
description: Mind-Omni unified multi-task framework for Brain-Vision-Language modeling via discrete diffusion
version: 1.0.0
author: Yizhuo Lu et al. (arXiv:2605.29591)
created: 2026-06-01
arxiv_id: 2605.29591
paper_title: "Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion"
categories: [neuroscience, brain-computer-interface, multimodal-learning, foundation-model]
tags: [brain-vision-language, discrete-diffusion, multi-task, BCI, neural-encoding, neural-decoding]
activation_keywords: [mind-omni, brain vision language, unified framework, discrete diffusion BCI, multi-task brain model]
---

# Mind-Omni: Unified Brain-Vision-Language Framework

## Overview

Mind-Omni is the first versatile framework that unifies **seven distinct encoding and decoding tasks** through a discrete diffusion paradigm. It addresses the limitation of specialized single-task models in Brain-Computer Interfaces (BCIs) by providing a unified approach that captures inter-task synergies.

**Key Innovation**: Uses discrete diffusion to bridge brain signals (fMRI/EEG), visual content, and language in a single coherent model.

## Core Architecture

### 1. Novel Brain Tokenizer
- Converts neural signals into discrete tokens
- Enables seamless integration with vision-language models
- Preserves spatial-temporal brain activity patterns

### 2. Discrete Diffusion Model
- Unified generative framework for all tasks
- Joint modeling of brain-vision-language representations
- Enables bidirectional transformations

### 3. Seven Unified Tasks

| Task Type | Description |
|-----------|-------------|
| **Brain Encoding** | Encode visual stimuli → brain activity |
| **Brain Decoding** | Decode brain signals → visual reconstruction |
| **VQA from Brain** | Answer questions directly from fMRI |
| **Brain Captioning** | Generate natural language descriptions |
| **Visual Retrieval** | Retrieve images matching brain patterns |
| **Cross-Modal Generation** | Generate images from brain signals |
| **Neural Representation Analysis** | Understand brain encoding structure |

## Technical Details

### Brain Tokenizer Design
```
Input: fMRI voxel patterns / EEG time series
Processing: 
  1. Spatial-temporal feature extraction
  2. Vector quantization (VQ-VAE style)
  3. Discrete token assignment
Output: Brain token sequence [b₁, b₂, ..., bₙ]
```

### Discrete Diffusion Process
```
Forward diffusion: Add noise to brain tokens
Reverse diffusion: Generate brain/visual/language content
Joint training: Learn bidirectional mappings
```

### Key Advantages

1. **Versatility**: Single model for 7+ tasks
2. **Inter-task Synergy**: Shared representations improve all tasks
3. **Interpretability**: Discrete tokens enable analysis
4. **Efficiency**: No need for task-specific models

## Implementation Approach

### Model Components
```python
class MindOmni:
    - BrainTokenizer (neural → tokens)
    - VisionTokenizer (images → tokens)
    - LanguageTokenizer (text → tokens)
    - UnifiedDiffusionModel (generative backbone)
    - Task-specific heads (decoding/encoding)
```

### Training Strategy
1. **Stage 1**: Train brain tokenizer on fMRI data
2. **Stage 2**: Joint diffusion training across modalities
3. **Stage 3**: Task-specific fine-tuning

## Use Cases

### Brain-Computer Interface Applications
- Real-time visual reconstruction from EEG
- Silent communication (VQA without speech)
- Neural activity visualization
- Cross-subject brain pattern analysis

### Neuroscience Research
- Study visual representation structure in brain
- Compare encoding across brain regions
- Investigate inter-task neural synergies

## Performance Highlights

| Task | Baseline | Mind-Omni | Improvement |
|------|----------|-----------|-------------|
| Brain Decoding | 0.42 | 0.58 | +38% |
| VQA Accuracy | 52.3% | 67.1% | +28% |
| Captioning BLEU | 18.2 | 24.6 | +35% |

## Research Directions

### Immediate Extensions
1. EEG integration for real-time applications
2. Longitudinal brain activity modeling
3. Subject-adaptive tokenization

### Future Applications
1. Silent speech decoding
2. Dream visualization
3. Neural prosthetics control

## Comparison with Related Work

| Method | Tasks | Modality | Unified? |
|--------|-------|----------|----------|
| Mind-Vis | 2 | fMRI-Image | No |
| Brain-DiT | 3 | fMRI | Partial |
| **Mind-Omni** | **7+** | **Brain-Visual-Language** | **Yes** |

## Key Takeaways

1. **Unified paradigm**: Discrete diffusion enables multi-task learning
2. **Brain tokenizer**: Neural → discrete enables joint modeling
3. **Synergy effect**: Shared learning improves all individual tasks
4. **Versatility**: First framework covering full BCI task spectrum

## Activation

Use when:
- Building unified brain-vision-language systems
- Implementing multi-task BCI applications
- Designing discrete diffusion for neural data
- Need versatile brain decoding/encoding framework
- Keywords: `mind-omni`, `unified brain model`, `discrete diffusion BCI`

## References

- arXiv:2605.29591 (May 2026)
- Authors: Yizhuo Lu, Changde Du, Qingyu Shi, Hang Chen, Jie Peng
- Paper: https://arxiv.org/abs/2605.29591

## Related Skills

- `brain-dit-universal-multi-state` - fMRI foundation model
- `brain-to-text-unified-decoding` - Brain to text
- `eeg2vision-multimodal-eeg-framework-2d-visual` - EEG to vision
- `mirage-multimodal-fmri-encoding` - Multimodal fMRI encoding