---
name: ai-intelligence-targeting-weapons-evals
description: "AI军事情报定位与常规武器能力评估方法论：kill chain各环节的模型能力基准——身份关联/分类(模拟社交媒体200任务三难度, F1)、照片地理定位(YFCC100M, 前沿模型中位误差37km超人类最强GeoGuessr选手151km)、文本地理定位(GeoText, 沙箱搜索工具)、无人机打击精度等。发现前沿模型定位能力接近超人类，开放权重模型(Kimi K3)落后一代但仍有令人担忧的能力。适用于AI滥用风险评估、军事情报能力基准设计。Activation: intelligence targeting evaluation, geolocation benchmark, kill chain AI, identity correlation, AI weapons capability, surveillance risk, model misuse assessment"
version: 1.0.0
author: Anthropic Frontier Red Team / Threat Intelligence Team
date: 2026-09-10
source: https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities
category: ai_collection
tags: [ai-misuse, intelligence-targeting, geolocation, kill-chain, capability-evals, national-security]
activation_keywords: [intelligence targeting, geolocation from photos, text geolocation, identity correlation, kill chain, AI weapons evaluation, surveillance misuse, F1 identity linkage, GeoGuessr baseline, synthetic social media corpus]
---

# AI 情报定位与常规武器能力评估

## 框架：Kill-chain 能力评估设计

"Find, fix, track, target, engage, assess" 各环节分别建基准。核心观察：保护人们免受情报定位的不是保密性而是**分析劳动力成本**——AI 把稀缺专家劳动变便宜，就是风险增量。

## 四类评估设计模板

**1. 身份关联与分类（find 环节）**
- 模拟社交媒体语料（WhatsApp/Telegram/Instagram/Facebook 模拟内容），两个虚构场景世界（墨西哥城/加尔各答抗议运动），200 任务三难度档（68 easy/68 medium/64 hard，按账号数与关联证据稀疏度）
- F1 评分（precision/recall 调和平均）
- 发现：Mythos Preview 最强；Kimi K3 在 easy/medium 接近前沿，hard 落后
- 速度：中位样本 37,000 词，人类分析师读 2.5 小时，模型 11 分钟完成评估

**2. 照片地理定位（fix 环节）**
- YFCC100M Flickr 严格 geotagged 子集，按大洲分层，过滤无法定位图像（矢量图/微距），ground truth 对模型隐藏
- 人类基线代理：竞技 GeoGuessr 数据（Champion 玩家中位 151km、Master 174km、Gold 1714km）
- 结果：Mythos Preview/Mythos 5 中位 37.0/47.2 km（23.7%/23.1% 在 1km 内）——**超过最强人类基线**；Opus 5 ≈ Master 级；Kimi K3 385km 但 1km 命中率 16.7%（超 Gold 级）
- 知识截止后图像的 held-out 测试结果分布相似（排除记忆）

**3. 文本地理定位**
- GeoText 语料（9,475 用户 geotagged tweets），把用户"家"定义为发推最大簇中心，句柄/提及/转推全部匿名化
- 给模型沙箱搜索工具；防记忆检验：仅凭假名提问，所有模型都不高于"永远猜纽约"基线（中位 800–2000km vs 677km）

**4. 常规武器开发（engage 环节）**
- 工程化无人机打击移动目标等任务（详见原文）

## 可复用模式

- **"保护的是成本不是数据"分析框架**：评估 AI 滥用风险时问"AI 把哪种稀缺专家劳动变便宜了"
- **ground truth 隐藏 + 人类基线代理**：用竞技游戏数据（GeoGuessr）替代昂贵的人类基线收集
- **记忆混淆检验**：对公开老数据集，用假名/知识截止后数据分离记忆与真实推理
- **难度分层按对抗强度**：hard = 更多噪音 + persona 更好的操作安全（opsec），直接映射现实对手
- **on-platform classifiers**：评估证明能力存在 → 必须配套平台级拦截分类器；开放权重模型落后前沿约一代但能力仍然令人担忧
