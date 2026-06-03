---
name: drl-gnn-brain-network
description: 深度强化学习引导图神经网络脑网络分析方法论。结合DRL和GNN进行脑网络分析。适用于脑网络分类、疾病诊断。触发词：深度强化学习、图神经网络、脑网络、DRL-GNN。
user-invocable: true
---

# DRL-GNN Brain Network Analysis

## 核心思想

深度强化学习引导图神经网络，优化脑网络表示学习。

**来源：** arXiv:2203.10093
**效用：** 0.92

---

## 实现

```python
import torch.nn as nn

class DRLGNN(nn.Module):
    def __init__(self, n_feat, n_hidden, n_class):
        super().__init__()
        self.gnn = nn.Linear(n_feat, n_hidden)
        self.policy = nn.Linear(n_hidden, n_class)
    
    def forward(self, x, adj):
        h = torch.relu(self.gnn(adj @ x))
        return self.policy(h)
```

---

## Activation Keywords
- 深度强化学习
- 图神经网络
- 脑网络

## Tools Used
- torch

## Instructions for Agents
1. 构建脑网络图
2. 使用DRL优化GNN
3. 进行分类

## Examples
脑疾病分类诊断。

## 参考文献
- arXiv:2203.10093