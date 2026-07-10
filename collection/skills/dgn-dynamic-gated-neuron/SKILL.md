---
name: dgn-dynamic-gated-neuron
description: Dynamic Gated Neuron (DGN) — brain-inspired gating mechanism for robust spiking neural networks. Dynamic conductance acts as biologically plausible gating for selective input filtering and adaptive noise suppression. Use when designing robust SNNs, implementing noise-resilient spike-based computation, or building biologically realistic neuron models with enhanced stochastic stability.
user-invocable: true
---

# Dynamic Gated Neuron (DGN)

**来源论文：** arXiv:2509.03281 (2025-09-03) - "A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks"
**作者:** Qianyi Bai, Haiteng Wang, Qiang Yu

## 核心方法论

### 1. 核心洞察

传统 LIF 神经元省略了生物神经元固有的动态电导机制，限制了应对噪声和时间变异性的能力。**动态电导本质上是生物学合理的门控机制**，可以调节信息流、选择性过滤输入和自适应抑制噪声。

### 2. DGN 神经元模型

#### 传统 LIF (基准)
```
τ_m dV/dt = -V + R * I_syn

当 V ≥ V_th: 发放脉冲, V → V_reset
```

#### DGN (改进)
```
τ_m dV/dt = -(V - V_rest) - g(t) * (V - E_syn) + R * I_syn(t)

dg/dt = (-g + g_0)/τ_g + β * spike_activity

其中:
- g(t): 动态膜电导，随神经活动演化
- g_0: 基线电导
- τ_g: 电导时间常数
- β: 活动-电导耦合系数
- E_syn: 突触反转电位
```

#### 门控机制解释
- **高 g(t)** → 强"门控" → 输入被抑制 → 噪声过滤
- **低 g(t)** → 弱"门控" → 输入被传递 → 信号通过
- 电导自动响应神经活动，实现自适应门控

### 3. 理论保证

#### 随机稳定性
DGN 相比标准 LIF 具有增强的随机稳定性：
```
定理: 在加性噪声 ξ(t) 下，
DGN 的方差 Var[V_DGN] < Var[V_LIF]

证明思路: 动态电导作为扰动抑制机制
dg/dt 项引入了负反馈，稳定膜电位波动
```

#### 噪声抑制
```
信噪比增益:
SNR_DGN / SNR_LIF ≈ 1 + (g_dynamic / g_leak)

动态电导越大，噪声抑制效果越强
```

### 4. Python 实现

```python
import numpy as np

class DynamicGatedNeuron:
    """
    Dynamic Gated Neuron (DGN) 实现
    
    动态电导作为门控机制，实现自适应噪声抑制
    """
    
    def __init__(self, tau_m=20.0, tau_g=50.0, v_th=1.0, v_reset=0.0,
                 g_baseline=0.1, beta=0.05, e_syn=0.0, v_rest=0.0,
                 r_input=1.0, dt=1.0):
        self.tau_m = tau_m      # 膜时间常数
        self.tau_g = tau_g      # 电导时间常数
        self.v_th = v_th        # 阈值
        self.v_reset = v_reset  # 复位电位
        self.g_baseline = g_baseline  # 基线电导
        self.beta = beta        # 活动-电导耦合系数
        self.e_syn = e_syn      # 突触反转电位
        self.v_rest = v_rest    # 静息电位
        self.r_input = r_input  # 输入电阻
        self.dt = dt            # 时间步长
        
        # 状态变量
        self.v = v_rest
        self.g = g_baseline
        
    def step(self, i_syn):
        """
        模拟一个时间步
        
        Args:
            i_syn: 突触输入电流
        Returns:
            spike: 是否发放脉冲
        """
        # 更新动态电导
        # 简化：如果发放了脉冲则增加电导
        dg = (-self.g + self.g_baseline) / self.tau_g * self.dt
        
        # 更新膜电位
        dv = (-(self.v - self.v_rest) 
              - self.g * (self.v - self.e_syn) 
              + self.r_input * i_syn) / self.tau_m * self.dt
        
        self.v += dv
        self.g += dg
        
        # 检查阈值
        spike = False
        if self.v >= self.v_th:
            spike = True
            self.v = self.v_reset
            # 发放后增加电导（活动-电导耦合）
            self.g += self.beta
        
        return spike
    
    def run(self, input_current, noise_level=0.0):
        """
        运行完整模拟
        
        Args:
            input_current: 输入电流数组 (T,)
            noise_level: 噪声标准差
        Returns:
            spike_train: 脉冲序列 (T,) 二进制
            v_trace: 膜电位轨迹 (T,)
            g_trace: 电导轨迹 (T,)
        """
        T = len(input_current)
        spike_train = np.zeros(T)
        v_trace = np.zeros(T)
        g_trace = np.zeros(T)
        
        for t in range(T):
            # 添加噪声
            i_with_noise = input_current[t] + noise_level * np.random.randn()
            
            spike_train[t] = self.step(i_with_noise)
            v_trace[t] = self.v
            g_trace[t] = self.g
        
        return spike_train, v_trace, g_trace


class LeakyIntegrateFire:
    """标准 LIF 神经元用于对比"""
    
    def __init__(self, tau_m=20.0, v_th=1.0, v_reset=0.0, 
                 v_rest=0.0, r_input=1.0, dt=1.0):
        self.tau_m = tau_m
        self.v_th = v_th
        self.v_reset = v_reset
        self.v_rest = v_rest
        self.r_input = r_input
        self.dt = dt
        self.v = v_rest
    
    def step(self, i_syn):
        dv = (-(self.v - self.v_rest) + self.r_input * i_syn) / self.tau_m * self.dt
        self.v += dv
        
        spike = False
        if self.v >= self.v_th:
            spike = True
            self.v = self.v_reset
        return spike
    
    def run(self, input_current, noise_level=0.0):
        T = len(input_current)
        spike_train = np.zeros(T)
        v_trace = np.zeros(T)
        
        for t in range(T):
            i_with_noise = input_current[t] + noise_level * np.random.randn()
            spike_train[t] = self.step(i_with_noise)
            v_trace[t] = self.v
        
        return spike_train, v_trace


# 对比实验
def compare_robustness():
    """对比 DGN 和 LIF 的噪声鲁棒性"""
    T = 1000
    t = np.arange(T)
    
    # 信号: 周期性输入
    signal = 0.5 + 0.3 * np.sin(2 * np.pi * t / 200)
    
    # 不同噪声水平
    noise_levels = [0.0, 0.1, 0.2, 0.3, 0.5, 0.8]
    
    results = {'dgn': [], 'lif': []}
    
    for noise in noise_levels:
        # DGN
        dgn = DynamicGatedNeuron()
        spikes_dgn, _, _ = dgn.run(signal, noise)
        
        # LIF
        lif = LeakyIntegrateFire()
        spikes_lif, _ = lif.run(signal, noise)
        
        # 计算信噪比 (基于发放率)
        rate_dgn = np.mean(spikes_dgn)
        rate_lif = np.mean(spikes_lif)
        
        # 理想发放率（无噪声）
        if noise == 0.0:
            ideal_rate_dgn = rate_dgn
            ideal_rate_lif = rate_lif
        else:
            snr_dgn = ideal_rate_dgn / (ideal_rate_dgn + abs(rate_dgn - ideal_rate_dgn) + 1e-10)
            snr_lif = ideal_rate_lif / (ideal_rate_lif + abs(rate_lif - ideal_rate_lif) + 1e-10)
            results['dgn'].append(snr_dgn)
            results['lif'].append(snr_lif)
    
    return results
```

### 5. 在 SNN 网络中的应用

```python
import torch
import torch.nn as nn

class DGNSNNLayer(nn.Module):
    """使用 DGN 神经元的 SNN 层"""
    
    def __init__(self, n_in, n_out, tau_m=20.0, tau_g=50.0, 
                 v_th=1.0, dt=1.0, n_steps=100):
        super().__init__()
        self.n_in = n_in
        self.n_out = n_out
        self.n_steps = n_steps
        self.dt = dt
        
        # 可学习权重
        self.weight = nn.Parameter(torch.randn(n_out, n_in) * 0.1)
        
        # 神经元参数
        self.tau_m = tau_m
        self.tau_g = tau_g
        self.v_th = v_th
        self.beta = nn.Parameter(torch.tensor(0.05))
        self.g_baseline = nn.Parameter(torch.tensor(0.1))
        
    def forward(self, x):
        """
        Args:
            x: 输入 [batch, n_steps, n_in] (脉冲序列)
        Returns:
            output: 输出 [batch, n_out] (累积脉冲计数)
        """
        batch = x.size(0)
        v = torch.zeros(batch, self.n_out)
        g = self.g_baseline * torch.ones(batch, self.n_out)
        output_spikes = torch.zeros(batch, self.n_steps, self.n_out)
        
        for t in range(self.n_steps):
            # 突触输入
            i_syn = F.linear(x[:, t, :], self.weight)
            
            # 动态电导更新
            g = g + (-g + self.g_baseline) / self.tau_g * self.dt
            
            # 膜电位更新
            dv = (-(v) - g * v + i_syn) / self.tau_m * self.dt
            v = v + dv
            
            # 发放检测
            spikes = (v >= self.v_th).float()
            v = v * (1 - spikes)  # 复位
            
            # 发放后增加电导
            g = g + self.beta * spikes
            
            output_spikes[:, t, :] = spikes
        
        return output_spikes.sum(dim=1)  # 累积脉冲计数
```

### 6. 实验验证

论文在以下基准上验证了 DGN 的优越性：
- **TIDIGITS**: 语音识别任务，DGN 在高噪声下显著优于 LIF
- **SHD (Spiking Heidelberg Digits)**: 听觉时序分类
- 抗噪声任务：在加性噪声下展示增强的鲁棒性

## 激活关键词
- DGN
- dynamic gated neuron
- brain-inspired gating SNN
- robust spiking neural network
- dynamic conductance neuron
- noise resilient SNN
- 动态门控神经元
- 鲁棒脉冲神经网络
- 动态电导机制

## Related Skills
- `snn-universal-approximation` - SNN 万能逼近定理
- `snn-learning-survey` - SNN 学习规则综合
- `spiking-neural-network-analysis` - SNN 论文分析