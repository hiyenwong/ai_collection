---
name: uncertainty-aware-predictive-safety-filters
description: "Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics. Safety-critical control using neural network dynamics with explicit uncertainty quantification. arXiv:2604.26836"
tags: ["neuroscience", "safety-filters", "uncertainty-quantification", "predictive-control", "neural-dynamics", "safety-critical"]
paper_source: "arXiv:2604.26836"
paper_title: "Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics"
paper_authors: ["Bernd Frauenknecht", "Lukas Kesper", "Daniel Mayfrank"]
paper_date: "2026-04-29"
---

# Uncertainty-Aware Predictive Safety Filters

针对概率神经网络动力学的不确定性感知预测安全滤波器。在神经网络动力学模型存在不确定性的情况下，确保安全关键系统的安全运行。

## 核心概念

### 预测安全滤波器 (Predictive Safety Filter, PSF)

**定义**: 在控制回路中插入的组件，确保只有安全的控制输入被应用到系统。

```
传统控制:       参考 → [控制器] → [系统] → 输出
                 
安全滤波控制:   参考 → [控制器] → [PSF] → [系统] → 输出
                      (验证安全)  (仅传递安全控制)
```

### 不确定性来源

| 来源 | 描述 | 建模方法 |
|------|------|----------|
| **模型误差** | 神经网络近似误差 | 概率输出 |
| **数据噪声** | 观测噪声 | 高斯噪声 |
| **参数不确定性** | 物理参数估计误差 | 贝叶斯推断 |
| **外部扰动** | 未建模动态 | 鲁棒约束 |

## 方法论

### 1. 概率神经网络动力学

```python
class ProbabilisticNeuralDynamics(nn.Module):
    """
    概率神经网络动力学模型
    
    输出状态分布而非点估计
    """
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super().__init__()
        self.state_dim = state_dim
        self.action_dim = action_dim
        
        # 编码器网络
        self.encoder = nn.Sequential(
            nn.Linear(state_dim + action_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        
        # 均值预测头
        self.mean_head = nn.Linear(hidden_dim, state_dim)
        
        # 方差预测头 (对角协方差)
        self.logvar_head = nn.Linear(hidden_dim, state_dim)
        
        # 相关性预测头 (可选)
        self.corr_head = nn.Linear(hidden_dim, state_dim * (state_dim - 1) // 2)
    
    def forward(self, state, action):
        """
        预测下一状态分布
        
        返回: 高斯分布参数 (mean, covariance)
        """
        # 编码
        x = torch.cat([state, action], dim=-1)
        h = self.encoder(x)
        
        # 预测分布参数
        mean = self.mean_head(h)
        logvar = self.logvar_head(h)
        
        # 确保正定性
        std = torch.exp(0.5 * logvar)
        
        return mean, std
    
    def sample_next_state(self, state, action, num_samples=100):
        """
        采样预测下一状态
        """
        mean, std = self.forward(state, action)
        
        # 重参数化采样
        eps = torch.randn(num_samples, *mean.shape, device=mean.device)
        samples = mean.unsqueeze(0) + std.unsqueeze(0) * eps
        
        return samples
    
    def predict_with_uncertainty(self, state, action, horizon=10, num_samples=100):
        """
        长期预测与不确定性传播
        """
        samples = [state.repeat(num_samples, 1)]
        
        for t in range(horizon):
            current_state = samples[-1]
            action_t = action.repeat(num_samples, 1)
            
            # 预测下一状态分布
            mean, std = self.forward(current_state, action_t)
            
            # 采样
            eps = torch.randn_like(mean)
            next_state = mean + std * eps
            samples.append(next_state)
        
        return torch.stack(samples, dim=1)  # [num_samples, horizon+1, state_dim]
```

### 2. 机会约束安全滤波

```python
class UncertaintyAwareSafetyFilter:
    """
    不确定性感知安全滤波器
    
    通过机会约束确保概率安全
    """
    def __init__(self, dynamics_model, safety_constraints, confidence_level=0.95):
        self.dynamics = dynamics_model
        self.constraints = safety_constraints
        self.confidence_level = confidence_level
        self.epsilon = 1 - confidence_level  # 违反概率
    
    def filter_control(self, nominal_control, current_state, horizon=10):
        """
        滤波控制输入以确保安全
        
        求解: min ||u - u_nominal||²
              s.t. P(safe) ≥ 1 - ε
        """
        # 使用采样的机会约束
        num_samples = 1000
        
        # 定义优化问题
        u = cp.Variable(self.dynamics.action_dim)
        
        # 目标: 最小化与名义控制的偏离
        objective = cp.Minimize(cp.sum_squares(u - nominal_control))
        
        # 约束: 机会约束（通过采样近似）
        constraints = []
        
        # 采样未来轨迹
        samples = self.dynamics.predict_with_uncertainty(
            current_state, u, horizon, num_samples
        )
        
        # 对每个约束，确保 (1-ε) 比例的样本满足
        for constraint_fn in self.constraints:
            constraint_values = constraint_fn(samples)
            
            # 使用条件风险价值 (CVaR) 近似机会约束
            # CVaR_ε[X] ≤ 0 近似 P(X ≤ 0) ≥ 1-ε
            cvar_constraint = self._cvar_constraint(
                constraint_values, self.epsilon
            )
            constraints.append(cvar_constraint)
        
        # 求解
        problem = cp.Problem(objective, constraints)
        problem.solve(solver=cp.ECOS)
        
        if problem.status == 'optimal':
            return u.value
        else:
            # 如果不可行，返回保守控制
            return self._get_safe_fallback_control(current_state)
    
    def _cvar_constraint(self, samples, epsilon):
        """
        构建CVaR约束
        
        CVaR_ε[X] = E[X | X ≥ VaR_ε[X]]
        """
        # 排序样本
        sorted_samples = torch.sort(samples)[0]
        
        # VaR是 (1-ε) 分位数
        var_index = int(len(sorted_samples) * (1 - epsilon))
        var = sorted_samples[var_index]
        
        # CVaR近似: 超过VaR的样本的平均
        cvar = torch.mean(sorted_samples[var_index:])
        
        return cvar <= 0
    
    def _get_safe_fallback_control(self, state):
        """
        获取安全回退控制
        """
        # 使用简单的安全控制器（如LQR）
        return -self.K_safe @ state
```

### 3. 鲁棒 Tube-based MPC

```python
class TubeBasedMPC:
    """
    Tube-based模型预测控制
    
    在存在有界不确定性时保证安全
    """
    def __init__(self, nominal_dynamics, uncertainty_bounds, horizon=20):
        self.nominal_dynamics = nominal_dynamics
        self.uncertainty_bounds = uncertainty_bounds  # 不确定性集合
        self.N = horizon
    
    def compute_control(self, current_state, reference_trajectory):
        """
        计算鲁棒MPC控制
        """
        # 状态分解: x = z + e
        # z: 名义状态, e: 误差状态
        
        z = [cp.Variable(self.state_dim) for _ in range(self.N+1)]
        v = [cp.Variable(self.action_dim) for _ in range(self.N)]
        
        # 名义轨迹优化
        constraints = [z[0] == current_state]
        
        for t in range(self.N):
            # 名义动力学
            constraints.append(
                z[t+1] == self.nominal_dynamics(z[t], v[t])
            )
            
            # 收紧的状态约束（考虑Tube）
            for constraint in self.state_constraints:
                # 原始: z ∈ X
                # 收紧: z ∈ X ⊖ S  (Minkowski差)
                constraints.append(
                    constraint(z[t+1]) - self.tube_size <= 0
                )
            
            # 收紧的输入约束
            for constraint in self.input_constraints:
                constraints.append(
                    constraint(v[t]) + self.tube_control_margin <= 0
                )
        
        # 目标: 跟踪性能
        objective = sum(
            cp.quad_form(z[t] - reference_trajectory[t], self.Q) +
            cp.quad_form(v[t], self.R)
            for t in range(self.N)
        )
        
        # 求解
        problem = cp.Problem(cp.Minimize(objective), constraints)
        problem.solve()
        
        if problem.status == 'optimal':
            return v[0].value
        else:
            return self._emergency_control()
```

### 4. 高斯过程安全滤波

```python
class GaussianProcessSafetyFilter:
    """
    基于高斯过程的不确定性量化
    
    GP提供预测不确定性估计
    """
    def __init__(self, state_dim, action_dim):
        from sklearn.gaussian_process import GaussianProcessRegressor
        from sklearn.gaussian_process.kernels import RBF, WhiteKernel
        
        kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
        self.gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
        
        self.state_dim = state_dim
        self.action_dim = action_dim
    
    def train(self, states, actions, next_states):
        """
        训练GP动力学模型
        """
        X = np.hstack([states, actions])
        y = next_states - states  # 预测状态差分
        
        self.gp.fit(X, y)
    
    def predict_with_uncertainty(self, state, action):
        """
        预测带不确定性的下一状态
        """
        X = np.hstack([state, action]).reshape(1, -1)
        
        y_mean, y_std = self.gp.predict(X, return_std=True)
        
        next_state_mean = state + y_mean
        next_state_std = y_std
        
        return next_state_mean, next_state_std
    
    def probabilistic_safety_check(self, state, action, safety_margin=3.0):
        """
        概率安全检验
        
        检查 (mean + margin * std) 是否安全
        """
        mean, std = self.predict_with_uncertainty(state, action)
        
        # 保守估计: 均值 + 3*标准差 (约99.7%置信度)
        conservative_state = mean + safety_margin * std
        
        return self.is_safe(conservative_state)
```

## 应用场景

### 1. 神经假肢控制

```python
def neural_prosthesis_safety_filter(neural_activity, desired_movement):
    """
    神经假肢的安全滤波控制
    
    从神经解码的运动意图中确保安全
    """
    # 神经解码器（不确定性已建模）
    decoder = ProbabilisticNeuralDecoder()
    
    # 解码带不确定性的运动意图
    movement_mean, movement_uncertainty = decoder.decode(neural_activity)
    
    # 安全滤波器
    safety_filter = UncertaintyAwareSafetyFilter(
        dynamics_model=ProsthesisDynamics(),
        safety_constraints=[
            joint_limit_constraints,
            velocity_constraints,
            collision_avoidance
        ]
    )
    
    # 滤波控制
    safe_control = safety_filter.filter_control(
        nominal_control=movement_mean,
        current_state=get_prosthesis_state(),
        uncertainty=movement_uncertainty
    )
    
    return safe_control
```

### 2. 脑机接口安全

```python
def bci_safety_monitor(neural_signals, intended_action):
    """
    BCI系统的安全监控
    
    确保解码的意图不会导致危险行为
    """
    # 不确定性估计
    uncertainty_model = NeuralUncertaintyEstimator()
    action_uncertainty = uncertainty_model.estimate(neural_signals)
    
    # 如果不确定性太高，拒绝控制
    if action_uncertainty > UNCERTAINTY_THRESHOLD:
        return SAFE_DEFAULT_ACTION, "HIGH_UNCERTAINTY"
    
    # 安全验证
    safety_checker = BCISafetyChecker()
    is_safe = safety_checker.check(intended_action, action_uncertainty)
    
    if not is_safe:
        return SAFE_DEFAULT_ACTION, "SAFETY_VIOLATION"
    
    return intended_action, "APPROVED"
```

### 3. 自主医疗系统

```python
def medical_robot_safety_control(patient_state, target_procedure):
    """
    医疗机器人的安全控制
    """
    # 患者状态的不确定性（来自生理监测）
    state_uncertainty = estimate_patient_state_uncertainty(patient_state)
    
    # 安全滤波器
    safety_filter = UncertaintyAwareSafetyFilter(
        confidence_level=0.99  # 医疗应用需要更高置信度
    )
    
    # 生成安全控制
    safe_procedure = safety_filter.filter_control(
        nominal_control=target_procedure,
        current_state=patient_state,
        state_uncertainty=state_uncertainty
    )
    
    return safe_procedure
```

## 评估指标

```python
def evaluate_safety_filter(safety_filter, test_scenarios):
    """
    评估安全滤波器性能
    """
    results = {
        'safety_rate': [],
        'intervention_rate': [],
        'performance_degradation': []
    }
    
    for scenario in test_scenarios:
        nominal_controls = scenario['nominal_controls']
        filtered_controls = []
        violations = 0
        
        for t, u_nom in enumerate(nominal_controls):
            u_safe = safety_filter.filter_control(
                u_nom, scenario['states'][t]
            )
            filtered_controls.append(u_safe)
            
            # 检查名义控制是否安全
            if not safety_filter.is_safe(scenario['states'][t], u_nom):
                violations += 1
        
        results['safety_rate'].append(1 - violations / len(nominal_controls))
        results['intervention_rate'].append(
            sum(u1 != u2 for u1, u2 in zip(nominal_controls, filtered_controls)) 
            / len(nominal_controls)
        )
        results['performance_degradation'].append(
            compute_performance_loss(scenario, filtered_controls)
        )
    
    return results
```

## 触发词

- 不确定性感知安全滤波
- 预测安全滤波器
- 机会约束控制
- 概率神经网络动力学
- Tube-based MPC
- 神经假肢安全
- BCI安全监控
- 安全关键神经控制

## 依赖

```bash
pip install torch numpy scipy cvxpy
```

## 参考文献

Frauenknecht, B., Kesper, L., & Mayfrank, D. (2026). Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics. arXiv:2604.26836.

## 相关技能

- neural-digital-twins-bci
- bci-rehabilitation-protocols
- mpc-drl-autonomous-driving
- formal-guaranteed-control-adaptation
