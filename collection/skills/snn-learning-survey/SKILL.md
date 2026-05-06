---
name: snn-learning-survey
description: 脉冲神经网络学习规则综合分析技能。涵盖无监督（STDP及变体）、监督（代理梯度）、强化学习及混合学习范式。提供SNN训练方法选择指南、关键参数配置和性能比较。适用于脉冲神经网络、神经形态计算、低功耗AI、事件驱动系统。触发词：SNN learning rules, STDP, surrogate gradient, neuromorphic computing, spiking neural network training, 脉冲神经网络学习
version: 1.0.0
metadata:
  hermes:
    tags: [neuroscience, spiking-neural-network, learning-rules, neuromorphic, training-methods]
    source_paper: "Learning rules in Spiking Neural Networks: A comprehensive survey (arXiv:2604.16060)"
    published: "2026-04-19"
---

# SNN Learning Rules Survey

## Overview

脉冲神经网络学习规则综合指南。涵盖四大类学习方法及其在神经形态硬件上的实现。

## Learning Rule Categories

### 1. Unsupervised Learning (STDP-based)
```python
def stdp_update(pre_spike, post_spike, weight, lr=0.01, 
                A_plus=0.1, A_minus=-0.12, tau_plus=20, tau_minus=20):
    """标准STDP更新规则"""
    if pre_spike and post_spike:
        # 时间依赖的权重更新
        dt = post_spike.time - pre_spike.time
        if dt > 0:  # 前突触先于后突触
            delta_w = A_plus * torch.exp(-dt / tau_plus)
        else:
            delta_w = A_minus * torch.exp(dt / tau_minus)
        weight = weight + lr * delta_w
    return weight.clamp(0, 1)
```

**STDP Variants:**
- Pair-based STDP: 标准脉冲对更新
- Triplet STDP: 考虑前/后脉冲三重态
- Voltage-based STDP: 加入膜电位依赖
- Reward-modulated STDP: 结合多巴胺信号

### 2. Supervised Learning (Surrogate Gradient)
```python
class SurrogateSpike(torch.autograd.Function):
    """代理梯度函数 - 使脉冲可微"""
    @staticmethod
    def forward(ctx, x, alpha=1.0):
        ctx.save_for_backward(x)
        ctx.alpha = alpha
        return (x > 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        # 使用分段线性替代导数
        alpha = ctx.alpha
        grad_input = grad_output * alpha * torch.relu(1 - torch.abs(x))
        return grad_input, None

# 使用示例
spike = SurrogateSpike.apply(membrane_potential, alpha=2.0)
```

### 3. Reinforcement Learning for SNNs
```python
class R_SNN(nn.Module):
    """奖励调制的脉冲神经网络"""
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, hidden_dim)
        self.out = nn.Linear(hidden_dim, output_dim)
        self.eligibility_trace = torch.zeros(hidden_dim, output_dim)
        
    def forward(self, x, reward=0):
        # 计算资格迹
        eligibility = torch.outer(self.spike_trace, self.output_trace)
        self.eligibility_trace = 0.9 * self.eligibility_trace + eligibility
        
        # 奖励调制更新
        if reward != 0:
            self.fc.weight += reward * self.eligibility_trace * 0.01
```

## Rule Selection Guide

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| 无标签数据 | STDP | 自组织学习，无需标注 |
| 分类任务 | 代理梯度 | 端到端训练，精度高 |
| 在线学习 | 奖励调制STDP | 适应动态环境 |
| 低功耗部署 | 二值SNN + STDP | 硬件友好 |

## Key Parameters

| 参数 | 典型范围 | 影响 |
|------|---------|------|
| 学习率 | 0.001-0.1 | 收敛速度和稳定性 |
| 时间窗口τ | 10-50ms | 时间依赖性强度 |
| 代理梯度α | 1-5 | 梯度传播质量 |
| 膜电位阈值 | 0.5-1.5 | 脉冲发放频率 |

## References
- Comprehensive survey of SNN learning rules. arXiv:2604.16060
