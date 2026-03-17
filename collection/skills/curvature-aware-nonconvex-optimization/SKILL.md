---
name: curvature-aware-nonconvex-optimization
description: 曲率感知的非凸优化方法论。核心思想：将二阶几何信息（曲率/海森矩阵特征值）显式纳入优化目标或约束，帮助逃逸鞍点、加速收敛。触发词：非凸优化、鞍点逃逸、曲率感知、CRGD、信赖域、二阶方法、Hessian-aware、escape saddle point、non-convex optimization。
---

# 曲率感知非凸优化

## Description

将二阶几何障碍显式写进目标函数，利用曲率信息指导优化方向，解决鞍点停滞问题。

## Activation Keywords

- 非凸优化
- 鞍点逃逸
- 曲率感知
- CRGD
- 信赖域
- 二阶方法
- Hessian-aware
- escape saddle point
- non-convex optimization

## Tools Used

- exec
- read
- write

## Instructions for Agents

当用户遇到非凸优化或鞍点问题时：

1. **诊断问题**：判断是否存在鞍点停滞（梯度小但非极小点）
2. **选择方法**：根据问题规模选择 CRGD、信赖域或 Hessian-free 方法
3. **实现曲率估计**：推荐 Hessian-vector product 方法
4. **调参指导**：根据问题特性推荐曲率正则化强度和阈值
5. **验证逃逸**：确认优化器成功离开鞍点区域

## Examples

User: 我的神经网络训练在某个 loss 值卡住了，梯度很小但 loss 不低。

Agent: 这可能是鞍点停滞。建议使用曲率感知方法：
1. 计算 Hessian 最小特征值，确认是否存在负曲率方向
2. 如果存在负曲率，沿负特征向量方向添加扰动逃逸鞍点
3. 可以使用 PyTorch 的 `torch.autograd.grad` 实现 Hessian-vector product

## 核心思想

传统一阶方法（如 SGD、Adam）在鞍点附近收敛缓慢甚至停滞。曲率感知方法通过：
1. **显式利用 Hessian 信息** - 检测曲率方向
2. **修改目标函数** - 惩罚平坦区域
3. **自适应步长** - 根据曲率调整探索强度

## 方法框架

### 1. 曲率惩罚目标函数

将原问题 min f(x) 转化为：
```
min f(x) + λ * curvature_penalty(x)
```

常用曲率惩罚：
- **Hessian 迹惩罚**: trace(H)^2
- **特征值惩罚**: Σ |λ_i|^p for p ∈ (0,1)
- **负曲率方向惩罚**: 沿负特征值方向加速

### 2. CRGD (Curvature-Regularized Gradient Descent)

```
输入: f, 初始点 x_0, 学习率 η, 正则化强度 λ
输出: 近似局部极小点

for t = 1, 2, ..., T:
    g_t = ∇f(x_t)
    H_t = ∇²f(x_t) 或其估计
    
    # 计算曲率感知方向
    if min(eig(H_t)) < -ε:  # 负曲率（鞍点）
        d_t = -v_neg * α  # 沿负特征向量方向
    else:
        d_t = -g_t  # 正常梯度下降
    
    x_{t+1} = x_t + η * d_t
```

### 3. 随机化信赖域方法

```
输入: f, 初始点 x_0, 初始半径 Δ_0
输出: 局部极小点

for t = 1, 2, ..., T:
    # 在信赖域内求解子问题
    min_{‖s‖ ≤ Δ_t} m_t(s) = f(x_t) + g_t^T s + 0.5 s^T H_t s
    
    # 随机化探索
    if improvement_ratio < threshold:
        x_{t+1} = x_t + noise  # 添加探索噪声
        Δ_{t+1} = expand(Δ_t)
    else:
        x_{t+1} = x_t + s*
        Δ_{t+1} = adjust(Δ_t, improvement_ratio)
```

## 应用场景

| 场景 | 适用性 | 关键参数 |
|------|--------|----------|
| 深度学习训练 | ★★★★★ | Hessian-free 近似 |
| 神经网络初始化 | ★★★★☆ | 负曲率检测阈值 |
| 强化学习策略优化 | ★★★★☆ | 信赖域半径 |
| 推荐系统矩阵分解 | ★★★☆☆ | 曲率正则化强度 |
| 机器人轨迹优化 | ★★★★☆ | 约束处理策略 |

## 实现要点

### Hessian 估计方法

1. **有限差分**: O(n) 梯度评估，精度受限
2. **Hessian-vector product**: O(n) 复杂度，适用于大规模
3. **随机估计**: 采样子集特征值
4. **Neumann 展开**: 无需显式 Hessian

```python
# Hessian-vector product 示例 (PyTorch)
def hvp(f, x, v):
    grad = torch.autograd.grad(f, x, create_graph=True)
    hvp = torch.autograd.grad(grad, x, v)
    return hvp
```

### 鞍点逃逸检测

```python
def detect_saddle(H, threshold=-1e-6):
    """检测是否在鞍点附近"""
    eigenvalues = torch.linalg.eigvalsh(H)
    min_eig = eigenvalues.min()
    return min_eig < threshold
```

## 参数调优指南

| 参数 | 推荐范围 | 影响 |
|------|----------|------|
| 曲率正则化 λ | 1e-4 ~ 1e-2 | 太大导致欠拟合，太小效果弱 |
| 负曲率阈值 ε | -1e-6 ~ -1e-4 | 控制逃逸敏感度 |
| 信赖域初始半径 Δ_0 | 0.1 ~ 1.0 | 影响探索范围 |
| Hessian 估计精度 | 10 ~ 100 samples | 精度 vs 计算成本权衡 |

## 与其他方法的对比

| 方法 | 曲率利用 | 鞍点逃逸 | 计算成本 | 适用规模 |
|------|----------|----------|----------|----------|
| SGD | 无 | 慢 | O(n) | 大规模 |
| Adam | 一阶矩 | 中 | O(n) | 大规模 |
| Newton | 全 Hessian | 快 | O(n²) | 小规模 |
| CRGD | 部分曲率 | 快 | O(n·k) | 中大规模 |
| 信赖域 | 子问题 Hessian | 快 | O(n·k) | 中规模 |

## 参考文献

- CRGD: Curvature-Regularized Gradient Descent (2024)
- Stochastic Trust Region Methods for Non-convex Optimization
- Escape Saddle Points Efficiently via Negative Curvature Directions