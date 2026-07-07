---
name: flow-based-connectivity-distribution
version: v1.0.0
last_updated: 2026-04-18
description: "Flow-based probabilistic inference for neural connectivity distribution. Uses normalizing flows to model the distribution of possible brain connectomes, enabling uncertainty quantification in connectivity estimation. Supports downstream tasks: network analysis, disease classification, and intervention planning with principled uncertainty estimates."
category: neuroscience
tags:
  - connectivity
  - distributional-inference
  - normalizing-flows
  - uncertainty-quantification
  - brain-network
  - probabilistic-modeling
paper:
  title: "Flow-based Connectivity Distribution Inference"
  published: "2026-04-16"
  url: "https://arxiv.org/abs/2604.11761"
activation: "flow-based, connectivity distribution, normalizing flows, uncertainty, probabilistic, brain network"
---

# Flow-based Connectivity Distribution Inference

## 概述

使用标准化流（Normalizing Flows）对脑连接组分布进行建模的概率推断方法。与传统点估计方法不同，该方法提供连接估计的不确定性量化，支持下游任务的可靠决策。

## 核心创新

将连接组推断从**点估计**提升为**分布推断**，使用标准化流学习连接空间上的概率分布。

## 方法论

### 标准化流架构

```python
class ConnectivityFlow(nn.Module):
    """使用标准化流建模连接分布"""
    
    def forward(self, base_dist):
        # 从简单分布（如高斯）采样
        z = base_dist.sample()
        # 通过可逆变换映射到连接空间
        for transform in self.transforms:
            z, log_det = transform(z)
        connectivity = z
        return connectivity, log_det.sum()
```

### 训练策略

1. **似然最大化**：最大化观测数据的边际似然
2. **变分推断**：使用流作为灵活的后验近似
3. **条件生成**：以协变量（年龄、疾病状态）为条件

### 不确定性量化

- **连接强度不确定性**：每条边的后验分布
- **网络指标不确定性**：传播连接到图指标的分布
- **分类不确定性**：结合连接不确定性进行疾病分类

## 应用场景

- **连接组推断**：从 fMRI/DTI 数据估计连接及其不确定性
- **疾病分类**：结合不确定性的鲁棒分类
- **干预规划**：考虑不确定性的最优干预策略

## 参考文献

```bibtex
@article{flow2026,
    title={Flow-based Connectivity Distribution Inference},
    journal={arXiv preprint arXiv:2604.11761},
    year={2026}
}
```

---
*Generated on 2026-04-18*