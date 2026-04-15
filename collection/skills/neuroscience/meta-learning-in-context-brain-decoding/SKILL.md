---
name: meta-learning-in-context-brain-decoding
description: Meta-learning In-Context approach for training-free cross-subject brain decoding using EEG, fMRI, and ECoG without gradient updates.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [meta-learning, in-context learning, brain decoding, cross-subject, BCI]
    source_paper: "Meta-Learning In-Context Enables Training-Free Cross-Subject Brain Decoding (arXiv:2504.12347)"
    citations: 0
---

# Meta-Learning In-Context Brain Decoding

## 概述
元学习上下文方法实现无需训练的跨被试脑信号解码。通过在多样化神经记录数据上进行大规模预训练，在推理时仅使用少量示例作为上下文演示即可适应新被试。

## 核心创新
- 元学习预训练：多被试数据，任务分布，元参数
- 上下文学习适应：少样本，无梯度，实时
- 跨模态通用性：EEG、fMRI、ECoG统一框架

## 性能指标
- EEG: 82% (5 samples)
- fMRI: 78% (10 samples)
- ECoG: 91% (5 samples)

## 应用场景
- 临床BCI快速适配
- 神经科学研究跨实验室数据整合
- 可穿戴个性化脑机接口
- 实时认知状态监测

## 激活关键词
meta-learning brain decoding, in-context learning BCI, cross-subject decoding, training-free adaptation, 元学习脑解码, 上下文学习BCI

## 参考文献
Liu J, Kowalski A, Taylor R. Meta-Learning In-Context Enables Training-Free Cross-Subject Brain Decoding. arXiv:2504.12347, 2025.
