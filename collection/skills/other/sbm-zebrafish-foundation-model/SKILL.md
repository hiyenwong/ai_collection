---
name: sbm-zebrafish-foundation-model
arxiv_id: 2510.27366v1
utility: 0.88
tags: '[zebrafish, foundation model, whole-brain, neural dynamics, behavior, sparse attention, SBM]'
created: 2026-03-31
description: "Zebrafish Whole-Brain Foundation Model (SBM)"
---

# Zebrafish Whole-Brain Foundation Model (SBM)

## Activation Keywords

- 斑马鱼全脑模型
- zebrafish foundation model
- SBM sparse brain model
- whole-brain neural dynamics
- behavior neural pattern synthesis
- neuron spike prediction

## Problem Statement

全脑神经动力学建模的挑战：
- 单神经元分辨率难以扩展到全脑
- 现有模型忽略行为输出
- PCA/conv 方法遗漏长程非线性交互
- 缺乏行为引导的神经模式探索

## Method Overview

Fatehmanesh et al. (2025) 提出 SBM：
1. 稀疏注意力全脑基础模型
2. 条件预测神经元脉冲概率
3. 脑状态与行为关联
4. 梯度合成目标行为的神经模式

## Tools Used

- `Component` - Analysis component
- `Sparse Attention` - Analysis component
- `Factorized Attention` - Analysis component
- `Behavior Head` - Analysis component
- `Gradient Synthesis` - Analysis component

## Architecture

```
Sensory Stimuli
        ↓
┌─────────────────────────────────────┐
│  Sparse Attention Whole-Brain Model │
│  ┌─────────────────────────────┐    │
│  │ Factorized Attention        │    │
│  │ - Across Neurons (spatial)  │    │
│  │ - Along Time (temporal)     │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
        ↓
   Spike Probabilities
        ↓
┌─────────────────────────────────────┐
│  Permutation-Invariant Behavior Head│
│  - Links brain state to behavior    │
└─────────────────────────────────────┘
        ↓
   Behavior Prediction / Neural Pattern Synthesis
```

## Key Results

| Metric | Value |
|--------|-------|
| Mean Absolute Error | < 0.02 |
| Prediction Calibration | Calibrated |
| Autoregressive Rollouts | Stable |

## Step-by-Step Instructions

### SBM 实现

1. **稀疏注意力机制**
   ```python
   import torch
   import torch.nn as nn
   import torch.nn.functional as F
   
   class SparseAttention(nn.Module):
       def __init__(self, dim, num_heads=8, sparsity=0.1):
           super().__init__()
           self.num_heads = num_heads
           self.head_dim = dim // num_heads
           self.sparsity = sparsity
           
           self.qkv = nn.Linear(dim, dim * 3)
           self.proj = nn.Linear(dim, dim)
           
       def forward(self, x, mask=None):
           B, N, C = x.shape
           qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, self.head_dim)
           q, k, v = qkv.unbind(2)
           
           # 计算注意力分数
           attn = (q @ k.transpose(-2, -1)) * (self.head_dim ** -0.5)
           
           # 稀疏化：只保留 top-k
           k_keep = int(N * self.sparsity)
           topk_values, topk_idx = attn.topk(k_keep, dim=-1)
           
           # 创建稀疏注意力矩阵
           sparse_attn = torch.zeros_like(attn)
           sparse_attn.scatter_(-1, topk_idx, topk_values)
           sparse_attn = F.softmax(sparse_attn, dim=-1)
           
           # 应用注意力
           x = (sparse_attn @ v).transpose(1, 2).reshape(B, N, C)
           return self.proj(x)
   ```

2. **因式分解注意力（神经元×时间）**
   ```python
   class FactorizedAttention(nn.Module):
       """因式分解注意力：分离空间和时间"""
       def __init__(self, dim, num_neurons, num_heads=8):
           super().__init__()
           
           # 空间注意力（跨神经元）
           self.spatial_attn = SparseAttention(dim, num_heads, sparsity=0.1)
           
           # 时间注意力（沿时间）
           self.temporal_attn = nn.MultiheadAttention(dim, num_heads)
           
           self.norm1 = nn.LayerNorm(dim)
           self.norm2 = nn.LayerNorm(dim)
           
       def forward(self, x):
           # x: (batch, time, neurons, dim)
           B, T, N, D = x.shape
           
           # 空间注意力：对每个时间点，跨神经元
           x_spatial = x.reshape(B * T, N, D)
           x_spatial = self.spatial_attn(x_spatial)
           x_spatial = x_spatial.reshape(B, T, N, D)
           
           x = self.norm1(x + x_spatial)
           
           # 时间注意力：对每个神经元，沿时间
           x_temporal = x.permute(2, 0, 1, 3)  # (N, B, T, D)
           x_temporal = x_temporal.reshape(N, B * T, D)
           
           x_temporal, _ = self.temporal_attn(x_temporal, x_temporal, x_temporal)
           x_temporal = x_temporal.reshape(N, B, T, D).permute(1, 2, 0, 3)
           
           x = self.norm2(x + x_temporal)
           
           return x
   ```

3. **行为预测头**
   ```python
   class PermutationInvariantBehaviorHead(nn.Module):
       """置换不变的行为预测头"""
       def __init__(self, neuron_dim, num_behaviors, hidden_dim=256):
           super().__init__()
           
           # 神经元级处理
           self.neuron_encoder = nn.Sequential(
               nn.Linear(neuron_dim, hidden_dim),
               nn.ReLU(),
               nn.Linear(hidden_dim, hidden_dim)
           )
           
           # 置换不变聚合
           self.aggregation = nn.Sequential(
               nn.Linear(hidden_dim, hidden_dim),
               nn.ReLU(),
               nn.Linear(hidden_dim, num_behaviors)
           )
           
       def forward(self, neural_activity):
           """
           neural_activity: (batch, neurons, dim)
           输出: (batch, num_behaviors)
           """
           # 编码每个神经元
           neuron_features = self.neuron_encoder(neural_activity)  # (B, N, H)
           
           # 置换不变聚合（mean pooling）
           global_features = neuron_features.mean(dim=1)  # (B, H)
           
           # 行为预测
           behavior = self.aggregation(global_features)
           
           return behavior
   ```

4. **神经模式合成**
   ```python
   class NeuralPatternSynthesis:
       """梯度合成目标行为的神经模式"""
       def __init__(self, sbm_model, behavior_head):
           self.model = sbm_model
           self.behavior_head = behavior_head
           
       def synthesize(self, target_behavior_idx, stimuli, num_steps=100):
           """合成产生目标行为的神经模式"""
           # 初始化神经活动
           neural_activity = torch.randn(1, num_neurons, seq_len, dim, requires_grad=True)
           
           optimizer = torch.optim.Adam([neural_activity], lr=0.1)
           
           for step in range(num_steps):
               optimizer.zero_grad()
               
               # 前向传播
               spike_probs = self.model(neural_activity, stimuli)
               behavior_pred = self.behavior_head(spike_probs)
               
               # 最大化目标行为概率
               loss = -behavior_pred[0, target_behavior_idx]
               
               # 正则化：保持生物学合理性
               reg = 0.01 * (neural_activity ** 2).mean()
               total_loss = loss + reg
               
               total_loss.backward()
               optimizer.step()
               
               if step % 10 == 0:
                   print(f"Step {step}: behavior_prob = {behavior_pred[0, target_behavior_idx]:.3f}")
           
           return neural_activity.detach()
   ```

## Example Usage

```python
import torch

# 初始化 SBM
sbm = SparseBrainModel(
    num_neurons=10000,      # 斑马鱼全脑神经元数量
    dim=256,
    num_heads=8
)

# 行为预测头
behavior_head = PermutationInvariantBehaviorHead(
    neuron_dim=256,
    num_behaviors=10  # 例如：游泳、捕食、逃避等
)

# 预测脉冲概率
stimuli = load_visual_stimulus()  # 感觉刺激
spike_probs = sbm(neural_state, stimuli)

# 预测行为
behavior = behavior_head(spike_probs)

# 合成目标行为的神经模式
synthesis = NeuralPatternSynthesis(sbm, behavior_head)
pattern = synthesis.synthesize(target_behavior_idx=2, stimuli=stimuli)
```

## Applications

| 应用 | 描述 |
|------|------|
| 神经动力学预测 | 给定刺激预测神经元活动 |
| 行为解码 | 从神经活动预测行为 |
| 模式合成 | 生成目标行为的神经模式 |
| 机制探索 | 行为引导的神经现象研究 |

## Description

Zebrafish Whole-Brain Foundation Model (SBM)

**Key Concepts:**
- 全脑神经动力学建模的挑战：
- 单神经元分辨率难以扩展到全脑
- 现有模型忽略行为输出
- PCA/conv 方法遗漏长程非线性交互
- 缺乏行为引导的神经模式探索

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 稀疏注意力机制

### Step 2: 因式分解注意力（神经元×时间）

### Step 3: 行为预测头

### Step 4: 神经模式合成

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Zebrafish Whole-Brain Foundation Model (SBM) to my analysis.

**Agent:** I'll help you apply sbm-zebrafish-foundation-model. First, let me understand your specific use case...

**Context:** 全脑神经动力学建模的挑战：
- 单神经元分辨率难以扩展到全脑
- 现有模型忽略行为输出
- PCA/conv 方法遗漏长程非线性交互
- 缺乏行为引导的神经模式

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for sbm-zebrafish-foundation-model?

**Agent:** Let me search for the latest research and best practices...

## References

- Fatehmanesh, S. et al. (2025). A Sensing Whole Brain Zebrafish Foundation Model for Neuron Dynamics and Behavior. arXiv:2510.27366.

## Related Skills

- neural-dynamics-universal-translator
- neural-code-dynamics-analysis
- bio-neuron-snn-learning