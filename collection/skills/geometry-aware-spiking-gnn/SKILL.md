---
name: geometry-aware-spiking-gnn
description: 几何感知脉冲图神经网络方法论。在黎曼流形上统一脉冲神经动力学与自适应表示学习，支持曲率感知的图学习。触发词：脉冲神经网络、图神经网络、黎曼流形、曲率感知、能量效率、spiking neural network、graph neural network、Riemannian manifold、curvature-aware、GSG。
user-invocable: true
---

# Geometry-Aware Spiking Graph Neural Network (GSG)

将脉冲神经网络与黎曼流形上的自适应表示学习统一，实现曲率感知、能量高效的图学习。

## 核心方法论

### 1. 黎曼嵌入层

```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, Optional

class ManifoldType:
    """流形类型枚举"""
    EUCLIDEAN = 'euclidean'
    SPHERICAL = 'spherical'
    HYPERBOLIC = 'hyperbolic'

class ConstantCurvatureManifold:
    """常曲率流形基类"""
    
    def __init__(self, dim: int, curvature: float = 0.0):
        self.dim = dim
        self.curvature = curvature  # K > 0: 球面, K < 0: 双曲, K = 0: 欧几里得
        
    def exp_map(self, v: torch.Tensor, base: torch.Tensor) -> torch.Tensor:
        """指数映射：将切空间向量映射到流形"""
        if self.curvature == 0:
            return base + v
        
        norm_v = torch.norm(v, dim=-1, keepdim=True)
        
        if self.curvature > 0:  # 球面
            sqrt_K = np.sqrt(self.curvature)
            return (torch.cos(sqrt_K * norm_v) * base + 
                    torch.sin(sqrt_K * norm_v) * v / (sqrt_K * norm_v + 1e-8))
        else:  # 双曲
            sqrt_neg_K = np.sqrt(-self.curvature)
            return (torch.cosh(sqrt_neg_K * norm_v) * base + 
                    torch.sinh(sqrt_neg_K * norm_v) * v / (sqrt_neg_K * norm_v + 1e-8))
    
    def log_map(self, x: torch.Tensor, base: torch.Tensor) -> torch.Tensor:
        """对数映射：将流形点映射到切空间"""
        if self.curvature == 0:
            return x - base
        
        # 计算距离
        dist = self.distance(x, base)
        
        if self.curvature > 0:
            sqrt_K = np.sqrt(self.curvature)
            return dist * (x - torch.cos(sqrt_K * dist) * base) / (torch.sin(sqrt_K * dist) + 1e-8)
        else:
            sqrt_neg_K = np.sqrt(-self.curvature)
            return dist * (x - torch.cosh(sqrt_neg_K * dist) * base) / (torch.sinh(sqrt_neg_K * dist) + 1e-8)
    
    def distance(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """测地距离"""
        if self.curvature == 0:
            return torch.norm(x - y, dim=-1)
        
        inner = torch.sum(x * y, dim=-1)
        
        if self.curvature > 0:
            return torch.arccos(torch.clamp(inner, -1, 1)) / np.sqrt(self.curvature)
        else:
            return torch.arccosh(torch.clamp(inner, 1, 1e8)) / np.sqrt(-self.curvature)


class RiemannianEmbeddingLayer(nn.Module):
    """黎曼嵌入层
    
    将节点特征投影到常曲率流形池
    """
    
    def __init__(
        self,
        in_features: int,
        out_features: int,
        manifold_types: list = ['euclidean', 'hyperbolic', 'spherical']
    ):
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        
        # 创建流形池
        self.manifolds = nn.ModuleList()
        self.manifold_weights = nn.Parameter(torch.ones(len(manifold_types)))
        
        curvatures = {
            'euclidean': 0.0,
            'spherical': 1.0,
            'hyperbolic': -1.0
        }
        
        for mtype in manifold_types:
            manifold = ConstantCurvatureManifold(out_features, curvatures[mtype])
            self.manifolds.append(manifold)
        
        # 投影权重
        self.projections = nn.ModuleList([
            nn.Linear(in_features, out_features, bias=False)
            for _ in manifold_types
        ])
        
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """前向传播
        
        Returns:
            embedding: 混合流形嵌入
            weights: 流形权重
        """
        batch_size = x.size(0)
        
        # 计算流形权重
        weights = F.softmax(self.manifold_weights, dim=0)
        
        # 各流形投影
        embeddings = []
        for proj, manifold in zip(self.projections, self.manifolds):
            v = proj(x)
            # 投影到流形
            if manifold.curvature == 0:
                emb = v
            else:
                # 从原点指数映射
                emb = manifold.exp_map(v, torch.zeros_like(v))
            embeddings.append(emb)
        
        # 加权组合
        embeddings = torch.stack(embeddings, dim=0)  # (n_manifolds, batch, dim)
        weights = weights.view(-1, 1, 1)
        combined = (embeddings * weights).sum(dim=0)
        
        return combined, weights
```

### 2. 流形脉冲层

```python
class ManifoldSpikingNeuron(nn.Module):
    """流形上的脉冲神经元
    
    在弯曲空间中建模膜电位演化
    """
    
    def __init__(
        self,
        dim: int,
        threshold: float = 1.0,
        decay: float = 0.9,
        reset_mechanism: str = 'subtract'
    ):
        super().__init__()
        
        self.dim = dim
        self.threshold = threshold
        self.decay = decay
        self.reset_mechanism = reset_mechanism
        
        # 可学习参数
        self.membrane_decay = nn.Parameter(torch.tensor(decay))
        self.threshold_param = nn.Parameter(torch.tensor(threshold))
        
    def forward(
        self,
        x: torch.Tensor,
        membrane_potential: torch.Tensor,
        manifold: Optional[ConstantCurvatureManifold] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """脉冲神经元前向传播
        
        Args:
            x: 输入电流
            membrane_potential: 当前膜电位
            manifold: 所在流形（可选）
            
        Returns:
            spike: 输出脉冲
            new_membrane: 更新后的膜电位
        """
        # 膜电位衰减
        membrane_potential = membrane_potential * torch.sigmoid(self.membrane_decay)
        
        # 积分输入
        if manifold is not None and manifold.curvature != 0:
            # 在流形上积分（使用测地线方向）
            # 简化实现：切空间投影
            v = manifold.log_map(x, membrane_potential)
            membrane_potential = manifold.exp_map(v * 0.1, membrane_potential)
        else:
            membrane_potential = membrane_potential + x
        
        # 生成脉冲
        spike = (membrane_potential > self.threshold_param).float()
        
        # 重置机制
        if self.reset_mechanism == 'subtract':
            membrane_potential = membrane_potential - spike * self.threshold_param
        else:  # reset to zero
            membrane_potential = membrane_potential * (1 - spike)
        
        return spike, membrane_potential


class ManifoldSpikingLayer(nn.Module):
    """流形脉冲层
    
    结合几何一致的邻居聚合和曲率注意力
    """
    
    def __init__(
        self,
        in_features: int,
        out_features: int,
        n_heads: int = 4
    ):
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        self.n_heads = n_heads
        
        # 查询、键、值投影
        self.query = nn.Linear(in_features, out_features * n_heads, bias=False)
        self.key = nn.Linear(in_features, out_features * n_heads, bias=False)
        self.value = nn.Linear(in_features, out_features * n_heads, bias=False)
        
        # 脉冲神经元
        self.spiking_neurons = nn.ModuleList([
            ManifoldSpikingNeuron(out_features)
            for _ in range(n_heads)
        ])
        
        # 曲率注意力
        self.curvature_attention = nn.Parameter(torch.zeros(n_heads))
        
        # 输出投影
        self.output_proj = nn.Linear(out_features * n_heads, out_features, bias=False)
        
    def forward(
        self,
        x: torch.Tensor,
        adj_matrix: torch.Tensor,
        manifolds: Optional[list] = None
    ) -> Tuple[torch.Tensor, list]:
        """前向传播
        
        Args:
            x: 节点特征 (batch, n_nodes, in_features)
            adj_matrix: 邻接矩阵 (batch, n_nodes, n_nodes)
            manifolds: 流形列表（可选）
            
        Returns:
            output: 更新后的特征
            membrane_states: 各头膜电位状态
        """
        batch_size, n_nodes, _ = x.shape
        
        # 多头投影
        Q = self.query(x).view(batch_size, n_nodes, self.n_heads, -1)
        K = self.key(x).view(batch_size, n_nodes, self.n_heads, -1)
        V = self.value(x).view(batch_size, n_nodes, self.n_heads, -1)
        
        # 注意力分数
        scores = torch.einsum('bnhd,bmhd->bhnm', Q, K) / np.sqrt(self.out_features)
        
        # 曲率调制
        if manifolds is not None:
            curvature_weights = torch.stack([
                torch.tensor([m.curvature for m in manifolds])
            ]).abs()
            curvature_modulation = torch.sigmoid(self.curvature_attention) * curvature_weights
            scores = scores * (1 + curvature_modulation.view(1, -1, 1, 1))
        
        # 应用邻接矩阵掩码
        mask = (adj_matrix.unsqueeze(1) > 0).float()
        scores = scores.masked_fill(mask == 0, float('-inf'))
        attention = F.softmax(scores, dim=-1)
        
        # 聚合
        aggregated = torch.einsum('bhnm,bmhd->bnhd', attention, V)
        
        # 脉冲化
        spike_outputs = []
        membrane_states = []
        
        for h in range(self.n_heads):
            h_aggregated = aggregated[:, :, h, :]  # (batch, nodes, features)
            
            # 展平处理
            h_flat = h_aggregated.view(batch_size * n_nodes, -1)
            
            # 初始化膜电位
            membrane = torch.zeros_like(h_flat)
            
            # 脉冲生成
            manifold = manifolds[h] if manifolds else None
            spike, new_membrane = self.spiking_neurons[h](h_flat, membrane, manifold)
            
            spike_outputs.append(spike.view(batch_size, n_nodes, -1))
            membrane_states.append(new_membrane.view(batch_size, n_nodes, -1))
        
        # 合并多头输出
        combined = torch.cat(spike_outputs, dim=-1)
        output = self.output_proj(combined)
        
        return output, membrane_states
```

### 3. 流形学习目标

```python
class ManifoldLearningObjective(nn.Module):
    """流形学习目标
    
    结合分类和链路预测损失，通过测地距离优化
    """
    
    def __init__(
        self,
        n_classes: int,
        embedding_dim: int,
        link_pred_weight: float = 0.5
    ):
        super().__init__()
        
        self.n_classes = n_classes
        self.link_pred_weight = link_pred_weight
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(embedding_dim, embedding_dim),
            nn.ReLU(),
            nn.Linear(embedding_dim, n_classes)
        )
        
        # 链路预测解码器
        self.link_decoder = nn.Sequential(
            nn.Linear(embedding_dim * 2, embedding_dim),
            nn.ReLU(),
            nn.Linear(embedding_dim, 1),
            nn.Sigmoid()
        )
        
    def forward(
        self,
        embeddings: torch.Tensor,
        labels: torch.Tensor,
        adj_matrix: torch.Tensor,
        manifolds: list
    ) -> Tuple[torch.Tensor, dict]:
        """计算总损失
        
        Args:
            embeddings: 节点嵌入 (batch, n_nodes, dim)
            labels: 节点标签 (batch, n_nodes)
            adj_matrix: 邻接矩阵 (batch, n_nodes, n_nodes)
            manifolds: 流形列表
            
        Returns:
            total_loss: 总损失
            loss_dict: 各项损失
        """
        batch_size, n_nodes, dim = embeddings.shape
        
        # 分类损失
        logits = self.classifier(embeddings)
        class_loss = F.cross_entropy(
            logits.view(-1, self.n_classes),
            labels.view(-1)
        )
        
        # 链路预测损失（基于测地距离）
        # 采样正负边
        pos_edges = (adj_matrix > 0).nonzero(as_tuple=False)
        neg_edges = (adj_matrix == 0).nonzero(as_tuple=False)
        
        # 随机采样负边
        n_pos = pos_edges.size(0)
        if neg_edges.size(0) > n_pos:
            idx = torch.randperm(neg_edges.size(0))[:n_pos]
            neg_edges = neg_edges[idx]
        
        # 计算测地距离
        pos_dist = self._compute_geodesic_distance(
            embeddings, pos_edges, manifolds
        )
        neg_dist = self._compute_geodesic_distance(
            embeddings, neg_edges, manifolds
        )
        
        # 链路预测损失（margin-based）
        margin = 1.0
        link_loss = F.relu(margin + pos_dist - neg_dist).mean()
        
        # 总损失
        total_loss = (1 - self.link_pred_weight) * class_loss + self.link_pred_weight * link_loss
        
        return total_loss, {
            'classification_loss': class_loss.item(),
            'link_prediction_loss': link_loss.item(),
            'total_loss': total_loss.item()
        }
    
    def _compute_geodesic_distance(
        self,
        embeddings: torch.Tensor,
        edges: torch.Tensor,
        manifolds: list
    ) -> torch.Tensor:
        """计算边端点间的测地距离"""
        # 提取边端点嵌入
        src_emb = embeddings[edges[:, 0], edges[:, 1]]
        dst_emb = embeddings[edges[:, 0], edges[:, 2]]
        
        # 在各流形上计算距离并取平均
        distances = []
        for manifold in manifolds:
            d = manifold.distance(src_emb, dst_emb)
            distances.append(d)
        
        return torch.stack(distances).mean(dim=0)
```

### 4. 完整GSG模型

```python
class GeometryAwareSpikingGNN(nn.Module):
    """完整的几何感知脉冲图神经网络"""
    
    def __init__(
        self,
        n_features: int,
        hidden_dim: int,
        n_classes: int,
        n_layers: int = 3,
        n_heads: int = 4,
        manifold_types: list = ['euclidean', 'hyperbolic', 'spherical']
    ):
        super().__init__()
        
        self.n_layers = n_layers
        
        # 黎曼嵌入层
        self.embedding_layer = RiemannianEmbeddingLayer(
            n_features, hidden_dim, manifold_types
        )
        
        # 创建流形
        self.manifolds = nn.ModuleList([
            ConstantCurvatureManifold(
                hidden_dim,
                {'euclidean': 0.0, 'spherical': 1.0, 'hyperbolic': -1.0}[m]
            )
            for m in manifold_types
        ])
        
        # 流形脉冲层
        self.spiking_layers = nn.ModuleList([
            ManifoldSpikingLayer(hidden_dim, hidden_dim, n_heads)
            for _ in range(n_layers)
        ])
        
        # 学习目标
        self.objective = ManifoldLearningObjective(
            n_classes, hidden_dim
        )
        
    def forward(
        self,
        x: torch.Tensor,
        adj_matrix: torch.Tensor,
        labels: Optional[torch.Tensor] = None
    ) -> dict:
        """前向传播
        
        Args:
            x: 节点特征 (batch, n_nodes, n_features)
            adj_matrix: 邻接矩阵 (batch, n_nodes, n_nodes)
            labels: 节点标签（可选，用于训练）
            
        Returns:
            包含嵌入、预测和损失的字典
        """
        # 黎曼嵌入
        embeddings, manifold_weights = self.embedding_layer(x)
        
        # 多层脉冲处理
        membrane_history = []
        for layer in self.spiking_layers:
            embeddings, membrane_states = layer(
                embeddings, adj_matrix, list(self.manifolds)
            )
            membrane_history.append(membrane_states)
        
        # 输出
        result = {
            'embeddings': embeddings,
            'manifold_weights': manifold_weights,
            'membrane_history': membrane_history
        }
        
        # 计算损失（如果提供标签）
        if labels is not None:
            loss, loss_dict = self.objective(
                embeddings, labels, adj_matrix, list(self.manifolds)
            )
            result['loss'] = loss
            result['loss_dict'] = loss_dict
        
        return result


class RiemannianSGD(torch.optim.Optimizer):
    """黎曼随机梯度下降
    
    在流形上进行优化，无需时间反向传播
    """
    
    def __init__(self, params, lr=1e-3, momentum=0.9):
        defaults = dict(lr=lr, momentum=momentum)
        super().__init__(params, defaults)
        
    @torch.no_grad()
    def step(self, closure=None):
        """执行优化步骤"""
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        
        for group in self.param_groups:
            momentum = group['momentum']
            lr = group['lr']
            
            for p in group['params']:
                if p.grad is None:
                    continue
                
                grad = p.grad
                state = self.state[p]
                
                if len(state) == 0:
                    state['momentum_buffer'] = torch.zeros_like(p)
                
                buf = state['momentum_buffer']
                buf.mul_(momentum).add_(grad, alpha=1 - momentum)
                
                # 欧几里得更新（对于黎曼参数，应使用指数映射）
                p.add_(buf, alpha=-lr)
        
        return loss
```

## 应用场景

### 1. 层次结构图学习
- 知识图谱推理
- 社交网络分析
- 生物网络建模

### 2. 环形结构检测
- 化学分子图
- 交通网络环检测
- 神经环路分析

### 3. 能量高效图学习
- 边缘设备部署
- 神经形态计算
- 低功耗推理

## 使用示例

```python
# 创建模型
model = GeometryAwareSpikingGNN(
    n_features=64,
    hidden_dim=128,
    n_classes=10,
    n_layers=3,
    n_heads=4
)

# 模拟数据
batch_size = 8
n_nodes = 100
n_features = 64

x = torch.randn(batch_size, n_nodes, n_features)
adj = torch.rand(batch_size, n_nodes, n_nodes)
adj = (adj + adj.transpose(1, 2)) / 2
adj = (adj > 0.5).float()
labels = torch.randint(0, 10, (batch_size, n_nodes))

# 前向传播
result = model(x, adj, labels)

print(f"嵌入维度: {result['embeddings'].shape}")
print(f"流形权重: {result['manifold_weights']}")
print(f"损失: {result['loss_dict']}")

# 计算"脉冲"比例（能量效率指标）
spike_ratio = sum(
    (m.mean() for ms in result['membrane_history'] for m in ms)
) / (3 * 4)  # n_layers * n_heads

print(f"平均脉冲比例: {spike_ratio:.2%}")

# 训练循环
optimizer = RiemannianSGD(model.parameters(), lr=1e-3)

for epoch in range(100):
    optimizer.zero_grad()
    result = model(x, adj, labels)
    result['loss'].backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss = {result['loss_dict']['total_loss']:.4f}")
```

## 参考文献

- arXiv:2508.06793 - Geometry-Aware Spiking Graph Neural Network