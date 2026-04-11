---
arxiv_id: 2407.13514v1
utility: 0.88
tags: '[topological data analysis, seizure, effective connectivity, Hodge decomposition, causal inference, EEG, brain hierarchy]'
created: 2026-03-31
---

# Causality-Based Topological Ranking (CBTR)

## Activation Keywords

- CBTR 方法
- 脑层次拓扑分析
- 有效连接拓扑
- Hodge decomposition brain
- 因果推断脑网络
- 癫痫发作脑层次变化

## Problem Statement

传统拓扑数据分析（TDA）方法的局限：
- Persistent Homology 依赖对称距离度量
- 无法捕捉有向动力学（有效连接）
- 难以识别脑区的层次结构
- 癫痫发作时的层次变化难以量化

## Method Overview

El-Yaagoubi et al. (2024) 提出 CBTR 方法：
1. 因果推断（CI）评估有效脑连接
2. Hodge 分解（HD）进行层次排序
3. 识别脑区间的相互影响
4. 分析癫痫发作期间的层次变化

## Tools Used

- `Component` - Analysis component
- `Causal Inference` - Analysis component
- `Hodge Decomposition` - Analysis component
- `TDA` - Analysis component
- `EEG` - Analysis component

## Architecture

```
EEG Time Series Data
        ↓
┌──────────────────────┐
│  Causal Inference    │
│  (Granger/Transfer   │
│   Entropy)           │
└──────────────────────┘
        ↓
  Directed Connectivity Matrix
        ↓
┌──────────────────────┐
│  Hodge Decomposition │
│  - Gradient (hierar) │
│  - Curl (circulation)│
│  - Harmonic          │
└──────────────────────┘
        ↓
  Hierarchical Ranking
        ↓
  Seizure Impact Analysis
```

## Step-by-Step Instructions

### CBTR 实现

1. **因果推断评估有效连接**
   ```python
   import numpy as np
   from statsmodels.tsa.stattools import grangercausalitytests
   
   def compute_granger_causality(eeg_data, maxlag=5):
       """计算 Granger 因果矩阵"""
       n_channels = eeg_data.shape[1]
       causality_matrix = np.zeros((n_channels, n_channels))
       
       for i in range(n_channels):
           for j in range(n_channels):
               if i != j:
                   # 测试 j -> i 的因果
                   test_result = grangercausalitytests(
                       np.column_stack([eeg_data[:, i], eeg_data[:, j]]),
                       maxlag=maxlag,
                       verbose=False
                   )
                   # 取最小 p 值
                   p_values = [test_result[lag][0]['ssr_ftest'][1] 
                               for lag in range(1, maxlag+1)]
                   causality_matrix[i, j] = -np.log(min(p_values) + 1e-10)
       
       return causality_matrix
   ```

2. **Hodge 分解**
   ```python
   from scipy import sparse
   from scipy.sparse.linalg import lsqr
   
   def hodge_decomposition(flow_matrix):
       """
       Hodge 分解：将有向流分解为梯度、旋度和调和分量
       
       flow_matrix: 有向连接矩阵 A[i,j] = flow from j to i
       """
       n = flow_matrix.shape[0]
       
       # 构建图拉普拉斯算子
       # L = D - A (有向版本)
       out_degree = flow_matrix.sum(axis=1)
       in_degree = flow_matrix.sum(axis=0)
       
       # 构建边-节点关联矩阵
       edges = [(i, j) for i in range(n) for j in range(n) 
                if i != j and flow_matrix[i, j] != 0]
       m = len(edges)
       
       # Incidence matrix B: B[e, v] = 1 if v is source, -1 if v is target
       B = sparse.lil_matrix((m, n))
       flow_values = np.zeros(m)
       
       for idx, (i, j) in enumerate(edges):
           B[idx, j] = 1   # source
           B[idx, i] = -1  # target
           flow_values[idx] = flow_matrix[i, j]
       
       B = B.tocsr()
       
       # 求解最小二乘问题: min ||B @ rank - flow||^2
       # 这给出梯度分量（层次排名）
       result = lsqr(B, flow_values)
       gradient_rank = result[0]
       
       # 残差 = 旋度 + 调和分量
       residual = flow_values - B @ gradient_rank
       
       return {
           'gradient': gradient_rank,  # 层次排名
           'residual': residual,        # 非层次分量
           'ranking': np.argsort(gradient_rank)[::-1]  # 从高到低排名
       }
   ```

3. **CBTR 完整流程**
   ```python
   def cbtr_analysis(eeg_preictal, eeg_ictal):
       """CBTR：癫痫发作前后的层次变化分析"""
       
       # 1. 计算因果矩阵
       causality_pre = compute_granger_causality(eeg_preictal)
       causality_ictal = compute_granger_causality(eeg_ictal)
       
       # 2. Hodge 分解
       hodge_pre = hodge_decomposition(causality_pre)
       hodge_ictal = hodge_decomposition(causality_ictal)
       
       # 3. 层次变化
       ranking_change = hodge_ictal['gradient'] - hodge_pre['gradient']
       
       # 4. 识别变化最大的脑区
       most_influenced = np.argsort(np.abs(ranking_change))[::-1]
       
       return {
           'preictal_ranking': hodge_pre['ranking'],
           'ictal_ranking': hodge_ictal['ranking'],
           'ranking_change': ranking_change,
           'most_influenced_regions': most_influenced[:5],
           'gradient_pre': hodge_pre['gradient'],
           'gradient_ictal': hodge_ictal['gradient']
       }
   ```

4. **可视化层次变化**
   ```python
   import matplotlib.pyplot as plt
   
   def plot_hierarchical_change(cbtr_result, channel_names):
       """可视化层次变化"""
       fig, axes = plt.subplots(1, 3, figsize=(15, 5))
       
       # 发作前排名
       axes[0].bar(range(len(channel_names)), 
                   cbtr_result['gradient_pre'])
       axes[0].set_title('Pre-ictal Hierarchy')
       axes[0].set_xlabel('Channel')
       axes[0].set_ylabel('Gradient Rank')
       
       # 发作时排名
       axes[1].bar(range(len(channel_names)), 
                   cbtr_result['gradient_ictal'])
       axes[1].set_title('Ictal Hierarchy')
       
       # 变化量
       axes[2].bar(range(len(channel_names)), 
                   cbtr_result['ranking_change'])
       axes[2].set_title('Hierarchical Change')
       axes[2].axhline(y=0, color='r', linestyle='--')
       
       plt.tight_layout()
       return fig
   ```

## Example Usage

```python
import numpy as np

# 加载 EEG 数据
eeg_preictal = load_eeg_segment('preictal')  # 发作前
eeg_ictal = load_eeg_segment('ictal')        # 发作时

# CBTR 分析
results = cbtr_analysis(eeg_preictal, eeg_ictal)

# 输出结果
print("Top 5 most influenced regions during seizure:")
for i, region in enumerate(results['most_influenced_regions'][:5]):
    print(f"  {i+1}. Channel {region}: Δrank = {results['ranking_change'][region]:.3f}")

# 可视化
plot_hierarchical_change(results, channel_names)
```

## Key Findings

### Traditional TDA vs CBTR

| Aspect | Traditional TDA | CBTR |
|--------|----------------|------|
| Directionality | Symmetric only | Captures directed flow |
| Hierarchy | Not directly accessible | Explicit ranking |
| Causal dynamics | Missing | Integrated |
| Seizure analysis | Limited | Effective |

### Hodge Decomposition Components

| Component | Interpretation |
|-----------|---------------|
| Gradient | Hierarchical influence |
| Curl | Circular flow |
| Harmonic | Global structure |

## Description

Causality-Based Topological Ranking (CBTR)

**Key Concepts:**
- 传统拓扑数据分析（TDA）方法的局限：
- Persistent Homology 依赖对称距离度量
- 无法捕捉有向动力学（有效连接）
- 难以识别脑区的层次结构
- 癫痫发作时的层次变化难以量化

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 因果推断评估有效连接

### Step 2: Hodge 分解

### Step 3: CBTR 完整流程

### Step 4: 可视化层次变化

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Causality-Based Topological Ranking (CBTR) to my analysis.

**Agent:** I'll help you apply cbtr-causality-topological-ranking. First, let me understand your specific use case...

**Context:** 传统拓扑数据分析（TDA）方法的局限：
- Persistent Homology 依赖对称距离度量
- 无法捕捉有向动力学（有效连接）
- 难以识别脑区的层次

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for cbtr-causality-topological-ranking?

**Agent:** Let me search for the latest research and best practices...

## References

- El-Yaagoubi, A.B. et al. (2024). Topological Analysis of Seizure-Induced Changes in Brain Hierarchy Through Effective Connectivity. arXiv:2407.13514.

## Related Skills

- conex-connect-eeg-extremal
- seizure-detection-connectivity
- time-varying-brain-connectivity