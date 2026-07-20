---
name: fped-moe-brain-decoding
description: Functional-Network Prior-Guided Mixture-of-Experts (MoE) framework for interpretable brain decoding from fMRI. Uses brain network topology as expert priors with adaptive routing for visual semantic reconstruction.
category: ai_collection
keywords: fMRI decoding, Mixture-of-Experts, brain network, visual reconstruction, functional connectivity, interpretable AI, brain-computer interface
created: 2026-05-21
arxiv_id: "2605.19279"
arxiv_url: "https://arxiv.org/abs/2605.19279"
source: cron-neuroscience-research
---

# FPED: Functional-Network Prior-Guided Mixture-of-Experts for Interpretable Brain Decoding

## Paper
- **Title**: FPED: A Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding
- **Authors**: Yudan Ren, Pengcheng Shi, Zihan Ma, Xiaowei He, Xiao Li
- **arXiv**: 2605.19279 (2026-05-19)
- **URL**: https://arxiv.org/abs/2605.19279

## Problem
Visual image reconstruction from fMRI is a fundamental brain decoding task for understanding perception and developing BCIs. Current methods flatten fMRI signals from localized visual cortices into 1D vectors and map directly to latent spaces (e.g., CLIP). This paradigm:
1. Disrupts inherent brain network topology
2. Limits neuroscientific interpretability
3. Overlooks synergistic contributions of distributed functional networks in visual semantic processing

## Core Methodology: FPED Framework

### Architecture
- **Functional-Network Priors**: Explicitly model different functional brain networks as specialized experts
- **Mixture-of-Experts (MoE)**: Each expert corresponds to a distinct functional brain network (visual, default mode, attention, etc.)
- **Adaptive Routing**: Learn to route fMRI signals to experts based on semantic content, capturing complementary contributions
- **Parameter Efficiency**: Only 0.68B parameters yet achieves highly competitive semantic reconstruction

### Key Innovations
1. **Neurobiologically Grounded Expert Design**: Rather than homogeneous MLP layers, each expert maps to a known functional network
2. **Structured Representation Learning**: Network-level representation preserves brain topology instead of flattening
3. **Interpretable Routing Dynamics**: Learned routing weights reveal which functional networks contribute to which semantic dimensions
4. **Biological Correspondence**: Routing patterns show meaningful correspondence between functional networks and modality-specific semantic processing

### Technical Approach
```
fMRI Input → Network-wise Partitioning → Expert Modules (per network)
    ↓
Adaptive Router → Weighted Expert Outputs → CLIP Latent Space → Image Reconstruction
```

## Findings
- FPED achieves competitive semantic reconstruction with only 0.68B parameters
- Routing dynamics reveal biologically meaningful expert specialization:
  - Visual networks route to perceptual features
  - Higher-order networks route to abstract semantic features
  - Cross-network routing captures integrative processing
- Framework is transparent: routing weights provide direct neuroscientific interpretability

## Activation Triggers
- fMRI decoding, visual reconstruction from brain activity
- Mixture-of-Experts for neural data
- Interpretable brain-computer interfaces
- Functional network modeling
- Brain-to-image/text decoding
- Neurobiologically-grounded deep learning

## Pitfalls
- Requires accurate functional network parcellation as input priors
- Routing interpretability depends on quality of network assignment
- May need task-specific routing calibration for different paradigms
- CLIP latent space may not capture all neural representational dimensions

## Related Skills
- `eeg-structure-guided-diffusion`: EEG-to-image reconstruction
- `brain-graph-neural`: GNN methods for brain connectivity
- `multimodal-brain-connectivity-gnn`: Multimodal brain network analysis
- `meta-learning-in-context-brain-decoding`: Training-free cross-subject decoding
