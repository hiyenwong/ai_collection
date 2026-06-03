---
name: brain-dit-universal-multi-state-fmri-foundation-model
description: Brain-DiT universal multi-state fMRI foundation model with metadata-conditioned diffusion pretraining (DiT), pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Diffusion-based generative pretraining outperforms masked reconstruction or alignment. Extends brain-dit-fmri-foundation-model with universal multi-state support.
version: 0.1.0
arxiv: 2604.12683v1
title: "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining"
tags:
  - fmri
  - foundation-model
  - diffusion-transformer
  - metadata-conditioning
  - multi-state
  - neuroscience
  - brain-states
---

# Brain-DiT: Universal Multi-State fMRI Foundation Model

**arXiv ID:** 2604.12683v1

## Overview

Brain-DiT is a universal fMRI foundation model pretrained on 349,898 sessions from 24 datasets. It uses **metadata-conditioned diffusion pretraining** with a Diffusion Transformer (DiT) to learn multi-scale representations covering resting, task, naturalistic, disease, and sleep brain states.

## Key Contributions

- Universal pretraining across 5 brain state categories (resting, task, naturalistic, disease, sleep)
- Diffusion-based generative pretraining outperforms masked reconstruction and alignment objectives
- Metadata conditioning disentangles intrinsic neural dynamics from population-level variability
- Downstream tasks prefer different representational scales: ADNI → global semantics; age/sex → fine-grained local structure

## Architecture

- **Backbone**: Diffusion Transformer (DiT) operating in a learned latent space
- **Conditioning**: Metadata embeddings (brain state, subject variables, task descriptors) via cross-attention or adaptive layer norm
- **Pretraining objective**: Denoising diffusion — predict noise added at timestep t to corrupted latent fMRI representation

## When to Use

- fMRI representation learning across diverse brain states
- Transfer learning for neurological classification (ADNI, disease detection)
- Demographic prediction from brain imaging (age, sex)
- Multi-dataset fMRI harmonization

## Activation Keywords

- "brain-dit-universal-multi-state-fmri-foundation-model"
- "brain dit universal multi state fmri"
- "universal fmri foundation model brain dit"
- "brain dit multi state fmri pretraining"
- "metadata conditioned fmri foundation model"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify the user's fMRI modeling task and target brain states
2. Gather context about datasets and downstream tasks
3. Guide usage of Brain-DiT pretrained representations for the specific use case
4. Provide code examples or configuration for fine-tuning

## Examples

### Basic usage
```
User: "How do I use Brain-DiT for ADNI classification?"
→ Explain multi-state pretraining → Show fine-tuning approach → Recommend global representation scale
```

### Advanced usage
```
User: "I need to harmonize fMRI data across multiple datasets"
→ Explain metadata conditioning → Guide dataset preparation → Provide transfer learning steps
```
