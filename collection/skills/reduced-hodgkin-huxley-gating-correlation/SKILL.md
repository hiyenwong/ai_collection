---
name: reduced-hodgkin-huxley-gating-correlation
description: "Use when reducing HH neuron models or deriving AP propagation speed laws. 门控相关HH降维。"
category: neuroscience
metadata:
  arxiv_id: "2402.19185"
  published: "2024-02-29 (v3 2026-10-02, q-bio.CB)"
  authors: "Lízia Branco, Rui Dilão"
  source: "University of Lisbon, Instituto Superior Técnico — arXiv nlin.AO cross-list"
  tags: [hodgkin-huxley, model-reduction, gating-variables, sodium-potassium-correlation, action-potential-propagation, cable-equation, bifurcation-analysis, bautin-bifurcation, solitary-spike, axon-resistivity, computational-neuroscience, neuron-model]
---

# 基于 Na⁺/K⁺ 门控相关的 Hodgkin-Huxley 降维模型

**arXiv 2402.19185 v3** (2026-10-02 更新) — Branco & Dilão (里斯本大学)。利用 4D HH 模型中钠失活门 h 与钾激活门 n 的经验反相关 h ≃ c(I) − n，构造保持分岔结构与传播动力学的 3D/2D 降维模型，并推导动作电位传播速度的统一幂律 v = a/(C_m·R^b)。

## 核心洞察：门控变量相关（FitzHugh 1961 遗产）

4D HH 假设 Na⁺/K⁺ 门控独立，但解的轮廓显示 h(t) 近似镜像 n(t)（FitzHugh 1961, Rinzel 1985, Keener & Sneyd 1998, Wang et al. 2023 均注意到）。本文系统利用该相关性：

**c 是电流依赖的（对 FitzHugh 常数假说的修正）**：
```
c_3D(I) = 1.0        (I ≤ 1)
        = 1.0·I^−0.0674  (I > 1)
c_2D(I) = 1.0        (I ≤ 1)
        = 1.0·I^−0.078  (I > 1)
```
（μA/cm²；I=8 时 c_3D=0.86，I=100 时 c_3D=0.73——最小二乘拟合数值解）

## 降维模型

**3D 模型**（h → c(I)−n，保留 m 动力学）：
```
C_m dV/dt = I − g_K n⁴(V−V_K) − g_Na m³(c(I)−n)(V−V_Na)
dn/dt = α_n(V)(1−n) − β_n(V)n
dm/dt = α_m(V)(1−m) − β_m(V)m
```

**2D 模型**（进一步 m → m_∞(V)，因 m 时间尺度快）：
```
C_m dV/dt = I − g_K n⁴(V−V_K) − g_Na m_∞(V)³(c_2D(I)−n)(V−V_Na)
dn/dt = α_n(V)(1−n) − β_n(V)n
```
⚠️ 反向尝试失败：n → n_∞ 会导致无 Hopf 分岔、全部不动点稳定的退化模型——**n 必须保留动力学，m 才可绝热消去**（快慢时间尺度论证）。

## 分岔结构保持（Bautin 余维 2 场景）

| 参数 | 4D | 3D | 2D |
|------|----|----|----|
| I_SNLC | 3.15 | 3.16 | 2.61 |
| I₁ (subcritical Hopf) | 6.18 | 5.60 | 5.31 |
| I₂ (supercritical Hopf) | 159.20 | 153.32 | 153.13 |

- 三模型共享 **Bautin 余维 2 分岔组织**（Cano & Dilão 2017）：亚临界 Hopf I₁ → 不稳定 LC → SNLC（I 型间歇性区域 I_th < I < I₁，尖峰数 ln M = C − 2 ln(I_SNLC − I)）→ 稳定 LC 振荡区 [I₁, I₂−ε] → 超临界 Hopf I₂
- I₂ 附近 ε₁ ≈ 10⁻⁴ 内有 canard 解
- 振荡周期幂律拟合：per_4D = 32.96·I^−0.35 ms；per_3D = 34.23·I^−0.37；per_2D = 37.33·I^−0.49

## 空间扩展（cable 方程）与传播速度幂律

轴突 = N 段电压门控段 + 内阻 R 结点耦合，第二方程含轴向扩散项 D∂²V/∂x²，D = ℓ²/R，Neumann 边界：

**中心结果——传播速度幂律**：
```
v(R, C_m) ≃ a / (C_m · R^b)
b = 0.55 (4D), 0.52 (3D), 0.66 (2D)    [a>0, b<1]
```
- **速度对刺激强度 I 弱依赖**（I=20/100/140 拟合几乎不可区分：v_4D = 1.82~1.83·R^−0.54~0.63 mm/ms）——动作电位全或无的定量表达
- 幂律推导：固定 R 拟合 v = a₁(R)/C_m^{b₁}，得 b₁ ≈ 1.01~1.10（≈1，验证 Keener & Sneyd 理论预测）；a₁ 本身也是幂律 a₁ = 4.34/R^0.78 → 合并成统一两参数律
- **尖峰宽度**也随 R 幂律变化：w_2D = 9.0/R^0.76 mm

## 传播的存在性区间（新发现）

动作电位传播只在内阻区间 R ∈ [R_m0, R_M0] 内发生；其中更窄的 [R_m1, R_M1] ⊂ [R_m0, R_M0] 产生周期/近周期尖峰列，其余区间（R < R_m1 或 R_m1 < R < R_M0 边缘）只有**单个孤波尖峰**传播到突触前终端后轴突回到静息态：
- 4D：I=20 时振荡区 R ∈ [0.4, 10.0]；I=140 时 R ∈ [0.01, 1.4]
- 3D：R ∈ [0.1, 7.0] 孤波，v_3D = 1.81/R^0.52
- 2D：R ∈ [0.01, 4.6] 周期传播；R < 0.05 或 R > 4.6 单尖峰 + 稳态收敛

**反向传播与湮灭**：在轴突中段 x_e 注入电流（模拟 patch-clamp/分支输入）产生双向尖峰——一支与来自 soma 的信号对撞湮灭，另一支向突触前传播。到达突触前的信号可能"诞生于轴突中段"而非 soma（与 Cano & Dilão 2024 的 4D 孤波结果一致）。

## 方法论要点（可复用模式）

1. **经验约束降维**：先在数值解中验证变量间的函数关系（h vs n 散点 + 最小二乘），再代入降维——而非 FitzHugh/Rinzel 式启发式常数假设；拟合参数必须是控制参数（I）的函数并检验其依赖性
2. **分岔图对照**：降维模型的合法性判据 = 分岔点对齐（I_SNLC/I₁/I₂ 三点），XPPAUT 实现
3. **快慢分离方向性**：m 可绝热消去（快），n 不可（慢）——消去顺序决定模型是否保有振荡
4. **传播律提取流程**：数值速度 → 固定单参数拟合（v–R 幂律、v–C_m 幂律）→ 双参数律合并 v = a/(C_m R^b) → 与解析理论（C_m 指数=1）交叉验证

## 应用

- **大规模网络仿真**：2D 模型保分岔 + 保传播律，可用于高效神经元回路/网络模拟（作者明示）
- **轴突电生理参数估计**：v(R, C_m) 幂律给出从传播速度反演轴突内阻/电容的定量工具
- **HH 模型教学**：3D/2D 模型保留全部定性动力学（含 canard 与间歇性），是理解 HH 复杂性的入口

## 相关技能

- [[neural-dynamics-universal-translator]] — 跨神经元模型动力学翻译
- [[spiking-neural-network-differential-equation]] — SNN 动力学微分方程分析
- [[chaotic-griffiths-phase-neuron-map-networks]] — Chialvo 映射神经元的混沌 Griffiths 相
- [[adaptive-fractional-state-cortical-dynamics]] — 皮层异常扩散分数态
