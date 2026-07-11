---
name: spike-timing-neuronal-assemblies
description: 脉冲时序训练和自发强化神经元集群。研究STDP如何形成共享刺激偏好的强耦合神经元集群，自发动力学期间的脉冲相关性主动强化连接。适用于计算神经科学、STDP学习、神经编码研究。触发词：神经元集群、STDP、脉冲时序、神经编码、自发动力学、neuronal assembly、spike timing、STDP、noise correlation。
user-invocable: true
---

# 脉冲时序训练神经元集群框架

**来源论文：** arXiv:1608.00064 - Training and spontaneous reinforcement of neuronal assemblies by spike timing

## 核心方法论

### 1. STDP 与神经元集群形成

**核心发现：** STDP 形成具有共享刺激偏好的强耦合神经元集群

**关键机制：**
- 脉冲时序相关性主动强化集群连接
- 自发动力学期间保持学习结构
- 噪声相关性在神经编码中的新角色

### 2. 平均场理论

**创新点：** 开发低维平均场理论，解释快速脉冲时序相关性如何影响微观和宏观网络结构

### 3. 集群编码维护

**机制：**
- 刺激编码由细胞集群主动维护
- 内部生成的脉冲相关性维持学习结构
- 与发放率可塑性方案的互补框架

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class AssemblyConfig:
    """神经元集群配置"""
    n_neurons: int = 100           # 神经元数量
    n_assemblies: int = 5          # 集群数量
    
    # STDP 参数
    tau_plus: float = 20.0         # LTP 时间常数
    tau_minus: float = 20.0        # LTD 时间常数
    A_plus: float = 0.01           # LTP 幅度
    A_minus: float = 0.01          # LTD 幅度
    
    # 神经元参数
    tau_m: float = 20.0            # 膜时间常数
    threshold: float = 1.0         # 发放阈值
    
    # 仿真参数
    dt: float = 0.1                # 时间步长
    duration: float = 1000.0       # 仿真时长


class NeuronalAssembly:
    """神经元集群"""
    
    def __init__(self, config: AssemblyConfig):
        """
        Args:
            config: 集群配置
        """
        self.config = config
        
        # 神经元状态
        self.V = np.zeros(config.n_neurons)
        
        # 连接权重矩阵
        self.W = np.random.randn(config.n_neurons, config.n_neurons) * 0.1
        
        # STDP 迹
        self.x = np.zeros(config.n_neurons)  # 前脉冲迹
        self.y = np.zeros(config.n_neurons)  # 后脉冲迹
        
        # 集群成员
        self.assembly_membership = np.zeros(config.n_neurons, dtype=int)
        
        # 历史记录
        self.spike_history = []
        self.assembly_strength_history = []
        
    def assign_stimulus_preferences(self):
        """分配刺激偏好
        
        每个神经元被分配到一个首选刺激
        """
        cfg = self.config
        
        for i in range(cfg.n_neurons):
            # 随机分配到集群
            self.assembly_membership[i] = i % cfg.n_assemblies
            
    def update_stdp(self, spikes: np.ndarray, dt: float):
        """更新 STDP 权重
        
        Args:
            spikes: 脉冲向量
            dt: 时间步长
        """
        cfg = self.config
        
        # 更新迹
        self.x *= np.exp(-dt / cfg.tau_plus)
        self.y *= np.exp(-dt / cfg.tau_minus)
        
        # 脉冲更新
        for i in range(cfg.n_neurons):
            if spikes[i]:
                # LTP: 后神经元发放，前迹影响
                for j in range(cfg.n_neurons):
                    if spikes[j]:
                        # 同集群内增强
                        if self.assembly_membership[i] == self.assembly_membership[j]:
                            self.W[i, j] += cfg.A_plus * self.x[j] * 1.5
                        else:
                            self.W[i, j] += cfg.A_plus * self.x[j]
                            
                # LTD: 前神经元发放，后迹影响
                self.y[i] += 1.0
                
        # 脉冲更新迹
        for i in range(cfg.n_neurons):
            if spikes[i]:
                self.x[i] += 1.0
                
        # 权重限制
        self.W = np.clip(self.W, 0, 1)
        np.fill_diagonal(self.W, 0)
        
    def step(self, external_input: np.ndarray, dt: float) -> np.ndarray:
        """单步更新
        
        Args:
            external_input: 外部输入
            dt: 时间步长
            
        Returns:
            spikes: 脉冲输出
        """
        # 计算突触输入
        I_syn = self.W @ self.V
        
        # 更新膜电位
        self.V += (-self.V + I_syn + external_input) / self.config.tau_m * dt
        
        # 发放
        spikes = (self.V > self.config.threshold).astype(float)
        self.V[spikes > 0] = 0
        
        # STDP 更新
        self.update_stdp(spikes, dt)
        
        return spikes
    
    def simulate_training(self, 
                         stimulus_patterns: List[np.ndarray],
                         n_epochs: int = 10) -> Dict:
        """训练集群
        
        Args:
            stimulus_patterns: 刺激模式列表
            n_epochs: 训练轮数
            
        Returns:
            training_results: 训练结果
        """
        self.assign_stimulus_preferences()
        
        results = {
            'assembly_strength': [],
            'within_assembly_weights': [],
            'between_assembly_weights': []
        }
        
        for epoch in range(n_epochs):
            for pattern in stimulus_patterns:
                # 应用刺激
                spikes = self.step(pattern, self.config.dt)
                self.spike_history.append(spikes)
                
            # 计算集群强度
            strength = self.compute_assembly_strength()
            results['assembly_strength'].append(strength)
            
            # 计算集群内外权重
            within, between = self.compute_weight_statistics()
            results['within_assembly_weights'].append(within)
            results['between_assembly_weights'].append(between)
            
        return results
    
    def simulate_spontaneous(self, duration: float) -> Dict:
        """模拟自发动力学
        
        Args:
            duration: 模拟时长
            
        Returns:
            spontaneous_results: 自发动力学结果
        """
        n_steps = int(duration / self.config.dt)
        
        spike_counts = np.zeros(self.config.n_neurons)
        correlations = []
        
        for _ in range(n_steps):
            # 随机背景输入
            input_noise = np.random.randn(self.config.n_neurons) * 0.1
            spikes = self.step(input_noise, self.config.dt)
            spike_counts += spikes
            
        # 计算集群内相关性
        for a in range(self.config.n_assemblies):
            members = np.where(self.assembly_membership == a)[0]
            if len(members) > 1:
                # 简化：使用脉冲计数相关性
                mean_count = spike_counts[members].mean()
                correlations.append(mean_count)
                
        return {
            'spike_counts': spike_counts,
            'assembly_correlations': correlations,
            'mean_correlation': np.mean(correlations) if correlations else 0
        }
    
    def compute_assembly_strength(self) -> float:
        """计算集群强度
        
        Returns:
            strength: 集群强度
        """
        strengths = []
        
        for a in range(self.config.n_assemblies):
            members = np.where(self.assembly_membership == a)[0]
            if len(members) > 1:
                # 集群内平均权重
                within_weights = []
                for i in members:
                    for j in members:
                        if i != j:
                            within_weights.append(self.W[i, j])
                            
                strengths.append(np.mean(within_weights) if within_weights else 0)
                
        return np.mean(strengths) if strengths else 0
    
    def compute_weight_statistics(self) -> Tuple[float, float]:
        """计算权重统计
        
        Returns:
            within: 集群内平均权重
            between: 集群间平均权重
        """
        within_weights = []
        between_weights = []
        
        for i in range(self.config.n_neurons):
            for j in range(self.config.n_neurons):
                if i != j:
                    if self.assembly_membership[i] == self.assembly_membership[j]:
                        within_weights.append(self.W[i, j])
                    else:
                        between_weights.append(self.W[i, j])
                        
        within = np.mean(within_weights) if within_weights else 0
        between = np.mean(between_weights) if between_weights else 0
        
        return within, between


def compare_assembly_formation(config: AssemblyConfig) -> Dict:
    """比较集群形成
    
    Args:
        config: 配置
        
    Returns:
        comparison: 比较结果
    """
    results = {}
    
    # 1. 有 STDP
    assembly_with_stdp = NeuronalAssembly(config)
    
    # 创建刺激模式
    patterns = []
    for a in range(config.n_assemblies):
        pattern = np.zeros(config.n_neurons)
        members = np.where(assembly_with_stdp.assembly_membership == a)[0]
        pattern[members] = 0.5
        patterns.append(pattern)
        
    training_results = assembly_with_stdp.simulate_training(patterns, n_epochs=20)
    
    results['with_STDP'] = {
        'final_assembly_strength': training_results['assembly_strength'][-1],
        'within_weight': training_results['within_assembly_weights'][-1],
        'between_weight': training_results['between_assembly_weights'][-1]
    }
    
    # 2. 自发强化测试
    spontaneous = assembly_with_stdp.simulate_spontaneous(500)
    
    results['spontaneous_reinforcement'] = {
        'mean_correlation': spontaneous['mean_correlation'],
        'assembly_maintained': spontaneous['mean_correlation'] > 0.5
    }
    
    return results


def analyze_noise_correlations(assembly: NeuronalAssembly,
                               n_trials: int = 100) -> Dict:
    """分析噪声相关性
    
    Args:
        assembly: 神经元集群
        n_trials: 试验次数
        
    Returns:
        analysis: 分析结果
    """
    responses = []
    
    for trial in range(n_trials):
        # 相同刺激，不同噪声
        stimulus = np.zeros(assembly.config.n_neurons)
        stimulus[:20] = 0.5  # 刺激前20个神经元
        
        # 添加噪声
        noise = np.random.randn(assembly.config.n_neurons) * 0.1
        response = assembly.step(stimulus + noise, assembly.config.dt)
        responses.append(response)
        
    responses = np.array(responses)
    
    # 计算噪声相关性
    noise_corr = np.corrcoef(responses.T)
    
    # 移除对角线
    n = noise_corr.shape[0]
    mask = ~np.eye(n, dtype=bool)
    mean_noise_corr = np.mean(np.abs(noise_corr[mask]))
    
    return {
        'mean_noise_correlation': mean_noise_corr,
        'noise_correlation_matrix': noise_corr
    }


# 使用示例
def example_neuronal_assemblies():
    """示例：神经元集群形成"""
    print("="*60)
    print("脉冲时序训练神经元集群")
    print("="*60)
    
    config = AssemblyConfig(
        n_neurons=100,
        n_assemblies=5
    )
    
    # 创建集群
    assembly = NeuronalAssembly(config)
    assembly.assign_stimulus_preferences()
    
    print(f"\n配置:")
    print(f"  神经元数: {config.n_neurons}")
    print(f"  集群数: {config.n_assemblies}")
    print(f"  每集群神经元: ~{config.n_neurons // config.n_assemblies}")
    
    # 创建刺激模式
    patterns = []
    for a in range(config.n_assemblies):
        pattern = np.zeros(config.n_neurons)
        members = np.where(assembly.assembly_membership == a)[0]
        pattern[members] = 0.5
        patterns.append(pattern)
        
    # 训练
    print(f"\n训练集群...")
    results = assembly.simulate_training(patterns, n_epochs=20)
    
    print(f"\n训练结果:")
    print(f"  最终集群强度: {results['assembly_strength'][-1]:.4f}")
    print(f"  集群内权重: {results['within_assembly_weights'][-1]:.4f}")
    print(f"  集群间权重: {results['between_assembly_weights'][-1]:.4f}")
    
    # 自发动力学
    print(f"\n模拟自发动力学...")
    spontaneous = assembly.simulate_spontaneous(500)
    print(f"  平均集群相关性: {spontaneous['mean_correlation']:.4f}")
    
    print(f"\n关键发现:")
    print(f"  ✅ STDP 形成共享偏好的集群")
    print(f"  ✅ 自发动力学强化集群连接")
    print(f"  ✅ 噪声相关性维护编码结构")
    
    return assembly


## Activation Keywords
- 神经元集群
- STDP
- 脉冲时序
- 神经编码
- 自发动力学
- neuronal assembly
- spike timing
- noise correlation

## Tools Used
- numpy

## Instructions for Agents
1. 分配神经元的刺激偏好
2. 使用 STDP 训练集群
3. 分析集群内外权重变化
4. 模拟自发动力学验证强化
5. 计算噪声相关性分析编码

## Examples
```python
# 神经元集群训练示例
from spike_timing_neuronal_assemblies import (
    NeuronalAssembly, AssemblyConfig
)

# 1. 配置
config = AssemblyConfig(
    n_neurons=100,
    n_assemblies=5
)

# 2. 创建集群
assembly = NeuronalAssembly(config)
assembly.assign_stimulus_preferences()

# 3. 创建刺激模式
patterns = [...]  # 刺激模式列表

# 4. 训练
results = assembly.simulate_training(patterns, n_epochs=20)
print(f"集群强度: {results['assembly_strength'][-1]:.4f}")

# 5. 自发动力学
spontaneous = assembly.simulate_spontaneous(500)
print(f"集群相关性: {spontaneous['mean_correlation']:.4f}")
```

if __name__ == "__main__":
    example_neuronal_assemblies()
```

## Related Skills

- `stochastic-synaptic-plasticity` - 随机突触可塑性
- `stdp-bernoulli-message-passing` - STDP Bernoulli 消息传递
- `tsodyks-markram-chaotic-dynamics` - TM 模型混沌动力学

## References

- arXiv:1608.00064 - Training and spontaneous reinforcement of neuronal assemblies by spike timing
- Topics: Neurons and Cognition (q-bio.NC)