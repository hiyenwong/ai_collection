---
name: loopcd-contrastive-decoding-looped-transformers
description: Looped Transformer推理加速时用。免训练对比解码：用早期循环弱预测对比最终预测引导token选择。Activation: looped transformer, contrastive decoding, inference acceleration, recurrent depth, weak-strong pairs, training-free decoding, inference FLOPs reduction
metadata:
  arxiv_id: "2610.02185"
  published: "2026-10-01"
  authors: "Weihao Liu, Huangjie Zheng, Tianrong Chen, Rohit Dilip, Richard He Bai et al. (8 authors)"
  source: "arXiv cs.LG"
  tags: [looped-transformer, contrastive-decoding, inference-efficiency, training-free]
---

# LoopCD: Decoding Looped Transformers Better for (Almost) Free

## 核心洞察

Looped Transformer 共享参数块循环执行，**每个循环产出可解码同一 next token 的中间表示**——早期循环 = 弱模型，最终循环 = 强模型。递归结构天然提供**对齐的 weak-and-strong 预测对**，无需辅助模型或额外训练——正是对比解码（CD）需要的原料。

## 两个变体

**LoopCD-Logits**（logit 空间）：
```
p_CD ∝ p_final(y)^(1+α) / p_early(y)^α
```
额外开销 = 一次早期循环的输出投影 pass。

**LoopCD-Hidden**（隐状态空间）：
在 hidden state 上做外推修正（沿 final→early 差方向调整），零输出层开销。

## 使用要点

1. 选择早期循环 k（如第 1 个循环）作为弱专家；α 控制对比强度
2. 收益 + 剪深联合：CD 增益可**减半循环数**仍匹配/超过全深度无引导基线 → 前向 FLOPs 降 22.5%–48.2%
3. 完全 training-free：不改权重、不改训练，仅解码期变换

## 结果（4 个 looped Transformer 家族）

- Ouro-2.6B-Thinking AIME 2024 pass@1：61.88% → **73.33%**（LoopCD-Logits）
- Huginn HumanEval pass@1：22.56% → **31.71%**（LoopCD-Hidden）
- 全深度增益显著且跨家族一致

## 何时使用

- 任何共享权重循环/递归深度模型（looped transformer、recurrent-depth LLM）的推理优化
- 有"同源弱-强预测对"的架构皆可类比：早 exit 层 vs 最终层、浅 rollouts vs 深 rollouts
- 推理算力受限（移动/边缘）下用解码期变换换取等效深度

## References

- arXiv: https://arxiv.org/abs/2610.02185
