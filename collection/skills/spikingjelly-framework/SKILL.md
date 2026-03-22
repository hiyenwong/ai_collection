---
name: spikingjelly-framework
description: 脉冲神经网络深度学习框架 SpikingJelly 的使用指南。用于构建、训练和部署 SNN 模型，支持神经形态数据集处理和神经形态芯片部署。触发词：脉冲神经网络、SNN、SpikingJelly、spiking neural network、神经形态计算、neuromorphic computing。
user-invocable: true
---

# SpikingJelly: 脉冲神经网络深度学习框架

## 核心方法论

SpikingJelly 是一个开源的脉冲神经网络（SNN）深度学习框架，基于 PyTorch 构建，提供：

1. **神经形态数据集处理** - 支持 DVS、N-MNIST、CIFAR10-DVS 等事件驱动数据集
2. **深度 SNN 构建** - 模块化的神经元模型（LIF、IF、PLIF 等）
3. **训练优化** - 支持代理梯度、ANN-to-SNN 转换、直接训练
4. **神经形态芯片部署** - 支持部署到 Loihi、TrueNorth 等芯片

### 关键特性

- **加速训练**: 相比传统方法加速 11x
- **可扩展性**: 多级继承和半自动代码生成
- **灵活性**: 支持自定义神经元模型和网络架构

## 安装

```bash
pip install spikingjelly
```

## Python 代码示例

### 1. 基础 LIF 神经元网络

```python
import torch
import torch.nn as nn
from spikingjelly.activation_based import neuron, layer, functional

# 构建 SNN 网络
class SNNNet(nn.Module):
    def __init__(self, T=4):
        super().__init__()
        self.T = T  # 时间步长
        
        self.conv1 = layer.Conv2d(1, 32, kernel_size=3, padding=1)
        self.lif1 = neuron.LIFNode(tau=2.0, v_threshold=1.0)
        
        self.conv2 = layer.Conv2d(32, 64, kernel_size=3, padding=1)
        self.lif2 = neuron.LIFNode(tau=2.0, v_threshold=1.0)
        
        self.fc = layer.Linear(64 * 7 * 7, 10)
        self.lif3 = neuron.LIFNode(tau=2.0, v_threshold=1.0)
    
    def forward(self, x):
        # 静态输入转为脉冲序列
        x = x.unsqueeze(0).repeat(self.T, 1, 1, 1, 1)
        
        for t in range(self.T):
            out = self.conv1(x[t])
            out = self.lif1(out)
            out = self.conv2(out)
            out = self.lif2(out)
            out = out.view(out.size(0), -1)
            out = self.fc(out)
            out = self.lif3(out)
        
        return out

# 训练循环
model = SNNNet()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for data, target in train_loader:
    optimizer.zero_grad()
    output = model(data)
    loss = functional.spike_rate_loss(output, target)
    loss.backward()
    optimizer.step()
    
    # 重置神经元状态
    functional.reset_net(model)
```

### 2. ANN-to-SNN 转换

```python
from spikingjelly.activation_based import ann2snn

# 定义 ANN 模型
ann = nn.Sequential(
    nn.Conv2d(1, 32, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(32, 64, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(64 * 7 * 7, 10)
)

# 转换为 SNN
snn_converter = ann2snn.Converter(mode='max')
snn = snn_converter(ann)

# 推理
with torch.no_grad():
    for t in range(T):
        output = snn(data)
```

### 3. 神经形态数据集处理

```python
from spikingjelly.datasets import dvs128_gesture, pad_sequence_collate

# 加载 DVS Gesture 数据集
dataset = dvs128_gesture.DVS128Gesture(
    root='./data',
    train=True,
    data_type='event'  # 事件格式
)

# 转换为帧格式
from spikingjelly.datasets import ToFrame

transform = ToFrame(
    frames_number=10,  # 转换为10帧
    split_by='time'
)

dataset = dvs128_gesture.DVS128Gesture(
    root='./data',
    train=True,
    data_type='frame',
    frames_number=10
)

dataloader = torch.utils.data.DataLoader(
    dataset,
    batch_size=16,
    shuffle=True,
    collate_fn=pad_sequence_collate
)
```

### 4. 代理梯度训练

```python
from spikingjelly.activation_based import surrogate

# 使用自定义代理函数
class CustomLIFNode(neuron.LIFNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.surrogate_function = surrogate.PiecewiseQuadratic(
            alpha=0.5,
            spiking=True
        )

# 或使用预定义代理函数
lif = neuron.LIFNode(
    tau=2.0,
    surrogate_function=surrogate.ATan(alpha=2.0)
)
```

### 5. 神经形态芯片部署

```python
from spikingjelly.deployment import loihi

# 导出 Loihi 兼容格式
loihi.export_model(
    model=snn_model,
    input_shape=(1, 28, 28),
    output_path='./loihi_model'
)
```

## 应用场景

1. **低功耗边缘计算** - SNN 在神经形态芯片上能耗极低
2. **事件驱动视觉** - DVS 相机的实时处理
3. **时序模式识别** - 利用神经元动态特性处理时序数据
4. **神经科学研究** - 模拟生物神经网络
5. **机器人控制** - 低延迟、低功耗的实时控制

## 性能优化建议

1. **时间步选择**: T=4-8 通常足够，过多会降低效率
2. **tau 参数**: 根据任务动态特性调整膜时间常数
3. **阈值设置**: v_threshold 影响稀疏性和精度平衡
4. **批处理**: 使用 `functional.reset_net()` 在每个批次后重置状态

## Activation Keywords
- 脉冲神经网络
- SNN
- SpikingJelly
- spiking neural network
- 神经形态计算
- neuromorphic computing
- LIF神经元
- 代理梯度
- ANN-to-SNN转换
- DVS数据集

## Tools Used
- pytorch
- spikingjelly
- numpy

## Instructions for Agents
1. 理解LIF神经元：膜电位更新、脉冲生成、状态重置
2. 掌握代理梯度：解决脉冲函数不可微的问题
3. 实现ANN-to-SNN转换：将训练好的ANN转为SNN
4. 处理神经形态数据集：DVS Gesture、N-MNIST等
5. 注意时间步选择：T=4-8通常足够

## Examples
```python
# 使用示例
from spikingjelly.activation_based import neuron, layer, functional

# 1. 构建SNN
class SNNNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = layer.Linear(784, 256)
        self.lif1 = neuron.LIFNode(tau=2.0)
        self.fc2 = layer.Linear(256, 10)
        self.lif2 = neuron.LIFNode(tau=2.0)
    
    def forward(self, x, T=4):
        for t in range(T):
            out = self.lif1(self.fc1(x))
            out = self.lif2(self.fc2(out))
        return out

# 2. 训练后重置状态
functional.reset_net(model)
```

## 参考资源

- [SpikingJelly 文档](https://spikingjelly.readthedocs.io/)
- [GitHub 仓库](https://github.com/fangwei123456/spikingjelly)
- Paper: arXiv:2310.16620