---
name: alzheimer-dit-fmri
description: "ADP-DiT: Text-Guided Diffusion Transformer for generating multi-modal fMRI data to track Alzheimer's disease progression. Use when generating synthetic fMRI for data augmentation in Alzheimer's research, building diffusion models for neuroimaging, or creating text-conditioned brain image generation pipelines. Trigger keywords: Alzheimer fMRI generation, diffusion transformer fMRI, ADP-DiT, text-guided brain generation, Alzheimer progression, synthetic fMRI, diffusion model neuroimaging, multi-modal fMRI synthesis."
---

# ADP-DiT: Alzheimer's fMRI Generation via Text-Guided Diffusion Transformer

## Key Finding (arXiv 2604.14837v1, April 2026)

Text-guided Diffusion Transformer (ADP-DiT) generates realistic multi-modal fMRI data conditioned on clinical descriptions, enabling data augmentation for Alzheimer's disease progression research where real data is scarce.

## Problem

- Alzheimer's fMRI data is limited and expensive to collect
- Disease progression studies need longitudinal data
- Data augmentation via synthetic generation can help
- Need to control generation by clinical attributes

## ADP-DiT Architecture

### 1. Diffusion Transformer (DiT) Backbone
- Transformer-based diffusion model for fMRI generation
- Captures complex spatial-temporal patterns in brain data
- Higher quality than traditional GAN-based approaches

### 2. Text-Guided Conditioning
- Clinical text descriptions (disease stage, symptoms) condition generation
- Enables targeted synthesis of specific disease profiles
- Supports data augmentation for underrepresented groups

### 3. Multi-Modal Generation
- Generates multiple fMRI modalities simultaneously
- Maintains cross-modal consistency
- Preserves disease-relevant patterns

## Applications

- Data augmentation for Alzheimer's classification
- Longitudinal disease progression modeling
- Synthetic data for privacy-preserving research
- Rare subtype generation

## Methodology

1. **Text encoding**: Clinical descriptions → embedding
2. **Conditional diffusion**: Text embedding guides fMRI generation
3. **Multi-modal consistency**: Ensure generated modalities align
4. **Evaluation**: Compare synthetic vs real fMRI quality

## Implications

1. **Data scarcity**: Alleviates limited fMRI datasets
2. **Privacy**: Synthetic data for sharing across institutions
3. **Research acceleration**: More data for model training
4. **Clinical insight**: Text-conditioned generation reveals disease patterns

## Activation Keywords

- Alzheimer fMRI generation
- ADP-DiT
- diffusion transformer fMRI
- text-guided brain generation
- Alzheimer progression
- synthetic fMRI
- diffusion model neuroimaging
- multi-modal fMRI synthesis
- fMRI data augmentation
- neuroimaging generation


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

**User:** 请解释 Alzheimer Dit Fmri

**Agent:** Alzheimer Dit Fmri 是关于...
