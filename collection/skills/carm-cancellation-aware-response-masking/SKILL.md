---
name: carm-cancellation-aware-response-masking
description: LLM RL后训练中off-policy响应过滤时用。序列级掩码的"符号对消"缺陷与绝对值对数比修正（CARM）。Activation: response masking, off-policy RL, LLM reinforcement learning, sequence filtering, policy drift, importance ratio, PPO filtering, GRPO
metadata:
  arxiv_id: "2610.02039"
  published: "2026-10-01"
  authors: "Yafei Zhang, Songshuo Lu, Sicong Liao, Zhi Chen, Yaohua Tang"
  source: "arXiv cs.LG/cs.CL"
  tags: [llm-rl, off-policy, response-masking, importance-sampling, post-training]
---

# CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning

## 核心问题

LLM RL 后训练（rollout 引擎 ≠ 训练引擎、异步更新）中，采样响应部分 off-policy。序列级掩码（决定整个 response 是否参与优化）的标准规则：

```
mask = |(1/T) Σ_t log π_θ(y_t)/π_old(y_t)| ≤ δ    (长度归一化几何均值)
```

**符号对消缺陷**：带符号 log-ratio 可跨位置抵消——某段 token 概率大幅上升、另一段大幅下降，均值却接近 0，掩码误判为"on-policy"，掩盖了**双向策略漂移**。

## CARM 修正

取绝对值后再平均：

```
CARM_mask = (1/T) Σ_t |log π_θ(y_t)/π_old(y_t)| ≤ δ
```

**理论保证**（接受响应的联合界）：接受 ⟹ 同时满足
1. 落在带 [1/δ', δ'] 外的采样 token 比例有界
2. 带外 token 的平均对数距离有界

即接受 = 双侧漂移都受控，无法靠正负抵消蒙混过关。

## 实现要点

1. **逐 token log-ratio**：对 rollout 采样 token 计算 log π_new/π_old（只对采样 token，非 teacher-forced 全 vocab）
2. **绝对值聚合**：mean(|log-ratio|) 与阈值 δ 比较（δ 为超参，典型与几何均值规则同量级）
3. **序列级二值掩码**：整条 response 保留或丢弃，不改动 token 级 loss
4. **兼容性**：即插即用替换现有 masking rule（如 TIS/GM 规则），不改训练循环其余部分

## 结果

- 数学推理：AIME 2024/2025/2026 + BeyondAIME mean@16 提升 up to +3.13 pp over 几何均值掩码
- 代码生成：4 基准平均 pass@1 +2.88 pp over 最强基线
- 消融确认收益来自防对消，非单纯更严阈值

## 何时使用

- 异步/引擎分离 RLHF 或 reasoning RL 训练管线中出现 off-policy 采样
- 诊断：检查 accepted responses 的逐 token log-ratio 分布，若均值小但绝对值大 → 存在对消
- 任何"聚合带符号量再判阈值"的过滤/门控设计都可类比检查对消风险

## References

- arXiv: https://arxiv.org/abs/2610.02039
