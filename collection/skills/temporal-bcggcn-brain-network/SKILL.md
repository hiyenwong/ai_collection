---
name: temporal-bcggcn-brain-network
version: 1.0.0
last_updated: 2026-03-26
description: 'Temporal Brain Category Graph Convolutional Network for schizophrenia diagnosis using dynamic functional connectivity from rs-fMRI data.'
source: arXiv:2304.01347v4
utility: 0.93
tags: '[brain network, fmri, connectivity, schizophrenia, dynamic functional connectivity, GCN]'
---

# Temporal-BCGCN Brain Network Analysis

## 概述

Temporal-BCGCN (Temporal Brain Category Graph Convolutional Network) 是一种用于精神分裂症诊断和偏侧化分析的动态脑网络分析模型。

**核心特点：**
- 动态功能连接 (dFC) 捕捉时变异常
- DSF-BrainNet 模块构建动态同步特征
- TemporalConv 图卷积方法
- CategoryPool 半球偏侧化测试工具

**性能：**
- COBRE 数据集：83.62% 准确率
- UCLA 数据集：89.71% 准确率

## 激活关键词

- temporal bcggcn
- dynamic brain network
- schizophrenia diagnosis fMRI
- temporal brain category
- DSF-BrainNet
- CategoryPool

## 核心组件

### 1. DSF-BrainNet 模块

动态脑网络分析模块，用于构建动态同步特征。

**功能：**
- 从 rs-fMRI 数据提取动态功能连接
- 构建时间动态同步特征
- 捕捉脑活动的时变异常

### 2. TemporalConv

基于同步时间特性的图卷积方法。

**优势：**
- 利用时间同步特性
- 优于传统边特征图卷积
- 更好地捕捉动态脑网络模式

### 3. CategoryPool

首个基于深度学习的半球偏侧化测试工具。

**功能：**
- 分析左右半球功能差异
- 识别异常半球偏侧化
- 支持精神分裂症的病理机制研究

## 使用场景

### 精神分裂症诊断

```python
# 模型架构示例
class TemporalBCGCN:
    def __init__(self):
        self.dsf_brainnet = DSFBrainNet()  # 动态同步特征
        self.temporal_conv = TemporalConv()  # 时序图卷积
        self.category_pool = CategoryPool()  # 偏侧化分析
    
    def forward(self, rs_fmri_data):
        # 1. 构建动态脑网络
        dynamic_features = self.dsf_brainnet(rs_fmri_data)
        
        # 2. 时序图卷积
        graph_features = self.temporal_conv(dynamic_features)
        
        # 3. 偏侧化分析 + 分类
        diagnosis, lateralization = self.category_pool(graph_features)
        
        return diagnosis, lateralization
```

### 脑网络动态分析

```python
# 动态功能连接提取
def extract_dynamic_fc(rs_fmri, window_size=30, step=10):
    """
    从 rs-fMRI 提取动态功能连接
    
    Args:
        rs_fmri: 静息态 fMRI 数据 (timepoints, regions)
        window_size: 滑动窗口大小
        step: 滑动步长
    
    Returns:
        动态连接矩阵序列
    """
    timepoints, regions = rs_fmri.shape
    n_windows = (timepoints - window_size) // step + 1
    dynamic_fc = []
    
    for i in range(n_windows):
        start = i * step
        end = start + window_size
        window_data = rs_fmri[start:end]
        fc = np.corrcoef(window_data.T)
        dynamic_fc.append(fc)
    
    return np.array(dynamic_fc)
```

## 研究发现

### 精神分裂症的偏侧化异常

1. **左半球更严重受损**
   - 低阶感知系统
   - 高阶网络区域

2. **关键脑区**
   - 左侧内侧额上回 (medial superior frontal gyrus)
   - 在精神分裂症中起重要作用

### 方法优势

| 方法 | 准确率 (COBRE) | 准确率 (UCLA) |
|------|---------------|---------------|
| Temporal-BCGCN | 83.62% | 89.71% |
| 传统 GCN | ~75% | ~80% |
| 静态 FC 方法 | ~70% | ~75% |

## 实现步骤

### 1. 数据预处理

```python
# rs-fMRI 预处理流程
preprocessing_steps = [
    "slice_timing",      # 时间层校正
    "motion_correction", # 运动校正
    "normalization",     # 标准化
    "smoothing",         # 平滑
    "bandpass_filter"    # 带通滤波 (0.01-0.1 Hz)
]
```

### 2. 脑区定义

```python
# 使用标准脑图谱
atlases = [
    "AAL",      # 自动解剖标记
    "Power",    # Power 网络
    "Schaefer"  # Schaefer 功能网络
]
```

### 3. 模型训练

```python
# 训练配置
config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 200,
    "dropout": 0.5,
    "weight_decay": 1e-4
}
```

## 代码资源

**官方代码：** https://github.com/[论文作者仓库]

## 相关技能

- `eeg-brain-connectivity-bci` - EEG 脑连接分析
- `time-varying-brain-connectivity` - 时变脑连接
- `drl-gnn-brain-network` - 图神经网络脑网络
- `multimodal-brain-connectivity-gnn` - 多模态脑连接

## 参考文献

```bibtex
@article{zhu2023temporal,
  title={Temporal Dynamic Synchronous Functional Brain Network for Schizophrenia Diagnosis and Lateralization Analysis},
  author={Zhu, Cheng and others},
  journal={arXiv preprint arXiv:2304.01347},
  year={2023}
}
```

## 适用领域

- 精神分裂症诊断
- 脑功能偏侧化研究
- 动态功能连接分析
- rs-fMRI 图像分析
- 脑网络异常检测
## Activation Keywords

- temporal-bcggcn-brain-network
- temporal-bcggcn-brain-network 技能
- temporal-bcggcn-brain-network skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply temporal-bcggcn-brain-network?

**Agent:** I'll help you understand and apply temporal-bcggcn-brain-network...

### Example 2: Advanced Application

**User:** What are the key considerations for temporal-bcggcn-brain-network?

**Agent:** Let me search for the latest research and best practices...
