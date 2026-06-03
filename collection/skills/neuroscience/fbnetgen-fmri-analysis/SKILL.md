---
name: fbnetgen-fmri-analysis
version: 1.0.0
description: |
  任务感知的 GNN fMRI 分析框架（FBNETGEN）。通过深度脑网络生成，
  实现端到端可训练的临床预测模型。
  触发词：fMRI分析、脑网络、GNN、功能连接、临床预测、FBNETGEN、
  functional brain network, graph neural network, fMRI analysis。
---

# FBNETGEN: Task-aware GNN-based fMRI Analysis

## 核心方法论

### 问题定义

**挑战：** 传统功能脑网络存在噪声、不感知下游任务、不兼容深度 GNN 模型。

**解决方案：** FBNETGEN - 任务感知的可解释 fMRI 分析框架

---

## 关键概念

### 1. 端到端框架

```
┌─────────────────────────────────────────────────────┐
│          FBNETGEN 框架                              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  fMRI 时间序列                                      │
│       │                                             │
│       ▼                                             │
│  ┌─────────────────────────────────────┐           │
│  │ 1. ROI 特征提取                     │           │
│  │    突出感兴趣区域特征                │           │
│  └─────────────────────────────────────┘           │
│       │                                             │
│       ▼                                             │
│  ┌─────────────────────────────────────┐           │
│  │ 2. 脑网络生成（可学习图生成器）      │           │
│  │    任务导向的网络构建                │           │
│  └─────────────────────────────────────┘           │
│       │                                             │
│       ▼                                             │
│  ┌─────────────────────────────────────┐           │
│  │ 3. GNN 临床预测                      │           │
│  │    图神经网络分类/回归                │           │
│  └─────────────────────────────────────┘           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 2. 可学习图生成器

**核心创新：** 学习将原始时间序列特征转换为任务导向的脑网络

**优势：**
- 任务感知：针对特定预测任务优化
- 可解释：高亮预测相关的脑区
- 端到端：整个流程可微分训练

### 3. 与传统方法对比

| 特性 | 传统脑网络 | FBNETGEN |
|------|------------|----------|
| 噪声处理 | ❌ 噪声敏感 | ✅ 自动降噪 |
| 任务感知 | ❌ 不感知 | ✅ 任务导向 |
| GNN 兼容 | ❌ 不兼容 | ✅ 直接输入 |
| 可解释性 | 部分 | ✅ 高亮关键脑区 |

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **疾病诊断** | 阿尔茨海默病、自闭症检测 |
| **临床预测** | 患者预后预测 |
| **生物标志物** | 识别关键脑区 |
| **神经科学研究** | 功能网络分析 |

---

## 技术实现

### PyTorch 示例

```python
import torch
import torch.nn as nn

class FBNETGEN(nn.Module):
    def __init__(self, n_rois, hidden_dim, n_classes):
        """
        n_rois: 感兴趣区域数量
        hidden_dim: 隐藏层维度
        n_classes: 分类类别数
        """
        super().__init__()
        
        # ROI 特征提取
        self.roi_encoder = nn.Sequential(
            nn.Linear(n_rois, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 图生成器（可学习邻接矩阵）
        self.graph_generator = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_rois * n_rois)
        )
        
        # GNN 分类器
        self.gnn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_classes)
        )
        
    def forward(self, fmri_timeseries):
        """
        fmri_timeseries: (batch, time, n_rois)
        """
        # ROI 特征提取
        roi_features = self.roi_encoder(fmri_timeseries.mean(dim=1))
        
        # 生成脑网络
        adj_logits = self.graph_generator(roi_features)
        adj = torch.sigmoid(adj_logits.view(-1, n_rois, n_rois))
        
        # GNN 预测
        node_features = torch.matmul(adj, roi_features.unsqueeze(-1)).squeeze(-1)
        output = self.gnn(node_features)
        
        return output, adj  # 返回预测和可解释的邻接矩阵
```

---

## 相关技能

- `gnn-transformer-fusion` - 多模态数据融合
- `time-varying-brain-connectivity` - 时变脑网络分析

---

## 来源

- **论文：** FBNETGEN: Task-aware GNN-based fMRI Analysis via Functional Brain Network Generation
- **arXiv：** 2205.12465
- **效用评分：** 0.91
- **学习日期：** 2026-03-22

## Activation Keywords

- fMRI分析
- 脑网络
- GNN
- 功能连接
- FBNETGEN

## Tools Used

- **read**: Read skill documentation
- **exec**: Run analysis scripts
- **web_fetch**: Fetch papers

## Instructions for Agents

1. Understand end-to-end fMRI analysis pipeline
2. Apply task-aware graph generation
3. Interpret highlighted brain regions
4. Validate on clinical datasets

## Examples

```python
# Example: fMRI clinical prediction
model = FBNETGEN(n_rois=200, hidden_dim=128, n_classes=2)
prediction, brain_network = model(fmri_data)
```