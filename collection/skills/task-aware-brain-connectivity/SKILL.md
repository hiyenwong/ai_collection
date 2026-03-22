---
name: task-aware-brain-connectivity
description: 任务感知有效脑连接学习方法论（TBDS）。使用DAG学习框架从fMRI时间序列构建任务相关的脑网络，结合图神经网络进行下游预测任务。适用于fMRI分析、脑网络建模、精神疾病诊断预测。触发词：有效连接、脑网络、fMRI分析、DAG学习、图神经网络、task-aware connectivity、brain network、effective connectivity。
user-invocable: true
---

# 任务感知有效脑连接学习方法论（TBDS）

**来源论文：** arXiv:2211.00261 - Learning Task-Aware Effective Brain Connectivity for fMRI Analysis with Graph Neural Networks

## 核心方法论

TBDS（Task-aware Brain connectivity DAG Structure generation）是一个端到端框架，核心思想：

1. **DAG学习**：将原始时间序列转换为有向无环图结构
2. **任务感知**：连接性学习与下游任务联合优化
3. **对比正则化**：注入任务特定知识

### 方法架构

```
fMRI时间序列 → DAG学习模块 → 脑连接图 → GNN编码器 → 预测任务
                    ↑                    ↓
                对比正则化 ← 任务标签
```

## Python 实现

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, Optional
import numpy as np
from torch_geometric.nn import GCNConv, global_mean_pool
from torch_geometric.data import Data, Batch


class DAGLayer(nn.Module):
    """DAG学习层
    
    将时间序列转换为有向无环图结构
    """
    
    def __init__(self, n_rois: int, hidden_dim: int, temperature: float = 1.0):
        """
        Args:
            n_rois: ROI数量
            hidden_dim: 隐藏层维度
            temperature: Gumbel-Softmax温度
        """
        super().__init__()
        self.n_rois = n_rois
        self.temperature = temperature
        
        # 连接权重学习
        self.edge_encoder = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
        
        # 时间序列编码器
        self.temporal_encoder = nn.GRU(
            input_size=1,
            hidden_size=hidden_dim,
            batch_first=True,
            bidirectional=True
        )
        
        # DAG约束参数
        self.dag_constraint_weight = 1.0
        
    def encode_timeseries(self, x: torch.Tensor) -> torch.Tensor:
        """编码时间序列
        
        Args:
            x: (batch, n_rois, time_steps)
            
        Returns:
            (batch, n_rois, hidden_dim * 2)
        """
        batch_size, n_rois, time_steps = x.shape
        
        # 重塑为 (batch * n_rois, time_steps, 1)
        x_flat = x.view(-1, time_steps).unsqueeze(-1)
        
        # GRU编码
        _, h = self.temporal_encoder(x_flat)
        # h: (2, batch * n_rois, hidden_dim)
        
        h = h.transpose(0, 1).contiguous().view(batch_size, n_rois, -1)
        return h
        
    def compute_adjacency(self, h: torch.Tensor) -> torch.Tensor:
        """计算邻接矩阵
        
        Args:
            h: (batch, n_rois, hidden_dim)
            
        Returns:
            adj: (batch, n_rois, n_rois) 有向邻接矩阵
        """
        batch_size, n_rois, hidden_dim = h.shape
        
        # 创建节点对特征
        h_i = h.unsqueeze(2).expand(-1, -1, n_rois, -1)  # (batch, n_rois, n_rois, hidden)
        h_j = h.unsqueeze(1).expand(-1, n_rois, -1, -1)  # (batch, n_rois, n_rois, hidden)
        
        # 拼接特征
        h_ij = torch.cat([h_i, h_j], dim=-1)  # (batch, n_rois, n_rois, hidden * 2)
        
        # 计算边权重
        logits = self.edge_encoder(h_ij).squeeze(-1)  # (batch, n_rois, n_rois)
        
        # Gumbel-Softmax采样
        adj = torch.sigmoid(logits)
        
        return adj
        
    def dag_constraint(self, adj: torch.Tensor) -> torch.Tensor:
        """DAG约束损失
        
        基于矩阵指数的DAG约束：
        h(A) = trace(e^{A ○ A}) - n
        
        当h(A) = 0时，A是无环的
        """
        batch_size, n, _ = adj.shape
        
        # A ○ A (Hadamard product)
        adj_sq = adj * adj
        
        # 使用泰勒展开近似矩阵指数
        # exp(A) ≈ I + A + A²/2! + A³/3! + ...
        M = torch.eye(n, device=adj.device).unsqueeze(0).expand(batch_size, -1, -1)
        E = M.clone()
        
        for i in range(1, n):
            M = torch.bmm(M, adj_sq) / i
            E = E + M
            
        # h(A) = trace(E) - n
        h = torch.diagonal(E, dim1=1, dim2=2).sum(dim=1) - n
        
        return h.abs().mean()


class ContrastiveRegularization(nn.Module):
    """对比正则化模块
    
    拉近同类样本的连接模式，推远不同类样本
    """
    
    def __init__(self, temperature: float = 0.1):
        super().__init__()
        self.temperature = temperature
        
    def forward(self, embeddings: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        """
        Args:
            embeddings: (batch, hidden_dim) 图嵌入
            labels: (batch,) 类别标签
            
        Returns:
            对比损失
        """
        batch_size = embeddings.shape[0]
        
        # 归一化
        embeddings = F.normalize(embeddings, dim=1)
        
        # 计算相似度矩阵
        sim_matrix = torch.mm(embeddings, embeddings.t()) / self.temperature
        
        # 创建标签掩码
        labels = labels.view(-1, 1)
        mask = torch.eq(labels, labels.t()).float()
        
        # 移除对角线
        mask_diag = 1 - torch.eye(batch_size, device=embeddings.device)
        mask = mask * mask_diag
        
        # 计算对比损失
        exp_sim = torch.exp(sim_matrix) * mask_diag
        log_prob = sim_matrix - torch.log(exp_sim.sum(dim=1, keepdim=True))
        
        # 只考虑正样本对
        mean_log_prob = (mask * log_prob).sum(dim=1) / (mask.sum(dim=1) + 1e-6)
        
        loss = -mean_log_prob.mean()
        return loss


class BrainGNN(nn.Module):
    """脑网络图神经网络"""
    
    def __init__(self, input_dim: int, hidden_dim: int, n_classes: int, 
                 n_layers: int = 3):
        super().__init__()
        
        self.convs = nn.ModuleList()
        self.convs.append(GCNConv(input_dim, hidden_dim))
        
        for _ in range(n_layers - 1):
            self.convs.append(GCNConv(hidden_dim, hidden_dim))
            
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(hidden_dim, n_classes)
        )
        
    def forward(self, x: torch.Tensor, edge_index: torch.Tensor, 
                batch: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            x: 节点特征
            edge_index: 边索引 (2, n_edges)
            batch: 批次索引
            
        Returns:
            logits: 分类输出
            embeddings: 图嵌入
        """
        for conv in self.convs:
            x = F.relu(conv(x, edge_index))
            
        # 图池化
        embeddings = global_mean_pool(x, batch)
        
        # 分类
        logits = self.classifier(embeddings)
        
        return logits, embeddings


class TBDSModel(nn.Module):
    """TBDS完整模型"""
    
    def __init__(self, n_rois: int, time_steps: int, hidden_dim: int, 
                 n_classes: int, temperature: float = 1.0):
        super().__init__()
        
        self.dag_layer = DAGLayer(n_rois, hidden_dim, temperature)
        self.contrastive = ContrastiveRegularization()
        self.gnn = BrainGNN(hidden_dim * 2, hidden_dim, n_classes)
        
        # 损失权重
        self.alpha = 0.1  # DAG约束权重
        self.beta = 0.1   # 对比损失权重
        
    def forward(self, x: torch.Tensor, labels: torch.Tensor = None) -> dict:
        """
        Args:
            x: (batch, n_rois, time_steps) fMRI时间序列
            labels: (batch,) 类别标签
            
        Returns:
            包含logits、损失等的字典
        """
        batch_size, n_rois, time_steps = x.shape
        
        # 1. 时间序列编码
        h = self.dag_layer.encode_timeseries(x)  # (batch, n_rois, hidden_dim * 2)
        
        # 2. 学习DAG邻接矩阵
        adj = self.dag_layer.compute_adjacency(h[:, :, :h.shape[2]//2])
        
        # 3. 转换为图结构
        graphs = []
        for i in range(batch_size):
            edge_index = (adj[i] > 0.5).nonzero(as_tuple=False).t()
            graphs.append(Data(x=h[i], edge_index=edge_index))
            
        batch_graph = Batch.from_data_list(graphs)
        
        # 4. GNN前向传播
        logits, embeddings = self.gnn(batch_graph.x, batch_graph.edge_index, 
                                       batch_graph.batch)
        
        # 5. 计算损失
        losses = {}
        
        # 分类损失
        if labels is not None:
            losses['cls_loss'] = F.cross_entropy(logits, labels)
            
        # DAG约束损失
        losses['dag_loss'] = self.dag_layer.dag_constraint(adj)
        
        # 对比损失
        if labels is not None:
            losses['contrast_loss'] = self.contrastive(embeddings, labels)
            
        # 总损失
        total_loss = losses.get('cls_loss', 0) + \
                     self.alpha * losses['dag_loss'] + \
                     self.beta * losses.get('contrast_loss', 0)
        losses['total_loss'] = total_loss
        
        return {
            'logits': logits,
            'embeddings': embeddings,
            'adjacency': adj,
            'losses': losses
        }


def train_tbds(model: TBDSModel, train_loader, val_loader, 
               epochs: int = 100, lr: float = 1e-3, device: str = 'cuda'):
    """训练TBDS模型"""
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    best_val_acc = 0
    
    for epoch in range(epochs):
        model.train()
        train_loss = 0
        
        for batch_x, batch_y in train_loader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)
            
            optimizer.zero_grad()
            outputs = model(batch_x, batch_y)
            loss = outputs['losses']['total_loss']
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            
        # 验证
        model.eval()
        val_correct = 0
        val_total = 0
        
        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x = batch_x.to(device)
                batch_y = batch_y.to(device)
                
                outputs = model(batch_x, batch_y)
                pred = outputs['logits'].argmax(dim=1)
                val_correct += (pred == batch_y).sum().item()
                val_total += batch_y.size(0)
                
        val_acc = val_correct / val_total
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_tbds_model.pt')
            
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}/{epochs} - Train Loss: {train_loss:.4f}, Val Acc: {val_acc:.4f}")
            
    return model


# 使用示例
def example_usage():
    """示例：TBDS模型使用"""
    # 模拟数据
    batch_size = 8
    n_rois = 100  # 100个ROI
    time_steps = 200  # 200个时间点
    n_classes = 2
    
    # 创建模型
    model = TBDSModel(
        n_rois=n_rois,
        time_steps=time_steps,
        hidden_dim=64,
        n_classes=n_classes
    )
    
    # 模拟fMRI数据
    x = torch.randn(batch_size, n_rois, time_steps)
    labels = torch.randint(0, n_classes, (batch_size,))
    
    # 前向传播
    outputs = model(x, labels)
    
    print(f"Logits shape: {outputs['logits'].shape}")
    print(f"Adjacency shape: {outputs['adjacency'].shape}")
    print(f"Total loss: {outputs['losses']['total_loss'].item():.4f}")
    print(f"DAG constraint: {outputs['losses']['dag_loss'].item():.4f}")
    
    return model, outputs


if __name__ == "__main__":
    example_usage()
```

## 应用场景

1. **精神疾病诊断**
   - ADHD/Autism分类
   - 精神分裂症检测
   - 抑郁症预测

2. **认知任务分析**
   - 工作记忆负荷估计
   - 注意力状态识别
   - 执行功能评估

3. **脑发育研究**
   - 年龄预测
   - 发育异常检测
   - 脑成熟度评估

4. **神经影像分析**
   - fMRI连接组学
   - 多模态融合
   - 纵向研究

## 关键参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| hidden_dim | 64-128 | 隐藏层维度 |
| temperature | 1.0 | Gumbel-Softmax温度 |
| alpha | 0.1 | DAG约束权重 |
| beta | 0.1 | 对比损失权重 |
| n_layers | 3 | GNN层数 |

## 参考文献

- Yu, Y., et al. (2022). Learning Task-Aware Effective Brain Connectivity for fMRI Analysis with Graph Neural Networks.
- Zheng, X., et al. (2018). DAGs with NO TEARS: Continuous Optimization for Structure Learning.
- Kipf, T. N., & Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks.