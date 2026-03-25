# Neural Dynamics Decision-Making Models

## 激活关键词

- neural dynamics decision-making
- drift diffusion model
- evidence accumulation
- decision-making neural circuits
- accumulator model
- state-space decision model

## 来源论文

**arXiv:** 2001.04571
**效用:** 0.94
**标题:** Unifying and generalizing models of neural dynamics during decision-making

## 核心内容

### 统一框架

将决策理论模型与神经活动建模统一：
- **经典漂移扩散模型 (DDM)** - 单维度证据累积
- **多维累积器** - 多证据维度
- **可变边界** - 动态决策阈值
- **坍缩边界** - 紧急决策机制
- **离散跳跃** - 突发证据更新

### 技术方法

**循环状态空间模型 (RNN-SSM)**
- 参数化约束实现不同决策模型
- 可扩展的变分拉普拉斯 EM 推断
- 支持 spike 数据直接拟合

### 应用场景

1. **神经解码** - 从 spike 数据推断决策变量
2. **模型比较** - 比较不同决策模型拟合度
3. **神经元分类** - 识别累积器 vs 感觉神经元

## 使用工具

- `read` - 读取神经数据文件
- `exec` - 运行 Python 分析脚本
- `web_fetch` - 获取论文详细内容

## 实现步骤

### 1. 数据准备

```python
# 神经活动数据格式
# trials: N trials × T timebins × M neurons
# choices: N binary choices
# stimulus: N stimulus strengths
```

### 2. 模型选择

```python
# 单累积器模型
config = {
    'model_type': 'single_accumulator',
    'boundary': 'fixed'  # or 'collapsing', 'variable'
}

# 多维累积器模型
config = {
    'model_type': 'multi_accumulator',
    'dimensions': 2,
    'boundary': 'collapsing'
}
```

### 3. 推断与拟合

```python
# 变分拉普拉斯 EM 算法
# 1. E-step: 推断隐状态轨迹
# 2. M-step: 更新模型参数
# 迭代至收敛
```

### 4. 模型验证

- AIC/BIC 比较不同模型
- 后验预测检验
- 参数恢复测试

## 关键发现

1. **双维累积器** - 顶叶皮层某些神经元需要 2D 累积器解释
2. **可变下边界** - LIP 神经元显示动态决策阈值
3. **模型统一** - DDM 是 RNN-SSM 的特例

## 相关技能

- `drift-diffusion-model` - 经典 DDM
- `recurrent-state-space-model` - RNN 状态空间
- `neural-decoding` - 神经解码方法

## 参考文献

- Zoltowski et al. (2020) - 原始论文
- Ratcliff & McKoon (2008) - DDM 综述
- Brunton et al. (2013) - 多维累积器