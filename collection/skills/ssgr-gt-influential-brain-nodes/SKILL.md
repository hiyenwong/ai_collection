---
arxiv_id: 2409.11174v1
utility: 0.88
tags: [influential nodes, brain networks, self-supervised, graph transformer, multimodal fusion, rich-club]
created: 2026-03-31
---

# Self-Supervised Graph Transformer Brain Networks

## Activation Keywords

- 脑网络影响力节点
- I-nodes brain networks
- self-supervised graph transformer
- graph reconstruction brain
- rich-club brain connectivity
- multimodal brain fusion

## Problem Statement

脑网络影响力节点（I-nodes）识别的挑战：
- 传统方法依赖图论先验知识
- 可能忽视脑网络的内在特性
- 缺乏自监督学习方法
- 多模态融合困难

## Method Overview

Kang et al. (2024) 提出 SSGR-GT 框架：
1. 自监督图重建
2. Graph-Transformer 架构（局部+全局特征）
3. 多模态融合（功能+结构）
4. 影响力节点识别

## Tools Used

| Component | Function |
|-----------|----------|
| Graph-Transformer | Local + global features |
| Self-Supervised Learning | Data-driven representation |
| Graph Reconstruction | Node importance extraction |
| Multimodal Fusion | Functional + structural |

## Architecture

```
Brain Network (fMRI + DTI)
        ↓
┌─────────────────────────────┐
│   Graph-Transformer Encoder │
│   ┌─────────────────────┐   │
│   │ Local Attention     │   │
│   │ Global Attention    │   │
│   │ Position Encoding   │   │
│   └─────────────────────┘   │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│   Graph Reconstruction      │
│   (Self-Supervised)         │
└─────────────────────────────┘
        ↓
  Node Importance Scores
        ↓
  Influential Nodes (I-nodes)
```

## Key Findings

### I-nodes 分布

- 额上回
- 外侧顶叶
- 外侧枕叶
- 共识别 56 个 I-nodes

### I-nodes 特性

| 特性 | 发现 |
|------|------|
| 网络参与 | 涉及更多脑网络 |
| 纤维连接 | 更长的纤维束 |
| 连接位置 | 结构连接中心位置 |
| 节点效率 | 功能/结构网络高效 |
| Rich-club | 与结构/功能 rich-club 重叠 |

## Step-by-Step Instructions

### SSGR-GT 实现

1. **Graph-Transformer 编码器**
   ```python
   import torch
   import torch.nn as nn
   import torch.nn.functional as F
   
   class GraphTransformerLayer(nn.Module):
       def __init__(self, hidden_dim, num_heads=8):
           super().__init__()
           self.num_heads = num_heads
           self.head_dim = hidden_dim // num_heads
           
           # 多头注意力
           self.W_q = nn.Linear(hidden_dim, hidden_dim)
           self.W_k = nn.Linear(hidden_dim, hidden_dim)
           self.W_v = nn.Linear(hidden_dim, hidden_dim)
           
           # 局部 + 全局
           self.local_attn = nn.MultiheadAttention(hidden_dim, num_heads)
           self.global_attn = nn.MultiheadAttention(hidden_dim, num_heads)
           
           self.ffn = nn.Sequential(
               nn.Linear(hidden_dim, hidden_dim * 4),
               nn.GELU(),
               nn.Linear(hidden_dim * 4, hidden_dim)
           )
           
       def forward(self, x, adj_matrix):
           # x: (N, hidden_dim), adj_matrix: (N, N)
           N = x.shape[0]
           
           # 局部注意力（邻居）
           local_mask = (adj_matrix > 0).float()
           local_out, _ = self.local_attn(x, x, x, attn_mask=local_mask)
           
           # 全局注意力（所有节点）
           global_out, _ = self.global_attn(x, x, x)
           
           # 融合
           combined = local_out + global_out
           
           # FFN
           output = combined + self.ffn(combined)
           
           return output
   ```

2. **自监督图重建**
   ```python
   class SelfSupervisedGraphReconstruction(nn.Module):
       def __init__(self, input_dim, hidden_dim=256, num_layers=4):
           super().__init__()
           
           # 节点嵌入
           self.node_encoder = nn.Linear(input_dim, hidden_dim)
           
           # Graph-Transformer 层
           self.layers = nn.ModuleList([
               GraphTransformerLayer(hidden_dim) 
               for _ in range(num_layers)
           ])
           
           # 重建头
           self.edge_recon = nn.Sequential(
               nn.Linear(hidden_dim * 2, hidden_dim),
               nn.ReLU(),
               nn.Linear(hidden_dim, 1),
               nn.Sigmoid()
           )
           
       def forward(self, node_features, adj_matrix):
           # 编码
           h = self.node_encoder(node_features)
           
           for layer in self.layers:
               h = layer(h, adj_matrix)
           
           # 重建边
           N = h.shape[0]
           recon_adj = torch.zeros(N, N)
           
           for i in range(N):
               for j in range(i+1, N):
                   edge_feat = torch.cat([h[i], h[j]], dim=-1)
                   recon_adj[i, j] = self.edge_recon(edge_feat)
                   recon_adj[j, i] = recon_adj[i, j]
           
           return recon_adj, h
       
       def compute_node_importance(self, h, adj_matrix):
           """计算节点重要性分数"""
           N = h.shape[0]
           importance = torch.zeros(N)
           
           for i in range(N):
               # 节点 i 对重建的贡献
               neighbors = torch.where(adj_matrix[i] > 0)[0]
               
               contribution = 0
               for j in neighbors:
                   edge_feat = torch.cat([h[i], h[j]], dim=-1)
                   contribution += self.edge_recon(edge_feat)
               
               importance[i] = contribution / len(neighbors) if len(neighbors) > 0 else 0
           
           return importance
   ```

3. **多模态融合**
   ```python
   class MultimodalBrainFusion(nn.Module):
       def __init__(self, func_dim, struct_dim, hidden_dim=256):
           super().__init__()
           
           # 功能网络编码器
           self.func_encoder = SelfSupervisedGraphReconstruction(func_dim, hidden_dim)
           
           # 结构网络编码器
           self.struct_encoder = SelfSupervisedGraphReconstruction(struct_dim, hidden_dim)
           
           # 融合层
           self.fusion = nn.Sequential(
               nn.Linear(hidden_dim * 2, hidden_dim),
               nn.ReLU(),
               nn.Linear(hidden_dim, hidden_dim)
           )
           
       def forward(self, func_features, func_adj, struct_features, struct_adj):
           # 功能编码
           _, func_h = self.func_encoder(func_features, func_adj)
           
           # 结构编码
           _, struct_h = self.struct_encoder(struct_features, struct_adj)
           
           # 融合
           fused = self.fusion(torch.cat([func_h, struct_h], dim=-1))
           
           return fused
   ```

4. **训练与评估**
   ```python
   def train_ssgr_gt(model, func_data, struct_data, epochs=100):
       optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
       
       for epoch in range(epochs):
           optimizer.zero_grad()
           
           # 功能重建损失
           func_recon, func_h = model.func_encoder(
               func_data['features'], func_data['adj']
           )
           func_loss = F.binary_cross_entropy(
               func_recon, func_data['adj']
           )
           
           # 结构重建损失
           struct_recon, struct_h = model.struct_encoder(
               struct_data['features'], struct_data['adj']
           )
           struct_loss = F.binary_cross_entropy(
               struct_recon, struct_data['adj']
           )
           
           # 总损失
           loss = func_loss + struct_loss
           
           loss.backward()
           optimizer.step()
           
           if epoch % 10 == 0:
               print(f"Epoch {epoch}: Loss = {loss.item():.4f}")
       
       return model
   
   def identify_influential_nodes(model, func_data, struct_data, top_k=56):
       """识别影响力节点"""
       fused = model(
           func_data['features'], func_data['adj'],
           struct_data['features'], struct_data['adj']
       )
       
       # 计算节点重要性
       importance = model.compute_node_importance(fused, func_data['adj'])
       
       # 排序获取 top-k
       i_nodes = torch.argsort(importance, descending=True)[:top_k]
       
       return i_nodes.tolist(), importance.tolist()
   ```

## Example Usage

```python
# 加载多模态脑数据
func_data = load_fmri_connectivity()    # 功能连接
struct_data = load_dti_connectivity()   # 结构连接

# 创建模型
model = MultimodalBrainFusion(
    func_dim=100,   # 功能特征维度
    struct_dim=100  # 结构特征维度
)

# 训练
model = train_ssgr_gt(model, func_data, struct_data)

# 识别影响力节点
i_nodes, importance = identify_influential_nodes(model, func_data, struct_data)

print(f"Top 10 I-nodes: {i_nodes[:10]}")
```

## References

- Kang, Y. et al. (2024). Identifying Influential nodes in Brain Networks via Self-Supervised Graph-Transformer. arXiv:2409.11174.

## Related Skills

- dcho-higher-order-brain-connectivity
- brain-network-controllability
- multimodal-brain-connectivity-gnn