---
name: event-triggered-formation-control
description: "Switched Event-Triggered Mechanism (SETM) for full state-constrained formation control of multi-vehicle systems. Uses smooth nonlinear mapping, RBFNN, and backstepping for intelligent transportation systems. Activation: event-triggered formation control, state-constrained formation, switched SETM, 事件触发编队控制."
---

# Event-Triggered Formation Control

## Description
切换事件触发机制(SETM)用于具有全状态约束的多车辆系统编队控制。通过平滑非线性映射转换约束状态空间，使用RBF神经网络在线逼近未知动力学，实现智能交通系统中自动驾驶车辆的编队控制。

## Activation Keywords
- event-triggered formation control
- state-constrained formation
- switched SETM
- 事件触发编队控制
- multi-vehicle formation
- formation control with constraints
- RBFNN formation control
- backstepping formation

## Problem Statement

### 编队控制挑战

在智能交通系统(ITS)中，车辆编队控制需要满足多种状态约束：
- **车间距约束**: 避免碰撞和保持安全距离
- **车速约束**: 满足道路限速要求
- **控制输入约束**: 执行器饱和限制

### 现有方法局限性

当系统状态接近约束边界时：
- 控制奇异性问题
- 过度控制努力
- 实际应用受限

## Core Methodology

### 1. 平滑非线性映射

将约束状态空间转换为无约束空间：

```python
import numpy as np

class ConstraintMapping:
    """平滑非线性映射处理状态约束"""
    
    def __init__(self, state_bounds):
        """
        Args:
            state_bounds: 状态约束边界 [(x_min, x_max), (v_min, v_max), ...]
        """
        self.bounds = state_bounds
        self.n_states = len(state_bounds)
    
    def forward_map(self, z):
        """
        将无约束变量 z 映射到约束状态 x
        
        使用tanh函数保证状态在约束范围内:
        x = (x_max + x_min)/2 + (x_max - x_min)/2 * tanh(z)
        
        Args:
            z: 无约束变量
        
        Returns:
            x: 约束状态
        """
        x = np.zeros(self.n_states)
        for i, (z_i, (x_min, x_max)) in enumerate(zip(z, self.bounds)):
            center = (x_max + x_min) / 2
            scale = (x_max - x_min) / 2
            x[i] = center + scale * np.tanh(z_i)
        return x
    
    def inverse_map(self, x):
        """
        将约束状态 x 映射回无约束变量 z
        
        z = arctanh((2x - x_max - x_min) / (x_max - x_min))
        
        Args:
            x: 约束状态
        
        Returns:
            z: 无约束变量
        """
        z = np.zeros(self.n_states)
        for i, (x_i, (x_min, x_max)) in enumerate(zip(x, self.bounds)):
            if x_i <= x_min or x_i >= x_max:
                # 边界保护
                epsilon = 1e-6
                x_i = np.clip(x_i, x_min + epsilon, x_max - epsilon)
            normalized = (2 * x_i - x_max - x_min) / (x_max - x_min)
            z[i] = 0.5 * np.log((1 + normalized) / (1 - normalized))
        return z
    
    def jacobian(self, z):
        """
        计算映射的雅可比矩阵
        
        dx/dz = diag((x_max - x_min)/2 * sech²(z))
        
        Args:
            z: 无约束变量
        
        Returns:
            J: 雅可比矩阵
        """
        J = np.zeros((self.n_states, self.n_states))
        for i, (z_i, (x_min, x_max)) in enumerate(zip(z, self.bounds)):
            scale = (x_max - x_min) / 2
            J[i, i] = scale * (1 - np.tanh(z_i)**2)
        return J
```

### 2. RBF神经网络在线逼近

使用径向基函数神经网络逼近未知非线性动力学：

```python
class RBFNN:
    """径向基函数神经网络"""
    
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        
        # 初始化中心和宽度
        self.centers = np.random.randn(hidden_dim, input_dim)
        self.widths = np.ones(hidden_dim) * 0.5
        
        # 输出权重（自适应更新）
        self.weights = np.zeros((hidden_dim, output_dim))
        self.gamma = 0.1  # 自适应学习率
    
    def gaussian(self, x, c, sigma):
        """高斯基函数"""
        return np.exp(-np.sum((x - c)**2) / (2 * sigma**2))
    
    def forward(self, x):
        """前向传播"""
        phi = np.array([self.gaussian(x, c, w) 
                       for c, w in zip(self.centers, self.widths)])
        return phi @ self.weights
    
    def adaptive_update(self, x, error, dt):
        """
        自适应权重更新
        
        基于Lyapunov稳定性设计更新律
        """
        phi = np.array([self.gaussian(x, c, w) 
                       for c, w in zip(self.centers, self.widths)])
        
        # 投影算子保证权重有界
        self.weights -= self.gamma * np.outer(phi, error) * dt
        self.weights = np.clip(self.weights, -10, 10)
        
        return self.weights
    
    def approximate_dynamics(self, state, control):
        """
        逼近系统动力学
        
        f(x, u) ≈ W^T * φ(x, u)
        """
        input_vec = np.concatenate([state, control])
        return self.forward(input_vec)
```

### 3. 反步控制器设计

基于反步技术设计自适应控制器：

```python
class BacksteppingController:
    """反步自适应控制器"""
    
    def __init__(self, n_vehicles, state_dim, control_dim):
        self.n = n_vehicles
        self.state_dim = state_dim
        self.control_dim = control_dim
        
        # 控制增益
        self.k1 = 1.0  # 位置误差增益
        self.k2 = 2.0  # 速度误差增益
        
        # RBFNN逼近器
        self.rbfnn = RBFNN(
            input_dim=state_dim + control_dim,
            hidden_dim=20,
            output_dim=state_dim
        )
    
    def compute_virtual_control(self, position_error, velocity):
        """
        计算虚拟控制输入
        
        α = -k1 * e_p + v_d
        
        Args:
            position_error: 位置误差
            velocity: 当前速度
        
        Returns:
            alpha: 虚拟控制
        """
        return -self.k1 * position_error
    
    def compute_actual_control(self, state, virtual_control, dynamics_estimate):
        """
        计算实际控制输入
        
        u = -k2 * e_v - e_p + α_dot - f_hat
        
        Args:
            state: 当前状态 [position, velocity]
            virtual_control: 虚拟控制
            dynamics_estimate: 动力学估计
        
        Returns:
            control: 实际控制输入
        """
        position = state[:self.state_dim//2]
        velocity = state[self.state_dim//2:]
        
        # 速度误差
        velocity_error = velocity - virtual_control
        
        # 位置误差
        position_error = position - self.desired_position
        
        # 控制律
        control = (-self.k2 * velocity_error 
                  - position_error 
                  - dynamics_estimate)
        
        return control
    
    def control_law(self, state, desired_state, dt):
        """
        完整控制律
        
        Args:
            state: 当前状态
            desired_state: 期望状态
            dt: 时间步长
        
        Returns:
            control: 控制输入
            rbfnn_update: RBFNN更新
        """
        self.desired_position = desired_state[:self.state_dim//2]
        
        # 估计动力学
        current_control = np.zeros(self.control_dim)  # 上一次控制
        dynamics_est = self.rbfnn.approximate_dynamics(state, current_control)
        
        # 计算虚拟控制
        position = state[:self.state_dim//2]
        position_error = position - self.desired_position
        virtual_control = self.compute_virtual_control(position_error, state[self.state_dim//2:])
        
        # 计算实际控制
        control = self.compute_actual_control(state, virtual_control, dynamics_est)
        
        # 更新RBFNN
        velocity = state[self.state_dim//2:]
        velocity_error = velocity - virtual_control
        self.rbfnn.adaptive_update(
            np.concatenate([state, control]),
            velocity_error,
            dt
        )
        
        return control
```

### 4. 切换事件触发机制(SETM)

```python
class SwitchedEventTriggeredMechanism:
    """切换事件触发机制"""
    
    def __init__(self, transient_threshold=0.1, steady_threshold=0.5):
        """
        Args:
            transient_threshold: 暂态阶段触发阈值
            steady_threshold: 稳态阶段触发阈值
        """
        self.epsilon_t = transient_threshold  # 暂态阈值
        self.epsilon_s = steady_threshold     # 稳态阈值
        
        self.is_transient = True
        self.steady_count = 0
        self.steady_window = 50  # 判断稳态的窗口
    
    def check_trigger(self, current_state, last_transmitted_state, error_norm):
        """
        检查是否触发控制更新
        
        Args:
            current_state: 当前状态
            last_transmitted_state: 上次传输的状态
            error_norm: 当前误差范数
        
        Returns:
            should_trigger: 是否触发
            mode: 当前模式 ('transient' or 'steady')
        """
        # 检测暂态/稳态
        if error_norm < self.epsilon_t:
            self.steady_count += 1
        else:
            self.steady_count = 0
            self.is_transient = True
        
        if self.steady_count > self.steady_window:
            self.is_transient = False
        
        # 选择阈值
        threshold = self.epsilon_t if self.is_transient else self.epsilon_s
        mode = 'transient' if self.is_transient else 'steady'
        
        # 触发条件
        should_trigger = error_norm > threshold
        
        return should_trigger, mode
    
    def get_transmission_statistics(self):
        """获取传输统计信息"""
        return {
            'mode': 'transient' if self.is_transient else 'steady',
            'transient_threshold': self.epsilon_t,
            'steady_threshold': self.epsilon_s
        }
```

### 5. 完整编队控制系统

```python
class FormationControlSystem:
    """多车辆编队控制系统"""
    
    def __init__(self, n_vehicles, vehicle_params):
        """
        Args:
            n_vehicles: 车辆数量
            vehicle_params: 车辆参数字典
        """
        self.n = n_vehicles
        self.params = vehicle_params
        
        # 状态约束 (位置, 速度)
        state_bounds = [
            (0, 1000),    # 位置范围
            (0, 30)       # 速度范围 (m/s)
        ]
        
        self.constraint_map = ConstraintMapping(state_bounds)
        self.controller = BacksteppingController(
            n_vehicles=n_vehicles,
            state_dim=2,  # [position, velocity]
            control_dim=1  # [acceleration]
        )
        self.event_trigger = SwitchedEventTriggeredMechanism()
        
        # 编队拓扑
        self.topology = self._create_platoon_topology()
    
    def _create_platoon_topology(self):
        """创建车队拓扑结构 (链式)"""
        topology = {}
        for i in range(self.n):
            neighbors = []
            if i > 0:
                neighbors.append(i-1)  # 前车
            if i < self.n - 1:
                neighbors.append(i+1)  # 后车
            topology[i] = neighbors
        return topology
    
    def simulate_step(self, states, desired_formation, dt):
        """
        模拟单步编队控制
        
        Args:
            states: 当前状态 (无约束变量)
            desired_formation: 期望编队
            dt: 时间步长
        
        Returns:
            new_states: 新状态
            controls: 控制输入
            trigger_info: 触发信息
        """
        new_states = []
        controls = []
        trigger_info = []
        
        for i in range(self.n):
            # 转换到约束状态空间
            constrained_state = self.constraint_map.forward_map(states[i])
            
            # 计算期望状态
            desired_state = desired_formation[i]
            
            # 事件触发检查
            error = np.linalg.norm(constrained_state - desired_state)
            should_trigger, mode = self.event_trigger.check_trigger(
                constrained_state, 
                desired_state, 
                error
            )
            
            if should_trigger or i == 0:  # 领导者始终更新
                # 计算控制
                control = self.controller.control_law(
                    constrained_state, 
                    desired_state, 
                    dt
                )
                
                # 状态更新 (简化模型)
                acceleration = control[0]
                velocity = constrained_state[1] + acceleration * dt
                position = constrained_state[0] + velocity * dt
                
                new_constrained = np.array([position, velocity])
                new_unconstrained = self.constraint_map.inverse_map(new_constrained)
            else:
                # 保持上一控制
                control = np.zeros(1)
                new_unconstrained = states[i]
            
            new_states.append(new_unconstrained)
            controls.append(control)
            trigger_info.append({'triggered': should_trigger, 'mode': mode})
        
        return np.array(new_states), controls, trigger_info
    
    def run_simulation(self, initial_states, desired_formation, T, dt):
        """
        运行完整仿真
        
        Args:
            initial_states: 初始状态
            desired_formation: 期望编队
            T: 总时间
            dt: 时间步长
        
        Returns:
            trajectory: 轨迹
            stats: 统计信息
        """
        states = initial_states.copy()
        trajectory = [states.copy()]
        trigger_events = []
        
        n_steps = int(T / dt)
        for step in range(n_steps):
            states, controls, info = self.simulate_step(
                states, 
                desired_formation, 
                dt
            )
            trajectory.append(states.copy())
            trigger_events.extend([i['triggered'] for i in info])
        
        # 统计
        stats = {
            'total_steps': n_steps * self.n,
            'trigger_events': sum(trigger_events),
            'communication_reduction': 1 - sum(trigger_events) / (n_steps * self.n)
        }
        
        return np.array(trajectory), stats
```

## Lyapunov稳定性分析

### 闭环系统稳定性

使用Lyapunov方法证明闭环系统中所有信号保持均匀有界：

```python
def analyze_stability(controller, system, initial_state):
    """
    分析系统稳定性
    
    Returns:
        stable: 是否稳定
        lyapunov_values: Lyapunov函数值历史
    """
    V_history = []
    state = initial_state.copy()
    
    for t in range(1000):
        # 计算Lyapunov函数
        V = 0.5 * np.sum(state**2)
        V_history.append(V)
        
        # 检查收敛
        if V < 1e-6:
            return True, V_history
        
        # 系统演化
        control = controller.control_law(state, np.zeros_like(state), 0.01)
        state += control * 0.01
    
    return V_history[-1] < V_history[0], V_history
```

### Zeno行为排除

通过设计最小触发间隔排除Zeno行为：

```python
class ZenoFreeTrigger:
    """无Zeno行为的事件触发"""
    
    def __init__(self, min_interval=0.01):
        self.min_interval = min_interval
        self.last_trigger_time = 0
    
    def check_with_zeno_protection(self, current_time, error):
        """
        带Zeno保护的事件触发检查
        
        Args:
            current_time: 当前时间
            error: 当前误差
        
        Returns:
            trigger: 是否触发
        """
        # 最小间隔检查
        if current_time - self.last_trigger_time < self.min_interval:
            return False
        
        # 正常触发检查
        if error > self.threshold:
            self.last_trigger_time = current_time
            return True
        
        return False
```

## 仿真验证

```python
# 创建编队控制系统
n_vehicles = 5
vehicle_params = {
    'mass': 1500,  # kg
    'max_acceleration': 3,  # m/s²
    'max_deceleration': 5   # m/s²
}

system = FormationControlSystem(n_vehicles, vehicle_params)

# 初始状态 (无约束变量)
initial_states = np.array([
    [0, 20],   # 车辆1: [位置偏移, 速度]
    [-50, 20], # 车辆2
    [-100, 20],# 车辆3
    [-150, 20],# 车辆4
    [-200, 20] # 车辆5
])

# 期望编队
desired_formation = np.array([
    [500, 20],  # 目标位置500m, 速度20m/s
    [450, 20],
    [400, 20],
    [350, 20],
    [300, 20]
])

# 运行仿真
trajectory, stats = system.run_simulation(
    initial_states, 
    desired_formation, 
    T=100,  # 100秒
    dt=0.01 # 10ms
)

print(f"通信开销降低: {stats['communication_reduction']*100:.1f}%")
print(f"总触发事件: {stats['trigger_events']}")
```

## Tools Used

- **python/numpy**: 数值计算
- **scipy.optimize**: 约束处理
- **matplotlib**: 编队轨迹可视化
- **networkx**: 通信拓扑分析

## Best Practices

### 1. 参数调优
```python
# 控制增益调优
def tune_gains(system, test_scenarios):
    best_gains = None
    best_performance = float('inf')
    
    for k1 in [0.5, 1.0, 2.0, 5.0]:
        for k2 in [1.0, 2.0, 5.0, 10.0]:
            controller.k1 = k1
            controller.k2 = k2
            
            performance = evaluate_performance(system, test_scenarios)
            if performance < best_performance:
                best_performance = performance
                best_gains = (k1, k2)
    
    return best_gains
```

### 2. 约束设计
- 确保约束可行
- 避免约束边界过于接近
- 考虑实际物理限制

### 3. 事件触发阈值选择
- 暂态阶段：较小阈值保证快速收敛
- 稳态阶段：较大阈值降低通信负担

## References

- Paper: "On Switched Event-triggered Full State-constrained Formation Control for Multi-vehicle Systems" (arXiv:2604.10993v1, 2026)
- Authors: Zihan Li, Ziming Wang, Xin Wang
- Category: eess.SY

## Related Skills

- `distributed-bilevel-macroscopic-optimization`: 分布式双层宏观优化
- `game-theoretic-consensus-control`: 博弈论一致性控制
- `multi-agent-density-control`: 多智能体密度控制
- `distributed-optimal-consensus`: 分布式最优一致性

## Limitations

- 需要准确的状态约束边界
- RBFNN中心点选择影响性能
- 复杂拓扑结构分析较困难
- 计算复杂度随车辆数量增加

## Extensions

### 异构车辆支持
```python
class HeterogeneousFormation(FormationControlSystem):
    def __init__(self, vehicle_list):
        """
        vehicle_list: 不同参数的车辆列表
        """
        super().__init__(len(vehicle_list), {})
        self.vehicles = vehicle_list
    
    def simulate_step(self, states, desired_formation, dt):
        # 为每辆车使用特定参数
        for i, vehicle in enumerate(self.vehicles):
            vehicle.update_dynamics(states[i], dt)
```

### 动态编队
```python
def dynamic_formation(self, time, formation_type='sinusoidal'):
    """时变编队"""
    if formation_type == 'sinusoidal':
        offset = 10 * np.sin(0.1 * time)
    elif formation_type == 'lane_change':
        offset = self.lane_change_trajectory(time)
    
    return self.base_formation + offset
```

---

_Last updated: 2026-04-14_