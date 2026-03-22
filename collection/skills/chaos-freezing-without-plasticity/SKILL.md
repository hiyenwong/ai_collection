---
name: chaos-freezing-without-plasticity
description: 无突触可塑性的混沌冻结方法论。引入Onsager反应项使神经网络动力学稳定化，不依赖Hebbian学习即可抑制混沌波动。适用于RNN稳定性分析、神经动力学控制。触发词：混沌冻结、Onsager反应、神经网络稳定性、混沌抑制、RNN动力学、chaos freezing、Onsager reaction、gradient dynamics。
user-invocable: true
---

# 无突触可塑性的混沌冻结

基于 arXiv:2503.08069 - "Freezing chaos without synaptic plasticity" (Phys. Rev. E 112, 044227, 2025)

## 核心方法论

### 1. Onsager反应项机制

传统RNN动力学：
```
dx/dt = -x + W·φ(x) + I_ext
```

引入Onsager反应项后：
```
dx/dt = -x + W·φ(x) - η·(∂H/∂x) + I_ext
```

其中 η·(∂H/∂x) 是Onsager反应项，使系统趋向梯度动力学。

```python
import numpy as np
from scipy.integrate import odeint

class ChaosFreezingRNN:
    """
    带Onsager反应项的RNN，实现混沌冻结
    """
    
    def __init__(self, n_neurons, connectivity=0.1, g=1.5, eta=0.1):
        """
        参数:
            n_neurons: 神经元数量
            connectivity: 连接稀疏度
            g: 耦合强度（g > 1 时产生混沌）
            eta: Onsager反应强度
        """
        self.N = n_neurons
        self.g = g
        self.eta = eta
        
        # 初始化随机权重矩阵
        self.W = np.random.randn(n_neurons, n_neurons) * g / np.sqrt(connectivity * n_neurons)
        self.W *= np.random.rand(n_neurons, n_neurons) < connectivity
    
    def phi(self, x, method='tanh'):
        """激活函数"""
        if method == 'tanh':
            return np.tanh(x)
        elif method == 'relu':
            return np.maximum(0, x)
        elif method == 'sigmoid':
            return 1 / (1 + np.exp(-x))
    
    def hamiltonian(self, x):
        """
        系统的哈密顿量/能量函数
        
        H = 0.5 * x^T · x - ∫φ(x) dx
        """
        # 简化形式
        return 0.5 * np.sum(x**2) - np.sum(np.log(np.cosh(x)))  # for tanh
    
    def onager_reaction(self, x):
        """
        Onsager反应项
        
        反馈神经元自身的活动，使驱动项成为梯度形式
        """
        # 自反馈项
        self_feedback = self.phi(x) - x
        
        # 与权重的耦合
        reaction = -self.eta * self_feedback
        
        return reaction
    
    def dynamics_vanilla(self, x, t):
        """标准RNN动力学（可能混沌）"""
        return -x + self.W @ self.phi(x)
    
    def dynamics_with_onsager(self, x, t):
        """带Onsager反应项的动力学（混沌冻结）"""
        return -x + self.W @ self.phi(x) + self.onager_reaction(x)
    
    def dynamics_gradient(self, x, t):
        """
        纯梯度动力学
        
        当Onsager项足够强时，系统趋近此形式
        """
        # 梯度 = -∂H/∂x
        return -x + self.phi(x)
    
    def simulate(self, initial_state, t_span, dt=0.1, use_onsager=True):
        """模拟网络动力学"""
        t = np.arange(t_span[0], t_span[1], dt)
        
        if use_onsager:
            dynamics = self.dynamics_with_onsager
        else:
            dynamics = self.dynamics_vanilla
        
        # RK4积分
        states = [initial_state.copy()]
        x = initial_state.copy()
        
        for ti in t[:-1]:
            k1 = dynamics(x, ti)
            k2 = dynamics(x + 0.5*dt*k1, ti + 0.5*dt)
            k3 = dynamics(x + 0.5*dt*k2, ti + 0.5*dt)
            k4 = dynamics(x + dt*k3, ti + dt)
            x = x + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
            states.append(x.copy())
        
        return t, np.array(states)


def compute_lyapunov_exponent(states, rnn, dt=0.1, n_exponents=10):
    """
    计算Lyapunov指数
    
    正的最大Lyapunov指数表示混沌
    """
    N = rnn.N
    T = len(states)
    
    # 初始化切向量
    Q = np.eye(N)[:, :min(n_exponents, N)]
    
    lyapunov_sums = np.zeros(min(n_exponents, N))
    
    for t_idx in range(1, T):
        x = states[t_idx]
        
        # Jacobian矩阵
        J = -np.eye(N) + rnn.W * (1 - np.tanh(x)**2)  # for tanh
        
        # 添加Onsager项的Jacobian贡献
        J -= rnn.eta * (1 - np.tanh(x)**2) * np.eye(N)
        
        # QR分解
        Q = J @ Q
        Q, R = np.linalg.qr(Q)
        
        # 累积Lyapunov指数
        lyapunov_sums += np.log(np.abs(np.diag(R[:min(n_exponents, N), :min(n_exponents, N)])))
    
    lyapunov_exponents = lyapunov_sums / (T * dt)
    
    return lyapunov_exponents


def freeze_chaos_trajectory(rnn, initial_state, t_span=(0, 100), 
                            eta_schedule=None, dt=0.1):
    """
    通过逐渐增加Onsager反应强度来冻结混沌轨迹
    
    参数:
        eta_schedule: η的调度函数，从混沌区逐渐过渡到冻结区
    """
    if eta_schedule is None:
        # 默认调度：从0逐渐增加到冻结所需强度
        eta_schedule = lambda t: min(t / 50.0, 1.0)
    
    t = np.arange(t_span[0], t_span[1], dt)
    states = [initial_state.copy()]
    x = initial_state.copy()
    
    for ti in t[:-1]:
        # 更新η
        rnn.eta = eta_schedule(ti)
        
        # 动力学
        dynamics = lambda x, t: -x + rnn.W @ rnn.phi(x) - rnn.eta * (rnn.phi(x) - x)
        
        # RK4
        k1 = dynamics(x, ti)
        k2 = dynamics(x + 0.5*dt*k1, ti + 0.5*dt)
        k3 = dynamics(x + 0.5*dt*k2, ti + 0.5*dt)
        k4 = dynamics(x + dt*k3, ti + dt)
        x = x + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
        states.append(x.copy())
    
    return t, np.array(states)
```

### 2. E-I网络扩展

```python
class EINetwork:
    """
    兴奋性-抑制性网络
    
    更符合生物学的网络结构
    """
    
    def __init__(self, n_exc, n_inh, connectivity=0.1, g=1.5, eta=0.1):
        """
        参数:
            n_exc: 兴奋性神经元数量
            n_inh: 抑制性神经元数量
        """
        self.N_e = n_exc
        self.N_i = n_inh
        self.N = n_exc + n_inh
        self.g = g
        self.eta = eta
        
        # 权重矩阵：E→E, E→I, I→E, I→I
        # Dale定律：E神经元输出为正，I神经元输出为负
        W_ee = np.random.randn(n_exc, n_exc) * g / np.sqrt(connectivity * n_exc)
        W_ei = np.random.randn(n_inh, n_exc) * g / np.sqrt(connectivity * n_exc)
        W_ie = np.random.randn(n_exc, n_inh) * g / np.sqrt(connectivity * n_inh)
        W_ii = np.random.randn(n_inh, n_inh) * g / np.sqrt(connectivity * n_inh)
        
        # 应用稀疏性和Dale定律
        mask_ee = np.random.rand(n_exc, n_exc) < connectivity
        mask_ei = np.random.rand(n_inh, n_exc) < connectivity
        mask_ie = np.random.rand(n_exc, n_inh) < connectivity
        mask_ii = np.random.rand(n_inh, n_inh) < connectivity
        
        self.W = np.zeros((self.N, self.N))
        self.W[:n_exc, :n_exc] = W_ee * mask_ee  # E→E (兴奋)
        self.W[n_exc:, :n_exc] = W_ei * mask_ei  # E→I (兴奋)
        self.W[:n_exc, n_exc:] = -np.abs(W_ie * mask_ie)  # I→E (抑制)
        self.W[n_exc:, n_exc:] = -np.abs(W_ii * mask_ii)  # I→I (抑制)
    
    def dynamics_with_onsager(self, x, t, tau_e=1.0, tau_i=2.0):
        """
        E-I网络动力学
        
        tau_e, tau_i: 兴奋性和抑制性神经元的时间常数
        """
        # 分离E和I神经元
        x_e = x[:self.N_e]
        x_i = x[self.N_e:]
        
        # 激活函数
        phi_e = np.tanh(x_e)
        phi_i = np.tanh(x_i)
        phi = np.concatenate([phi_e, phi_i])
        
        # 网络输入
        network_input = self.W @ phi
        
        # Onsager反应项
        onsager_e = -self.eta * (phi_e - x_e)
        onsager_i = -self.eta * (phi_i - x_i)
        
        # 动力学
        dx_e = (-x_e + network_input[:self.N_e] + onsager_e) / tau_e
        dx_i = (-x_i + network_input[self.N_e:] + onsager_i) / tau_i
        
        return np.concatenate([dx_e, dx_i])
    
    def find_fixed_points(self, n_attempts=10, max_iter=1000, tol=1e-6):
        """寻找不动点"""
        fixed_points = []
        
        for _ in range(n_attempts):
            # 随机初始化
            x = np.random.randn(self.N) * 0.1
            
            # 梯度下降
            for _ in range(max_iter):
                dx = self.dynamics_with_onsager(x, 0)
                x = x + 0.1 * dx
                
                if np.linalg.norm(dx) < tol:
                    fixed_points.append(x.copy())
                    break
        
        return fixed_points


def approach_fixed_point(rnn, initial_state, target_fixed_point, dt=0.1, max_t=100):
    """
    通过降低动能逼近不动点
    
    方法：逐步减小η，让系统沿梯度方向移动
    """
    trajectory = [initial_state.copy()]
    x = initial_state.copy()
    
    for t in np.arange(0, max_t, dt):
        # 计算到不动点的距离
        distance = np.linalg.norm(x - target_fixed_point)
        
        if distance < 0.01:
            break
        
        # 动能衰减
        rnn.eta = 1.0 + 0.5 * distance  # 自适应η
        
        # 动力学
        dynamics = lambda x, t: -x + rnn.W @ rnn.phi(x) - rnn.eta * (rnn.phi(x) - x)
        
        # RK4
        k1 = dynamics(x, t)
        k2 = dynamics(x + 0.5*dt*k1, t + 0.5*dt)
        k3 = dynamics(x + 0.5*dt*k2, t + 0.5*dt)
        k4 = dynamics(x + dt*k3, t + dt)
        x = x + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
        trajectory.append(x.copy())
    
    return np.array(trajectory)
```

### 3. 记忆与预测任务

```python
def recall_task(rnn, pattern, t_recall=50, noise_level=0.1):
    """
    记忆回忆任务
    
    测试冻结动力学是否能恢复存储的模式
    """
    # 从含噪版本开始
    noisy_pattern = pattern + noise_level * np.random.randn(len(pattern))
    
    # 冻结轨迹
    t, states = rnn.simulate(noisy_pattern, (0, t_recall), use_onsager=True)
    
    # 计算恢复精度
    final_state = states[-1]
    recall_accuracy = np.corrcoef(pattern, final_state)[0, 1]
    
    return recall_accuracy, states


def prediction_task(rnn, time_series, prediction_horizon=10, dt=0.1):
    """
    时间序列预测任务
    
    测试梯度动力学对时序刺激的响应
    """
    n_steps = len(time_series)
    predictions = []
    errors = []
    
    x = np.zeros(rnn.N)
    
    for t_idx in range(n_steps - prediction_horizon):
        # 输入当前值
        rnn.input = time_series[t_idx]
        
        # 模拟一步
        t, states = rnn.simulate(x, (0, prediction_horizon * dt), use_onsager=True)
        
        # 预测
        pred = states[-1, 0]  # 假设第一个神经元输出预测值
        predictions.append(pred)
        
        # 真实值
        true_value = time_series[t_idx + prediction_horizon]
        errors.append(np.abs(pred - true_value))
        
        # 更新状态
        x = states[-1]
    
    return predictions, errors
```

## 应用场景

### 1. RNN稳定性分析
- 分析混沌与稳定边界
- 设计稳定性参数

### 2. 神经动力学建模
- 不依赖可塑性的记忆机制
- 吸引子网络设计

### 3. 神经计算
- 混沌计算与冻结计算
- 时序信息处理

## 参考文献

- Huang, H. (2025). "Freezing chaos without synaptic plasticity" Phys. Rev. E 112, 044227, arXiv:2503.08069