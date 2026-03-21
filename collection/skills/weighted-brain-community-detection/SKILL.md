---
name: weighted-brain-community-detection
version: 1.0.0
description: |
  加权脑网络社区检测方法论，突破分辨率限制。
  使用 Asymptotical Surprise 检测多尺度功能模块。
  触发词：脑网络、社区检测、模块化、分辨率限制、Surprise、
  community detection, weighted network, brain connectivity, modular organization。
---

# Weighted Brain Community Detection

## 核心方法论

### 问题定义

**挑战：** 传统图论方法存在分辨率限制，无法检测小于特定尺度的模块。

**解决方案：** Asymptotical Surprise - 连续版本的 Surprise 函数

---

## 关键概念

### 1. 分辨率限制问题

传统社区检测方法（如 Modularity）存在固有局限：
- 无法检测过小的模块
- 依赖于预设的尺度参数
- 可能遗漏重要的脑功能组织

### 2. Surprise 方法

**原理：** 基于离散概率论的分辨率无关函数

$$S = -\log P(M | p)$$

其中 $M$ 是观察到的模块结构，$p$ 是零假设下的连接概率。

### 3. Asymptotical Surprise

**扩展：** 连续版本，支持加权网络

**优势：**
- 检测任意尺度的模块
- 处理连续连接强度分布
- 抗噪声和被试间变异性

---

## 技术要点

### 与传统方法对比

| 方法 | 权重支持 | 分辨率限制 | 小模块检测 |
|------|----------|------------|------------|
| Modularity | ❌ | 有 | ❌ |
| Louvain | 部分 | 有 | ❌ |
| Surprise | ❌ | 无 | ✅ |
| **Asymptotical Surprise** | ✅ | 无 | ✅ |

### 算法流程

```
1. 构建加权功能连接矩阵
   ↓
2. 初始化社区分配
   ↓
3. 迭代优化 Asymptotical Surprise
   - 合并/分裂社区
   - 计算目标函数变化
   ↓
4. 输出多尺度模块结构
```

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **静息态 fMRI** | 检测功能模块组织 |
| **脑发育研究** | 追踪模块演化 |
| **脑疾病诊断** | 模块结构异常检测 |
| **多尺度分析** | 跨尺度功能组织 |

---

## 验证数据

**合成网络验证：**
- 已知地面真值的模块结构
- 添加噪声和被试变异
- Asymptotical Surprise 灵敏度最高

**fMRI 数据应用：**
- 静息态功能连接网络
- 发现异质模块组织
- 跨多尺度的簇分布

---

## 技术实现

### 数据预处理

```python
# 构建功能连接矩阵
fc_matrix = compute_correlation(time_series)

# 阈值处理（可选）
fc_thresholded = apply_threshold(fc_matrix, threshold=0.1)
```

### 社区检测

```python
# 使用 Asymptotical Surprise
from surprise import asymptotical_surprise

communities = asymptotical_surprise(
    weighted_matrix=fc_matrix,
    n_iterations=100,
    random_seed=42
)
```

### 结果分析

```python
# 模块大小分布
module_sizes = get_module_sizes(communities)

# 多尺度分析
scales = analyze_multiscale(communities)
```

---

## 相关技能

- `time-varying-brain-connectivity` - 时变脑网络分析
- `gnn-transformer-fusion` - 多模态数据融合

---

## 来源

- **论文：** Community detection in weighted brain connectivity networks beyond the resolution limit
- **arXiv：** 1609.04316
- **效用评分：** 0.96
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
