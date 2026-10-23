---
name: weil-quadratic-form-rank-zeta-zero-density
description: "ζ零点密度下界：Weil非对角二次型整体正负定+矩信息秩不等式。"
version: 1.0.0
author: Anthropic (Claude research version; validated by L. Alpöge, R. Furmer)
date: 2026-10-23
source: https://www.anthropic.com/research/riemann-zeta
category: ai_collection
tags: [analytic-number-theory, riemann-zeta, quadratic-forms, moment-method, zero-density]
license: MIT
related_skills: krein-space-riemann-xi, random-riemann-zeta-spectrum, goldbach-proposition-weighted-sieves, prime-cohomological-iterative-maps
---

# Weil 二次型秩不等式 → ζ 零点临界线密度下界

## When to Use

- Proving or improving **zero-density / critical-line density bounds** for the Riemann zeta function or general L-functions via explicit-formula positivity arguments.
- Any counting problem where a **quadratic form's signature encodes a target quantity** (e.g. eigenvalue sign statistics) and moment/trace data is computable.
- Designing AI-for-math pipelines that combine mass idea generation with validator subagents and Lean formalization.

Anthropic Claude 研究版在尝试 Riemann 假设时的意外成果：把临界线上零点比例的下界从 41.6%（Conrey）推进到 **67.2%**。专家核验（Levent Alpöge、Ralph Furman）+ Lean 形式化通过 comparator。本文提炼其数学技术与发现流程的可复用模式。

## 核心技术（可移植）

1. **Weil 诱导二次型**：在测试函数空间上由 Weil 显式公式（Guinand–Weil positivity）诱导二次型 Q。零点在线上 → **正定**子空间；零点在线外 → **负定**子空间。目标量（在线零点比例）= 正惯性指数相对全空间的下界。
2. **秩不等式（关键一步）**：用一阶、二阶矩信息写出 Q 的秩不等式。二阶矩经素数侧对偶图景计算，或经 Hilbert 变换控制——解析数论的标准可计算量。
3. **整体处理正负定（突破点）**：把整个空间一起处理——正定与负定同时纳入，且**允许二次型非对角**。此前工作（Montgomery 及后续）只在正定/对角部分论证。非对角不定型的惯性指数计数是超越 41.6% 的杠杆。
4. **文献组合**：Aryan 与 Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh（使 Montgomery 技术不依赖 RH）+ Bombieri (2000)。

## 可复用模式（跨域）

- **惯性指数计数论证**：当二次型的符号差（signature）编码目标计数（零点在线 vs 离线）、且矩/迹可计算时，秩不等式给出密度下界。适用：一般 L 函数零点密度、随机矩阵谱符号问题、量子能级符号统计。
- **非对角化的勇气**：对角化丢弃子空间耦合信息；保留非对角结构+同时处理正负定，常是打破既有界的关键。检查你领域里"大家都对角化/只取正部"的论证是否损失常数。
- **对偶图景**：零点侧不可控的量（二阶矩）换到素数侧可控表达，或经积分变换（Hilbert transform）控制。

## 多 agent 发现流程（参考）

- 2 个 session、31M output tokens；第一轮 650 个想法全部失败
- 第二轮 ~60 subagents：2 核心想法开发者、13 贡献者、30 探索者（未产出）、13 验证者、2 写作者；2,400 条 shell 命令、数百 Python 脚本
- 自我验证闭环：数值对照已知 ζ 零点、subagent 互相 referee、下载 54 篇 arXiv 查新颖性、从零独立重证
- 教训：鼓励性提示（keep going）帮助模型克服对开放问题难度的先验怀疑；意外发现在主线失败中产生

## 验证标准

- 数学结果必须：专家核验 + Lean 形式化双重确认才算成立
- 论文 + 简明专家注记 + 形式化三件套 = AI 产出数学结果的可信输出格式

## 适用场景

- 解析数论：临界线/临界带零点密度、显式公式正性论证改进
- 谱理论：由矩数据推断符号计数/能级统计
- AI for Math：想法生成→验证者筛选→形式化确认流水线设计
