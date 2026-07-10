---
name: potassium-current-gain-control
description: A型钾电流介导的神经元增益控制机制。研究IA作为减法抑制与除法抑制之间的开关，通过动力学系统分析理解神经元如何自调节抑制效果。适用于计算神经科学、神经元建模、增益控制研究。触发词：A型钾电流、增益控制、抑制模式、IA电流、神经元增益、divisive inhibition、subtractive inhibition、gain control、potassium current。
user-invocable: true
---

# A型钾电流介导的神经元增益控制机制

**来源论文：** arXiv:1802.04794 - Gain control with A-type potassium current: IA as a switch between divisive and subtractive inhibition

## 核心方法论

基于动力学系统的神经元增益控制分析框架：

### 1. 两种抑制模式

**减法抑制 (Subtractive Inhibition)**
- 缩小引发脉冲活动的输入范围
- 消除对非偏好输入的响应
- 选择性过滤信息

**除法抑制 (Divisive Inhibition)**
- 形式上的增益控制
- 修改发放率但保留输入范围
- 保持信息编码宽度

### 2. A型钾电流 (IA) 的开关作用

```
IA 强 + 快 → 减法抑制
IA 弱/慢 → 除法抑制
```

**IA 特性：**
- 快速激活（类似脉冲启动时间尺度）
- 慢速失活
- 外向电流

### 3. 动力学系统分析

通过相平面分析定义脉冲阈值条件：
- 阈值依赖突触输入和 IA 状态
- 分岔分析确定发放模式

## Python 实现

```python
import numpy as np
from scipy.integrate import solve_ivp
from typing import Dict, Tuple, List, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class IAParameters:
    """A型钾电流参数"""
    g_A: float = 10.0          # IA 最大电导 (nS)
    E_A: float = -80.0         # IA 反转电位 (mV)
    tau_m_A: float = 1.0       # 激活时间常数 (ms)
    tau_h_A: float = 100.0     # 失活时间常数 (ms)
    
    # 激活/失活曲线参数
    V_half_m: float = -45.0    # 激活半电压
    k_m: float = 10.0          # 激活斜率
    V_half_h: float = -65.0    # 失活半电压
    k_h: float = -8.0          # 失活斜率


@dataclass
class NeuronParameters:
    """神经元参数"""
    C: float = 100.0           # 膜电容 (pF)
    g_L: float = 5.0           # 漏电导 (nS)
    E_L: float = -70.0         # 漏反转电位 (mV)
    g_Na: float = 1000.0       # Na 电导 (nS)
    g_K: float = 300.0         # K 电导 (nS)
    E_Na: float = 50.0         # Na 反转电位 (mV)
    E_K: float = -90.0         # K 反转电位 (mV)
    
    # 突触参数
    g_exc: float = 0.0         # 兴奋性输入电导
    g_inh: float = 0.0         # 抑制性输入电导
    E_exc: float = 0.0         # 兴奋性反转电位
    E_inh: float = -75.0       # 抑制性反转电位


class IAGainControlNeuron:
    """带 A型钾电流的增益控制神经元模型"""
    
    def __init__(self, ia_params: IAParameters = None, 
                 neuron_params: NeuronParameters = None):
        """
        Args:
            ia_params: IA 参数
            neuron_params: 神经元参数
        """
        self.ia_params = ia_params or IAParameters()
        self.neuron_params = neuron_params or NeuronParameters()
        
    def m_inf(self, V: float) -> float:
        """IA 激活稳态"""
        p = self.ia_params
        return 1.0 / (1.0 + np.exp(-(V - p.V_half_m) / p.k_m))
    
    def h_inf(self, V: float) -> float:
        """IA 失活稳态"""
        p = self.ia_params
        return 1.0 / (1.0 + np.exp(-(V - p.V_half_h) / p.k_h))
    
    def I_A(self, V: float, m: float, h: float) -> float:
        """A型钾电流"""
        p = self.ia_params
        return p.g_A * m**4 * h * (V - p.E_A)
    
    def I_L(self, V: float) -> float:
        """漏电流"""
        p = self.neuron_params
        return p.g_L * (V - p.E_L)
    
    def I_syn(self, V: float, g_exc: float, g_inh: float) -> float:
        """突触电流"""
        p = self.neuron_params
        I_exc = g_exc * (V - p.E_exc)
        I_inh = g_inh * (V - p.E_inh)
        return I_exc + I_inh
    
    def derivatives(self, t: float, state: np.ndarray,
                   g_exc: float = 0, g_inh: float = 0) -> np.ndarray:
        """计算状态导数
        
        state = [V, m, h]
        """
        V, m, h = state
        p_n = self.neuron_params
        p_a = self.ia_params
        
        # IA 电流
        I_A = self.I_A(V, m, h)
        
        # 漏电流
        I_L = self.I_L(V)
        
        # 突触电流
        I_syn = self.I_syn(V, g_exc, g_inh)
        
        # 电压导数
        dV = -(I_A + I_L + I_syn) / p_n.C
        
        # 门控变量导数
        dm = (self.m_inf(V) - m) / p_a.tau_m_A
        dh = (self.h_inf(V) - h) / p_a.tau_h_A
        
        return np.array([dV, dm, dh])
    
    def simulate(self, T: float, dt: float = 0.01,
                 g_exc_func=None, g_inh_func=None,
                 V0: float = -70.0) -> Dict:
        """模拟神经元响应
        
        Args:
            T: 模拟时长 (ms)
            dt: 时间步长 (ms)
            g_exc_func: 兴奋性输入函数 (t -> g_exc)
            g_inh_func: 抑制性输入函数 (t -> g_inh)
            V0: 初始电压
            
        Returns:
            results: 模拟结果字典
        """
        # 默认输入函数
        if g_exc_func is None:
            g_exc_func = lambda t: 0
        if g_inh_func is None:
            g_inh_func = lambda t: 0
            
        # 初始状态
        m0 = self.m_inf(V0)
        h0 = self.h_inf(V0)
        state0 = np.array([V0, m0, h0])
        
        # 时间点
        t_span = (0, T)
        t_eval = np.arange(0, T, dt)
        
        # 定义 ODE 函数
        def ode_func(t, y):
            g_exc = g_exc_func(t)
            g_inh = g_inh_func(t)
            return self.derivatives(t, y, g_exc, g_inh)
        
        # 求解
        sol = solve_ivp(ode_func, t_span, state0, 
                       t_eval=t_eval, method='RK45')
        
        return {
            't': sol.t,
            'V': sol.y[0],
            'm': sol.y[1],
            'h': sol.y[2],
            'I_A': self.I_A(sol.y[0], sol.y[1], sol.y[2])
        }
    
    def compute_firing_rate(self, g_exc_range: np.ndarray,
                           g_inh: float = 0,
                           T: float = 1000.0) -> np.ndarray:
        """计算不同兴奋性输入下的发放率
        
        Args:
            g_exc_range: 兴奋性电导范围
            g_inh: 抑制性电导
            T: 模拟时长
            
        Returns:
            firing_rates: 发放率数组
        """
        firing_rates = np.zeros_like(g_exc_range)
        
        for i, g_exc in enumerate(g_exc_range):
            # 恒定输入
            results = self.simulate(T, g_exc_func=lambda t: g_exc,
                                   g_inh_func=lambda t: g_inh)
            
            # 检测脉冲（简化：电压超过 -20 mV）
            spikes = np.diff(results['V'] > -20)
            spike_times = results['t'][:-1][spikes > 0]
            
            # 发放率
            firing_rates[i] = len(spike_times) / (T / 1000)  # Hz
            
        return firing_rates
    
    def analyze_inhibition_mode(self, g_exc_range: np.ndarray,
                                g_inh_values: np.ndarray) -> Dict:
        """分析抑制模式
        
        Args:
            g_exc_range: 兴奋性电导范围
            g_inh_values: 抑制性电导值数组
            
        Returns:
            analysis: 分析结果
        """
        # 基线（无抑制）发放率
        baseline_rate = self.compute_firing_rate(g_exc_range, g_inh=0)
        
        results = {
            'g_exc': g_exc_range,
            'baseline_rate': baseline_rate,
            'inhibition_data': []
        }
        
        for g_inh in g_inh_values:
            rate = self.compute_firing_rate(g_exc_range, g_inh=g_inh)
            
            # 计算抑制模式指标
            # 减法抑制：f-I 曲线水平位移
            # 除法抑制：f-I 曲线斜率降低
            
            # 简化分析：比较峰值发放率和阈值变化
            threshold_shift = self._estimate_threshold_shift(
                baseline_rate, rate, g_exc_range
            )
            gain_reduction = self._estimate_gain_reduction(
                baseline_rate, rate, g_exc_range
            )
            
            results['inhibition_data'].append({
                'g_inh': g_inh,
                'rate': rate,
                'threshold_shift': threshold_shift,
                'gain_reduction': gain_reduction,
                'mode': 'subtractive' if threshold_shift > gain_reduction else 'divisive'
            })
            
        return results
    
    def _estimate_threshold_shift(self, baseline: np.ndarray,
                                   inhibited: np.ndarray,
                                   g_exc: np.ndarray) -> float:
        """估计阈值位移"""
        # 找到基线中第一个非零发放率的位置
        baseline_threshold = None
        for i, r in enumerate(baseline):
            if r > 0.5:  # 阈值：0.5 Hz
                baseline_threshold = g_exc[i]
                break
                
        # 找到抑制后的阈值
        inh_threshold = None
        for i, r in enumerate(inhibited):
            if r > 0.5:
                inh_threshold = g_exc[i]
                break
                
        if baseline_threshold is None or inh_threshold is None:
            return 0
            
        return inh_threshold - baseline_threshold
    
    def _estimate_gain_reduction(self, baseline: np.ndarray,
                                  inhibited: np.ndarray,
                                  g_exc: np.ndarray) -> float:
        """估计增益降低"""
        # 计算线性区域的斜率
        # 找到发放率在 10-50 Hz 范围内的数据点
        
        mask_baseline = (baseline > 10) & (baseline < 50)
        mask_inhibited = (inhibited > 10) & (inhibited < 50)
        
        if not np.any(mask_baseline) or not np.any(mask_inhibited):
            return 0
            
        # 简单线性拟合
        try:
            slope_baseline = np.polyfit(
                g_exc[mask_baseline], baseline[mask_baseline], 1
            )[0]
            slope_inhibited = np.polyfit(
                g_exc[mask_inhibited], inhibited[mask_inhibited], 1
            )[0]
            
            return 1 - slope_inhibited / slope_baseline
        except:
            return 0


def compare_ia_strengths(g_exc_range: np.ndarray,
                        g_A_values: List[float]) -> Dict:
    """比较不同 IA 强度下的抑制模式
    
    Args:
        g_exc_range: 兴奋性电导范围
        g_A_values: IA 电导值列表
        
    Returns:
        comparison: 比较结果
    """
    results = {
        'g_exc': g_exc_range,
        'ia_data': []
    }
    
    for g_A in g_A_values:
        # 创建不同 IA 强度的神经元
        ia_params = IAParameters(g_A=g_A)
        neuron = IAGainControlNeuron(ia_params=ia_params)
        
        # 分析抑制模式
        g_inh_values = np.array([0, 5, 10, 15])
        analysis = neuron.analyze_inhibition_mode(g_exc_range, g_inh_values)
        
        results['ia_data'].append({
            'g_A': g_A,
            'analysis': analysis
        })
        
    return results


def visualize_gain_control(g_exc_range: np.ndarray,
                          g_inh_values: np.ndarray,
                          g_A_strong: float = 15.0,
                          g_A_weak: float = 5.0):
    """可视化增益控制模式
    
    Args:
        g_exc_range: 兴奋性电导范围
        g_inh_values: 抑制性电导值
        g_A_strong: 强 IA 电导
        g_A_weak: 弱 IA 电导
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 强 IA（减法抑制）
    ia_strong = IAParameters(g_A=g_A_strong)
    neuron_strong = IAGainControlNeuron(ia_params=ia_strong)
    
    ax = axes[0, 0]
    for g_inh in g_inh_values:
        rate = neuron_strong.compute_firing_rate(g_exc_range, g_inh=g_inh)
        ax.plot(g_exc_range, rate, label=f'g_inh = {g_inh}')
    ax.set_xlabel('Excitatory Conductance (nS)')
    ax.set_ylabel('Firing Rate (Hz)')
    ax.set_title(f'Strong IA (g_A = {g_A_strong} nS)\nSubtractive Inhibition')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 弱 IA（除法抑制）
    ia_weak = IAParameters(g_A=g_A_weak)
    neuron_weak = IAGainControlNeuron(ia_params=ia_weak)
    
    ax = axes[0, 1]
    for g_inh in g_inh_values:
        rate = neuron_weak.compute_firing_rate(g_exc_range, g_inh=g_inh)
        ax.plot(g_exc_range, rate, label=f'g_inh = {g_inh}')
    ax.set_xlabel('Excitatory Conductance (nS)')
    ax.set_ylabel('Firing Rate (Hz)')
    ax.set_title(f'Weak IA (g_A = {g_A_weak} nS)\nDivisive Inhibition')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # IA 门控变量
    V_range = np.linspace(-80, -30, 100)
    neuron = IAGainControlNeuron()
    
    ax = axes[1, 0]
    ax.plot(V_range, [neuron.m_inf(v) for v in V_range], 
            label='m∞ (activation)', linewidth=2)
    ax.plot(V_range, [neuron.h_inf(v) for v in V_range], 
            label='h∞ (inactivation)', linewidth=2)
    ax.axvline(x=ia_strong.V_half_m, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Membrane Potential (mV)')
    ax.set_ylabel('Gating Variable')
    ax.set_title('IA Gating Curves')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 模式切换示意
    ax = axes[1, 1]
    g_A_values = np.linspace(0, 30, 20)
    modes = []
    for g_A in g_A_values:
        ia_params = IAParameters(g_A=g_A)
        neuron = IAGainControlNeuron(ia_params=ia_params)
        analysis = neuron.analyze_inhibition_mode(
            np.linspace(0, 30, 10), np.array([10])
        )
        mode = analysis['inhibition_data'][0]['mode']
        modes.append(1 if mode == 'subtractive' else 0)
    
    ax.plot(g_A_values, modes, 'o-', markersize=8)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Divisive', 'Subtractive'])
    ax.set_xlabel('IA Conductance (nS)')
    ax.set_ylabel('Inhibition Mode')
    ax.set_title('Mode Switching by IA Strength')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('ia_gain_control.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'ia_gain_control.png'


# 使用示例
def example_gain_control():
    """示例：增益控制分析"""
    print("="*60)
    print("A型钾电流增益控制分析")
    print("="*60)
    
    # 兴奋性电导范围
    g_exc_range = np.linspace(0, 30, 30)
    
    # 抑制性电导值
    g_inh_values = np.array([0, 5, 10, 15])
    
    # 比较 IA 强度
    print("\n比较不同 IA 强度下的抑制模式：")
    print("-"*40)
    
    # 强 IA
    print("\n强 IA (g_A = 15 nS):")
    neuron_strong = IAGainControlNeuron(ia_params=IAParameters(g_A=15.0))
    analysis_strong = neuron_strong.analyze_inhibition_mode(
        g_exc_range, np.array([10])
    )
    for data in analysis_strong['inhibition_data']:
        if data['g_inh'] > 0:
            print(f"  g_inh = {data['g_inh']}: {data['mode']} inhibition")
    
    # 弱 IA
    print("\n弱 IA (g_A = 5 nS):")
    neuron_weak = IAGainControlNeuron(ia_params=IAParameters(g_A=5.0))
    analysis_weak = neuron_weak.analyze_inhibition_mode(
        g_exc_range, np.array([10])
    )
    for data in analysis_weak['inhibition_data']:
        if data['g_inh'] > 0:
            print(f"  g_inh = {data['g_inh']}: {data['mode']} inhibition")
    
    # 可视化
    print("\n生成可视化图表...")
    img_path = visualize_gain_control(g_exc_range, g_inh_values)
    print(f"图表已保存: {img_path}")
    
    return analysis_strong, analysis_weak


def example_dynamic_simulation():
    """示例：动态响应模拟"""
    print("\n" + "="*60)
    print("动态响应模拟")
    print("="*60)
    
    # 创建神经元
    neuron = IAGainControlNeuron(ia_params=IAParameters(g_A=10.0))
    
    # 定义输入：阶跃输入
    def g_exc_func(t):
        if t < 200:
            return 0
        elif t < 600:
            return 15
        else:
            return 25
    
    def g_inh_func(t):
        if t < 400:
            return 0
        else:
            return 8
    
    # 模拟
    results = neuron.simulate(1000, g_exc_func=g_exc_func, g_inh_func=g_inh_func)
    
    print(f"\n模拟时长: 1000 ms")
    print(f"峰值电压: {results['V'].max():.2f} mV")
    print(f"平均 IA 电流: {results['I_A'].mean():.2f} pA")
    
    # 检测脉冲
    spikes = np.diff(results['V'] > -20)
    spike_times = results['t'][:-1][spikes > 0]
    print(f"脉冲数量: {len(spike_times)}")
    
    return results


## Activation Keywords
- A型钾电流
- 增益控制
- 抑制模式
- IA电流
- 神经元增益
- divisive inhibition
- subtractive inhibition
- gain control
- potassium current
- A-type current

## Tools Used
- numpy
- scipy
- matplotlib

## Instructions for Agents
1. 理解两种抑制模式：减法抑制缩小输入范围，除法抑制降低增益
2. 分析 IA 作为开关的机制：强/快 IA → 减法抑制，弱/慢 IA → 除法抑制
3. 使用动力学系统方法分析脉冲阈值条件
4. 模拟不同 IA 参数下的神经元响应
5. 计算 f-I 曲线分析抑制模式

## Examples
```python
# 增益控制分析示例
from potassium_current_gain_control import IAGainControlNeuron, IAParameters

# 1. 创建带强 IA 的神经元（减法抑制）
neuron_subtractive = IAGainControlNeuron(
    ia_params=IAParameters(g_A=15.0)  # 强 IA
)

# 2. 创建带弱 IA 的神经元（除法抑制）
neuron_divisive = IAGainControlNeuron(
    ia_params=IAParameters(g_A=5.0)  # 弱 IA
)

# 3. 计算发放率曲线
g_exc = np.linspace(0, 30, 30)
rate_sub = neuron_subtractive.compute_firing_rate(g_exc, g_inh=10)
rate_div = neuron_divisive.compute_firing_rate(g_exc, g_inh=10)

# 4. 分析抑制模式
analysis = neuron_subtractive.analyze_inhibition_mode(
    g_exc, np.array([0, 5, 10, 15])
)
for data in analysis['inhibition_data']:
    print(f"g_inh={data['g_inh']}: {data['mode']}")
```

if __name__ == "__main__":
    example_gain_control()
    example_dynamic_simulation()
```

## Related Skills

- `heterogeneous-synaptic-dynamics` - 异质性突触动力学
- `neuromodulated-synaptic-plasticity` - 神经调制突触可塑性
- `bio-neuron-snn-learning` - 生物神经元SNN学习

## References

- arXiv:1802.04794 - Gain control with A-type potassium current
- PLOS Computational Biology: 10.1371/journal.pcbi.1006292
- Topics: Neurons and Cognition (q-bio.NC)