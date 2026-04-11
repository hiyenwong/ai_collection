# BrainGB - Brain Network Analysis Benchmark with GNNs

**来源论文：** arXiv:2204.07054 - BrainGB: A Benchmark for Brain Network Analysis with Graph Neural Networks
**效用评分：** 0.99
**创建时间：** 2026-03-24 09:37

---

## 概述

BrainGB 是一个用于脑网络分析的图神经网络基准工具包，标准化了脑网络构建流程和 GNN 设计实现。支持功能性和结构性神经影像模态，提供开箱即用的 Python 包。

## 激活关键词

- BrainGB
- brain network benchmark
- GNN brain analysis
- connectome GNN
- brain graph neural network
- 脑网络基准
- 脑连接组 GNN

## 官方资源

- **网站：** https://braingb.us
- **Python 包：** `pip install braingb`
- **论文：** IEEE Transactions on Medical Imaging

## 核心架构

```
┌──────────────────────────────────────────────────────────┐
│                    BrainGB 流程                          │
│                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ 神经影像数据 │ →  │ 脑网络构建  │ →  │ GNN 模型    │  │
│  │ (fMRI/DWI)  │    │ (标准化)    │    │ (模块化)    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                  │                  │          │
│         ↓                  ↓                  ↓          │
│    功能连接           Pearson 相关        GraphConv     │
│    结构连接           纤维束追踪         GAT           │
│                                          GCN           │
│                                          GraphSAGE     │
└──────────────────────────────────────────────────────────┘
```

## 脑网络构建流程

### 1. 功能性脑网络（fMRI）

```python
import numpy as np
from nilearn import connectome

def build_functional_brain_network(fmri_timeseries, atlas_labels, method='correlation'):
    """
    从 fMRI 时间序列构建功能脑网络
    
    Args:
        fmri_timeseries: [n_timepoints, n_rois]
        atlas_labels: ROI 标签列表
        method: 连接性度量方法
    
    Returns:
        adj_matrix: [n_rois, n_rois] 邻接矩阵
    """
    # 计算功能连接
    conn_measure = connectome.ConnectivityMeasure(
        kind=method,
        standardize=True
    )
    
    # Pearson 相关矩阵
    corr_matrix = conn_measure.fit_transform([fmri_timeseries])[0]
    
    # 阈值化（保留强连接）
    threshold = np.percentile(np.abs(corr_matrix), 90)
    adj_matrix = np.where(np.abs(corr_matrix) > threshold, corr_matrix, 0)
    
    # 移除对角线
    np.fill_diagonal(adj_matrix, 0)
    
    return adj_matrix, corr_matrix
```

### 2. 结构性脑网络（DWI）

```python
def build_structural_brain_network(dwi_data, atlas_labels, tracking_params):
    """
    从 DWI 数据构建结构脑网络
    
    Args:
        dwi_data: 扩散加权成像数据
        atlas_labels: ROI 标签
        tracking_params: 纤维束追踪参数
    
    Returns:
        adj_matrix: [n_rois, n_rois] 邻接矩阵
    """
    # 纤维束追踪
    streamlines = perform_tractography(dwi_data, tracking_params)
    
    # 构建连接矩阵
    n_rois = len(atlas_labels)
    adj_matrix = np.zeros((n_rois, n_rois))
    
    for streamline in streamlines:
        # 找到纤维束经过的 ROI
        endpoints = get_streamline_endpoints(streamline)
        roi_start = find_nearest_roi(endpoints[0], atlas_labels)
        roi_end = find_nearest_roi(endpoints[1], atlas_labels)
        
        if roi_start != roi_end:
            adj_matrix[roi_start, roi_end] += 1
            adj_matrix[roi_end, roi_start] += 1
    
    # 归一化
    adj_matrix = adj_matrix / adj_matrix.max()
    
    return adj_matrix
```

## GNN 模型实现

### 基础 GNN 模块

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GATConv, SAGEConv, global_mean_pool

class BrainGNN(nn.Module):
    """
    BrainGB 推荐的 GNN 架构
    """
    def __init__(self, node_dim, hidden_dim, n_classes, n_layers=3, gnn_type='GCN'):
        super().__init__()
        
        # 输入投影
        self.input_proj = nn.Linear(node_dim, hidden_dim)
        
        # GNN 层
        self.gnn_layers = nn.ModuleList()
        for _ in range(n_layers):
            if gnn_type == 'GCN':
                self.gnn_layers.append(GCNConv(hidden_dim, hidden_dim))
            elif gnn_type == 'GAT':
                self.gnn_layers.append(GATConv(hidden_dim, hidden_dim // 8, heads=8))
            elif gnn_type == 'SAGE':
                self.gnn_layers.append(SAGEConv(hidden_dim, hidden_dim))
        
        # 批归一化
        self.batch_norms = nn.ModuleList([
            nn.BatchNorm1d(hidden_dim) for _ in range(n_layers)
        ])
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(hidden_dim, n_classes)
        )
        
        self.gnn_type = gnn_type
    
    def forward(self, x, edge_index, batch):
        """
        Args:
            x: 节点特征 [n_nodes, node_dim]
            edge_index: 边索引 [2, n_edges]
            batch: 批索引 [n_nodes]
        """
        # 输入投影
        h = self.input_proj(x)
        
        # GNN 层
        for i, gnn_layer in enumerate(self.gnn_layers):
            h = gnn_layer(h, edge_index)
            h = self.batch_norms[i](h)
            h = F.relu(h)
            h = F.dropout(h, p=0.1, training=self.training)
        
        # 图级池化
        graph_embedding = global_mean_pool(h, batch)
        
        # 分类
        logits = self.classifier(graph_embedding)
        
        return logits
```

### 节点特征工程

```python
def extract_brain_node_features(adj_matrix, roi_labels):
    """
    提取脑网络节点特征
    
    BrainGB 推荐的特征:
    1. 度中心性
    2. 介数中心性
    3. 聚类系数
    4. ROI 位置编码
    """
    import networkx as nx
    
    G = nx.from_numpy_array(adj_matrix)
    
    features = []
    
    for i, label in enumerate(roi_labels):
        # 度中心性
        degree = nx.degree_centrality(G)[i]
        
        # 介数中心性
        betweenness = nx.betweenness_centrality(G)[i]
        
        # 聚类系数
        clustering = nx.clustering(G, i)
        
        # 特征向量中心性
        try:
            eigenvector = nx.eigenvector_centrality(G, max_iter=1000)[i]
        except:
            eigenvector = 0.0
        
        features.append([degree, betweenness, clustering, eigenvector])
    
    return np.array(features)
```

## 实验推荐

### 数据集

BrainGB 在以下数据集上验证：

| 数据集 | 模态 | 任务 |
|--------|------|------|
| ABIDE | fMRI | 自闭症分类 |
| PNC | fMRI | 性别分类 |
| UKB | fMRI | 年龄预测 |
| HCP | DWI | 认知能力 |

### 推荐配置

```python
# BrainGB 推荐的 GNN 设计

RECOMMENDED_CONFIGS = {
    'GNN_Type': 'GCN or GAT',
    'Num_Layers': '2-4',
    'Hidden_Dim': '64-256',
    'Dropout': '0.3-0.5',
    'Learning_Rate': '1e-3 to 1e-4',
    'Batch_Size': '32-128',
    'Node_Features': 'Degree + Betweenness + Clustering',
    'Edge_Features': 'Connection Strength',
    'Pooling': 'Global Mean Pooling'
}

# 推荐的数据增强
AUGMENTATION_STRATEGIES = [
    'edge_perturbation',      # 边扰动
    'node_feature_masking',   # 节点特征掩码
    'graph_subsampling',      # 图子采样
    'random_walk_augmentation' # 随机游走增强
]
```

### 训练脚本

```python
def train_braingb_model(model, train_loader, val_loader, epochs=200, lr=1e-3):
    """
    训练 BrainGB 模型
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.CrossEntropyLoss()
    
    best_val_acc = 0
    
    for epoch in range(epochs):
        # 训练
        model.train()
        train_loss = 0
        train_correct = 0
        
        for batch in train_loader:
            x, edge_index, batch_idx, y = batch.x, batch.edge_index, batch.batch, batch.y
            
            optimizer.zero_grad()
            logits = model(x, edge_index, batch_idx)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            train_correct += (logits.argmax(dim=1) == y).sum().item()
        
        # 验证
        model.eval()
        val_correct = 0
        val_total = 0
        
        with torch.no_grad():
            for batch in val_loader:
                x, edge_index, batch_idx, y = batch.x, batch.edge_index, batch.batch, batch.y
                logits = model(x, edge_index, batch_idx)
                val_correct += (logits.argmax(dim=1) == y).sum().item()
                val_total += y.size(0)
        
        val_acc = val_correct / val_total
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_model.pt')
        
        scheduler.step()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch}: Train Loss={train_loss/len(train_loader):.4f}, Val Acc={val_acc:.4f}")
    
    return best_val_acc
```

## 关键发现

BrainGB 的实验推荐：

1. **GNN 类型**：GCN 和 GAT 在脑网络上表现最好
2. **层数**：2-4 层足够，过深会导致过平滑
3. **节点特征**：度中心性 + 介数中心性 + 聚类系数组合最佳
4. **池化方法**：全局平均池化简单有效
5. **数据增强**：边扰动对脑网络最有效

## 应用场景

1. **疾病分类** - 自闭症、ADHD、精神分裂症
2. **认知预测** - 智商、年龄、认知能力
3. **生物标志物** - 脑网络特征作为诊断指标
4. **药物反应** - 预测治疗响应

## 相关技能

- `gnn-transformer-fusion` - GNN Transformer 融合
- `multimodal-brain-connectivity-gnn` - 多模态脑连接 GNN
- `neurograph-benchmark` - 神经图基准
- `drl-gnn-brain-network` - 深度强化学习 GNN 脑网络

---

_此技能基于 BrainGB 基准工具包，用于标准化脑网络 GNN 分析_
## Description

BrainGB - Brain Network Analysis Benchmark with GNNs

## Activation Keywords

- braingb-benchmark
- braingb-benchmark 技能
- braingb-benchmark skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: GNN 类型

### Step 2: 层数

### Step 3: 节点特征

### Step 4: 池化方法

### Step 5: 数据增强

## Examples

### Example 1: Basic Application

**User:** I need to apply BrainGB - Brain Network Analysis Benchmark with GNNs to my analysis.

**Agent:** I'll help you apply braingb-benchmark. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for braingb-benchmark?

**Agent:** Let me search for the latest research and best practices...
