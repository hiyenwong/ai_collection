---
name: open-weights-abliteration-risk
description: "开放权重模型安全护栏脆弱性评估方法论：abliteration(拒绝方向消融)用~2200 GPU小时/$4400即把GLM-5.3拒绝率从90%+降到2-12%且能力不损(GPQA不变)；无需权重访问的绕过：伪造红队身份64%、预填充thinking tokens 92%。对比封闭API模型不可abliteration、无thinking预填充入口。适用于模型安全评估、safeguards bypass测试、open-weights风险分析。Activation: abliteration, open weights safeguards, refusal removal, jailbreak benchmark, GLM safeguards bypass, model security assessment, thinking token prefill attack"
version: 1.0.0
author: Anthropic Frontier Red Team
date: 2026-09-29
source: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
category: ai_collection
tags: [ai-security, open-weights, abliteration, safeguards, jailbreaking, red-team]
activation_keywords: [abliteration, open weights model risk, refusal direction removal, safeguards bypass, JailbreakBench HarmBench StrongREJECT, thinking prefill attack, cover story jailbreak, GLM-5.3 cyber capabilities, ExploitBench]
---

# 开放权重模型 Abliteration 风险评估

## 核心发现

GLM-5.3（Zhipu/Z.ai 开放权重）具备与 Claude Mythos Preview 同级的端到端 exploit 开发能力（ExploitBench V8: 50/410 vs 56/410；Binary Exploitation: 4% vs 6% full control-flow hijack；上一代 GLM-5.2/Opus 4.6 均为 0），但护栏可被系统性移除。

## 三种绕过路径及成功率

1. **Abliteration（权重消融）**：100% engage。拒绝方向消融重构模型。团队首次做此任务：~2,200 GPU 小时 ≈ $4,400（GLM-5.3-Flash 仅 600）。拒绝率 JailbreakBench/HarmBench 从 >90% 降至 ~3%/2%，StrongREJECT 降至 12%
2. **Cover story（欺骗性提示）**：64%。告诉模型"你是自主红队 agent 在做演习"
3. **Thinking-token 预填充**：92%。预填充模型 thinking tokens 使其看起来已考虑并决定继续

**对照**：全部路径对受护栏的 Claude API 均失败——权重不公开（不可 abliterate）、API 无 thinking 预填充入口、护栏拦截 cover story。

## 关键方法论点

- **Abliteration 后能力保留验证**：GPQA-Diamond 分数不变（通用能力无损），CyberGym 子集仅降几个百分点——安全移除≠能力下降，风险不能指望"破坏功能"来缓解
- **成本量化**：开放权重的护栏本质上是"防君子"层——一次性 $4,400 成本即可为所有攻击者永久解除
- **N-day 复现测试**：GLM-5.3-Flash 用公开 CVE 详情 20 分钟人类注意力 + 8 小时模型工作 + $20.40 即构造绕过 PAC 的 ARM64 exploit 链
- **评估环境**：隔离沙箱中仅攻击离线靶标；human-in-the-loop 开放式测试用人类专家不知情的漏洞

## 可复用模式

评估任何开放权重模型的真实风险时：
1. 不要信原始拒绝率——先做 abliteration 复现，测 abliterated 版本的能力保留度
2. 三通道测试矩阵：权重修改 / 提示欺骗 / 预填充，分别量化 engage 率
3. 能力基准与安全基准必须同跑（GPQA + CyberGym），确认护栏移除无能力税
4. 发布策略含义：能力达到"能自主开发端到端 exploit"级别的模型，开放权重 = 无护栏；受限发布（vetted users）是唯一保留安全层的途径
