---
name: bursty-persistent-brain-networks-pbm
arxiv_id: 1601.03236v1
utility: 0.88
tags: '[dynamic functional connectivity, fMRI, point-based method, brain networks, resting-state, temporal dynamics]'
created: 2026-03-31
description: "Bursty Persistent Brain Networks (PBM)"
---

# Bursty Persistent Brain Networks (PBM)

## Activation Keywords

- 动态功能连接
- 点方法 fMRI
- bursty connectivity
- resting-state networks
- 脑网络时间动力学
- PBM 点方法

## Problem Statement

研究静息态 fMRI 脑连接动态的传统方法存在局限：
- 滑动窗口方法时间分辨率低
- 无法在单时间点估计连接
- 难以区分 bursty vs persistent 连接模式

## Method Overview

Fransson (2016) 提出了 Point-Based Method (PBM)：
1. 单时间点连接估计
2. 高时间敏感性
3. 区分 bursty 和 persistent 连接模式
4. 估计连接持久性（persistency）

## Tools Used

- `Method` - Analysis component
- `Sliding Window` - Analysis component
- `PBM` - Analysis component
- `Temporal Graph Theory` - Analysis component

## Key Concepts

### Bursty vs Persistent Connectivity

| Pattern | Characteristics | Example |
|---------|-----------------|---------|
| Bursty | Intermittent bursts, short duration | Between-network integration |
| Persistent | Tonic, periodic patterns | Within-network coherence |

### Persistency

- 连接模式的内在轨迹/记忆持续时间
- 反映脑网络状态的稳定性

## Step-by-Step Instructions

### PBM 实现流程

1. **预处理 fMRI 数据**
   ```python
   # 标准预处理流程
   import nibabel as nib
   from nilearn import input_data
   
   # 提取时间序列
   masker = input_data.NiftiLabelsMasker(labels_img=atlas)
   time_series = masker.fit_transform(fmri_img)
   ```

2. **单时间点连接估计**
   ```python
   def point_based_connectivity(ts, t):
       """估计时间点 t 的功能连接"""
       # 使用滑动窗口或瞬时方法
       window = ts[max(0, t-w):t+w+1]
       return np.corrcoef(window.T)
   ```

3. **Bursty 检测**
   ```python
   def detect_bursty(conn_series, threshold=0.5):
       """检测 bursty 连接模式"""
       # 连接强度的突发性
       bursts = conn_series > threshold
       return bursts, np.mean(bursts)  # burst fraction
   ```

4. **Persistency 估计**
   ```python
   def estimate_persistency(conn_series, tau=10):
       """估计连接持久性"""
       # 自相关衰减时间
       autocorr = np.correlate(conn_series, conn_series, mode='full')
       return np.sum(autocorr[:tau] > 0.5 * autocorr[0])
   ```

## Example Usage

```python
import numpy as np
from scipy import signal

class PointBasedConnectivity:
    """PBM 动态功能连接分析"""
    
    def __init__(self, time_series, window_size=5):
        self.ts = time_series
        self.w = window_size
        
    def compute_pbm(self):
        """计算点方法连接矩阵序列"""
        n_timepoints = self.ts.shape[0]
        n_regions = self.ts.shape[1]
        
        conn_series = []
        for t in range(self.w, n_timepoints - self.w):
            window = self.ts[t-self.w:t+self.w+1]
            conn = np.corrcoef(window.T)
            conn_series.append(conn)
        
        return np.array(conn_series)
    
    def classify_pattern(self, conn_series):
        """分类连接模式（bursty vs persistent）"""
        # 计算 Fano factor
        mean_conn = np.mean(conn_series)
        var_conn = np.var(conn_series)
        fano = var_conn / mean_conn if mean_conn > 0 else 0
        
        # Fano factor 高 → bursty
        return 'bursty' if fano > 1.0 else 'persistent'
```

## Key Findings

| Network Pair | Pattern | Interpretation |
|--------------|---------|----------------|
| Between RSNs | Bursty | Intermittent integration |
| Within RSN | Persistent | Stable coherence |

## Description

Bursty Persistent Brain Networks (PBM)

**Key Concepts:**
- --------|-----------------|---------|
- network integration |
- network coherence |

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 预处理 fMRI 数据

### Step 2: 单时间点连接估计

### Step 3: Bursty 检测

### Step 4: Persistency 估计

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Bursty Persistent Brain Networks (PBM) to my analysis.

**Agent:** I'll help you apply bursty-persistent-brain-networks-pbm. First, let me understand your specific use case...

**Context:** --------|-----------------|---------|

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for bursty-persistent-brain-networks-pbm?

**Agent:** Let me search for the latest research and best practices...

## References

- Fransson, P. et al. (2016). Bursty and persistent properties of large-scale brain networks. arXiv:1601.03236.

## Related Skills

- time-varying-brain-connectivity
- dynamic-functional-connectivity
- brain-network-controllability