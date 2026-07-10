---
name: sparse-neural-connectivity-recovery
description: Covariance-based method with Granger-causality refinement for recovering sparse neural connectivity from partial measurements
last_updated: 2026-06-11
paper_id: arXiv:2603.18497
paper_date: 2026-03-19
authors: Quilee Simeon
category: neuroscience
tags: [neuroscience, connectivity-recovery, covariance-method, granger-causality, neural-circuits]
---

# Recovering Sparse Neural Connectivity from Partial Measurements

## Overview

从稀疏、部分测量中恢复神经回路连接性的方法，使用协方差方法结合 Granger 因果精化。

## Problem Statement

神经科学核心挑战：
- 从不完整观察推断神经回路连接性
- 不同 session 观察不同神经元子集
- 无法同时记录所有神经元

## Solution: Covariance-Based Method

### Core Algorithm

**Phase 1: Covariance Accumulation**
- 跨多个 session 累积成对协方差估计
- 从部分观察重建完整连接矩阵

**Phase 2: Granger-Causality Refinement**
- 使用 Granger 因果性施加生物约束
- 投影梯度下降优化

## Key Discovery: Control-Estimation Tradeoff

**控制-估计权衡**：
- 刺激有助于可识别性 → 但破坏内在动力学
- 最优刺激水平取决于测量密度

## Surprising Result: Linear Approximation Advantage

**Stein-Price Identity 关键发现**：
- "错误"的线性近似作为隐式正则化
- 在所有操作条件下优于 oracle estimator
- 隐式正则化避免过拟合

## Practical Applications

- 神经疾病连接异常检测
- 实验设计优化
- 脑机接口连接分析

## Implementation Workflow

1. 数据收集（多 session 电生理）
2. 协方差计算和累积
3. 连接估计（最小二乘）
4. Granger 精化（投影梯度）
5. 验证和不确定性估计

## Activation Triggers

Use this skill when:
- 从部分电生理记录恢复连接矩阵
- 分析跨 session 神经数据
- 设计刺激实验策略

**Keywords**: neural connectivity, partial measurements, covariance method, Granger causality, Stein-Price identity

## References

- Simeon (2026). arXiv:2603.18497