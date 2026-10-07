---
name: mpc-taylor-lagrange-remainder-safety
description: Use when MPC safety constraints need exact Taylor-Lagrange remainder. Fewer tuning knobs than HOCBF.
category: ai_collection
metadata:
  arxiv_id: "2610.06976"
  published: "2026-10-03"
  authors: "Liu, Wu, Xiao, Drgona, Belta (BU/JHU/NTU/UMD)"
  source: "arXiv eess.SY"
---

# Taylor–Lagrange 余项 MPC：安全关键控制的新约束形式（MPC-TLR）

**论文**: "Model Predictive Control for Safety-Critical Systems Using Taylor's Theorem with Lagrange Remainder" (arXiv:2610.06976, Liu, Wu, Xiao, Drgoňa, Belta — Boston Univ / Johns Hopkins / NTU-MIT / Maryland, 2026-10)

## 核心发现

安全关键 MPC 的 barrier 约束（HOCBF/DHOCBF）随相对阶 m 增长引入多个 class-K 函数参数，调参困难且趋于保守。MPC-TLR 改用**精确 Taylor 展开加 Lagrange 积分余项**表达安全函数未来值：必要充分条件、无递归 class-K 函数、单一保守度旋钮 δ。

## TLR 核心公式（式 14，精确恒等式）

对相对阶 m 的安全函数 h(x)，ZOH 控制下：

```
h(x(t+Δt)) = Σ_{i=0}^{m-1} (Δt^i / i!) h^(i)(x(t))
           + ∫_t^{t+Δt} ((t+Δt−t_m)^{m-1} / (m-1)!) h^(m)(x(t_m), u(t)) dt_m
```

右端**恒等于** h(x(t+Δt))——安全条件 h(x(t+Δt))≥0 当且仅当右端非负（必要充分，非 CBF 的充分条件）。

## 数字化实现（三步）

1. **中间态采样**：将 [t, t+Δt] 分成 M+1 个子点 s_j = jΔt/M，用离散模型递推 x_{t,j+1} = F(x_{t,j}, u(t))
2. **数值求积近似余项**：`∫(...) ≈ Σ_j w_j · ((Δt−s_j)^{m-1}/(m-1)!) h^(m)(x_{t,j}, u(t))`
3. **可调安全裕度**：约束 `h̃(x(t+Δt)) ≥ δ`；若近似误差 |h−h̃| ≤ ε_M，则取 δ ≥ ε_M 即保证 h(x(t+Δt)) ≥ 0。δ 大 → 更保守；δ=0 → 名义近似

## MPC-TLR 优化问题（式 20）

标准有限时域 MPC（代价/动力学/状态输入约束不变），仅把每步安全约束替换为：

```
Σ_{i=0}^{m-1} (Δt^i/i!) h^(i)(x_{t+k}) + Σ_j w_j ((Δt−s_j)^{m-1}/(m-1)!) h^(m)(x_{t+k,j}, u_{t+k}) ≥ δ
```

复杂度：每步约 N(M+1) 个额外非线性函数求值；问题非凸，用 SQP/内点法局部最优。

## 与三种基线的系统对比（本文最有价值的分析，Remark 2）

| 方法 | 安全约束进入的控制输入数 | 调参量 | 特点 |
|------|------|------|------|
| MPC-DC（直接 h(x)≥0） | N−m_d+1（延迟 m_d 步才受控）| 1 (δ) | 最简单但短时域盲区 |
| MPC-DHOCBF | N−m_d+1（前向差分同样截断时域）| m 个 γ_i | 离散域构造 |
| **MPC-TLR** | **N（全部）** | **1–2 (δ, M)** | 连续域导出+余项显式 |
| MPC-HOCBF | N（全部）| m 个 k_i | 最安全但最保守 |

**关键洞察**：当预测时域 N 与离散相对阶 m_d 相当（短时域实时控制），TLR/HOCBF 的"全输入覆盖"显著改善可行性与安全性；N≫m_d 时四者差异消失。

## 实验结果（unicycle 避障, m=2, Δt=0.1s, IPOPT）

- **安全性排序**：MPC-HOCBF（最大间隙、零违反）> **MPC-TLR**（三方法中最大最小间隙）> MPC-DHOCBF ≈ MPC-DC（均出现 inter-sampling 违反）
- **短时域 N=4 高权重场景**：TLR 与 HOCBF 保持障碍外，DHOCBF 与 DC 进入不安全区
- **可行性率**：TLR 高于 HOCBF（更不保守）；MPC-HOCBF 在 N=12 出现中途不可行
- **计算时间**：TLR 求解时间与 HOCBF 同量级（12.704 vs 10.351 s @ 某设置），非数值近似未带来数量级开销

## 理论诚实边界

- TLR 约束是**数值近似**（vs 基线的"精确"约束形式）；但四者都用离散预测模型作用于连续系统，**没有任何一个**对连续时间闭环提供无误差安全保证——离散化误差是共同软肋
- inter-sampling 安全不保证（未来工作）；Δt 缩小或更高精度离散化可缓解

## 可复用模式

1. **用精确余项替代递归 class-K 链**：任何"h 及其导数可算"的安全/性能约束，都可以用 Taylor–Lagrange 恒等式写成必要充分形式，把 m 个调参压缩为 1 个裕度 δ
2. **近似误差→裕度换算**（式 19）：|h−h̃|≤ε_M ⇒ δ≥ε_M 保安全——通用的"数值方法进入形式化保证"桥梁
3. **控制输入覆盖度分析**：比较不同安全约束形式下"多少个决策变量显式进入约束"——短时域方法选型的快速判据
4. **约束复杂度预算**：N(M+1) 次额外非线性求值 vs 基线，选 M 时按求解器耗时实测而非理论估计

**Activation**: MPC safety, control barrier function, high-order CBF, Taylor-Lagrange remainder, safety-critical control, inter-sampling safety, zero-order hold, safety margin tuning, unicycle obstacle avoidance, receding horizon
