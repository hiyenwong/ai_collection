---
name: stochastic-synaptic-plasticity
description: 神经突触可塑性随机模型框架。基于STDP规则的突触权重演化数学模型，引入塑性核概念表示不同STDP规则，使用随机过程分析神经元-突触系统动力学。适用于计算神经科学、突触可塑性建模、STDP学习规则。触发词：突触可塑性、STDP、塑性核、突触权重、随机模型、synaptic plasticity、STDP、plasticity kernel、Hebbian learning。
user-invocable: true
---

# 神经突触可塑性随机模型

**来源论文：** arXiv:2010.08195 - Stochastic Models of Neural Synaptic Plasticity

## 核心方法论

### 1. STDP (Spike-Timing Dependent Plasticity)

突触权重变化依赖于前后脉冲时序：
- 前脉冲先于后脉冲 → 长时程增强 (LTP)
- 后脉冲先于前脉冲 → 长时程抑制 (LTD)

### 2. 塑性核 (Plasticity Kernel)

**定义：** 描述突触权重演化作为脉冲历史泛函的核函数

\[
\frac{dw}{dt} = K(t; \text{spike history})
\]

**特性：**
- 概括多种 STDP 规则
- 时间不对称性
- 脉冲对依赖性

### 3. 马尔可夫公式化

将突触系统建模为马尔可夫过程：
- 状态：膜电位 + 化学成分浓度 + 突触权重
- 转移：由脉冲事件驱动
- 稳态分析

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from collections import defaultdict
import matplotlib.pyplot as plt


@dataclass
class STDPConfig:
    """STDP 配置"""
    # 时间常数
    tau_plus: float = 20.0      # LTP 时间常数 (ms)
    tau_minus: float = 20.0     # LTD 时间常数 (ms)
    
    # 幅度
    A_plus: float = 0.01        # LTP 幅度
    A_minus: float = 0.012      # LTD 幅度
    
    # 权重限制
    w_min: float = 0.0
    w_max: float = 1.0
    
    # 塑性核类型
    kernel_type: str = "pair-based"  # pair-based, triplet, or custom


@dataclass
class NeuronState:
    """神经元状态"""
    V: float = -70.0           # 膜电位 (mV)
    x: float = 0.0             # 前脉冲迹
    y: float = 0.0             # 后脉冲迹


class PlasticityKernel:
    """塑性核基类"""
    
    def __init__(self, config: STDPConfig):
        self.config = config
        
    def compute_weight_change(self, 
                               pre_spike_time: float,
                               post_spike_time: float,
                               current_time: float) -> float:
        """计算权重变化
        
        Args:
            pre_spike_time: 前神经元脉冲时间
            post_spike_time: 后神经元脉冲时间
            current_time: 当前时间
            
        Returns:
            dw: 权重变化
        """
        raise NotImplementedError


class PairBasedKernel(PlasticityKernel):
    """基于脉冲对的塑性核"""
    
    def compute_weight_change(self,
                               pre_spike_time: float,
                               post_spike_time: float,
                               current_time: float) -> float:
        """计算权重变化
        
        标准 STDP 规则：
        Δt = t_post - t_pre
        Δw = A+ * exp(-|Δt|/τ+)  if Δt > 0 (LTP)
        Δw = -A- * exp(-|Δt|/τ-) if Δt < 0 (LTD)
        """
        config = self.config
        
        # 时间差
        delta_t = post_spike_time - pre_spike_time
        
        if delta_t > 0:  # 前脉冲先 → LTP
            dw = config.A_plus * np.exp(-delta_t / config.tau_plus)
        else:  # 后脉冲先 → LTD
            dw = -config.A_minus * np.exp(delta_t / config.tau_minus)
            
        return dw


class TripletKernel(PlasticityKernel):
    """三脉冲塑性核"""
    
    def __init__(self, config: STDPConfig):
        super().__init__(config)
        # 额外的三脉冲参数
        self.tau_x = 101.0        # 前脉冲迹时间常数
        self.tau_y = 125.0        # 后脉冲迹时间常数
        self.A2_plus = 0.006      # 二脉冲 LTP
        self.A3_plus = 0.0007     # 三脉冲 LTP
        self.A2_minus = 0.0045    # 二脉冲 LTD
        self.A3_minus = 0.00045   # 三脉冲 LTD
        
    def compute_weight_change(self,
                               pre_spike_time: float,
                               post_spike_time: float,
                               current_time: float) -> float:
        """三脉冲 STDP
        
        Δw+ = exp(-Δt/τ+) * (A2+ + A3+ * y1)
        Δw- = -exp(Δt/τ-) * (A2- + A3- * x1)
        
        其中 x1, y1 是前/后脉冲迹
        """
        delta_t = post_spike_time - pre_spike_time
        
        if delta_t > 0:
            # LTP：依赖后神经元的历史
            dw = np.exp(-delta_t / self.config.tau_plus) * (
                self.A2_plus + self.A3_plus * 0.5  # 简化：假设 y1 = 0.5
            )
        else:
            # LTD：依赖前神经元的历史
            dw = -np.exp(delta_t / self.config.tau_minus) * (
                self.A2_minus + self.A3_minus * 0.5  # 简化：假设 x1 = 0.5
            )
            
        return dw


class StochasticSynapticPlasticity:
    """随机突触可塑性模型"""
    
    def __init__(self, 
                 kernel: PlasticityKernel,
                 config: STDPConfig):
        """
        Args:
            kernel: 塑性核
            config: STDP 配置
        """
        self.kernel = kernel
        self.config = config
        
        # 突触权重
        self.w = 0.5  # 初始权重
        
        # 神经元状态
        self.pre_state = NeuronState()
        self.post_state = NeuronState()
        
        # 脉冲历史
        self.pre_spikes: List[float] = []
        self.post_spikes: List[float] = []
        
    def update_traces(self, dt: float):
        """更新脉冲迹
        
        dx/dt = -x/τ
        dy/dt = -y/τ
        """
        config = self.config
        
        # 衰减
        self.pre_state.x *= np.exp(-dt / config.tau_plus)
        self.post_state.y *= np.exp(-dt / config.tau_minus)
        
    def on_pre_spike(self, t: float):
        """前神经元脉冲"""
        self.pre_spikes.append(t)
        self.pre_state.x += 1.0
        
        # 检查最近的后脉冲
        if self.post_spikes:
            last_post = self.post_spikes[-1]
            if t - last_post < 100:  # 100ms 窗口内
                dw = self.kernel.compute_weight_change(t, last_post, t)
                self.w = np.clip(self.w + dw, 
                                self.config.w_min, 
                                self.config.w_max)
                
    def on_post_spike(self, t: float):
        """后神经元脉冲"""
        self.post_spikes.append(t)
        self.post_state.y += 1.0
        
        # 检查最近的前脉冲
        if self.pre_spikes:
            last_pre = self.pre_spikes[-1]
            if t - last_pre < 100:
                dw = self.kernel.compute_weight_change(last_pre, t, t)
                self.w = np.clip(self.w + dw,
                                self.config.w_min,
                                self.config.w_max)
                
    def simulate(self, 
                 duration: float,
                 pre_rate: float = 10.0,
                 post_rate: float = 10.0,
                 dt: float = 1.0) -> Dict:
        """模拟突触可塑性
        
        Args:
            duration: 模拟时长 (ms)
            pre_rate: 前神经元发放率 (Hz)
            post_rate: 后神经元发放率 (Hz)
            dt: 时间步长 (ms)
            
        Returns:
            results: 模拟结果
        """
        n_steps = int(duration / dt)
        time = np.arange(n_steps) * dt
        
        # 记录
        weight_history = np.zeros(n_steps)
        pre_spike_times = []
        post_spike_times = []
        
        for i, t in enumerate(time):
            # 更新迹
            self.update_traces(dt)
            
            # 泊松脉冲生成
            if np.random.random() < pre_rate * dt / 1000:
                self.on_pre_spike(t)
                pre_spike_times.append(t)
                
            if np.random.random() < post_rate * dt / 1000:
                self.on_post_spike(t)
                post_spike_times.append(t)
                
            # 记录权重
            weight_history[i] = self.w
            
        return {
            'time': time,
            'weight': weight_history,
            'pre_spikes': np.array(pre_spike_times),
            'post_spikes': np.array(post_spike_times)
        }
    
    def simulate_correlated(self,
                            duration: float,
                            correlation: float = 0.5,
                            rate: float = 10.0,
                            dt: float = 1.0) -> Dict:
        """模拟相关脉冲输入
        
        Args:
            duration: 模拟时长
            correlation: 前后脉冲相关性 (0-1)
            rate: 基础发放率
            dt: 时间步长
            
        Returns:
            results: 模拟结果
        """
        n_steps = int(duration / dt)
        time = np.arange(n_steps) * dt
        
        weight_history = np.zeros(n_steps)
        
        for i, t in enumerate(time):
            self.update_traces(dt)
            
            # 生成独立脉冲
            pre_spike = np.random.random() < rate * dt / 1000
            post_spike = np.random.random() < rate * dt / 1000
            
            # 添加相关性（共同脉冲）
            if np.random.random() < correlation * rate * dt / 1000:
                pre_spike = True
                post_spike = True
                
            if pre_spike:
                self.on_pre_spike(t)
            if post_spike:
                self.on_post_spike(t)
                
            weight_history[i] = self.w
            
        return {
            'time': time,
            'weight': weight_history
        }


def analyze_steady_state_weight(config: STDPConfig,
                                 pre_rates: np.ndarray,
                                 post_rates: np.ndarray) -> np.ndarray:
    """分析稳态权重
    
    Args:
        config: STDP 配置
        pre_rates: 前神经元发放率数组
        post_rates: 后神经元发放率数组
        
    Returns:
        steady_weights: 稳态权重矩阵
    """
    kernel = PairBasedKernel(config)
    
    steady_weights = np.zeros((len(pre_rates), len(post_rates)))
    
    for i, pre_rate in enumerate(pre_rates):
        for j, post_rate in enumerate(post_rates):
            model = StochasticSynapticPlasticity(kernel, config)
            
            # 模拟足够长时间达到稳态
            results = model.simulate(50000, pre_rate, post_rate)
            
            # 取最后 10% 的平均作为稳态
            steady_weights[i, j] = results['weight'][-int(len(results['weight']) * 0.1):].mean()
            
    return steady_weights


def compare_stdp_rules(duration: float = 10000.0) -> Dict:
    """比较不同 STDP 规则
    
    Args:
        duration: 模拟时长
        
    Returns:
        comparison: 比较结果
    """
    config = STDPConfig()
    
    results = {}
    
    # 1. 基于脉冲对的 STDP
    kernel_pair = PairBasedKernel(config)
    model_pair = StochasticSynapticPlasticity(kernel_pair, config)
    results['pair-based'] = model_pair.simulate(duration, pre_rate=15, post_rate=20)
    
    # 2. 三脉冲 STDP
    kernel_triplet = TripletKernel(config)
    model_triplet = StochasticSynapticPlasticity(kernel_triplet, config)
    results['triplet'] = model_triplet.simulate(duration, pre_rate=15, post_rate=20)
    
    # 3. 相关性分析
    correlations = [0.0, 0.3, 0.6, 0.9]
    results['correlation'] = {}
    
    for corr in correlations:
        model = StochasticSynapticPlasticity(kernel_pair, config)
        results['correlation'][corr] = model.simulate_correlated(duration, corr)
        
    return results


def visualize_stdp_results(results: Dict):
    """可视化 STDP 结果"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 权重演化
    ax = axes[0, 0]
    if 'pair-based' in results:
        ax.plot(results['pair-based']['time'], 
                results['pair-based']['weight'],
                label='Pair-based STDP', alpha=0.8)
    if 'triplet' in results:
        ax.plot(results['triplet']['time'],
                results['triplet']['weight'],
                label='Triplet STDP', alpha=0.8)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Synaptic Weight')
    ax.set_title('Weight Evolution')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 2. 相关性影响
    ax = axes[0, 1]
    if 'correlation' in results:
        for corr, data in results['correlation'].items():
            ax.plot(data['time'], data['weight'],
                   label=f'Corr = {corr}', alpha=0.8)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Synaptic Weight')
    ax.set_title('Effect of Spike Correlation')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 3. STDP 曲线
    ax = axes[1, 0]
    config = STDPConfig()
    delta_t = np.linspace(-100, 100, 200)
    
    # Pair-based
    kernel_pair = PairBasedKernel(config)
    dw_pair = [kernel_pair.compute_weight_change(
        0, dt, 0
    ) for dt in delta_t]
    ax.plot(delta_t, dw_pair, label='Pair-based', linewidth=2)
    
    # Triplet
    kernel_triplet = TripletKernel(config)
    dw_triplet = [kernel_triplet.compute_weight_change(
        0, dt, 0
    ) for dt in delta_t]
    ax.plot(delta_t, dw_triplet, label='Triplet', linewidth=2)
    
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Δt = t_post - t_pre (ms)')
    ax.set_ylabel('Δw')
    ax.set_title('STDP Learning Window')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 4. 权重分布
    ax = axes[1, 1]
    if 'pair-based' in results:
        ax.hist(results['pair-based']['weight'], bins=50, 
               alpha=0.7, label='Pair-based', density=True)
    if 'triplet' in results:
        ax.hist(results['triplet']['weight'], bins=50,
               alpha=0.7, label='Triplet', density=True)
    ax.set_xlabel('Synaptic Weight')
    ax.set_ylabel('Density')
    ax.set_title('Weight Distribution')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('stochastic_synaptic_plasticity.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'stochastic_synaptic_plasticity.png'


# 使用示例
def example_stdp_simulation():
    """示例：STDP 模拟"""
    print("="*60)
    print("神经突触可塑性随机模型")
    print("="*60)
    
    config = STDPConfig()
    
    # 创建模型
    kernel = PairBasedKernel(config)
    model = StochasticSynapticPlasticity(kernel, config)
    
    # 模拟
    print("\n1. 基本模拟 (pre_rate=15Hz, post_rate=20Hz)")
    results = model.simulate(20000, pre_rate=15, post_rate=20)
    
    print(f"   初始权重: {results['weight'][0]:.4f}")
    print(f"   最终权重: {results['weight'][-1]:.4f}")
    print(f"   前脉冲数: {len(results['pre_spikes'])}")
    print(f"   后脉冲数: {len(results['post_spikes'])}")
    
    # 比较 STDP 规则
    print("\n2. 比较 STDP 规则")
    comparison = compare_stdp_rules(duration=10000)
    
    print("\n3. 生成可视化")
    img_path = visualize_stdp_results(comparison)
    print(f"   图表已保存: {img_path}")
    
    return comparison


## Activation Keywords
- 突触可塑性
- STDP
- 塑性核
- 突触权重
- 随机模型
- synaptic plasticity
- STDP
- plasticity kernel
- Hebbian learning
- spike-timing dependent plasticity

## Tools Used
- numpy
- matplotlib

## Instructions for Agents
1. 理解 STDP 学习规则：Δt > 0 → LTP，Δt < 0 → LTD
2. 使用塑性核表示不同 STDP 规则（pair-based, triplet）
3. 模拟突触权重演化过程
4. 分析稳态权重与发放率关系
5. 比较不同 STDP 规则的行为差异

## Examples
```python
# STDP 模拟示例
from stochastic_synaptic_plasticity import (
    StochasticSynapticPlasticity, 
    PairBasedKernel, 
    STDPConfig
)

# 1. 配置
config = STDPConfig(
    tau_plus=20.0,
    tau_minus=20.0,
    A_plus=0.01,
    A_minus=0.012
)

# 2. 创建塑性核
kernel = PairBasedKernel(config)

# 3. 创建模型
model = StochasticSynapticPlasticity(kernel, config)

# 4. 模拟
results = model.simulate(
    duration=10000,    # 10秒
    pre_rate=15.0,     # 前神经元 15Hz
    post_rate=20.0     # 后神经元 20Hz
)

# 5. 查看权重演化
print(f"初始权重: {results['weight'][0]:.3f}")
print(f"最终权重: {results['weight'][-1]:.3f}")
```

if __name__ == "__main__":
    example_stdp_simulation()
```

## Related Skills

- `neuromodulated-synaptic-plasticity` - 神经调制突触可塑性
- `heterogeneous-synaptic-dynamics` - 异质性突触动力学
- `multi-plasticity-snn-training` - 多重可塑性SNN训练

## References

- arXiv:2010.08195 - Stochastic Models of Neural Synaptic Plasticity
- Topics: Probability (math.PR), Neurons and Cognition (q-bio.NC)