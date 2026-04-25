---
name: working-memory-recurrent-spiking-neural-networks
description: "Working memory implementation in recurrent Spiking Neural Networks using heterogeneous synaptic delays (D=41) and surrogate gradient BPTT, achieving perfect F1 on pattern storage and recall tasks."
triggers:
  - working memory SNN
  - recurrent spiking
  - heterogeneous delays
  - spiking motifs
  - delay learning
  - pattern storage
  - surrogate gradient
  - BPTT
paper: "2604.14096"
date_created: "2026-04-23"
---

# Working Memory in Recurrent Spiking Neural Networks 使用异质突触延迟的工作记忆方法论

## 概述

本方法论在循环脉冲神经网络(RSNN)中实现工作记忆功能，通过引入异质突触延迟(heterogeneous synaptic delays)和代理梯度BPTT训练，实现模式存储与回忆。权重张量 W∈R^{N×N×D} 编码了异质延迟连接，其中D=41个延迟槽位使得网络能够形成"脉冲基序"(Spiking Motifs)作为记忆的神经表征。

## 核心架构

### 1. 异质延迟连接模型

```
权重张量: W ∈ R^{N×N×D}

其中：
- N: 神经元数量
- D: 延迟槽位数 (默认 D=41)
- W[i,j,d]: 从神经元j到神经元i、延迟为d个时间步的突触权重

膜电位更新：
V_i(t) = V_i(t-1)·(1 - s_i(t-1)) + Σ_j Σ_d W[i,j,d]·s_j(t-d)

其中 s_i(t) 是神经元i在时间t的脉冲输出（0或1）
```

**延迟范围设计：**
- 延迟 d ∈ {1, 2, ..., D}，每个突触有D个独立的权重
- 这种参数化允许网络学习时间精确的脉冲链
- 延迟覆盖范围决定了记忆保持的最大时间跨度

### 2. 脉冲基序（Spiking Motifs）

```
概念：Spiking Motif = 跨时间的有序脉冲序列链

结构：
  神经元 A (t=0)  ──→  神经元 B (t=3)  ──→  神经元 C (t=7)
       │                      │                      │
       └── delay=3 ──┘       └── delay=4 ──┘

特性：
- 每个Spiking Motif编码一个特定模式/记忆
- 通过延迟连接形成自维持的脉冲循环
- 不同Motif可以并行存在（利用不同神经元子集）
- 精确的时序结构使得回忆具有确定性
```

### 3. 代理梯度BPTT训练

```python
class SurrogateGradientBPTT:
    """代理梯度反向传播通过时间"""
    
    def __init__(self, network, lr=1e-3, beta=5.0):
        self.network = network
        self.lr = lr
        self.beta = beta  # 代理梯度陡度参数
    
    def surrogate_derivative(self, x):
        """ATen代理梯度函数"""
        return self.beta / (2 * (1 + torch.cosh(self.beta * (x - 0.5))))
    
    def train_step(self, patterns):
        """
        训练步骤：
        1. 钳位输入模式到网络
        2. 自由运行多个时间步
        3. 计算回忆误差
        4. BPTT更新权重
        """
        self.network.reset_state()
        for pattern in patterns:
            self.network.clamp_input(pattern, duration=clamp_steps)
        
        recalls = []
        for t in range(free_run_steps):
            spikes = self.network.forward()
            recalls.append(spikes)
        
        loss = self.compute_recall_loss(recalls, patterns)
        loss.backward()
        self.optimizer.step()
```

### 4. 钳位初始化传播（Clamped Initialization Propagation）

```
存储过程：
1. 输入模式通过钳位(clamping)注入网络
   - 将指定神经元的膜电位强制设为目标值
   - 持续钳位 T_clamp 个时间步

2. 网络通过异质延迟连接形成Spiking Motifs
   - 钳位期间激活的神经元通过延迟连接传播
   - 形成自维持的循环脉冲链

回忆过程：
1. 给予部分提示(cue)：激活部分神经元
2. Spiking Motifs按学习到的延迟链传播
3. 完整模式被逐步回忆出来

提示→ 神经元A激活→ 延迟d₁→ 神经元B激活→ 延迟d₂→ ... → 完整回忆
```

## 实现指南

### 网络构建
```python
class WorkingMemoryRSNN(nn.Module):
    def __init__(self, N=200, D=41, tau_m=20.0, threshold=1.0):
        super().__init__()
        self.N = N
        self.D = D
        self.tau_m = tau_m
        self.threshold = threshold
        
        # 异质延迟权重张量
        self.W = nn.Parameter(torch.randn(N, N, D) * 0.1)
        self.spike_buffer = None
    
    def reset_state(self):
        self.v = torch.zeros(self.N)
        self.spike_buffer = torch.zeros(self.D, self.N)
    
    def forward(self, t):
        syn_input = torch.zeros(self.N)
        for d in range(self.D):
            syn_input += self.W[:, :, d] @ self.spike_buffer[d]
        
        self.v = self.v * (1 - 1/self.tau_m) + syn_input
        spikes = (self.v > self.threshold).float()
        self.v = self.v * (1 - spikes)
        
        self.spike_buffer = torch.roll(self.spike_buffer, 1, dims=0)
        self.spike_buffer[0] = spikes
        return spikes
    
    def clamp_pattern(self, pattern, duration=10):
        for _ in range(duration):
            self.v[pattern > 0] = self.threshold * 1.5
            spikes = self.forward(None)
```

## 关键实验结果

| 配置 | 存储模式数 | F1分数 | 备注 |
|------|:--------:|:-----:|------|
| D=41, N=200 | 5 | 1.00 | 完美回忆 |
| D=21, N=200 | 5 | ~0.95 | 延迟不足 |
| D=41, N=100 | 3 | ~0.98 | 容量限制 |
| D=1, N=200 | 2 | ~0.60 | 无异质延迟 |

## 应用场景

- **认知建模**：研究工作记忆的神经机制
- **神经形态计算**：低功耗记忆系统实现
- **序列学习**：时序模式存储与回忆
- **脉冲神经网络**：延迟连接的工程应用
- **脑启发AI**：短期记忆模块设计

## 注意事项

- 延迟范围D需要匹配任务的时间尺度需求
- 代理梯度的陡度参数β影响训练稳定性
- 大规模网络中权重张量W内存开销显著（N²×D）
- 钳位持续时间影响Spiking Motif形成的质量
- 训练时BPTT的梯度可能消失/爆炸，需要梯度裁剪
- 多个模式存储时需要足够的神经元池以避免串扰

## 参考文献

- Paper: 2604.14096 "Working Memory in a Recurrent Spiking Neural Network with Heterogeneous Delays"
- 相关：SNN Working Memory, Delay Learning, Surrogate Gradient Methods
