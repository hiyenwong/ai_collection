---
name: discounted-mpc-robust-control
description: "Discounted Model Predictive Control (MPC) robustness analysis under plant-model mismatch. Unified framework for stability and suboptimality guarantees with discounted/undiscounted costs, finite/infinite horizons. Activation: discounted MPC, plant-model mismatch, robust control, infinite-horizon optimal control."
category: systems-engineering
---

# Discounted MPC Robust Control Under Plant-Model Mismatch

基于论文 "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality" (Moldenhauer et al., 2026) 的方法论技能。

## 核心思想

研究在使用代理模型(surrogate model)求解MPC和无限视界最优控制时，当代理模型与真实系统(plant)存在不匹配情况下的闭环稳定性和次优性。基于二次成本的统一框架分析有限和无限视界问题，涵盖折扣和非折扣场景。

## 关键贡献

1. **统一分析框架**
   - 同时处理折扣(γ < 1)和非折扣(γ = 1)成本
   - 同时处理有限视界(N < ∞)和无限视界(N = ∞)
   - 基于二次成本的Lyapunov稳定性分析

2. **模型不匹配鲁棒性**
   - 比例边界假设：|f(x,u) - g(x,u)| ≤ p̄(|x| + |u|)
   - 保证指数稳定性（在成本可控性条件下）
   - 次优性边界恢复代理模型的最优成本

3. **三参数权衡**
   - 视界长度 N
   - 折扣因子 γ
   - 模型不匹配程度 |f-g|ₛ

## 理论基础

### 系统模型

**真实系统 (Plant):**
```
x⁺ = g(x, u)
```

**代理模型 (Surrogate):**
```
x⁺ = f(x, u)
```

### 比例模型不匹配

```
|f - g|ₛ := inf{p̄ ≥ 0: |f(x,u) - g(x,u)| ≤ p̄(|x| + |u|) ∀x ∈ 𝒮, u ∈ 𝕌}
```

### 最优控制问题 (OCP)

```
min Jᵧ,ₙᶠ(x, uₙ) = Σₖ₌₀ᴺ⁻¹ γᵏ ℓ(φᶠ(k,x,uₖ), uₖ)

其中 ℓ(x,u) = xᵀQx + uᵀRu （二次阶段成本）
```

### B-成本可控性

```
V₁,∞ᶠ(x) ≤ B‖x‖²_Q ∀x ∈ ℝⁿ
```

其中 B ≥ 1，保证存在控制序列使成本有界。

## 主要结果

### 定理1：稳定性和次优性

在满足以下条件时：
- f 是 L-Lipschitz连续的
- 满足B-成本可控性
- 模型不匹配 |f-g|ₛ < ∞

如果视界长度 N 和折扣因子 γ 满足：
```
Aᵧ,ₙᶠ,ᵍ < 1
```

其中：
```
Aᵧ,ₙᶠ,ᵍ = 1 + (1/γ)(1 - γ + Be^(-N/B) + κ̃ᵧ(|f-g|ₛ) - 1/B)
```

则：

1. **指数稳定性**：原点是闭环差分包含的指数稳定平衡点
   ```
   ‖xₖ‖_Q ≤ √B · (Aᵧ,ₙᶠ,ᵍ)^(k/2) · ‖x₀‖_Q
   ```

2. **次优性边界**：
   ```
   αᵧ,ₙᶠ,ᵍ · J̄ᵧ,∞ᵍ(x, 𝒰ᵧ,ₙᶠ(x)) ≤ Vᵧ,ₙᶠ(x)
   ```

### 关键优势

与现有文献[20, 17]相比：
- 允许 N = ∞（无限视界）
- 允许 γ < 1（折扣）
- **视界无关边界**：鲁棒性保证不随N增加而恶化
- 更大的N不需要更小的模型不匹配

## 实际应用

### 数据驱动控制

当使用以下方法获得代理模型时：
- 核扩展动态模态分解 (Kernel EDMD)
- Koopman算子理论
- 神经网络近似

### 参数不确定性处理

适用于以下场景：
- 外部扰动
- 参数不确定性
- 数值离散化误差
- 简化模型用于计算可行性

### 强化学习集成

折扣成本(γ < 1)在RL中广泛使用：
- 缓解预测误差累积
- 改善数值特性
- 与MPC稳定性分析结合

## 实现步骤

### 步骤1：验证成本可控性

```python
def verify_cost_controllability(f, Q, R, x_samples):
    """
    验证B-成本可控性假设
    
    对于采样状态x，计算V_1,∞^f(x)并验证V ≤ B‖x‖²_Q
    """
    B_values = []
    for x in x_samples:
        V = compute_value_function(f, Q, R, x, gamma=1, N=1000)
        x_norm_Q = np.sqrt(x.T @ Q @ x)
        B_values.append(V / (x_norm_Q ** 2))
    
    B_max = max(B_values)
    return B_max, B_max >= 1
```

### 步骤2：估计模型不匹配

```python
def estimate_plant_model_mismatch(f, g, S, n_samples=1000):
    """
    在状态空间S上估计|f-g|_S
    
    采样状态-控制对，计算max |f(x,u) - g(x,u)| / (|x| + |u|)
    """
    max_ratio = 0
    for _ in range(n_samples):
        x = sample_state(S)
        u = sample_control()
        mismatch = np.linalg.norm(f(x,u) - g(x,u))
        norm_xu = np.linalg.norm(x) + np.linalg.norm(u)
        if norm_xu > 0:
            ratio = mismatch / norm_xu
            max_ratio = max(max_ratio, ratio)
    
    return max_ratio
```

### 步骤3：计算稳定性条件

```python
def compute_stability_parameters(B, L, gamma, N, mismatch):
    """
    计算稳定性参数A和α
    """
    # 计算κ̃_γ
    if gamma * L**2 < 1:
        K_gamma = 1 / (1 - gamma * L**2)
        M_gamma = B / (1 - gamma * (1 - 1/B) * L)
    else:
        K_gamma = (1 - (gamma * L**2)**N) / (1 - gamma * L**2)
        M_gamma = B * (1 - (gamma * (1 - 1/B) * L)**N) / (1 - gamma * (1 - 1/B) * L)
    
    kappa_gamma_N = lambda s: K_gamma * s**2 + 2 * M_gamma * s
    
    # 缩放因子
    scale = (1/lambda_min(Q) + B/lambda_min(R)) * lambda_max(Q) * gamma / B
    kappa_tilde = kappa_gamma_N(scale * mismatch)
    
    # 计算A
    A = 1 + (1/gamma) * (1 - gamma + B * np.exp(-N/B) + kappa_tilde - 1/B)
    
    # 计算α
    alpha = 1 - B**2 * np.exp(-N/B) - B * kappa_tilde
    
    return A, alpha
```

### 步骤4：设计控制器

```python
def design_robust_mpc_controller(f, g, Q, R, gamma, N, B, L):
    """
    设计具有鲁棒性保证的MPC控制器
    """
    mismatch = estimate_plant_model_mismatch(f, g, S)
    A, alpha = compute_stability_parameters(B, L, gamma, N, mismatch)
    
    if A >= 1:
        # 需要调整参数
        # 选项1：增加N
        # 选项2：增加γ
        # 选项3：减小模型不匹配
        raise ValueError(f"稳定性条件不满足: A={A:.4f} >= 1")
    
    if alpha <= 0:
        raise ValueError(f"次优性条件不满足: α={alpha:.4f} <= 0")
    
    # 返回控制器配置
    return {
        'gamma': gamma,
        'N': N,
        'A': A,
        'alpha': alpha,
        'stability_rate': np.sqrt(A),
        'suboptimality_factor': 1/alpha
    }
```

## 参数选择指南

### 折扣因子 γ

- **γ → 1**：更关注长期性能，稳定性更容易保证
- **γ < 1**：减轻预测误差累积，数值特性更好
- **临界值**：γ > 1 - 1/B 保证稳定性（当N=∞, f=g时）

### 视界长度 N

- **N > 2B log(B)**：无折扣、精确模型时的最小值
- **更大N**：提供更多余地容纳折扣和模型不匹配
- **无限视界(N=∞)**：不需要终端约束

### 模型不匹配 |f-g|ₛ

- 必须足够小以满足 A < 1
- 与γ和N存在权衡关系
- 可通过更多数据改善（数据驱动场景）

## 与其他方法的关系

| 方法 | 终端约束 | 视界要求 | 模型不匹配处理 |
|------|----------|----------|----------------|
| 终端成本/约束 | 需要 | 短视界可行 | 特定条件下有结果 |
| 长视界MPC | 不需要 | 需要长视界 | 本方法核心 |
| 本方法 | 不需要 | 灵活(有限/无限) | 统一框架，视界无关边界 |

## 数值示例

考虑非线性系统：
```
x⁺ = g(x, u) = [x₂, -sin(x₁) + u]ᵀ
```

代理模型（线性化）：
```
x⁺ = f(x, u) = [x₂, -x₁ + u]ᵀ
```

在x=0附近，模型不匹配与|x|成正比，满足比例边界假设。

通过选择：
- B = 10（成本可控性常数）
- γ = 0.95
- N = 50

可以保证A < 1和α > 0，实现指数稳定和次优性边界。

## 触发词

- discounted MPC
- plant-model mismatch
- robust MPC
- infinite-horizon optimal control
- 折扣MPC
- 模型不匹配
- 鲁棒模型预测控制
- 无限视界控制

## 相关技能

- **density-driven-optimal-control**: 多智能体系统密度驱动最优控制
- **mpc-stability-suboptimality**: MPC稳定性和次优性分析
- **discounted-mpc-control**: 折扣MPC控制基础

## 参考文献

Moldenhauer, R. H., Worthmann, K., Postoyan, R., Nešić, D., & Granzotto, M. (2026). Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality. arXiv:2604.08521 [math.OC].

## 实现注意事项

1. **Lipschitz常数L**：需要估计代理模型f的Lipschitz常数
2. **成本可控性B**：可通过求解Lyapunov方程或采样验证
3. **数值稳定性**：当γᴸ²接近1时，Kᵧ,ₙ可能很大
4. **水平集**：稳定性保证在Vᵧ,ₙᶠ的最大水平集内有效

## 扩展方向

- 随机系统扩展
- 时变系统
- 分布式MPC
- 与机器学习模型的集成
- 在线模型更新和自适应
