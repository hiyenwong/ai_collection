---
name: hyperbolic-brain-network-embedding-for-neurodegene
description: **来源论文：** arXiv:2407.16589 - Hyperbolic embedding of brain networks detects regions disrupted by neurodegeneration in Alzheimer's disease
---

# Hyperbolic Brain Network Embedding for Neurodegeneration Detection

**来源论文：** arXiv:2407.16589 - Hyperbolic embedding of brain networks detects regions disrupted by neurodegeneration in Alzheimer's disease
**效用评分：** 0.99
**创建时间：** 2026-03-24 07:03

---

## 概述

将脑网络嵌入双曲平面（双曲圆盘），利用几何扰动分数检测神经退行性疾病（如阿尔茨海默病）影响的脑区。相比标准图方法，该方法能更准确地识别受神经退行影响的区域。

## 激活关键词

- hyperbolic brain network
- hyperbolic embedding
- geometric perturbation score
- neurodegeneration detection
- Alzheimer brain connectivity
- hyperbolic disk
- 双曲嵌入
- 神经退行检测

## 核心原理

### 为什么使用双曲空间？

```
欧几里得空间                    双曲空间
┌─────────────────┐          ┌─────────────────┐
│ 线性距离        │          │ 指数增长空间    │
│ 网络嵌入受限    │          │ 天然适应层级结构│
│ 边权重失真      │          │ 连接性保持更好  │
└─────────────────┘          └─────────────────┘

双曲圆盘 (Poincaré Disk):
        ╭───────────────╮
      ╱   ·  ·  ·  ·  ·   ╲
     │  ·    节点位置     · │
     │ ·   (r, θ) 坐标   · │
     │  ·  ·  ·  ·  ·  ·  │
      ╲                  ╱
        ╰───────────────╯
```

### 核心方法：几何扰动分数

```python
def geometric_perturbation_score(G_original, G_perturbed, embedding):
    """
    计算几何扰动分数
    
    核心思想：测量扰动前后节点在双曲空间邻域的畸变程度
    """
    scores = {}
    
    for node in G_original.nodes():
        # 计算双曲空间中的邻域
        neighbors_orig = get_hyperbolic_neighbors(node, embedding, radius)
        neighbors_pert = get_hyperbolic_neighbors(node, embedding_perturbed, radius)
        
        # 计算几何畸变
        distortion = 0
        for neighbor in neighbors_orig:
            d_orig = hyperbolic_distance(node, neighbor, embedding)
            d_pert = hyperbolic_distance(node, neighbor, embedding_perturbed)
            
            # 相对距离变化
            distortion += abs(d_pert - d_orig) / d_orig
        
        # 归一化
        scores[node] = distortion / len(neighbors_orig)
    
    return scores
```

## 实现步骤

### 步骤 1：双曲嵌入

```python
import torch
import torch.nn as nn

class HyperbolicEmbedding(nn.Module):
    """
    将脑网络嵌入双曲圆盘
    """
    def __init__(self, n_nodes, dim=2):
        super().__init__()
        # 双曲空间中的坐标 (r, θ)
        # r: 径向距离 (0 到 1)
        # θ: 角度 (0 到 2π)
        self.radii = nn.Parameter(torch.rand(n_nodes) * 0.9 + 0.05)
        self.angles = nn.Parameter(torch.rand(n_nodes) * 2 * torch.pi)
    
    def hyperbolic_distance(self, i, j):
        """
        Poincaré 圆盘中的双曲距离
        """
        r_i, theta_i = self.radii[i], self.angles[i]
        r_j, theta_j = self.radii[j], self.angles[j]
        
        # 角度差
        delta_theta = torch.abs(theta_i - theta_j)
        delta_theta = torch.min(delta_theta, 2 * torch.pi - delta_theta)
        
        # 双曲距离公式
        # d = arccosh(1 + 2 * (r_i^2 + r_j^2 - 2*r_i*r_j*cos(Δθ)) / ((1-r_i^2)(1-r_j^2)))
        numerator = r_i**2 + r_j**2 - 2 * r_i * r_j * torch.cos(delta_theta)
        denominator = (1 - r_i**2) * (1 - r_j**2)
        
        arg = 1 + 2 * numerator / denominator
        return torch.arccosh(torch.clamp(arg, min=1.0))
    
    def forward(self, adj_matrix):
        """
        优化嵌入以匹配网络连接性
        """
        loss = 0
        n_nodes = len(self.radii)
        
        for i in range(n_nodes):
            for j in range(i + 1, n_nodes):
                if adj_matrix[i, j] > 0:
                    # 连接的节点应该距离近
                    dist = self.hyperbolic_distance(i, j)
                    loss += dist
                else:
                    # 不连接的节点应该距离远
                    dist = self.hyperbolic_distance(i, j)
                    loss += torch.exp(-dist)
        
        return loss
```

### 步骤 2：训练嵌入

```python
def train_hyperbolic_embedding(adj_matrix, epochs=500, lr=0.01):
    """
    训练双曲嵌入
    """
    n_nodes = adj_matrix.shape[0]
    model = HyperbolicEmbedding(n_nodes)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        loss = model(adj_matrix)
        loss.backward()
        optimizer.step()
        
        # 确保半径在有效范围内
        with torch.no_grad():
            model.radii.data.clamp_(0.01, 0.99)
    
    return model
```

### 步骤 3：计算扰动分数

```python
def compute_perturbation_scores(healthy_embeddings, patient_embeddings, radius=0.5):
    """
    计算每个脑区的几何扰动分数
    
    Args:
        healthy_embeddings: 健康组的嵌入（参考）
        patient_embeddings: 患者组的嵌入
        radius: 双曲空间邻域半径
    
    Returns:
        节点级扰动分数
    """
    n_nodes = len(healthy_embeddings.radii)
    scores = torch.zeros(n_nodes)
    
    for node in range(n_nodes):
        # 获取健康组中的邻域
        healthy_neighbors = []
        for other in range(n_nodes):
            if other != node:
                d = healthy_embeddings.hyperbolic_distance(node, other)
                if d < radius:
                    healthy_neighbors.append(other)
        
        # 计算距离畸变
        distortion = 0
        for neighbor in healthy_neighbors:
            d_healthy = healthy_embeddings.hyperbolic_distance(node, neighbor)
            d_patient = patient_embeddings.hyperbolic_distance(node, neighbor)
            
            # 相对变化
            distortion += torch.abs(d_patient - d_healthy) / (d_healthy + 1e-6)
        
        scores[node] = distortion / max(len(healthy_neighbors), 1)
    
    return scores
```

### 步骤 4：识别受影响区域

```python
def identify_affected_regions(scores, node_labels, threshold_percentile=95):
    """
    识别受神经退行影响最严重的脑区
    """
    threshold = torch.quantile(scores, threshold_percentile / 100)
    
    affected_regions = []
    for node, score in enumerate(scores):
        if score >= threshold:
            affected_regions.append({
                'node': node,
                'label': node_labels[node],
                'score': score.item()
            })
    
    # 按分数排序
    affected_regions.sort(key=lambda x: x['score'], reverse=True)
    
    return affected_regions
```

## 应用场景

1. **阿尔茨海默病检测** - 识别异常脑区
2. **疾病进展监测** - 跟踪几何分数变化
3. **生物标志物** - 潜在的诊断指标
4. **网络分析** - 理解脑网络的几何结构

## 验证数据集

论文使用以下数据验证：

| 数据类型 | 描述 |
|---------|------|
| DWI | 扩散加权成像（结构连接） |
| fMRI | 功能磁共振成像（功能连接） |
| AD 患者 | 阿尔茨海默病患者组 |
| 健康对照 | 健康参与者组 |

## 关键发现

- **记忆相关区域**：高扰动分数（海马、内嗅皮层）
- **额叶区域**：显著异常
- **多尺度一致性**：在不同脑分区尺度上结果稳健
- **优于标准图方法**：比图论方法更准确

## 相关技能

- `brain-higher-order-structures` - 脑高阶结构
- `weighted-brain-community-detection` - 加权脑社区检测
- `graph-laplacian-denoising` - 图拉普拉斯去噪
- `brain-chains-topological-alzheimer` - 阿尔茨海默拓扑链

## 工具使用

- `exec`：运行嵌入训练脚本
- `read`：检查网络数据和嵌入结果
- `write`：保存扰动分数分析

---

_此技能基于双曲几何嵌入方法，用于神经退行性疾病的脑网络分析_
## Description

Hyperbolic Brain Network Embedding for Neurodegeneration Detection

## Activation Keywords

- hyperbolic-brain-network-neurodegeneration
- hyperbolic-brain-network-neurodegeneration 技能
- hyperbolic-brain-network-neurodegeneration skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 阿尔茨海默病检测

### Step 2: 疾病进展监测

### Step 3: 生物标志物

### Step 4: 网络分析

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Hyperbolic Brain Network Embedding for Neurodegeneration Detection to my analysis.

**Agent:** I'll help you apply hyperbolic-brain-network-neurodegeneration. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for hyperbolic-brain-network-neurodegeneration?

**Agent:** Let me search for the latest research and best practices...
