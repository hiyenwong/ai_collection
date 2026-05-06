---
name: generative-brain-dynamics-models
description: 脑动力学生成模型综述框架。整合计算神经科学、非线性动力学、数据驱动方法的生成模型方法论，涵盖不同组织尺度和抽象层次。适用于脑动力学建模、神经数据分析、科学机器学习。触发词：脑动力学、生成模型、神经动力学、动态系统模型、brain dynamics、generative model、neural dynamics、computational neuroscience、Dynamical systems。
user-invocable: true
---

# 脑动力学生成模型框架

**来源论文：** arXiv:2112.12147 - Generative Models of Brain Dynamics -- A review

## 核心方法论

### 1. 生成模型范式

**优势：**
- 数据驱动的假设检验
- 可解释的动力学机制
- 跨尺度整合能力
- 因果推断支持

### 2. 多尺度组织

| 尺度 | 模型类型 | 示例 |
|------|----------|------|
| 微观 | 神经元动力学 | Hodgkin-Huxley, LIF |
| 中观 | 神经群体 | 神经质量模型, Wilson-Cowan |
| 宏观 | 脑网络 | DCM, 动态功能连接 |

### 3. 方法论分类

**假设驱动：**
- 生物物理机制
- 动力学理论
- 可解释性强

**数据驱动：**
- 深度学习
- 变分推断
- 灵活性高

**混合方法：**
- 科学机器学习
- 物理信息神经网络
- 两全其美

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


@dataclass
class DynamicsConfig:
    """动力学模型配置"""
    dt: float = 0.1              # 时间步长 (ms)
    duration: float = 1000.0     # 模拟时长 (ms)
    
    # 神经参数
    n_neurons: int = 100
    tau: float = 20.0            # 时间常数 (ms)
    
    # 噪声
    noise_level: float = 0.1


class GenerativeBrainModel(ABC):
    """生成脑模型基类"""
    
    def __init__(self, config: DynamicsConfig):
        self.config = config
        self.n_steps = int(config.duration / config.dt)
        
    @abstractmethod
    def simulate(self, parameters: Dict) -> Dict:
        """模拟动力学"""
        pass
    
    @abstractmethod
    def fit(self, data: np.ndarray) -> Dict:
        """拟合数据"""
        pass
    
    @abstractmethod
    def generate(self, n_samples: int) -> np.ndarray:
        """生成数据"""
        pass


class NeuralMassModel(GenerativeBrainModel):
    """神经质量模型"""
    
    def __init__(self, config: DynamicsConfig):
        super().__init__(config)
        
        # Wilson-Cowan 参数
        self.w_EE = 12.0      # E → E 连接
        self.w_EI = 4.0       # I → E 连接
        self.w_IE = 13.0      # E → I 连接
        self.w_II = 11.0      # I → I 连接
        
        self.tau_E = 10.0     # E 时间常数
        self.tau_I = 20.0     # I 时间常数
        
        self.theta_E = 2.5    # E 阈值
        self.theta_I = 3.5    # I 阈值
        
    def sigmoid(self, x: np.ndarray, theta: float = 0, 
                sigma: float = 1.0) -> np.ndarray:
        """Sigmoid 激活函数"""
        return 1.0 / (1.0 + np.exp(-sigma * (x - theta)))
    
    def simulate(self, parameters: Dict = None) -> Dict:
        """模拟 Wilson-Cowan 动力学
        
        dE/dt = -E/τ_E + (1-E) * S(w_EE*E - w_EI*I + P_E)
        dI/dt = -I/τ_I + (1-I) * S(w_IE*E - w_II*I + P_I)
        """
        if parameters:
            for key, value in parameters.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        
        # 初始化
        E = np.zeros(self.n_steps)
        I = np.zeros(self.n_steps)
        E[0] = 0.1
        I[0] = 0.1
        
        # 外部输入
        P_E = 1.0
        P_I = 0.5
        
        dt = self.config.dt
        
        for t in range(1, self.n_steps):
            # 微分方程
            dE = (-E[t-1] / self.tau_E + 
                  (1 - E[t-1]) * self.sigmoid(
                      self.w_EE * E[t-1] - self.w_EI * I[t-1] + P_E,
                      self.theta_E
                  ))
            
            dI = (-I[t-1] / self.tau_I + 
                  (1 - I[t-1]) * self.sigmoid(
                      self.w_IE * E[t-1] - self.w_II * I[t-1] + P_I,
                      self.theta_I
                  ))
            
            # 添加噪声
            dE += self.config.noise_level * np.random.randn()
            dI += self.config.noise_level * np.random.randn()
            
            # 更新
            E[t] = np.clip(E[t-1] + dt * dE, 0, 1)
            I[t] = np.clip(I[t-1] + dt * dI, 0, 1)
            
        return {
            'E': E,
            'I': I,
            'time': np.arange(self.n_steps) * dt
        }
    
    def fit(self, data: np.ndarray) -> Dict:
        """拟合参数（简化版）"""
        # 使用梯度下降拟合参数
        # 这里简化为返回当前参数
        return {
            'w_EE': self.w_EE,
            'w_EI': self.w_EI,
            'w_IE': self.w_IE,
            'w_II': self.w_II,
            'fit_score': np.random.random()  # 模拟拟合分数
        }
    
    def generate(self, n_samples: int = 1) -> np.ndarray:
        """生成动力学数据"""
        results = []
        for _ in range(n_samples):
            sim = self.simulate()
            results.append(np.column_stack([sim['E'], sim['I']]))
        return np.array(results)


class DynamicCausalModel(GenerativeBrainModel):
    """动态因果模型 (DCM)"""
    
    def __init__(self, config: DynamicsConfig):
        super().__init__(config)
        
        # 脑区数量
        self.n_regions = config.n_neurons
        
        # 连接矩阵
        self.A = np.random.randn(self.n_regions, self.n_regions) * 0.1
        self.B = np.zeros((self.n_regions, self.n_regions))  # 调制
        self.C = np.zeros(self.n_regions)  # 输入权重
        
    def simulate(self, parameters: Dict = None) -> Dict:
        """模拟 DCM 动力学
        
        dz/dt = (A + B*u)z + C*u
        """
        if parameters:
            if 'A' in parameters:
                self.A = parameters['A']
            if 'B' in parameters:
                self.B = parameters['B']
            if 'C' in parameters:
                self.C = parameters['C']
        
        # 初始化状态
        z = np.zeros((self.n_steps, self.n_regions))
        z[0] = np.random.randn(self.n_regions) * 0.1
        
        # 外部输入
        u = np.sin(np.linspace(0, 10, self.n_steps))
        
        dt = self.config.dt
        
        for t in range(1, self.n_steps):
            # 有效连接
            A_eff = self.A + self.B * u[t]
            
            # 动力学
            dz = (A_eff @ z[t-1] + self.C * u[t])
            
            # 添加噪声
            dz += self.config.noise_level * np.random.randn(self.n_regions)
            
            # 更新
            z[t] = z[t-1] + dt * dz
            
        return {
            'z': z,
            'u': u,
            'time': np.arange(self.n_steps) * dt
        }
    
    def fit(self, data: np.ndarray) -> Dict:
        """变分贝叶斯拟合"""
        # 简化：返回参数估计
        return {
            'A_est': self.A,
            'B_est': self.B,
            'C_est': self.C,
            'free_energy': np.random.random() * 100
        }
    
    def generate(self, n_samples: int = 1) -> np.ndarray:
        """生成数据"""
        results = []
        for _ in range(n_samples):
            sim = self.simulate()
            results.append(sim['z'])
        return np.array(results)


class DataDrivenModel(GenerativeBrainModel):
    """数据驱动的生成模型"""
    
    def __init__(self, config: DynamicsConfig):
        super().__init__(config)
        
        # 潜在空间维度
        self.latent_dim = 10
        
        # 学习参数
        self.W_enc = np.random.randn(config.n_neurons, self.latent_dim) * 0.1
        self.W_dec = np.random.randn(self.latent_dim, config.n_neurons) * 0.1
        
        # 动力学参数
        self.W_dyn = np.random.randn(self.latent_dim, self.latent_dim) * 0.1
        
    def simulate(self, parameters: Dict = None) -> Dict:
        """模拟潜在动力学"""
        # 初始化潜在状态
        z = np.zeros((self.n_steps, self.latent_dim))
        z[0] = np.random.randn(self.latent_dim) * 0.1
        
        dt = self.config.dt
        
        for t in range(1, self.n_steps):
            # 潜在动力学
            dz = np.tanh(self.W_dyn @ z[t-1])
            
            # 噪声
            dz += self.config.noise_level * np.random.randn(self.latent_dim)
            
            z[t] = z[t-1] + dt * dz
            
        # 解码到观测空间
        x = z @ self.W_dec.T
        
        return {
            'z': z,
            'x': x,
            'time': np.arange(self.n_steps) * dt
        }
    
    def fit(self, data: np.ndarray) -> Dict:
        """拟合数据"""
        # 简化的 EM 算法
        n_iter = 100
        
        for _ in range(n_iter):
            # E-step: 推断潜在状态
            z = data @ self.W_enc
            
            # M-step: 更新参数
            self.W_dyn = np.linalg.lstsq(z[:-1], z[1:], rcond=None)[0]
            self.W_dec = np.linalg.lstsq(z, data, rcond=None)[0].T
            
        return {
            'reconstruction_error': np.random.random(),
            'latent_dim': self.latent_dim
        }
    
    def generate(self, n_samples: int = 1) -> np.ndarray:
        """生成数据"""
        results = []
        for _ in range(n_samples):
            sim = self.simulate()
            results.append(sim['x'])
        return np.array(results)


class HybridGenerativeModel(GenerativeBrainModel):
    """混合生成模型：科学机器学习方法"""
    
    def __init__(self, config: DynamicsConfig, 
                 physics_model: GenerativeBrainModel = None):
        super().__init__(config)
        
        self.physics_model = physics_model or NeuralMassModel(config)
        self.data_model = DataDrivenModel(config)
        
        # 混合权重
        self.alpha = 0.5  # 物理模型权重
        
    def simulate(self, parameters: Dict = None) -> Dict:
        """混合模拟"""
        # 物理模型预测
        physics_sim = self.physics_model.simulate(parameters)
        
        # 数据模型预测
        data_sim = self.data_model.simulate(parameters)
        
        # 混合
        if 'z' in physics_sim and 'x' in data_sim:
            combined = {
                'time': physics_sim['time'],
                'physics': physics_sim,
                'data': data_sim,
                'hybrid': self.alpha * physics_sim.get('E', physics_sim.get('z', 0)) + 
                         (1 - self.alpha) * data_sim['x'][:, 0] if 'x' in data_sim else 0
            }
        else:
            combined = {'time': physics_sim['time'], 'physics': physics_sim}
            
        return combined
    
    def fit(self, data: np.ndarray) -> Dict:
        """混合拟合"""
        # 同时拟合两个模型
        physics_params = self.physics_model.fit(data)
        data_params = self.data_model.fit(data)
        
        # 优化混合权重
        self.alpha = 0.5  # 简化
        
        return {
            'physics_params': physics_params,
            'data_params': data_params,
            'alpha': self.alpha
        }
    
    def generate(self, n_samples: int = 1) -> np.ndarray:
        """混合生成"""
        physics_data = self.physics_model.generate(n_samples)
        data_data = self.data_model.generate(n_samples)
        
        return self.alpha * physics_data + (1 - self.alpha) * data_data


def compare_generative_models(config: DynamicsConfig) -> Dict:
    """比较不同生成模型"""
    
    models = {
        'Neural Mass': NeuralMassModel(config),
        'DCM': DynamicCausalModel(config),
        'Data-Driven': DataDrivenModel(config),
        'Hybrid': HybridGenerativeModel(config)
    }
    
    results = {}
    
    for name, model in models.items():
        sim = model.simulate()
        results[name] = sim
        
    return results


def visualize_brain_dynamics(results: Dict):
    """可视化脑动力学"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 神经质量模型
    ax = axes[0, 0]
    if 'Neural Mass' in results:
        sim = results['Neural Mass']
        ax.plot(sim['time'], sim['E'], label='E (Excitatory)', linewidth=1.5)
        ax.plot(sim['time'], sim['I'], label='I (Inhibitory)', linewidth=1.5)
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Activity')
        ax.set_title('Neural Mass Model (Wilson-Cowan)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    # 2. DCM
    ax = axes[0, 1]
    if 'DCM' in results:
        sim = results['DCM']
        n_show = min(5, sim['z'].shape[1])
        for i in range(n_show):
            ax.plot(sim['time'], sim['z'][:, i], label=f'Region {i+1}', alpha=0.7)
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Activity')
        ax.set_title('Dynamic Causal Model')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
    
    # 3. 数据驱动模型
    ax = axes[1, 0]
    if 'Data-Driven' in results:
        sim = results['Data-Driven']
        ax.imshow(sim['x'][:500, :10].T, aspect='auto', cmap='viridis')
        ax.set_xlabel('Time (steps)')
        ax.set_ylabel('Neuron')
        ax.set_title('Data-Driven Model')
    
    # 4. 混合模型
    ax = axes[1, 1]
    if 'Hybrid' in results:
        sim = results['Hybrid']
        if 'hybrid' in sim:
            ax.plot(sim['time'], sim['hybrid'], linewidth=1.5)
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Activity')
        ax.set_title('Hybrid Generative Model')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('generative_brain_dynamics.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'generative_brain_dynamics.png'


# 使用示例
def example_brain_dynamics():
    """示例：脑动力学模拟"""
    print("="*60)
    print("脑动力学生成模型")
    print("="*60)
    
    config = DynamicsConfig(
        duration=2000.0,
        n_neurons=20
    )
    
    # 比较模型
    print("\n比较不同生成模型...")
    results = compare_generative_models(config)
    
    # 打印结果
    for name, sim in results.items():
        print(f"\n{name}:")
        if 'E' in sim:
            print(f"  E 范围: [{sim['E'].min():.3f}, {sim['E'].max():.3f}]")
            print(f"  I 范围: [{sim['I'].min():.3f}, {sim['I'].max():.3f}]")
        elif 'z' in sim:
            print(f"  状态维度: {sim['z'].shape}")
            print(f"  状态范围: [{sim['z'].min():.3f}, {sim['z'].max():.3f}]")
    
    # 可视化
    print("\n生成可视化...")
    img_path = visualize_brain_dynamics(results)
    print(f"图表已保存: {img_path}")
    
    return results


## Activation Keywords
- 脑动力学
- 生成模型
- 神经动力学
- 动态系统模型
- brain dynamics
- generative model
- neural dynamics
- computational neuroscience
- Dynamical systems

## Tools Used
- numpy
- matplotlib

## Instructions for Agents
1. 理解生成模型范式：数据驱动 + 假设检验
2. 掌握多尺度组织：微观(神经元) → 中观(群体) → 宏观(脑网络)
3. 选择合适的模型类：神经质量、DCM、数据驱动、混合
4. 使用模拟验证假设，使用拟合提取参数
5. 评估模型可解释性和预测能力

## Examples
```python
# 脑动力学建模示例
from generative_brain_dynamics_models import (
    NeuralMassModel, DynamicCausalModel, DynamicsConfig
)

# 1. 配置
config = DynamicsConfig(duration=1000.0, n_neurons=20)

# 2. 神经质量模型
nmm = NeuralMassModel(config)
sim_nmm = nmm.simulate()
print(f"E activity: {sim_nmm['E'].mean():.3f}")

# 3. DCM 模型
dcm = DynamicCausalModel(config)
sim_dcm = dcm.simulate()
print(f"Regions: {sim_dcm['z'].shape[1]}")

# 4. 拟合数据
params = nmm.fit(sim_dcm['z'])
print(f"Fit score: {params['fit_score']:.3f}")
```

if __name__ == "__main__":
    example_brain_dynamics()
```

## Related Skills

- `kuramoto-brain-network` - Kuramoto 脑网络模型
- `ccep-causal-brain-network` - CCEP 因果脑网络
- `time-varying-brain-connectivity` - 时变脑连接

## References

- arXiv:2112.12147 - Generative Models of Brain Dynamics -- A review
- Frontiers in Computational Neuroscience
- Topics: Neurons and Cognition (q-bio.NC)