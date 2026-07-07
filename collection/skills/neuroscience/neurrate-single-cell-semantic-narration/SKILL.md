---
name: neurrate-single-cell-semantic-narration
description: NEURRATOR methodology for generating natural language descriptions of visual scenes from single-neuron spike trains. Uses CLIP embeddings and multimodal LLM for zero-shot decoding without language-side training.
---

# NEURRATOR: Semantic Narration at Single-Cell Resolution

NEURRATOR framework - 从单个神经元的脉冲活动生成自然语言场景描述。将神经元编码问题转化为语言生成问题，实现单细胞分辨率的视觉场景语义叙述。

## 核心创新

1. **Single-cell semantic narration**: 从单个神经元生成自由形式的场景描述
2. **CLIP embedding mapping**: 学习 spike trains → CLIP patch embeddings
3. **Zero-shot decoding**: 无语言侧训练，利用预训练模型

## 技术架构

### 编码流程
```
Spike trains (任意神经元子集) → Learned encoder → CLIP embeddings → Multimodal LLM → Natural language description
```

### 关键组件
- **Learned encoder**: 映射脉冲序列到 CLIP patch embedding space
- **Frozen CLIP**: 预训练 CLIP 作为视觉语义锚点
- **Sparse autoencoder**: 验证和精炼生成描述

## 实验数据

- **物种**: Mouse (小鼠)
- **脑区**: Visual cortex (视觉皮层)
- **记录**: Neuropixel recordings, natural movie viewing
- **规模**: Thousands of neurons

## 解码层级

| 层级 | 描述 |
|------|------|
| 单神经元 | Single neuron → Scene description |
| 皮层区域 | Singular cortical regions |
| 局部群体 | Local populations |
| 细胞类型 | Molecularly-defined cell-types |

## "Neurrate" 概念

**定义**: 用自然语言叙述单个神经元/细胞类型对视觉表征的贡献

**应用价值**:
- 将细胞身份从分类目标 → 功能探针
- 提供新的生物学洞察单位
- Quantify population size vs. decoding fidelity

## 实现要点

### CLIP 空间锚定
- Pre-trained frozen CLIP
- Patch-level embeddings
- Multimodal grounding

### 稀疏自编码器验证
- Validate descriptions
- Filter hallucinations
- Ensure semantic coherence

### 跨子集泛化
- Arbitrary neuron subsets
- No neuron-specific training
- Plug-and-play decoding

## 应用场景

### 神经编码研究
- Single-neuron functional characterization
- Cell-type contribution mapping
- Population representation analysis

### 跨物种迁移
- Framework applicable to other species
- Human neuroscience potential
- Other sensory modalities

## 技术指标

- **解码分辨率**: Single-cell level
- **输入规模**: Thousands of neurons
- **语言生成**: Free-form natural language
- **训练需求**: No language-side training

## 论文信息

**标题**: Can neurons speak? Semantic narration of vision at single-cell resolution

**作者**: Arnau Marin-Llobet, Richard Hakim, Sara Matias, Venkatesh N. Murthy, Na Li, Demba Ba

**arXiv**: 2606.18667 (Submitted 2026-06-17)

**领域**: q-bio.NC (Neurons and Cognition), q-bio.QM (Quantitative Methods)

## 引用

```bibtex
@article{marin2026neurrate,
  title={Can neurons speak? Semantic narration of vision at single-cell resolution},
  author={Marin-Llobet, Arnau and Hakim, Richard and Matias, Sara and Murthy, Venkatesh N. and Li, Na and Ba, Demba},
  journal={arXiv preprint arXiv:2606.18667},
  year={2026}
}
```