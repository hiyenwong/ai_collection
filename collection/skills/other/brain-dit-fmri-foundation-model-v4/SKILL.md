---
name: brain-dit-fmri-foundation-model-v4
description: Brain-DiT universal multi-state fMRI foundation model methodology. Metadata-conditioned diffusion pretraining with DiT on 349,898 sessions across 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Activation: brain-dit, fmri foundation model, diffusion transformer brain, metadata-conditioned pretraining, multi-state fmri, brain diffusion
---

# Brain-DiT: Universal Multi-state fMRI Foundation Model

Based on: *Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining* (Xia et al., 2026, arXiv:2604.12683)

## Core Contribution

Brain-DiT is a **universal multi-state fMRI foundation model** that adopts **metadata-conditioned diffusion pretraining** with a Diffusion Transformer (DiT), pretrained on **349,898 sessions from 24 datasets** spanning resting, task, naturalistic, disease, and sleep states.

## Key Findings

1. **Diffusion-based generative pretraining is stronger** than masked reconstruction or alignment for fMRI representation learning
2. **Metadata-conditioned pretraining** improves downstream performance by disentangling intrinsic neural dynamics from population-level variability
3. **Downstream tasks exhibit distinct preferences for representational scale**:
   - ADNI classification benefits more from global semantic representations
   - Age/sex prediction relies more on fine-grained local structure
4. Multi-scale representations capture both fine-grained functional structure and global semantics

## Architecture

```
fMRI Input → Metadata Conditioning → Diffusion Transformer (DiT) → Multi-scale Representations
                                                              ├── Fine-grained local structure
                                                              └── Global semantics
```

## Pretraining Strategy

| Aspect | Detail |
|--------|--------|
| Method | Metadata-conditioned diffusion pretraining |
| Data | 349,898 sessions from 24 datasets |
| Brain States | Resting, task, naturalistic, disease, sleep |
| Model | Diffusion Transformer (DiT) |

## Comparison with Prior Methods

| Method | Pretraining Objective | Limitation |
|--------|----------------------|------------|
| Prior fMRI FMs | Masked reconstruction (raw/latent) | Limited brain states, mismatched tasks |
| Brain-DiT | Metadata-conditioned diffusion | Multi-state, multi-scale, disentangled |

## Downstream Task Scale Preferences

| Task | Preferred Scale | Rationale |
|------|----------------|-----------|
| ADNI classification | Global semantic | Disease patterns are distributed |
| Age prediction | Fine-grained local | Regional developmental changes |
| Sex prediction | Fine-grained local | Structural dimorphism patterns |

## Implementation

- **Code**: https://github.com/REDMAO4869/Brain-DiT
- **PDF**: https://arxiv.org/pdf/2604.12683

## Pitfalls

1. **Scale mismatch**: Different downstream tasks need different representational scales — don't use a single-scale model
2. **Metadata quality**: Metadata-conditioned pretraining requires well-structured, consistent metadata
3. **Data heterogeneity**: 24 datasets with different acquisition protocols need careful harmonization

## Use Cases

1. fMRI foundation model pretraining with diffusion
2. Multi-state brain representation learning
3. Metadata-conditioned neural representation disentanglement
4. Cross-dataset fMRI analysis

## Related Skills

- `neural-dynamics-universal-translator`: Cross-model neural dynamics translation
- `brain-foundation-model-batch-effects`: Batch effects in brain FMs
- `brain-network-controllability`: Network control analysis
