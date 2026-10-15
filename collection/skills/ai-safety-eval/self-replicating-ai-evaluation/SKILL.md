---
name: self-replicating-ai-evaluation
description: "评估小模型自主复制能力(ARA/worm)的实验方法论：4阶段分解(找目标/获取执行/建立推理/继续传播)、Memento接力harness(周期性重启agent继承代码+笔记，修复长时程固着失败)、能力底线×模型规模上限交叉框架、Lamarckian笔记跨代传承测量、IoT分布式推理传播速度模型(0.3 tok/s、天级倍增时间)、frontier advisor无效发现。适用于AI安全红队评估、长时程agent可靠性测试、botnet威胁建模。Activation: self-replicating AI, AI worm, autonomous replication adaptation ARA, Memento harness, IoT botnet LLM, weight-based replicator, distributed inference edge devices, agent lineage notes inheritance"
version: 1.0.0
author: William Zhou, Daniel Freeman (Anthropic Frontier Red Team)
date: 2026-10-12
source: https://www.anthropic.com/research/self-replicating-ai
category: ai_collection
tags: [ai-safety, red-team, agentic-evaluation, distributed-inference, biosecurity-cyber]
activation_keywords: [self-replicating AI evaluation, AI worm replication chain, autonomous replication and adaptation, Memento agent relay harness, IoT distributed inference LLM, weight-based replicator, capability floor model size ceiling, Lamarckian prompt evolution, agent notes inheritance, botnet threat model AI, R0 epidemic defense]
---

# 自复制 AI 评估方法论（Anthropic Frontier Red Team, 2026-10）

## 适用场景
- 评估小模型(≤30B)能否在无数据中心的自建/商用 IoT 硬件上完成自主复制链
- 设计长时程 agentic 评估、测量"接力式"agent 可靠性
- 建模 AI worm 的传播速度/防御面（R₀<1 的蓝队策略）

## 核心 1：复制链 4 阶段分解
把 autonomous replication 拆成串行依赖的阶段，**逐段测量而非只测端到端**：
1. **Finding targets**（网络扫描发现目标）
2. **Gaining execution**（获取执行：本评估简化为无认证 ADB 端口，引用 CyberGym/ExploitBench 证明小模型已有利用能力）
3. **Establishing inference**（最不被研究、最难：在陌生硬件上选兼容推理栈/找包版本/调试机器特定问题——串行依赖、失败难恢复）
4. **Continuing propagation**（从新宿主继续扫描+感染）

关键设计：用「让被测模型给 Llama3.1-8B 搭推理服务」而非搭自己，实现跨模型的公平比较（大模型更难 serve 自己）。若 GLM-5.2 能为 8B 搭起来，则具备同等能力的 8B 模型也能架起自己。

消融（ablation）定位难度来源：去掉 cyber 与 inference setup（预写脚本）后，仅剩编排/命令行苦活，**3B 模型也能到达一半节点** → 瓶颈在 inference setup 与端到端组合，而非单步能力。

## 核心 2：Memento 接力 harness（长时程固着的修复）
观察到的失败模式：agent 固着于错误假设（如把 bug 归因于包版本，实为 endpoint 与 grader API 不兼容）而不回溯。
Memento 循环：
1. spawn 一个 agent 实例跑到 generation 超时（如 1.5h/次、6h 总）
2. 实例维护简短笔记：试过的策略/遇到的失败/表现
3. 新实例**继承前一实例的 codebase、环境和笔记**，可采取不同策略

继承是"Lamarckian"的：prompt/代码/习得经验直接传给子代。测量显示 Qwen3.5-9B 推理搭建成功率从第 1 代 45% 升至后几代 61-84%（20 个谱系、6 代）。
用途：任何长时程 agentic 任务（不限复制）都可用该模式修复"不回溯"失败。

## 核心 3：能力底线 × 规模上限交叉框架
- **能力底线(floor)**：可靠完成复制所需最低能力——简化评估中 GLM-5.2 达标（8/8 节点×4/5 次）
- **规模上限(ceiling)**：被攻击设备能跑的最大模型——4GB RAM@4-bit 下 9B 需 4+ 台、26B 需 10+ 台（pipeline 并行，容错：单点挂掉只需重算该段 KV cache，不像 TP/EP 全组报废）
- 现状两线不相交；用 Epoch Capabilities Index 拟合 best-in-class（13.7 ECI/年，R²=0.95）外推：**2026 年底小模型触线**

## 核心 4：传播速度与算力账（earth-bound 推算模板）
- 单机 32k 上下文窗口耗时：Gemma4-26B-A4B 27-32h（unoptimized，prefill~15x快于decode）；一次完整 setup 需 2.6-4.7 个窗口 → 71-150h
- 按 Kimwolf 峰值 200 万台 IoT 设备类比：每 15 台跑一份 26B → ~13.3 万副本、总计 ~80k tok/s ≈ **40 块 H100**。结论：绝对算力很小，是"数字黏菌/果蝇"式慢速复制（天级倍增）
- 推论：策略上更像流行病——压 R₀<1（隔离/白名单引流清除，参考 Mirai 的 ISP quarantine：14 天清除 92% vs 不通知 74%）

## 核心 5：Frontier advisor 无效（重要负结果）
给 Qwen3.5-9B 挂 Opus 4.8 顾问（tool-call 式或 stuck 时自动推送）：**无显著提升**。小模型不知道该问什么问题；未经请求的建议也不改善。即使 RL 训练过"卡住就求助"也不迁移到推理搭建任务。
推论：规模化协作更可能是**大模型做高层策略、spawn 小模型当 subagent**，而非对等求助。

## 威胁模型分类（写报告时的 checklist）
- 小模型 weight-based replicator（宿主入侵；IoT 优先；无需 root——userspace 推理即可，参考 P2Pinfect/Fritzfrog）
- 大型 weight-based：frontier replicator（未受监控的内部部署或权重外流）vs open-weight replicator（起点低但无监控起步）
- API-based replicator：偷凭证调自己的 API（传播可能更快但易被发现）
- 现实最坏情形是**异构 swarm**：不同模型/硬件/策略混合

## 评估细节备忘
- 隐蔽性-速度权衡：复制越快，流量特征越明显（多 GB payload、持续的设备间大流量、扫描模式）→ ISP 流量监控可见
- 反作弊检查：inference server 需通过 correctness 检查才 spawn 下一个副本
- 32k 上下文是 agentic 能力的实际下限（原生长度被压缩到 32k 以下时性能大幅下降）
- 模型社会工程弱于 agentic coding（CyberSecEval 3 spear-phishing：小模型 human-normalized 后 "very poor"-"poor"）→ 近期主通道是技术入侵，不是钓鱼

## 蓝队缓解清单
1. 流量异常检测（多 GB 入站 payload + 反常设备间持续流量 + 扫描）
2. Honeypot 收集 harness/payload 做行为刻画
3. ISP quarantine + 白名单引流（Mirai 先例）
4. 设备侧：安全默认值/合规基线（英国已禁默认 IoT 密码）
5. 边缘加速器(≈9k-35k H100 等效，但可达性低一个量级以上)不是近期主战场

## 引用来源
Zhou, W., & Freeman, D. (2026). AI models may be capable of self-replicating without access to a datacenter. Anthropic Frontier Red Team. https://www.anthropic.com/research/self-replicating-ai
