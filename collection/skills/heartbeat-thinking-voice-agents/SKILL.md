---
name: heartbeat-thinking-voice-agents
description: Use when building realtime voice agents that call tools during speech. Heartbeat Thinking - overlapping Thinker invocations with non-blocking speculative preparation and cancellation-at-handoff.
category: ai_collection
metadata:
  arxiv_id: "2610.26233"
  published: "2026-10-19"
  authors: "Zhang, Fu, Tong, Zheng, Wu, Yang, Li (Ant International)"
  source: "arXiv cs.CL"
---

# Heartbeat Thinking: 语音输入期间的投机推理与工具执行

**论文**: "Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents" (arXiv:2610.26233, Ant International)

## 核心思想

语音 agent 的可执行信息往往在请求的中途就已到达（用户还在描述配送问题时订单号已出现），但级联管线把推理+工具调用全部推迟到语音结束。已有投机方法的共同缺陷是**把计算时间耦合到语音更新上**：

- **SHANKS / Window Thinking**：每段生成被语音 chunk 边界截断——工具调用参数没生成完就被掐掉
- **SIA / interrupt-on-update**：新事件中断进行中的生成——调用可能还没发出就被打断

Heartbeat Thinking 的原则：**新输入由新调用处理，进行中的调用和已派发的工具让它们跑完**。听的时间变成可复用的准备时间。

## 架构

**周期 Thinker（听期间）**：
- 每 Δ 秒（实验用 500ms）触发一次新 Thinker 调用；最多 K 个并发（K=2），槽满则跳过本次触发
- 每次调用读：最新部分 transcript + 共享记录（已完成推理、已请求的调用、工具返回结果）
- 新语音和工具结果进入**下一次**调用，绝不中断进行中的生成
- 单次调用可：不动作 / 返回推理 / 请求带结构化参数的工具调用
- 推理先落盘共享记录，工具再异步派发 → 模型推理与工具执行重叠
- 后续调用用返回结果补齐缺失参数、发起依赖调用——**即使 transcript 没有更新，准备也能推进**（区别于 chunk 触发式）
- prompt 指示避免重复 pending/已完成的名字+参数完全相同的调用
- Thinker 与 Responder 可用不同模型（实验 Thinker=Qwen3.6-35B-A3B）

**Handoff（VAD 检测语音结束）**：
- 调度器停止新调用，**取消**未完成的 Thinker 与投机工具任务（含排队中的）
- Responder 收：最终 transcript + 历史 + schema + **完成准备的快照**（之后的投机输出丢弃）
- Responder 走 ReAct：对照完整请求检查准备，**拒绝被后续语音推翻的解读**，复用适用结果，缺失的调用自己执行——不等未完成的准备

## 结果（SpeechFCEval / FDBench v3 / AudioCRAG）

- FDBench v3：投机工具覆盖率 STC 34.67%→50.67%（+16pp），平均最终响应延迟 6.90s→4.39s（**−36.4%**，比最快级联基线 Pipecat 低 45.7%）；Quality 72.0→77.0
- 覆盖率优势跨 3 个不同 Responder（DeepSeek-V4-Flash / Qwen3.5-397B-A17B / Qwen3.8-Flash-Next）保持
- **诚实负结果**：最终任务质量与 benchmark 相关——FDBench 提升，但 SpeechFCEval acc 67.95→66.85、AudioCRAG correct 57.24→55.49 均略降。解释与复用投机结果本身是独立挑战：覆盖更多 ≠ 用得更好
- STC 定义：参考调用中被"已完成的匹配投机调用"覆盖的比例（结果进入 Responder 上下文且未重复执行）

## 设计清单（实时语音 agent 投机执行）

1. 触发与生成分离：新触发只影响后续调用，永不打断进行中的调用/工具（chunk 截断和中断是主要失败模式）
2. 跨调用状态用**共享记录**（完成推理+调用+结果）而非模型内部状态传递
3. 推理先落盘再派发工具，让模型与工具并行
4. 无 transcript 更新也照常触发——工具结果本身驱动下一跳（依赖链）
5. Handoff 硬边界：取消未完成投机任务 + 快照语义（之后到达的一律丢弃），Responder 免等待
6. Responder 必须显式校验投机结果对完整请求的适用性（用户后半句可能推翻前半句的解读）
7. 去重约束写进 Thinker prompt（同参数调用不重复）
8. 评测时分开报告覆盖率与最终质量——两者会背离

## 局限

- 质量提升 benchmark 依赖；投机解释的复核/复用策略是开放问题
- Δ 与 K 是新的超参；未覆盖 barge-in（用户打断响应）场景
- 共享记录增长需要截断策略（论文以完成记录为界）

## 相关 skill

- [[voice-agent-patterns]] — 语音 agent 交互模式总览
- [[speculative-decoding-optimization]] — token 级投机解码（不同层次的投机）
- [[rt-opd-reward-tilted-distillation]] — 推理模型延迟优化
