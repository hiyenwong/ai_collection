---
name: grid-fields-place-cells-self-organization
arxiv_id: 1503.07707v2
utility: 0.88
tags: '[grid cells, place cells, hippocampus, entorhinal cortex, synaptic plasticity, BCM rule, self-organization]'
created: 2026-03-31
description: "Grid Fields Place Cells Self-Organization"
---

# Grid Fields Place Cells Self-Organization

## Activation Keywords

- grid cells 自组织
- place cells 空间编码
- 海马体 空间导航
- BCM 突触可塑性规则
- 内嗅皮层 网格模式
- 六边形空间场

## Problem Statement

理解大脑如何编码空间信息是一个核心问题：
- Grid cells（网格细胞）如何形成六边形空间场？
- Place cells（位置细胞）如何指导网格细胞发育？
- 突触可塑性如何驱动空间编码网络的自组织？

## Method Overview

Stepanyuk (2015) 提出了一个基于突触可塑性的网格场自组织模型：
1. Place cells 提供空间信息输入
2. BCM 规则驱动联想可塑性
3. Homeostatic 规则限制权重范围
4. 六边形网格场快速涌现

## Tools Used

- `Plasticity Rule` - Analysis component
- `BCM Rule` - Analysis component
- `Homeostatic` - Analysis component
- `PCA-like extraction` - Analysis component

## Neural Architecture

```
Place Cells (Hippocampus) → Synaptic Plasticity → Grid Cells (MEC)
         ↑                                         ↓
    Spatial Input                         Hexagonal Fields
```

## Step-by-Step Instructions

### 网格场自组织模型实现

1. **初始化 Place Cells 网络**
   - 定义空间环境边界
   - Place cells 随机位置响应
   - 输出：空间激活向量

2. **配置 BCM 可塑性规则**
   ```python
   # BCM-like plasticity
   dw = eta * (r * (r - theta) * x)  # r: postsynaptic, x: presynaptic
   theta = theta_avg * r^2  # sliding threshold
   ```

3. **添加 Homeostatic 约束**
   - 权重上限
   - 权重下限
   - 总权重归一化

4. **模拟导航学习**
   - 短时间导航体验
   - 六边形场快速形成
   - 测试空间选择性

## Key Insights

| 特性 | 传统模型 | 本模型 |
|------|---------|--------|
| 学习速度 | 长时间训练 | 短时间导航即可 |
| 可塑性类型 | 复杂规则 | BCM + Homeostatic |
| 生物合理性 | 低 | 高 |
| Place Cell 依赖 | 不明确 | 明确监督作用 |

## Example Usage

```python
# 简化的网格场自组织模型
import numpy as np

class GridFieldSelfOrganization:
    def __init__(self, n_place_cells=100, n_grid_cells=50):
        self.W = np.random.randn(n_grid_cells, n_place_cells) * 0.1
        self.theta = np.ones(n_grid_cells) * 0.1  # BCM threshold
    
    def bcm_plasticity(self, x, r, eta=0.01):
        """BCM rule: dw = eta * r * (r - theta) * x"""
        return eta * r * (r - self.theta) * x
    
    def homeostatic(self, W, w_min=0, w_max=1):
        """Weight bounds"""
        W = np.clip(W, w_min, w_max)
        return W / np.sum(W, axis=1, keepdims=True)
    
    def learn_navigation(self, place_activity, steps=1000):
        for _ in range(steps):
            r = np.dot(self.W, place_activity)
            self.W += self.bcm_plasticity(place_activity, r)
            self.W = self.homeostatic(self.W)
            self.theta = 0.1 * np.mean(r**2)  # sliding threshold
```

## Description

Grid Fields Place Cells Self-Organization

**Key Concepts:**
- 理解大脑如何编码空间信息是一个核心问题：
- Grid cells（网格细胞）如何形成六边形空间场？
- Place cells（位置细胞）如何指导网格细胞发育？
- 突触可塑性如何驱动空间编码网络的

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 初始化 Place Cells 网络

### Step 2: 配置 BCM 可塑性规则

### Step 3: 添加 Homeostatic 约束

### Step 4: 模拟导航学习

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Grid Fields Place Cells Self-Organization to my analysis.

**Agent:** I'll help you apply grid-fields-place-cells-self-organization. First, let me understand your specific use case...

**Context:** 理解大脑如何编码空间信息是一个核心问题：
- Grid cells（网格细胞）如何形成六边形空间场？
- Place cells（位置细胞）如何指导网格细胞发育

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for grid-fields-place-cells-self-organization?

**Agent:** Let me search for the latest research and best practices...

## References

- Stepanyuk, A. (2015). Self-organization of grid fields under supervision of place cells. arXiv:1503.07707.
- BCM Rule: Bienenstock, Cooper, Munro (1982)

## Related Skills

- synaptic-weight-distributions-plasticity-geometry
- meta-learning-biological-plasticity
- neuromodulated-synaptic-plasticity