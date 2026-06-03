---
name: green-wearable-computing-physics
description: "Towards Green Wearable Computing: A Physics-Aware Spiking Neural Network for Energy-Efficient IMU-ba... Activation: 物理感知, spiking, physics-aware, snn"
---

# Towards Green Wearable Computing: A Physics-Aware Spiking Neural Network for Energy-Efficient IMU-based Human Activity Recognition

## 概述
Wearable IMU-based Human Activity Recognition (HAR) relies heavily on Deep Neural Networks (DNNs), which are burdened by immense computational and buffering demands. Their power-hungry floating-point operations and rigid requirement to process complete temporal windows severely cripple battery-constrained edge devices. While Spiking Neural Networks (SNNs) offer extreme event-driven energy efficiency, standard architectures struggle with complex biomechanical topologies and temporal gradient degr

## 来源论文
- **标题:** Towards Green Wearable Computing: A Physics-Aware Spiking Neural Network for Energy-Efficient IMU-based Human Activity Recognition
- **作者:** Naichuan Zheng, Hailun Xia, Zepeng Sun, Weiyi Li, Yinze Zhou
- **arXiv:** 2604.10458v1
- **发布日期:** 2026-04-12
- **类别:** None

## 核心概念
- 脉冲神经网络(spiking neural network)
- SNN(snn)
- 物理感知(physics-aware)
- 人体活动识别(human activity recognition)

## 核心贡献
1. To bridge this gap, we propose the Physics-Aware Spiking Neural Network (PAS-Net), a fully multiplier-free architecture explicitly tailored for Green HAR.
2. 详见论文原文
3. 详见论文原文

## 技术方法
- While Spiking Neural Networks (SNNs) offer extreme event-driven energy efficiency, standard architectures struggle with complex biomechanical topologies and temporal gradient degradation
- To bridge this gap, we propose the Physics-Aware Spiking Neural Network (PAS-Net), a fully multiplier-free architecture explicitly tailored for Green HAR

## 应用领域
- 可穿戴设备活动识别
- 人体活动识别

## 实现要点
### 关键组件
- 数据预处理管道
- 神经网络架构设计
- 训练策略与优化
- 评估指标与验证

### 技术挑战
- To bridge this gap, we propose the Physics-Aware Spiking Neural Network (PAS-Net), a fully multiplier-free architecture explicitly tailored for Green HAR.
- 详见论文讨论部分

## 实验结果
Evaluated across seven diverse datasets, PAS-Net achieves state-of-the-art accuracy while replacing dense operations with sparse 0.1 pJ integer accumulations.

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
- Naichuan Zheng et al. (2026). "Towards Green Wearable Computing: A Physics-Aware Spiking Neural Network for Energy-Efficient IMU-based Human Activity Recognition." arXiv:2604.10458v1.

## 激活关键词
- 物理感知
- spiking
- physics-aware
- snn

---
*技能自动生成于: 2026-04-15*
*来源: arXiv自动化研究工作流*
