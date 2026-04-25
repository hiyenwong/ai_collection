---
name: brain-dit-fmri-foundation-model-v4
category: ai_collection
description: "Brain-DiT: Universal multi-state fMRI foundation model with Diffusion Transformers. Handles 18 brain states across 7 datasets with state embeddings."
source: arXiv:2604.14759v1
paper_title: "Brain-DiT: Universal multi-state fMRI foundation model with Diffusion Transformers"
authors: "Zijin Lu et al."
date: 2026-04-15
keywords: ["fMRI", "diffusion transformer", "foundation model", "brain states", "multi-state", "UK Biobank", "ADNI", "brain decoding"]
trigger: ["brain dit", "fmri foundation model", "diffusion transformer fmri", "multi-state fmri", "brain state modeling", "universal fmri model"]
---

## Brain-DiT: Universal Multi-State fMRI Foundation Model

### Core Innovation
**Brain-DiT** is a universal multi-state fMRI foundation model using Diffusion Transformers (DiT). It handles **18 brain states** across **7 datasets**, using state embeddings to condition generation on specific functional contexts.

### Key Features
- **Multi-state support**: 18 distinct brain states (resting, task-specific, clinical)
- **7 datasets**: UK Biobank, ADNI, ABCD, HCP, and more
- **DiT backbone**: Diffusion Transformer architecture for fMRI time series generation
- **State embeddings**: Condition model on specific brain states
- **Pre-training**: Large-scale unsupervised pre-training on diverse fMRI data
- **Transfer learning**: Fine-tune on downstream tasks

### Architecture
```
Input: fMRI time series + State ID
  -> State Embedding Lookup
  -> Concatenate with fMRI features
  -> Diffusion Transformer (DiT)
  -> Reverse diffusion process
  -> Generate/Reconstruct fMRI time series
```

### Benchmarks
- **UK Biobank**: State-of-the-art on brain age prediction
- **ADNI**: Improved Alzheimer's classification accuracy
- **HCP**: Better functional connectivity prediction
- **ABCD**: Enhanced developmental trajectory modeling

### Applications
1. **Brain decoding**: Predict cognitive states from fMRI
2. **Clinical diagnosis**: Alzheimer's, ADHD, depression detection
3. **Data augmentation**: Generate synthetic fMRI for rare conditions
4. **Cross-study transfer**: Apply models trained on one dataset to another
5. **Brain state simulation**: Simulate fMRI under different conditions

### Advantages over Prior Work
| Feature | Brain-DiT | Prior Methods |
|---------|-----------|---------------|
| Brain states | 18 | 1-3 |
| Datasets | 7 | 1-2 |
| Generation quality | SOTA | Moderate |
| Transfer capability | Strong | Limited |
| State conditioning | Native | Not supported |

### Implementation Notes
- Uses PyTorch + HuggingFace Transformers
- Requires GPU for training (A100 recommended)
- Pre-trained weights available on HuggingFace Hub
- Fine-tuning script included for custom datasets

### Limitations
- Requires significant compute for training
- State definitions must be consistent across datasets
- Clinical validation still needed for diagnostic use