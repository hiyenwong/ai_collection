---
name: brain-dit-fmri-foundation-model-v5
description: >
  Brain-DiT v5 universal multi-state fMRI foundation model methodology. Metadata-conditioned diffusion pretraining
  with DiT on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states.
  Enables generalized fMRI representation learning across diverse brain states.
  Use when: fMRI foundation models, diffusion pretraining, multi-state brain modeling, metadata-conditioned learning, Brain-DiT, universal fMRI models, cross-state fMRI analysis.
---

# Brain-DiT v5: Universal Multi-state fMRI Foundation Model

## Core Idea

Brain-DiT is a universal multi-state fMRI foundation model that uses **metadata-conditioned diffusion pretraining** with a Diffusion Transformer (DiT) architecture. Unlike prior models relying on masked reconstruction, diffusion-based generative pretraining learns multi-scale representations capturing both fine-grained functional structure and global semantics.

## Key Findings

- **Pretrained on 349,898 sessions** from 24 datasets spanning resting, task, naturalistic, disease, and sleep states
- **Diffusion pretraining outperforms** reconstruction and alignment as a pretraining proxy
- **Metadata-conditioned pretraining** disentangles intrinsic neural dynamics from population-level variability
- **Downstream task preferences vary**: ADNI classification benefits from global semantic representations; age/sex prediction relies more on fine-grained local structure
- Evaluated across **7 downstream tasks** with consistent improvements

## Architecture

```
Metadata-conditioned Diffusion Transformer (DiT)
├── Multi-scale representation learning
├── Fine-grained functional structure
├── Global semantic representations
└── Disentangled population variability
```

## Methodology

1. **Metadata-conditioned diffusion**: Use session metadata (brain state, task type, disease status) as conditioning signal during diffusion pretraining
2. **Multi-scale learning**: Capture representations at both local (fine-grained) and global (semantic) scales
3. **Cross-state generalization**: Train on diverse brain states to learn transferable representations

## Applications

- fMRI-based brain disorder diagnosis
- Cross-state fMRI representation learning
- Age/sex prediction from brain scans
- Alzheimer's disease classification (ADNI)
- Brain state decoding across conditions

## Code

Available at: https://github.com/REDMAO4869/Brain-DiT

## Citation

Xia, J., Ye, W., Pan, X., Shen, X., & Wang, M. (2026). Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining. arXiv:2604.12683.
