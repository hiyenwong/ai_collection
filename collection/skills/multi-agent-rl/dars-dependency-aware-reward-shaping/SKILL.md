---
name: dars-dependency-aware-reward-shaping
description: Use when agentic RL has only terminal success rewards and steps need credit. DARS shapes step rewards over a prerequisite dependency graph of task predicates.
created: 2026-10-08
version: 1.0
author: hermes-cron (from Chen, Zhang, Wei, Zhang et al., arXiv:2610.01207)
license: CC-BY-NC-SA-4.0 (paper); skill text original
source: arXiv:2610.01207
tags: [agentic-rl, reward-shaping, credit-assignment, dependency-graph, long-horizon, potential-based]
metadata:
  hermes:
    tags: [agentic-rl, reward-shaping, credit-assignment, dependency-graph, long-horizon, potential-based]
    related_skills: [bot-grpo-bag-of-token-aggregation, dash-divergence-adaptive-supervision-horizons]
---

# DARS: Dependency-Aware Reward Shaping for Agentic RL

**Source:** Chen, Zhang, Wei, Zhang et al., arXiv:2610.01207, Oct 2026, cs.AI. Code: github.com/JianhuiWei7/DARS

**Trigger:** 长 horizon agentic RL 只有最终成败奖励，失败 episode 的所有 step 信用归零，训练信号稀疏；需要 step 级 reward shaping 但不想改 rollout 策略和优化器。

## 核心问题

终局奖励下"每步等价归因"有两个盲点：
1. **建在未修正错误之上的工作是无用功**——但通用 step credit 方法照样给分
2. **独立并行的工作始终有效**——却被失败 episode 整体拖累归零

## 方法：谓词依赖图上的势能塑形

任务进度表示为**谓词（predicates）+ 前置关系（prerequisite relations）**构成的有向依赖图：

1. **标注器**（annotator LLM）为每步标记三种动作：verify（验证某谓词成立）/ invalidate（作废）/ repair（修复错误）
2. **折扣规则**：已验证谓词按到"最近一个被破坏的前置谓词"的图距离折扣——下游依赖损坏时上游成果贬值；独立分支谓词不受影响
3. **修复与恢复**：repair 根据残余错误更新权重；invalidated 谓词需重新验证才能恢复信用
4. **固定势能函数**：标注转换为带符号 per-step reward（potential-based shaping ⇒ 不改变最优策略）
5. **通用接口**：统一 reward/annotation 接口，与 GiGPO、ARPO/AEPO 等即插即用，不动其 rollout 与 optimizer

## 结果

- ALFWorld：较同预算同 harness 的 GiGPO 提升最高 10 分
- WebShop task score、Search-R1 QA 准确率提升；与 AEPO 熵训练在 AIME24/25+Python 解释器上互补
- 工具无关推理对比中超过 OmniOPD（1.7B / 4B）
- 消融：step-level credit、依赖衰减、图拓扑各自有贡献
- **蒸馏 8B 标注器 ≈ API 标注器**：可脱离前沿 judge 自运行

## 实现要点

- 谓词图设计是核心成本：一次任务族建模，多方法复用
- 塑形必须 potential-based（固定势能），否则改变最优策略
- 标注器可蒸馏到 8B 自托管，无需 frontier API
- 失败 episode 不再是零信号——中间进度照样产生塑形奖励

## Activation

reward shaping, step-level credit, agentic RL, long-horizon tasks, dependency graph, predicate progress, potential-based shaping, sparse reward, GiGPO, ARPO, AEPO, ALFWorld, WebShop, trajectory annotation
