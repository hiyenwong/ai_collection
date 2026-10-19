---
name: contest-envelope-codesign
category: systems-engineering
description: Control+estimation co-design via dual-variable gradients.
trigger_words: control co-design, estimation co-design, sensor placement, actuator placement, bilevel design optimization, envelope theorem, SDP dual gradient, LQG co-design, H-infinity design, sensor selection, plant controller co-optimization, information architecture design
---

# ContEst: Control and Estimation Co-Design via Envelope-Theorem Gradients

Source: Ramadan, Dinenis, Anitescu (Argonne National Lab), arXiv:2609.36090, submitted to Automatica.

## Core Idea

传统工程采用 plant → control → estimator 串行设计流水线，每阶段限制下一阶段，**一般不是联合最优**。ContEst 将执行机构参数 θf 与传感/估计参数 θh 放入单一**两阶段优化**：

```
Design (first stage):   min_θ  J(θ) = J_des(θ) + J_sc*(Z₀; θ),   θ ∈ Θ
Control (second stage): J_sc*(Z₀; θ) = min_κ  E[ Σ ℓ(x_k, u_k) ]   (随机最优控制/对偶控制)
```

关键：输出反馈下成本依赖**信息状态**（滤波密度 p(x_k|Z_k)），而非未观测状态，因此优化同时改进控制器与估计器。

## Key Enabler: Envelope-Theorem Gradients（免微分求解器）

内层最优值对设计参数的梯度**直接从内层求解器已返回的对偶变量读出**：

```
∇_θ J*(θ) = ∇_θ L(z*, μ*, S*, θ) = ∂_θ J + ⟨μ*, ∂_θ g⟩ − ⟨S*, ∂_θ G⟩
```

- **无需**对优化器本身微分，**无需**隐式微分 KKT 系统。
- 复杂度对比：KKT 隐式微分每个方向导数 O(rx⁶)（rx=状态维数）；包络路线整个梯度 O(rx²)。

### 正则条件 (Assumption 1)
- (A.I) 内层对 z 凸，数据 C¹，Slater 条件成立 → 强对偶
- (A.II) 原始最小点 z*(θ) 唯一
- (A.III) 原始-对偶非退化且严格互补 → 对偶唯一
- (A.IV) θ 只通过有限数据对象 D(θ)（如 A_θ,B_θ,C_θ）进入，且 C¹

**优雅降级**：当 (A.II)/(A.III) 失败但原始或对偶解仍唯一时，返回的对偶仍构造 **Clarke 次梯度**（提供下降方向 + 平稳性证书 0 ∈ ∂J*）——方法退化但不崩溃。

### LQG 情形的正则性判据（实用）
可控 + 可观 + 权重正定 ⇒ 包络定理可用（stabilizable/detectable + Q,R,W,V ≻ 0 ⇒ Slater、原始唯一、严格互补）。

## 三个内层变体

### 1. LQG (H₂)：控制/估计 SDP 对
控制 SDP（Lyapunov LMI，变量 Σ,L）与估计 SDP 是**互为转置对偶**，在替换 (A,B,Q,R,W) → (Aᵀ,Cᵀ,W,V,Q) 下。梯度 Jacobian 从 LMI 对偶块读出：
```
∂J_cont/∂A_θ = 2 S₂*[1,1] Y*,   ∂J_cont/∂B_θ = 2 S₂*[1,1] (L*)ᵀ
∂J_est/∂C_θ = 2 F*ᵀ S̃₂*[1,2]
```
再经链式法则 ∇_θ J = Σ (∂J/∂A_θ)(∂A_θ/∂θ_i) 组装。

### 2. H∞（最坏情况）：有界实引理 SDP
- **最小-γ 问题：对偶在退化面上集值，只有次梯度**。
- **修复**：固定 γ 严格高于最优衰减（fixed-γ + epigraph slack T）→ 严格可行、非退化、严格互补 → **精确梯度**。Schur 补 slack T ⪰ W_θ^{1/2} Y⁻¹ W_θ^{1/2} 使 tr(T) 精确上界估计方差。

### 3. 非线性系统：eKF–MPC 代理（近似）
信息状态 (x_{k|k}, Σ_{k|k}) 经 eKF 传播 → 对信息状态动力学局部线性化 → 凸 MPC；设计"梯度"从动力学 costates（伴随变量）读出。**多层近似 ⇒ 非精确梯度**，但数值验证有效。

## 建模灵活性（SDP 路线的价值）
- LMI 正则化：trace/核范数惩罚 → 稀疏执行/传感
- 预算约束与 ℓ1 传感器选择松弛（对偶价格"必要传感器"）
- 多面体（凸包）不确定性集上的二次型稳定性
- 结构化增益模式 / 掩码协方差
- 任何附加凸锥可表示成分，只要增广后仍满足 Assumption 1，精确梯度机制全部继承（Remark 5）

## 验证结果（4 个案例研究）
| 研究 | 内层 | J_est↓ | J_sc↓ |
|------|------|--------|-------|
| 航天器姿态确定与控制 ADCS | H₂+H∞ | 42.7% | 18.3% |
| 二元精馏塔 | eKF-MPC | 35.3% | 5.6% |
| 低惯量电网 PLL/DSE 调参 | eKF-MPC | 17.6% | 39.5% |
| 多端 HVDC 环稀疏传感 | blockdiag H∞ | 31.8% | 33.4% |

HVDC 案例亮点：协同设计的 droop 增益 + 仅 4 个传感器即可接近固定 droop 基线 15 个传感器的估计质量（**砍掉 73% 电压遥测**）——纯传感器选择方法无法表述此权衡，因为 droop 重塑了估计器需跟踪的动力学。

## Reusable Pattern（何时使用）
1. 任何"plant 参数 + 传感配置 + 执行配置"需联合权衡的系统设计（CPS、航天器、电网、过程系统）
2. 内层问题可凸化（LQG/H∞ LMI、凸 MPC 代理）且求解器返回对偶
3. 传感器布设以混合整数或 ℓ1 松弛进入设计变量
4. 与 MDO（多学科设计优化）架构兼容：ContEst 唯一外部输出是设计梯度，可与现有方法组合而非替换

## Pitfalls
- 最小-γ H∞ 内层：最优对偶集值 → 用 fixed-γ 恢复精确性
- eKF-MPC 路线的梯度是近似值，报告时需注明
- 基线对比：论文基线是"合理标称值"而非精调 SOTA， reductions 不代表超越最优调参
