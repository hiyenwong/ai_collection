---
name: specificity-aware-federated-graph-learning
description: 特异性感知联邦图学习框架(SFGL)。在保护数据隐私的前提下进行多站点fMRI协作训练，通过共享分支和个性化分支平衡知识共享与站点特异性保持。适用于多中心脑疾病识别、联邦学习、rs-fMRI分析。触发词：联邦学习、图神经网络、fMRI分析、多站点、数据隐私、federated learning、GNN、multi-site、brain disorder identification。
user-invocable: true
---

# Specificity-Aware Federated Graph Learning for fMRI

特异性感知联邦图学习框架

## 核心方法论

**来源：** arXiv:2308.10302
**效用：** 0.92

### 问题背景

多站点 fMRI 数据训练面临挑战：

| 挑战 | 描述 |
|------|------|
| 数据隐私 | 无法集中多站点数据 |
| 站点特异性 | 人口统计因素（年龄、性别、教育）差异 |
| 存储负担 | 大规模数据集中存储困难 |

传统联邦学习方法忽略了站点特异性，导致性能下降。

### SFGL 核心创新

**双分支架构**：

| 分支 | 功能 | 参数处理 |
|------|------|----------|
| **共享分支** | 知识共享 | 发送到服务器聚合 |
| **个性化分支** | 保持站点特异性 | 保持本地 |

### 实现框架

```python
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional
import numpy as np

class SpatioTemporalAttentionGIN(nn.Module):
    """
    时空注意力图同构网络
    
    用于学习动态 fMRI 表示
    """
    
    def __init__(
        self,
        n_rois: int = 200,
        hidden_dim: int = 64,
        n_layers: int = 3,
        n_timepoints: int = 200
    ):
        super().__init__()
        
        self.n_rois = n_rois
        self.hidden_dim = hidden_dim
        
        # 空间注意力（ROI 之间）
        self.spatial_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=4,
            batch_first=True
        )
        
        # 时间注意力
        self.temporal_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=4,
            batch_first=True
        )
        
        # GIN 层
        self.gin_layers = nn.ModuleList([
            GINConv(hidden_dim, hidden_dim) for _ in range(n_layers)
        ])
        
        # 节点嵌入
        self.node_embedding = nn.Linear(n_timepoints, hidden_dim)
        
        # 输出
        self.output = nn.Linear(hidden_dim * n_rois, hidden_dim)
    
    def forward(
        self,
        fmri_data: torch.Tensor,
        adj_matrix: torch.Tensor
    ) -> torch.Tensor:
        """
        前向传播
        
        参数:
            fmri_data: fMRI 数据 (batch, n_rois, n_timepoints)
            adj_matrix: 邻接矩阵 (batch, n_rois, n_rois)
            
        返回:
            图表示 (batch, hidden_dim)
        """
        batch_size = fmri_data.shape[0]
        
        # 节点嵌入
        h = self.node_embedding(fmri_data)  # (batch, n_rois, hidden_dim)
        
        # 时间注意力
        h = h.permute(0, 2, 1)  # (batch, hidden_dim, n_rois)
        h, _ = self.temporal_attention(h, h, h)
        h = h.permute(0, 2, 1)  # (batch, n_rois, hidden_dim)
        
        # GIN 层
        for gin_layer in self.gin_layers:
            h = gin_layer(h, adj_matrix)
        
        # 空间注意力
        h, _ = self.spatial_attention(h, h, h)
        
        # 全局池化
        h = h.view(batch_size, -1)
        out = self.output(h)
        
        return out


class GINConv(nn.Module):
    """图同构网络卷积层"""
    
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        
        self.mlp = nn.Sequential(
            nn.Linear(in_dim, out_dim),
            nn.ReLU(),
            nn.Linear(out_dim, out_dim)
        )
        
        self.eps = nn.Parameter(torch.zeros(1))
    
    def forward(
        self,
        x: torch.Tensor,
        adj: torch.Tensor
    ) -> torch.Tensor:
        """
        参数:
            x: 节点特征 (batch, n_nodes, in_dim)
            adj: 邻接矩阵 (batch, n_nodes, n_nodes)
        """
        # 聚合邻居
        neighbor_sum = torch.bmm(adj, x)
        
        # 自身 + 邻居
        out = (1 + self.eps) * x + neighbor_sum
        
        return self.mlp(out)


class PersonalizedBranch(nn.Module):
    """
    个性化分支
    
    整合人口统计信息和功能连接网络
    """
    
    def __init__(
        self,
        n_rois: int = 200,
        hidden_dim: int = 64,
        n_demographics: int = 3  # age, gender, education
    ):
        super().__init__()
        
        # 人口统计编码
        self.demographic_encoder = nn.Sequential(
            nn.Linear(n_demographics, 32),
            nn.ReLU(),
            nn.Linear(32, hidden_dim)
        )
        
        # 功能连接编码
        self.fc_encoder = nn.Sequential(
            nn.Linear(n_rois * n_rois, 256),
            nn.ReLU(),
            nn.Linear(256, hidden_dim)
        )
        
        # 融合层
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def forward(
        self,
        demographics: torch.Tensor,
        fc_matrix: torch.Tensor
    ) -> torch.Tensor:
        """
        参数:
            demographics: 人口统计 (batch, n_demographics)
            fc_matrix: 功能连接矩阵 (batch, n_rois, n_rois)
        """
        # 编码人口统计
        demo_feat = self.demographic_encoder(demographics)
        
        # 编码功能连接
        fc_flat = fc_matrix.view(fc_matrix.shape[0], -1)
        fc_feat = self.fc_encoder(fc_flat)
        
        # 融合
        combined = torch.cat([demo_feat, fc_feat], dim=-1)
        out = self.fusion(combined)
        
        return out


class SFGLClient(nn.Module):
    """
    SFGL 客户端模型
    
    包含共享分支和个性化分支
    """
    
    def __init__(
        self,
        n_rois: int = 200,
        hidden_dim: int = 64,
        n_classes: int = 2,
        n_demographics: int = 3
    ):
        super().__init__()
        
        # 共享分支（参数会发送到服务器）
        self.shared_branch = SpatioTemporalAttentionGIN(
            n_rois=n_rois,
            hidden_dim=hidden_dim
        )
        
        # 个性化分支（参数保持本地）
        self.personalized_branch = PersonalizedBranch(
            n_rois=n_rois,
            hidden_dim=hidden_dim,
            n_demographics=n_demographics
        )
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_classes)
        )
    
    def forward(
        self,
        fmri_data: torch.Tensor,
        adj_matrix: torch.Tensor,
        demographics: torch.Tensor,
        fc_matrix: torch.Tensor
    ) -> torch.Tensor:
        """
        前向传播
        """
        # 共享分支
        shared_feat = self.shared_branch(fmri_data, adj_matrix)
        
        # 个性化分支
        personal_feat = self.personalized_branch(demographics, fc_matrix)
        
        # 融合
        combined = torch.cat([shared_feat, personal_feat], dim=-1)
        
        # 分类
        logits = self.classifier(combined)
        
        return logits
    
    def get_shared_parameters(self) -> Dict:
        """获取共享分支参数"""
        return {
            name: param.clone()
            for name, param in self.shared_branch.named_parameters()
        }
    
    def set_shared_parameters(self, params: Dict):
        """设置共享分支参数"""
        for name, param in params.items():
            self.shared_branch.state_dict()[name].copy_(param)


class SFGLServer:
    """
    SFGL 服务器
    
    负责聚合多个客户端的共享参数
    """
    
    def __init__(self, aggregation: str = 'fedavg'):
        self.aggregation = aggregation
        self.global_params = None
    
    def aggregate(
        self,
        client_params: List[Dict],
        client_weights: Optional[List[float]] = None
    ) -> Dict:
        """
        聚合客户端参数
        
        参数:
            client_params: 各客户端的参数列表
            client_weights: 客户端权重（如样本数量）
            
        返回:
            聚合后的参数
        """
        if client_weights is None:
            client_weights = [1.0 / len(client_params)] * len(client_params)
        
        # 归一化权重
        total_weight = sum(client_weights)
        client_weights = [w / total_weight for w in client_weights]
        
        # FedAvg 聚合
        aggregated = {}
        for name in client_params[0].keys():
            aggregated[name] = torch.zeros_like(client_params[0][name])
            for params, weight in zip(client_params, client_weights):
                aggregated[name] += weight * params[name]
        
        self.global_params = aggregated
        return aggregated


class SFGLFramework:
    """
    完整的 SFGL 训练框架
    """
    
    def __init__(
        self,
        n_clients: int,
        n_rois: int = 200,
        hidden_dim: int = 64,
        n_classes: int = 2,
        n_demographics: int = 3
    ):
        self.n_clients = n_clients
        
        # 创建客户端
        self.clients = [
            SFGLClient(n_rois, hidden_dim, n_classes, n_demographics)
            for _ in range(n_clients)
        ]
        
        # 创建服务器
        self.server = SFGLServer()
    
    def train_round(
        self,
        client_data: List[Tuple],
        local_epochs: int = 5,
        lr: float = 1e-3
    ) -> Dict:
        """
        执行一轮联邦训练
        
        参数:
            client_data: 各客户端数据 [(fmri, adj, demo, fc, labels), ...]
            local_epochs: 本地训练轮数
            lr: 学习率
            
        返回:
            训练统计
        """
        stats = {'client_losses': [], 'global_update': None}
        
        # 1. 本地训练
        client_params = []
        client_weights = []
        
        for i, (client, data) in enumerate(zip(self.clients, client_data)):
            fmri, adj, demo, fc, labels = data
            
            # 本地训练
            optimizer = torch.optim.Adam(client.parameters(), lr=lr)
            total_loss = 0.0
            
            for epoch in range(local_epochs):
                optimizer.zero_grad()
                
                logits = client(fmri, adj, demo, fc)
                loss = nn.CrossEntropyLoss()(logits, labels)
                
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
            
            stats['client_losses'].append(total_loss / local_epochs)
            
            # 收集共享参数
            client_params.append(client.get_shared_parameters())
            client_weights.append(len(labels))  # 以样本数为权重
        
        # 2. 服务器聚合
        aggregated = self.server.aggregate(client_params, client_weights)
        stats['global_update'] = aggregated
        
        # 3. 分发全局参数
        for client in self.clients:
            client.set_shared_parameters(aggregated)
        
        return stats
    
    def train(
        self,
        client_data: List[Tuple],
        n_rounds: int = 100,
        local_epochs: int = 5,
        lr: float = 1e-3,
        verbose: bool = True
    ) -> List[Dict]:
        """
        完整训练过程
        """
        history = []
        
        for round_idx in range(n_rounds):
            stats = self.train_round(client_data, local_epochs, lr)
            history.append(stats)
            
            if verbose and round_idx % 10 == 0:
                avg_loss = np.mean(stats['client_losses'])
                print(f"Round {round_idx}: Avg Loss = {avg_loss:.4f}")
        
        return history


def run_federated_fmri_analysis(
    site_data: List[Dict],
    n_rounds: int = 100,
    hidden_dim: int = 64,
    n_classes: int = 2
) -> Dict:
    """
    运行联邦 fMRI 分析
    
    参数:
        site_data: 各站点数据
        n_rounds: 训练轮数
        hidden_dim: 隐藏维度
        n_classes: 分类数
        
    返回:
        分析结果
    """
    n_sites = len(site_data)
    n_rois = site_data[0]['fmri'].shape[1]
    
    # 创建框架
    framework = SFGLFramework(
        n_clients=n_sites,
        n_rois=n_rois,
        hidden_dim=hidden_dim,
        n_classes=n_classes
    )
    
    # 准备数据
    client_data = [
        (
            site['fmri'],
            site['adj'],
            site['demographics'],
            site['fc'],
            site['labels']
        )
        for site in site_data
    ]
    
    # 训练
    history = framework.train(client_data, n_rounds=n_rounds)
    
    # 评估
    results = {
        'history': history,
        'final_loss': history[-1]['client_losses'],
        'n_sites': n_sites,
        'n_rounds': n_rounds
    }
    
    return results
```

## 应用场景

### 1. 多中心脑疾病识别
- 联邦训练保护隐私
- 保持各中心特异性

### 2. rs-fMRI 分析
- 时空特征提取
- 功能连接建模

### 3. 数据隐私敏感场景
- 医疗数据协作
- 跨机构研究

## 方法优势

| 优势 | 说明 |
|------|------|
| **隐私保护** | 数据不出本地 |
| **特异性保持** | 个性化分支捕获站点特征 |
| **知识共享** | 共享分支学习通用表示 |
| **可扩展** | 支持任意数量站点 |

## Activation Keywords
- 联邦学习
- 图神经网络
- fMRI分析
- 多站点
- 数据隐私
- federated learning
- GNN
- multi-site
- brain disorder identification
- privacy-preserving

## Tools Used
- torch
- numpy

## Instructions for Agents
1. 理解双分支架构：共享分支 + 个性化分支
2. 掌握联邦学习流程：本地训练 → 服务器聚合 → 参数分发
3. 注意特异性保持：人口统计信息本地处理
4. 实现时空注意力：捕获 fMRI 动态
5. 应用场景：多中心脑疾病识别

## Examples
```python
# 使用示例
from specificity_aware_federated_graph_learning import SFGLFramework, run_federated_fmri_analysis

# 1. 准备多站点数据
site_data = [
    {
        'fmri': fmri_site1,       # (n_subjects, n_rois, n_timepoints)
        'adj': adj_site1,          # (n_subjects, n_rois, n_rois)
        'demographics': demo_site1, # (n_subjects, 3)
        'fc': fc_site1,            # (n_subjects, n_rois, n_rois)
        'labels': labels_site1     # (n_subjects,)
    },
    # 更多站点...
]

# 2. 运行联邦分析
results = run_federated_fmri_analysis(
    site_data=site_data,
    n_rounds=100,
    n_classes=2  # 健康vs疾病
)

# 3. 查看结果
print(f"最终损失: {results['final_loss']}")
```

## 参考文献
- Wang, Q., et al. (2023). "Preserving Specificity in Federated Graph Learning for fMRI-based Neurological Disorder Identification" arXiv:2308.10302
- McMahan, B., et al. (2017). "Communication-Efficient Learning of Deep Networks from Decentralized Data" AISTATS