---
name: ogp-separating-quantum-inspired-optimization
description: Use when OGP separates classical heuristics from QAOA depth barriers.
trigger: overlap gap property, OGP, QAOA vs mean-field MF-AOA, quantum-inspired classical algorithm limits, AMP obstruction, adiabatic to non-adiabatic QAOA parameter transition, clustered solution space, combinatorial optimization barrier
category: ai_collection
---

# OGP 分离量子与量子启发式优化算法

**来源**: arXiv:2609.35131 — Goh & Müller (DLR / Univ. Cologne), 2026-09-28

## 核心论断

问题具有 **Overlap Gap Property (OGP)** 时，解空间中 ε-最优解分裂为 Hamming 距离上不连通的簇（禁止重叠区间）。由此可以**刚性分离**两类算法：

1. **MF-AOA（量子启发经典算法）被阻塞**: 将 MF-AOA 的平均场自旋动力学嵌入**有限记忆 AMP** 框架（坐标式 Lipschitz 函数 f_t/F_t + 截断），直接继承 Gamarnik–Jagannath OGP 阻碍定理 → 无法任意接近最优。
2. **QAOA 可以穿越屏障**: Max-4-XORSAT 数值模拟显示 QAOA 超越 OGP 能量阈值，有限尺寸标度支持**超多项式**（亚指数）而非多项式深度依赖。

## 方法模式（可复用）

### 模式 1: 有限记忆 AMP 归约（证明经典启发式被 OGP 阻塞）

把一个经典启发式的迭代写成 AMP 递推 U^t = F_t(J(·, f_t(U^0..U^{t-1})), U^0..U^{t-1})，只需验证：
- f_t(0)=0、f_t/F_t 坐标式 Lipschitz（算子范数界：旋转矩阵正交 → ‖R_t(x)-R_t(y)‖ ≤ 2s(t)|x-y|，telescoping 得 K=2√T）
- 催化场项仿射 Lipschitz（max s²(1-s) = 4/27）

→ 任何能写成这种张量缩合 + 有限记忆 + 坐标截断形式的算法，都被 OGP 定理一网打尽。

### 模式 2: OGP 实例制备（branch-and-bound 扫描 ε）

对候选实例跑 branch-and-bound 收集 ε-优解集，计算重叠谱 q(σ,τ)；逐次降 ε 直到谱出现**单个间隙** → OGP 实例；无任何 ε 产生间隙 → 无 OGP 对照实例。要点：对照实验用同一生成器产出，只差几何性质。

### 模式 3: 深度临界点检测（adiabatic → non-adiabatic 转变）

- 对单实例逐深度优化 (γ,β)：浅深度最优参数呈线性绝热 schedule；到临界深度 p* 出现**不可微点**，全局最优跳到非绝热分支。
- 对齐技巧：把所有实例按 (p−p*, F_p−E_OGP) 平移后叠加 → 转变发生在 OGP 阈值附近略下方，是**实例共性**而非个体涨落。
- 优化器鲁棒性检查：COBYLA/BFGS/Nelder-Mead 换优化器、多初始化、Fourier 参数化都要复现同一 kink。

### 模式 4: 优化目标改变景观结构

优化 approximation ratio F_p 出现 kink；换成优化 ground-state overlap P_p 则 kink 消失。**可复用教训**: 变分参数的最优 schedule 定性依赖于所选优化目标——选择目标函数本身是算法设计自由度。TTS proxy = p/P_p 在有限深度取最小（28–52 层），盲目加深不如在 TTS 最优点停。

### 模式 5: 资源估计桥接算法-硬件鸿沟

两条曲线判定硬件可达性：
- 屏障深度 p_OGP(N)（数值外推，N=50 时 p≈250，线性外推为乐观下界）
- 相干极限深度 p_T2 = T2 / (D_p·t_2Q)，D_p = G_p/(Δ+1)（并行度折算）

超导参数下 p_T2 = 13–33 ≪ p_OGP → **当前硬件在到达 OGP 屏障之前就耗尽相干时间**。保真度模型 F_2Q = (1−e_2Q)^G 随深度指数衰减。任何"量子优势宣称"都应同时报告 p_barrier 与 p_T2 的差距。

## 实验结果速查

| 观察 | 数值 |
|------|------|
| N=15 代表实例临界深度 | p* ≈ 28 |
| TTS 最优深度 (N=15→21) | p = 28 → 52 |
| N=50 外推屏障深度 | p ≈ 250（线性外推，乐观）|
| 超多项式拟合优势 (N=27-29) | RMSE_poly/RMSE_spoly ≈ 10.95 |
| 小尺寸 (N=23-26) | RMSE 比率 0.44（多项式略优，无法区分）|
| IBM Heron 相干极限 | p_T2 = 13–33 ≪ 250 |
| MF-AOA Lipschitz 常数 | K ≤ 2√T（与 N 无关）|

## 应用边界

- 稀疏图上对数深度 QAOA 已知被 OGP 限制（Chou et al.）；本文给出的是**穿越屏障所需深度**的第一个数值刻画。
- MF-AOA 阻碍结论 conditional on H_N 上的 OGP 扩展假设（Conjecture 3.2 of Gamarnik-Jagannath）。
- N=50 是经典模拟开始失效的交叉点，也是首个可能的量子优势实验规模。

## 相关技能

- `qaoa-landscape-audit` — QAOA 变分景观审计
- `comet-constraint-preserving-qaoa` — 约束保持 QAOA
- `qaoa-interaction-threshold` — QAOA 模拟复杂度阈值
- `quantum-mcts-fixed-confidence` — 量子 vs 经典混合成本切换

## 参考文献

1. Goh & Müller, arXiv:2609.35131 (2026)
2. Gamarnik & Jagannath, Ann. Probab. 49(1) 180 (2021) — AMP 的 OGP 阻碍定理
3. Chou, Love, Sandhu, Shi, ICALP 2022 — 局域量子算法极限
4. Boulebnane & Montanaro, PRX Quantum 5, 030348 (2024) — k-SAT QAOA 指数标度
5. Misra-Spieldenner et al., PRX Quantum 4, 030335 (2023) — MF-AOA 原始定义
6. Zhou, Wang, Choi, Pichler, Lukin, PRX 10, 021067 (2020) — Fourier 参数化
