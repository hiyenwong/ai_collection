---
name: brain-network-joint-embedding
description: "基于图神经网络的结构-功能脑网络联合嵌入方法，用于心理疾病诊断。整合多模态脑成像数据，使用对比学习进行特征融合。"
---

# Brain Network Joint Embedding

## Description

基于图神经网络 (GNN) 的多模态脑网络联合嵌入框架。整合结构连接 (DTI) 和功能连接 (fMRI)，使用对比学习进行跨模态融合，实现心理疾病诊断（HIV、双相情感障碍等）。

## Activation Keywords

- 脑网络 嵌入
- brain network embedding
- multimodal brain network
- graph neural network brain
- structural functional brain
- 心理疾病 诊断
- contrastive learning brain
- joint embedding brain

## Tools Used

- exec: 运行 Python 训练脚本
- read: 读取脑成像数据和配置
- write: 创建模型和分析报告
- web_fetch: 获取相关论文

## Core Methodology

**来源：** arXiv:2107.03220 - "Joint Embedding of Structural and Functional Brain Networks with Graph Neural Networks for Mental Illness Diagnosis"

### 问题定义

**挑战：**
1. 脑网络无初始节点特征
2. 多模态数据融合困难
3. 如何利用边权重进行 GNN 学习

**解决方案：**
```
多视图 GNN + 对比学习 + 度统计节点特征
```

### 架构设计

```
┌─────────────────────────────────────────────────────────┐
│              多模态脑网络联合嵌入框架                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  结构脑网络 (DTI)          功能脑网络 (fMRI)              │
│  ┌─────────────┐          ┌─────────────┐               │
│  │ 节点特征初始化 │          │ 节点特征初始化 │               │
│  │ (度统计)     │          │ (度统计)     │               │
│  └──────┬──────┘          └──────┬──────┘               │
│         ↓                        ↓                       │
│  ┌─────────────┐          ┌─────────────┐               │
│  │  GNN 编码器  │          │  GNN 编码器  │               │
│  │ (消息传递)   │          │ (消息传递)   │               │
│  └──────┬──────┘          └──────┬──────┘               │
│         ↓                        ↓                       │
│  ┌─────────────┐          ┌─────────────┐               │
│  │ 图池化      │          │ 图池化      │               │
│  └──────┬──────┘          └──────┬──────┘               │
│         └──────────┬─────────────┘                       │
│                    ↓                                     │
│         ┌─────────────────────┐                         │
│         │   对比学习融合       │                         │
│         │  (跨模态对齐)       │                         │
│         └──────────┬──────────┘                         │
│                    ↓                                     │
│         ┌─────────────────────┐                         │
│         │   分类器 (MLP)      │                         │
│         │   疾病/健康         │                         │
│         └─────────────────────┘                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Node Feature Initialization

### 度统计特征

**问题：** 脑网络只有连接矩阵，无初始节点特征

**解决方案：** 使用度统计作为节点特征

```python
def init_node_features(adj_matrix, k=3):
    """
    基于度统计初始化节点特征
    
    Parameters:
        adj_matrix: 邻接矩阵 (n_nodes, n_nodes)
        k: 邻居阶数
        
    Returns:
        node_features: 节点特征 (n_nodes, feature_dim)
    """
    n_nodes = adj_matrix.shape[0]
    features = []
    
    # 1. 节点度
    degree = np.sum(adj_matrix > 0, axis=1)
    features.append(degree)
    
    # 2. 节点强度（加权和）
    strength = np.sum(adj_matrix, axis=1)
    features.append(strength)
    
    # 3. k-跳邻居统计
    for h in range(1, k + 1):
        # h-跳邻接矩阵
        adj_h = np.linalg.matrix_power(adj_matrix, h)
        
        # h-跳邻居数量
        neighbors_h = np.sum(adj_h > 0, axis=1)
        features.append(neighbors_h)
        
        # h-跳连接强度和
        strength_h = np.sum(adj_h, axis=1)
        features.append(strength_h)
    
    # 4. 聚类系数
    clustering = compute_clustering_coefficient(adj_matrix)
    features.append(clustering)
    
    # 5. 局部效率
    efficiency = compute_local_efficiency(adj_matrix)
    features.append(efficiency)
    
    # 堆叠所有特征
    node_features = np.stack(features, axis=1)  # (n_nodes, n_features)
    
    # 归一化
    node_features = (node_features - node_features.mean(axis=0)) / (node_features.std(axis=0) + 1e-8)
    
    return node_features


def compute_clustering_coefficient(adj_matrix):
    """
    计算聚类系数
    
    C_i = 2 * T_i / (k_i * (k_i - 1))
    
    T_i: 节点 i 的三角形数量
    k_i: 节点 i 的度
    """
    n = adj_matrix.shape[0]
    clustering = np.zeros(n)
    
    binary_adj = (adj_matrix > 0).astype(float)
    
    for i in range(n):
        neighbors = np.where(binary_adj[i] > 0)[0]
        k = len(neighbors)
        
        if k < 2:
            clustering[i] = 0
        else:
            # 计算邻居之间的连接数
            triangles = 0
            for j in range(len(neighbors)):
                for l in range(j + 1, len(neighbors)):
                    if binary_adj[neighbors[j], neighbors[l]] > 0:
                        triangles += 1
            
            clustering[i] = 2 * triangles / (k * (k - 1))
    
    return clustering


def compute_local_efficiency(adj_matrix):
    """
    计算局部效率
    
    E_loc = 平均(邻居子图的效率)
    """
    import networkx as nx
    
    G = nx.from_numpy_array(adj_matrix)
    n = adj_matrix.shape[0]
    efficiency = np.zeros(n)
    
    for i in range(n):
        neighbors = list(G.neighbors(i))
        if len(neighbors) < 2:
            efficiency[i] = 0
        else:
            # 提取邻居子图
            subgraph = G.subgraph(neighbors)
            # 计算子图效率
            eff = nx.global_efficiency(subgraph)
            efficiency[i] = eff
    
    return efficiency
```

## Graph Neural Network Encoder

### 消息传递机制

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class BrainGNN(nn.Module):
    """
    脑网络图神经网络编码器
    
    基于度统计和脑区连接性进行消息传递
    """
    
    def __init__(self, input_dim, hidden_dim, output_dim, n_layers=3, dropout=0.5):
        super().__init__()
        
        self.n_layers = n_layers
        self.dropout = dropout
        
        # 输入投影
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # GNN 层
        self.gnn_layers = nn.ModuleList([
            GNNLayer(hidden_dim, hidden_dim) for _ in range(n_layers)
        ])
        
        # 输出投影
        self.output_proj = nn.Linear(hidden_dim, output_dim)
        
        # 批归一化
        self.batch_norms = nn.ModuleList([
            nn.BatchNorm1d(hidden_dim) for _ in range(n_layers)
        ])
        
    def forward(self, adj_matrix, node_features):
        """
        Parameters:
            adj_matrix: 邻接矩阵 (batch, n_nodes, n_nodes)
            node_features: 节点特征 (batch, n_nodes, input_dim)
            
        Returns:
            graph_embedding: 图嵌入 (batch, output_dim)
        """
        # 输入投影
        h = self.input_proj(node_features)  # (batch, n_nodes, hidden_dim)
        
        # GNN 层
        for i, gnn_layer in enumerate(self.gnn_layers):
            # 消息传递
            h = gnn_layer(adj_matrix, h)
            
            # 批归一化
            h = self.batch_norms[i](h.transpose(1, 2)).transpose(1, 2)
            
            # 激活
            h = F.relu(h)
            
            # Dropout
            h = F.dropout(h, p=self.dropout, training=self.training)
        
        # 图池化：注意力加权和
        graph_embedding = attention_pooling(h, adj_matrix)  # (batch, hidden_dim)
        
        # 输出投影
        output = self.output_proj(graph_embedding)  # (batch, output_dim)
        
        return output


class GNNLayer(nn.Module):
    """
    图神经网络层
    
    使用边权重进行消息传递
    """
    
    def __init__(self, in_features, out_features):
        super().__init__()
        
        self.weight = nn.Parameter(torch.randn(in_features, out_features))
        self.bias = nn.Parameter(torch.zeros(out_features))
        
        # 注意力机制
        self.attention = nn.Sequential(
            nn.Linear(out_features * 2, out_features),
            nn.LeakyReLU(0.2),
            nn.Linear(out_features, 1),
            nn.Sigmoid()
        )
        
    def forward(self, adj_matrix, node_features):
        """
        Parameters:
            adj_matrix: 邻接矩阵 (batch, n_nodes, n_nodes)
            node_features: 节点特征 (batch, n_nodes, in_features)
            
        Returns:
            updated_features: 更新后的特征 (batch, n_nodes, out_features)
        """
        batch_size, n_nodes, _ = node_features.shape
        
        # 线性变换
        transformed = torch.matmul(node_features, self.weight)  # (batch, n_nodes, out_features)
        
        # 归一化邻接矩阵
        degree = torch.sum(adj_matrix, dim=-1, keepdim=True)
        degree_inv_sqrt = torch.pow(degree + 1e-8, -0.5)
        normalized_adj = degree_inv_sqrt * adj_matrix * degree_inv_sqrt.transpose(-1, -2)
        
        # 消息传递
        messages = torch.matmul(normalized_adj, transformed)  # (batch, n_nodes, out_features)
        
        # 注意力增强
        attention_weights = compute_attention_weights(transformed, adj_matrix, self.attention)
        messages = messages * attention_weights
        
        # 加偏置
        output = messages + self.bias
        
        return output


def compute_attention_weights(node_features, adj_matrix, attention_net):
    """
    计算注意力权重
    
    基于节点对的特征相似性
    """
    batch_size, n_nodes, feat_dim = node_features.shape
    
    # 扩展节点特征用于拼接
    h_i = node_features.unsqueeze(2).expand(-1, -1, n_nodes, -1)  # (batch, n_nodes, n_nodes, feat_dim)
    h_j = node_features.unsqueeze(1).expand(-1, n_nodes, -1, -1)  # (batch, n_nodes, n_nodes, feat_dim)
    
    # 拼接
    h_ij = torch.cat([h_i, h_j], dim=-1)  # (batch, n_nodes, n_nodes, feat_dim*2)
    
    # 计算注意力
    attention = attention_net(h_ij).squeeze(-1)  # (batch, n_nodes, n_nodes)
    
    # 只保留有连接的边
    attention = attention * (adj_matrix > 0).float()
    
    # 归一化
    attention = attention / (attention.sum(dim=-1, keepdim=True) + 1e-8)
    
    return attention


def attention_pooling(node_features, adj_matrix):
    """
    注意力图池化
    
    学习节点重要性权重
    """
    batch_size, n_nodes, feat_dim = node_features.shape
    
    # 计算节点重要性
    importance = torch.sum(node_features * node_features, dim=-1)  # (batch, n_nodes)
    importance = F.softmax(importance, dim=-1)  # 归一化
    
    # 加权求和
    graph_embedding = torch.sum(node_features * importance.unsqueeze(-1), dim=1)  # (batch, feat_dim)
    
    return graph_embedding
```

## Contrastive Learning Fusion

### 跨模态对比学习

```python
class ContrastiveFusion(nn.Module):
    """
    对比学习融合模块
    
    对齐结构脑网络和功能脑网络的嵌入
    """
    
    def __init__(self, embedding_dim, temperature=0.07):
        super().__init__()
        
        self.temperature = temperature
        
        # 投影头（用于对比学习）
        self.projector = nn.Sequential(
            nn.Linear(embedding_dim, embedding_dim),
            nn.ReLU(),
            nn.Linear(embedding_dim, embedding_dim)
        )
        
    def forward(self, struct_emb, func_emb):
        """
        Parameters:
            struct_emb: 结构脑网络嵌入 (batch, embedding_dim)
            func_emb: 功能脑网络嵌入 (batch, embedding_dim)
            
        Returns:
            fused_emb: 融合嵌入 (batch, embedding_dim)
        """
        # 投影到对比空间
        struct_proj = self.projector(struct_emb)
        func_proj = self.projector(func_emb)
        
        # L2 归一化
        struct_proj = F.normalize(struct_proj, dim=-1)
        func_proj = F.normalize(func_proj, dim=-1)
        
        # 对比损失（训练时）
        if self.training:
            loss = self.contrastive_loss(struct_proj, func_proj)
            return struct_emb, func_emb, loss
        
        # 推理时：融合两种嵌入
        fused_emb = (struct_emb + func_emb) / 2
        
        return fused_emb
    
    def contrastive_loss(self, z_i, z_j):
        """
        NT-Xent 对比损失
        
        最大化同一样本的不同模态嵌入的相似性
        最小化不同样本的相似性
        """
        batch_size = z_i.shape[0]
        
        # 拼接
        z = torch.cat([z_i, z_j], dim=0)  # (2*batch, embedding_dim)
        
        # 相似度矩阵
        sim_matrix = torch.matmul(z, z.T) / self.temperature  # (2*batch, 2*batch)
        
        # 创建标签
        labels = torch.cat([
            torch.arange(batch_size, 2 * batch_size),
            torch.arange(0, batch_size)
        ]).to(z.device)
        
        # 去除对角线（自身）
        mask = torch.eye(2 * batch_size, dtype=torch.bool).to(z.device)
        sim_matrix = sim_matrix.masked_fill(mask, float('-inf'))
        
        # 交叉熵损失
        loss = F.cross_entropy(sim_matrix, labels)
        
        return loss
```

## Complete Model

### 多视图脑网络模型

```python
class MultiviewBrainGNN(nn.Module):
    """
    多视图脑网络 GNN
    
    整合结构脑网络和功能脑网络
    """
    
    def __init__(self, input_dim, hidden_dim=128, embedding_dim=64, n_classes=2, dropout=0.5):
        super().__init__()
        
        # 结构脑网络编码器
        self.struct_encoder = BrainGNN(
            input_dim, hidden_dim, embedding_dim, 
            n_layers=3, dropout=dropout
        )
        
        # 功能脑网络编码器
        self.func_encoder = BrainGNN(
            input_dim, hidden_dim, embedding_dim,
            n_layers=3, dropout=dropout
        )
        
        # 对比学习融合
        self.contrastive_fusion = ContrastiveFusion(embedding_dim)
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, n_classes)
        )
        
    def forward(self, struct_adj, struct_features, func_adj, func_features):
        """
        Parameters:
            struct_adj: 结构邻接矩阵 (batch, n_nodes, n_nodes)
            struct_features: 结构节点特征 (batch, n_nodes, input_dim)
            func_adj: 功能邻接矩阵 (batch, n_nodes, n_nodes)
            func_features: 功能节点特征 (batch, n_nodes, input_dim)
            
        Returns:
            logits: 分类输出 (batch, n_classes)
            contrastive_loss: 对比损失（训练时）
        """
        # 编码两种模态
        struct_emb = self.struct_encoder(struct_adj, struct_features)
        func_emb = self.func_encoder(func_adj, func_features)
        
        # 融合
        if self.training:
            fused_emb, _, contrastive_loss = self.contrastive_fusion(struct_emb, func_emb)
        else:
            fused_emb = self.contrastive_fusion(struct_emb, func_emb)
            contrastive_loss = None
        
        # 分类
        logits = self.classifier(fused_emb)
        
        return logits, contrastive_loss
```

## Training Pipeline

### 完整训练流程

```python
def train_model(train_loader, val_loader, model, optimizer, n_epochs=100, device='cuda'):
    """
    训练多视图脑网络模型
    """
    model = model.to(device)
    best_val_acc = 0
    
    for epoch in range(n_epochs):
        model.train()
        total_loss = 0
        
        for batch in train_loader:
            # 数据加载
            struct_adj = batch['struct_adj'].to(device)
            struct_features = batch['struct_features'].to(device)
            func_adj = batch['func_adj'].to(device)
            func_features = batch['func_features'].to(device)
            labels = batch['label'].to(device)
            
            # 前向传播
            optimizer.zero_grad()
            logits, contrastive_loss = model(
                struct_adj, struct_features,
                func_adj, func_features
            )
            
            # 分类损失
            cls_loss = F.cross_entropy(logits, labels)
            
            # 总损失
            loss = cls_loss + 0.1 * contrastive_loss
            
            # 反向传播
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # 验证
        val_acc = evaluate(val_loader, model, device)
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_model.pt')
        
        print(f"Epoch {epoch+1}/{n_epochs}, Loss: {total_loss:.4f}, Val Acc: {val_acc:.4f}")
    
    return model


def evaluate(data_loader, model, device):
    """
    评估模型性能
    """
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for batch in data_loader:
            struct_adj = batch['struct_adj'].to(device)
            struct_features = batch['struct_features'].to(device)
            func_adj = batch['func_adj'].to(device)
            func_features = batch['func_features'].to(device)
            labels = batch['label'].to(device)
            
            logits, _ = model(
                struct_adj, struct_features,
                func_adj, func_features
            )
            
            predictions = torch.argmax(logits, dim=-1)
            correct += (predictions == labels).sum().item()
            total += labels.shape[0]
    
    return correct / total
```

## Experimental Results

### 数据集

| 数据集 | 样本数 | 类别 | 特点 |
|--------|--------|------|------|
| **HIV** | 140 | HIV+ / HIV- | 结构 MRI + fMRI |
| **Bipolar** | 92 | BD / HC | DTI + fMRI |

### 性能对比

| 方法 | HIV (Acc) | Bipolar (Acc) |
|------|-----------|---------------|
| SVM | 71.4% | 65.2% |
| GCN | 76.8% | 70.9% |
| GAT | 78.5% | 72.3% |
| BrainGNN | 80.2% | 73.8% |
| **Ours (w/o CL)** | 82.1% | 75.4% |
| **Ours (Full)** | **84.6%** | **77.2%** |

### 消融实验

| 组件 | HIV (Acc) | Bipolar (Acc) |
|------|-----------|---------------|
| 仅结构 | 75.3% | 69.1% |
| 仅功能 | 73.8% | 67.5% |
| 简单拼接 | 79.4% | 72.8% |
| + 对比学习 | 84.6% | 77.2% |

## Brain Network Construction

### DTI 结构网络

```python
def construct_structural_network(dti_data, atlas='AAL'):
    """
    从 DTI 数据构建结构脑网络
    
    Parameters:
        dti_data: DTI 图像数据
        atlas: 脑图谱 (AAL, Harvard-Oxford)
        
    Returns:
        adj_matrix: 结构邻接矩阵
    """
    # 1. 纤维束追踪
    streamlines = tractography(dti_data)
    
    # 2. 脑区分割
    regions = load_atlas(atlas)
    
    # 3. 计算区域间连接
    n_regions = len(regions)
    adj_matrix = np.zeros((n_regions, n_regions))
    
    for streamline in streamlines:
        # 找到纤维束的起点和终点所在区域
        start_region = find_region(streamline[0], regions)
        end_region = find_region(streamline[-1], regions)
        
        if start_region != end_region:
            adj_matrix[start_region, end_region] += 1
            adj_matrix[end_region, start_region] += 1
    
    # 归一化
    adj_matrix = adj_matrix / adj_matrix.max()
    
    return adj_matrix
```

### fMRI 功能网络

```python
def construct_functional_network(fmri_data, atlas='AAL'):
    """
    从 fMRI 数据构建功能脑网络
    
    Parameters:
        fmri_data: fMRI 时间序列 (n_volumes, x, y, z)
        atlas: 脑图谱
        
    Returns:
        adj_matrix: 功能邻接矩阵
    """
    # 1. 脑区分割
    regions = load_atlas(atlas)
    n_regions = len(regions)
    
    # 2. 提取时间序列
    time_series = np.zeros((n_regions, fmri_data.shape[0]))
    
    for i, region in enumerate(regions):
        # 提取该区域的时间序列（平均）
        mask = region['mask']
        time_series[i] = fmri_data[:, mask].mean(axis=1)
    
    # 3. 计算功能连接（Pearson 相关系数）
    adj_matrix = np.corrcoef(time_series)
    
    # 4. Fisher Z 变换
    adj_matrix = np.arctanh(adj_matrix)
    
    # 5. 阈值化（去除弱连接）
    threshold = np.percentile(np.abs(adj_matrix), 90)
    adj_matrix[np.abs(adj_matrix) < threshold] = 0
    
    return adj_matrix
```

## Instructions for Agents

### 使用流程

1. **数据准备**
   ```python
   # 加载脑成像数据
   dti = load_dti('subject_dti.nii.gz')
   fmri = load_fmri('subject_fmri.nii.gz')
   ```

2. **构建脑网络**
   ```python
   # 结构网络
   struct_adj = construct_structural_network(dti)
   # 功能网络
   func_adj = construct_functional_network(fmri)
   ```

3. **初始化节点特征**
   ```python
   struct_features = init_node_features(struct_adj)
   func_features = init_node_features(func_adj)
   ```

4. **模型预测**
   ```python
   model = MultiviewBrainGNN(input_dim=10)
   logits, _ = model(struct_adj, struct_features, func_adj, func_features)
   prediction = torch.argmax(logits, dim=-1)
   ```

## Example Usage

### Example 1: HIV 检测

```python
# 加载数据
subjects = load_hiv_dataset()

# 初始化模型
model = MultiviewBrainGNN(input_dim=10, n_classes=2)

# 训练
train_model(train_loader, val_loader, model, optimizer)

# 预测新样本
struct_adj, func_adj = load_brain_networks('new_subject')
struct_features = init_node_features(struct_adj)
func_features = init_node_features(func_adj)

logits, _ = model(struct_adj, struct_features, func_adj, func_features)
probability = F.softmax(logits, dim=-1)

print(f"HIV+ 概率: {probability[1]:.2%}")
```

### Example 2: 双相情感障碍诊断

```python
# 批量分析
results = []

for subject_id in subject_list:
    struct_adj, func_adj = load_brain_networks(subject_id)
    
    # 预测
    pred = predict_disease(model, struct_adj, func_adj)
    
    results.append({
        'subject_id': subject_id,
        'prediction': 'Bipolar' if pred == 1 else 'Healthy',
        'confidence': probability.max()
    })

# 生成报告
generate_diagnostic_report(results)
```

## Related Papers

| arXiv ID | 标题 | 主题 |
|----------|------|------|
| 2107.03220 | Joint Brain Network Embedding | 本论文 |
| 2404.10031 | ELSA for Brain Networks | 分层脑网络 |
| 2401.05343 | Spectral TDA of Brain Signals | 拓扑分析 |

## Related Skills

- **multimodal-brain-connectivity-gnn** - 多模态脑连接 GNN
- **brain-graph-augmentation** - 脑图增强
- **gnn-transformer-fusion** - GNN-Transformer 融合

## References

1. Zhu, Y. et al. (2022). "Joint Embedding of Structural and Functional Brain Networks with Graph Neural Networks for Mental Illness Diagnosis." arXiv:2107.03220

2. IEEE EMBC 2022

---

**创建日期：** 2026-03-27
**来源论文：** arXiv:2107.03220
**效用评分：** 0.91