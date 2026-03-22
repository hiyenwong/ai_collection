---
name: music-perception-brain-network
description: 音乐感知脑网络建模方法论。使用FitzHugh-Nagumo模型和经验脑连接数据研究听觉刺激对神经网络动力学的影响，分析同步与频率/振幅的关系。触发词：音乐感知、脑网络、听觉刺激、神经同步、FitzHugh-Nagumo、gamma同步、music perception、brain network、auditory stimulus。
user-invocable: true
---

# 音乐感知脑网络建模

基于 arXiv:2504.07721 - "From empirical brain networks towards modeling music perception"

## 核心方法论

### 1. FitzHugh-Nagumo (FHN) 模型

FHN模型是简化的神经元模型，用于模拟神经元的兴奋性：

```python
import numpy as np
from scipy.integrate import odeint

class FitzHughNagumoNetwork:
    """FHN神经网络模型"""
    
    def __init__(self, n_nodes, connectivity_matrix, epsilon=0.08, a=0.7, b=0.8):
        """
        参数:
            n_nodes: 节点数量
            connectivity_matrix: 连接矩阵 (N x N)
            epsilon: 时间尺度分离参数
            a, b: FHN模型参数
        """
        self.n_nodes = n_nodes
        self.C = connectivity_matrix
        self.epsilon = epsilon
        self.a = a
        self.b = b
        
    def dynamics(self, state, t, coupling_strength=0.1, external_input=None):
        """
        神经网络动力学方程
        
        dx/dt = (x - x^3/3 + y + I_ext + coupling) / epsilon
        dy/dt = a + b*x - y
        """
        x = state[:self.n_nodes]  # 快变量（膜电位）
        y = state[self.n_nodes:]  # 慢变量（恢复变量）
        
        # 耦合项：来自其他节点的影响
        coupling = coupling_strength * (self.C @ x - x * np.sum(self.C, axis=1))
        
        # 外部输入（听觉刺激）
        I_ext = external_input if external_input is not None else np.zeros(self.n_nodes)
        
        dxdt = (x - x**3/3 + y + I_ext + coupling) / self.epsilon
        dydt = self.a + self.b * x - y
        
        return np.concatenate([dxdt, dydt])
    
    def simulate(self, initial_state, t_span, coupling_strength=0.1, 
                 external_input_func=None, dt=0.1):
        """模拟网络动力学"""
        t = np.arange(t_span[0], t_span[1], dt)
        states = [initial_state]
        state = initial_state.copy()
        
        for i, ti in enumerate(t[:-1]):
            # 计算当前时刻的外部输入
            I_ext = external_input_func(ti) if external_input_func else None
            
            # RK4积分
            k1 = self.dynamics(state, ti, coupling_strength, I_ext)
            k2 = self.dynamics(state + 0.5*dt*k1, ti + 0.5*dt, coupling_strength, I_ext)
            k3 = self.dynamics(state + 0.5*dt*k2, ti + 0.5*dt, coupling_strength, I_ext)
            k4 = self.dynamics(state + dt*k3, ti + dt, coupling_strength, I_ext)
            state = state + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
            states.append(state)
        
        return t, np.array(states)


def generate_auditory_stimulus(t, frequency, amplitude, nodes_indices=None, n_nodes=10):
    """
    生成听觉刺激信号
    
    参数:
        t: 时间
        frequency: 刺激频率 (Hz)
        amplitude: 刺激振幅
        nodes_indices: 接受刺激的节点索引
        n_nodes: 总节点数
    """
    if nodes_indices is None:
        nodes_indices = [0]  # 默认刺激第一个节点
    
    stimulus = np.zeros(n_nodes)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    
    for idx in nodes_indices:
        stimulus[idx] = signal
    
    return stimulus


def compute_synchronization_index(states, n_nodes):
    """
    计算同步指数 (Kuramoto order parameter)
    
    同步指数衡量网络中神经元的相位同步程度
    """
    x = states[:, :n_nodes]
    
    # 提取相位（使用Hilbert变换）
    from scipy.signal import hilbert
    phases = np.zeros_like(x)
    for i in range(n_nodes):
        analytic = hilbert(x[:, i])
        phases[:, i] = np.unwrap(np.angle(analytic))
    
    # Kuramoto order parameter
    r = np.abs(np.mean(np.exp(1j * phases), axis=1))
    
    return r


def compute_gamma_coherence(states, n_nodes, fs=100.0):
    """
    计算Gamma频段相干性
    
    Gamma频段 (30-100 Hz) 对音乐处理至关重要
    """
    from scipy.signal import coherence
    
    x = states[:, :n_nodes]
    gamma_band = (30, 100)  # Hz
    
    coherence_matrix = np.zeros((n_nodes, n_nodes))
    
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            f, Cxy = coherence(x[:, i], x[:, j], fs=fs)
            # 提取Gamma频段的平均相干性
            gamma_idx = (f >= gamma_band[0]) & (f <= gamma_band[1])
            coherence_matrix[i, j] = np.mean(Cxy[gamma_idx])
            coherence_matrix[j, i] = coherence_matrix[i, j]
    
    return coherence_matrix
```

### 2. 经验脑连接数据集成

```python
import numpy as np

def load_empirical_connectivity(filepath):
    """
    加载经验脑连接数据
    
    支持格式：
    - DTI结构连接矩阵
    - fMRI功能连接矩阵
    """
    # 示例：从文件加载
    if filepath.endswith('.npy'):
        return np.load(filepath)
    elif filepath.endswith('.csv'):
        return np.loadtxt(filepath, delimiter=',')
    else:
        raise ValueError("不支持的文件格式")


def create_auditory_network_template(n_regions=68):
    """
    创建听觉网络模板
    
    基于Desikan-Killiany脑图谱
    """
    # 听觉相关区域
    auditory_regions = {
        'primary_auditory': [41, 42],  # Heschl's gyrus
        'secondary_auditory': [51, 52],  # superior temporal gyrus
        'associative': [81, 82],  # middle temporal gyrus
    }
    
    # 创建连接模板
    template = np.zeros((n_regions, n_regions))
    
    # 强化听觉区域之间的连接
    for region_id in auditory_regions.values():
        for i in region_id:
            for j in region_id:
                if i < n_regions and j < n_regions:
                    template[i, j] = 1.0
    
    return template, auditory_regions


def analyze_frequency_response(model, freq_range=(0.1, 50), n_freqs=50, 
                                 amplitude=1.0, t_span=(0, 100)):
    """
    分析网络对不同频率刺激的响应
    
    返回：
    - 频率-同步曲线
    - 最佳频率
    - 同步范围
    """
    frequencies = np.linspace(freq_range[0], freq_range[1], n_freqs)
    sync_indices = []
    
    for freq in frequencies:
        # 创建频率相关的刺激
        def stimulus(t):
            return generate_auditory_stimulus(t, freq, amplitude, n_nodes=model.n_nodes)
        
        # 模拟
        initial = np.random.randn(2 * model.n_nodes) * 0.1
        t, states = model.simulate(initial, t_span, external_input_func=stimulus)
        
        # 计算同步指数（取最后10%时间）
        sync = compute_synchronization_index(states[-int(len(states)*0.1):], model.n_nodes)
        sync_indices.append(np.mean(sync))
    
    sync_indices = np.array(sync_indices)
    
    # 找到最佳频率
    optimal_freq = frequencies[np.argmax(sync_indices)]
    
    # 计算同步范围（FWHM）
    half_max = np.max(sync_indices) / 2 + np.min(sync_indices) / 2
    above_half = sync_indices > half_max
    
    return {
        'frequencies': frequencies,
        'sync_indices': sync_indices,
        'optimal_frequency': optimal_freq,
        'max_sync': np.max(sync_indices),
        'sync_range': (frequencies[above_half][0], frequencies[above_half][-1]) if np.any(above_half) else None
    }
```

### 3. 相变与临界动力学分析

```python
def detect_phase_transitions(sync_timeseries, threshold=0.5, min_duration=10):
    """
    检测同步-去同步相变
    
    识别脑活动在同步和去同步状态之间的交替
    """
    binary_states = (sync_timeseries > threshold).astype(int)
    
    transitions = []
    current_state = binary_states[0]
    duration = 1
    
    for i in range(1, len(binary_states)):
        if binary_states[i] == current_state:
            duration += 1
        else:
            if duration >= min_duration:
                transitions.append({
                    'from_state': 'synchronized' if current_state == 1 else 'desynchronized',
                    'to_state': 'desynchronized' if current_state == 1 else 'synchronized',
                    'duration': duration,
                    'position': i - duration
                })
            current_state = binary_states[i]
            duration = 1
    
    return transitions


def compute_criticality_metrics(states, n_nodes):
    """
    计算临界动力学指标
    
    包括：
    - 变异系数
    - 幂律拟合
    - 雪崩大小分布
    """
    x = states[:, :n_nodes]
    
    # 变异系数
    cv = np.std(x) / np.mean(np.abs(x)) if np.mean(np.abs(x)) > 0 else 0
    
    # 检测雪崩（连续活动超过阈值）
    threshold = np.mean(np.abs(x)) + 2 * np.std(x)
    events = np.abs(x) > threshold
    
    # 计算雪崩大小
    avalanche_sizes = []
    current_size = 0
    for t in range(len(events)):
        if np.any(events[t]):
            current_size += np.sum(events[t])
        elif current_size > 0:
            avalanche_sizes.append(current_size)
            current_size = 0
    
    return {
        'coefficient_of_variation': cv,
        'avalanche_sizes': avalanche_sizes,
        'mean_avalanche_size': np.mean(avalanche_sizes) if avalanche_sizes else 0
    }
```

## 应用场景

### 1. 音乐认知研究
- 分析不同类型音乐对大脑同步的影响
- 研究音乐训练对神经网络的塑形作用

### 2. 神经调控
- 设计最优听觉刺激参数（频率、振幅）
- 预测刺激效果

### 3. 临床应用
- 音乐治疗参数优化
- 听觉障碍诊断

## Activation Keywords
- 音乐感知
- 脑网络
- 听觉刺激
- 神经同步
- FitzHugh-Nagumo
- gamma同步
- music perception
- brain network
- auditory stimulus
- 相位动力学
- 频率响应

## Tools Used
- numpy
- scipy

## Instructions for Agents
1. 理解FHN模型：简化的神经元兴奋性模型
2. 创建听觉刺激：生成频率和振幅可控的正弦信号
3. 计算同步指数：Kuramoto序参量
4. 分析频率响应：不同频率刺激下的网络响应
5. 注意Gamma频段（30-100 Hz）对音乐处理的重要性

## Examples
```python
# 使用示例
from music_perception_brain_network import FitzHughNagumoNetwork, generate_auditory_stimulus

# 1. 创建网络
network = FitzHughNagumoNetwork(
    n_nodes=10,
    connectivity_matrix=connectivity,
    epsilon=0.08
)

# 2. 生成听觉刺激
def stimulus(t):
    return generate_auditory_stimulus(t, frequency=10.0, amplitude=1.0, n_nodes=10)

# 3. 模拟
initial_state = np.random.randn(20) * 0.1
t, states = network.simulate(initial_state, (0, 100), external_input_func=stimulus)

# 4. 计算同步指数
sync_index = compute_synchronization_index(states, n_nodes=10)
print(f"平均同步指数: {sync_index.mean():.4f}")
```

## 参考文献

- Sawicki, J. et al. (2025). "From empirical brain networks towards modeling music perception" arXiv:2504.07721