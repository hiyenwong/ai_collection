---
name: multispectral-sky-inpainting-agentic
description: "用agent团队构建跨仪器科学数据产品的方法论：多UV巡天数据(GALEX/Swift/FIMS等)内部一致性校准(逐观测去大气辉光/亮星glare)→跨仪器交叉定标统一分辨率坐标系→跨波长迁移学习inpainting(用可见/红外/射电学UV亮度关系，填1/3未观测天区)→掩膜自验证(hidden-patch holdout达~10%误差)→Gaia 1亿恒星叠加。人只做高层指令和'发现图上圆盘伪影'式纠错，agent并行数小时计算。适用于多仪器数据融合、缺失数据补全、科学数据产品backlog项目。Activation: multi-instrument data fusion, cross-calibration pipeline, wavelength transfer inpainting, holdout self-validation, agentic science data product, GALEX UV map, agent-orchestrated calibration"
version: 1.0.0
author: Brice Ménard (Johns Hopkins / Anthropic)
date: 2026-10-08
source: https://www.anthropic.com/research/the-missing-map-of-the-sky
category: ai_collection
tags: [agentic-science, data-fusion, inpainting, cross-calibration, multi-agent-pipeline]
activation_keywords: [multi survey data fusion, cross calibration astrophysics, inpainting missing sky coverage, transfer learning wavelength relation, mask validation holdout, agentic data pipeline orchestration, bright star glare removal, atmospheric glow calibration, Claude Science data product, backlog project automation]
---

# 跨仪器数据融合 + 修复补全（agentic 科学数据产品方法论）

## 项目模板：把"没人有空做的 backlog 数据产品"做成成品
科学界普遍存在"关键但低优先级"的数据产品（能讲清概念、帮同行，但永远排不上日程——因为像素级定标+反复分析要数周人工）。本案例证明：**高层指令 + agent 编排 + 专家只做 steering** 可以一夏完成（完整 UV 全天图）。

## 五步流水线（多源数据融合的通用骨架）
1. **搜集**：agent 团队联网检索所有公开巡天（GALEX 38,000 次观测、Swift、FIMS/SPEAR、TD-1…）
2. **单巡天内部一致化**：同一仪器不同时期/条件可比——重点处理亮星 glare（如同地面上的太阳/路灯眩光）逐区域并行抹平
3. **跨仪器交叉定标**：不同望远镜捕获的"UV 天空"略有不同 → 互相交叉定标、重采样到同一分辨率、映射到公共坐标系后合并
4. **跨波长迁移学习 inpainting（核心创新）**：~1/3 天区无 UV 数据。利用**已有 UV 的 2/3 天区**学习 UV 亮度与可见光/红外/射电的关系，把该关系应用到无 UV 天区，逐点估计+置信度（图像修复思路：模型从百万图像学到局部与整体的关系，补缺失部分）
5. **叠加离散源**：在弥散背景上叠加 Gaia DR3 推断的 1 亿+ 恒星 UV 贡献

## 掩膜自验证（无 ground truth 时的精度评估模板）
取**已有 UV 数据的区域，人为挖空一部分**，制造 inpainting 设计要填补的空白 → 模型不得接触真值补全 → 与真值比对。迭代数轮后**误差 ~10%**，肉眼不可辨。这把"预测可信吗"变成可测的实验。

## 人机分工节奏（agentic 项目的协作模板）
- 专家给**高层指令**（"gather → 统一尺度 → 合并 → 填空"），不写像素级细节
- Claude 派 agent 团队并行（不同天区同时处理）
- 节奏：几轮对话规划 → Claude 独立跑数小时计算 → 专家做别的 → 十几个版本迭代
- **专家的真正贡献 = steering + 肉眼发现系统性伪影**：例——傍晚看图发现最暗场里相邻圆斑明暗不一（GALEX 单次观测的圆形footprint，大气残余辉光未除净）。关键教训：该问题 Claude 开工时已列为已知问题，但**两轮 agent 互审都没抓住**；专家一句"我能看到观测盘印子，能修吗"→ agent 定位到大气辉光 → 全部 38,000 次观测重定标 → 伪影消失
- 产品须带**逐像素 provenance**：每个像素标注 "measured" 或 "predicted" + 不确定度估计

## 可迁移要点
- 每个数据产品附 per-pixel 来源与置信度层（"measured/predicted"），透明度是教育/科研复用的关键
- Agent 并行化天然适配"分区域独立处理"类任务（校准、去伪影）
- 数据流图把"确定性步骤"(蓝)与"统计学习组件"(紫)分开画——审阅者一眼看出哪些环节需要验证
- 跨波长关系替代缺失波段的观测 = 任何"某模态缺失、多模态冗余"问题的通用解法

## 引用来源
Ménard, B. (2026). The missing map of the sky. Anthropic Science. https://www.anthropic.com/research/the-missing-map-of-the-sky
数据：NASA GALEX GR6/7、Swift-UVOT、FIMS/SPEAR (KASI)、TD-1、ESA Gaia DR3、Planck & Ha templates。
