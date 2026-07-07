---
name: bridge-neurodivergence-detection
description: BRIDGE神经多样性检测方法论。整合图规范建模和深度生成网络，创建神经典型发育轨迹参考，评估个体神经偏离程度。适用于神经发育障碍诊断、脑龄预测、连接组分析。触发词：神经多样性、神经发育障碍、脑龄、规范建模、neurodivergence、brain age。
user-invocable: true
---

# BRIDGE Neurodivergence Detection - 神经多样性检测

## 核心思想

整合图规范建模和深度生成网络，创建神经典型发育轨迹参考，量化神经偏离。

**来源：** arXiv:2410.11064
**效用：** 0.93

---

## 方法论

### 框架组件

- 规范建模：建立神经典型发育轨迹
- 深度生成模型：学习连接组变化
- 偏离评估：计算神经多样性分数

---

## 实现

```python
import torch.nn as nn

class BRIDGEModel(nn.Module):
    def __init__(self, n_regions=200, latent_dim=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_regions * n_regions, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.age_predictor = nn.Linear(latent_dim, 1)
    
    def predict_brain_age(self, connectivity):
        x = connectivity.flatten()
        h = self.encoder(x)
        return self.age_predictor(h)
    
    def compute_neurodivergence(self, conn, age):
        brain_age = self.predict_brain_age(conn)
        return abs(brain_age - age)
```

---

## Activation Keywords
- 神经多样性
- 神经发育障碍
- 脑龄
- 规范建模

## Tools Used
- torch
- numpy

## Instructions for Agents
1. 建立神经典型参考轨迹
2. 预测个体脑龄
3. 计算偏离分数

## Examples
评估自闭症儿童的脑连接偏离程度。

## 参考文献
- arXiv:2410.11064