---
name: federated-brain-trajectory-gnn
description: 联邦多轨迹图神经网络预测婴儿脑连接演化。FedGmTE-Net++框架，支持多模态/多轨迹预测，在数据稀缺环境下聚合多家医院的学习，保护数据隐私。包含辅助正则化和两步插补策略。触发词：婴儿脑发育、脑连接预测、联邦学习、图神经网络、多轨迹预测、数据稀缺、infant brain、federated learning、trajectory prediction、GNN。
---

# Federated Multi-Trajectory GNN for Infant Brain Connectivity Prediction

## 核心方法论

FedGmTE-Net++：联邦学习框架下的多轨迹脑连接演化预测

### 1. 联邦学习架构
- **隐私保护**：数据保留在本地医院
- **模型聚合**：聚合多家医院的本地学习
- **数据稀缺适应**：少量样本即可训练

### 2. 多轨迹预测
- **多模态支持**：T1-w、T2-w、DTI等
- **多连接类型**：功能连接、结构连接
- **统一框架**：单一模型预测多轨迹

### 3. 关键创新

#### 辅助正则化器
```python
# 利用纵向数据的完整轨迹
loss_aux = auxiliary_regularizer(all_timepoints)
```

#### 两步插补
1. **KNN预补全**：初步填充缺失时间点
2. **回归器精炼**：基于相似性分数改进插补

## 实现代码示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GATConv
from torch_geometric.data import Data
import numpy as np
from sklearn.neighbors import KNNImputer
from typing import List, Dict, Tuple, Optional


class GraphTrajectoryEncoder(nn.Module):
    """图轨迹编码器"""
    
    def __init__(self, num_nodes, input_dim, hidden_dim, num_layers=3):
        super().__init__()
        self.num_nodes = num_nodes
        self.hidden_dim = hidden_dim
        
        # 输入投影
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # GCN层
        self.gcn_layers = nn.ModuleList([
            GCNConv(hidden_dim, hidden_dim) for _ in range(num_layers)
        ])
        
        # 时序编码
        self.temporal_encoding = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ELU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def forward(self, graph_sequence):
        """
        Args:
            graph_sequence: List[Data] 图序列，每个时间点一个图
        
        Returns:
            trajectory_embedding: [hidden_dim] 轨迹嵌入
        """
        time_embeddings = []
        
        for t, graph in enumerate(graph_sequence):
            # 节点特征投影
            h = self.input_proj(graph.x)
            
            # 图卷积
            for gcn in self.gcn_layers:
                h = F.elu(gcn(h, graph.edge_index, graph.edge_attr))
            
            # 全局池化
            h_global = h.mean(dim=0)
            
            # 时间编码
            h_temporal = self.temporal_encoding(h_global)
            time_embeddings.append(h_temporal)
        
        # 聚合时序信息
        trajectory_embedding = torch.stack(time_embeddings).mean(dim=0)
        return trajectory_embedding


class TrajectoryGenerator(nn.Module):
    """轨迹生成器 - 预测未来脑连接"""
    
    def __init__(self, num_nodes, hidden_dim, num_timepoints):
        super().__init__()
        self.num_nodes = num_nodes
        self.num_timepoints = num_timepoints
        
        # 条件编码器
        self.condition_encoder = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ELU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 时间点特定解码器
        self.decoders = nn.ModuleList([
            nn.Sequential(
                nn.Linear(hidden_dim, hidden_dim),
                nn.ELU(),
                nn.Linear(hidden_dim, num_nodes * (num_nodes - 1) // 2)  # 上三角
            ) for _ in range(num_timepoints)
        ])
    
    def forward(self, trajectory_embedding, target_timepoints):
        """
        Args:
            trajectory_embedding: [hidden_dim]
            target_timepoints: List[int] 要预测的时间点
        
        Returns:
            predicted_graphs: Dict[int, Data] 预测的图
        """
        condition = self.condition_encoder(trajectory_embedding)
        predicted_graphs = {}
        
        for t in target_timepoints:
            # 预测邻接矩阵上三角
            adj_upper = self.decoders[t](condition)
            
            # 重构完整邻接矩阵
            adj = torch.zeros(self.num_nodes, self.num_nodes)
            triu_indices = torch.triu_indices(self.num_nodes, self.num_nodes, offset=1)
            adj[triu_indices[0], triu_indices[1]] = adj_upper
            adj = adj + adj.T  # 对称化
            
            # 创建图对象
            edge_index = (adj > 0.5).nonzero(as_tuple=False).t()
            edge_attr = adj[adj > 0.5]
            
            predicted_graphs[t] = Data(
                x=torch.eye(self.num_nodes),  # 单位矩阵作为节点特征
                edge_index=edge_index,
                edge_attr=edge_attr
            )
        
        return predicted_graphs


class AuxiliaryRegularizer(nn.Module):
    """辅助正则化器 - 利用所有纵向数据"""
    
    def __init__(self, hidden_dim):
        super().__init__()
        self.predictor = nn.Linear(hidden_dim, 1)
    
    def forward(self, all_embeddings, timepoints):
        """
        Args:
            all_embeddings: List[Tensor] 所有时间点的嵌入
            timepoints: List[int] 对应的时间点
        
        Returns:
            aux_loss: 辅助损失
        """
        losses = []
        
        for i, (emb, t) in enumerate(zip(all_embeddings, timepoints)):
            # 预测下一个时间点
            if i < len(all_embeddings) - 1:
                next_emb = all_embeddings[i + 1]
                pred = self.predictor(emb)
                target = torch.tensor([timepoints[i + 1] - t], dtype=torch.float)
                losses.append(F.mse_loss(pred.squeeze(), target))
        
        # 时序一致性损失
        if len(all_embeddings) > 2:
            # 相邻时间点嵌入应相似
            consistency_loss = sum(
                F.mse_loss(all_embeddings[i], all_embeddings[i + 1])
                for i in range(len(all_embeddings) - 1)
            ) / (len(all_embeddings) - 1)
            losses.append(consistency_loss)
        
        return sum(losses) / len(losses) if losses else torch.tensor(0.0)


class TwoStepImputation:
    """两步插补策略"""
    
    def __init__(self, n_neighbors=5):
        self.knn_imputer = KNNImputer(n_neighbors=n_neighbors)
        self.regressors = {}
    
    def precomplete(self, data, mask):
        """
        第一步：KNN预补全
        
        Args:
            data: [num_samples, num_features] 原始数据
            mask: [num_samples, num_features] 缺失掩码 (1=观测, 0=缺失)
        
        Returns:
            precompleted: 预补全后的数据
        """
        # KNN插补
        precompleted = self.knn_imputer.fit_transform(data)
        return precompleted
    
    def refine(self, data, precompleted, mask, similarity_scores):
        """
        第二步：回归器精炼
        
        Args:
            data: 原始数据
            precompleted: KNN预补全结果
            mask: 缺失掩码
            similarity_scores: 样本间相似性分数
        
        Returns:
            refined: 精炼后的数据
        """
        refined = precompleted.copy()
        
        # 对每个缺失值用回归器精炼
        missing_indices = np.where(mask == 0)
        
        for i, j in zip(*missing_indices):
            # 找到最相似的完整样本
            similar_samples = np.argsort(similarity_scores[i])[::-1]
            similar_complete = [s for s in similar_samples if mask[s, j] == 1]
            
            if len(similar_complete) > 0:
                # 用相似样本的加权平均
                weights = similarity_scores[i, similar_complete]
                weights = weights / weights.sum()
                refined[i, j] = np.average(
                    precompleted[similar_complete, j],
                    weights=weights
                )
        
        return refined
    
    def fit_regressors(self, data, mask):
        """训练回归器用于插补精炼"""
        from sklearn.linear_model import Ridge
        
        for j in range(data.shape[1]):
            # 找到该特征的完整样本
            complete_mask = mask[:, j] == 1
            if complete_mask.sum() > 1:
                X = data[complete_mask]
                y = X[:, j]
                # 用其他特征预测
                X_other = np.delete(X, j, axis=1)
                
                self.regressors[j] = Ridge(alpha=1.0)
                self.regressors[j].fit(X_other, y)
    
    def __call__(self, data, mask, similarity_scores=None):
        """完整的两步插补流程"""
        # 第一步
        precompleted = self.precomplete(data, mask)
        
        # 计算相似性（如果未提供）
        if similarity_scores is None:
            from sklearn.metrics.pairwise import cosine_similarity
            similarity_scores = cosine_similarity(precompleted)
        
        # 第二步
        refined = self.refine(data, precompleted, mask, similarity_scores)
        
        return refined


class FedGmTE_Net(nn.Module):
    """
    Federated Graph Multi-Trajectory Evolution Network++
    
    联邦多轨迹图神经网络预测婴儿脑连接演化
    """
    
    def __init__(self, num_nodes, input_dim, hidden_dim, 
                 num_trajectories=3, num_future_timepoints=5):
        super().__init__()
        self.num_nodes = num_nodes
        self.hidden_dim = hidden_dim
        self.num_trajectories = num_trajectories
        self.num_future_timepoints = num_future_timepoints
        
        # 每个轨迹的编码器
        self.encoders = nn.ModuleList([
            GraphTrajectoryEncoder(num_nodes, input_dim, hidden_dim)
            for _ in range(num_trajectories)
        ])
        
        # 共享的条件生成器
        self.condition_generator = nn.Sequential(
            nn.Linear(hidden_dim * num_trajectories, hidden_dim),
            nn.ELU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 每个轨迹的生成器
        self.generators = nn.ModuleList([
            TrajectoryGenerator(num_nodes, hidden_dim, num_future_timepoints)
            for _ in range(num_trajectories)
        ])
        
        # 辅助正则化器
        self.aux_regularizer = AuxiliaryRegularizer(hidden_dim)
        
        # 两步插补
        self.imputer = TwoStepImputation()
    
    def forward(self, trajectory_sequences, return_aux_loss=True):
        """
        Args:
            trajectory_sequences: List[List[Data]] 
                外层列表：轨迹类型（T1-w, T2-w, DTI等）
                内层列表：时间点序列
        
        Returns:
            predictions: Dict[int, Dict[int, Data]] 
                预测的未来图 {trajectory_idx: {timepoint: graph}}
        """
        # 编码所有轨迹
        embeddings = []
        for traj_idx, seq in enumerate(trajectory_sequences):
            emb = self.encoders[traj_idx](seq)
            embeddings.append(emb)
        
        # 拼接所有轨迹嵌入
        combined = torch.cat(embeddings, dim=-1)
        
        # 生成条件向量
        condition = self.condition_generator(combined)
        
        # 预测每个轨迹的未来图
        predictions = {}
        target_timepoints = list(range(self.num_future_timepoints))
        
        for traj_idx in range(self.num_trajectories):
            predictions[traj_idx] = self.generators[traj_idx](
                condition, target_timepoints
            )
        
        if return_aux_loss:
            # 计算辅助损失
            all_embeddings = []
            for seq in trajectory_sequences:
                for t, graph in enumerate(seq):
                    # 简化：使用编码器的中间表示
                    pass
            
            aux_loss = torch.tensor(0.0)  # 简化实现
            return predictions, aux_loss
        
        return predictions


class FederatedClient:
    """联邦学习客户端（医院）"""
    
    def __init__(self, client_id, model, local_data):
        self.client_id = client_id
        self.model = model
        self.local_data = local_data
        self.optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    def local_train(self, epochs=10):
        """本地训练"""
        self.model.train()
        total_loss = 0
        
        for epoch in range(epochs):
            for batch in self.local_data:
                self.optimizer.zero_grad()
                
                # 前向传播
                predictions, aux_loss = self.model(batch)
                
                # 计算损失
                main_loss = self.compute_loss(predictions, batch)
                loss = main_loss + 0.1 * aux_loss
                
                # 反向传播
                loss.backward()
                self.optimizer.step()
                
                total_loss += loss.item()
        
        return total_loss / len(self.local_data)
    
    def compute_loss(self, predictions, batch):
        """计算预测损失"""
        loss = 0
        for traj_idx, pred_graphs in predictions.items():
            for t, pred_graph in pred_graphs.items():
                target = batch['targets'][traj_idx][t]
                # 图重建损失
                loss += F.binary_cross_entropy(
                    pred_graph.edge_attr,
                    target.edge_attr
                )
        return loss
    
    def get_model_params(self):
        """获取模型参数"""
        return {k: v.clone() for k, v in self.model.state_dict().items()}
    
    def set_model_params(self, params):
        """设置模型参数"""
        self.model.load_state_dict(params)


class FederatedServer:
    """联邦学习服务器"""
    
    def __init__(self, model_template, num_clients):
        self.global_model = model_template
        self.clients = []
        self.num_clients = num_clients
    
    def register_client(self, client):
        """注册客户端"""
        self.clients.append(client)
    
    def aggregate_models(self, client_params_list):
        """
        FedAvg聚合策略
        
        Args:
            client_params_list: List[Dict] 各客户端的模型参数
        
        Returns:
            aggregated_params: 聚合后的参数
        """
        aggregated = {}
        
        for key in client_params_list[0].keys():
            # 平均聚合
            aggregated[key] = sum(
                params[key] for params in client_params_list
            ) / len(client_params_list)
        
        return aggregated
    
    def federated_round(self):
        """执行一轮联邦学习"""
        # 分发全局模型
        global_params = self.global_model.state_dict()
        for client in self.clients:
            client.set_model_params(global_params)
        
        # 本地训练
        client_params = []
        for client in self.clients:
            loss = client.local_train(epochs=10)
            client_params.append(client.get_model_params())
            print(f"Client {client.client_id}: Loss = {loss:.4f}")
        
        # 聚合
        aggregated = self.aggregate_models(client_params)
        self.global_model.load_state_dict(aggregated)
        
        return aggregated


def train_federated_example():
    """联邦学习训练示例"""
    # 参数
    num_nodes = 50  # 脑区数量
    input_dim = 10
    hidden_dim = 64
    num_clients = 5  # 5家医院
    
    # 创建模型模板
    model_template = FedGmTE_Net(
        num_nodes=num_nodes,
        input_dim=input_dim,
        hidden_dim=hidden_dim
    )
    
    # 创建服务器
    server = FederatedServer(model_template, num_clients)
    
    # 创建客户端（模拟）
    for i in range(num_clients):
        local_model = FedGmTE_Net(
            num_nodes=num_nodes,
            input_dim=input_dim,
            hidden_dim=hidden_dim
        )
        # 模拟本地数据
        local_data = [generate_mock_trajectory(num_nodes, input_dim) 
                      for _ in range(10)]
        client = FederatedClient(i, local_model, local_data)
        server.register_client(client)
    
    # 执行联邦训练
    for round_idx in range(10):
        print(f"\n=== Round {round_idx + 1} ===")
        server.federated_round()
    
    return server.global_model


def generate_mock_trajectory(num_nodes, input_dim):
    """生成模拟轨迹数据"""
    def create_graph(t):
        adj = torch.rand(num_nodes, num_nodes)
        adj = (adj + adj.T) / 2
        adj = (adj > 0.5).float()
        edge_index = adj.nonzero(as_tuple=False).t()
        return Data(
            x=torch.randn(num_nodes, input_dim),
            edge_index=edge_index,
            edge_attr=torch.rand(edge_index.shape[1])
        )
    
    return {
        'sequences': [[create_graph(t) for t in range(5)] for _ in range(3)],
        'targets': [[create_graph(t) for t in range(5, 10)] for _ in range(3)]
    }


if __name__ == "__main__":
    model = train_federated_example()
    print("\nFederated training complete!")
```

## 应用场景

1. **婴儿脑发育研究**
   - 预测出生后第一年的脑网络演化
   - 早期识别发育异常风险
   - 理解脑连接的发展轨迹

2. **多中心协作**
   - 多家医院数据联合分析
   - 保护患者隐私
   - 克服单中心样本不足

3. **多模态预测**
   - T1-w MRI轨迹预测
   - DTI白质连接预测
   fMRI功能连接预测

## 关键优势

- **数据稀缺适应**：辅助正则化利用纵向数据
- **不完整数据支持**：两步插补处理缺失
- **隐私保护**：数据不出医院
- **多轨迹联合**：单一模型预测多种模态

## Activation Keywords
- 婴儿脑发育
- 脑连接预测
- 联邦学习
- 图神经网络
- 多轨迹预测
- 数据稀缺
- infant brain
- federated learning
- trajectory prediction
- GNN
- 纵向分析
- 隐私保护

## Tools Used
- pytorch
- torch_geometric
- numpy
- sklearn

## Instructions for Agents
1. 理解联邦学习架构：数据保留在本地，只聚合模型参数
2. 掌握多轨迹编码：处理多种模态（T1-w、T2-w、DTI）
3. 实现两步插补：KNN预补全+回归器精炼
4. 应用辅助正则化：利用纵向数据的完整轨迹
5. 注意隐私保护：模型参数聚合而非数据共享

## Examples
```python
# 使用示例
from federated_brain_trajectory_gnn import FedGmTE_Net, FederatedServer

# 1. 创建模型
model = FedGmTE_Net(
    num_nodes=50,
    input_dim=10,
    hidden_dim=64,
    num_trajectories=3
)

# 2. 创建联邦服务器
server = FederatedServer(model, num_clients=5)

# 3. 注册客户端（医院）
for i in range(5):
    client = FederatedClient(i, model, local_data)
    server.register_client(client)

# 4. 执行联邦训练
for round_idx in range(10):
    server.federated_round()
```

## 参考文献

- arXiv:2401.01383 - Predicting Infant Brain Connectivity with Federated Multi-Trajectory GNNs