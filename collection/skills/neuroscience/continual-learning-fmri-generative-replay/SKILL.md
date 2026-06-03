---
name: continual-learning-fmri-generative-replay
description: "Continual learning framework for fMRI-based brain disorder diagnosis using functional connectivity matrices generative replay. Use when building clinical ML systems that need to learn from sequential multi-site fMRI data without catastrophic forgetting. Covers structure-aware VAE for FC matrix synthesis, multi-level knowledge distillation, and hierarchical contextual bandit replay sampling. Trigger keywords: continual learning fMRI, brain disorder diagnosis, functional connectivity, generative replay, catastrophic forgetting, multi-site fMRI, MDD, schizophrenia, autism."
---

# Continual Learning for fMRI-Based Brain Disorder Diagnosis

## Key Finding (arXiv 2604.14259v1, April 2026)

First continual learning framework specifically for fMRI-based brain disorder diagnosis across heterogeneous clinical sites. Uses structure-aware VAE to generate realistic FC matrices for replay, preventing catastrophic forgetting when training on sequential multi-site data.

## Problem

- Clinical fMRI data arrives sequentially from different institutions
- Standard models suffer catastrophic forgetting when trained on new sites
- Privacy regulations prevent full multi-site data pooling
- Existing methods: single-site training or full access (unrealistic)

## Framework: FORGE

### 1. Structure-Aware Variational Autoencoder
- Generates realistic FC matrices for patient and control groups
- Preserves brain network topology in synthetic samples
- Enables replay without storing original data (privacy-preserving)

### 2. Multi-Level Knowledge Distillation
- Aligns predictions between new-site model and replayed samples
- Aligns graph representations across sites
- Maintains knowledge from previous sites while learning new ones

### 3. Hierarchical Contextual Bandit
- Adaptive replay sampling strategy
- Selects most informative past samples for replay
- Balances memory efficiency with knowledge retention

## Datasets & Disorders

- **MDD** (Major Depressive Disorder)
- **SZ** (Schizophrenia)
- **ASD** (Autism Spectrum Disorder)
- Multi-site heterogeneous data

## Methodology Steps

1. **Train VAE** on current site's FC matrices
2. **Generate replay samples** for previous site groups
3. **Knowledge distillation** from old model to new model
4. **Adaptive sampling** via contextual bandit for efficient replay
5. **Joint training** on new data + replayed samples

## Key Advantages

- Privacy-preserving (no raw data storage)
- Handles heterogeneous site distributions
- Substantially outperforms baselines in forgetting mitigation
- Applicable to any FC-matrix-based disorder diagnosis

## Code

https://github.com/4me808/FORGE

## Activation Keywords

- continual learning fMRI
- brain disorder diagnosis
- functional connectivity
- generative replay
- catastrophic forgetting
- multi-site fMRI
- MDD diagnosis
- schizophrenia detection
- autism detection
- FC matrix synthesis
- FORGE framework


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Continual Learning Fmri Generative Replay

**Agent:** Continual Learning Fmri Generative Replay 是关于...
