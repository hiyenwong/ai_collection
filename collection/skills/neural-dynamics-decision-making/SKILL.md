---
name: neural-dynamics-decision-making
description: Neural Dynamics Decision-Making Models
---

# Neural Dynamics Decision-Making Models

## Description

统一决策理论模型与神经活动建模的框架，包括经典漂移扩散模型（DDM）、多维累积器、可变边界等扩展。

## Activation Keywords

- neural dynamics decision-making
- drift diffusion model
- evidence accumulation
- decision-making neural circuits
- accumulator model
- state-space decision model

## Tools Used

- `read` - 读取神经数据文件
- `exec` - 运行 Python 分析脚本
- `web_fetch` - 获取论文详细内容

## Instructions for Agents

### 1. 理解统一框架

决策理论模型与神经活动的统一：
- **经典漂移扩散模型 (DDM)** - 单维度证据累积
- **多维累积器** - 多证据维度
- **可变边界** - 动态决策阈值
- **坍缩边界** - 紧急决策机制
- **离散跳跃** - 突发证据更新

### 2. 技术方法

**循环状态空间模型 (RNN-SSM)**
- 参数化约束实现不同决策模型
- 可扩展的变分拉普拉斯 EM 推断
- 支持 spike 数据直接拟合

### 3. 应用场景

1. **神经解码** - 从 spike 数据推断决策变量
2. **模型比较** - 比较不同决策模型拟合度
3. **神经元分类** - 识别累积器 vs 感觉神经元

### 4. 实现步骤

```python
# 数据准备
# trials: N trials × T timebins × M neurons
# choices: N binary choices
# stimulus: N stimulus strengths

# 模型选择
config = {
    'model_type': 'multi_accumulator',  # or 'single_accumulator'
    'dimensions': 2,
    'boundary': 'collapsing'  # or 'fixed', 'variable'
}

# 推断与拟合：变分拉普拉斯 EM 算法
# E-step: 推断隐状态轨迹
# M-step: 更新模型参数
# 迭代至收敛

# 模型验证
# - AIC/BIC 比较不同模型
# - 后验预测检验
# - 参数恢复测试
```

## Examples

### Example 1: 分析顶叶皮层神经元的决策动力学

```
User: 帮我分析猴子顶叶皮层神经元在随机点运动任务中的决策动力学

Agent: 我将使用 neural-dynamics-decision-making 技能来分析。

首先，我需要了解数据格式：
- 试验数量、时间仓数、神经元数量
- 选择和刺激强度信息

根据 arXiv:2001.04571 的方法：
1. 使用多维累积器模型（2D 累积器更好地解释顶叶神经元）
2. 设置可变下边界（LIP 神经元显示动态决策阈值）
3. 应用变分拉普拉斯 EM 推断

预期发现：
- 双维累积器比单累积器更好地拟合顶叶神经元
- 某些 LIP 神经元显示可变下边界
```

### Example 2: 模型比较与选择

```
User: 如何比较 DDM 和多维累积器模型哪个更适合我的数据？

Agent: 使用 AIC/BIC 信息准则进行比较：

1. 拟合单累积器模型，记录 AIC1, BIC1
2. 拟合双累积器模型，记录 AIC2, BIC2
3. 比较 ΔAIC = AIC2 - AIC1 和 ΔBIC = BIC2 - BIC1

决策规则：
- Δ < -2: 支持复杂模型（双累积器）
- Δ > 2: 支持简单模型（单累积器）
- -2 ≤ Δ ≤ 2: 无法区分

arXiv:2001.04571 的研究发现，顶叶皮层神经元需要双维累积器解释。
```

## Source

- **arXiv:** 2001.04571
- **效用:** 0.94
- **标题:** Unifying and generalizing models of neural dynamics during decision-making

## Key Findings

1. **双维累积器** - 顶叶皮层某些神经元需要 2D 累积器解释
2. **可变下边界** - LIP 神经元显示动态决策阈值
3. **模型统一** - DDM 是 RNN-SSM 的特例

## Related Skills

- `drift-diffusion-model` - 经典 DDM
- `recurrent-state-space-model` - RNN 状态空间
- `neural-decoding` - 神经解码方法

## References

- Zoltowski et al. (2020) - 原始论文
- Ratcliff & McKoon (2008) - DDM 综述
- Brunton et al. (2013) - 多维累积器