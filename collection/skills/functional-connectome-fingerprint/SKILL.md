---
name: functional-connectome-fingerprint
version: 1.0.0
description: |
  功能性连接组指纹分析方法论。扩展 differential identifiability 框架，
  检测个体指纹梯度和双胞胎指纹梯度。
  触发词：脑指纹、连接组指纹、个体差异、可识别性、fingerprint、
  differential identifiability, connectome fingerprint。
---

# Functional Connectome Fingerprint

## 核心方法论

### 问题定义

**传统方法：** 只关注同一被试不同扫描之间的指纹（test/retest）

**扩展：** 研究指纹梯度 - 基于遗传和环境相似性的指纹差异

---

## 关键概念

### 1. 脑连接指纹

**定义：** 脑功能连接模式的个体特异性

**用途：**
- 评估神经影像数据质量
- 研究个体差异
- 被试识别和匹配

### 2. Differential Identifiability 框架

**核心公式：**

$$I_{diff} = I_{within} - I_{between}$$

其中：
- $I_{within}$：同一被试不同扫描间的相似度
- $I_{between}$：不同被试扫描间的相似度

### 3. 指纹梯度扩展

| 梯度类型 | 定义 | 含义 |
|----------|------|------|
| **Subject Fingerprint** | 同一被试的多个扫描 | 个体特异性 |
| **Twin Fingerprint** | 同卵/异卵双胞胎的扫描 | 遗传贡献 |
| **Gradient** | 指纹强度沿遗传相似度的变化 | 基因vs环境 |

---

## 技术要点

### 数据处理流程

```
1. fMRI 数据预处理
   ↓
2. 功能连接矩阵计算
   ↓
3. 脑图谱分割（Schaefer Atlas）
   ↓
4. 最优重建 FC
   ↓
5. 指纹梯度分析
```

### 关键发现

1. **指纹梯度存在**：遗传相似性越高，指纹相似度越高
2. **最优重建必要**：只有最优重建的 FC 才能揭示高分辨率图谱的指纹
3. **扫描长度效应**：静息态扫描长度和图谱分辨率影响指纹强度

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **数据质量评估** | 通过指纹强度判断数据可靠性 |
| **个体识别** | 被试匹配和去重 |
| **遗传研究** | 量化遗传对脑连接的影响 |
| **纵向研究** | 追踪个体脑连接变化 |

---

## 数据集

**Human Connectome Project - Young Adult (HCP-YA)**

- ~1200 名被试
- 8 个 fMRI 条件
- 多分辨率 Schaefer Atlas
- 包含双胞胎数据

---

## 技术实现

### 功能连接计算

```python
# 计算 FC 矩阵
fc_matrix = compute_functional_connectivity(timeseries, atlas='schaefer')

# 最优重建
fc_reconstructed = optimal_reconstruction(fc_matrix)
```

### 指纹分析

```python
# 计算 differential identifiability
I_diff = compute_differential_identifiability(fc_list, subject_ids)

# 双胞胎指纹分析
twin_fingerprint = analyze_twin_pairs(fc_list, twin_pairs, zygosity)
```

### 梯度检测

```python
# 指纹梯度
gradient = compute_fingerprint_gradient(
    subject_fp,  # 同卵双胞胎
    sibling_fp,  # 异卵双胞胎
    unrelated_fp # 无关被试
)
```

---

## 相关技能

- `time-varying-brain-connectivity` - 时变脑网络分析
- `weighted-brain-community-detection` - 加权脑网络社区检测

---

## 来源

- **论文：** Functional Connectome Fingerprint Gradients in Young Adults
- **arXiv：** 2011.05212
- **效用评分：** 0.91
- **学习日期：** 2026-03-21
## Activation Keywords

- 脑网络分析
- 神经科学方法
- 计算神经科学
- 脑连接建模

## Tools Used

- **read**: Read skill documentation and references
- **exec**: Run analysis scripts and data processing
- **web_fetch**: Fetch papers and resources

## Instructions for Agents

1. Read the skill documentation carefully
2. Understand the methodology and key concepts
3. Apply the techniques to the specific problem
4. Document results and insights

## Examples

```python
# Example usage of the skill methodology
# Refer to the Technical Implementation section for details
```
