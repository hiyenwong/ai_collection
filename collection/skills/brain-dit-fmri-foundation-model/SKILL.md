---
name: brain-dit-fmri-foundation-model
description: Brain-DiT is a universal multi-state fMRI foundation model using metadata-conditioned diffusion pretraining with a Diffusion Transformer (DiT). Pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Diffusion-based generative pretraining outperforms masked reconstruction or alignment as a proxy task. Metadata conditioning disentangles intrinsic neural dynamics from population-level variability.
version: 0.1.0
arxiv: 2604.12683v1
title: "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining"
tags:
  - fmri
  - foundation-model
  - diffusion-transformer
  - metadata-conditioning
  - pretraining
  - brain-states
  - multi-scale-representations
---

# Brain-DiT: Multi-State fMRI Foundation Model

## Overview

Brain-DiT is a universal fMRI foundation model that uses **metadata-conditioned diffusion pretraining** with a Diffusion Transformer (DiT). Unlike prior models that rely on masked reconstruction in raw-signal or latent space, Brain-DiT learns multi-scale representations through a diffusion-based generative objective conditioned on metadata (brain state, subject info, task labels).

## Key Findings

- **Scale**: 349,898 fMRI sessions from 24 datasets
- **Brain states**: resting, task-evoked, naturalistic stimulation, disease, sleep
- **Pretraining superiority**: Diffusion-based generative pretraining consistently outperforms masked reconstruction and alignment objectives
- **Metadata conditioning**: Disentangles intrinsic neural dynamics from population-level variability, improving downstream performance
- **Scale-dependent representations**: Downstream tasks prefer different representational scales:
  - ADNI classification → benefits from global semantic representations
  - Age/sex prediction → relies more on fine-grained local structure

## Architecture

- **Backbone**: Diffusion Transformer (DiT) — applies diffusion process in a learned latent space
- **Conditioning**: Metadata embeddings (categorical brain state, continuous subject variables, task descriptors) injected via cross-attention or adaptive layer norm
- **Multi-scale**: Captures both fine-grained functional connectivity and global brain semantics
- **Pretraining objective**: Denoising diffusion — predict noise added at timestep t to corrupted latent fMRI representation

## When to Use

- fMRI representation learning across diverse brain states
- Transfer learning for neurological classification tasks (ADNI, disease detection)
- Demographic prediction from brain imaging (age, sex)
- Multi-dataset fMRI harmonization
- Studying brain state transitions and neural dynamics
