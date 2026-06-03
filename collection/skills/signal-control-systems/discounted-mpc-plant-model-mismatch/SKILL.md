---
name: discounted-mpc-plant-model-mismatch
description: "Discounted MPC under plant-model mismatch - stability and suboptimality analysis for infinite-horizon optimal control with surrogate models. Activation: MPC, model predictive control, plant-model mismatch, robustness, stability, discounted control."
---

# Discounted MPC under Plant-Model Mismatch

## Paper Information

**Title:** Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality  
**Authors:** Robert H. Moldenhauer, Karl Worthmann, Romain Postoyan, Dragan Nešić, Mathieu Granzotto  
**arXiv:** https://arxiv.org/abs/2604.08521v1  
**Published:** 2026-04-09  
**Category:** math.OC (Optimization and Control), eess.SY (Systems and Control)

## Core Problem

如何在使用**替代模型**(surrogate model)求解模型预测控制(MPC)和无限时域最优控制问题时，保证闭环系统的**稳定性**和**次优性**，即使替代模型与真实被控对象之间存在不匹配?

## Key Contributions

### 1. Unified Framework
- 基于**二次型代价**的统一框架
- 同时分析有限时域和无限时域问题
- 涵盖折扣(discounted)和非折扣(undiscounted)场景

### 2. Stability Guarantees
**假设条件:**
- 植物与模型之间的不匹配与状态和控制成比例
- 原点保持为平衡点
- 模型连续且代价可控

**结论:**
- 在上述条件下，闭环系统**指数稳定**
- 鲁棒性保证对时域长度一致，即更长的时域不要求更小的模型不匹配

### 3. Suboptimality Bounds
- 给出了闭环代价的次优性界
- 恢复了替代模型的最优代价
- 揭示了**时域长度、折扣因子和模型不匹配之间的权衡关系**

## Mathematical Framework

### Plant-Model Mismatch Model
```
真实系统: x+ = f(x, u) + Δf(x, u)
替代模型: x+ = g(x, u)
```
其中 `Δf(x,u)` 表示模型不匹配，假设满足:
```
||Δf(x, u)|| ≤ σ_x||x|| + σ_u||u||
```

### Stability Analysis
关键工具:
- Lyapunov 函数
- 输入到状态稳定性 (ISS)
- 小增益定理

### Suboptimality Analysis
```
V_N(x) ≤ V_∞*(x) + bound(ε, N, γ)
```
其中:
- `V_N` 是 N 步 MPC 代价
- `V_∞*` 是无限时域最优代价
- `ε` 是模型不匹配参数
- `γ` 是折扣因子

## Key Insights

### 1. Horizon Robustness
**重要发现:** 更长的预测时域不需要更小的模型不匹配来维持稳定性
- 这与直觉相反
- 提供了实际设计的灵活性

### 2. Discount Factor Trade-off
折扣因子的影响:
- **较小的折扣因子:** 更关注近期性能，但对模型误差更敏感
- **较大的折扣因子:** 更接近无限时域，需要更精确的模型

### 3. Model Mismatch Bounds
模型不匹配的可容忍范围:
- 与代价可控性相关
- 与系统稳定性裕度相关
- 可以显式计算

## Practical Implications

### 1. Controller Design
使用替代模型时的设计指南:
1. 确保模型连续性和代价可控性
2. 验证模型不匹配在允许范围内
3. 根据性能要求选择合适的时域长度
4. 考虑折扣因子对鲁棒性的影响

### 2. Model Reduction
该框架可以用于:
- 降阶模型的设计
- 近似模型的选择
- 计算复杂度与性能的权衡

### 3. Adaptive Control
为自适应 MPC 提供理论基础:
- 在线模型更新的稳定性保证
- 模型改进的量化指标

## Related Work

- Classic MPC stability: Mayne et al. (2000)
- Robust MPC: Bemporad & Morari (1999)
- Model mismatch:近来更多关注，但缺乏系统性框架

## Limitations & Future Directions

### Current Limitations
1. 假设原点为平衡点 (可扩展到跟踪问题)
2. 二次型代价 (可扩展到一般凸代价)
3. 比例型的模型不匹配 (可考虑更一般的形式)

### Future Research
1. 非线性系统的扩展
2. 约束处理
3. 分布式 MPC 中的应用
4. 学习型 MPC 中的应用

## Key Equations

### Stability Condition
```
α1(||x||) ≤ V_N(x) ≤ α2(||x||)
V_N(f(x, κ_N(x))) - V_N(x) ≤ -α3(||x||) + ε·σ(x)
```

### Suboptimality Bound
```
J(x, κ_N) ≤ J*(x) · (1 + δ(ε, N))
```
其中 `δ(ε, N)` 是关于模型不匹配 ε 和时域 N 的函数。

## Code Example (Conceptual)

```python
class DiscountedMPC:
    def __init__(self, model, horizon, discount):
        self.model = model  # surrogate model
        self.N = horizon
        self.gamma = discount
        
    def solve(self, x0):
        """Solve MPC with surrogate model"""
        # Optimize over control sequence
        u_opt = self._optimize(x0)
        # Apply first control
        return u_opt[0]
    
    def check_stability(self, mismatch_bound):
        """Verify stability condition"""
        # Check if mismatch is within allowable range
        return mismatch_bound < self._compute_tolerance()
```

## References

1. Mayne, D. Q., et al. (2000). Constrained model predictive control: Stability and optimality. Automatica.
2. Rawlings, J. B., & Mayne, D. Q. (2017). Model predictive control: Theory and design.
3. Grüne, L., & Pannek, J. (2017). Nonlinear model predictive control.

## Summary

这篇论文为**模型不匹配下的 MPC** 提供了一个统一的理论框架，证明了即使使用不完美的替代模型，也能保证闭环系统的稳定性和可量化的次优性。关键贡献是揭示了时域长度、折扣因子和模型不匹配之间的权衡关系，为实际控制器设计提供了理论基础。

该工作是控制系统理论和系统工程的重要进展，特别是在以下场景中具有重要应用:
- 复杂系统的降阶控制
- 自适应和学习的 MPC
- 计算资源受限的实时控制
- 模型不确定性较大的系统

---

_Skill generated from arXiv:2604.08521v1 on 2026-04-10_