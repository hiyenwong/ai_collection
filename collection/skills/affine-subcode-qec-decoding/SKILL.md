---
name: affine-subcode-qec-decoding
description: 仿射子码集成解码方法论，用于退化感知量子纠错。通过在稳定子码校验矩阵中添加线性无关行扩展搜索空间，结合过完备矩阵实现多路径BP解码，显著提升量子LDPC码收敛性与逻辑错误率表现。
category: quantum
tags: [quantum-error-correction, qldpc, belief-propagation, affine-subcode, degeneracy, ensemble-decoding, toric-code, gb-code]
version: 1.0.0
created: 2026-05-10
freedom: low
---

# Affine Subcode Ensemble Decoding for Degeneracy-Aware Quantum Error Correction

## 概述

量子低密度奇偶校验（QLDPC）码是低开销容错量子计算的有希望候选者，但**简并性（degeneracy）**会严重损害 belief-propagation（BP）解码的收敛性。本方法论将经典仿射子码集成解码技术扩展到量子领域，通过在校验矩阵中添加线性无关行来减少有效简并解的搜索空间。

## 核心原理

### 简并性问题

在量子纠错中，多个不同的错误模式可能对应相同的综合征（syndrome），这称为简并性。传统 BP 解码器在遇到简并错误时会：
1. 产生振荡，无法收敛
2. 选择高权重错误而非低权重逻辑等价错误
3. 逻辑错误率显著高于理论极限

### 仿射子码扩展

通过在稳定子码的校验矩阵 $H$ 中添加线性无关行，构造扩展矩阵 $H'$：

$$H' = \begin{bmatrix} H \\ R \end{bmatrix}$$

其中 $R$ 是与 $H$ 线性无关的额外校验行。这有效地：
- 将原码 $C$ 限制为其子码 $C' \subset C$
- 减少简并错误模式的搜索空间
- 使 BP 解码器更容易找到低权重解

### 过完备矩阵

对每个解码路径使用过完备矩阵（overcomplete matrix），进一步增加冗余度，提高解码成功率。

## 算法流程

### Phase 1: 仿射子码构造

1. **输入**：稳定子码校验矩阵 $H$（$m \times n$）
2. **选择扩展行**：从 $H$ 的零空间中选取 $k$ 个线性无关向量 $\{r_1, ..., r_k\}$
3. **构造扩展矩阵**：$H' = [H^T, r_1^T, ..., r_k^T]^T$
4. **验证**：确保 $H'$ 仍保持低密度特性

### Phase 2: 集成解码

1. **生成多个解码路径**：对每个仿射子码 $C'_i$，构造对应的过完备矩阵
2. **并行 BP 解码**：在每个路径上独立运行 BP 解码器
3. **综合征验证**：检查每个路径的输出是否满足原始综合征约束
4. **选择最优解**：从所有有效解中选择权重最小的错误模式

### Phase 3: 后处理

1. **逻辑等价性检查**：验证所选错误模式是否与真实错误逻辑等价
2. **失败处理**：若所有路径均失败，回退到标准 BP 或 OSD 解码

## 配置参数

| 参数 | 描述 | 默认值 | 范围 |
|------|------|--------|------|
| `num_paths` | 解码路径数量 | 10 | 5-50 |
| `extension_rows` | 每个路径的扩展行数 | 3 | 1-10 |
| `max_iterations` | BP 最大迭代次数 | 100 | 50-500 |
| `convergence_threshold` | 收敛阈值 | 1e-6 | 1e-8 - 1e-4 |

## 适用场景

- **QLDPC 码解码**：Toric codes、Generalized Bicycle codes、Hypergraph Product codes
- **高简并性场景**：错误率接近阈值的容错量子计算
- **低开销需求**：需要保持解码复杂度接近线性的应用

## 性能基准

在 Toric codes 和 Generalized Bicycle codes 上的 Monte-Carlo 模拟表明：
- 收敛率提升 15-30%
- 逻辑错误率降低 1-2 个数量级（在阈值以下区域）
- 解码复杂度增加因子约为 $O(\text{num\_paths})$

## 边界条件与陷阱

- **过完备性损失**：扩展行过多会导致矩阵密度增加，破坏 LDPC 特性
- **路径相关性**：不同解码路径应尽可能独立，否则集成增益有限
- ** syndrome 匹配**：扩展后的解码结果必须映射回原始 syndrome 空间进行验证

## 参考实现

- 论文: https://arxiv.org/abs/2605.06547v1
- 相关工具: `pymatching`, `ldpc` Python 库
