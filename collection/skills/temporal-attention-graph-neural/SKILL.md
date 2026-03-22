---
name: temporal-attention-graph-neural
description: 时序注意力增强变分图循环神经网络（TAVRNN）用于神经动力学和行为建模。整合概率图学习与时序注意力机制，建模时变神经连接。支持单单元级别潜在动力学和群体级别可解释表示。触发词：神经动力学、时变连接、图神经网络、TAVRNN、神经群体、行为解码、neuronal dynamics、time-varying connectivity、graph neural network、temporal attention。
---

# Temporal Attention-enhanced Variational Graph RNN (TAVRNN)

## 核心方法论

TAVRNN框架用于学习时变神经连接及其与行为的关系：

### 1. 概率图学习
- **时变邻接矩阵**：A(t) 表示t时刻的神经连接
- **变分推断**：学习连接的概率分布
- **不确定性量化**：捕获连接估计的置信度

### 2. 时序注意力机制
- **跨时间依赖**：捕捉长程时间依赖
- **自注意力计算**：动态关注重要的历史时间点
- **多头注意力**：并行学习多种连接模式

### 3. 可解释表示
- **单单元动力学**：保留神经元级别的可解释性
- **群体级别模式**：识别与行为相关的连接模式
- **拓扑组织演化**：追踪网络结构的时变特性

## 实现代码示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GATConv, GCNConv
from torch_geometric.utils import dense_to_sparse

class TemporalAttention(nn.Module):
    """时序注意力模块"""
    
    def __init__(self, hidden_dim, num_heads=4, dropout=0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
        
        self.dropout = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(hidden_dim)
    
    def forward(self, x, mask=None):
        """
        Args:
            x: [batch, time, hidden_dim]
        Returns:
            attended: [batch, time, hidden_dim]
        """
        batch_size, seq_len, _ = x.shape
        
        # 多头投影
        Q = self.q_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim)
        K = self.k_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim)
        V = self.v_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim)
        
        # 转置以便计算注意力 [batch, heads, time, head_dim]
        Q = Q.transpose(1, 2)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)
        
        # 缩放点积注意力
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attn_weights = F.softmax(scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # 应用注意力
        attended = torch.matmul(attn_weights, V)
        attended = attended.transpose(1, 2).contiguous()
        attended = attended.view(batch_size, seq_len, self.hidden_dim)
        
        # 输出投影和残差连接
        output = self.out_proj(attended)
        return self.layer_norm(x + output)


class VariationalGraphLearner(nn.Module):
    """变分图学习器 - 学习时变邻接矩阵"""
    
    def __init__(self, num_nodes, hidden_dim, latent_dim):
        super().__init__()
        self.num_nodes = num_nodes
        
        # 图编码器
        self.encoder = nn.Sequential(
            nn.Linear(num_nodes, hidden_dim),
            nn.ELU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 均值和对数方差
        self.mu_layer = nn.Linear(hidden_dim, latent_dim)
        self.logvar_layer = nn.Linear(hidden_dim, latent_dim)
        
        # 图重构器
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ELU(),
            nn.Linear(hidden_dim, num_nodes)
        )
    
    def reparameterize(self, mu, logvar):
        """重参数化技巧"""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def forward(self, x, temperature=1.0):
        """
        Args:
            x: [batch, num_nodes, features] 节点特征
            temperature: Gumbel-Softmax温度
        Returns:
            adj_pred: 预测的邻接矩阵
            mu, logvar: 潜在分布参数
        """
        batch_size = x.shape[0]
        
        # 编码
        h = self.encoder(x)
        mu = self.mu_layer(h)
        logvar = self.logvar_layer(h)
        
        # 采样
        z = self.reparameterize(mu, logvar)
        
        # 重构邻接矩阵
        adj_logits = torch.bmm(
            self.decoder(z),
            self.decoder(z).transpose(1, 2)
        )
        
        # 使用温度缩放的sigmoid
        adj_pred = torch.sigmoid(adj_logits / temperature)
        
        return adj_pred, mu, logvar


class TAVRNN(nn.Module):
    """
    Temporal Attention-enhanced Variational Graph Recurrent Neural Network
    
    用于建模时变神经连接及其与行为的关系
    """
    
    def __init__(self, num_neurons, hidden_dim, latent_dim, num_heads=4, 
                 num_layers=2, behavior_dim=10, dropout=0.1):
        super().__init__()
        self.num_neurons = num_neurons
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim
        
        # 输入嵌入
        self.input_embed = nn.Linear(num_neurons, hidden_dim)
        
        # 变分图学习器
        self.graph_learner = VariationalGraphLearner(num_neurons, hidden_dim, latent_dim)
        
        # 图卷积层
        self.gcn_layers = nn.ModuleList([
            GCNConv(hidden_dim, hidden_dim) for _ in range(num_layers)
        ])
        
        # 时序注意力
        self.temporal_attention = TemporalAttention(hidden_dim, num_heads, dropout)
        
        # GRU用于时序建模
        self.gru = nn.GRU(hidden_dim, hidden_dim, batch_first=True)
        
        # 行为预测头
        self.behavior_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, behavior_dim)
        )
        
        # 分类头（用于聚类任务）
        self.classify_head = nn.Linear(hidden_dim, 2)
    
    def forward(self, x_sequence, return_graphs=True):
        """
        Args:
            x_sequence: [batch, time, num_neurons, features] 神经活动序列
            return_graphs: 是否返回学习的图结构
        
        Returns:
            behavior_pred: 行为预测
            classify_logits: 分类logits
            graphs: (可选) 学习的图序列
            kl_loss: KL散度损失
        """
        batch_size, seq_len, num_neurons, features = x_sequence.shape
        
        # 对每个时间步学习图结构
        graphs = []
        kl_losses = []
        hidden_states = []
        
        for t in range(seq_len):
            x_t = x_sequence[:, t, :, 0]  # [batch, num_neurons]
            
            # 学习时变邻接矩阵
            adj_t, mu, logvar = self.graph_learner(x_t)
            
            # KL散度
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            kl_losses.append(kl_loss)
            
            if return_graphs:
                graphs.append(adj_t)
            
            # 图卷积
            h = self.input_embed(x_t)
            edge_index, edge_weight = dense_to_sparse(adj_t)
            
            for gcn in self.gcn_layers:
                h = F.elu(gcn(h, edge_index, edge_weight))
            
            hidden_states.append(h)
        
        # 堆叠时序表示
        hidden_sequence = torch.stack(hidden_states, dim=1)  # [batch, time, hidden_dim]
        
        # 时序注意力
        attended = self.temporal_attention(hidden_sequence)
        
        # GRU建模
        gru_out, _ = self.gru(attended)
        
        # 最终表示
        final_hidden = gru_out[:, -1, :]  # [batch, hidden_dim]
        
        # 预测
        behavior_pred = self.behavior_head(final_hidden)
        classify_logits = self.classify_head(final_hidden)
        
        outputs = {
            'behavior_pred': behavior_pred,
            'classify_logits': classify_logits,
            'kl_loss': torch.stack(kl_losses).mean()
        }
        
        if return_graphs:
            outputs['graphs'] = graphs
        
        return outputs


def train_tavrnn_example():
    """TAVRNN训练示例"""
    # 模拟参数
    num_neurons = 100
    seq_len = 50
    batch_size = 32
    hidden_dim = 64
    latent_dim = 32
    
    # 创建模型
    model = TAVRNN(
        num_neurons=num_neurons,
        hidden_dim=hidden_dim,
        latent_dim=latent_dim
    )
    
    # 模拟数据
    x = torch.randn(batch_size, seq_len, num_neurons, 1)
    behavior_labels = torch.randn(batch_size, 10)
    class_labels = torch.randint(0, 2, (batch_size,))
    
    # 前向传播
    outputs = model(x)
    
    # 计算损失
    behavior_loss = F.mse_loss(outputs['behavior_pred'], behavior_labels)
    classify_loss = F.cross_entropy(outputs['classify_logits'], class_labels)
    kl_loss = outputs['kl_loss']
    
    total_loss = behavior_loss + classify_loss + 0.01 * kl_loss
    
    print(f"Total Loss: {total_loss.item():.4f}")
    print(f"Behavior Loss: {behavior_loss.item():.4f}")
    print(f"Classify Loss: {classify_loss.item():.4f}")
    print(f"KL Loss: {kl_loss.item():.4f}")
    
    return model, outputs


if __name__ == "__main__":
    model, outputs = train_tavrnn_example()
    print(f"Learned {len(outputs['graphs'])} time-varying graphs")
```

## 应用场景

1. **神经动力学分析**
   - 自由行为动物的神经记录分析
   - 运动任务中的神经群体解码
   - 学习过程的网络演化追踪

2. **脑机接口**
   - 时变连接模式解码
   - 自适应神经信号处理
   - 行为意图预测

3. **神经科学发现**
   - 识别行为相关的关键连接
   - 揭示网络拓扑的动态重组
   - 跨模态神经数据分析

## 验证数据集

- 大鼠自由行为电生理数据
- 灵长类感觉运动皮层记录
- DishBrain平台生物神经元数据

## 参考文献

- arXiv:2410.00665 - Graph-Based Representation Learning of Neuronal Dynamics and Behavior