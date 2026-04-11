# Fractional-order Spiking Neural Network (f-SNN)

## Overview

分数阶脉冲神经网络框架。使用分数阶微分方程替代传统整数阶 ODE，捕获膜电位和脉冲序列的长期依赖，实现更丰富的时序模式表达能力。

**来源论文：** arXiv:2507.16937 - Fractional-order Spiking Neural Network

## 触发词

分数阶 SNN、f-SNN、fractional SNN、非马尔可夫 SNN、长期依赖 SNN、fractional-order spiking、分数阶神经元

## 核心方法

### 动机

传统 IF/LIF 模型是一阶 ODE，具有**马尔可夫特性**：当前状态仅依赖于紧邻的过去值。

真实神经元显示：
- 长程相关性
- 分形树突结构
- 非马尔可夫行为

### 分数阶扩展

| 传统 SNN | 分数阶 SNN |
|---------|-----------|
| 整数阶 ODE | 分数阶 ODE |
| 马尔可夫 | 非马尔可夫 |
| 短期依赖 | 长期依赖 |
| 有限表达力 | 更丰富时序模式 |

### 开源工具

**spikeDE**：支持 f-SNN 多种架构的开源工具箱

## 使用场景

### 适用情况

- 需要捕获长期时序依赖的任务
- 生物真实性要求高的模拟
- 复杂时序模式识别
- 记忆密集型任务

### 数据要求

- 时序数据流
- 需要历史信息积累的任务

## 实施步骤

1. **模型选择**
   - 选择分数阶 LIF 或其他变体
   - 设置分数阶数 α (0 < α < 1)

2. **动力学定义**
   - 分数阶微分方程
   - 脉冲发放阈值

3. **训练**
   - 使用 spikeDE 工具箱
   - 适配反向传播或代理梯度

4. **评估**
   - 对比整数阶 SNN
   - 分析长期依赖捕获能力

## 技术细节

### 分数阶微分

- α 接近 1：接近传统整数阶
- α 接近 0：更强的长期依赖
- 中间值：平衡局部和全局信息

### 优势

1. 严格推广整数阶 SNN
2. 自动捕获长期记忆
3. 更丰富的动力学行为

## 与其他方法对比

| 方法 | 长期依赖 | 生物真实性 | 计算复杂度 |
|------|---------|-----------|-----------|
| f-SNN | ✅ 分数阶 | ✅ 高 | ⚠️ 中等 |
| LIF | ❌ 马尔可夫 | ⚠️ 中等 | ✅ 低 |
| LSTM-SNN | ✅ 门控 | ⚠️ 中等 | ⚠️ 高 |

## 工具使用

- `exec`: 运行 spikeDE 工具箱
- `read`: 查看分数阶配置参数
- `web_fetch`: 获取开源代码

## 注意事项

- 分数阶导数计算需要历史积分
- 内存占用可能高于传统 SNN
- α 参数需要调优

## 扩展阅读

- 相关技能：`spikingjelly-framework`（SNN 框架）
- 相关技能：`decolle-snn-learning`（局部学习）
- 相关技能：`bio-neuron-snn-learning`（生物神经元学习）
- 论文链接：https://arxiv.org/abs/2507.16937
## Description

Fractional-order Spiking Neural Network (f-SNN)

## Activation Keywords

- fractional-order-snn
- fractional-order-snn 技能
- fractional-order-snn skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 模型选择

### Step 2: 动力学定义

### Step 3: 训练

### Step 4: 评估

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Fractional-order Spiking Neural Network (f-SNN) to my analysis.

**Agent:** I'll help you apply fractional-order-snn. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for fractional-order-snn?

**Agent:** Let me search for the latest research and best practices...
