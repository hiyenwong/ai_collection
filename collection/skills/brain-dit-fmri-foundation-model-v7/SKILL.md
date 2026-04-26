---
name: brain-dit-fmri-foundation-model-v7
description: "Brain-DiT: Universal multi-state fMRI foundation model with metadata-conditioned diffusion pretraining using Diffusion Transformer (DiT). Trained on 349,898 sessions from 24 datasets across diverse brain states. Activation: brain-dit, fmri foundation model, diffusion transformer, multi-state, metadata-conditioned, brain representation."
---

# Brain-DiT: Universal Multi-state fMRI Foundation Model v7

> Diffusion Transformer-based universal fMRI foundation model with metadata-conditioned pretraining, trained on 349,898 sessions spanning resting, task, naturalistic, disease, and sleep states.

## Metadata
- **Source**: arXiv:2604.12683v1
- **Authors**: Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, et al.
- **Published**: 2026-04-14
- **Code**: https://github.com/REDMAO4869/Brain-DiT

## Core Methodology

### Key Innovation
First fMRI foundation model using diffusion-based generative pretraining with metadata conditioning, enabling learning of multi-scale representations that capture both fine-grained functional structure and global semantics across diverse brain states.

### Limitations of Prior Work
- Limited range of brain states in training data
- Mismatched pretraining tasks (masked reconstruction in raw/latent space)
- Inability to generalize across diverse neural conditions

### Technical Framework

#### Model Architecture
- **Base**: Diffusion Transformer (DiT)
- **Pretraining Task**: Metadata-conditioned diffusion
- **Conditioning**: Population-level variability disentanglement
- **Representation**: Multi-scale (local structure + global semantics)

#### Training Data Scale
| Metric | Value |
|--------|-------|
| Total Sessions | 349,898 |
| Datasets | 24 |
| Brain States | Resting, Task, Naturalistic, Disease, Sleep |

#### Pretraining Advantages
1. **Diffusion vs. Reconstruction**: Stronger proxy for representation learning
2. **Metadata Conditioning**: Disentangles intrinsic dynamics from population variability
3. **Multi-scale**: Captures both local and global patterns

## Implementation Guide

### Model Usage
```python
# Brain-DiT Usage Pattern

# 1. Load pretrained model
model = BrainDiT.from_pretrained("brain-dit-v1")

# 2. Extract representations
representations = model.encode(fmri_data, metadata=session_info)

# 3. Downstream tasks
# - ADNI classification
# - Age/sex prediction
# - Brain state decoding
```

### Downstream Task Considerations
| Task | Preferred Representation |
|------|--------------------------|
| ADNI Classification | Global semantic representations |
| Age/Sex Prediction | Fine-grained local structure |

### Evaluation Results
- Consistent evidence that diffusion pretraining outperforms reconstruction/alignment
- Metadata conditioning improves downstream performance
- State-specific representational preferences observed

## Applications
- **Alzheimer's Disease Classification**: ADNI benchmark performance
- **Brain State Decoding**: Rest, task, naturalistic, sleep
- **Population Variability Modeling**: Demographic factor disentanglement
- **Clinical fMRI Analysis**: Generalized representations for diagnosis

## Pitfalls
- **Data Requirements**: Large-scale multi-site data needed for pretraining
- **Metadata Availability**: Requires rich session metadata
- **Computational Cost**: Diffusion training computationally intensive
- **Domain Gap**: Pretraining vs. target task distribution mismatch

## Advances Over Previous Brain-DiT Versions
- Expanded dataset coverage (24 datasets)
- Enhanced metadata conditioning
- Improved multi-state generalization
- Validated on 7 downstream tasks with extensive ablations

## Related Skills
- `brain-dit-fmri-foundation-model-v6`: Previous version
- `brain-dit-fmri-foundation-model-v5`: Earlier version
- `brain-dit-fmri-foundation-model-v4`: Base version
- `brain-dit-fmri-foundation-model`: Original version
- `brain-dit-universal-multi-state`: Alternative variant

## References
- Xia, J. et al. "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining." arXiv:2604.12683 (2026).
