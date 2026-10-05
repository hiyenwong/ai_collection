---
name: pivot-sd-masked-diffusion-self-distillation
description: "Masked diffusion语言模型(dLM)后训练/自蒸馏时用。Pivot-SD：仅监督去噪中高影响力commitment(pivot)，信息增益选点+失败轨迹定向unlikelihood。Activation: masked diffusion LM, dLM post-training, self-distillation, credit assignment, denoising commitment, unlikelihood training, LLaDA"
metadata:
  arxiv_id: "2610.03665"
  published: "2026-10-02"
  authors: "Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, Chen-Hao Chao, Se-Young Yun et al."
  source: "arXiv cs.LG/cs.CL"
  tags: [masked-diffusion-lm, self-distillation, credit-assignment, post-training]
---

# Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models

## 核心问题

Masked diffusion LM（dLM）并行生成中存在独特的 credit assignment 难题：去噪过程中少数 **commitment**（把某些 mask 位置定为具体 token）会急剧降低剩余 mask 位置的不确定性，主导整条 response。现有 post-training 要么训练最终文本、要么把 reward 分给整个去噪 step，都不定位这些关键 commitment。

## Pivot-SD 方法

离线自蒸馏，只监督高影响力 commitment（pivots）：

1. **Pivot 选择**：信息增益度量 = 该 commitment 对剩余 mask 位置的不确定性缩减量
2. **成功轨迹**：pivots 用 cross-entropy 训练
3. **失败轨迹**：仅对 pivots 施加定向 unlikelihood，其余部分不动（不污染失败样本中的有效片段）

## 实现要点

- 离线框架：先采样 rollout 再离线训练，无需在线 RL 基础设施
- 极度数据高效：200 个问题 × 4 rollouts 即可
- 失败轨迹处理是关键差异点：整体 SFT 会把错误也学进去，整体丢弃浪费有效片段，pivot 级定向 unlikelihood 两全

## 结果

LLaDA-8B-Instruct 在数学与代码基准上同时超越 full-sequence SFT 与 budget-matched diffusion RL 基线。
