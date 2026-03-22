---
name: associative-presynaptic-plasticity
description: 联合突触前短时程可塑性方法论。扩展Fisher信息学习规则到Tsodyks-Markram突触，推导基线权重和释放概率的学习规则。触发词：突触可塑性、短时程可塑性、突触前、信息论、Tsodyks-Markram、学习规则、temporal coding、STP、synaptic plasticity、presynaptic。
user-invocable: true
---

# Associative Presynaptic Short-Term Plasticity

基于信息论的联合突触前短时程可塑性（STP）学习规则，用于快速重构时序编码。

## 核心方法论

### 1. Tsodyks-Markram 突触模型

```python
import numpy as np
from dataclasses import dataclass

@dataclass
class TMParameters:
    """Tsodyks-Markram 突触参数"""
    U: float = 0.5      # 利用参数（释放概率）
    D: float = 0.2      # 抑郁恢复时间常数 (s)
    F: float = 0.01     # 促进恢复时间常数 (s)
    A: float = 1.0      # 突触强度

class TsodyksMarkramSynapse:
    """Tsodyks-Markram 短时程可塑性突触模型"""
    
    def __init__(self, params: TMParameters = None):
        self.params = params or TMParameters()
        self.reset()
        
    def reset(self):
        """重置突触状态"""
        self.x = 1.0  # 可用资源
        self.u = self.params.U  # 利用变量
        
    def process_spike(self, t_spike: float):
        """处理单个突触前脉冲
        
        Args:
            t_spike: 自上次脉冲以来的时间间隔
            
        Returns:
            突触后电流幅度
        """
        # 状态更新（时间演化）
        self.x = 1 + (self.x - 1) * np.exp(-t_spike / self.params.D)
        self.u = self.params.U + (self.u - self.params.U) * np.exp(-t_spike / self.params.F)
        
        # 脉冲响应
        response = self.params.A * self.u * self.x
        
        # 状态更新（脉冲后）
        self.x = self.x * (1 - self.u)
        self.u = self.u + self.params.U * (1 - self.u)
        
        return response
    
    def get_fisher_information(self, input_rate: float):
        """计算给定输入速率下的Fisher信息
        
        Fisher信息衡量突触对刺激的敏感性
        """
        # 稳态分析
        r = input_rate
        U = self.params.U
        D = self.params.D
        F = self.params.F
        
        # 稳态资源
        x_ss = 1 / (1 + U * r * D / (1 + r * F))
        
        # Fisher信息（近似）
        # 衡量突触响应随输入变化的敏感度
        dxdU = -r * D * x_ss**2 / (1 + r * F)
        fisher = dxdU**2 / (self.params.A * x_ss)
        
        return fisher
```

### 2. 信息论学习规则

```python
class AssociativeSTPLearner:
    """联合STP学习规则
    
    基于Fisher信息最大化推导的学习规则
    """
    
    def __init__(self, n_synapses: int = 100):
        self.n_synapses = n_synapses
        self.synapses = [TsodyksMarkramSynapse() for _ in range(n_synapses)]
        self.weights = np.ones(n_synapses)  # 基线权重
        
        # 学习率
        self.eta_w = 0.01   # 权重学习率
        self.eta_U = 0.001  # 释放概率学习率
        
    def compute_postsynaptic_response(self, spike_times: list, weights: np.ndarray = None):
        """计算突触后响应"""
        if weights is None:
            weights = self.weights
            
        response = np.zeros(len(spike_times))
        for i, syn in enumerate(self.synapses):
            syn.reset()
            prev_t = 0
            for j, t in enumerate(spike_times):
                dt = t - prev_t if j > 0 else 0.1
                r = syn.process_spike(dt)
                response[j] += weights[i] * r
                prev_t = t
        
        return response
    
    def fisher_learning_rule(self, pre_activity: np.ndarray, post_activity: float):
        """Fisher信息学习规则
        
        最大化刺激信息的Fisher信息
        
        Args:
            pre_activity: 突触前活动向量
            post_activity: 突触后活动（标量）
        """
        # 突触后项：追踪局部发放率
        post_term = post_activity
        
        # 突触前项：相位超前，检测刺激起始
        pre_term = np.gradient(pre_activity)  # 检测变化率
        
        # 联合学习规则
        dW = self.eta_w * post_term * pre_term
        
        # 资源约束下的释放概率学习
        for i, syn in enumerate(self.synapses):
            dU = self.eta_U * pre_activity[i] * post_activity
            syn.params.U = np.clip(syn.params.U + dU, 0.01, 0.99)
        
        self.weights += dW
        self.weights = np.clip(self.weights, 0.01, 10.0)
        
    def optimize_release_probability(self, input_rates: np.ndarray):
        """优化释放概率
        
        根据输入统计特性调整释放概率
        """
        for i, (syn, rate) in enumerate(zip(self.synapses, input_rates)):
            # 目标：平衡促进和抑郁
            optimal_U = 1.0 / (1.0 + rate * syn.params.D)
            syn.params.U = 0.9 * syn.params.U + 0.1 * optimal_U
```

### 3. 频率依赖相位选择性

```python
class FrequencyPhaseSelector:
    """频率依赖相位选择性
    
    STP产生对不同频率的相位选择性
    """
    
    def __init__(self, synapse: TsodyksMarkramSynapse = None):
        self.synapse = synapse or TsodyksMarkramSynapse()
        
    def frequency_response(self, frequencies: np.ndarray):
        """计算不同频率下的响应特性"""
        responses = []
        phases = []
        
        for freq in frequencies:
            # 模拟周期性输入
            T = 1.0 / freq
            n_cycles = 10
            total_time = n_cycles * T
            dt = T / 100
            
            times = np.arange(0, total_time, dt)
            spike_times = np.arange(0, total_time, T)
            
            # 计算稳态响应
            self.synapse.reset()
            responses_list = []
            prev_t = 0
            
            for t in spike_times:
                dt_spike = t - prev_t
                r = self.synapse.process_spike(dt_spike)
                responses_list.append(r)
                prev_t = t
            
            # 稳态响应（最后几个周期）
            steady_state = np.mean(responses_list[-5:])
            responses.append(steady_state)
            
            # 相位延迟
            phase = np.angle(np.fft.fft(responses_list)[-1])
            phases.append(phase)
        
        return np.array(responses), np.array(phases)
    
    def compute_temporal_asymmetry(self, freq: float):
        """计算时序不对称性
        
        STP在不同频率下产生不同的时序偏好
        """
        # 正向输入
        T = 1.0 / freq
        forward_response = self._compute_ordered_response([T] * 10)
        
        # 反向输入（逆序）
        backward_response = self._compute_ordered_response([T] * 10, reverse=True)
        
        asymmetry = (forward_response - backward_response) / (forward_response + backward_response + 1e-10)
        return asymmetry
    
    def _compute_ordered_response(self, intervals: list, reverse: bool = False):
        """计算有序间隔下的响应"""
        if reverse:
            intervals = intervals[::-1]
            
        self.synapse.reset()
        responses = []
        for dt in intervals:
            r = self.synapse.process_spike(dt)
            responses.append(r)
        
        return np.mean(responses[-5:])
```

### 4. 环路动态模拟

```python
class RecurrentCircuit:
    """递归环路模拟
    
    展示STP如何产生反向回放和驱动响应偏移
    """
    
    def __init__(self, n_neurons: int = 10):
        self.n_neurons = n_neurons
        self.synapses = [[TsodyksMarkramSynapse() 
                          for _ in range(n_neurons)] 
                         for _ in range(n_neurons)]
        self.weights = np.random.rand(n_neurons, n_neurons) * 0.5
        np.fill_diagonal(self.weights, 0)  # 无自连接
        
    def simulate(self, initial_pattern: np.ndarray, duration: float, dt: float = 0.001):
        """模拟网络动态
        
        Args:
            initial_pattern: 初始活动模式
            duration: 模拟时长 (s)
            dt: 时间步长 (s)
            
        Returns:
            活动轨迹
        """
        n_steps = int(duration / dt)
        trajectory = np.zeros((n_steps, self.n_neurons))
        trajectory[0] = initial_pattern
        
        # 外部驱动时间
        drive_duration = duration / 3
        
        for t in range(1, n_steps):
            current_time = t * dt
            
            # 外部驱动（前1/3时间）
            external_drive = np.zeros(self.n_neurons)
            if current_time < drive_duration:
                external_drive = 0.5 * np.exp(-current_time / 0.1)
            
            # 突触输入
            synaptic_input = np.zeros(self.n_neurons)
            for i in range(self.n_neurons):
                for j in range(self.n_neurons):
                    if self.weights[i, j] > 0:
                        # STP调制
                        stp_gain = self.synapses[i][j].params.U * self.synapses[i][j].x
                        synaptic_input[i] += self.weights[i, j] * trajectory[t-1, j] * stp_gain
            
            # 更新活动（简化的激活函数）
            total_input = external_drive + synaptic_input
            trajectory[t] = np.tanh(total_input)
        
        return trajectory
    
    def demonstrate_reverse_replay(self):
        """演示驱动移除后的反向回放"""
        # 初始化模式（神经元序列激活）
        initial = np.zeros(self.n_neurons)
        initial[0] = 1.0
        
        # 模拟
        trajectory = self.simulate(initial, duration=0.5)
        
        # 分析
        return {
            'trajectory': trajectory,
            'peak_times': np.argmax(trajectory, axis=0)
        }
```

## 应用场景

### 1. 时序编码学习
- 学习刺激的时序结构
- 时序记忆的形成
- 序列预测和生成

### 2. 神经形态计算
- 脉冲神经网络的可塑性机制
- 在线学习算法
- 低功耗神经计算

### 3. 认知神经科学建模
- 工作记忆机制
- 时序信息处理
- 感觉适应和学习

## 使用示例

```python
# 创建STP学习器
learner = AssociativeSTPLearner(n_synapses=100)

# 模拟学习过程
n_steps = 1000
for t in range(n_steps):
    # 模拟突触前活动（带有时序结构）
    pre_activity = np.random.poisson(5, 100) * (1 + 0.5 * np.sin(2 * np.pi * t / 100))
    
    # 计算突触后响应
    post_activity = np.dot(learner.weights, pre_activity) / 100
    
    # 应用学习规则
    learner.fisher_learning_rule(pre_activity, post_activity)

# 分析结果
print(f"权重分布: 均值={learner.weights.mean():.3f}, 标准差={learner.weights.std():.3f}")
print(f"释放概率范围: [{min(s.params.U for s in learner.synapses):.3f}, "
      f"{max(s.params.U for s in learner.synapses):.3f}]")

# 频率选择性分析
selector = FrequencyPhaseSelector()
freqs = np.logspace(-1, 2, 20)  # 0.1-100 Hz
responses, phases = selector.frequency_response(freqs)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.semilogx(freqs, responses)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Steady-state response')
plt.subplot(122)
plt.plot(freqs, phases)
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase shift (rad)')
plt.tight_layout()
plt.savefig('frequency_selectivity.png')
```

## 参考文献

- arXiv:2601.10397 - Reshaping Neural Representation via Associative, Presynaptic Short-Term Plasticity