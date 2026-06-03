---
name: conv-delay-learning-recurrent-snn
description: "Combining convolutional recurrent connections with DelRec delay learning mechanism for streamlined SNN architecture, achieving 99% recurrent parameter savings and 52x faster inference on audio classification tasks."
triggers:
  - convolutional SNN
  - delay learning
  - DelRec
  - recurrent spiking
  - convolution delay
  - SNN architecture
  - audio classification SNN
  - parameter efficient SNN
paper: "2604.15997"
date_created: "2026-04-23"
---

# 卷积延迟学习循环脉冲神经网络 (Conv+DelRec SNN) 方法论

## 概述

本方法论结合卷积循环连接与DelRec延迟学习机制，构建高效的脉冲神经网络架构。通过用卷积运算替代全连接循环权重矩阵，并利用DelRec方法学习异质突触延迟，实现99%的循环参数节省和52倍的推理加速，同时保持竞争力的音频分类性能。

## 核心架构

### 1. 传统循环SNN的问题

```
标准循环连接：
  全连接权重矩阵 W_rec ∈ R^{N×N}
  
  问题：
  1. 参数量大：N² 个参数（如 N=1000 → 1M 参数）
  2. 计算密集：O(N²) 矩阵乘法
  3. 内存占用高：权重存储和中间状态
  4. 训练困难：梯度消失/爆炸

  时间步更新：
    h(t) = f(W_rec · s(t-1) + W_in · x(t))
    其中 s(t-1) 是上一时间步的脉冲向量
```

### 2. 卷积循环连接（Convolutional Recurrent Connections）

```
核心思想：用卷积核替代全连接矩阵

标准循环：  W_rec ∈ R^{N×N}    → N² 参数
卷积循环：  K_conv ∈ R^{C×C×K×K} → C²·K² 参数

当 K << √N 时，参数量大幅减少

实现：
  h(t) = f(Conv2D(K_conv, s(t-1)) + Conv2D(K_in, x(t)))
  
  其中：
  - K_conv: 循环卷积核（空间局部连接）
  - K_in: 输入卷积核
  - s(t-1): 上一时间步的脉冲图（保持空间结构）

优势：
1. 参数共享：同一卷积核应用于所有空间位置
2. 局部连接：只连接空间邻近的神经元
3. 平移等变性：自然处理空间模式
4. 硬件友好：卷积运算高度优化
```

### 3. DelRec延迟学习机制

```
DelRec (Delay Reconstruction)：

原理：在卷积循环连接基础上，为每个突触学习延迟权重

权重分解：
  W_rec = K_conv ⊗ D_delay
  
  其中：
  - K_conv: 空间卷积核（学习空间模式）
  - D_delay: 延迟权重向量（学习时序模式）
  - ⊗: 张量积/外积

延迟缓冲区：
  对于延迟 d ∈ {1, 2, ..., D_max}：
  spike_buffer[d] 存储第 d 个时间步前的脉冲图
  
  循环输入：
  input_rec(t) = Σ_{d=1}^{D_max} K_conv(d) * spike_buffer[d]
  
  其中 K_conv(d) 是延迟d对应的卷积核（从分解得到）

参数效率：
  全连接循环：  N² = 1,000,000 (N=1000)
  卷积+延迟：  C²·K²·D = 64·9·20 = 11,520
  节省比例：  ~99%
```

### 4. 完整Conv+DelRec架构

```python
class ConvDelRecSNN(nn.Module):
    """卷积延迟学习循环SNN"""
    
    def __init__(self, in_channels, hidden_channels, 
                 kernel_size=3, n_delays=20, n_layers=4):
        super().__init__()
        self.n_delays = n_delays
        
        # 输入卷积层
        self.input_conv = nn.Conv2d(
            in_channels, hidden_channels, kernel_size, 
            padding=kernel_size//2
        )
        
        # 延迟卷积核：D个独立的卷积核
        self.delay_kernels = nn.ParameterList([
            nn.Parameter(torch.randn(hidden_channels, hidden_channels, 
                                     kernel_size, kernel_size) * 0.01)
            for _ in range(n_delays)
        ])
        
        # 读出层
        self.readout = nn.Linear(hidden_channels, n_classes)
        
        # LIF神经元参数
        self.tau_m = nn.Parameter(torch.ones(hidden_channels) * 20.0)
        self.threshold = nn.Parameter(torch.ones(hidden_channels))
        
    def forward(self, x_seq):
        """
        Args:
            x_seq: [T, B, C, H, W] 输入脉冲序列
        Returns:
            output: [B, n_classes] 分类输出
        """
        T, B, C, H, W = x_seq.shape
        
        # 初始化状态
        v = torch.zeros(B, self.hidden_channels, H, W)  # 膜电位
        spike_buffer = [torch.zeros(B, self.hidden_channels, H, W) 
                       for _ in range(self.n_delays)]
        
        output_accumulator = torch.zeros(B, self.hidden_channels, H, W)
        
        for t in range(T):
            # 输入卷积
            input_current = self.input_conv(x_seq[t])
            
            # 延迟循环卷积
            recurrent_current = torch.zeros_like(v)
            for d in range(self.n_delays):
                delayed_spikes = spike_buffer[d]
                conv_result = F.conv2d(
                    delayed_spikes, 
                    self.delay_kernels[d],
                    padding=self.delay_kernels[d].shape[-1]//2
                )
                recurrent_current += conv_result
            
            # LIF神经元动力学
            total_current = input_current + recurrent_current
            v = v * (1 - 1/self.tau_m.unsqueeze(-1).unsqueeze(-1)) + total_current
            
            # 脉冲生成
            spikes = (v > self.threshold.unsqueeze(-1).unsqueeze(-1)).float()
            v = v * (1 - spikes)  # 重置
            
            # 更新延迟缓冲区
            spike_buffer.insert(0, spikes.detach())
            spike_buffer.pop()  # 移除最旧的
            
            # 累积输出
            output_accumulator += spikes
        
        # 全局平均池化 + 读出
        pooled = output_accumulator.mean(dim=[-2, -1])  # [B, C]
        output = self.readout(pooled)
        
        return output
```

### 5. 训练策略

```python
def train_conv_delrec(model, train_loader, optimizer, n_epochs=100):
    """Conv+DelRec训练流程"""
    
    surrogate = ATenSurrogate(alpha=5.0)  # 代理梯度函数
    
    for epoch in range(n_epochs):
        for batch in train_loader:
            spike_input = encode_to_spikes(batch['audio'])  # 音频→脉冲
            
            # 前向传播
            output = model(spike_input)
            
            # 损失计算（交叉熵 + 活动正则化）
            loss_ce = F.cross_entropy(output, batch['label'])
            loss_reg = firing_rate_reg(model, target_rate=0.1)
            loss = loss_ce + 0.01 * loss_reg
            
            # 代理梯度BPTT
            optimizer.zero_grad()
            loss.backward()
            
            # 梯度裁剪（防止延迟权重的梯度爆炸）
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
```

## 关键实验结果

### 参数效率对比

| 方法 | 循环参数量 | 总参数量 | 准确率 |
|------|:---------:|:-------:|:-----:|
| 全连接RSNN | 1,000K | 1,050K | 92.3% |
| Conv-RSNN | 5.8K | 55K | 91.8% |
| **Conv+DelRec** | **5.8K×D=116K** | **165K** | **93.1%** |
| 参数节省 | 99% | 84% | +0.8% |

### 推理速度对比

| 方法 | 推理时间/样本 | 加速比 | GPU利用率 |
|------|:----------:|:-----:|:--------:|
| FC-RSNN | 52ms | 1x | 23% |
| Conv-RSNN | 2.1ms | 25x | 78% |
| **Conv+DelRec** | **1.0ms** | **52x** | **91%** |

### 音频分类性能（SHD/SSC数据集）

| 数据集 | Conv+DelRec | 最佳RSNN | 最佳ANN |
|--------|:----------:|:-------:|:------:|
| SHD | 93.1% | 92.3% | 94.5% |
| SSC | 81.2% | 79.8% | 83.0% |

## 延迟学习可视化

```
学到的延迟卷积核示意（D=20中的选择）：

延迟 d=1 (即时):
  ┌─────────────┐
  │ 0  0.1  0   │   强中心响应
  │ 0.1 0.8 0.1 │   类似兴奋性连接
  │ 0  0.1  0   │
  └─────────────┘

延迟 d=5 (短程):
  ┌─────────────┐
  │ 0.2  0  0.2 │   扩散模式
  │  0  0.3  0  │   局部传播
  │ 0.2  0  0.2 │
  └─────────────┘

延迟 d=15 (长程):
  ┌─────────────┐
  │-0.1 0.1 -0.1│   抑制性模式
  │ 0.1 -0.2 0.1│   负反馈
  │-0.1 0.1 -0.1│
  └─────────────┘
```

## 应用场景

- **音频分类**：语音命令识别、环境声分类
- **神经形态硬件**：低功耗边缘推理
- **时间序列**：事件驱动的时序数据处理
- **语音增强**：噪声环境下的语音分离
- **可穿戴设备**：超低功耗音频感知

## 注意事项

- 延迟数量D需要匹配信号的时序特征尺度
- 卷积核大小K影响空间感受野和参数量的平衡
- 代理梯度陡度参数α需要调优以稳定训练
- 延迟缓冲区的内存占用为 O(D·B·C·H·W)
- 大D值时梯度路径变长，可能需要分层延迟学习
- 音频编码方式（频率/时间/ cochlear）影响最终性能

## 参考文献

- Paper: 2604.15997 "Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks"
- 相关：DelRec, SNN Architecture Design, Audio Classification with SNNs


## Activation Keywords

- conv-delay-learning-recurrent-snn
- conv delay learning
- conv delay learning recurrent snn


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Conv Delay Learning Recurrent Snn

**Agent:** Conv Delay Learning Recurrent Snn 是关于...
