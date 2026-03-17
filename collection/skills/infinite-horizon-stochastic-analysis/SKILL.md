---
name: infinite-horizon-stochastic-analysis
description: 无限视界随机系统分析方法论。核心思想：使用加权 L^p 空间、resolvent kernel 和测度变换处理无限时间跨度的随机优化问题。适用于长期决策、随机控制、无限视界规划。触发词：无限视界、随机系统、BSVIE、倒向随机 Volterra 积分方程、长期决策、infinite horizon、stochastic control、discounted problem。
---

# 无限视界随机分析

处理无限时间跨度的随机优化问题，解决传统方法无法处理的长期决策。

## 核心思想

无限视界问题的挑战：
1. **无终止条件** - 传统动态规划失效
2. **积分发散** - 需要适当的加权空间
3. **测度依赖** - 概率测度随时间演变

**解决方案**：
- 加权 L^p 空间处理积分收敛
- Resolvent kernel 分解长期依赖
- 测度变换处理概率演变

## 方法框架

### 1. 加权 L^p 空间

定义加权空间：
```
L^p_ρ([0,∞); R^n) = {f: ∫_0^∞ |f(t)|^p ρ(t) dt < ∞}
```

常用权函数：
- **指数权重**: ρ(t) = e^{-βt}, β > 0 (折扣因子)
- **多项式权重**: ρ(t) = (1+t)^{-α}, α > 1/p
- **混合权重**: 指数衰减 + 多项式尾

```python
# 验证函数在加权空间的可积性
def check_integrability(f, rho, p=2, T_max=100):
    """检查 f ∈ L^p_ρ"""
    t = np.linspace(0, T_max, 1000)
    integrand = np.abs(f(t))**p * rho(t)
    integral = np.trapz(integrand, t)
    return integral < np.inf
```

### 2. BSVIE (倒向随机 Volterra 积分方程)

一般形式：
```
Y(t) = ξ + ∫_t^∞ f(s, Y(s), Z(s, t)) ds - ∫_t^∞ Z(s, t) dW(s)
```

关键特性：
- **无限上界**: 积分上限为 ∞
- **Volterra 结构**: Z(s, t) 双参数
- **正则性**: Y, Z 在加权空间

### 3. Resolvent Kernel 方法

对于线性 BSVIE：
```
Y(t) = g(t) + ∫_t^∞ K(t, s)Y(s) ds
```

使用 Resolvent kernel R 解耦：
```
Y(t) = g(t) + ∫_t^∞ R(t, s)g(s) ds
```

计算方法：
```python
def resolvent_kernel(K, t, s, n_terms=100):
    """
    计算 Resolvent kernel R(t,s)
    R = K + K*K + K*K*K + ... (Neumann 级数)
    """
    R = K(t, s)  # 第一项
    K_composed = K(t, s)
    
    for _ in range(n_terms):
        # K 的复合积分
        K_composed = compose_kernel(K, K_composed, t, s)
        R = R + K_composed
    
    return R
```

### 4. 测度变换 (Girsanov)

处理概率测度依赖：
```
原测度: P
新测度: Q, dQ/dP = exp(∫_0^T θ_s dW_s - 0.5∫_0^T |θ_s|^2 ds)
```

在无限视界中：
```
dQ/dP = exp(∫_0^∞ θ_s dW_s^P - 0.5∫_0^∞ |θ_s|^2 ds)
       = exp(∫_0^∞ θ_s dW_s^Q + 0.5∫_0^∞ |θ_s|^2 ds)
```

应用：
```python
# 计算测度变换后的期望
def expectation_under_Q(f, theta, T_max, n_samples=10000):
    """在测度 Q 下计算 E[f]"""
    # 在测度 P 下采样
    W = np.cumsum(np.random.randn(n_samples, int(T_max*100)), axis=1) * 0.1
    dW = np.diff(W, axis=1)
    
    # 计算密度比
    log_ratio = np.sum(theta * dW - 0.5 * theta**2 * 0.01, axis=1)
    density_ratio = np.exp(log_ratio)
    
    # 加权期望
    return np.mean(f(W) * density_ratio)
```

## 应用场景

| 场景 | 方法组合 | 关键技术点 |
|------|----------|------------|
| 长期投资组合 | 加权空间 + 测度变换 | 风险中性定价 |
| 永续债券定价 | BSVIE + Resolvent | 无限久期现金流 |
| 退休金规划 | 指数折扣 + 随机控制 | 跨期消费优化 |
| 气候政策 | 多项式权重 + 不确定性 | 代际公平 |
| 机器维护 | 无限视界 MDP | 最优停止时间 |

## 实现要点

### 加权空间选择

| 目标 | 推荐权重 | 理由 |
|------|----------|------|
| 折扣问题 | e^{-βt} | 时间一致性 |
| 渐近稳定 | e^{-αt} | 保证有限值 |
| 长期平均 | (1+t)^{-α} | 允许非衰减解 |
| 不确定增长 | 混合权重 | 兼顾短期和长期 |

### Resolvent 计算技巧

```python
# 使用 Neumann 级数加速收敛
def resolvent_neumann_fast(K, t_grid, s_grid, tol=1e-10):
    """快速计算 Resolvent kernel"""
    n = len(t_grid)
    R = np.zeros((n, n))
    K_matrix = np.array([[K(t, s) for s in s_grid] for t in t_grid])
    
    K_current = K_matrix.copy()
    R = K_matrix.copy()
    
    max_iter = 1000
    for _ in range(max_iter):
        K_next = K_current @ K_matrix / n  # 离散卷积
        if np.max(np.abs(K_next)) < tol:
            break
        R += K_next
        K_current = K_next
    
    return R
```

### 无限视界截断

实际计算需要有限截断 T_max：
```python
def choose_truncation(rho, p=2, tol=1e-6):
    """选择合适的截断时间"""
    # 使尾积分 < tol
    # ∫_T^∞ ρ(t) dt < tol
    if isinstance(rho, str) and rho.startswith('exp'):
        beta = float(rho.split('-')[1])
        return -np.log(tol) / beta
    elif isinstance(rho, str) and rho.startswith('poly'):
        alpha = float(rho.split('-')[1])
        return (tol * (alpha - 1))**(1/(1-alpha))
    return 100  # 默认值
```

## 参数调优指南

| 参数 | 推荐范围 | 影响 |
|------|----------|------|
| 折扣因子 β | 0.01 ~ 0.1 | 太小收敛慢，太大忽略长期 |
| 截断时间 T_max | 根据权重选择 | 精度 vs 计算成本 |
| Neumann 级数项数 | 100 ~ 1000 | 精度 vs 计算时间 |
| 测度变换参数 θ | 问题依赖 | 需满足 Novikov 条件 |

## 与其他方法的对比

| 方法 | 适用问题 | 优点 | 缺点 |
|------|----------|------|------|
| 有限视界近似 | 快速估计 | 简单直接 | 遗漏长期效应 |
| 折扣动态规划 | 马尔可夫问题 | 结构清晰 | 需要指数折扣 |
| BSVIE 方法 | 一般随机问题 | 通用性强 | 计算复杂 |
| 平均成本准则 | 稳态问题 | 无折扣偏好 | 不适用于瞬态 |

## 参考文献

- Backward Stochastic Volterra Integral Equations (BSVIE) on Infinite Horizon
- Weighted L^p Spaces for Infinite Horizon Problems
- Resolvent Kernels and Volterra Equations
- Girsanov Theorem for Infinite Time Horizon