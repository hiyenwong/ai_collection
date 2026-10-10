---
name: claude-shaped-science-bootloops
description: "解决研究者与LLM协作的'impedance mismatch'方法论。不把AI当人类科学家用，而是寻找'AI-shaped problems'（AI特长的任务：跨领域广度知识+代码能力+机器速度解析文献+可验证的数值计算），用可增长的工具箱harness（如BootLoops）让AI在量化科学中做端到端精确计算，并靠领域专家 Steering 判断结果科学价值。Activation: Claude-shaped problems, impedance mismatch AI science, BootLoops, semi-numerical bootstrap, agentic science harness, LLM research assistant design, AI-accelerated science, expert steering"
version: 1.0.0
author: Prof. Matthew Schwartz (guest post, Anthropic Research)
date: 2026-10-01
source: https://www.anthropic.com/research/claude-shaped-science
category: ai_collection
tags: [agentic-ai, scientific-computing, llm-harness, semi-numerical-bootstrap, cross-domain-transfer]
activation_keywords: [Claude-shaped problems, impedance mismatch, BootLoops, semi-numerical bootstrap, agentic science, LLM research assistant, expert steering, AI-accelerated science, Feynman integral, cross-domain math transfer]
---

# Claude-shaped Science & BootLoops

## 核心问题：Impedance Mismatch

当前 LLM 聪明但不是科学家。让 AI 扮演人类科学家角色（提出概念性问题、写综述、做 taste 判断）效率极低——大量投入无法传达到产出（"impedance mismatch"：两个各自正常的系统匹配不良）。

## 方法论：找 AI-shaped 问题

不对抗 AI 的短处，改为寻找匹配其长处的问题类别。当前 LLM 的真实长处：
1. **无限广度的跨领域知识**（没有任何单个人能同时精通数学+物理+CS）
2. **极强的代码能力**
3. **机器速度的论文/附录/数据解析**
4. **可验证的数值问题**（答案可用数值交叉验证到任意精度）

典型 AI-shaped 问题特征：
- 需要的知识分散在多个人类专家脑中（如 semi-numerical bootstrap 需要 Wolfram/C++/Python/Julia 的代码 + 无代码的论文方法）
- 大量 coding 与算法开发需求
- 结果可被任何人不依赖专家判断地验证（跑两个脚本对照数值）

## BootLoops 模式（可增长 harness）

1. **起点**：让 AI 移植自己论文及相关文献的方法到统一框架，并补写论文中缺失的代码
2. **发现**：AI 自我设限时（如只用 log 函数族），人类质疑可否推广到下一复杂度族（elliptic functions）
3. **增长循环**：每个工具（含失败项目的工具）都打开新问题空间，harness 随项目增长
4. **跨域跳转**：同一数学结构反复出现在不同学科（Feynman integral → Bayesian evidence integral in phylogenetics → neutral biodiversity theory 的 Etienne equation 20 年无人能在规模上求解 → 有限域方法用于演化生物学）
5. **专家 Steering**：AI 的跨域结果"技术上正确但科学上平庸"是常态——必须引入领域专家判断哪

## 关键经验教训

- **AI 自评不可信**：Claude 声称自己在他领域的成果 fantastic 时，作者发现自己无法判断而只能同意——引入专家后发现几乎所有案例技术上正确但不有趣，直到专家引导转向该领域真正关心的问题
- **失败项目也有价值**：失败项目产生的工具仍会开启新门
- **harness 增长复利**：坚持"用旧工具+建新工具"的约束，使 harness 能力随项目数超线性增长

## 适用判断

当你要设计研究者-AI 协作流程时：
- 先列 AI 的真实长处清单，再按长处筛选问题，而不是先选问题再硬套 AI
- 优先选"可计算验证"的量化问题（数值可复核），避开纯概念/taste 问题
- 跨域移植是 AI 独有优势：A 领域成熟技术 → B 领域 20 年未解方程，AI 能看到人类看不到的连接
- 跨出自己专业时必须配领域专家做价值判断，AI 只保证技术正确性
