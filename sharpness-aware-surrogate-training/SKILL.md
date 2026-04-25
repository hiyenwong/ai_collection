---
name: sharpness-aware-surrogate-training
description: "Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks... Activation: spiking, snn"
---

# Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks

## 概述
Spiking neural networks (SNNs) are a natural computational model for on-sensor and near-sensor vision, where event driven processors must operate under strict power budgets with hard binary spikes. However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy. We study Sharpness-Aware Surrogate Training (SAST), which applies Sharp

## 来源论文
- **标题:** Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks
- **作者:** Maximilian Nicholson
- **arXiv:** 2604.09696v1
- **发布日期:** 2026-04-06
- **类别:** None

## 核心概念
- 脉冲神经网络(spiking neural network)
- SNN(snn)
- 锐度感知(sharpness-aware)

## 核心贡献
1. 详见论文原文
2. 详见论文原文
3. 详见论文原文

## 技术方法
- Spiking neural networks (SNNs) are a natural computational model for on-sensor and near-sensor vision, where event driven processors must operate under strict power budgets with hard binary spikes
- However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy

## 应用领域
- 可穿戴设备活动识别

## 实现要点
### 关键组件
- 数据预处理管道
- 神经网络架构设计
- 训练策略与优化
- 评估指标与验证

### 技术挑战
- However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy.
- We study Sharpness-Aware Surrogate Training (SAST), which applies Sharpness-Aware Minimization (SAM) to a surrogate-forward SNN so that the training objective is smooth and the gradient is exact, and position it as one gap-reduction strategy under the tested settings rather than the only viable mechanism.

## 实验结果
However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy.

## 代码示例
```python
# 核心架构示例

# 脉冲神经网络示例
import torch
import torch.nn as nn

class SNNLayer(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.fc = nn.Linear(input_size, hidden_size)
        self.threshold = 1.0
        
    def forward(self, x):
        # 前向传播与脉冲生成
        mem = self.fc(x)
        spike = (mem > self.threshold).float()
        return spike

```

## 限制与展望
- 当前方法的主要限制
- 未来研究方向
- 潜在改进空间

## 参考文献
- Maximilian Nicholson et al. (2026). "Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks." arXiv:2604.09696v1.

## 激活关键词
- spiking
- snn

---
*技能自动生成于: 2026-04-15*
*来源: arXiv自动化研究工作流*
