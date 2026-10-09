---
name: bot-grpo-bag-of-token-aggregation
description: Use when doing GRPO-style LLM RL with token-level process rewards. BoT-GRPO length-invariant bag-of-tokens aggregation gives per-token advantages, critic-free, drop-in GRPO replacement.
created: 2026-10-08
version: 1.0
author: hermes-cron (from Yang et al., arXiv:2610.09804)
license: CC-BY-NC-SA-4.0 (paper); skill text original
source: arXiv:2610.09804
tags: [llm-rl, grpo, process-reward-model, credit-assignment, token-level-reward, reasoning]
metadata:
  hermes:
    tags: [llm-rl, grpo, process-reward-model, credit-assignment, token-level-reward, reasoning]
    related_skills: [carm-cancellation-aware-response-masking, dash-divergence-adaptive-supervision-horizons]
---

# BoT-GRPO: Efficient Process-Reward RL via Bag-of-Token Aggregation

**Source:** Yang, Xiao, Wang, Flashner et al., arXiv:2610.09804, Oct 2026, cs.LG.

**Trigger:** 用 GRPO 训练 LLM 但手上有 token 级 process reward model（PRM），想在不引入 value network 的前提下把细粒度奖励变成 per-token advantage；或 GRPO 收敛太慢/质量受限。

## 核心问题

GRPO 对同一 rollout 内所有 token 赋相同 advantage（outcome 级），浪费了 token 级奖励信号。直接用 value network 做 process supervision 成本高、训练不稳。目标是：**critic-free** 地把 token-level reward 融进 group-relative 框架。

## 方法：Bag-of-Tokens 聚合

把整个 rollout group 的 token 级奖励"打散进一个袋子"再做组统计：

1. **收集**：一个 prompt 的所有 rollouts、每个 rollout 的所有 token-level rewards 全部收集
2. **长度不变加权**：每个 token reward 乘以其来源序列长度的倒数 `1/|y_i|` —— 消除长 rollout 在统计中的主导（length-invariance）
3. **组统计**：per-token advantage 相对加权后的组均值/方差计算（替代 GRPO 的 outcome 组统计）
4. **Drop-in**：其余训练循环（clip、组采样）不变，凡用 GRPO 处可直接替换

关键洞察：per-token 优势不需要逐位置 critic —— 只需要一个跨 rollout 的聚合统计来"中心化"token 奖励。

## 奖励模型配方（重要实验结论）

**稳定性 > 丰富性**：干净、有界、稳定的细粒度信号一致加速学习；噪声大的替代品会让训练停滞。选 PRM 时优先 bounded + stable，而非信息量大但 noisy。

## 结果

- React 前端代码生成：80% compile rate，达速比 GRPO 快 1.9×；收敛快于 GSPO/DAPO/PURE，最终 compile 与 VLM-judged win rate 更高
- AIME 数学推理：Pass@k 绝对提升最高 8.1%，步数减半
- reasoning 与非 reasoning 底座（Qwen2.5-3B / SmolLM3-3B / Phi-4-mini-reasoning）均有效

## 实现要点

- token-level reward 可来自 PRM、编译器/单测输出、工具反馈等任意来源
- 加权统计注意数值稳定（组内 reward 方差过小时按 GRPO 惯例跳过该组）
- 与 importance-ratio clip、async rollout 引擎兼容（不改变 actor 目标形式，仅换 advantage 来源）

## Activation

process reward model, token-level reward, GRPO variant, per-token advantage, critic-free RL, PRM integration, group relative policy optimization, LLM reasoning RL, code generation RL
