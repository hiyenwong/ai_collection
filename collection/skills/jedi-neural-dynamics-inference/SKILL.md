---
name: jedi-neural-dynamics-inference
description: JEDI联合嵌入神经动力学推断框架。通过学习RNN权重的共享嵌入空间，捕获跨任务和上下文的神经动力学，从有限、噪声、高维的神经记录中识别任务特定的动力学规则。适用于多任务神经动力学分析、运动皮层记录、神经群体动态建模。触发词：神经动力学、RNN嵌入、多任务学习、群体神经、neural dynamics、population dynamics、recurrent neural network、embedding、multi-task。
user-invocable: true
---

# JEDI: Jointly Embedded Inference of Neural Dynamics

联合嵌入神经动力学推断框架

## 核心方法论

**来源：** arXiv:2603.10489
**效用：** 0.92

### 问题背景

动物大脑使用单个神经网络灵活高效地完成多种行为任务。从神经记录中识别任务特定的动力学规则面临挑战：

| 挑战 | 描述 |
|------|------|
| 数据有限 | 实验记录通常有限 |
| 噪声高 | 神经记录噪声大 |
| 高维度 | 群体神经元维度高 |
| 部分观测 | 只能访问部分脑状态 |

现有 RNN 方法局限于单一任务，难以跨行为条件泛化。

### JEDI 核心创新

**分层模型**：学习 RNN 权重的共享嵌入空间

| 组件 | 功能 |
|------|------|
| **嵌入层** | 学习任务/上下文特定的嵌入向量 |
| **RNN 权重生成器** | 从嵌入生成 RNN 权重 |
| **动力学模型** | 捕获神经群体动态 |

### 实现框架

```python
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional
import numpy as np

class JEDIModel(nn.Module):
    """
    JEDI: Jointly Embedded Inference of Neural Dynamics
    
    核心思想：
    1. 学习任务/上下文的嵌入向量
    2. 从嵌入生成 RNN 权重
    3. RNN 捕获神经动力学
    """
    
    def __init__(
        self,
        n_neurons: int,
        hidden_dim: int = 64,
        embedding_dim: int = 32,
        n_tasks: int = 10,
        dt: float = 0.01
    ):
        super().__init__()
        
        self.n_neurons = n_neurons
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.dt = dt
        
        # 任务嵌入
        self.task_embeddings = nn.Embedding(n_tasks, embedding_dim)
        
        # 从嵌入生成 RNN 权重的网络
        self.weight_generator = nn.Sequential(
            nn.Linear(embedding_dim, 128),
            nn.ReLU(),
            nn.Linear(128, hidden_dim * (n_neurons + hidden_dim + 1))
        )
        
        # 输出层
        self.output_layer = nn.Linear(hidden_dim, n_neurons)
        
    def generate_rnn_weights(
        self,
        task_id: int
    ) -> Dict[str, torch.Tensor]:
        """
        从任务嵌入生成 RNN 权重
        
        参数:
            task_id: 任务 ID
            
        返回:
            权重字典 (W_in, W_rec, b_rec)
        """
        # 获取任务嵌入
        embedding = self.task_embeddings(torch.tensor([task_id]))
        
        # 生成权重
        weights_flat = self.weight_generator(embedding)
        
        # 解析权重
        hidden = self.hidden_dim
        input_size = self.n_neurons
        
        W_in_end = hidden * input_size
        W_rec_end = W_in_end + hidden * hidden
        
        W_in = weights_flat[:, :W_in_end].view(hidden, input_size)
        W_rec = weights_flat[:, W_in_end:W_rec_end].view(hidden, hidden)
        b_rec = weights_flat[:, W_rec_end:].view(hidden)
        
        return {
            'W_in': W_in,
            'W_rec': W_rec,
            'b_rec': b_rec
        }
    
    def forward(
        self,
        neural_data: torch.Tensor,
        task_id: int
    ) -> torch.Tensor:
        """
        前向传播
        
        参数:
            neural_data: 神经数据 (batch, time, n_neurons)
            task_id: 任务 ID
            
        返回:
            预测的神经活动 (batch, time, n_neurons)
        """
        batch_size, seq_len, _ = neural_data.shape
        
        # 生成任务特定权重
        weights = self.generate_rnn_weights(task_id)
        W_in = weights['W_in']
        W_rec = weights['W_rec']
        b_rec = weights['b_rec']
        
        # 初始化隐藏状态
        h = torch.zeros(batch_size, self.hidden_dim, device=neural_data.device)
        
        outputs = []
        for t in range(seq_len):
            # RNN 更新
            x_t = neural_data[:, t, :]
            h = torch.tanh(x_t @ W_in.T + h @ W_rec.T + b_rec)
            
            # 输出
            out = self.output_layer(h)
            outputs.append(out)
        
        outputs = torch.stack(outputs, dim=1)
        return outputs
    
    def get_task_embedding(self, task_id: int) -> torch.Tensor:
        """获取任务嵌入向量"""
        with torch.no_grad():
            return self.task_embeddings(torch.tensor([task_id])).squeeze(0)


class JEDITrainer:
    """
    JEDI 训练器
    """
    
    def __init__(
        self,
        model: JEDIModel,
        lr: float = 1e-3,
        weight_decay: float = 1e-5
    ):
        self.model = model
        self.optimizer = torch.optim.Adam(
            model.parameters(),
            lr=lr,
            weight_decay=weight_decay
        )
    
    def train_epoch(
        self,
        data_loader: torch.utils.data.DataLoader,
        task_ids: List[int]
    ) -> float:
        """
        训练一个 epoch
        
        参数:
            data_loader: 数据加载器
            task_ids: 任务 ID 列表
            
        返回:
            平均损失
        """
        self.model.train()
        total_loss = 0.0
        
        for batch_idx, (neural_data, task_id) in enumerate(data_loader):
            self.optimizer.zero_grad()
            
            # 前向传播
            predictions = self.model(neural_data, task_id)
            
            # 计算损失（MSE）
            loss = nn.MSELoss()(predictions, neural_data)
            
            # 反向传播
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(data_loader)
    
    def extract_dynamics(
        self,
        task_id: int
    ) -> Dict:
        """
        提取任务特定的动力学特征
        
        返回:
            动力学特征（固定点、特征值等）
        """
        self.model.eval()
        
        with torch.no_grad():
            weights = self.model.generate_rnn_weights(task_id)
            W_rec = weights['W_rec']
            
            # 计算特征值（揭示动力学）
            eigenvalues = torch.linalg.eigvals(W_rec)
            
            # 找固定点（近似）
            # 固定点满足 h = tanh(W_rec @ h + b)
            # 这里使用简单迭代
            h = torch.zeros(self.model.hidden_dim)
            for _ in range(100):
                h_new = torch.tanh(h @ W_rec.T + weights['b_rec'])
                if torch.norm(h_new - h) < 1e-6:
                    break
                h = h_new
            
            return {
                'eigenvalues': eigenvalues.numpy(),
                'fixed_point': h.numpy(),
                'spectral_radius': torch.max(torch.abs(eigenvalues)).item()
            }


class MultiTaskDynamicsAnalyzer:
    """
    多任务动力学分析器
    """
    
    def __init__(self, model: JEDIModel):
        self.model = model
    
    def analyze_shared_structure(
        self,
        task_ids: List[int]
    ) -> Dict:
        """
        分析跨任务共享结构
        
        参数:
            task_ids: 任务 ID 列表
            
        返回:
            共享结构分析结果
        """
        embeddings = []
        dynamics = []
        
        for task_id in task_ids:
            emb = self.model.get_task_embedding(task_id)
            embeddings.append(emb.numpy())
            
            dyn = JEDITrainer(self.model).extract_dynamics(task_id)
            dynamics.append(dyn)
        
        embeddings = np.array(embeddings)
        
        # 计算嵌入相似性
        from sklearn.metrics.pairwise import cosine_similarity
        similarity = cosine_similarity(embeddings)
        
        return {
            'embeddings': embeddings,
            'similarity_matrix': similarity,
            'dynamics': dynamics
        }
    
    def find_task_relationships(
        self,
        task_ids: List[int],
        task_names: List[str]
    ) -> List[Dict]:
        """
        发现任务间关系
        
        返回:
            任务关系列表
        """
        analysis = self.analyze_shared_structure(task_ids)
        similarity = analysis['similarity_matrix']
        
        relationships = []
        n = len(task_ids)
        
        for i in range(n):
            for j in range(i + 1, n):
                if similarity[i, j] > 0.7:  # 高相似阈值
                    relationships.append({
                        'task1': task_names[i],
                        'task2': task_names[j],
                        'similarity': similarity[i, j],
                        'relationship': 'shared_dynamics'
                    })
        
        return relationships
    
    def visualize_embedding_space(
        self,
        task_ids: List[int],
        task_names: List[str]
    ):
        """
        可视化嵌入空间
        """
        import matplotlib.pyplot as plt
        from sklearn.decomposition import PCA
        
        embeddings = []
        for task_id in task_ids:
            emb = self.model.get_task_embedding(task_id)
            embeddings.append(emb.numpy())
        
        embeddings = np.array(embeddings)
        
        # PCA 降维
        pca = PCA(n_components=2)
        embeddings_2d = pca.fit_transform(embeddings)
        
        # 绘图
        plt.figure(figsize=(10, 8))
        plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], s=100)
        
        for i, name in enumerate(task_names):
            plt.annotate(name, (embeddings_2d[i, 0], embeddings_2d[i, 1]))
        
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.title('Task Embedding Space')
        plt.savefig('jedi_embedding_space.png')
        plt.close()


def infer_neural_dynamics(
    neural_data: np.ndarray,
    task_ids: List[int],
    n_neurons: int,
    n_epochs: int = 100
) -> Dict:
    """
    从神经数据推断动力学
    
    参数:
        neural_data: 神经数据列表 [(time, n_neurons), ...]
        task_ids: 任务 ID 列表
        n_neurons: 神经元数量
        n_epochs: 训练轮数
        
    返回:
        推断结果
    """
    # 创建模型
    n_tasks = max(task_ids) + 1
    model = JEDIModel(n_neurons=n_neurons, n_tasks=n_tasks)
    trainer = JEDITrainer(model)
    
    # 准备数据
    dataset = []
    for i, (data, task_id) in enumerate(zip(neural_data, task_ids)):
        tensor = torch.tensor(data, dtype=torch.float32).unsqueeze(0)
        dataset.append((tensor, task_id))
    
    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=1,
        shuffle=True
    )
    
    # 训练
    for epoch in range(n_epochs):
        loss = trainer.train_epoch(data_loader, task_ids)
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {loss:.6f}")
    
    # 提取动力学
    dynamics = {}
    for task_id in set(task_ids):
        dynamics[task_id] = trainer.extract_dynamics(task_id)
    
    return {
        'model': model,
        'dynamics': dynamics,
        'embeddings': {
            task_id: model.get_task_embedding(task_id).numpy()
            for task_id in set(task_ids)
        }
    }
```

## 应用场景

### 1. 多任务神经动力学分析
- 跨任务共享结构发现
- 任务特定动力学提取

### 2. 运动皮层记录分析
- 猴子到达任务
- 运动控制动力学

### 3. 神经群体建模
- 高维神经记录
- 低维动力学提取

## 方法优势

| 优势 | 说明 |
|------|------|
| **跨任务泛化** | 单一模型处理多任务 |
| **可扩展** | 适用于任意大规模数据集 |
| **可解释** | 反向工程揭示动力学机制 |
| **统一模型** | 单一框架捕获所有条件 |

## Activation Keywords
- 神经动力学
- RNN嵌入
- 多任务学习
- 群体神经
- neural dynamics
- population dynamics
- recurrent neural network
- embedding
- multi-task
- fixed points

## Tools Used
- torch
- numpy
- scikit-learn

## Instructions for Agents
1. 理解分层嵌入：任务嵌入 → RNN 权重
2. 掌握动力学分析：特征值、固定点
3. 注意权重生成：从嵌入到权重矩阵
4. 分析共享结构：跨任务嵌入相似性
5. 应用场景：多任务神经记录分析

## Examples
```python
# 使用示例
from jedi_neural_dynamics_inference import JEDIModel, JEDITrainer, MultiTaskDynamicsAnalyzer

# 1. 创建模型
model = JEDIModel(n_neurons=100, n_tasks=5)

# 2. 训练
trainer = JEDITrainer(model)
for epoch in range(100):
    loss = trainer.train_epoch(data_loader, task_ids)

# 3. 提取动力学
dynamics = trainer.extract_dynamics(task_id=0)
print(f"特征值: {dynamics['eigenvalues']}")
print(f"谱半径: {dynamics['spectral_radius']}")

# 4. 分析共享结构
analyzer = MultiTaskDynamicsAnalyzer(model)
structure = analyzer.analyze_shared_structure([0, 1, 2, 3, 4])

# 5. 发现任务关系
relationships = analyzer.find_task_relationships(
    task_ids=[0, 1, 2, 3, 4],
    task_names=['reach', 'grasp', 'hold', 'release', 'withdraw']
)
```

## 参考文献
- Jamkhandi, A.G., et al. (2026). "JEDI: Jointly Embedded Inference of Neural Dynamics" arXiv:2603.10489
- Sussillo, D., & Barak, O. (2013). "Opening the black box: low-dimensional dynamics in high-dimensional recurrent neural networks" Neural Computation