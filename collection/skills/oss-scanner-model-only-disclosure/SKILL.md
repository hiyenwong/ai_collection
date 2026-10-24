---
name: oss-scanner-model-only-disclosure
description: "规模化LLM漏洞披露的运营方法论：人工triage是瓶颈(29k候选只审6k)→维护者主动要原始报告→opt-in无人工审阅的model-only披露通道；报告结构=self-contained reproducer+漏洞解释+引入点bisection+候选patch；验证数据：专家抽检97个高危中85个(88%)达CVD标准、11个重复、仅1个假阳性；收录标准借用OSS-Fuzz(critical infrastructure)；维持者实测反馈(curl/wolfSSL 72/74有效5个成CVE/PostgreSQL)。适用于AI安全扫描服务设计、vulnerability disclosure流程、open source安全运营。Activation: OSS Scanner, model-generated vulnerability report, coordinated vulnerability disclosure, unverified findings fast track, reproducer bisection patch, vuln triage bottleneck, opt-in security scanning, LLM false positive rate security"
version: 1.0.0
author: Anthropic (Frontier Red Team)
date: 2026-10-08
source: https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source
category: ai_collection
tags: [ai-security, vulnerability-disclosure, open-source, llm-scanning, cvd]
activation_keywords: [OSS Scanner enrollment, model only vulnerability disclosure, fast track unverified reports, CVD bar validation, 88 percent valid findings, bug report structure reproducer, maintainer feedback loop, OSS-Fuzz eligibility criteria, triage bottleneck human capacity, LLM vulnerability false positive]
---

# OSS Scanner：model-only 漏洞披露的运营设计

## 核心矛盾与解法
LLM 找漏洞能力爆发（CyberSecEval/CyberGym：一年多前 <20% → 今 >85%），但**人工 triage 是瓶颈**：Anthropic 六个月扫出 29,000+ 候选漏洞，人工只验证了 ~6,000。同时维护者反馈变了：早期 LLM 报告是 slop，现在"和人写的一样好甚至更好"，于是**维护者主动要求"把没验证的全给我"**（已直发近 5,000 份）。
解法 = 双通道披露：
1. **人工验证 CVD 通道**（默认，尤其为无力自审的项目）
2. **Opt-in model-only 快车道**：全模型生成、无人工审阅、随产随发、更快更频繁——代价是可能有不正确/无效报告（明确告知）

## 报告结构（model-only 报告的质量契约）
每份报告必须 self-contained：
- **复现器（reproducer）**：可独立运行的漏洞复现
- **漏洞解释**：包括 **bisection 定位引入 commit**（能定位时）
- **候选 patch**（有则附）
运营验证：97 个 critical/high 报告（48 个项目）由 CVD 专家复核 → **85 个 (88%) 达 CVD 门槛；11 个是重复/已知；仅 1 个假阳性**。维护者侧：wolfSSL 74 份里 72 份有效、5 个成 CVE；curl "近年来最严重的漏洞之一"；PostgreSQL 大量可用度 ≥ nearly-as-is 的修复。

## 运营要点
- **错误类型要分开讲**：假阳性极少；但**severity 通胀**和**误解项目威胁模型**是真实存在的抱怨 → 沟通中明确"报告可能不准"并按反馈迭代
- **收录标准沿用 OSS-Fuzz**：对基础设施和用户安全有 critical 影响，逐案决定；**opt-in 机制**(维护者提交 PR 注册)把"未经请求的报告"变成应邀服务，化解合规/伦理争议
- 披露速度成为防御变量："exploits 现在几分钟就能开发"→ 快速收到未验证报告+补丁 > 等人工验证
- 无验证披露的前提是**报告自带可验证性**（reproducer 一跑便知），把验证成本转移给接收方但降到最低
- 配套生态：Cyber Verification Program（给安全专家开放更强能力）、Claude for OSS（免费订阅帮修复）

## 可迁移的设计模式
- 任何"AI 产出 >> 人工审核产能"的领域（代码审查、文献筛选、医疗初筛）都可套用：**分层交付**（人工验证版 + opt-in 原始版）+ **自验证产物**（每份产出附带低成本验证手段）+ **邀请制**（opt-in 明确授权边界）
- 与 [[glasswing-vulnerability-discovery]]（发现方法论）配合：Glasswing 讲怎么找，本 skill 讲找到了怎么规模化交付

## 引用来源
Anthropic (2026). Launching an opt-in vulnerability-finding service for open-source software. https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source
