---
name: brain-dit-universal-multi-state-fmri
description: "Brain-DiT: Universal multi-state fMRI foundation model with metadata-conditioned pretraining. Supports resting, task, naturalistic, disease, and sleep states. Activation: brain-dit, fMRI foundation model, multi-state brain, neuroimaging, brain foundation model, brain state decoding, 脑基础模型."
---

# Brain-DiT: A Universal Multi-state fMRI Foundation Model

## Overview
**arXiv ID:** 2604.12683v1  
**Published:** April 14, 2026  
**Categories:** cs.CV (Computer Vision and Pattern Recognition); q-bio.NC (Neurons and Cognition)  
**Authors:** Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu

## Paper Abstract
> Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. We present Brain-DiT, a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal space or a latent space, Brain-DiT adopts metadata-conditioned diffusion pretraining with a Diffusion Transformer (DiT), enabling the model to learn multi-scale representations that capture both fine-grained functional structure and global semantics. Across extensive evaluations and ablations on 7 downstream tasks, we find consistent evidence that diffusion-based generative pretraining is a stronger proxy than reconstruction or alignment, with metadata-conditioned pretraining further improving downstream performance by disentangling intrinsic neural dynamics from population-level variability.

## Key Contributions

1. **Universal Multi-State Coverage**: Pretrained on 349,898 sessions from 24 datasets
2. **Diverse Brain States**: Resting, task, naturalistic, disease, and sleep states
3. **Diffusion-Based Pretraining**: DiT architecture with diffusion modeling
4. **Metadata-Conditioned Training**: Disentangles intrinsic dynamics from population variability
5. **Multi-Scale Representations**: Captures fine-grained structure and global semantics
6. **Superior Downstream Performance**: Outperforms reconstruction/alignment approaches on 7 tasks

## Methodology

### Pretraining Data
- **349,898 sessions** from 24 diverse datasets
- **States covered**:
  - Resting state
  - Task-based (multiple cognitive tasks)
  - Naturalistic (movie watching, etc.)
  - Disease states
  - Sleep states

### Architecture: Diffusion Transformer (DiT)
- **Base architecture**: Diffusion Transformer
- **Training paradigm**: Metadata-conditioned diffusion pretraining
- **Novelty**: Unlike masked reconstruction, uses diffusion-based generative modeling

### Metadata Conditioning
- Conditions on dataset metadata (acquisition parameters, population info)
- Disentangles intrinsic neural dynamics from population-level variability
- Improves generalization across different acquisition conditions

### Multi-Scale Representation Learning
- Captures **fine-grained functional structure** (local connectivity)
- Captures **global semantics** (whole-brain patterns)
- Enables task-specific feature selection

## Performance Results

### Downstream Tasks (7 tasks)
| Task | Performance Improvement |
|------|------------------------|
| ADNI Classification | Benefits from global semantic representations |
| Age Prediction | Relies on fine-grained local structure |
| Sex Prediction | Uses fine-grained local structure |
| Other tasks | Task-dependent representation preference |

### Key Findings
- **Diffusion-based pretraining** > reconstruction/alignment
- **Metadata conditioning** improves downstream performance
- **Representation scale preference varies** by task:
  - ADNI: prefers global semantics
  - Age/Sex: prefers fine-grained structure

## Activation Keywords

- brain-dit, Brain-DiT
- fMRI foundation model
- multi-state brain model
- neuroimaging foundation model
- brain state decoding
- 脑基础模型
- diffusion transformer brain
- metadata-conditioned pretraining
- universal brain representation
- resting-task-disease-sleep states

## Tools Used

- `pytorch`: Model implementation
- `diffusers`: Diffusion model components
- `nilearn`: Neuroimaging data processing
- `huggingface`: Model sharing

## References

- **Paper**: "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining" (arXiv:2604.12683v1)
- **Code & Parameters**: https://github.com/REDMAO4869/Brain-DiT
- **arXiv**: https://arxiv.org/abs/2604.12683
- **Published**: April 14, 2026

## Related Work

- Prior fMRI foundation models: Limited state coverage
- Brain-DiT advances: Multi-state, diffusion-based, metadata-conditioned
- Applications: Clinical prediction, cognitive decoding, disease classification

## Use Cases

1. **Clinical Neuroscience**: Disease classification (ADNI)
2. **Cognitive Neuroscience**: Task decoding across cognitive domains
3. **Sleep Research**: Sleep state analysis
4. **Precision Medicine**: Individualized brain representations
5. **Cross-Dataset Generalization**: Robust to acquisition differences

## Code Availability

- **Repository**: https://github.com/REDMAO4869/Brain-DiT
- **Pretrained Models**: Available
- **License**: Check repository for details

_Last updated: 2026-04-17_
