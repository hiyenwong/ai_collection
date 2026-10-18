---
name: dkgi-knowledge-graphs-as-files
description: "Agent直接把KG当文件用Python读写,工具创建与使用共演化,Hit@1超最强基线6.7+"
version: 1.0.0
author: Yuyang Bai, Yu Wang, Yu Zhang. arXiv:2610.18616
date: 2026-10-18
source: https://arxiv.org/abs/2610.18616
category: ai_collection
tags: [knowledge-graph, agent-harness, tool-use, rag, code-interpreter, information-retrieval]
activation_keywords: [text-rich knowledge graph search, agent harness tool creation, DKGI direct graph interaction, KGQA multi-hop, shell grep over graph files, program synthesis retrieval, STaRK benchmark, tool use co-evolution, training-free agent]
---

# DKGI: Knowledge Graphs as Files（工具创建与使用共演化）

## 适用场景
- 文本富集知识图谱（text-rich KG）上的多跳问答/检索（STaRK-MAG/Amazon/PrimeKB 类）
- 预定义图接口（neighbors API、子图 retriever）截断了 agent 可访问的证据时
- 需要批量处理大节点集 + 精选文本证据的 agent 架构设计

## 核心论点
预定义图接口（bounded neighbors 调用、top-k 子图检索）**结构性截断证据**：STaRK-MAG 例中 neighbors 调用只返回 66 个研究者中的 20 个，gold paper 永远不会被看到。解法不是更好的 retriever，而是**取消接口本身**——把完整节点/边文件直接给 agent。

## 方法（Direct Knowledge Graph Interaction）

### 1. KG as Files
- 完整图导出为平铺文件：nodes 文件（每行一个节点+全部文本属性）、edges 文件（每行一条边）
- 无 API、无 retriever、无 schema 抽象层——agent 用 shell（grep/awk）+ Python 直接读写

### 2. Agent 写代码做图操作
- 跟随关系：写 Python 循环沿边走多跳
- 集合代数：合并节点集、求交、过滤（Case 2: 一个程序=对两个关系的集合代数）
- 文本证据筛选：大输出落盘成文件，只把选中片段返回给模型上下文

### 3. 工具创建与使用共演化（关键机制）
- 执行反馈驱动代码修订：报错→修 bug；结果不足→扩搜索（Case 3: 一次错误修复+四轮逐步收窄的过滤器）
- 演化中的工具决定下一步能取什么证据——工具即证据访问能力
- 轨迹显示 agent 会主动**重写自己早期的检索代码**来扩展搜索面

### 4. 大输出处理
- 批量图操作在代码里跑（不占 LLM 上下文）；只有"选中的文本"回给模型判断
- 这解决 token 瓶颈：处理 10 万节点但只让模型看 50 条候选

## 结果
- 训练免费（training-free），最小 harness 下所有三个域 STaRK Hit@1 超最强已发表基线 ≥6.7 分
- 消融：多轮编程 > 纯 shell 访问 > 预定义图工具（三者严格排序）

## 与相关 skill 的关系
- [[cqc-rag-cross-query-consistency]]：查询间一致性是输出侧质量保障；DKGI 是访问侧的结构解法
- [[reasoning-driven-retrieval]]：检索即推理的迭代观一致；DKGI 给出"工具演化"这一具体机制

## 可迁移设计模式
1. **接口即瓶颈**：当预定义工具截断证据空间时，给原始数据+编程能力优于给更好的封装
2. **反馈-修订环**：执行错误和结果不足都是一等信号，驱动工具本身演化
3. **批量算+精选读**：计算在代码层、判断在语言层——上下文只花在语义判断上
4. 对自建 agent（如 Hermes cron）的启示：与其给固定的 search 工具，不如给 sqlite/grep+写脚本能力

## 引用
Bai, Y., Wang, Y., Zhang, Y. (2026). Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve. arXiv:2610.18616. Code: github.com/leopoldwhite/DKGI
