---
name: spiking-temporal-memory-stm-sequence-timing
description: Spiking Temporal Memory (sTM) model for learning sequence timing and control of replay speed in networks of spiking neurons
version: 1.0.0
author: Neuroscience Cron Job
created: 2026-06-09
arxiv_id: 2605.22523v1
paper_title: "Learning sequence timing and control of replay speed in networks of spiking neurons"
paper_date: 2026-05-21
activation_keywords:
  - spiking temporal memory
  - sTM model
  - sequence timing
  - replay speed control
  - oscillatory clock signal
  - working memory
  - spiking neural network
  - sequence processing
  - time representation
---

# Spiking Temporal Memory (sTM) for Sequence Timing

## 概述

该方法论扩展了 Spiking Temporal Memory (sTM) 模型，使其能够学习序列元素的精确时序，并通过振荡背景输入灵活控制序列重放速度。核心创新在于提出了一种机制：**序列元素的持续时间通过元素特异性神经元群体的顺序激活表示**，实现了跨广泛时间尺度的序列编码和重放。

## 背景：sTM 模型基础

### 原始 sTM 模型特点

**序列元素表示**：
- 每个序列元素由一小群神经元同步发放表示
- 活跃神经元集合编码元素在序列上下文中的身份
- **稀疏、上下文依赖的编码**

**原始模型的局限**：
- 只学习序列元素的顺序，不学习时序
- 无法灵活控制重放速度
- 缺乏生物可实现的时序编码机制

### 本研究的核心问题

1. **如何编码元素特异性时序？**
2. **如何灵活控制序列重放速度？**
3. **如何实现跨时间尺度的序列学习？**

## 核心方法论

### 1. 时序编码机制：元素持续时间表示

**关键洞察**：
- 序列元素的持续时间通过**元素特异性神经元群体的顺序激活**表示
- 每个序列元素分解为多个子状态，每个子状态由不同神经元群体激活
- 持续时间越长，激活的子状态越多

**机制示意**：
```
序列元素 A (持续时间 = 3个时间单位):
  - 子状态 A_1: 神经群体 G1 发放
  - 子状态 A_2: 神经群体 G2 发放  
  - 子状态 A_3: 神经群体 G3 发放
  
序列元素 B (持续时间 = 2个时间单位):
  - 子状态 B_1: 神经群体 G4 发放
  - 子状态 B_2: 神经群体 G5 发放
```

**神经网络架构**：
```python
import nest  # NEST simulator for spiking neural networks

class STMWithTiming:
    """
    扩展的 sTM 模型支持时序编码
    
    Attributes:
        element_neurons: 元素识别神经元群体
        timing_neurons: 时序编码神经元群体
        sequence_memory: 序列记忆连接矩阵
    """
    
    def __init__(self, n_elements, max_duration=10):
        """
        Args:
            n_elements: 序列元素数量
            max_duration: 最大持续时间单位
        """
        self.n_elements = n_elements
        self.max_duration = max_duration
        
        # 创建神经元群体
        self.element_neurons = nest.Create(
            'iaf_psc_alpha', 
            n=n_elements * max_duration  # 每个元素有 max_duration 个时序神经元
        )
        
        # 连接模式：顺序激活
        self.setup_timing_connections()
    
    def setup_timing_connections(self):
        """
        建立时序编码的顺序连接
        
        每个元素的时序神经元顺序连接：
        G1 -> G2 -> G3 ... (正向)
        """
        for elem_idx in range(self.n_elements):
            base_idx = elem_idx * self.max_duration
            
            for t in range(self.max_duration - 1):
                # 时序神经元 t -> t+1 连接
                nest.Connect(
                    self.element_neurons[base_idx + t],
                    self.element_neurons[base_idx + t + 1],
                    syn_spec={'weight': 2.0, 'delay': 1.0}
                )
    
    def encode_sequence(self, sequence):
        """
        编码带时序的序列
        
        Args:
            sequence: [(element_id, duration), ...] 序列元素和持续时间
        """
        for idx, (elem_id, duration) in enumerate(sequence):
            # 激活元素的时序神经元序列
            for t in range(duration):
                neuron_idx = elem_id * self.max_duration + t
                nest.SetStatus(
                    self.element_neurons[neuron_idx],
                    {'V_m': -50.0}  # 触发发放
                )
```

### 2. 振荡时钟信号机制

**核心发现**：
- 振荡背景输入可作为**时钟信号**
- 提供稳健、灵活的序列重放速度控制机制
- 重放速度与全局振荡活动特性相关（EEG/LFP 可观测）

**振荡输入建模**：
```python
import numpy as np

def oscillatory_clock_signal(frequency, amplitude, duration):
    """
    生成振荡时钟信号
    
    Args:
        frequency: 振荡频率 (Hz)
        amplitude: 振荡幅度
        duration: 信号持续时间 (s)
    
    Returns:
        signal: 振荡信号时间序列
    """
    time = np.linspace(0, duration, int(duration * 1000))
    
    # 正弦振荡
    signal = amplitude * np.sin(2 * np.pi * frequency * time)
    
    return signal

def inject_oscillation(neurons, oscillation_params):
    """
    向神经元群体注入振荡背景输入
    
    Args:
        neurons: NEST 神经元群体
        oscillation_params: {
            'frequency': 振荡频率,
            'amplitude': 幅度,
            'phase': 相位
        }
    """
    # 创建振荡输入发生器
    oscillation_generator = nest.Create(
        'ac_generator',
        params={
            'amplitude': oscillation_params['amplitude'],
            'frequency': oscillation_params['frequency'],
            'phase': oscillation_params['phase']
        }
    )
    
    # 连接到神经元群体
    nest.Connect(
        oscillation_generator,
        neurons,
        syn_spec={'weight': 1.0}
    )
```

**速度控制原理**：
- **振荡频率 ↑ → 重放速度 ↑**
- **振荡频率 ↓ → 重放速度 ↓**
- 不同频率对应不同速度倍率（如 2x、1x、0.5x）

**生物对应**：
- 清醒状态：高频率振荡（如 gamma band）→ 快速重放
- 睡眠状态：低频率振荡（如 delta band）→ 慢速重放
- EEG/LFP 观测到的全局振荡活动特性反映重放速度

### 3. 序列学习与重放完整流程

**学习阶段**：
```python
def learn_sequence_with_timing(sequence_data, stm_model):
    """
    学习带时序的序列
    
    Args:
        sequence_data: 输入序列数据（包含元素和持续时间）
        stm_model: sTM 模型实例
    
    Returns:
        learned_weights: 学习到的连接权重
    """
    # 阶段 1: 元素顺序学习
    for i in range(len(sequence_data) - 1):
        current_elem = sequence_data[i][0]
        next_elem = sequence_data[i + 1][0]
        
        # 建立元素间的预测连接
        stm_model.connect_elements(current_elem, next_elem)
    
    # 阶段 2: 时序编码学习
    for elem_id, duration in sequence_data:
        # 学习持续时间表示
        stm_model.encode_duration(elem_id, duration)
    
    # 阶段 3: 通过 STDP 优化连接
    stm_model.optimize_connections(stdp_rule='stdp')
    
    return stm_model.get_weights()
```

**重放阶段**：
```python
def replay_sequence(stm_model, speed_factor=1.0):
    """
    以指定速度重放序列
    
    Args:
        stm_model: 已学习的 sTM 模型
        speed_factor: 重放速度倍率 (0.5x, 1x, 2x, etc.)
    
    Returns:
        replay_pattern: 重放的脉冲模式
    """
    # 计算振荡频率
    base_frequency = 40.0  # Hz (gamma band)
    oscillation_frequency = base_frequency * speed_factor
    
    # 注入振荡时钟信号
    stm_model.inject_clock_signal(
        frequency=oscillation_frequency,
        amplitude=1.0
    )
    
    # 触发序列重放（从第一个元素开始）
    stm_model.trigger_replay(start_element=0)
    
    # 记录脉冲活动
    spike_recorder = nest.Create('spike_recorder')
    nest.Connect(stm_model.element_neurons, spike_recorder)
    
    # 运行模拟
    nest.Simulate(1000.0)  # 1秒
    
    # 获取重放模式
    spikes = nest.GetStatus(spike_recorder, 'events')[0]
    
    return spikes
```

### 4. 稀疏时空模式编码

**关键特性**：
- **elapsed time is encoded by unique and sparse spatiotemporal patterns**
- 每个时间点对应独特的时空发放模式
- 稀疏表示减少资源消耗，提高效率

**时空模式可视化**：
```python
import matplotlib.pyplot as plt

def visualize_spatiotemporal_pattern(spike_events, n_neurons):
    """
    可视化稀疏时空发放模式
    
    Args:
        spike_events: NEST spike_recorder events
        n_neurons: 神经元数量
    """
    times = spike_events['times']
    neurons = spike_events['senders']
    
    # 创建 raster plot
    plt.figure(figsize=(12, 8))
    plt.scatter(times, neurons, s=1, c='black', marker='.')
    
    plt.xlabel('Time (ms)')
    plt.ylabel('Neuron ID')
    plt.title('Sparse Spatiotemporal Pattern: Time Encoding')
    plt.grid(True, alpha=0.3)
    
    plt.show()

def analyze_pattern_sparsity(spike_events, time_window):
    """
    分析时空模式的稀疏度
    
    Returns:
        sparsity_ratio: 稀疏度比例
    """
    times = spike_events['times']
    
    # 计算每个时间窗口的活跃神经元比例
    window_activity = []
    for t_start in range(0, max(times), time_window):
        window_spikes = [s for s in times if t_start <= s < t_start + time_window]
        activity_ratio = len(window_spikes) / n_neurons
        window_activity.append(activity_ratio)
    
    sparsity_ratio = 1 - np.mean(window_activity)
    
    return sparsity_ratio
```

## 实验验证要点

### 1. 时序编码能力测试

**测试任务**：
- 序列元素具有不同持续时间（如 100ms, 200ms, 500ms）
- 验证模型能否准确学习并重现时序

**评估指标**：
```python
def evaluate_timing_accuracy(learned_sequence, target_sequence):
    """
    评估时序学习准确度
    
    Returns:
        timing_error: 时序误差 (ms)
        order_accuracy: 顺序准确度
    """
    timing_errors = []
    
    for i in range(len(target_sequence)):
        target_duration = target_sequence[i][1]
        learned_duration = learned_sequence[i][1]
        
        error = abs(target_duration - learned_duration)
        timing_errors.append(error)
    
    return {
        'mean_timing_error': np.mean(timing_errors),
        'max_timing_error': np.max(timing_errors),
        'order_accuracy': evaluate_order(learned_sequence, target_sequence)
    }
```

### 2. 重放速度控制测试

**测试条件**：
- 不同振荡频率：10 Hz, 20 Hz, 40 Hz, 80 Hz
- 验证重放速度与振荡频率的关系

**预期结果**：
- 振荡频率 ↑ → 重放速度 ↑（线性关系）
- 速度范围：0.25x ~ 4x

### 3. 跨时间尺度测试

**测试范围**：
- 短时序序列：毫秒级（如 50ms ~ 200ms）
- 中时序序列：秒级（如 1s ~ 5s）
- 长时序序列：分钟级（如 1min ~ 5min）

### 4. 生物可实现性验证

**验证维度**：
- 神经元模型：使用生物可实现模型（如 LIF, Izhikevich）
- 连接规则：遵循生物约束（如 Dale's law, 轴突延迟）
- 振荡对应：匹配 EEG/LFP 观测数据

## 应用场景

### 1. 工作记忆研究
- 序列记忆的神经机制
- 时序记忆的编码与提取
- 工作记忆容量限制研究

### 2. 语言处理
- 语音序列的时序编码
- 语言节奏学习
- 句法结构的时间表示

### 3. 运动控制
- 运动序列学习
- 动作节奏控制
- 运动技能巩固

### 4. 睡眠与记忆巩固
- 睡眠期间的序列重放
- 振荡活动与记忆巩固的关系
- REM vs. NREM 状态的重放速度差异

### 5. 神经形态计算
- 时间序列处理硬件实现
- 低功耗序列记忆系统
- 实时序列重放应用

## 关键优势

1. **生物可实现**：基于真实的脉冲神经元和网络架构
2. **时序精确性**：准确编码序列元素的持续时间
3. **速度灵活控制**：振荡机制提供简单有效的速度调节
4. **跨时间尺度**：支持从毫秒到分钟的时序编码
5. **稀疏高效**：时空模式稀疏表示减少资源消耗

## 技术实现建议

### 1. NEST 模拟器实现

**完整模型代码**：
```python
import nest
import numpy as np

class STMCompleteModel:
    """
    完整的 sTM 时序模型实现
    """
    
    def __init__(self, config):
        # 初始化 NEST
        nest.ResetKernel()
        nest.SetKernelStatus({
            'resolution': 0.1,  # 0.1 ms
            'local_num_threads': 4
        })
        
        # 网络参数
        self.n_elements = config['n_elements']
        self.max_duration = config['max_duration']
        
        # 创建神经元
        self.create_neurons()
        
        # 创建连接
        self.create_connections()
        
        # 创建记录器
        self.create_recorders()
    
    def create_neurons(self):
        """
        创建神经元群体
        """
        # 时序编码神经元
        self.timing_neurons = nest.Create(
            'iaf_psc_alpha',
            n=self.n_elements * self.max_duration,
            params={
                'V_th': -50.0,
                'V_reset': -70.0,
                'tau_m': 20.0,
                'C_m': 250.0
            }
        )
        
        # 振荡时钟输入
        self.clock_generator = nest.Create(
            'ac_generator',
            params={'amplitude': 1.0, 'frequency': 40.0}
        )
    
    def create_connections(self):
        """
        建立网络连接
        """
        # 时序顺序连接
        for elem in range(self.n_elements):
            for t in range(self.max_duration - 1):
                nest.Connect(
                    self.timing_neurons[elem * self.max_duration + t],
                    self.timing_neurons[elem * self.max_duration + t + 1],
                    syn_spec={'weight': 2.0, 'delay': 1.0}
                )
        
        # 振荡时钟注入
        nest.Connect(
            self.clock_generator,
            self.timing_neurons,
            syn_spec={'weight': 1.0}
        )
    
    def create_recorders(self):
        """
        创建记录设备
        """
        self.spike_recorder = nest.Create('spike_recorder')
        nest.Connect(self.timing_neurons, self.spike_recorder)
    
    def run_simulation(self, duration):
        """
        运行模拟
        """
        nest.Simulate(duration)
        
        spikes = nest.GetStatus(self.spike_recorder, 'events')[0]
        
        return spikes
```

### 2. NeuroML 标准化实现

```xml
<!-- NeuroML 定义 -->
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2">
  <network id="STMWithTiming">
    <population id="timing_neurons" component="iaf" size="100"/>
    
    <continuousConnection id="timing_chain">
      <!-- 时序顺序连接 -->
      <from population="timing_neurons" cell="0"/>
      <to population="timing_neurons" cell="1"/>
      <synapse component="excitatory"/>
    </continuousConnection>
    
    <inputList id="oscillatory_clock">
      <input id="clock_0" target="timing_neurons[0]" component="oscillation"/>
    </inputList>
  </network>
</neuroml>
```

## 参考文献

- arXiv:2605.22523v1 - "Learning sequence timing and control of replay speed in networks of spiking neurons"
- Diesmann et al. - 脉冲神经网络模拟
- STDP 学习规则文献
- EEG/LFP 振荡与睡眠研究

## 相关 Skill

- [[spiking-neural-network-simulation]] - 脉冲神经网络模拟方法
- [[oscillatory-brain-dynamics]] - 振荡脑动力学
- [[sequence-memory-learning]] - 序列记忆学习
- [[working-memory-neural-models]] - 工作记忆神经模型
- [[neuromorphic-hardware-sequence]] - 神经形态硬件序列处理