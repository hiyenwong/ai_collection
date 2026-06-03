---
name: quantum-feature-pyramid-gating
description: >
  Quantum Feature Pyramid Gating (QFPG) methodology for hybrid quantum-classical
  image segmentation using multi-scale quantum feature extraction with adaptive gating.
  Use when: designing hybrid quantum-classical image segmentation models,
  implementing quantum feature pyramids, or adding quantum-enhanced multi-scale features.
  Trigger words: quantum feature pyramid, QFPG, quantum segmentation,
  量子特征金字塔, hybrid quantum segmentation
---

# Quantum Feature Pyramid Gating

Hybrid quantum-classical image segmentation using multi-scale
quantum feature extraction with adaptive gating mechanisms.

## Core Methodology

### Architecture
1. **Multi-Scale Feature Pyramid**: Extract features at multiple resolutions
2. **Quantum Feature Encoding**: Map classical features to quantum states
3. **Quantum Circuit Processing**: Apply parameterized quantum circuits
4. **Adaptive Gating**: Combine quantum and classical features dynamically
5. **Segmentation Output**: Generate pixel-wise predictions

### Key Components

- Quantum data encoding via amplitude/angle encoding
- Parameterized quantum circuits (PQCs) for feature processing
- Gating mechanism to weigh quantum vs classical contributions
- Multi-scale pyramid for capturing different spatial frequencies

## Implementation Pattern

1. Build classical feature pyramid (e.g., FPN-style)
2. Encode features at each scale into quantum states
3. Apply trainable quantum circuits per scale
4. Measure quantum outputs as enhanced features
5. Use adaptive gates to fuse quantum+classical features
6. Feed fused features to segmentation decoder

## When to Use

- Image segmentation with limited training data
- Hybrid quantum-classical model design
- Multi-scale quantum feature enhancement
- Applications requiring both local and global context

## References

- arXiv: 2605.15370
