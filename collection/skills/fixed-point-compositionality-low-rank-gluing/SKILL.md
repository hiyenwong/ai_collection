---
name: fixed-point-compositionality-low-rank-gluing
description: Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks — mathematical framework for compositional dynamics
version: 1.0.0
category: neuroscience
activation_keywords:
  - compositionality
  - fixed point
  - low-rank gluing
  - threshold-linear network
  - TLN
  - inhibition-dominated
  - neural network modularity
  - attractor dynamics
  - compositional dynamics
  - gCTLN
  - combinatorial threshold-linear network
tags:
  - computational neuroscience
  - neural dynamics
  - network modularity
  - fixed points
  - attractors
  - compositional computation
  - threshold-linear networks
  - mathematical framework
authors:
  - Juliana Londono Alvarez
arxiv_id: 2606.07336
date_added: 2026-06-08
source: arXiv q-bio.NC
---

# Fixed Point Compositionality via Low-Rank Gluing Rules

## Core Concept

组合性计算框架 - 揭示结构模块化如何支持功能组合性。通过低秩粘合规则,证明抑制主导阈值线性网络(TLN)的全局固定点可分解为局部模块固定点的组合。

**核心贡献**:
- **低秩粘合(Low-Rank Gluings)**: 新型模块化网络组装方法,组件子网络通过特定低秩耦合连接
- **固定点分解定理**: 全局固定点约束为局部固定点的组合
- **Rank-1粘合完整刻画**: 完全确定哪些局部固定点组合产生全局固定点
- **gCTLN扩展**: 将固定点分解规则从CTLN扩展到广义CTLN

## Mathematical Framework

### Threshold-Linear Networks (TLN)
抑制主导网络动力学:
```
dx_i/dt = -x_i + [∑_j W_ij * σ(x_j - T_j) + b_i]_+
```

### Low-Rank Gluing Assembly
模块连接规则:
- **组件模块**: 任意内部连接子网络
- **低秩耦合**: 通过特定低秩矩阵连接模块
- **组合性约束**: 全局固定点必须是局部固定点的组合

### Fixed Point Decomposition
关键定理:
1. **约束定理**: 全局固定点受限于局部固定点组合
2. **Rank-1粘合**: 完全刻画组合性条件
3. **组合性极限环**: 不仅固定点,极限环也具有组合性

## Key Insights

### Compositionality Mechanism
大脑组合性机制的数学基础:
- **结构模块化** → **功能组合性**
- **简单基元** → **复杂行为**
- **可预测吸引子** → **组合性大容量**

### Engineering Compositional Dynamics
构建组合性网络的配方:
1. 定义局部模块及其固定点
2. 使用低秩粘合规则连接
3. 预测全局固定点为局部组合
4. 扩展到组合性极限环

## Applications

### Computational Neuroscience
- **大脑模块化**: 解释结构-功能关系
- **组合性行为**: 灵活复杂行为的数学基础
- **资源高效**: 有限结构实现大容量行为库

### Neural Network Design
- **可预测吸引子**: 组合性大容量吸引子库
- **模块化架构**: 可工程化的组合性网络
- **动力学工程**: 构建特定动力学模式

### Extensions
- **gCTLN**: 广义组合性阈值线性网络
- **极限环**: 组合性周期动力学
- **复杂网络**: 从简单基元构建复杂动力学

## Technical Details

### Fixed Point Computation
组合性固定点计算:
1. 计算每个模块的局部固定点
2. 确定粘合规则约束的组合集合
3. 验证全局固定点存在性
4. 扩展到动力学轨迹

### Network Assembly
网络构建步骤:
```python
# 定义局部模块
module_A = define_module(connectivity_A)
module_B = define_module(connectivity_B)

# 低秩粘合
gluing_matrix = construct_low_rank_coupling(rank=1)

# 组合网络
network = assemble_modules([module_A, module_B], gluing_matrix)

# 预测固定点
global_fps = compose_fixed_points(module_A.fps, module_B.fps, gluing_matrix)
```

## Critical Analysis

### Strengths
- **严谨数学**: 完整的理论证明
- **工程化方法**: 可预测的网络构建
- **组合性扩展**: 从固定点到极限环
- **生物学启示**: 解释大脑组合性机制

### Limitations
- **抑制主导约束**: 限于特定网络类型
- **低秩假设**: 可能限制耦合灵活性
- **固定点聚焦**: 相变和动力学轨迹需进一步研究

### Future Directions
- **时变模块**: 动态组合性
- **学习规则**: 如何学习粘合规则
- **生物学验证**: 在真实神经网络中验证
- **认知任务**: 应用到具体认知行为建模

## Research Questions

1. **学习机制**: 如何通过学习获得低秩粘合规则?
2. **动力学扩展**: 组合性如何扩展到非固定点动力学?
3. **生物学对应**: 大脑中的低秩粘合是什么?
4. **容量极限**: 组合性容量与网络规模关系?
5. **噪声鲁棒性**: 组合性对噪声的敏感性?

## Implementation Notes

### When to Use
- 构建组合性神经网络
- 设计可预测吸引子动力学
- 解释模块化功能组合性
- 理解大脑组合性机制

### Key Parameters
- **低秩rank**: 粘合矩阵秩数(通常1)
- **模块数量**: 组合容量基元数
- **抑制强度**: 抑制主导程度
- **阈值参数**: TLN阈值设置

### Expected Results
- 可预测的固定点组合
- 组合性大容量吸引子库
- 灵活的动力学模式生成
- 简单基元的复杂组合

## Related Work

- **CTLN**: 组合性阈值线性网络基础
- **吸引子网络**: 固定点和极限环理论
- **网络模块化**: 结构-功能关系研究
- **组合性认知**: 认知科学组合性理论

## Reference

- arXiv:2606.07336 - "Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks"
- Author: Juliana Londono Alvarez
- Submitted: 2026-06-05
- Category: q-bio.NC (Neurons and Cognition)