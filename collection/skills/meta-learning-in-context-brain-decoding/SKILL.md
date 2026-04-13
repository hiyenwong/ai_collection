---
name: meta-learning-in-context-brain-decoding-v3
description: "Meta-learning in-context approach for training-free cross-subject brain decoding from fMRI signals. Enables generalizable visual decoding without per-subject training. Activation: cross-subject brain decoding, meta-learning fMRI, training-free neural decoding, 跨个体脑解码, 元学习脑信号解码."
arxiv_id: 2604.08537
---

# Meta-learning In-Context Brain Decoding

## Description

视觉解码是计算机视觉与神经科学交叉的关键挑战，需要弥合神经表征与视觉计算模型之间的鸿沟。跨个体泛化是该领域的核心目标，但神经表征在个体间的显著变异一直是一大障碍——此前需要为每个受试者单独训练或微调模型。

本文提出一种元优化方法，实现从 fMRI 进行语义视觉解码并泛化到新个体，无需针对新受试者的训练。通过元学习优化模型以利用上下文样本，在测试时使用少量示例提示即可解码新个体的神经活动。

## Core Methodology

### 1. In-Context Learning Framework
- 利用上下文样本进行脑信号解码
- 无需针对新受试者重新训练
- 元优化学习如何有效使用上下文示例

### 2. Cross-Subject Generalization
- 处理个体间神经表征的显著变异
- 通过学习可迁移的解码策略
- 支持零样本或少样本跨个体解码

### 3. Meta-Optimization Strategy
- 训练阶段：学习如何从上下文样本快速适应
- 测试阶段：使用少量示例提示解码新个体
- 端到端优化解码性能

## Activation Keywords
- cross-subject brain decoding
- meta-learning fMRI
- training-free neural decoding
- 跨个体脑解码
- 元学习脑信号解码
- in-context brain decoding
- zero-shot brain decoding

## Applications

1. **Brain-Computer Interfaces**
   - 跨用户 BCI 系统
   - 无需个性化校准
   - 快速部署神经接口

2. **Neuroscience Research**
   - 群体水平的视觉表征研究
   - 个体差异分析
   - 神经编码比较

3. **Clinical Applications**
   - 神经疾病诊断
   - 康复评估
   - 认知功能监测

## Technical Specifications

- **Input**: fMRI 时间序列数据
- **Output**: 视觉刺激语义解码
- **Training**: 元学习（MAML-style）
- **Inference**: In-context few-shot learning
- **Generalization**: Cross-subject without fine-tuning

## Related Skills
- in-context-brain-decoding
- brain-meta-learning-in-context-decoding
- meta-learning-brain-decoding
- meta-learning-brain-decoding-v2

## References
- arXiv: 2604.08537
- Paper: Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding
- PDF: https://arxiv.org/pdf/2604.08537

_Last updated: 2026-04-13_
