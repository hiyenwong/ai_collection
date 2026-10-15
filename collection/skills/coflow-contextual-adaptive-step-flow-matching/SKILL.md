---
name: coflow-contextual-adaptive-step-flow-matching
description: "Flow Matching图像/视频生成加速时用。COFLOW：推理时按prompt特征自适应选步数，在线无监督奖励训练，免重训底层生成模型即插即用，2.5x加速保质。Activation: flow matching acceleration, adaptive NFE, step count selection, image generation efficiency, video generation, inference-time optimization, O(1/K) discretization"
metadata:
  arxiv_id: "2610.03202"
  published: "2026-10-02"
  authors: "Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal"
  source: "arXiv cs.CV/cs.AI"
  tags: [flow-matching, inference-efficiency, visual-generation]
---

# COFLOW: Contextual Flow Matching — 自适应步数选择

## 核心问题

Flow Matching 推理成本高（多次串行函数评估）。现有加速法（蒸馏、少步模型）需要额外训练、损质、且忽略**输入依赖的难度差异**——简单 prompt 无需与复杂 prompt 相同的步数。

## COFLOW 方法

推理时方法，按每次生成的 prompt 特征自适应选步数：

1. **上下文感知步数预测器**：从 prompt 特征预测该样本所需步数 K
2. **在线训练**：无监督奖励 = 推理效率与生成保真的平衡（无需人工标注的难度标签）
3. **即插即用**：底层生成模型冻结，不重训

## 理论

标准正则条件下 forward-Euler 离散化误差 O(1/K) 上界——为自适应步数提供收敛依据。

## 结果

图像与视频生成通用，>2.5x 加速且感知/语义质量保持。
