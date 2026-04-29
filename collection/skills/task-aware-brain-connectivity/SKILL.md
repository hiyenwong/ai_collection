---
name: task-aware-brain-connectivity
description: "任务感知有效脑连接学习方法论（TBDS）。使用DAG学习框架从fMRI时间序列构建任务相关的脑网络，结合图神经网络进行分类。 触发词: task-aware, brain connectivity, DAG learning, 任务感知, 脑连接"
---

# 任务感知有效脑连接学习方法论

## 概述
任务感知有效脑连接学习方法论（TBDS）。使用DAG学习框架从fMRI时间序列构建任务相关的脑网络，结合图神经网络进行分类。

## 核心概念

1. **任务感知学习 (Task-Aware Learning)**
2. **有效连接 (Effective Connectivity)**
3. **DAG学习 (DAG Learning)**
4. **因果发现 (Causal Discovery)**
5. **图神经网络分类 (GNN Classification)**

## 应用领域

- 神经疾病诊断
- 认知状态分类
- 个体指纹识别
- 任务性能预测

## 方法论与实现


## 方法论

### 1. 任务感知 DAG 学习
```python
import numpy as np
import torch
import torch.nn as nn

def learn_task_aware_dag(fmri_data, task_labels, lambda1=0.1, lambda2=0.1):
    '''
    学习任务感知的DAG结构
    fmri_data: [subjects, time_points, regions]
    task_labels: [subjects] 任务标签
    '''
    n_subjects, t, n_regions = fmri_data.shape
    
    # 初始化邻接矩阵
    W = np.zeros((n_regions, n_regions))
    
    # NOTEARS 算法变体
    for subject in range(n_subjects):
        X = fmri_data[subject]  # [time, regions]
        
        # 考虑任务标签的加权
        task_weight = get_task_importance(task_labels[subject])
        
        # 计算条件独立性
        for i in range(n_regions):
            for j in range(n_regions):
                if i != j:
                    # 使用偏相关或条件互信息
                    score = compute_causal_score(X[:, i], X[:, j], X[:, [k for k in range(n_regions) if k != i and k != j]])
                    W[i, j] += task_weight * score
    
    # 无环约束投影
    W = project_dag(W)
    return W

def project_dag(W):
    '''确保无环性'''
    # 使用拓扑排序或循环移除
    # 简化版: 保留上三角矩阵
    W_dag = np.triu(W, k=1)
    return W_dag
```

### 2. 图神经网络分类器
```python
class TaskAwareGNN(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, num_layers=3):
        super().__init__()
        self.convs = nn.ModuleList()
        self.convs.append(nn.Linear(in_channels, hidden_channels))
        
        for _ in range(num_layers - 1):
            self.convs.append(nn.Linear(hidden_channels, hidden_channels))
        
        self.classifier = nn.Linear(hidden_channels, out_channels)
        self.task_embedding = nn.Embedding(10, hidden_channels)  # 任务嵌入
    
    def forward(self, x, edge_index, task_id):
        # x: [nodes, features]
        # edge_index: [2, edges] DAG边
        # task_id: 任务ID
        
        for conv in self.convs:
            x = torch.relu(conv(x))
        
        # 融入任务信息
        task_embed = self.task_embedding(task_id)
        x = x + task_embed
        
        # 全局池化
        x = x.mean(dim=0)
        
        return self.classifier(x)
```

### 3. 端到端训练
```python
def train_task_aware_model(model, data_loader, optimizer, epochs=100):
    for epoch in range(epochs):
        for batch in data_loader:
            fmri, dag_adj, task_id, label = batch
            
            optimizer.zero_grad()
            
            # 前向传播
            output = model(fmri, dag_adj, task_id)
            
            # 损失: 分类 + DAG 正则化
            loss = F.cross_entropy(output, label)
            loss += 0.01 * dag_regularization(dag_adj)  # 稀疏性约束
            
            loss.backward()
            optimizer.step()
```

## 应用实例

### 神经疾病诊断
```python
# 阿尔茨海默病 vs 正常对照
model = TaskAwareGNN(in_channels=100, hidden_channels=64, out_channels=2)

# 准备数据: fMRI + 任务标签
train_data = load_fmri_with_tasks('ADNI', tasks=['rest', 'memory', 'attention'])

# 训练
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
train_task_aware_model(model, train_data, optimizer)
```

### 个体指纹识别
```python
def fingerprint_identification(model, fmri_data, subject_id):
    '''
    使用任务感知连接进行个体识别
    '''
    model.eval()
    # 提取连接特征
    with torch.no_grad():
        features = model.extract_features(fmri_data)
    
    # 与数据库比对
    similarity = cosine_similarity(features, database_features)
    predicted_id = np.argmax(similarity)
    
    return predicted_id == subject_id
```

## 优势

1. **任务特异性**: 针对不同认知任务学习专门的连接模式
2. **因果解释**: DAG结构提供方向性连接，增强可解释性
3. **分类性能**: 任务感知特征提升下游分类准确率
4. **泛化能力**: 跨任务和跨被试的泛化性能提升


## 激活关键词
- task-aware, brain connectivity, DAG learning, 任务感知, 脑连接
- neuroscience
- brain
- neural

---
*该 skill 基于神经科学领域知识创建（arXiv API 暂时不可用）*
