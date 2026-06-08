---
name: fixed-point-compositionality-low-rank-gluing
description: Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks — mathematical framework proving structural modularity supports functional compositionality in neural networks
version: 1.0.0
author: Juliana Londono Alvarez (arXiv:2606.07336)
created: 2026-06-08
source: https://arxiv.org/abs/2606.07336
category: computational neuroscience
tags: [neural dynamics, compositionality, threshold-linear networks, fixed points, modular networks, low-rank coupling, inhibition-dominated, attractors]
activation_keywords: [compositionality, fixed point, low-rank, threshold-linear network, TLN, modular network, gluing rules, attractor dynamics, neural circuit]
readiness_status: available
---

# Fixed Point Compositionality via Low-Rank Gluing Rules

**来源论文**: arXiv:2606.07336 (2026-06-05)  
**作者**: Juliana Londono Alvarez  
**领域**: Neurons and Cognition (q-bio.NC)  

## 核心创新

本文首次提供了结构模块化支持功能组合性的严格数学表征，在抑制主导的阈值线性网络（TLNs）中引入**低秩粘合规则（low-rank gluings）**这一新型模块化网络组装方式，证明全局不动点受限于其组成模块局部不动点的组合。

## 核心方法论

### 1. 低秩粘合规则 (Low-Rank Gluings)

**定义**: 将具有任意内部连接的组件子网络通过特定的低秩耦合连接起来。

**关键性质**:
- 全局不动点必须是其组成模块局部不动点的组合
- 对于更结构化的 **rank-1 gluings**，提供完整表征：确定哪些局部不动点组合产生全局不动点

**数学框架**:
```
全局不动点 ⊆ {组合 | 组合 = Σ(局部不动点_i)}
```

### 2. 从 CTLNs 到 gCTLNs 的扩展

将组合性阈值线性网络（CTLNs）的固定点分解规则扩展到更灵活的 **广义CTLNs (gCTLNs)**，证明这些结构规则比最初假设的更鲁棒。

### 3. 组合性动力学的工程配方

低秩粘合规则提供了数学可追踪的组合性动力学工程方法：
- 可构建具有组合大量可预测吸引子库的网络
- 这些吸引子可从更简单的组件基元理解
- 范围从不动点组合到组合性极限环

## 理论意义

### 组合性的数学基础

1. **结构-功能映射**: 证明模块化结构如何支持组合性行为
2. **可复用基元**: 简化组件模块可组合产生复杂全局动力学
3. **可预测性**: 全局吸引子可通过局部模块行为预测

### 抑制主导网络的优势

- 抑制主导的TLNs天然支持稳定不动点
- 低秩耦合保持组合性约束
- 灵活性与稳定性的平衡

## 实践应用

### 神经网络设计

**场景**: 构建具有组合性动力学的神经网络
**方法**:
1. 设计局部模块的内部连接（任意拓扑）
2. 应用低秩粘合规则连接模块
3. 验证全局不动点分解

**优势**:
- 组合大量可预测吸引子
- 可从简单基元理解复杂动力学
- 数学可追踪的设计流程

### 脑科学建模

**应用场景**:
- 研究大脑如何高效分解复杂任务为可复用基元
- 理解结构模块化与功能组合性的关系
- 分析抑制主导脑区（如基底节）的动力学

**验证方法**:
- 识别脑网络的模块化结构
- 检验低秩耦合假设
- 分析局部不动点组合对应的全局动力学

## 技术要点

### 关键定理

1. **组合性约束定理**: 低秩粘合网络的全局不动点受限于局部不动点组合
2. **Rank-1 表征定理**: 对于rank-1 gluings，完整确定有效组合
3. **gCTLN 扩展定理**: CTLN分解规则扩展到更灵活的gCTLNs

### 数学工具

- **阈值线性网络 (TLN)**: `dx/dt = -x + [Wy + b]_+`
- **低秩矩阵**: 用秩约束限制模块间耦合复杂性
- **不动点稳定性**: Lyapunov方法分析吸引子稳定性

### 实验验证

**网络构建示例**:
1. 定义局部模块（如简单的吸引子网络）
2. 设计低秩耦合矩阵
3. 计算全局不动点并验证分解规则
4. 测试组合性极限环的存在

## 与相关工作的对比

| 方法 | 组合性保证 | 网络灵活性 | 数学可追踪性 |
|------|----------|-----------|------------|
| 低秩粘合规则 | ✓ 严格证明 | ✓ 任意内部连接 | ✓ 完全可追踪 |
| 传统CTLNs | ✓ 组合规则 | ✗ 有限拓扑 | ✓ 可追踪 |
| 非线性RNN | ✗ 无保证 | ✓ 高度灵活 | ✗ 难追踪 |

## 局限性与未来方向

### 当前局限

1. **网络类型限制**: 仅适用于阈值线性网络
2. **抑制主导假设**: 需要网络处于抑制主导状态
3. **计算复杂性**: 大规模网络的固定点计算可能困难

### 未来扩展

- 扩展到更一般的非线性网络
- 研究动态耦合（时变低秩）
- 应用到实际脑网络数据
- 结合学习机制训练粘合规则

## 论文贡献总结

| 贡献 | 创新性 | 影响 |
|------|-------|------|
| 低秩粘合规则定义 | ★★★★★ | 提供组合性网络设计新范式 |
| 组合性数学证明 | ★★★★★ | 首次严格证明结构-功能组合性映射 |
| gCTLN扩展 | ★★★★ | 扩展CTLN理论的适用范围 |
| 工程配方 | ★★★★ | 实用的组合性动力学构建方法 |

## 参考文献

- arXiv:2606.07336 - 原始论文
- CTLN相关文献（待补充）
- 模块化神经网络综述（待补充）

---

## Skill Metadata

- **Activation**: compositionality, fixed point, low-rank, TLN, modular network
- **Use Case**: Design compositional neural networks, analyze brain network modularity
- **Prerequisites**: Understanding of threshold-linear networks, fixed point analysis
- **Output**: Mathematical framework for compositional dynamics engineering