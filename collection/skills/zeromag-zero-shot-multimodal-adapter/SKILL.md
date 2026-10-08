---
name: zeromag-zero-shot-multimodal-adapter
description: "EEG基础模型(EFM)扩展异构多模态（伴生生理信号）时用。ZeroMAG：冻结编码器+免目标标签免目标侧优化，从无标签记录生成adapter权重（配置不变adapter+模态-被试-任务条件+函数约束潜空间），零样本接近监督适配。Activation: EEG foundation model, multimodal adapter, zero-shot adaptation, hypernetwork, adapter generation, physiological signals, cross-dataset generalization, unlabeled target"
metadata:
  arxiv_id: "2610.03546"
  published: "2026-10-02"
  authors: "Yubo Wang, Jingying Ma, Xinliang Zhou et al. (11 authors)"
  source: "arXiv cs.LG"
  tags: [eeg-foundation-model, multimodal, adapter, zero-shot]
---

# ZeroMAG: 零样本多模态 Adapter 生成

## 核心问题

EEG foundation model (EFM) 预训练知识需要保留，同时要扩展到含伴生生理模态（EOG/EMG/呼吸等）的异构多模态记录——且目标数据无标签、不允许目标侧优化。

## ZeroMAG 方法

冻结 EEG 编码器与预测头，从无标签目标记录生成 adapter 权重：

1. **配置不变 adapter**：伴生模态围绕一个配置不变（configuration-invariant）的 adapter 组织，容忍异构模态组合
2. **条件构造**：从无标签记录 + 任务上下文构造 模态-被试-任务 条件向量
3. **函数约束潜空间**：在源 adapter 学到的函数约束潜空间中生成权重——直接权重回归缺函数监督会退化

目标数据集在训练与模型选择中完全 held-out。

## 结果

6 个 held-out 目标数据集 × 3 个 EFM backbone：
- 平衡准确率较 EEG-only 推理 +7.22pp，较直接权重回归 +4.89pp
- 距监督多模态适配平均仅差 0.50pp
- 消融：表征学习或条件生成任一去掉函数监督均退化——两组件缺一不可
