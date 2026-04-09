# HOGANN - High-Order Graph Attention for Marijuana Brain Networks

**来源论文：** arXiv:2403.00033 - Spatial Craving Patterns in Marijuana Users: Insights from fMRI Brain Connectivity Analysis with High-Order Graph Attention Neural Networks
**效用评分：** 0.99
**创建时间：** 2026-03-24 08:54

---

## 概述

HOGANN（高阶图注意力神经网络）用于分析大麻使用者的脑网络异常活动，结合 GAT-LSTM 捕捉时序网络动力学，使用高阶注意力模块进行信息融合和消息传递。

## 激活关键词

- HOGANN
- high-order graph attention
- marijuana brain network
- craving pattern detection
- GAT-LSTM
- brain community analysis
- 大麻脑网络
- 高阶图注意力

## 核心架构

```
┌──────────────────────────────────────────────────────────┐
│              HOGANN 架构                              │
│                                                            │
│  ┌─────────────┐    ┌──────────────────┐    ┌─────────────────┐ │
│  │ fMRI 数据     │ →  │ 功能脑网络      │ →  │ GAT-LSTM      │ │
│  │ (时间序列）  │    │ (动态构建）      │    │ (时序建模）   │ │
│  └─────────────┘    └──────────────────┘    └─────────────────┘ │
│                            │                        │                │
│                            ↓                        ↓                ↓
│                      ┌─────────────────────────────────────┐          │
│                      │  高阶注意力模块（HOM）           │          │
│                      │ - 邻域信息融合                │          │
│                      │ - 多跳消息传递                │          │
│                      │ - 超图构建                   │          │
│                      └─────────────────────────────────────┘          │
│                                     │                                │
│                                     ↓                                │
│                      ┌─────────────────────────────────────┐          │
│                      │ 社区检测 + 分类                │          │
│                      │ - 异常子网络识别              │          │
│                      │ - 渴望脑图绘制              │          │
│                      └─────────────────────────────────────┘          │
└──────────────────────────────────────────────────────────┘
```

## 核心组件

### 1. 动态脑网络构建

```python
import numpy as np
import torch
import torch.nn as nn

class DynamicBrainNetwork:
    """
    从 fMRI 时序数据构建动态脑网络
    """
    def __init__(self, n_rois, window_size=10):
        self.n_rois = n_rois
        self.window_size = window_size
        
        # 相关性矩阵窗口
        self.correlation_window = []
    
    def compute_static_network(self, fmri_window):
        """
        计算静态功能连接网络
        """
        # Pearson 相关性
        fmri_centered = fmri_window - fmri_window.mean(axis=0)
        cov = np.dot(fmri_centered.T, fmri_centered)
        std = np.std(fmri_window, axis=0, keepdims=True)
        corr = cov / (std.T * std + 1e-6)
        
        return np.abs(corr)  # 取绝对值作为连接强度
    
    def build_dynamic_networks(self, fmri_series):
        """
        构建时序网络序列
        """
        networks = []
        
        for t in range(self.window_size, len(fmri_series)):
            window = fmri_series[t-self.window_size:t]
            network = self.compute_static_network(window)
            networks.append(network)
        
        return np.array(networks)
```

### 2. 图注意力 LSTM

```python
class GraphAttentionLSTM(nn.Module):
    """
    GAT-LSTM：捕捉图上的时序动力学
    """
    def __init__(self, node_dim, hidden_dim, n_heads=4):
        super().__init__()
        self.node_dim = node_dim
        self.hidden_dim = hidden_dim
        
        # 图注意力层
        self.gat = GATLayer(node_dim, hidden_dim, n_heads)
        
        # LSTM 处理时序
        self.lstm = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=2,
            batch_first=True
        )
    
    def forward(self, node_features, adj_matrix_sequence):
        """
        Args:
            node_features: [batch, n_nodes, node_dim]
            adj_matrix_sequence: [batch, n_time, n_nodes, n_nodes]
        """
        batch_size, n_time = adj_matrix_sequence.shape[:2]
        
        # 时序图注意力编码
        hiddens = []
        for t in range(n_time):
            # 当前时间步的图注意力
            attn_output = self.gat(
                node_features, 
                adj_matrix_sequence[:, t]
            )
            hiddens.append(attn_output)
        
        hiddens = torch.stack(hiddens, dim=1)  # [batch, n_time, n_nodes, hidden_dim]
        
        # LSTM 时序建模
        lstm_out, (h_n, c_n) = self.lstm(hiddens)
        
        return lstm_out, (h_n, c_n)

class GATLayer(nn.Module):
    """
    图注意力层
    """
    def __init__(self, in_dim, out_dim, n_heads=4):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = out_dim // n_heads
        
        # 注意力权重参数
        self.W_q = nn.Linear(in_dim, n_heads * self.head_dim)
        self.W_k = nn.Linear(in_dim, n_heads * self.head_dim)
        self.W_v = nn.Linear(in_dim, n_heads * self.head_dim)
        
        # 输出变换
        self.W_o = nn.Linear(n_heads * self.head_dim, out_dim)
    
    def forward(self, x, adj):
        """
        Args:
            x: [batch, n_nodes, in_dim]
            adj: [batch, n_nodes, n_nodes]
        """
        batch_size, n_nodes, _ = x.shape
        
        # 计算注意力
        Q = self.W_q(x).view(batch_size, n_nodes, self.n_heads, self.head_dim)
        K = self.W_k(x).view(batch_size, n_nodes, self.n_heads, self.head_dim)
        V = self.W_v(x).view(batch_size, n_nodes, self.n_heads, self.head_dim)
        
        # 注意力分数
        scores = torch.matmul(Q, K.transpose(-2, -1)) / np.sqrt(self.head_dim)
        
        # 掩码处理
        mask = adj.unsqueeze(1).unsqueeze(1).expand_as(scores)
        scores = scores.masked_fill(mask == 0, -1e9)
        
        # Softmax 注意力
        attn_weights = torch.softmax(scores, dim=-1)
        
        # 加权聚合
        output = torch.matmul(attn_weights, V)
        output = output.transpose(1, 2).contiguous()
        output = output.view(batch_size, n_nodes, -1)
        
        # 输出变换
        return self.W_o(output)
```

### 3. 高阶注意力模块（HOM）

```python
class HighOrderAttention(nn.Module):
    """
    高阶注意力模块：多跳信息融合和超图构建
    """
    def __init__(self, node_dim, hidden_dim, order=3):
        super().__init__()
        self.order = order
        self.W_self = nn.Linear(node_dim, hidden_dim)
        self.W_neighbor = nn.Linear(node_dim, hidden_dim)
        self.W_higher = nn.Linear(node_dim * order, hidden_dim)
        
        self.attention = nn.MultiheadAttention(hidden_dim, num_heads=4)
        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.ReLU(),
            nn.Linear(hidden_dim * 4, hidden_dim)
        )
    
    def forward(self, node_features, adj_matrix):
        """
        高阶注意力计算
        """
        # 自特征
        h_self = self.W_self(node_features)
        
        # 一跳邻居
        one_hop = torch.matmul(adj_matrix, node_features)
        h_1hop = self.W_neighbor(one_hop)
        
        # 高跳特征（二阶、三阶等）
        higher_features = []
        for k in range(2, self.order + 1):
            higher_order_adj = torch.matrix_power(adj_matrix, k)
            higher_hop = torch.matmul(higher_order_adj, node_features)
            higher_features.append(higher_hop)
        
        h_higher = torch.cat(higher_features, dim=-1)
        h_higher = self.W_higher(h_higher)
        
        # 融合所有阶的特征
        h_combined = h_self + h_1hop + h_higher
        
        # 多头注意力
        h_attended, _ = self.attention(
            h_combined.unsqueeze(1),
            h_combined.unsqueeze(1)
        )
        
        # 前馈网络
        output = self.ffn(h_attended.squeeze(1))
        
        return output

def torch_matrix_power(adj, k):
    """
    矩阵的 k 次幂
    """
    result = torch.eye(adj.size(0), device=adj.device)
    power = adj.clone()
    
    for _ in range(k):
        result = torch.matmul(result, power)
    
    return result
```

### 4. 渴望脑图识别

```python
class CravingBrainMap(nn.Module):
    """
    识别与渴望相关的脑区
    """
    def __init__(self, node_dim, hidden_dim, n_classes=2):
        super().__init__()
        self.gat_lstm = GraphAttentionLSTM(node_dim, hidden_dim)
        self.high_order = HighOrderAttention(hidden_dim, hidden_dim)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, n_classes)
        )
        
    def forward(self, node_features, adj_sequence):
        # 时序图注意力
        lstm_out, _ = self.gat_lstm(node_features, adj_sequence)
        
        # 高阶注意力（使用最后一个时间步）
        last_adj = adj_sequence[:, -1]
        ho_output = self.high_order(lstm_out[:, -1], last_adj)
        
        # 分类
        logits = self.classifier(ho_output)
        
        return logits, ho_output

def identify_abnormal_communities(adj_matrix, model, threshold=2.0):
    """
    识别异常活跃的脑区社区
    """
    with torch.no_grad():
        # 获取每个节点的特征表示
        node_embeddings = model.high_order(
            torch.eye(adj_matrix.size(0)),
            adj_matrix
        )
        
        # 计算节点重要性（注意力权重）
        node_importance = node_embeddings.abs().sum(dim=-1)
        
        # 高重要性节点
        abnormal_nodes = torch.where(
            node_importance > threshold * node_importance.mean()
        )[0]
        
        # 子网络提取
        subnetwork = adj_matrix[abnormal_nodes][:, abnormal_nodes]
        
        return {
            'abnormal_nodes': abnormal_nodes.numpy(),
            'node_importance': node_importance.numpy(),
            'subnetwork': subnetwork.numpy()
        }
```

## 实现步骤

### 步骤 1：数据准备

```python
def prepare_fmri_data(fmri_dataset, atlas_labels):
    """
    准备 fMRI 脑网络数据
    
    Args:
        fmri_dataset: [n_subjects, n_timepoints, n_rois]
        atlas_labels: ROI 标签列表
    """
    data = []
    labels = []
    
    for subject in range(len(fmri_dataset)):
        # 构建动态网络
        net_builder = DynamicBrainNetwork(
            n_rois=fmri_dataset.shape[2],
            window_size=10
        )
        dynamic_networks = net_builder.build_dynamic_networks(
            fmri_dataset[subject]
        )
        
        # 特征工程
        node_features = extract_node_features(dynamic_networks)
        
        data.append({
            'dynamic_networks': dynamic_networks,
            'node_features': node_features,
            'subject_id': subject
        })
        
        # 标签（大麻使用者 vs 对照组）
        labels.append(get_subject_label(subject))
    
    return data, np.array(labels), atlas_labels

def extract_node_features(networks):
    """
    从时序网络提取节点特征
    """
    # 度中心性
    degrees = np.array([np.sum(net) for net in networks])
    
    # 介数中心性
    betweenness = np.array([compute_betweenness(net) for net in networks])
    
    # 聚类系数
    clustering = np.array([compute_clustering(net) for net in networks])
    
    return np.stack([degrees, betweenness, clustering], axis=-1)
```

### 步骤 2：模型训练

```python
def train_hogann(model, dataloader, epochs=100, lr=1e-4):
    """
    训练 HOGANN 模型
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        
        for batch in dataloader:
            node_features = batch['node_features']
            adj_sequence = batch['dynamic_networks']
            labels = batch['labels']
            
            # 前向传播
            logits, ho_features = model(node_features, adj_sequence)
            
            # 计算损失
            loss = criterion(logits, labels)
            
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # 统计
            total_loss += loss.item()
            _, predicted = torch.max(logits, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
        
        acc = 100.0 * correct / total
        print(f"Epoch {epoch}: Loss={total_loss/len(dataloader):.4f}, Acc={acc:.2f}%")
```

### 步骤 3：渴望脑图可视化

```python
def visualize_craving_brain_map(model, fmri_data, atlas_coords, save_path):
    """
    可视化渴望脑图
    """
    # 识别异常社区
    abnormal = identify_abnormal_communities(fmri_data, model)
    
    # 创建脑图可视化
    fig = go.Figure()
    
    # 绘制脑区节点
    fig.add_trace(go.Scatter3d(
        x=atlas_coords[:, 0],
        y=atlas_coords[:, 1],
        z=atlas_coords[:, 2],
        mode='markers',
        marker=dict(
            size=abnormal['node_importance'] * 10,
            color=abnormal['node_importance'],
            colorscale='Viridis',
            showscale=True
        ),
        name='Brain Regions'
    ))
    
    # 绘制异常连接
    for i in range(len(abnormal['abnormal_nodes'])):
        for j in range(i + 1, len(abnormal['abnormal_nodes'])):
            if abnormal['subnetwork'][i, j] > 0:
                idx_i = abnormal['abnormal_nodes'][i]
                idx_j = abnormal['abnormal_nodes'][j]
                fig.add_trace(go.Scatter3d(
                    x=[atlas_coords[idx_i, 0], atlas_coords[idx_j, 0]],
                    y=[atlas_coords[idx_i, 1], atlas_coords[idx_j, 1]],
                    z=[atlas_coords[idx_i, 2], atlas_coords[idx_j, 2]],
                    mode='lines',
                    line=dict(width=2, color='red'),
                    showlegend=False
                ))
    
    fig.update_layout(
        title='Craving Brain Map',
        scene=dict(
            xaxis=dict(title='X (mm)'),
            yaxis=dict(title='Y (mm)'),
            zaxis=dict(title='Z (mm)')
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    
    fig.write_html(save_path)
```

## 应用场景

1. **成瘾脑网络分析** - 大麻等物质使用影响
2. **渴望模式检测** - 识别 craving 相关脑区
3. **功能连接异常** - 检测网络功能异常
4. **认知影响评估** - 评估对注意力和额叶的影响

## 验证数据集

论文在两个独立队列上验证：
- **队列 1**：短依赖大麻使用者
- **队列 2**：长期依赖大麻使用者
- **对照组**：健康参与者

## 关键发现

- **分类准确性**：显著优于基准算法
- **关键脑区**：背侧注意网络、额顶叶网络
- **依赖时长影响**：长期依赖导致更明显的网络改变
- **渴望脑图**：成功绘制 craving 相关脑区

## 相关技能

- `multimodal-brain-connectivity-gnn` - 多模态脑连接
- `weighted-brain-community-detection` - 加权脑社区检测
- `social-exclusion-brain-dynamics` - 社会排除脑动力学
- `gnn-transformer-fusion` - GNN Transformer 融合

---

_此技能基于 HOGANN 方法，用于分析大麻使用者的脑网络渴望模式_
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- hogann-marijuana-brain-network
- hogann-marijuana-brain-network 技能
- hogann-marijuana-brain-network skill

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

**User:** How can I apply hogann-marijuana-brain-network?

**Agent:** I'll help you understand and apply hogann-marijuana-brain-network...

### Example 2: Advanced Application

**User:** What are the key considerations for hogann-marijuana-brain-network?

**Agent:** Let me search for the latest research and best practices...
