---
name: fixed-point-compositionality-low-rank-gluing
description: 固定点组合性低秩胶合理论框架。研究结构模块化如何支持抑制主导阈值线性网络的功能组合性，引入低秩胶合规则实现不动点的组合式分解。
version: 1.0.0
category: computational neuroscience
tags: [neural dynamics, fixed point, compositionality, low-rank, threshold-linear networks, modular networks, attractor dynamics]
activation_keywords: [fixed point, compositionality, low-rank, gluing, threshold-linear, modularity, attractor, compositional dynamics]
authors: ["Juliana Londono Alvarez"]
arxiv_id: "2606.07336"
date_added: "2026-06-09"
---

# Fixed Point Compositionality via Low-Rank Gluing Rules

## Background & Motivation

大脑在相对稳定的结构和有限资源下能产生高度灵活的复杂行为，其核心机制是**组合性**（compositionality）——将复杂任务分解为可重用的简单基元。虽然网络模块化常与组合性联系，但在非线性网络中缺乏严格的数学表征。

**核心问题**：
- 结构模块化如何支持功能组合性？
- 如何在非线性网络中实现组合式动力学？
- 如何构建具有可预测吸引子组合的网络？

## Core Methodology: Low-Rank Gluing Framework

### 1. Threshold-Linear Networks (TLNs)

阈值线性网络是研究抑制主导电路的标准模型：

**动力学方程**：
$$
\dot{x}_i = -x_i + \left[\sum_{j=1}^n W_{ij}x_j + b_i\right]^+
$$

其中：
- $x_i$：神经元活动
- $W_{ij}$：连接权重（抑制主导）
- $b_i$：外部输入
- $[\cdot]^+$：阈值线性函数 $\max(\cdot, 0)$

**关键性质**：
- 抑制主导保证不动点的存在性
- 支持多个稳定吸引子
- 连接性与动力学有明确对应

### 2. Modular Network Assembly: Low-Rank Gluing

**定义**：将多个子网络通过特定的低秩耦合连接：

$$
W = \begin{pmatrix}
W_1 & L_{12} \\
L_{21} & W_2
\end{pmatrix}
$$

其中：
- $W_1, W_2$：子网络内部连接（任意）
- $L_{12}, L_{21}$：**低秩胶合矩阵**（rank $\leq k$）

**核心定理**：全局不动点受限于局部不动点的组合

$$
\text{Fixed}(W) \subseteq \text{comb}(\text{Fixed}(W_1), \text{Fixed}(W_2))
$$

### 3. Rank-1 Gluing: Complete Characterization

对于秩-1胶合，提供完整刻画：

**胶合条件**：
$$
L_{12} = u_1 v_2^T, \quad L_{21} = u_2 v_1^T
$$

**组合规则**：
1. 识别局部不动点：$(x_1^*, b_1^*)$ 和 $(x_2^*, b_2^*)$
2. 验证组合可行性条件
3. 计算全局不动点：$x^* = (x_1^*, x_2^*)$

**可预测性**：通过局部模块的不动点组合，预测全局网络的吸引子库。

### 4. Generalized Combinatorial TLNs (gCTLNs)

扩展固定点分解规则：

**CTLN → gCTLN**：
- CTLN：基于图的组合式阈值线性网络
- gCTLN：更灵活的连接模式

**定理**：固定点分解规则在gCTLN中仍然成立，结构规则比原假设更稳健。

## Key Results

### 1. Mathematical Rigor

- **定理1**：低秩胶合的约束性组合
- **定理2**：秩-1胶合的完整刻画
- **定理3**：gCTLN的固定点分解

### 2. Combinatorial Attractor Repertoire

组合式动力学使网络具有：
- 组合式大量的可预测吸引子
- 从简单组件基元理解复杂动力学
- 支持固定点组合和组合式极限环

### 3. Engineering Compositionality

低秩胶合提供：
- 数学可操作的组合式动力学构建方法
- 可预测的吸引子工程
- 从组件基元组合全局动力学

## Applications

### 1. Neural Circuit Design

构建具有可预测多稳态的抑制主导电路：
- 记忆存储网络
- 决策电路
- 感觉表征组合

### 2. Compositional Dynamics

理解大脑如何组合：
- 简单行为基元 → 复杂行为序列
- 局部表征 → 全局表征
- 模块功能 → 整体功能

### 3. Network Architecture

设计组合式神经网络架构：
- 模块化约束
- 低秩连接
- 可预测动力学

## Implementation Guide

### Step 1: Identify Component Modules

```python
# 定义子网络
W1 = define_subnetwork(n1, internal_connectivity)
W2 = define_subnetwork(n2, internal_connectivity)

# 计算局部不动点
fixed_points_1 = compute_fixed_points(W1, b1)
fixed_points_2 = compute_fixed_points(W2, b2)
```

### Step 2: Design Low-Rank Gluing

```python
# 秩-1胶合设计
L12 = np.outer(u1, v2)  # rank-1 coupling
L21 = np.outer(u2, v1)

# 组装全局网络
W_global = assemble_network(W1, W2, L12, L21)
```

### Step 3: Verify Compositional Fixed Points

```python
# 验证组合可行性
combinations = enumerate_combinations(fixed_points_1, fixed_points_2)
valid_combinations = verify_gluing_conditions(combinations, L12, L21)

# 计算全局不动点
global_fixed_points = compute_global_fixed(W_global, valid_combinations)
```

### Step 4: Analyze Dynamics

```python
# 模拟动力学
trajectory = simulate_TLN(W_global, b_global, x0)

# 分析吸引子结构
attractors = classify_attractors(global_fixed_points)
```

## Pitfalls & Considerations

### 1. Inhibition Dominance Requirement

- TLN理论要求抑制主导
- 低秩胶合依赖不动点存在性
- 检查网络参数约束

### 2. Rank Selection

- 秩过高 → 组合约束失效
- 秩过低 → 限制组合能力
- 秩-1提供完整刻画但最受限

### 3. Combinatorial Explosion

- 组合式吸引子库指数增长
- 需要验证所有组合
- 考虑计算效率

### 4. Stability vs Compositionality

- 组合可行性 ≠ 稳定性
- 需额外验证Lyapunov稳定性
- 不动点组合可能不稳定

## Related Work

- **Combinatorial Threshold Linear Networks (CTLNs)** - 曲线图基础的网络
- **Low-Rank RNN Theory** - 低秩递归网络动力学
- **Modular Networks** - 网络模块化理论
- **Attractor Dynamics** - 神经网络吸引子动力学

## Experimental Validation

### Test Scenarios

1. **Two-Module Composition**
   - 每个模块：2-3个不动点
   - 验证组合：4-9个全局不动点

2. **Multi-Module Networks**
   - 3-4个模块
   - 组合式吸引子库增长

3. **Compositional Limit Cycles**
   - 固定点组合 → 极限环组合
   - 周期轨道的组合式结构

## Key References

- arXiv:2606.07336 - 论文原文
- Curto et al. (2019) - CTLN理论基础
- Morrison et al. (2016) - 低秩RNN动力学
- Seung (1996) - 抑制主导网络吸引子

## Summary

低秩胶合理论框架为神经网络的组合性动力学提供了严格的数学基础：

**核心贡献**：
1. 证明结构模块化 → 功能组合性的数学联系
2. 提供组合式吸引子的可预测工程方法
3. 扩展CTLN固定点分解规则到gCTLN

**关键洞察**：
- 组合性源于低秩耦合的约束性
- 全局动力学可从局部基元组合理解
- 简单连接规则 → 组合式复杂动力学

**意义**：为理解大脑如何在稳定结构上产生灵活行为，以及设计组合式神经网络架构提供了理论基础。