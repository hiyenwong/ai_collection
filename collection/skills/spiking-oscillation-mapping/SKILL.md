---
name: spiking-oscillation-mapping-v2
description: "Systematic regime mapping of oscillatory states in balanced spiking networks with multiple time scales. Analyzes transitions between silent, asynchronous-irregular, and oscillatory states. Activation: spiking oscillation mapping, balanced network regimes, multi-time-scale SNN, 脉冲振荡机制映射, 平衡网络动力学."
arxiv_id: 2604.04770
---

# Spiking Oscillation Mapping in Balanced Networks

## Description

平衡脉冲神经网络可以在静默、异步不规则和振荡状态之间转换，这取决于相互作用的突触和时间尺度，但其联合参数结构仍未完全表征。

本研究系统映射了突触后衰减(τs)、传导延迟(d)和可塑性率(λp)如何共同塑造递归 leaky integrate-and-fire 网络中的振荡机制。通过结合 Brian2 模拟和 Hopf 参考边界，构建了直接可视化 SIL-AI-OSC 转换的机制图。

## Core Methodology

### 1. Parameter Space Exploration
三个关键时间尺度：
- **τs (postsynaptic decay)**: 突触后衰减时间常数
- **d (conduction delay)**: 传导延迟
- **λp (plasticity rate)**: 可塑性率

### 2. Network Regimes
三种主要动力学状态：
- **SIL (Silent)**: 静默状态
- **AI (Asynchronous-Irregular)**: 异步不规则发放
- **OSC (Oscillatory)**: 振荡状态

### 3. Brian2 Simulation Framework
```python
# 网络配置
eqs = '''
dv/dt = (ge + gi - v + I) / tau_m : volt
ge : volt
gi : volt
'''
```

## Key Findings

### 1. Regime Boundaries
- Hopf 分岔边界
- 双稳态区域
- 临界转换线

### 2. Multi-Time-Scale Interactions
- 快衰减 vs 慢衰减
- 短延迟 vs 长延迟
- 突触可塑性的影响

### 3. Biological Relevance
- 皮层振荡模式
- 注意力调节
- 睡眠-觉醒周期

## Applications

### 1. Computational Neuroscience
- 理解皮层动力学
- 神经振荡建模
- 病理状态分析

### 2. Neuromorphic Engineering
- 优化 SNN 设计
- 脉冲编码策略
- 能量效率优化

### 3. Brain-Inspired AI
- 振荡神经网络
- 时序信息处理
- 注意力机制

## Activation Keywords
- spiking oscillation mapping
- balanced network regimes
- multi-time-scale SNN
- 脉冲振荡机制映射
- 平衡网络动力学
- Brian2 simulation
- neural regime transitions

## Related Skills
- spiking-oscillation-mapping
- spiking-neural-network-training
- brain-neuromorphic
- snn-multimodal-brain

## References
- arXiv: 2604.04770
- Paper: Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales
- PDF: https://arxiv.org/pdf/2604.04770

_Last updated: 2026-04-13_


## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
