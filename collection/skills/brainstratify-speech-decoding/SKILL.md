---
name: brainstratify-speech-decoding
description: BrainStratify颅内神经动力学语音解码方法论。从粗到细的解耦框架，通过空间上下文引导的时空建模识别功能组，使用解耦乘积量化(DPQ)分离神经动力学。适用于sEEG/ECoG语音解码、BCI语音接口。触发词：语音解码、BrainStratify、sEEG、ECoG、神经解耦、speech decoding、intracranial、BCI。
user-invocable: true
---

# BrainStratify Speech Decoding - 颅内神经语音解码

## 核心思想

从粗到细的神经解耦框架，从 sEEG/ECoG 信号中解码语音，解决任务相关信号稀疏分布和纠缠问题。

**来源：** arXiv:2505.20480
**效用：** 1.0

---

## 挑战

1. **信号稀疏：** 任务相关神经信号在电极间稀疏分布
2. **信号纠缠：** 任务相关/无关信号混合

---

## 方法论

### 两阶段框架

**Stage 1: 功能组识别**
- 空间上下文引导的时空建模
- 识别任务相关电极组

**Stage 2: 神经动力学解耦**
- 解耦乘积量化 (DPQ)
- 分离功能组内的不同动力学

### DPQ 实现

```python
import numpy as np
import torch
import torch.nn as nn

class DecoupledProductQuantization(nn.Module):
    """解耦乘积量化"""
    
    def __init__(self, n_subspaces=8, n_centroids=256, dim=128):
        super().__init__()
        self.n_subspaces = n_subspaces
        self.subspace_dim = dim // n_subspaces
        
        # 每个子空间的码本
        self.codebooks = nn.Parameter(
            torch.randn(n_subspaces, n_centroids, self.subspace_dim)
        )
    
    def encode(self, x):
        """编码：找到最近质心"""
        # x: (batch, dim)
        batch_size = x.shape[0]
        x = x.view(batch_size, self.n_subspaces, self.subspace_dim)
        
        codes = []
        for i in range(self.n_subspaces):
            # 计算距离
            dist = torch.cdist(x[:, i:i+1], self.codebooks[i])
            code = torch.argmin(dist, dim=-1)
            codes.append(code)
        
        return torch.stack(codes, dim=1)
    
    def decode(self, codes):
        """解码：从码本重建"""
        # codes: (batch, n_subspaces)
        batch_size = codes.shape[0]
        reconstructed = []
        
        for i in range(self.n_subspaces):
            reconstructed.append(self.codebooks[i][codes[:, i]])
        
        return torch.cat(reconstructed, dim=-1)


class BrainStratify(nn.Module):
    """BrainStratify 框架"""
    
    def __init__(self, n_electrodes, n_features, hidden_dim=128):
        super().__init__()
        
        # Stage 1: 时空建模
        self.spatial_attn = nn.MultiheadAttention(hidden_dim, num_heads=4)
        self.temporal_conv = nn.Conv1d(n_features, hidden_dim, kernel_size=3, padding=1)
        
        # Stage 2: DPQ 解耦
        self.dpq = DecoupledProductQuantization()
        
        # 解码器
        self.decoder = nn.Linear(hidden_dim, n_features)
    
    def forward(self, x):
        """
        x: (batch, n_electrodes, n_times, n_features)
        """
        # 时空建模
        x = self.temporal_conv(x.flatten(0, 1)).unflatten(0, (x.shape[0], x.shape[1]))
        
        # 空间注意力
        x = x.permute(2, 0, 1, 3)  # (n_times, batch, n_electrodes, hidden)
        x, _ = self.spatial_attn(x, x, x)
        
        # DPQ 解耦
        x = x.permute(1, 2, 0, 3).flatten(-2)
        codes = self.dpq.encode(x)
        reconstructed = self.dpq.decode(codes)
        
        # 解码
        output = self.decoder(reconstructed)
        
        return output
```

---

## 应用场景

1. **语音 BCI：** 从神经信号直接解码语音
2. **功能定位：** 识别任务相关脑区
3. **信号解耦：** 分离不同神经动力学

---

## 数据集

- sEEG 语音产生数据集
- sEEG 语音感知数据集
- ECoG 语音数据集

---

## 关键参数

| 参数 | 推荐值 |
|------|--------|
| 子空间数 | 8 |
| 质心数 | 256 |
| 注意力头 | 4 |

---

## 参考文献

- arXiv:2505.20480 - BrainStratify: Coarse-to-Fine Disentanglement of Intracranial Neural Dynamics