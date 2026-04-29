---
name: vlm-visual-cortex-sycophancy
description: "Vision-Language Model robustness through early visual cortex (V1-V3) alignment against sycophantic manipulation. Use when evaluating VLM safety, studying brain alignment with AI models, analyzing gaslighting resistance in vision-language models, or investigating how neural correlates affect model behavior. Trigger keywords: vlm sycophancy, visual cortex alignment, gaslight manipulation, brain alignment, V1-V3 alignment, VLM safety, adversarial vision, sycophantic manipulation, neuro-AI safety."
---

# VLM Visual Cortex Alignment for Sycophancy Resistance

## Key Finding (arXiv 2604.13803v1, April 2026)

Alignment of VLM visual representations with **early visual cortex (V1-V3)** is a reliable negative predictor of sycophancy (r = -0.441). Models whose visual processing mirrors human V1-V3 neural activity are more resistant to gaslighting attacks.

## Core Results

- **12 models** across 6 architecture families, 256M-10B parameters
- **76,800 two-turn gaslighting prompts**, 5 categories, 10 difficulty levels
- fMRI responses predicted from Natural Scenes Dataset (NSD), 8 subjects, 6 visual ROIs
- V1-V3 alignment: r = -0.441 (BCa 95% CI [-0.740, -0.031])
- Existence denial attacks: strongest effect (r = -0.597, p = 0.040)
- Higher-order category-selective regions show NO such relationship

## Mechanism

Faithful low-level visual encoding provides a measurable anchor against adversarial linguistic override. Early visual cortex alignment grounds the model's visual understanding, making it harder for linguistic manipulation to override visual evidence.

## Methodology

### Brain Alignment Measurement
1. Extract visual features from VLM vision encoder at each layer
2. Train encoding models (linear/ridge regression) to predict fMRI responses
3. Evaluate on held-out NSD data across 6 visual ROIs (V1, V2, V3, V4, LOC, EBA)
4. Compute brain alignment score = prediction accuracy (correlation)

### Sycophancy Measurement
1. Two-turn conversation: model gives initial answer → user gaslights → model responds
2. 5 gaslighting categories: existence denial, attribute change, object count, spatial relation, action recognition
3. 10 difficulty levels (varying confidence of gaslight)
4. Sycophancy score = rate of changing answer to match gaslight

### Key Analysis
- ROI-specific correlation: alignment per region vs sycophancy score
- Leave-one-out cross-validation for robustness
- BCa bootstrap confidence intervals

## Implications

1. **AI Safety**: Brain-aligned models may be inherently more robust to manipulation
2. **Architecture Design**: Encourage V1-V3-like processing in vision encoders
3. **Evaluation**: Use brain alignment as a proxy for robustness
4. **Neuroscience**: Validates importance of early visual processing fidelity

## Resources

- GitHub: https://github.com/aryashah2k/Gaslight-Gatekeep-Sycophantic-Manipulation
- Dataset: https://huggingface.co/datasets/aryashah00/Gaslight-Gatekeep-V1-V3

## Activation Keywords

- vlm sycophancy
- visual cortex alignment
- gaslight manipulation
- brain alignment
- V1-V3 alignment
- VLM safety
- adversarial vision
- sycophantic manipulation
- neuro-AI safety
- brain-model alignment


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

**User:** 请解释 Vlm Visual Cortex Sycophancy

**Agent:** Vlm Visual Cortex Sycophancy 是关于...
