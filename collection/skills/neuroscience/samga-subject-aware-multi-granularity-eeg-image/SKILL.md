---
name: samga-subject-aware-multi-granularity-eeg-image
description: "Subject-Aware Multi-Granularity Alignment (SAMGA) for zero-shot EEG-to-image retrieval. Enables cross-subject brain-computer interfaces with hierarchical neural representation alignment. Keywords: EEG, zero-shot retrieval, brain decoding, cross-subject, multi-granularity alignment."
---

# SAMGA: Subject-Aware Multi-Granularity Alignment for Zero-Shot EEG-to-Image Retrieval

> A hierarchical framework for zero-shot EEG-to-image retrieval that captures both subject-specific characteristics and shared neural representations through multi-granularity alignment.

## Metadata
- **Source**: arXiv:2604.17782
- **Authors**: Lin Jiang, Qingshan She, Jiale Xu, et al.
- **Published**: 2026-04-20
- **Category**: Computer Vision and Pattern Recognition (cs.CV), Neural and Evolutionary Computing (cs.NE)

## Core Methodology

### Problem Statement
Zero-shot EEG-to-image retrieval aims to decode perceived visual content from electroencephalography (EEG) by aligning neural responses with pretrained visual representations. Key challenges:
1. **Single fixed visual targets**: Previous methods rely on one-size-fits-all approaches
2. **Subject-invariant designs**: Overlook individual differences in neural encoding
3. **Cross-subject generalization**: Poor performance on unseen subjects

### Key Innovation: Multi-Granularity Alignment

SAMGA introduces a three-level hierarchical alignment framework:

1. **Fine-grained alignment**: Subject-specific neural patterns
2. **Coarse-grained alignment**: Shared semantic representations  
3. **Cross-granularity fusion**: Integration across levels

### Technical Framework

#### Architecture Components

```
Input: EEG signal (subject s, visual stimulus v)
├── Subject-Specific Encoder
│   └── Extracts individual neural response patterns
├── Multi-Granularity Representations
│   ├── Fine-grained: Patch-level visual features
│   ├── Mid-grained: Object-level semantic features
│   └── Coarse-grained: Scene-level conceptual features
├── Cross-Granularity Fusion Module
│   └── Attention-based aggregation across granularities
└── Output: Image embedding aligned with neural activity
```

#### Subject-Aware Target Construction
Instead of fixed visual targets, SAMGA generates **subject-conditioned visual representations**:
- Learns subject-specific neural encoding mappings
- Adapts visual target space per subject
- Maintains shared semantic backbone across subjects

#### Zero-Shot Transfer
- Training: Align EEG from seen subjects with visual embeddings
- Inference: Generalize to unseen subjects via subject-agnostic semantic alignment
- No calibration data required from new subjects

## Implementation Guide

### Prerequisites
- EEG data (64+ channels recommended)
- Pretrained CLIP or similar vision-language model
- PyTorch or TensorFlow

### Step-by-Step

1. **Data Preprocessing**
   ```python
   # Band-pass filter (e.g., 1-50 Hz)
   # Epoch extraction (-200ms to +1000ms from stimulus onset)
   # Baseline correction
   ```

2. **Subject-Specific Encoder**
   ```python
   class SubjectEncoder(nn.Module):
       def __init__(self, n_channels, n_subjects):
           self.eeg_encoder = EEGConvNet(n_channels)
           self.subject_embedding = nn.Embedding(n_subjects, 128)
       
       def forward(self, eeg, subject_id):
           features = self.eeg_encoder(eeg)
           subject_bias = self.subject_embedding(subject_id)
           return features + subject_bias  # Subject-conditioned encoding
   ```

3. **Multi-Granularity Alignment**
   ```python
   # Fine-grained: Patch-level CLIP features
   fine_features = clip.encode_patches(image)  # [N_patches, D]
   
   # Coarse-grained: Global CLIP features
   coarse_features = clip.encode_image(image)  # [D]
   
   # Hierarchical alignment loss
   loss_fine = contrastive_loss(eeg_features, fine_features)
   loss_coarse = contrastive_loss(eeg_features, coarse_features)
   loss = alpha * loss_fine + (1-alpha) * loss_coarse
   ```

4. **Cross-Granularity Fusion**
   ```python
   class CrossGranularityFusion(nn.Module):
       def __init__(self, dim):
           self.granularity_attention = MultiHeadAttention(dim)
       
       def forward(self, fine, coarse):
           # Cross-attention between granularities
           fused = self.granularity_attention(fine, coarse)
           return fused
   ```

### Training Configuration
- Batch size: 64-128
- Learning rate: 1e-4 with cosine decay
- Temperature for contrastive loss: 0.07
- Granularity weight α: 0.5 (tune per dataset)

## Applications

- **Visual BCI for accessibility**: Image selection via EEG
- **Marketing research**: Implicit preference detection
- **Clinical diagnostics**: Visual processing assessment
- **VR/AR control**: Gaze-free visual selection

## Pitfalls

1. **Subject variability**: Requires sufficient training subjects for robust zero-shot transfer
2. **Calibration trade-off**: Subject-aware targets need careful balance between personalization and generalization
3. **Granularity selection**: Not all granularities equally important for different visual categories
4. **Temporal dynamics**: EEG temporal windows need careful tuning

## Related Skills
- eeg-visual-attention-decoding
- meta-learning-in-context-brain-decoding
- contrastive-learning-neural-alignment
- zero-shot-brain-decoding

## Citation
```bibtex
@article{jiang2026samga,
  title={Subject-Aware Multi-Granularity Alignment for Zero-Shot EEG-to-Image Retrieval},
  author={Jiang, Lin and She, Qingshan and Xu, Jiale and others},
  journal={arXiv preprint arXiv:2604.17782},
  year={2026}
}
```
