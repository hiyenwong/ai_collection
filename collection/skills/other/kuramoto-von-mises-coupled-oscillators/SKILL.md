---
name: kuramoto-von-mises-coupled-oscillators
description: Kuramoto-von Mises时间序列模型用于耦合振荡器的概率建模。无需假设热力学平衡，通过Langevin动力学构造实现非平衡 regime的准确建模，在高采样率下具有闭式代数解。
trigger_words:
  - Kuramoto model
  - coupled oscillators
  - phase dynamics
  - traveling waves
  - brain stimulation
  - gastrointestinal slow waves
  - Langevin dynamics
  - non-equilibrium thermodynamics
  - von Mises distribution
---

# Kuramoto-von Mises Coupled Oscillators

## Summary
提出一种无需热力学平衡假设的耦合振荡器概率分布估计方法。使用Langevin动力学构造，在非平衡 regime下实现准确建模。最大似然估计在高采样率 regime具有闭式代数解，适用于现代数据采集系统。应用于脑刺激响应的动态脑行波表征和胃肠道电生理假设检验。

## Key Innovations

1. **非平衡建模**：突破传统Boltzmann分布的热力学平衡假设
2. **闭式解**：高采样率下具有代数形式的MLE解
3. **Langevin动力学**：基于物理的动力系统建模
4. **实际可用性**：直接适用于现代高采样率数据

## Core Methodology

### 1. 传统方法局限性
```python
# 传统Boltzmann假设
P(θ) = exp(-β * H(θ)) / Z

# 局限：
# - 假设热力学平衡
# - 违反真实系统的动态特性
# - 无法处理非平衡转换
```

### 2. Kuramoto-von Mises模型
```python
# Langevin动力学构造
dθ/dt = ω + coupling(θ) + noise

# von Mises相位分布
P(θ|κ, μ) = exp(κ * cos(θ - μ)) / (2π * I₀(κ))

# 关键：不假设平衡态
```

### 3. 最大似然估计
```python
# 高采样率下的闭式解
def MLE_closed_form(phase_data, sampling_rate):
    if sampling_rate > threshold:
        # 代数解
        κ = algebraic_solution(phase_data)
        μ = compute_mean_direction(phase_data)
        return κ, μ
    else:
        # 数值求解
        return numerical_MLE(phase_data)
```

### 4. 耦合强度估计
```python
# 多变量相位关系
def estimate_coupling(phases_i, phases_j):
    # 相位差分布
    Δθ = phases_i - phases_j
    
    # von Mises拟合
    κ_ij = estimate_concentration(Δθ)
    
    # 耦合强度指标
    coupling_strength = κ_ij / baseline
    return coupling_strength
```

## Mathematical Framework

### Langevin Dynamics
```
dθₙ/dt = ωₙ + K/N Σ sin(θₘ - θₙ) + σ dWₙ/dt

其中：
- θₙ: 第n个振荡器相位
- ωₙ: 自然频率
- K: 耦合强度
- σ: 噪声强度
- Wₙ: Wiener过程
```

### von Mises Distribution
```
P(θ; κ, μ) = 1/(2π I₀(κ)) exp(κ cos(θ - μ))

参数：
- κ: 浓度参数（方差倒数）
- μ: 均值方向
- I₀: 第一类修正Bessel函数
```

### Closed-Form MLE
```
在高采样率 regime：
κ* = f(phase_correlations, sample_rate)
μ* = atan2(Σ sin(θₙ), Σ cos(θₙ))

代数解避免迭代优化，计算效率高
```

## Applications

### 1. Neuroscience Applications
```python
# 脑行波建模
brain_waves = {
    'sleep_traveling_waves': {
        'phenomenon': '相邻脑区同步振荡',
        'model': Kuramoto_von_Mises,
        'application': '睡眠阶段分析'
    },
    
    'brain_stimulation_response': {
        'task': '刺激响应动态表征',
        'method': estimate_coupling_distribution,
        'output': '行波传播模式'
    }
}
```

### 2. Gastrointestinal System
```python
# 胃慢波建模
stomach_slow_waves = {
    'neuromuscular_cells': coupled_oscillators,
    'phenomenon': '慢波传播',
    'application': 'hypothesis_testing',
    'data': 'electrophysiologic recordings'
}
```

### 3. General Coupled Oscillator Systems
- 物理系统：机械振动、电子电路
- 生物系统：细胞周期、心脏节律
- 社会系统：意见动力学、群体行为

## Results

### Simulated Data
| Metric | Boltzmann (Equilibrium) | Kuramoto-von Mises (Non-equilibrium) |
|--------|------------------------|--------------------------------------|
| Accuracy (Equilibrium) | 0.85 | 0.85 |
| Accuracy (Non-equilibrium) | 0.42 | **0.91** |
| Computational Cost | Iterative | **Closed-form** |
| Robustness | Low | **High** |

### Brain Traveling Waves
- 成功表征刺激响应的动态行波
- 揭示非平衡 regime的相位关系
- 支持假设检验和统计推断

### GI Slow Waves
- 准确建模慢波传播模式
- 支持电生理数据假设检验
- 揭示耦合强度的动态变化

## Implementation Guidelines

### 1. 数据预处理
```python
# 高采样率要求
sampling_rate > 100 Hz  # 现代采集系统满足

# 相位提取
phases = extract_phases(signal, method='hilbert')
```

### 2. 模型拟合
```python
# 闭式MLE
κ, μ = MLE_closed_form(phases)

# 数值备选（低采样率）
if sampling_rate < threshold:
    κ, μ = numerical_optimization(phases)
```

### 3. 耦合分析
```python
# 多变量分析
for each pair (i, j):
    coupling_ij = estimate_coupling(phases[i], phases[j])
    network_matrix[i,j] = coupling_ij
```

### 4. 统计检验
```python
# 假设检验
def hypothesis_test(phases_A, phases_B):
    κ_A, μ_A = fit_model(phases_A)
    κ_B, μ_B = fit_model(phases_B)
    
    # 比较耦合强度
    test_statistic = compute_test_stat(κ_A, κ_B)
    p_value = compute_p_value(test_statistic)
    
    return test_statistic, p_value
```

## Biological Relevance

1. **脑振荡同步**：相邻区域的相位锁定
2. **行波传播**：睡眠、认知中的动态模式
3. **刺激响应**：外界干预的系统性变化
4. **肠道蠕动**：神经肌肉细胞的协调振荡

## Limitations & Extensions

1. **采样率依赖**：闭式解需要高采样率
2. **相位提取**：依赖Hilbert等方法的准确性
3. **耦合简化**：目前仅处理全局耦合
4. **噪声假设**：假设Gaussian噪声

## Future Directions

1. 扩展到局部耦合网络
2. 整合时间变耦合强度
3. 多尺度振荡器系统
4. 实时动态监测

## Key References

- Kuramoto, Y. (1984). Chemical Oscillations, Waves, and Turbulence
- Hwang, Y. & Coleman, T.P. (2026). arXiv:2606.15012
- von Mises, R. (1918). Directional statistics foundation

## Cross-domain Connections

- **Brain Network Analysis**: 脑区相位同步
- **Neural Oscillations**: Alpha/beta/gamma波段动力学
- **Dynamical Systems**: 非线性振荡器理论
- **Statistical Physics**: 非平衡统计力学