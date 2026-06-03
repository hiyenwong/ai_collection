---
name: dina-v1-population-activity-interpretation
description: "Dual-Tower Image-Neural Alignment (DINA) framework for interpreting V1 population activity. Contrastive learning aligning visual stimuli and V1 responses in shared latent space at intermediate feature map level. Use when: analyzing V1 population activity, visual decoding from neural data, calcium imaging analysis, interpretable neural alignment."
---

# DINA: V1 Population Activity Interpretation

Interpretable contrastive framework for analyzing population-level visual computations in primary visual cortex.

## arXiv Reference
- **Paper**: "Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment"
- **arXiv ID**: 2605.04309
- **Date**: May 5, 2026
- **Authors**: Xin Wang, Zhuangzhi Gao, Hongyi Qin, Zhongli Wu, Feixiang Zhou, He Zhao

## Core Innovation
**Dual-Tower Image-Neural Alignment (DINA)**: A contrastive framework that aligns visual stimuli and V1 population responses in a shared latent space at the level of intermediate feature maps, enabling both accurate decoding and direct access to interpretable features.

## Architecture
- **Biologically Motivated Dual-Tower**: Joint training of image and neural encoders
- **Intermediate Feature Alignment**: Alignment occurs at feature map level, not just final embeddings
- **Shared Latent Space**: Visual stimuli and neural responses mapped to common space
- **Contrastive Learning**: Drives alignment through positive/negative sample pairs

## Key Findings
1. **Coarse Structure Dominance**: Decoding performance primarily supported by coarse, low-level visual structure, not semantic category information
2. **Spatial Distribution**: Alignable feature maps emerge from multiple spatially distributed image regions
3. **Sparse Neuron Contributions**: Reconstruction predominantly by sparse subsets of strongly responsive neurons
4. **Functional Interactions**: Strongly responsive neurons and their interactions drive alignment

## Validation
- Evaluated on large-scale two-photon calcium imaging data from mouse V1
- Achieves accurate neural-based decoding
- Provides principled framework for probing computational mechanisms

## Application Triggers
- Analyzing V1 population activity from calcium imaging
- Visual stimulus decoding from neural recordings
- Studying neural computation in early visual cortex
- Interpretable neural alignment research
- Investigating sparse coding in sensory cortices

## Technical Details
- **Data Type**: Two-photon calcium imaging
- **Species**: Mouse V1
- **Analysis Level**: Population-level, intermediate feature maps
- **Method**: Contrastive learning, dual-tower architecture

## Related Skills
- `eeg-visual-attention-decoding`
- `neural-encoding-evaluation-ground-truth`
- `untrained-cnns-match-backpropagation-at-v1`
