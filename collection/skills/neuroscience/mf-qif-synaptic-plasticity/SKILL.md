---
name: mf-qif-synaptic-plasticity
version: 1.0.0
last_updated: 2026-03-26
description: 'Mean-field approximations for networks of spiking neurons with short-term synaptic plasticity, enabling macroscopic analysis of neural dynamics.'
source: arXiv:2101.06057v2
utility: 0.93
tags: '[mean-field, spiking neurons, QIF, synaptic plasticity, neural mass model]'
---

# Mean-Field QIF Networks with Short-Term Synaptic Plasticity

## 概述

平均场近似方法，用于描述具有短时程突触可塑性的二次积分发放（QIF）神经元网络。

**核心特点：**
- 低维描述神经网络动力学
- 跨尺度桥接脑结构和功能
- 预突触短时程可塑性建模
- 周期性爆发活动和双稳态机制

**应用：**
- 神经质量模型开发
- 宏观神经活动分析
- 短时程适应建模

## 激活关键词

- mean field qif
- short-term synaptic plasticity
- quadratic integrate-and-fire
- neural mass model
- mean-field approximation
- presynaptic plasticity

## 核心概念

### 1. 二次积分发放（QIF）神经元

```python
# QIF 神经元模型
class QIFNeuron:
    """
    二次积分发放神经元

    dv/dt = v² + η + I(t)
    当 v → ∞ 时发放，重置到 -∞
    """
    def __init__(self, eta=0.0):
        self.eta = eta  # 异质性参数
        self.v = -float('inf')  # 初始膜电位

    def update(self, I, dt):
        """更新膜电位"""
        self.v += (self.v**2 + self.eta + I) * dt
        if self.v > self.threshold:
            self.v = -float('inf')
            return True  # 发放
        return False
```

### 2. 短时程突触可塑性

```python
# 预突触短时程可塑性模型
class ShortTermPlasticity:
    """
    短时程突触可塑性（STP）

    基于Tsodyks-Markram模型：
    - u: 利用参数
    - x: 资源可用性
    - 短时程抑制（STD）
    - 短时程易化（STF）
    """
    def __init__(self, U=0.5, D=0.1, F=0.05):
        self.U = U  # 利用参数
        self.D = D  # 抑制时间常数
        self.F = F  # 易化时间常数
        self.u = U
        self.x = 1.0  # 资源可用性

    def update(self, spike, dt):
        """更新突触状态"""
        du = -self.u / self.F + self.U * (1 - self.u) * spike
        dx = (1 - self.x) / self.D - self.u * self.x * spike

        self.u += du * dt
        self.x += dx * dt

        return self.u * self.x  # 突触效能
```

### 3. 平均场方程

```python
# 平均场方程推导
class MeanFieldQIF:
    """
    QIF 网络的平均场近似

    宏观变量：
    - r: 平均发放率
    - v: 平均膜电位
    - s: 突触变量

    dr/dt = Δ/π + 2rv
    dv/dt = v² + η₀ + Jr - (πr)²
    ds/dt = -s/τs + r * plasticity_factor
    """
    def __init__(self, J=15.0, eta_0=-5.0, Delta=1.0, tau_s=5.0):
        self.J = J           # 耦合强度
        self.eta_0 = eta_0   # 平均输入
        self.Delta = Delta   # 异质性宽度
        self.tau_s = tau_s   # 突触时间常数

        # 状态变量
        self.r = 0.01  # 发放率
        self.v = -2.0  # 平均电位
        self.s = 0.0   # 突触变量

    def step(self, dt):
        """积分一个时间步"""
        # 发放率方程
        dr = (self.Delta / 3.14159 + 2 * self.r * self.v) * dt

        # 电位方程
        dv = (self.v**2 + self.eta_0 +
              self.J * self.s - (3.14159 * self.r)**2) * dt

        # 突触方程（包含可塑性）
        ds = (-self.s / self.tau_s + self.r * self.plasticity_factor()) * dt

        self.r += dr
        self.v += dv
        self.s += ds
```

## 动态机制

### 1. 周期性爆发活动

```python
# 爆发活动检测
def detect_bursting(r_timeseries, threshold=0.1):
    """
    检测周期性爆发活动

    特征：
    - 高频发放后跟随静默期
    - 短时程可塑性驱动
    """
    peaks = []
    for i, r in enumerate(r_timeseries):
        if r > threshold:
            peaks.append(i)

    if len(peaks) > 2:
        intervals = np.diff(peaks)
        period = np.mean(intervals)
        return True, period
    return False, None
```

### 2. 双稳态机制

```python
# 双稳态分析
def analyze_bistability(mf_model, param_range):
    """
    分析参数空间中的双稳态

    方法：分岔分析
    - 找到稳定不动点
    - 检测鞍点分岔
    """
    fixed_points = []

    for J in param_range:
        mf_model.J = J
        # 找不动点
        fp = find_fixed_point(mf_model)
        stability = analyze_stability(mf_model, fp)
        fixed_points.append((J, fp, stability))

    return fixed_points
```

## 使用场景

### 神经质量模型开发

```python
# 完整的平均场模型
class NeuralMassModel:
    """
    神经质量模型（包含短时程可塑性）

    适用场景：
    - EEG/MEG 信号建模
    - 麻醉深度分析
    - 癫痫发作建模
    """
    def __init__(self, n_populations=1):
        self.populations = [MeanFieldQIF() for _ in range(n_populations)]
        self.plasticity = [ShortTermPlasticity() for _ in range(n_populations)]

    def simulate(self, duration, dt=0.1):
        """模拟网络动力学"""
        times = np.arange(0, duration, dt)
        r_history = []

        for t in times:
            for pop, pl in zip(self.populations, self.plasticity):
                pop.step(dt)
                pl.update(pop.r, dt)

            r_history.append([pop.r for pop in self.populations])

        return times, np.array(r_history)
```

### 宏观活动分析

```python
# 分岔分析
from scipy.optimize import fsolve

def bifurcation_analysis(model, param_name, param_range):
    """
    分岔分析

    Args:
        model: 平均场模型
        param_name: 参数名称
        param_range: 参数范围

    Returns:
        分岔图数据
    """
    results = {'stable': [], 'unstable': [], 'saddle': []}

    for param_val in param_range:
        setattr(model, param_name, param_val)

        # 求解不动点
        def equations(state):
            model.r, model.v, model.s = state
            return model.dynamics()

        try:
            fp = fsolve(equations, [model.r, model.v, model.s])
            stability = check_stability(model, fp)
            results[stability].append((param_val, fp))
        except:
            pass

    return results
```

## 与其他模型比较

| 模型 | 优势 | 局限 |
|------|------|------|
| 本方法 | 准确描述确定性网络 | 数学较复杂 |
| 随机发放假设 | 数学简单 | 对确定性网络不准确 |
| 速率模型 | 计算高效 | 缺乏时序信息 |

## 实现步骤

### 1. 参数校准

```python
# 从微观到宏观参数映射
def calibrate_parameters(n_neurons=10000, g=15.0, eta_mean=-5.0):
    """
    从微观网络参数校准平均场参数

    微观参数：
    - n_neurons: 神经元数量
    - g: 耦合强度
    - eta_mean: 平均输入

    宏观参数：
    - J = g / N
    - η₀ = η_mean
    """
    return {
        'J': g / np.sqrt(n_neurons),
        'eta_0': eta_mean,
        'Delta': 1.0  # 异质性宽度
    }
```

### 2. 验证平均场近似

```python
# 与微观模拟比较
def validate_mean_field(mf_model, spiking_network, duration):
    """
    验证平均场近似的准确性

    方法：
    1. 运行微观网络模拟
    2. 计算宏观活动（发放率）
    3. 与平均场预测比较
    """
    # 微观模拟
    r_micro = spiking_network.simulate(duration)

    # 平均场模拟
    t, r_macro = mf_model.simulate(duration)

    # 比较
    error = np.mean((r_micro - r_macro[:, 0])**2)

    return error
```

## 代码资源

**论文引用：** arXiv:2101.06057

## 相关技能

- `kuramoto-brain-network` - 耦合振子平均场
- `neuromodulated-synaptic-plasticity` - 神经调制可塑性
- `bcmi-motion-control-detection` - BCI 应用
- `bio-neuron-snn-learning` - 生物神经元 SNN

## 参考文献

```bibtex
@article{montbrio2021meanfield,
  title={Mean-field approximations of networks of spiking neurons with short-term synaptic plasticity},
  author={Montbrió, Ernest and Pazó, Diego and others},
  journal={arXiv preprint arXiv:2101.06057},
  year={2021}
}
```

## 适用领域

- 神经质量模型开发
- EEG/MEG 信号建模
- 麻醉状态分析
- 癫痫发作建模
- 短时程可塑性研究
## Activation Keywords

- mf-qif-synaptic-plasticity
- mf-qif-synaptic-plasticity 技能
- mf-qif-synaptic-plasticity skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply Mean-Field QIF Networks with Short-Term Synaptic Plasticity to my analysis.

**Agent:** I'll help you apply mf-qif-synaptic-plasticity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for mf-qif-synaptic-plasticity?

**Agent:** Let me search for the latest research and best practices...
