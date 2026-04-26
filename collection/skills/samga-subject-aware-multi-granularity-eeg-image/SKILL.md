---
name: samga-subject-aware-multi-granularity-eeg-image
description: "SAMGA (Subject-Aware Multi-Granularity Alignment) framework for zero-shot EEG-to-image retrieval. Adaptively aggregates multi-scale visual representations from pretrained vision encoders, with coarse-to-fine cross-modal alignment. Achieves 91.3% Top-1 intra-subject accuracy on THINGS-EEG. Activation: EEG-to-image, zero-shot retrieval, cross-modal alignment, visual decoding, brain-computer interface."
---

# SAMGA: Subject-Aware Multi-Granularity Alignment for Zero-Shot EEG-to-Image Retrieval

**arXiv:** [2604.17782](https://arxiv.org/abs/2604.17782)  
**Published:** 2026-04-20  
**Authors:** Lin Jiang, Qingshan She, Jiale Xu, Haiqi Xu, Duanpo Wu et al.  
**Categories:** cs.CV

## Problem

Zero-shot EEG-to-image retrieval aligns EEG neural responses with pretrained visual representations for scalable visual neural decoding. Prior methods use single fixed visual targets or subject-invariant construction, ignoring:
1. EEG preserves information across multiple representational scales
2. The optimal visual granularity varies across subjects

## Core Method: SAMGA Framework

### Component 1: Subject-Aware Visual Supervision Target
- Adaptively aggregates **multiple intermediate representations** from a pretrained vision encoder
- Learns subject-dependent aggregation weights during training
- Preserves **subject-agnostic inference** (no subject ID needed at test time)
- Allows the model to absorb subject-dependent granularity deviations

### Component 2: Coarse-to-Fine Cross-Modal Alignment
- **Shared encoder** architecture between EEG and visual modalities
- **Coarse stage:** Stabilizes shared semantic geometry, reduces subject-induced distribution shift
- **Fine stage:** Improves instance-level retrieval discrimination
- Both stages use contrastive learning objectives at different granularities

## Key Results

### THINGS-EEG Benchmark
| Setting | Top-1 Accuracy | Top-5 Accuracy |
|---------|---------------|----------------|
| Intra-subject | **91.3%** | **98.8%** |
| Inter-subject | **34.4%** | **64.8%** |

- Outperforms all recent state-of-the-art methods
- Significant improvement in inter-subject generalization

## Technical Details

### Architecture
- **EEG Encoder:** Processes raw EEG signals from visual perception tasks
- **Vision Encoder:** Pretrained model providing multi-layer features
- **Aggregation Module:** Learns subject-dependent weights for visual layer selection
- **Shared Projection:** Maps both modalities to common embedding space

### Training Strategy
- Multi-granularity contrastive loss
- Subject-aware target construction with adaptive weighting
- Coarse alignment pre-training followed by fine-grained refinement

## Reusable Methodology

### 1. Subject-Aware Multi-Granularity Targets
```
# Pseudocode for adaptive target construction
for each subject:
    layer_weights = learnable_parameters(n_layers)
    target = softmax(layer_weights) * stack(layer_features)
    # Subject-dependent aggregation, subject-agnostic at inference
```

### 2. Coarse-to-Fine Alignment Pipeline
1. Train coarse alignment with class-level contrastive loss
2. Freeze coarse encoder, train fine-grained instance-level head
3. Joint fine-tuning with weighted loss combination

### 3. Cross-Subject Generalization
- No subject-specific fine-tuning required at inference
- Adaptation happens through learned aggregation weights during training

## Applications

- **Zero-shot visual BCI:** Decode perceived images without retraining per image class
- **Cross-subject EEG decoding:** Generalize across individuals
- **Visual neural decoding:** Reconstruct visual experience from brain signals
- **Brain-computer interfaces:** Practical systems for visual content retrieval

## Datasets

- **THINGS-EEG:** Large-scale EEG dataset with visual perception tasks
  - Multiple subjects viewing natural images
  - 50ms-1000ms post-stimulus EEG epochs

## Key Innovations

1. **Multi-granularity visual targets** instead of single fixed representation
2. **Subject-aware aggregation** that adapts to individual neural patterns
3. **Coarse-to-fine alignment** for stable and discriminative embeddings
4. State-of-the-art results on established benchmark

## Limitations

- Requires multi-subject training data for subject-aware target learning
- Performance gap between intra-subject and inter-subject settings
- Dependent on quality of pretrained vision encoder

## Related Skills

- `eeg2vision-multimodal-eeg-framework-2d-visual`: EEG-to-image reconstruction
- `meta-learning-in-context-brain-decoding`: Cross-subject brain decoding
- `brain-inspired-capture-visual-decoding`: Visual decoding from brain signals
- `eccentricity-confound-eeg-visual-attention-decoding`: EEG visual attention
