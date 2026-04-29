---
name: causal-brain-network-inference
description: "从神经影像数据中推断脑区间因果连接关系的方法论。整合Granger因果、动态因果模型(DCM)和因果发现算法。"
---

# 脑网络因果推断 (Causal Brain Network Inference)

## 概述

从神经影像数据中推断脑区间因果连接关系的方法论。整合Granger因果、动态因果模型(DCM)和因果发现算法。

本技能整合了神经科学领域的前沿方法论，为研究人员和开发者提供实用的技术指导。

## 核心概念

- **Granger因果分析**
- **动态因果模型 (DCM)**
- **结构方程模型 (SEM)**
- **因果发现算法 (PC, GES)**
- **干预与反事实推理**

## 应用场景

- 脑功能网络因果结构识别
- 神经疾病因果机制研究
- 脑刺激靶点选择
- 认知任务因果建模

## 方法论

- 多变量Granger因果
- 频域Granger因果
- 贝叶斯网络学习
- 独立成分分析 (ICA)

## 代码示例

```python

import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests

def compute_granger_causality_matrix(data, maxlag=5):
    """
    计算多变量Granger因果矩阵
    data: (n_regions, n_timepoints) 时间序列数据
    """
    n_regions = data.shape[0]
    gc_matrix = np.zeros((n_regions, n_regions))
    
    for i in range(n_regions):
        for j in range(n_regions):
            if i != j:
                # 检验 j 是否Granger导致 i
                test_data = np.column_stack([data[i], data[j]])
                gc_result = grangercausalitytests(test_data, maxlag=maxlag, verbose=False)
                # 提取p值
                p_value = gc_result[maxlag][0]['ssr_ftest'][1]
                gc_matrix[i, j] = -np.log10(p_value)  # 转换为显著性分数
    
    return gc_matrix

```

## 相关工具与库

- **Python**: NumPy, SciPy, scikit-learn
- **深度学习**: PyTorch, TensorFlow
- **神经影像**: Nilearn, MNE-Python, ANTsPy
- **拓扑分析**: GUDHI, Ripser, scikit-tda
- **信息论**: PyInform, JIDT

## 学习资源

### 论文
- 相关领域的经典和最新论文
- 建议关注 NeurIPS, ICML, Nature Neuroscience, PLOS Computational Biology

### 数据集
- Human Connectome Project (HCP)
- OpenNeuro
- EEG-BIDS 标准数据集

## 激活关键词

- causal brain network inference
- 脑网络因果推断
- Granger因果分析

## 备注

本技能基于神经科学领域的前沿研究方法论创建，反映了当前该领域的最新发展趋势。
由于网络限制，技能内容基于领域专业知识整理，建议在实际应用时参考最新文献。

---
*技能生成时间: 2026-04-12*
*来源: 自动化神经科学研究工作流*


## Activation Keywords

- causal-brain-network-inference
- causal brain network
- causal brain network inference


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Causal Brain Network Inference

**Agent:** Causal Brain Network Inference 是关于...
