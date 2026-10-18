---
name: long-horizon-llm-scientific-compute
description: "长时程LLM科学计算执行模式：Fable 5.1在Claude Science harness内用'简单prompt+keep going'指令完成N=4 super-Yang-Mills九圈振幅计算——两条独立路径(bootstrap+form factor)，~$100/96CPU一周，一夜无监督指令('我在睡觉，继续工作每4-6小时汇报')。核心启示：专家以为的算力壁垒实为'没人雇程序员'的低垂果实。适用于设计长时程agentic科学任务、评估LLM计算极限、harness设计。Activation: long horizon agent task, nine loop amplitude, scattering amplitude AI, keep going prompt, academic compute budget, LLM scientific computing, unattended research run"
version: 1.0.0
author: Matt von Hippel (guest post); Liam Fitzpatrick & Siddharth Mishra-Sharma (Anthropic)
date: 2026-09-25
source: https://www.anthropic.com/research/yes-claude-can-do-nine-loops
category: ai_collection
tags: [agentic-computing, scattering-amplitudes, long-horizon-tasks, llm-harness, computational-physics]
activation_keywords: [nine loop amplitude, N=4 super Yang-Mills, scattering amplitude bootstrap, long horizon LLM run, keep going prompt, unattended scientific computation, academic compute budget, low hanging fruit science, form factor approach, Claude Science harness]
---

# 长时程 LLM 科学计算（九圈振幅案例）

## 案例核心

挑战（von Hippel 2026-08 博客）："用学者级算力解决振幅学前沿问题，证明大家以为的算力极限不是问题——N=8 supergravity 到七圈，或 N=4 SYM 到九圈。"

一个月后被完成：
- 模型 Fable 5.1 + Claude Science harness（结构化规则/提示使行为更稳健科学）
- 初始 prompt 极简："计算 planar N=4 SYM 六粒子（六边形）振幅的九圈项"
- 后续人类输入几乎只有："我要睡觉了，接下来几小时不在。继续工作直到我叫停，每 4-6 小时汇报。"
- 模型用**两条独立路径**完成：原版 bootstrap + 间接 form-factor 方法，互为验证
- 成本：bootstrap 路径 ~$100 = 96 CPU 跑一周（SymPy/Python）；整体 $1000–2000/路径
- Lance Dixon（SLAC，八圈记录保持者）验证了结果

## 与人类的赛跑

几乎同时，中科院 Song He 组用 GPT-6 辅助（人类主导）拿到结果的主体。人类将发表并分析结果；Claude 的角色已完成。**作者结论：这不是 AI 突破算力壁垒的奇迹，而是低垂果实比专家以为的多得多**——CS 背景的人多年来说"振幅学家雇几个程序员就能大进一步"，他们是对的。

## 可复用模式

1. **"极简 goal + keep going"**：长时程任务的 prompt 工程不是写 16,000 词的操作手册，而是给清晰目标 + 持续运转许可 + 定期汇报节奏
2. **双路径独立验证**：让模型用两种方法解同一问题（bootstrap vs form-factor），天然交叉校验——比单路径+人工审查便宜得多
3. **"专家以为做不到"是信号**：当专家群体认为某计算"原理上可行但没人有算力/人手"，这是 LLM agent 的甜区——不是需要新想法的问题，是需要无限耐心+良好软件工程的问题
4. **预算敏感的任务选择**：先问模型自己最可能攻克哪个问题（Fitzpatrick/Mishra-Sharma 先问了 Claude），再投入
5. **工具链现代化红利**：Python+SymPy vs Maple/Mathematica 可能是隐性优势——LLM 带来的不只是智力，还有软件工程实践
