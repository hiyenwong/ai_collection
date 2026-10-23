---
name: prove2me-collaborative-autoformalization
description: "大规模数学形式化（Lean证明）的多agent协作框架。Prove2Me平台维护定理DAG分解依赖、独立文件存定理statement与proof加速编译、自然语言描述支持搜索复用；多agent按DAG并行证明，规避单agent记忆退化；11天完成Fermat大定理形式化（1300万行Lean、29500个中间定理、60亿output tokens）。适用于AI辅助定理证明、证明检查自动化、多agent协作形式化项目。Activation: autoformalization, Lean proof assistant, Prove2Me, multi-agent theorem proving, formal verification, Fermat's Last Theorem formalization, Mathlib, proof DAG"
version: 1.0.0
author: Anthropic Research (Tianyi Peng et al.)
date: 2026-09-04
source: https://www.anthropic.com/research/formalizing-fermats-last-theorem
category: ai_collection
tags: [autoformalization, lean, theorem-proving, multi-agent, formal-verification, dag]
activation_keywords: [autoformalization, Lean, Prove2Me, multi-agent theorem proving, formal verification, FLT, proof DAG, Mathlib, computer-checked proof, collaborative formalization]
---

# Prove2Me：协作式自动形式化框架

## 核心成果

Claude 多 agent 在 11 天内完成 Fermat 大定理的端到端计算机验证证明：
- 1300 万行 Lean（Mathlib 的 5 倍以上）
- 30,300 个定理被证明（最终证明使用 29,500 个）
- ~60 亿 output tokens（通用研究模型，约等于 Claude Fable 5.1）
- 仅用 Lean 三个标准公理；comparator 确认 statement 与 Mathlib 版 FLT 一致

## 关键架构：Prove2Me 平台

多 agent 协作形式化的三大支柱：

1. **定理 DAG（有向无环图）**：把整个证明分解为定理依赖图，agent 依据 DAG 决定下一步尝试哪个证明——这是对抗记忆退化的关键机制，多 agent 可并行工作
2. **statement/proof 分离**：定理陈述与证明存于不同文件，链接独立维护——加速 Lean 编译、最小化资源消耗
3. **自然语言描述**：每个定理 statement 附自然语言版本——支持搜索与复用，产生更简单的证明路径

## 失败模式与修复

早期尝试失败：agent 快速丢失项目状态、停止有效协作。失败贡献了最终证明非样板代码行的 ~7%。
修复 = 切换到 Prove2Me（DAG + 文件分离 + 描述搜索）+ Claude Code 多 agent harness。

## 人类角色

仅高层级指令："Jacobian as a scheme sounds high priority"、"push the Mazur theorem to be done soon"。
证明路线遵循 Darmon–Diamond–Taylor 对 Wiles 证明的简化版本。

## 可复用模式

- **DAG 驱动的任务分配**：任何大型多 agent 项目都可用"任务依赖 DAG + agent 自选可执行节点"替代中央调度，天然支持并行与断点续传
- **statement/proof 分离**：接口与实现分文件、链接独立，加速编译类工作流
- **形式化即自检**：Claude 在证明新结果时并行写 Lean，用部分证明独立检查自己的假设——类似写数值模拟验证轨道
- **消费级可复现**：三个 Claude Max 订阅 + Prove2Me 三天完成 Vinogradov 三素数定理形式化（Hardy–Littlewood 圆法应用）——正确 scaffold 下协作形式化不需要企业级资源

## 适用场景

- AI 辅助数学研究：形式化证明作为 AI 产出可信度的验证层（人审跟不上 AI 产出速度时）
- 任何"长链依赖+可机器验证"的大型项目：DAG 分解 + 多 agent 并行 + 独立验证器
- 降低形式验证门槛：为人类读者写 exposition 的同时附形式化证明将成为常态
