---
name: computational-taste-perception
description: 计算味觉感知方法论。混合神经元模型结合Hodgkin-Huxley生物物理保真度和Izhikevich脉冲神经元计算效率，模拟味觉传导通路。适用于味觉受体建模、脉冲神经网络、多尺度学习。触发词：味觉感知、脉冲神经网络、Hodgkin-Huxley、Izhikevich、味觉受体、STDP、taste perception、spiking neural network、gustatory。
user-invocable: true
---

# Computational Taste Perception - 计算味觉感知

## 核心思想

混合神经元模型结合 Hodgkin-Huxley 生物物理保真度和 Izhikevich 脉冲神经元计算效率，实现味觉传导通路的精确模拟。

**来源：** arXiv:2510.00010
**效用：** 1.0

---

## 方法论

### 1. 混合神经元模型

**两层架构：**
| 层级 | 模型 | 用途 |
|------|------|------|
| 受体细胞 | Hodgkin-Huxley | 生物物理保真度 |
| 网络层 | Izhikevich | 计算效率 |

### 2. 味觉受体建模

**模态特异性受体动力学：**
- **T1R/T2R** - 甜/苦味受体
- **ENaC** - 咸味通道
- **PKD** - 酸味通道

**GHK 驱动离子电流：**
```python
def ghk_current(V, ion_conc_in, ion_conc_out, permeability, z=1):
    """
    Goldman-Hodgkin-Katz 电流方程
    
    Parameters:
    -----------
    V : float
        膜电位
    ion_conc_in/out : float
        膜内外离子浓度
    permeability : float
        离子通透性
    z : int
        离子价态
    
    Returns:
    --------
    I : float
        离子电流
    """
    F = 96485  # 法拉第常数
    R = 8.314  # 气体常数
    T = 310    # 温度 (K)
    
    # GHK 方程
    E = (R * T / (z * F)) * np.log(ion_conc_out / ion_conc_in)
    I = permeability * z**2 * (F**2 * V / (R * T)) * \
        (ion_conc_in - ion_conc_out * np.exp(-z * F * V / (R * T))) / \
        (1 - np.exp(-z * F * V / (R * T)))
    
    return I
```

### 3. 突触建模

**谷氨酸释放动力学：**
- Alpha 函数配置文件
- AMPA 受体贩运
- 磷酸化调节

**STDP 学习规则：**
```python
def stdp_update(w, delta_t, A_plus=0.1, A_minus=0.1, tau_plus=20, tau_minus=20):
    """
    Spike-Timing-Dependent Plasticity
    
    Parameters:
    -----------
    w : float
        当前突触权重
    delta_t : float
        突触前-后脉冲时间差 (ms)
    """
    if delta_t > 0:
        # LTP: 突触前先于突触后
        dw = A_plus * np.exp(-delta_t / tau_plus)
    else:
        # LTD: 突触后先于突触前
        dw = -A_minus * np.exp(delta_t / tau_minus)
    
    return w + dw
```

### 4. 多尺度学习

**两个维度：**
1. **时间脉冲同步** - van Rossum 指标
2. **组合群体编码** - 秩序模式

**van Rossum 距离：**
```python
def van_rossum_distance(spike_train1, spike_train2, tau=10):
    """
    计算两个脉冲序列的van Rossum距离
    """
    # 指数核滤波
    def filter_spikes(spikes, tau):
        t = np.linspace(0, 1000, 10000)
        filtered = np.zeros_like(t)
        for spike in spikes:
            filtered += np.exp(-(t - spike) / tau) * (t >= spike)
        return filtered
    
    f1 = filter_spikes(spike_train1, tau)
    f2 = filter_spikes(spike_train2, tau)
    
    distance = np.sqrt(np.trapz((f1 - f2)**2))
    return distance
```

---

## 实现框架

```python
import numpy as np

class HybridTasteNetwork:
    """混合味觉网络模型"""
    
    def __init__(self, n_receptors=50, n_neurons=200):
        self.n_receptors = n_receptors
        self.n_neurons = n_neurons
        
        # HH 受体模型参数
        self.receptor_params = {
            'T1R': {'g_Na': 120, 'g_K': 36, 'g_L': 0.3},
            'T2R': {'g_Na': 100, 'g_K': 40, 'g_L': 0.3},
            'ENaC': {'g_Na': 150, 'g_K': 30, 'g_L': 0.3},
            'PKD': {'g_Na': 80, 'g_K': 35, 'g_L': 0.3}
        }
        
        # Izhikevich 网络参数
        self.neuron_params = {
            'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8
        }
    
    def simulate_receptor(self, stimulus, receptor_type, dt=0.01):
        """HH 受体模拟"""
        params = self.receptor_params[receptor_type]
        # 简化的 HH 动力学
        V = -65  # 静息电位
        spikes = []
        
        for i, I in enumerate(stimulus):
            # HH 方程 (简化)
            dV = (params['g_Na'] * (V - 50) + params['g_K'] * (-77 - V) + 
                  params['g_L'] * (-54.4 - V) + I) * dt
            V += dV
            
            if V > 0:  # 阈值
                spikes.append(i * dt)
                V = params['c']
        
        return spikes
    
    def simulate_network(self, receptor_spikes, duration=1000):
        """Izhikevich 网络模拟"""
        a, b, c, d = self.neuron_params.values()
        
        v = np.ones(self.n_neurons) * c
        u = np.ones(self.n_neurons) * b * c
        
        # 突触权重矩阵
        W = np.random.rand(self.n_neurons, self.n_neurons) * 0.1
        
        network_spikes = [[] for _ in range(self.n_neurons)]
        
        for t in range(int(duration)):
            # 输入电流
            I = np.zeros(self.n_neurons)
            
            # 从受体接收输入
            for rs in receptor_spikes:
                if t in rs:
                    I += np.random.rand(self.n_neurons) * 10
            
            # Izhikevich 动力学
            fired = v >= 30
            v[fired] = c
            u[fired] += d
            
            dv = 0.04 * v**2 + 5 * v + 140 - u + I
            du = a * (b * v - u)
            
            v += dv
            u += du
            
            for n in np.where(fired)[0]:
                network_spikes[n].append(t)
        
        return network_spikes
```

---

## 应用场景

### 1. 味觉研究
- 味觉传导机制建模
- 受体动力学分析
- 味觉编码研究

### 2. 神经形态计算
- 混合神经元网络
- 多尺度学习
- STDP 实现

### 3. 仿生传感
- 电子舌设计
- 味觉传感器
- 食品质量检测

---

## 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| HH 时间步长 | 0.01 ms | 生物物理精度 |
| Izhikevich 时间步长 | 1 ms | 计算效率 |
| STDP tau | 20 ms | 可塑性窗口 |
| van Rossum tau | 10 ms | 脉冲距离 |

---

## 预期结果

1. **受体响应：** 模态特异性味觉受体脉冲
2. **网络同步：** 多尺度学习模式
3. **计算效率：** Izhikevich 比 HH 快 100x+

---

## 注意事项

- HH 模型计算成本高，用于受体层
- Izhikevich 模型高效，用于大规模网络
- STDP 参数影响学习收敛
- 需要验证生物保真度

---

## 参考文献

- arXiv:2510.00010 - Computational Advances in Taste Perception: From Ion Channels to Neural Coding