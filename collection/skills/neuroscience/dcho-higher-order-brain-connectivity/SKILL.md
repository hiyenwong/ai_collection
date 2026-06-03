---
name: dcho-higher-order-brain-connectivity
description: DCHO高阶脑连接预测方法论。通过分解-组合框架预测三个或更多脑区之间的相互作用，捕获比传统成对连接更丰富的组织信息。适用于脑网络预测、状态分类、脑动力学预测。触发词：高阶脑连接、HOBC、脑网络预测、分解组合、higher-order connectivity、brain dynamics。
user-invocable: true
---

# DCHO Higher-Order Brain Connectivity - 高阶脑连接预测

## 核心思想

通过分解-组合框架预测高阶脑连接（HOBC）的时序演化，捕获三个或更多脑区之间的相互作用。

**来源：** arXiv:2509.09696
**效用：** 0.99

---

## 方法论

### 分解-组合策略

| 阶段 | 任务 |
|------|------|
| 分解 | HOBC 推断 + 潜在轨迹预测 |
| 组合 | 多尺度拓扑特征 + 高阶信息 |

### 实现框架

```python
import torch
import torch.nn as nn

class DCHOModel(nn.Module):
    """DCHO高阶脑连接预测模型"""
    
    def __init__(self, n_regions=200, latent_dim=64):
        super().__init__()
        
        # 双视图编码器
        self.local_encoder = nn.Sequential(
            nn.Linear(n_regions, 128),
            nn.ReLU(),
            nn.Linear(128, latent_dim)
        )
        
        self.global_encoder = nn.Sequential(
            nn.Linear(n_regions * n_regions, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        
        # 潜在组合学习器
        self.combiner = nn.Sequential(
            nn.Linear(latent_dim * 2, latent_dim),
            nn.ReLU(),
            nn.Linear(latent_dim, latent_dim)
        )
        
        # 轨迹预测器
        self.predictor = nn.LSTM(latent_dim, latent_dim, batch_first=True)
    
    def encode(self, fc_matrix):
        """多尺度编码"""
        local_feat = self.local_encoder(fc_matrix.mean(dim=1))
        global_feat = self.global_encoder(fc_matrix.flatten())
        return self.combiner(torch.cat([local_feat, global_feat], dim=-1))
    
    def predict_trajectory(self, fc_sequence):
        """预测脑动力学轨迹"""
        latents = [self.encode(fc) for fc in fc_sequence]
        latents = torch.stack(latents, dim=1)
        output, _ = self.predictor(latents)
        return output
```

---

## 应用场景

1. 脑状态分类
2. 脑动力学预测
3. 神经疾病诊断

---

## Activation Keywords
- 高阶脑连接
- HOBC
- 脑网络预测
- 分解组合

## Tools Used
- torch
- numpy

## Instructions for Agents
1. 提取多尺度拓扑特征
2. 学习高阶连接信息
3. 预测时序演化

## Examples
预测fMRI时间序列中的高阶脑连接变化。

## 参考文献
- arXiv:2509.09696