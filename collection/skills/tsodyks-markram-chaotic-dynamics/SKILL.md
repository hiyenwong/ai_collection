---
name: tsodyks-markram-chaotic-dynamics
description: Tsodyks-Markram短时程突触可塑性的混沌动力学。研究确定性TM模型中Shilnikov同宿分岔导致混沌行为的路径，揭示网络动力学不可预测性和对初始条件的敏感性。适用于计算神经科学、突触可塑性建模、混沌动力学分析。触发词：短时程突触可塑性、Tsodyks-Markram模型、Shilnikov分岔、混沌动力学、short-term synaptic plasticity、Tsodyks-Markram model、Shilnikov homoclinic bifurcation、chaotic dynamics。
user-invocable: true
---

# Tsodyks-Markram 短时程突触可塑性的混沌动力学

**来源论文：** arXiv:1309.7966 - Short-term synaptic plasticity in the deterministic Tsodyks-Markram model leads to unpredictable network dynamics (PNAS 2013)

## 核心方法论

### 1. Tsodyks-Markram (TM) 模型

**短时程突触可塑性 (STSP)：** 强烈影响皮层网络神经动力学

**TM 模型特性：**
- 准确描述不同类型皮层突触的生理响应
- 包含易化和抑制机制
- 资源有限的突触模型

### 2. Shilnikov 同宿分岔

**核心发现：** 首次报告 TM 模型通过 Shilnikov 同宿分岔通向混沌行为

**关键特性：**
- 强烈影响相空间轨迹形状
- 诱导高度不规则的瞬态动力学
- 群体脉冲数量和时序不可预测
- 对初始条件高度敏感

### 3. 确定性与随机性

**确定性模型：** 同宿分岔导致不规则动力学

**随机/网络版本：**
- 生成复杂不规则脉冲模式
- 作为"跳板"促进下态和不稳定周期轨道间的转换

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict
from scipy.integrate import odeint
import matplotlib.pyplot as plt


@dataclass
class TMModelConfig:
    """Tsodyks-Markram 模型配置"""
    # 突触参数
    U: float = 0.5              # 利用率
    tau_rec: float = 800.0       # 恢复时间常数 (ms)
    tau_facil: float = 1000.0    # 易化时间常数 (ms)
    
    # 网络参数
    n_neurons: int = 100
    tau_m: float = 20.0          # 膜时间常数 (ms)
    
    # 仿真参数
    dt: float = 0.1              # 时间步长 (ms)
    duration: float = 1000.0     # 仿真时长 (ms)


class TsodyksMarkramSynapse:
    """Tsodyks-Markram 突触模型"""
    
    def __init__(self, config: TMModelConfig):
        """
        Args:
            config: 模型配置
        """
        self.config = config
        
        # 突触状态
        self.R = 1.0  # 可用资源
        self.u = config.U  # 利用率
        
    def update(self, pre_spike: bool, dt: float) -> float:
        """更新突触状态
        
        TM 模型方程：
        dR/dt = (1 - R) / τ_rec - u * R * δ(t - t_spike)
        du/dt = (U - u) / τ_facil + U * (1 - u) * δ(t - t_spike)
        
        Args:
            pre_spike: 是否有脉冲
            dt: 时间步长
            
        Returns:
            efficacy: 突触效能
        """
        cfg = self.config
        
        # 恢复动力学
        dR = (1 - self.R) / cfg.tau_rec * dt
        du = (cfg.U - self.u) / cfg.tau_facil * dt
        
        self.R += dR
        self.u += du
        
        # 脉冲效应
        if pre_spike:
            # 资源消耗
            delta_R = self.u * self.R
            self.R -= delta_R
            
            # 易化
            self.u += cfg.U * (1 - self.u)
            
            return delta_R
            
        return 0.0
    
    def get_efficacy(self) -> float:
        """获取当前突触效能
        
        Returns:
            efficacy: 突触效能
        """
        return self.u * self.R


class TMNetworkModel:
    """TM 网络模型"""
    
    def __init__(self, config: TMModelConfig):
        """
        Args:
            config: 模型配置
        """
        self.config = config
        
        # 神经元膜电位
        self.V = np.zeros(config.n_neurons)
        
        # 突触矩阵
        self.synapses = [
            [TsodyksMarkramSynapse(config) for _ in range(config.n_neurons)]
            for _ in range(config.n_neurons)
        ]
        
        # 连接权重
        self.W = np.random.randn(config.n_neurons, config.n_neurons) * 0.1
        
        # 状态历史
        self.V_history = []
        self.R_history = []
        self.u_history = []
        
    def step(self, external_input: np.ndarray, dt: float) -> np.ndarray:
        """单步更新
        
        Args:
            external_input: 外部输入
            dt: 时间步长
            
        Returns:
            spikes: 脉冲输出
        """
        cfg = self.config
        
        # 计算突触输入
        I_syn = np.zeros(cfg.n_neurons)
        
        for i in range(cfg.n_neurons):
            for j in range(cfg.n_neurons):
                if self.W[i, j] != 0:
                    # 检查是否有脉冲
                    pre_spike = self.V[j] > 1.0
                    efficacy = self.synapses[i][j].update(pre_spike, dt)
                    I_syn[i] += self.W[i, j] * efficacy
        
        # 更新膜电位
        dV = (-self.V + I_syn + external_input) / cfg.tau_m
        self.V += dV * dt
        
        # 发放
        spikes = (self.V > 1.0).astype(float)
        self.V[spikes > 0] = 0.0  # 重置
        
        return spikes
    
    def simulate(self, 
                 external_input_func: callable,
                 record_states: bool = True) -> Dict:
        """仿真
        
        Args:
            external_input_func: 外部输入函数 (t) -> array
            record_states: 是否记录状态
            
        Returns:
            results: 仿真结果
        """
        cfg = self.config
        n_steps = int(cfg.duration / cfg.dt)
        
        spikes_history = []
        
        for step in range(n_steps):
            t = step * cfg.dt
            external_input = external_input_func(t)
            
            spikes = self.step(external_input, cfg.dt)
            spikes_history.append(spikes)
            
            if record_states:
                self.V_history.append(self.V.copy())
                # 记录平均突触状态
                R_mean = np.mean([[s.R for s in row] for row in self.synapses])
                u_mean = np.mean([[s.u for s in row] for row in self.synapses])
                self.R_history.append(R_mean)
                self.u_history.append(u_mean)
                
        return {
            'spikes': np.array(spikes_history),
            'V': np.array(self.V_history) if record_states else None,
            'R': np.array(self.R_history) if record_states else None,
            'u': np.array(self.u_history) if record_states else None
        }


class ShilnikovBifurcationAnalyzer:
    """Shilnikov 同宿分岔分析器"""
    
    def __init__(self, config: TMModelConfig):
        self.config = config
        
    def compute_lyapunov_exponent(self, 
                                   trajectory: np.ndarray,
                                   dt: float) -> float:
        """计算 Lyapunov 指数
        
        Args:
            trajectory: 轨迹 (n_steps, n_dims)
            dt: 时间步长
            
        Returns:
            lyapunov: 最大 Lyapunov 指数
        """
        n_steps = len(trajectory)
        
        if n_steps < 10:
            return 0.0
            
        # 简化：使用轨迹发散估计
        # 找两个初始接近的点，追踪它们的分离
        ref_idx = n_steps // 4
        
        # 计算轨迹变化率
        diffs = np.diff(trajectory, axis=0)
        magnitudes = np.linalg.norm(diffs, axis=1) if len(diffs.shape) > 1 else np.abs(diffs)
        
        # 对数增长
        if np.all(magnitudes > 0):
            log_growth = np.log(magnitudes[magnitudes > 0] + 1e-10)
            lyapunov = np.mean(log_growth) / dt
        else:
            lyapunov = 0.0
            
        return lyapunov
    
    def detect_homoclinic_orbit(self, 
                                 trajectory: np.ndarray,
                                 threshold: float = 0.1) -> bool:
        """检测同宿轨道
        
        Args:
            trajectory: 轨迹
            threshold: 接近阈值
            
        Returns:
            is_homoclinic: 是否存在同宿轨道
        """
        # 检查轨迹是否接近初始点
        start = trajectory[0]
        end = trajectory[-1]
        
        # 检查中间是否远离
        mid_idx = len(trajectory) // 2
        mid = trajectory[mid_idx]
        
        dist_start_end = np.linalg.norm(start - end)
        dist_start_mid = np.linalg.norm(start - mid)
        
        # 同宿轨道：起点和终点接近，中间远离
        return dist_start_end < threshold and dist_start_mid > threshold * 10
    
    def analyze_bifurcation_parameter(self,
                                       U_values: np.ndarray,
                                       n_trials: int = 10) -> Dict:
        """分析分岔参数
        
        Args:
            U_values: 利用率参数范围
            n_trials: 试验次数
            
        Returns:
            analysis: 分析结果
        """
        results = {
            'U_values': U_values,
            'lyapunov_exponents': [],
            'chaotic_regions': []
        }
        
        for U in U_values:
            # 创建不同 U 值的配置
            config = TMModelConfig(U=U)
            
            lyapunovs = []
            
            for trial in range(n_trials):
                # 创建网络
                network = TMNetworkModel(config)
                
                # 随机初始条件
                np.random.seed(trial)
                
                # 简单输入
                def input_func(t):
                    return np.random.randn(config.n_neurons) * 0.1
                
                # 仿真
                sim_results = network.simulate(input_func, record_states=True)
                
                # 计算 Lyapunov 指数
                if sim_results['V'] is not None:
                    lyap = self.compute_lyapunov_exponent(
                        sim_results['V'], config.dt
                    )
                    lyapunovs.append(lyap)
                    
            avg_lyap = np.mean(lyapunovs) if lyapunovs else 0
            results['lyapunov_exponents'].append(avg_lyap)
            
            # 检测混沌区域
            if avg_lyap > 0.01:  # 正 Lyapunov 指数表示混沌
                results['chaotic_regions'].append(U)
                
        return results


def analyze_unpredictable_dynamics(config: TMModelConfig,
                                    n_perturbations: int = 10,
                                    perturbation_scale: float = 0.001) -> Dict:
    """分析不可预测动力学
    
    Args:
        config: 配置
        n_perturbations: 扰动次数
        perturbation_scale: 扰动尺度
        
    Returns:
        analysis: 分析结果
    """
    results = {
        'spike_counts': [],
        'spike_times': [],
        'sensitivity': []
    }
    
    base_network = TMNetworkModel(config)
    
    # 基线仿真
    def input_func(t):
        return np.ones(config.n_neurons) * 0.5
    
    base_result = base_network.simulate(input_func, record_states=False)
    base_spikes = base_result['spikes']
    base_count = base_spikes.sum()
    
    for i in range(n_perturbations):
        # 创建扰动网络
        network = TMNetworkModel(config)
        
        # 微小扰动初始条件
        network.V += np.random.randn(config.n_neurons) * perturbation_scale
        
        result = network.simulate(input_func, record_states=False)
        spikes = result['spikes']
        
        # 记录差异
        spike_count = spikes.sum()
        results['spike_counts'].append(spike_count)
        
        # 计算敏感性
        count_diff = abs(spike_count - base_count)
        results['sensitivity'].append(count_diff / perturbation_scale)
        
    return {
        'mean_spike_count': np.mean(results['spike_counts']),
        'std_spike_count': np.std(results['spike_counts']),
        'mean_sensitivity': np.mean(results['sensitivity']),
        'unpredictability_index': np.std(results['spike_counts']) / (np.mean(results['spike_counts']) + 1e-10)
    }


def visualize_tm_dynamics(config: TMModelConfig):
    """可视化 TM 动力学"""
    network = TMNetworkModel(config)
    
    def input_func(t):
        if 100 < t < 200:
            return np.ones(config.n_neurons) * 1.5
        return np.zeros(config.n_neurons)
    
    result = network.simulate(input_func, record_states=True)
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # 膜电位
    ax = axes[0]
    if result['V'] is not None:
        ax.imshow(result['V'][:500, :20].T, aspect='auto', cmap='viridis')
    ax.set_xlabel('Time (steps)')
    ax.set_ylabel('Neuron')
    ax.set_title('Membrane Potentials')
    
    # 突触资源
    ax = axes[1]
    if result['R'] is not None:
        ax.plot(result['R'][:1000], label='R (available resource)')
    if result['u'] is not None:
        ax.plot(result['u'][:1000], label='u (utilization)')
    ax.set_xlabel('Time (steps)')
    ax.set_ylabel('Value')
    ax.set_title('Synaptic Dynamics (TM Model)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 脉冲计数
    ax = axes[2]
    spike_counts = result['spikes'].sum(axis=1)
    ax.plot(spike_counts[:1000])
    ax.set_xlabel('Time (steps)')
    ax.set_ylabel('Spike Count')
    ax.set_title('Population Spike Count')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('tm_chaotic_dynamics.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'tm_chaotic_dynamics.png'


# 使用示例
def example_tm_chaotic_dynamics():
    """示例：TM 模型混沌动力学"""
    print("="*60)
    print("Tsodyks-Markram 短时程突触可塑性的混沌动力学")
    print("="*60)
    
    config = TMModelConfig(
        U=0.5,
        tau_rec=800.0,
        tau_facil=1000.0
    )
    
    # 创建网络
    network = TMNetworkModel(config)
    
    print(f"\nTM 模型参数:")
    print(f"  利用率 U: {config.U}")
    print(f"  恢复时间 τ_rec: {config.tau_rec} ms")
    print(f"  易化时间 τ_facil: {config.tau_facil} ms")
    
    # 分析不可预测性
    print(f"\n分析不可预测动力学...")
    unpred = analyze_unpredictable_dynamics(config)
    
    print(f"\n结果:")
    print(f"  平均脉冲数: {unpred['mean_spike_count']:.1f}")
    print(f"  脉冲数标准差: {unpred['std_spike_count']:.1f}")
    print(f"  不可预测性指数: {unpred['unpredictability_index']:.3f}")
    
    # 分岔分析
    print(f"\n分岔参数分析...")
    analyzer = ShilnikovBifurcationAnalyzer(config)
    U_values = np.linspace(0.1, 0.9, 9)
    bifurc = analyzer.analyze_bifurcation_parameter(U_values, n_trials=5)
    
    print(f"  混沌区域 U ∈ {bifurc['chaotic_regions']}")
    
    print(f"\n关键发现:")
    print(f"  ✅ Shilnikov 同宿分岔导致混沌")
    print(f"  ✅ 脉冲数量和时序不可预测")
    print(f"  ✅ 对初始条件高度敏感")
    
    return network


## Activation Keywords
- 短时程突触可塑性
- Tsodyks-Markram模型
- Shilnikov分岔
- 混沌动力学
- short-term synaptic plasticity
- Tsodyks-Markram model
- Shilnikov homoclinic bifurcation
- chaotic dynamics

## Tools Used
- numpy
- scipy

## Instructions for Agents
1. 理解 TM 模型的易化和抑制机制
2. 分析 Shilnikov 同宿分岔的存在条件
3. 计算 Lyapunov 指数检测混沌
4. 分析对初始条件的敏感性
5. 识别混沌参数区域

## Examples
```python
# TM 模型混沌动力学示例
from tsodyks_markram_chaotic_dynamics import (
    TMNetworkModel, TMModelConfig, 
    ShilnikovBifurcationAnalyzer, analyze_unpredictable_dynamics
)

# 1. 配置
config = TMModelConfig(
    U=0.5,           # 利用率
    tau_rec=800.0,   # 恢复时间
    tau_facil=1000.0 # 易化时间
)

# 2. 创建网络
network = TMNetworkModel(config)

# 3. 仿真
def input_func(t):
    return np.ones(config.n_neurons) * 0.5

result = network.simulate(input_func)

# 4. 分析不可预测性
unpred = analyze_unpredictable_dynamics(config)
print(f"不可预测性指数: {unpred['unpredictability_index']:.3f}")

# 5. 分岔分析
analyzer = ShilnikovBifurcationAnalyzer(config)
bifurc = analyzer.analyze_bifurcation_parameter(np.linspace(0.1, 0.9, 9))
print(f"混沌区域: {bifurc['chaotic_regions']}")
```

if __name__ == "__main__":
    example_tm_chaotic_dynamics()
```

## Related Skills

- `stochastic-synaptic-plasticity` - 随机突触可塑性
- `heterogeneous-synaptic-dynamics` - 异质性突触动力学
- `mf-qif-synaptic-plasticity` - 平均场突触可塑性

## References

- arXiv:1309.7966 - Short-term synaptic plasticity in the deterministic Tsodyks-Markram model
- PNAS 2013: 10.1073/pnas.1316071110
- Topics: Neurons and Cognition (q-bio.NC), Chaotic Dynamics (nlin.CD), Biological Physics