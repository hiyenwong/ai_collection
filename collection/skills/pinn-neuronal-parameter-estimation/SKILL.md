---
name: pinn-neuronal-parameter-estimation
description: 使用物理信息神经网络(PINN)进行神经元模型参数估计和状态重构的方法论。仅需要部分电压观测即可重建未观测状态变量和估计未知生物物理参数，对初始参数猜测不敏感。适用于Morris-Lecar模型、快慢放电/爆发模型、呼吸神经元模型。触发词：参数估计、状态重构、PINN、神经元模型、逆向问题、逆向建模、physics-informed neural network、parameter estimation、state reconstruction、Morris-Lecar。
user-invocable: true
---

# Physics-Informed Neural Networks for Neuronal Parameter Estimation

使用物理信息神经网络进行多尺度神经元系统的鲁棒参数和状态估计

## 核心方法论

**来源：** arXiv:2603.08742
**效用：** 0.90

### 问题背景

从部分和噪声观测推断生物物理参数和隐藏状态变量是计算神经科学的基本挑战：

| 挑战 | 描述 |
|------|------|
| 强非线性 | 快-慢放电/爆发模型具有强非线性 |
| 多尺度动态 | 不同时间尺度的变量耦合 |
| 观测数据有限 | 往往只能测量膜电位 |
| 初始猜测敏感 | 传统方法对初始参数极度敏感 |

### PINN 框架优势

| 传统方法 | PINN 方法 |
|----------|-----------|
| 需要数值求解器 | 无网格方法 |
| 对初始猜测敏感 | 鲁棒性强 |
| 短观测窗口失败 | 短窗口有效 |
| 计算成本高 | 端到端学习 |

### 实现框架

```python
import numpy as np
import torch
import torch.nn as nn
from typing import Tuple, List, Optional

class PhysicsInformedNeuronNet(nn.Module):
    """
    用于神经元模型的物理信息神经网络
    
    核心思想：
    1. 神经网络近似状态变量（如 v(t), n(t)）
    2. 自动微分计算导数
    3. 将神经元模型方程作为物理约束加入损失函数
    4. 同时学习未知参数
    """
    
    def __init__(
        self,
        hidden_dims: List[int] = [64, 64, 64],
        n_state_vars: int = 2,  # v, n for Morris-Lecar
        activation: str = 'tanh'
    ):
        super().__init__()
        
        self.n_state_vars = n_state_vars
        
        # 激活函数
        if activation == 'tanh':
            self.act = nn.Tanh()
        elif activation == 'sin':
            self.act = torch.sin
        else:
            self.act = nn.ReLU()
        
        # 时间输入层
        layers = [nn.Linear(1, hidden_dims[0]), self.act]
        
        # 隐藏层
        for i in range(len(hidden_dims) - 1):
            layers.append(nn.Linear(hidden_dims[i], hidden_dims[i+1]))
            layers.append(self.act)
        
        # 输出层：状态变量
        layers.append(nn.Linear(hidden_dims[-1], n_state_vars))
        
        self.net = nn.Sequential(*layers)
        
        # 可学习的生物物理参数
        # 初始化为随机值（体现鲁棒性）
        self.params = nn.ParameterDict({
            'g_Ca': nn.Parameter(torch.tensor(4.0)),  # 钙电导
            'g_K': nn.Parameter(torch.tensor(8.0)),   # 钾电导
            'g_L': nn.Parameter(torch.tensor(2.0)),   # 漏电导
            'V_Ca': nn.Parameter(torch.tensor(120.0)), # 钙反转电位
            'V_K': nn.Parameter(torch.tensor(-80.0)),  # 钾反转电位
            'V_L': nn.Parameter(torch.tensor(-60.0)),  # 漏反转电位
            'phi': nn.Parameter(torch.tensor(0.04)),   # 门控时间尺度
            'C': nn.Parameter(torch.tensor(20.0))      # 膜电容
        })
    
    def forward(self, t: torch.Tensor) -> torch.Tensor:
        """
        前向传播：输入时间，输出状态变量
        
        参数:
            t: 时间点 (batch_size, 1)
            
        返回:
            状态变量 (batch_size, n_state_vars)
        """
        return self.net(t)
    
    def get_state_and_derivatives(
        self, 
        t: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        获取状态变量及其时间导数
        
        使用自动微分计算 dv/dt, dn/dt
        """
        t.requires_grad_(True)
        
        # 前向传播
        state = self.forward(t)
        
        # 计算导数
        derivatives = []
        for i in range(self.n_state_vars):
            grad = torch.autograd.grad(
                state[:, i].sum(),
                t,
                create_graph=True
            )[0]
            derivatives.append(grad)
        
        derivatives = torch.cat(derivatives, dim=1)
        
        return state, derivatives


class MorrisLecarPINN:
    """
    Morris-Lecar 模型的 PINN 实现
    
    Morris-Lecar 方程：
    C * dv/dt = -g_Ca*m_inf(v)*(v-V_Ca) - g_K*n*(v-V_K) - g_L*(v-V_L) + I_app
    dn/dt = phi * (n_inf(v) - n) / tau_n(v)
    
    其中：
    m_inf(v) = 0.5 * (1 + tanh((v-V1)/V2))
    n_inf(v) = 0.5 * (1 + tanh((v-V3)/V4))
    tau_n(v) = 1 / cosh((v-V3)/(2*V4))
    """
    
    def __init__(self, V1: float = -1.2, V2: float = 18.0, 
                 V3: float = 2.0, V4: float = 30.0):
        """
        参数:
            V1, V2: m_inf 参数
            V3, V4: n_inf 和 tau_n 参数
        """
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        
        self.net = PhysicsInformedNeuronNet(n_state_vars=2)
    
    def m_inf(self, v: torch.Tensor) -> torch.Tensor:
        """稳态钙门控"""
        return 0.5 * (1 + torch.tanh((v - self.V1) / self.V2))
    
    def n_inf(self, v: torch.Tensor) -> torch.Tensor:
        """稳态钾门控"""
        return 0.5 * (1 + torch.tanh((v - self.V3) / self.V4))
    
    def tau_n(self, v: torch.Tensor) -> torch.Tensor:
        """钾门控时间常数"""
        return 1.0 / torch.cosh((v - self.V3) / (2 * self.V4))
    
    def physics_loss(
        self,
        t: torch.Tensor,
        I_app: float
    ) -> torch.Tensor:
        """
        物理约束损失
        
        确保 PINN 输出满足 Morris-Lecar 方程
        """
        # 获取状态和导数
        state, deriv = self.net.get_state_and_derivatives(t)
        
        v = state[:, 0:1]   # 膜电位
        n = state[:, 1:2]   # 钾门控
        
        dv_dt = deriv[:, 0:1]
        dn_dt = deriv[:, 1:2]
        
        # 获取可学习参数
        g_Ca = self.net.params['g_Ca']
        g_K = self.net.params['g_K']
        g_L = self.net.params['g_L']
        V_Ca = self.net.params['V_Ca']
        V_K = self.net.params['V_K']
        V_L = self.net.params['V_L']
        phi = self.net.params['phi']
        C = self.net.params['C']
        
        # 计算方程右端
        I_Ca = g_Ca * self.m_inf(v) * (v - V_Ca)
        I_K = g_K * n * (v - V_K)
        I_L = g_L * (v - V_L)
        
        # Morris-Lecar 方程残差
        residual_v = C * dv_dt + I_Ca + I_K + I_L - I_app
        residual_n = dn_dt - phi * (self.n_inf(v) - n) / self.tau_n(v)
        
        # 物理损失
        loss = torch.mean(residual_v**2) + torch.mean(residual_n**2)
        
        return loss
    
    def data_loss(
        self,
        t: torch.Tensor,
        v_obs: torch.Tensor
    ) -> torch.Tensor:
        """
        数据拟合损失
        
        确保 PINN 预测与观测电压一致
        """
        state = self.net(t)
        v_pred = state[:, 0]
        
        loss = torch.mean((v_pred - v_obs)**2)
        
        return loss
    
    def train(
        self,
        t_data: np.ndarray,
        v_data: np.ndarray,
        t_physics: np.ndarray,
        I_app: float,
        n_epochs: int = 10000,
        lr: float = 1e-3,
        lambda_data: float = 1.0,
        lambda_physics: float = 1.0,
        verbose: bool = True
    ) -> dict:
        """
        训练 PINN
        
        参数:
            t_data: 观测时间点
            v_data: 观测电压
            t_physics: 物理约束点
            I_app: 外加电流
            n_epochs: 训练轮数
            lr: 学习率
            lambda_data: 数据损失权重
            lambda_physics: 物理损失权重
            verbose: 是否打印训练信息
            
        返回:
            训练历史
        """
        optimizer = torch.optim.Adam(self.net.parameters(), lr=lr)
        
        # 转换为张量
        t_data_tensor = torch.tensor(t_data, dtype=torch.float32).reshape(-1, 1)
        v_data_tensor = torch.tensor(v_data, dtype=torch.float32).reshape(-1)
        t_physics_tensor = torch.tensor(t_physics, dtype=torch.float32).reshape(-1, 1)
        
        history = {'loss': [], 'data_loss': [], 'physics_loss': []}
        
        for epoch in range(n_epochs):
            optimizer.zero_grad()
            
            # 计算损失
            l_data = self.data_loss(t_data_tensor, v_data_tensor)
            l_physics = self.physics_loss(t_physics_tensor, I_app)
            
            loss = lambda_data * l_data + lambda_physics * l_physics
            
            # 反向传播
            loss.backward()
            optimizer.step()
            
            # 记录
            history['loss'].append(loss.item())
            history['data_loss'].append(l_data.item())
            history['physics_loss'].append(l_physics.item())
            
            if verbose and epoch % 1000 == 0:
                print(f"Epoch {epoch}: Loss = {loss.item():.6f}, "
                      f"Data = {l_data.item():.6f}, Physics = {l_physics.item():.6f}")
        
        return history
    
    def get_estimated_params(self) -> dict:
        """获取估计的参数"""
        return {k: v.item() for k, v in self.net.params.items()}
    
    def predict(
        self, 
        t: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        预测状态变量
        
        返回:
            v: 膜电位
            n: 钾门控
        """
        t_tensor = torch.tensor(t, dtype=torch.float32).reshape(-1, 1)
        with torch.no_grad():
            state = self.net(t_tensor)
        
        v = state[:, 0].numpy()
        n = state[:, 1].numpy()
        
        return v, n


class MultiScalePINN:
    """
    多尺度神经元模型的 PINN
    
    处理快-慢系统（如爆发模型）
    """
    
    def __init__(self, n_fast: int = 2, n_slow: int = 1):
        """
        参数:
            n_fast: 快变量数量
            n_slow: 慢变量数量
        """
        self.n_fast = n_fast
        self.n_slow = n_slow
        
        # 分别处理快慢变量
        self.fast_net = PhysicsInformedNeuronNet(n_state_vars=n_fast)
        self.slow_net = PhysicsInformedNeuronNet(n_state_vars=n_slow)
    
    def adaptive_physics_points(
        self,
        t_obs: np.ndarray,
        v_obs: np.ndarray,
        n_points: int = 1000
    ) -> np.ndarray:
        """
        自适应选择物理约束点
        
        在电压变化剧烈的区域增加采样密度
        """
        # 计算电压变化率
        dv = np.abs(np.diff(v_obs))
        
        # 变化剧烈的区域
        high_activity = dv > np.percentile(dv, 75)
        
        # 时间范围
        t_min, t_max = t_obs.min(), t_obs.max()
        
        # 基础均匀采样
        t_uniform = np.linspace(t_min, t_max, n_points // 2)
        
        # 在高活动区域额外采样
        t_high_activity = t_obs[:-1][high_activity]
        t_high = np.random.choice(
            t_high_activity, 
            size=min(n_points // 2, len(t_high_activity)),
            replace=True
        )
        
        # 合并
        t_physics = np.concatenate([t_uniform, t_high])
        t_physics = np.sort(np.unique(t_physics))
        
        return t_physics


def estimate_neuron_parameters(
    t_data: np.ndarray,
    v_data: np.ndarray,
    I_app: float,
    model_type: str = 'morris-lecar',
    n_epochs: int = 10000,
    verbose: bool = True
) -> dict:
    """
    从电压观测估计神经元模型参数
    
    参数:
        t_data: 时间点
        v_data: 观测电压
        I_app: 外加电流
        model_type: 模型类型
        n_epochs: 训练轮数
        verbose: 是否打印信息
        
    返回:
        估计结果字典
    """
    # 归一化
    t_norm = (t_data - t_data.min()) / (t_data.max() - t_data.min())
    v_norm = (v_data - v_data.mean()) / v_data.std()
    
    # 创建模型
    if model_type == 'morris-lecar':
        model = MorrisLecarPINN()
    
    # 生成物理约束点
    t_physics = np.linspace(0, 1, 500)
    
    # 训练
    history = model.train(
        t_norm, v_norm,
        t_physics, I_app,
        n_epochs=n_epochs,
        verbose=verbose
    )
    
    # 获取结果
    params = model.get_estimated_params()
    v_pred, n_pred = model.predict(t_norm)
    
    return {
        'parameters': params,
        'v_predicted': v_pred * v_data.std() + v_data.mean(),
        'n_predicted': n_pred,
        'history': history
    }
```

## 应用场景

### 1. Morris-Lecar 模型参数估计
- 多种放电模式（静息、周期放电、爆发）
- 短观测窗口即可

### 2. 呼吸神经元模型
- 快慢耦合系统
- 部分观测场景

### 3. 神经元逆向问题
- 从行为推断参数
- 状态重构

## 方法优势

| 优势 | 说明 |
|------|------|
| **鲁棒性强** | 对初始参数猜测不敏感 |
| **数据需求低** | 仅需部分电压观测 |
| **短窗口有效** | 不需要长时间序列 |
| **端到端** | 同时估计参数和重构状态 |

## Activation Keywords
- 参数估计
- 状态重构
- PINN
- 神经元模型
- 逆向问题
- 逆向建模
- physics-informed neural network
- parameter estimation
- state reconstruction
- Morris-Lecar
- inverse problem

## Tools Used
- torch
- numpy
- scipy

## Instructions for Agents
1. 理解物理信息神经网络：将物理方程作为损失函数
2. 掌握自动微分：计算状态变量的时间导数
3. 设置可学习参数：nn.Parameter 用于生物物理参数
4. 平衡数据损失和物理损失：调整权重
5. 注意归一化：对时间和电压归一化

## Examples
```python
# 使用示例
from pinn_neuronal_parameter_estimation import MorrisLecarPINN, estimate_neuron_parameters

# 1. 生成模拟数据（或使用真实观测）
import numpy as np
t = np.linspace(0, 100, 1000)
v_true = ...  # Morris-Lecar 模型电压轨迹

# 2. 估计参数
results = estimate_neuron_parameters(
    t_data=t,
    v_data=v_true,
    I_app=50.0,  # 外加电流
    model_type='morris-lecar',
    n_epochs=10000
)

# 3. 查看估计的参数
print("Estimated parameters:")
for k, v in results['parameters'].items():
    print(f"  {k}: {v:.4f}")

# 4. 预测状态
v_pred = results['v_predicted']
n_pred = results['n_predicted']
```

## 参考文献
- Zhu, X., et al. (2026). "Robust Parameter and State Estimation in Multiscale Neuronal Systems Using Physics-Informed Neural Networks" arXiv:2603.08742
- Raissi, M., et al. (2019). "Physics-informed neural networks" Journal of Computational Physics