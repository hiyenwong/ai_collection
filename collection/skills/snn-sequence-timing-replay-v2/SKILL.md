---
name: snn-sequence-timing-replay-v2
description: Spiking Temporal Memory (sTM) model extension for learning sequence timing and controlling replay speed via oscillatory background inputs
category: neuroscience
authors: ["Melissa Lober", "Younes Bouhadjar", "Markus Diesmann", "Tom Tetzlaff"]
arxiv_id: "2605.22523"
submission_date: "2026-05-21"
doi: "https://doi.org/10.48550/arXiv.2605.22523"
tags: ["spiking neural network", "sequence timing", "temporal memory", "replay control", "oscillatory dynamics", "biologically plausible"]
activation_keywords: ["sequence timing", "replay speed", "spiking temporal memory", "oscillatory control", "element-specific timing", "EEG/LFP oscillation"]
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

## 概述

扩展 sTM（spiking Temporal Memory）模型以学习序列元素的精确时序，并通过振荡背景输入灵活控制序列重放速度。

## 核心创新

### 1. 元素特定时序编码机制

**问题**：原sTM模型仅学习序列顺序，无法编码元素间时间间隔。

**解决方案**：
- 每个序列元素持续时间由元素特定神经元群体的顺序激活表示
- 稀疏时空模式编码经过时间，支持宽范围时间尺度
- 同步激活的小神经元集合编码元素身份和序列上下文

**数学框架**：
```
序列 S = {e₁, e₂, ..., eₙ} with timing {t₁, t₂, ..., tₙ}
元素持续时间 Δt_i 由神经元群体 P_i = {n₁, n₂, ..., nₖ} 的顺序激活编码
总时间编码: T = Σ Δt_i = Σ |P_i| × τ_base
```

### 2. 振荡背景输入作为时钟信号

**机制**：
- 振荡背景输入（模拟EEG/LFP全局振荡）作为时钟信号
- 振荡频率调制重放速度：f_clock → v_replay
- 支持清醒和睡眠状态不同重放速度

**生物对应**：
- 清醒状态：高频振荡 → 快速重放
- 睡眠状态：低频振荡 → 慢速重放（记忆巩固）
- EEG/LFP记录的振荡特性与重放速度相关性

### 3. 灵活重放速度控制

**实现方式**：
- 振荡相位触发元素切换
- 相位锁定确保元素间同步
- 频率调制实现速度调整

**控制方程**：
```
v_replay = f_clock × k_phase
k_phase = 相位耦合强度参数
```

## 方法论框架

### 模型结构

1. **输入层**：接收序列元素（有序刺激）
2. **时空编码层**：
   - 元素身份编码（稀疏神经元集合）
   - 时序编码（顺序激活的持续时间群体）
3. **振荡调制层**：背景振荡输入控制重放速度
4. **输出层**：序列重放（带精确时序）

### 学习规则

- **顺序学习**：标准sTM机制（序列位置依赖）
- **时序学习**：持续时间群体的STDP适应
- **振荡适应**：频率-速度映射的在线调整

### 关键参数

| 参数 | 范围 | 说明 |
|------|------|------|
| τ_base | 10-50 ms | 基础神经元激活周期 |
| f_clock | 4-100 Hz | 振荡时钟频率（θ波到γ波） |
| k_phase | 0.5-2.0 | 相位耦合强度 |
| |P_i| | 5-20 | 每个元素的持续时间群体大小 |

## 应用场景

### 1. 序列记忆学习

- **语言处理**：学习语音序列的节奏和停顿
- **音乐感知**：学习旋律的时序结构
- **运动控制**：学习动作序列的时间协调

### 2. 记忆巩固模拟

- 睡眠状态慢振荡 → 慢速重放 → 记忆巩固
- 清醒状态快振荡 → 快速重放 → 工作记忆刷新

### 3. BCI应用

- 序列任务的精确时间预测
- 基于EEG振荡状态的适应性控制

## 技术实现要点

### SNN实现

```python
# 伪代码结构
class SpikingTemporalMemoryV2:
    def __init__(self, base_tau=20, clock_freq=10, phase_coupling=1.0):
        self.element_groups = {}  # 元素身份编码
        self.duration_populations = {}  # 时序编码
        self.clock_oscillator = Oscillator(freq=clock_freq)
        self.phase_coupling = phase_coupling
    
    def encode_sequence(self, sequence, timings):
        for elem, duration in zip(sequence, timings):
            # 元素身份编码
            identity_group = select_sparse_group(elem)
            # 时序编码（持续时间群体）
            duration_pop = create_duration_population(duration, self.base_tau)
            self.duration_populations[elem] = duration_pop
    
    def replay(self, sequence):
        for elem in sequence:
            # 振荡相位触发
            phase = self.clock_oscillator.get_phase()
            # 顺序激活持续时间群体
            for neuron in self.duration_populations[elem]:
                fire_with_timing(neuron, phase, self.phase_coupling)
```

### 振荡调制实现

- **振荡源**：模拟背景振荡（正弦/脉冲）
- **相位触发**：相位阈值触发元素切换
- **频率调制**：动态调整振荡频率改变重放速度

### 稀疏编码策略

- 每个元素由固定大小神经元集合编码（5-20个）
- 稀疏性确保高效和鲁棒性
- 顺序激活避免同时激活冲突

## 验证指标

1. **时序精度**：重放序列与原序列时间偏差
2. **速度灵活性**：不同振荡频率下的重放速度范围
3. **生物对应性**：EEG/LFP振荡特性与重放速度相关性

## 与现有工作对比

| 模型 | 顺序编码 | 时序编码 | 重放控制 | 生物合理性 |
|------|----------|----------|----------|------------|
| Standard Hopfield | ✓ | ✗ | ✗ | 低 |
| LSTM | ✓ | ✓ | ✗ | 低 |
| sTM (原版) | ✓ | ✗ | ✗ | 高 |
| **sTM v2 (本工作)** | ✓ | ✓ | ✓ | **高** |

## 局限与扩展方向

### 当前局限

1. 时序范围受限于神经元激活周期
2. 振荡调制精度依赖振荡源稳定性
3. 大规模序列的计算成本

### 扩展方向

1. 多振荡耦合（θ-γ耦合）
2. 学习可变持续时间群体大小
3. 与其他SNN模型集成（如NEST模拟）
4. 实验验证（EEG/LFP数据分析）

## 参考文献

- Lober et al. (2026) - 本工作
- Tetzlaff et al. (前序sTM工作)
- Diesmann et al. (NEST模拟器)
- EEG/LFP振荡与记忆巩固研究

## 关键术语

- **sTM**：Spiking Temporal Memory，脉冲时序记忆模型
- **元素特定时序编码**：Element-specific timing encoding
- **振荡背景输入**：Oscillatory background input
- **时钟信号**：Clock signal for replay control
- **稀疏时空模式**：Sparse spatiotemporal pattern
- **重放速度控制**：Replay speed control via oscillation

---

**Activation**: 当讨论序列学习、时序编码、脉冲神经网络、记忆重放、振荡控制、EEG/LFP分析时激活此技能。

**Related Skills**: 
- `snn-sequence-timing-replay` (原版，无时序)
- `snn-working-memory-heterogeneous-delays`
- `learning-sequence-timing-snn`
- `kuramoto-brain-network` (振荡建模)