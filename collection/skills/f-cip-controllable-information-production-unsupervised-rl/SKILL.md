---
name: f-cip-controllable-information-production-unsupervised-rl
description: 无监督RL内在动机设计时用。仅由系统动力学定义的F-CIP目标，无需选择信息变量。Activation: unsupervised RL, intrinsic motivation, controllable information, empowerment, reward-free exploration, primitive behavior discovery, forward CIP, robotics pretraining
metadata:
  arxiv_id: "2610.02012"
  published: "2026-10-01"
  authors: "Tristan Shah, Wooyoung Chung, Volodomyr Makarenko, Juan Wachs, Stas Tiomkin (Purdue)"
  source: "arXiv cs.LG"
  tags: [unsupervised-rl, intrinsic-motivation, controllability, empowerment, reward-design]
---

# F-CIP: Unsupervised RL via Forward Controllable Information Production

## 核心问题

现有内在动机（IM）目标都要**选择信息变量**（哪些状态维度进目标函数）——把领域专家知识从奖励设计转移到了变量选择，违背无监督 RL 初衷。

## F-CIP：RL 原生的 CIP 形式

**Controllable Information Production (CIP)**：仅由系统动力学定义，无需变量选择：

- 目标 = 最大化智能体**可产生/控制**的信息生产，而非任意状态熵（区分可控信息与噪声扰动）
- **Forward** 形式化：以 RL 兼容的方式表达（可与现有 actor-critic/RL 算法直接组合），证明与 RL 训练管线兼容

## 使用流程

1. 写出环境动力学 p(s'|s,a)（或可采样模拟器）
2. 以 F-CIP 为内在奖励训练（无外部奖励）→ 无监督涌现**原语行为**：平衡、维持可控性
3. 接少量任务奖励（如简单 forward-velocity）→ 涌现协调步态（hopping/running），无需精细奖励工程

## 结果

- F-CIP 单独：发现 balancing、controllability maintenance 等机器人原语行为
- F-CIP + forward-velocity：产生 hopping、running 协调步态（通常需奖励工程才能学到）

## 何时使用

- 免奖励/少奖励机器人预训练：先学可控性原语，再用极简任务奖励解锁复杂行为
- 设计内在动机目标时检查：是否引入了隐性变量选择？能否改为纯动力学定义
- 与 empowerment 类方法对比：CIP 强调"可控信息生产"而非信道容量，避免奖励噪声维度

## References

- arXiv: https://arxiv.org/abs/2610.02012
