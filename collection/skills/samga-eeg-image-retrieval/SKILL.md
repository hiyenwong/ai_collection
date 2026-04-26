---
name: samga-eeg-image-retrieval
description: "Subject-Aware Multi-Granularity Alignment (SAMGA) framework for zero-shot EEG-to-image retrieval with cross-subject generalization. Activation: Visual decoding from EEG, Brain-computer interfaces."
---

# SAMGA: Subject-Aware Multi-Granularity Alignment for EEG-to-Image Retrieval

> Subject-Aware Multi-Granularity Alignment (SAMGA) framework for zero-shot EEG-to-image retrieval with cross-subject generalization.

## Metadata
- **Source**: arXiv:2604.17782v1
- **Authors**: Lin Jiang, Qingshan She, Jiale Xu et al.
- **Published**: 2026-04-20
- **Categories**: cs.CV

## Core Methodology

### Key Innovation
### Core Method
SAMGA addresses subject variability in EEG-to-image retrieval through:

1. **Multi-Granularity Alignment**: Aligns EEG and image features at multiple semantic levels
2. **Subject-Aware Module**: Learns subject-specific and subject-invariant representations
3. **Zero-Shot Capability**: Enables retrieval for unseen subjects without retraining
4. **Hierarchical Features**: Leverages hierarchical semantic information

### Technical Framework
- **EEG Encoder**: Temporal convolution + attention mechanism
- **Image Encoder**: Pre-trained Vision Transformer (ViT)
- **Alignment Loss**: Contrastive learning at multiple granularity levels
- **Subject Adapter**: Lightweight subject-specific adaptation module

## Implementation Guide

### Prerequisites
### Prerequisites
- PyTorch or TensorFlow
- Pre-trained ViT model (e.g., DINOv2, CLIP)
- EEG dataset with paired image stimuli
- GPU with 16GB+ VRAM

### Step-by-Step
1. **EEG Preprocessing**: Filter, epoch, baseline correction
2. **Feature Extraction**: Extract multi-scale EEG features
3. **Image Encoding**: Use pre-trained ViT for image embeddings
4. **Multi-Granularity Alignment**: Train alignment at object, scene, and fine-grained levels
5. **Subject Adaptation**: Fine-tune subject adapter for new subjects
6. **Zero-Shot Retrieval**: Retrieve images using EEG queries

### Applications
- Visual decoding from EEG
- Brain-computer interfaces
- Neuroimaging research
- Assistive technology

## Pitfalls
- Requires paired EEG-image training data
- Performance degrades with longer EEG-image time gaps
- Subject calibration still needed for optimal performance

## Related Skills
- neuroscience-research-method
- brain-connectivity-analysis
- eeg-decoding-brain-computer-interface

## References
- arXiv: https://arxiv.org/abs/2604.17782v1
