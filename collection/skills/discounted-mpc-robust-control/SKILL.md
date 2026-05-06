---
name: discounted-mpc-robust-control
description: "Discounted Model Predictive Control (MPC) and infinite-horizon optimal control under plant-model mismatch. Unified framework for stability and suboptimality analysis with robustness guarantees. Use for: robust MPC, plant-model mismatch handling, discounted optimal control, stability analysis, surrogate model control. Activation: discounted MPC, plant-model mismatch, robust MPC, infinite-horizon control, suboptimality analysis."
---

# Discounted MPC Robust Control

基于论文 "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality" (arXiv:2604.08521v1, 2026) 的鲁棒控制方法论。

## 核心贡献

该论文提出了一个统一的框架，用于分析在模型-植物不匹配情况下折扣MPC和无限时域最优控制的闭环稳定性和次优性。

### 主要创新点

1. **统一分析框架**: 基于二次成本分析有限和无限时域问题，涵盖折扣和非折扣场景
2. **鲁棒性保证**: 在状态和控制的植物-模型不匹配边界比例假设下，保证原点的指数稳定性
3. **次优性界限**: 提供闭环成本的次优性界限，恢复替代模型的最优成本
4. **权衡关系**: 揭示时域长度、折扣和植物-模型不匹配之间的权衡关系

## 理论基础

### 问题设置

考虑离散时间非线性系统:
```
x_{k+1} = f(x_k, u_k)  # 真实植物
```

使用替代模型进行预测:
```
x_{k+1} = f_hat(x_k, u_k)  # 替代模型
```

### 植物-模型不匹配假设

假设存在常数 ε_f, ε_V 使得:
```
||f(x,u) - f_hat(x,u)|| ≤ ε_f * ||(x,u)||
```

### 折扣成本函数

```
J_N(x, u) = Σ_{k=0}^{N-1} γ^k * l(x_k, u_k) + γ^N * V_f(x_N)
```

其中 γ ∈ (0,1] 是折扣因子

## 稳定性保证

### 定理1: 指数稳定性

在以下条件下:
1. 成本可控性 (cost-controllability)
2. 模型连续性
3. 终端成本V_f是控制李雅普诺夫函数

闭环系统在原点是指数稳定的。

### 鲁棒性特性

鲁棒性保证在时域长度上是均匀的，意味着:
- 更大的时域不需要连续更小的植物-模型不匹配
- 稳定性裕度与时域长度无关

## 次优性分析

### 性能界限

闭环成本 J_cl 满足:
```
J_cl ≤ J_opt + Δ
```

其中:
- J_opt 是替代模型的最优成本
- Δ 是与植物-模型不匹配相关的附加项

### 折扣因子的影响

折扣因子 γ 影响:
1. 稳定性区域大小
2. 次优性界限的紧致性
3. 对模型不匹配的敏感度

## 实际应用

### 场景1: 基于学习的MPC

当使用神经网络学习系统动力学时:
```python
# 学习得到的替代模型
f_hat = learned_dynamics(x, u)

# 应用折扣MPC
mpc = DiscountedMPC(
    model=f_hat,
    discount=0.95,
    horizon=N,
    mismatch_bound=ε_f
)
```

### 场景2: 自适应控制

在系统参数变化时:
```python
# 在线模型更新
f_hat = update_model(estimates)

# 保持稳定性保证
mpc.update_model(f_hat, mismatch_bound=new_bound)
```

### 场景3: 多速率控制

当模型在不同时间尺度上运行时:
```python
# 慢速模型更新
f_hat_slow = slow_update(x, u)

# 快速MPC执行
mpc = DiscountedMPC(
    model=f_hat_slow,
    discount=0.9,  # 较低折扣适应模型老化
    horizon=N_fast
)
```

## 设计指南

### 参数选择

1. **折扣因子 γ**:
   - 接近1: 长期性能优先，对不匹配更敏感
   - 较小: 短期性能优先，更鲁棒
   - 推荐: 0.9-0.99

2. **时域长度 N**:
   - 与稳定性保证无关
   - 影响计算复杂度
   - 根据实时约束选择

3. **植物-模型不匹配界限**:
   - 通过系统辨识或学习误差估计
   - 保守估计保证稳定性

### 实现注意事项

1. **终端成本设计**: 确保V_f是控制李雅普诺夫函数
2. **约束处理**: 考虑不匹配对约束满足的影响
3. **实时性**: 折扣降低了对长时域的需求

## 与其他方法比较

| 方法 | 鲁棒性 | 计算复杂度 | 适用场景 |
|------|--------|-----------|----------|
| 标准MPC | 低 | 中 | 精确模型 |
| Tube MPC | 高 | 高 | 有界不确定性 |
| **折扣MPC** | 中 | 中 | 模型不匹配 |
| 鲁棒MPC | 高 | 高 | 最坏情况保证 |

## 激活关键词

- discounted MPC
- plant-model mismatch
- robust MPC
- infinite-horizon control
- suboptimality analysis
- surrogate model control
- 折扣MPC
- 模型不匹配
- 鲁棒控制

## 相关技能

- `advanced-control-systems-2026`: 更广泛的控制系统方法论
- `mpc-stability-suboptimality`: MPC稳定性和次优性分析
- `system-resilience-design-patterns`: 系统弹性设计模式

## 参考文献

Moldenhauer, R.H., Worthmann, K., Postoyan, R., Nešić, D., & Granzotto, M. (2026). Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality. arXiv:2604.08521v1.
