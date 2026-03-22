---
name: am-mteeg-classification
description: 基于脉冲关联记忆的多任务 EEG 分类方法（AM-MTEEG）。受海马体学习记忆原理启发，实现跨个体 BCI 分类，具有生物可解释性。触发词：EEG分类、多任务学习、关联记忆、associative memory、跨个体BCI、海马体启发、hippocampus-inspired。
user-invocable: true
---

# AM-MTEEG: Multi-task EEG Classification with Associative Memory

## 核心方法论

AM-MTEEG 受海马体学习记忆原理启发，提出多任务 EEG 分类框架：

1. **脉冲神经表示** - 模拟海马体神经元的脉冲编码
2. **双向关联记忆** - Hopfield 式记忆矩阵用于特征-类别映射
3. **多任务学习** - 每个个体作为独立任务，跨个体共享特征
4. **生物可解释性** - 神经发放模式与海马体编码高度协调

### 核心优势

- 提高平均分类准确率
- 减少跨个体性能方差
- 提供波形重建可解释性
- 神经发放模式具有生物相似性

## Python 代码示例

### 1. 脉冲神经表示模块

```python
import torch
import torch.nn as nn
import numpy as np

class SpikingNeuronPopulation(nn.Module):
    """脉冲神经群体模块 - 模拟海马体神经元的脉冲编码"""
    
    def __init__(self, n_neurons, n_inputs, tau=20.0, threshold=1.0):
        super().__init__()
        self.n_neurons = n_neurons
        self.tau = tau
        self.threshold = threshold
        self.weights = nn.Parameter(torch.randn(n_inputs, n_neurons) * 0.1)
        self.register_buffer('membrane_potential', torch.zeros(1, n_neurons))
    
    def reset_state(self, batch_size=1):
        self.membrane_potential = torch.zeros(batch_size, self.n_neurons)
    
    def forward(self, x, time_steps=10):
        batch_size = x.shape[0]
        self.reset_state(batch_size)
        spike_output = []
        
        for t in range(time_steps):
            current = torch.matmul(x, self.weights)
            self.membrane_potential = self.membrane_potential * np.exp(-1.0 / self.tau) + current
            spikes = (self.membrane_potential > self.threshold).float()
            self.membrane_potential = self.membrane_potential * (1 - spikes)
            spike_output.append(spikes)
        
        spike_output = torch.stack(spike_output, dim=1)
        spike_rate = spike_output.mean(dim=1)
        return spike_output, spike_rate
```

### 2. 卷积编码器-解码器

```python
class ConvEncoderDecoder(nn.Module):
    """卷积编码器-解码器 - 提取共享的 EEG 特征"""
    
    def __init__(self, n_channels, n_timepoints, latent_dim=64):
        super().__init__()
        
        self.encoder = nn.Sequential(
            nn.Conv1d(n_channels, 32, kernel_size=5, stride=2, padding=2),
            nn.BatchNorm1d(32), nn.ELU(),
            nn.Conv1d(32, 64, kernel_size=5, stride=2, padding=2),
            nn.BatchNorm1d(64), nn.ELU(),
            nn.Conv1d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.BatchNorm1d(128), nn.ELU(),
            nn.Flatten(),
            nn.Linear(128 * (n_timepoints // 8), latent_dim)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 128 * (n_timepoints // 8)),
            nn.Unflatten(1, (128, n_timepoints // 8)),
            nn.ConvTranspose1d(128, 64, kernel_size=5, stride=2, padding=2, output_padding=1),
            nn.BatchNorm1d(64), nn.ELU(),
            nn.ConvTranspose1d(64, 32, kernel_size=5, stride=2, padding=2, output_padding=1),
            nn.BatchNorm1d(32), nn.ELU(),
            nn.ConvTranspose1d(32, n_channels, kernel_size=5, stride=2, padding=2, output_padding=1)
        )
    
    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return latent, reconstructed
```

### 3. 双向关联记忆矩阵

```python
class BidirectionalAssociativeMemory(nn.Module):
    """双向关联记忆（BAM）- Hopfield 式记忆矩阵"""
    
    def __init__(self, feature_dim, n_classes, n_memories=16):
        super().__init__()
        self.memory_features = nn.Parameter(torch.randn(n_memories, feature_dim) * 0.1)
        self.memory_classes = nn.Parameter(torch.randn(n_memories, n_classes) * 0.1)
        self.association_matrix = nn.Parameter(torch.zeros(feature_dim, n_classes))
    
    def update_association(self):
        """Hebbian 学习更新关联矩阵"""
        with torch.no_grad():
            self.association_matrix.data = torch.mm(self.memory_features.T, self.memory_classes)
    
    def forward(self, features):
        class_output = torch.mm(features, self.association_matrix)
        class_probs = torch.softmax(class_output, dim=-1)
        reconstructed_features = torch.mm(class_probs, self.association_matrix.T)
        return class_output, reconstructed_features
```

### 4. 完整 AM-MTEEG 模型

```python
class AM_MTEEG(nn.Module):
    """AM-MTEEG: 完整的多任务 EEG 分类模型"""
    
    def __init__(self, n_channels, n_timepoints, n_classes, n_tasks=10, latent_dim=64, n_neurons=128):
        super().__init__()
        self.n_tasks = n_tasks
        
        self.encoder_decoder = ConvEncoderDecoder(n_channels, n_timepoints, latent_dim)
        self.spiking_population = SpikingNeuronPopulation(n_neurons=n_neurons, n_inputs=latent_dim)
        self.bam = BidirectionalAssociativeMemory(feature_dim=n_neurons, n_classes=n_classes)
        
        self.task_adapters = nn.ModuleList([
            nn.Sequential(nn.Linear(latent_dim, latent_dim), nn.ELU())
            for _ in range(n_tasks)
        ])
    
    def forward(self, x, task_id=None):
        latent, reconstructed = self.encoder_decoder(x)
        if task_id is not None:
            latent = self.task_adapters[task_id](latent)
        spike_output, spike_rate = self.spiking_population(latent)
        logits, _ = self.bam(spike_rate)
        return logits, reconstructed, spike_output
```

## 应用场景

1. **跨个体 BCI** - 减少个体差异影响
2. **运动想象分类** - 手部运动想象识别
3. **情绪识别** - EEG 情绪状态分类
4. **注意力监测** - 注意力状态检测

## 生物可解释性

1. **脉冲编码** - 类似海马体神经元的发放模式
2. **关联记忆** - 模拟海马体的情景记忆机制
3. **波形重建** - 提供分类决策的可视化解释

## Activation Keywords
- EEG分类
- 多任务学习
- 关联记忆
- associative memory
- 跨个体BCI
- 海马体启发
- hippocampus-inspired
- 脉冲神经网络
- SNN

## Tools Used
- Python
- PyTorch
- NumPy
- SciPy

## Instructions for Agents
1. 确认任务类型是否为EEG分类或脑机接口相关
2. 检查数据格式（通道数、时间点数、类别数）
3. 根据数据规模选择合适的模型参数（神经元数量、潜在维度）
4. 实现脉冲神经群体模块进行特征编码
5. 使用双向关联记忆进行分类
6. 如需跨个体迁移，启用任务适配器

## Examples
```python
# 使用AM-MTEEG进行EEG分类
model = AM_MTEEG(
    n_channels=64,
    n_timepoints=1000,
    n_classes=4,
    n_tasks=10
)

# 前向传播
eeg_data = torch.randn(32, 64, 1000)  # batch, channels, timepoints
logits, reconstructed, spikes = model(eeg_data, task_id=0)

# 分类预测
predictions = logits.argmax(dim=1)
```

## 参考文献

- Paper: arXiv:2409.18375