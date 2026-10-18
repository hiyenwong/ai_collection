---
name: evidence-drift-principled-stopping
description: "发表偏置下检索越深假阳性越高(DACG-agent双层停止:KL收敛+PRM下降检测)"
version: 1.0.0
author: Fred Sun, Shangqi Guo (Tsinghua). arXiv:2609.24101
date: 2026-10-18
source: https://arxiv.org/abs/2609.24101
category: ai_collection
tags: [publication-bias, retrieval-stopping, causal-inference, evidence-synthesis, rag, reliability]
activation_keywords: [publication bias correction, evidence drift, retrieval stopping criterion, biomedical evidence synthesis, KL divergence posterior convergence, Bradley-Terry process reward model, noisy-OR aggregation, null effect false positive, retrieval budget, meta-analysis automation]
---

# Evidence Drift 与检索的原则性停止

## 适用场景（When to Use）
- 自动化文献综合/证据合成系统（PubMed/Cochrane 检索 agent）
- 迭代式 RAG 检索何时停止的决策设计
- 任何"检索越深越好"假设的审查——尤其是语料有系统性偏置（发表偏置）时
- 从文献构建因果知识图谱（causal KG）的 pipeline

## 核心发现
**检索更深可能更糟**：生物医学文献系统性偏向阳性结果。在标准发表偏置模型下，真效应为 null 的查询的假阳性概率随检索深度 d 严格递增，大样本包络趋于 1（Theorem 1，evidence drift）。

实证（140 个 Cochrane 衍生查询）：假阳性率随预算从 3→20 步单调从 7.9%→15.7%，且集中在 null-effect 类。零样本 LLM 继承预训练偏置（NoEffect 准确率仅 42.9%）；标准 RAG 注入偏置文档后降至 31.4%。

## 方法：DACG-agent 双层停止策略

### 架构
从 PubMed 摘要增量构建因果知识图谱 → noisy-OR 聚合后验 → 停止决策。

### 层 1（准确层）：KL 散度收敛监控
- 监控标签后验的 KL(new||old)：KL → 0 即后验收敛，继续检索不再改变信念
- 检测的是"证据已饱和"（Proposition 1）

### 层 2（效率层）：Bradley–Terry 过程奖励模型（PRM）在线下降检测
- PRM 对每步检索的证据质量打分；检测到质量峰值后下降即停
- 检测的是"证据质量已过峰"（Theorem 2）

### 两层互补
KL 层保证准确（防过早停）；PRM 层保证效率（防过晚停）。

### 结果
- 证据漂移 15.7%→6.4%；null-effect 准确率 +21pp（40.0%→61.4%）；检索步数省 67%；总体 61.4%→69.3%
- 模拟确认漂移结论从投票计数聚合器迁移到部署的 noisy-OR

## 可迁移原则
1. **检索深度不是免费午餐**：语料有偏时，"多证据"=偏置积累。先审计语料偏置结构再定检索预算
2. **后验收敛（KL 监控）是通用的停止信号**：可移植到任何迭代检索 agent（网页搜索、KG 查询、工具调用）
3. **质量峰值检测（PRM 下降）是第二停止信号**：对"新证据质量递减"敏感，KL 只看分布稳定
4. **停止策略要与聚合器联合设计**：漂移结论依赖聚合器（投票计数/noisy-OR），换聚合器要重验证
5. **与 Hermes cron 的直接关联**：本 hourly 研究 pipeline 也从 arXiv 检索论文——检索深度默认封顶（max_results=20）是对的，不要盲目加大

## 与相关 skill 的关系
- [[dkgi-knowledge-graphs-as-files]]：访问侧（怎么取证据）；本 skill 是预算侧（取多少就停）
- [[availability-contract-earnings-nlp]]：label-clock 有效性审计同类精神——审计聚合层而非只看下游指标

## 引用
Sun, F., Guo, S. (2026). When More Evidence Hurts: Publication-Bias Drift and Principled Stopping for Biomedical Causal Search. arXiv:2609.24101
