---
name: brain-dit-fmri-foundation-model-v6
category: ai_collection
description: "Brain-DiT v6: Universal multi-state fMRI foundation model with metadata-conditioned pretraining (2026-04-14). Extends v5 with 34 datasets, metadata-conditioned pretraining, unified multi-state representation."
tags: ["fmri", "foundation model", "brain-dit", "multi-state", "diffusion transformer", "neuroimaging"]
source: "arXiv:2604.12683 (2026-04-14)"
authors: "Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu"
version: "v6"
---

# Brain-DiT v6: Universal Multi-state fMRI Foundation Model

## Overview
Brain-DiT is a universal multi-state fMRI foundation model pretrained on 34 diverse datasets with metadata-conditioned pretraining. It addresses limitations of previous fMRI models that rely on limited brain states and mismatched pretraining tasks.

## Key Innovations

### 1. Multi-state Pretraining
- **34 datasets** covering diverse brain states (resting, task, clinical populations)
- **Metadata-conditioned** pretraining to handle heterogeneous data sources
- Unified representation learning across brain states

### 2. Diffusion Transformer Architecture
- **DiT (Diffusion Transformer)** backbone for fMRI data modeling
- Handles spatiotemporal patterns in brain activity
- Generates realistic fMRI data through diffusion process

### 3. Generalized Representations
- Learns **generalized representations** across diverse brain states
- Overcomes limitations of state-specific models
- Enables transfer learning across different neuroimaging paradigms

## Technical Details

### Architecture
- **Backbone**: Diffusion Transformer (DiT)
- **Input**: fMRI volumes (4D spatiotemporal data)
- **Conditioning**: Metadata (scan parameters, task type, population)
- **Training**: Masked diffusion pretraining

### Pretraining Strategy
- **Multi-dataset** aggregation (34 datasets)
- **Metadata-conditioned** learning to handle heterogeneity
- **Unified** representation space for all brain states

## Applications

### Primary Uses
1. **fMRI data generation** - realistic synthetic brain activity
2. **Cross-state transfer** - apply knowledge across different brain states
3. **Brain decoding** - decode cognitive states from fMRI patterns
4. **Clinical analysis** - identify disease-specific patterns
5. **Data augmentation** - generate training data for downstream tasks

### Downstream Tasks
- Brain state classification
- Disease biomarker discovery
- Cognitive task decoding
- Functional connectivity analysis
- Individual fingerprinting

## Comparison with Previous Versions

| Feature | v1-v4 | v5 | v6 |
|---------|-------|----|----|
| Datasets | Limited | Expanded | 34 datasets |
| Conditioning | None | Basic | Full metadata |
| Brain States | Single | Multiple | Universal |
| Pretraining | Task-specific | Multi-task | Unified |

## Implementation Considerations

### Data Requirements
- Access to multiple fMRI datasets (34+ recommended)
- Metadata standardization (BIDS format preferred)
- Quality control across heterogeneous sources

### Computational Requirements
- GPU cluster for pretraining (DiT is compute-intensive)
- Large storage for multi-dataset aggregation
- Efficient data loading for 4D fMRI volumes

### Key Challenges
- **Heterogeneity**: Different scanners, protocols, populations
- **Metadata quality**: Incomplete or inconsistent metadata
- **Domain shift**: Cross-site variability
- **Scale**: 34 datasets require significant compute

## Related Skills
- `brain-dit-fmri-foundation-model-v5`
- `brain-dit-universal-multi-state`
- `brain-foundation-model-batch-effects`
- `multimodal-brain-connectivity-gnn`
- `bleg-llm-brain-graph-enhancer`

## Trigger Words
brain-dit, fmri foundation model, multi-state pretraining, diffusion transformer, metadata-conditioned, neuroimaging foundation model, brain decoding, 34 datasets, universal fMRI

## References
- arXiv:2604.12683 (2026-04-14)
- Authors: Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu
