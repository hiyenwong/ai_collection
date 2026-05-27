---
name: srf-similarity-representation-factorization
description: "Similarity-Based Representation Factorization (SRF) - 从相似性矩阵恢复低维、非负、可解释嵌入的通用计算方法。适用于神经、行为和计算数据的表征分析，支持稀疏采样和不完整数据，提供更高的假设检验效力。"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.26921"
  published: "2026-05-26"
  authors: "Florian P. Mahner, Ka Chun Lam, Francisco Pereira, Martin N. Hebart"
  tags: [neuroscience, representation-analysis, factorization, similarity-matrix, interpretability, neural-data, behavioral-data]
---

# SRF: Similarity-Based Representation Factorization

## 方法概述

SRF (Similarity-Based Representation Factorization) 是一种通用计算方法，用于从测量数据的相似性矩阵中恢复低维、非负、可解释的嵌入表征。

## 核心优势

### 相比传统方法的改进

现有表征研究方法（通过刺激相似性比较）局限性：
- 对塑造表征的维度访问有限
- 可解释性受限

SRF 解决方案：
- 恢复可解释的维度
- 支持稀疏采样、不完整数据
- 提供更高假设检验效力

## 技术原理

### 相似性矩阵分解

从相关性矩阵 $S$ 恢复低维嵌入 $W$：

$$W = f(S, constraints)$$

约束条件：
- **非负性**：$W \geq 0$（提高可解释性）
- **低维度**：$dim(W) << dim(S)$（简化分析）
- **可解释性**：维度对应具体特征或概念

### 数据兼容性

SRF 支持多种数据类型：
1. **神经数据**：fMRI、EEG、神经影像相似性
2. **行为数据**：心理测量、决策相似性
3. **计算数据**：AI模型表征相似性

## 应用场景

### 仿真验证

- 从各种形式的表征数据中恢复可解释维度
- 即使数据稀疏采样或不完整也能有效

### 神经数据分析

**验证成果**：
- 从神经数据恢复的维度与任务特定模型匹配
- 预测独立行为属性

### 行为与计算研究

**改进探索性分析**：
- 揭示隐藏在相似性矩阵背后的维度
- 提高假设检验效力

## 使用流程

### 步骤 1: 构建相似性矩阵

从原始数据计算刺激或条件间的相似性：

```python
# 示例：神经活动相似性
S = compute_similarity_matrix(neural_activations)
```

### 步骤 2: 执行 SRF 分解

应用 SRF 方法提取维度：

```python
# 非负低维嵌入
W = srf_factorize(S, n_dimensions=5, nonnegative=True)
```

### 步骤 3: 解释维度

分析每个维度的含义：

```python
# 维度解释
for i in range(n_dimensions):
    interpret_dimension(W[:, i], stimulus_labels)
```

### 步骤 4: 假设检验

使用恢复的维度进行统计检验：

```python
# 比较相似性矩阵的假设检验效力
test_power = compare_power(SRF_dimensions, similarity_matrix_comparison)
```

## 实验验证结果

### 模拟数据

- 稀疏采样数据恢复准确率高
- 不完整数据容忍性好

### 神经数据

- 维度与任务特定模型一致
- 预测独立行为测量

### 行为数据

- 提高探索性分析质量
- 增强假设检验统计效力

## 关键贡献

1. **通用性**：适用于神经、行为、计算数据
2. **可解释性**：非负约束确保维度语义清晰
3. **鲁棒性**：稀疏和不完整数据下仍有效
4. **统计效力**：相比直接比较相似性矩阵，假设检验效力更高
5. **跨域应用**：神经科学、心理学、AI表征研究

## 与相关方法的对比

| 方法 | 可解释性 | 稀疏数据支持 | 假设检验效力 |
|------|---------|------------|------------|
| RSA | 低 | 有限 | 中 |
| PCA | 中 | 好 | 中 |
| SRF | 高 | 好 | 高 |

## 实践建议

### 维数选择

- 从 3-10 个维度开始探索
- 根据可解释性和预测能力调整

### 数据预处理

- 相似性计算标准化
- 处理缺失数据（SRF 支持不完整矩阵）

### 结果验证

1. 与任务特定模型对比
2. 预测独立行为属性
3. 统计显著性检验

## Activation Keywords

- similarity-based representation factorization
- SRF method
- representation dimensionality
- neural representation analysis
- interpretability embeddings
- similarity matrix factorization
- behavioral data analysis
- computational representation

## 参考文献

arXiv:2605.26921 [cs.CV, q-bio.NC] - Submitted 26 May 2026