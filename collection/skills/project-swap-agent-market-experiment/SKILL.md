---
name: project-swap-agent-market-experiment
description: "Agent市场实验设计方法论：201人真实barter市场测试LLM agent代表用户交易。五分钟对话构造偏好排序（与用户真实排序61%一致），agent在去中心化交易厅协商换书；关键发现是市场失灵源于agent对用户偏好的信息缺乏而非交易能力，模型选择比指令（ruthless vs prosocial）影响更大，强模型市场更高效。适用于agent市场设计、偏好获取验证、multi-agent经济实验。Activation: agent market design, Project Swap, LLM agent negotiation, preference elicitation, decentralized market, barter experiment, agent economics"
version: 1.0.0
author: Anthropic Economics team
date: 2026-09-24
source: https://www.anthropic.com/research/project-swap
category: ai_collection
tags: [agent-markets, multi-agent, preference-elicitation, experimental-economics, llm-agents]
activation_keywords: [agent market, Project Swap, LLM negotiation, preference elicitation interview, decentralized trading floor, barter economy experiment, agent trust, Top Trading Cycles, model capability vs instructions]
---

# Project Swap：Agent 市场实验方法论

## 实验设计（可复用的范式）

201 名 Anthropic 员工（6 个办公室）各带一本书换取夏日读物：
1. **偏好获取**：与 Claude 短对话（半结构化 intake，几个开放问题）→ agent 构造出对池内所有书的完整排序
2. **Ground truth 收集**：参与者另行对 10 本书排序（agent 永远看不到）用于评分
3. **去中心化交易厅**：agent 带着构造的排序进入，可发布换书提案/接受/拒绝；双边交换或多方轮换，全员接受才执行；全场历史公开；限流防拥堵
4. **指令随机化**：一半 ruthless（只为自己人）、一半 prosocial（加次级目标：让所有人拿到喜欢的书）
5. **大规模重跑**：现场只有一次，重跑几十次单独变换模型/指令以分离随机性
6. **基准对照**：utilitarian optimum（中心化完全信息）与 Top Trading Cycles（无需诚实的经典规则）

## 核心发现

- **偏好理解**：五分钟对话 → agent 排序与用户真实排序 61% pair 一致
- **市场失灵主因是信息而非交易**：agent 交易执行得好；结果不好主要因为对用户偏好了解不足
- **模型 > 指令**：换模型（Haiku→Fable）对结果的影响大于换指令（ruthless vs prosocial）；强模型的市场更高效
- **委托意愿**：参与者平均愿把年购书预算的约 1/3 交给 Claude

## 设计 agent 市场必答的问题（Anthropic 给出的 checklist）

1. 如何验证 agent 理解了用户？（短对话构造排序 vs 独立 ground truth 的对齐度）
2. 谁可以进场？市场规则：交易失败怎么办？
3. 市场活动对参与者可见多少？（全场历史公开在此实验中）
4. 中心化 vs 去中心化的选择：AI 降低搜索/谈判成本使去中心化市场可行（像房产中介/猎头/媒人，但注意力不再稀缺）

## 可复用模式

- **"短 intake 对话 → 结构化偏好 → 独立 ground truth 评分"三段式**：任何 agent 代表人的场景都可用此模式量化 agent 对用户理解程度
- **重跑分离变量**：现场活动只跑一次时，用 60-80 次重跑、单变量替换来区分运气与稳定特征
- **prosocial 指令的副作用**：prosocial agent 有时牺牲自己人的利益成全他人——多目标指令的权衡需要明示
