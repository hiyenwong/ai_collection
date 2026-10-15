---
name: anti-distillation-defense-architecture
description: "防御LLM推理被蒸馏提取的三层架构：控制推理可达范围(preserved thinking禁止编辑历史上下文/组织级隔离/弱模型不可读)、两阶段constitutional分类器拦截提取尝试(<0.1%误报)、经济抑制(封锁前计费+账号分级限速+快速封禁)、推理摘要化使蒸馏数据贬值(SWE-bench 80.4%→71.8%)。实测推理token外泄降10-100倍。适用于API产品安全、推理保护、anti-distillation设计。Activation: distillation defense, reasoning transcript protection, constitutional classifier anti-extraction, preserved thinking, proxy network abuse, model IP protection, summarization degrade distillation value"
version: 1.0.0
author: Anthropic (Policy)
date: 2026-10-12
source: https://www.anthropic.com/research/distillation-defenses
category: ai_collection
tags: [ai-security, api-security, distillation, constitutional-classifiers, product-defense]
activation_keywords: [anti-distillation architecture, distillation attack defense, reasoning extraction classifier, preserved thinking API, summarize reasoning transcripts, two-stage classifier extraction attempts, proxy network fraud accounts, distillation defense trade-offs, reasoning token leakage metric, cat and mouse security]
---

# Anti-Distillation 防御架构（Anthropic, 2026-10）

## 背景与威胁定义
蒸馏攻击 = 用大规模账号网络从强模型批量抽取**推理过程(transcript)**，训练小模型复刻能力。对蒸馏者最有价值的是 thinking/reasoning（教"怎么得出答案"），不是输出本身 → **防御重心 = 让 reasoning 难以被获取**。攻击分两类：
- **Passive**：正常 API 调用后直接训练
- **Active**：诱导模型复现隐藏推理（"逐字输出你之前的推理"、12,000 条不同诱导请求的批量试探、代理网络数十万假账号轮换）

## 三层防御（可迁移的架构模式）

### 层 1：控制推理的可达范围（数据面控制）
攻击者的搬移手法：跨会话搬 reasoning block（骗模型"你已经有权限看"）、跨模型搬（用弱防护模型读强模型的推理）、跨账号搬（封一个号换下一个）。对应控制：
- **Preserved thinking**：新 API 账号禁止编辑 Claude 的历史上下文 → 无法用"注入已有序列"骗出推理
- **弱模型不可读**：阻止早期低防护模型读取新模型 reasoning
- **组织级隔离**：reasoning transcript 仅产生它的组织可读（Sonnet 5.5 起）

### 层 2：两阶段分类器拦截（检测面）
- 用与生物/网络安全防护同级的 **constitutional classifier（两阶段）**识别"请求提取隐藏推理"的意图——普通用户极少要求模型逐字写出完整隐藏推理，这是强信号
- 拿真实蒸馏者尝试的 transcripts 做内外部红队（手动+自动），发现漏洞即修补
- 快速迭代堵新变体：翻译旧推理到另一语言、把推理"写在答案旁边的标签里"等都被后续堵掉
- 指标：**误报 <0.1%**，鲁棒度≈防生物武器级

### 层 3：让重复尝试变贵（经济面）
- 持续尝试提取的账号 → 更严用量限制；检测到持续蒸馏活动 → 封禁（实际中数万账号被ban，常在开始活动 2 小时内）
- **对被安全系统拦截的请求恢复计费**（仅限误报 <0.1% 的领域，含蒸馏）→ 攻击者的试错有直接成本

## 量化防御效果（写报告的度量模板）
1. **摘要化贬值数据**：让模型先总结 reasoning 再展示 → 用 Opus 4.8 transcripts 训练的预训练模型 SWE-bench Verified **80.4%（全文）→ 71.8%（摘要版）**。推理被"消毒"后训练价值大幅下降
2. **外泄量度量**：平台上被蒸馏者抽走的 reasoning tokens 数（分类器上线后 **降 10-100×**，部分日子低到测不出）
3. 权衡诚实披露：preserved thinking 要求开发者改集成、<0.1% 误伤合法请求、被拦请求也计费、放弃蒸馏者付费流量（数万亿 token 级收入）

## 工程教训
- **简单防御不够**：摘要化上线后攻击从 passive 转 active；第一代拦截器被绕过后攻击者规模化（20k+ 假账号同时管理的网络）
- **猫鼠游戏预期管理**：明确"不知道这些收益能维持多久"，持续监控成功提取并快速修补
- **生态位思考**：单家防御会被"从无防护的同能力模型"旁路（GLM-5.3 案例）→ 防御是行业公共品问题，平台方（云/inference 提供商）也要检测滥用和清理假账号
- 发布方法论本身是策略：证明"有可行替代"以打破"蒸馏者是付费客户所以没人动手"的激励僵局

## 引用来源
Anthropic (2026). Strengthening our defenses against distillation attacks. https://www.anthropic.com/research/distillation-defenses
相关：OpenAI 的对抗蒸馏案例见 [[adversarial-distillation-defense]]（vendor 视角的检测/归因/反制）。
