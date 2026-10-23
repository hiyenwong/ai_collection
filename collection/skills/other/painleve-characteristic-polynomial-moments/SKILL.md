---
name: painleve-characteristic-polynomial-moments
description: "USp/SO特征多项式×二阶导联合矩全参数域：Painlevé III′+Bessel逆幂和。"
version: 1.0.0
author: Assiotis, Bothner, Keating, Simm & Wei (arXiv:2610.29947); skill by 工程狮5号
date: 2026-10-23
source: https://arxiv.org/abs/2610.29947
category: ai_collection
tags: [random-matrix-theory, painleve-equations, characteristic-polynomial, bessel-point-process, jacobi-ensemble, riemann-hilbert, l-function-moments]
license: MIT
related_skills: krein-space-riemann-xi, random-riemann-zeta-spectrum, weil-quadratic-form-rank-zeta-zero-density, goldbach-proposition-weighted-sieves
---

# Painlevé 表示：USp/SO 特征多项式×二阶导联合矩（全容许参数域）

## When to Use

- 计算经典紧群 (USp(2N)/SO(2N)) 上特征多项式与导数联合矩的大 N 渐近——L-函数矩的 RMT 模型（Keating–Snaith 纲领）。
- 把矩问题化归为 Jacobi 系综奇异逆幂统计 → Hankel 行列式 → σ-Painlevé V/III′ 的两层塔。
- 需要用 τ-函数/Painlevé 超越函数显式表示矩的 leading coefficients。
- 把可积概率量（逆幂和）的极限识别为点过程泛函期望。

## 背景

- Montgomery pair correlation ↔ Dyson 观察；Katz–Sarnak 把 L-函数族分为 unitary/symplectic/orthogonal 对称类；Keating–Snaith 用特征多项式矩预测 L-函数中心值矩；CFKS 进一步给出低阶项精化猜想。
- **自反演对称**：A ∈ USp(2N) 或 SO(2N) 时 φ_A(θ) = det(I−e^{−iθ}A) 满足 φ'(0) 由 φ(0) 决定 ⟹ **二阶导是第一个非平庸导数统计量**。
- 定义：F_N^{USp}(s,h) = E_Haar[|φ_A(0)|^{s−h}·|φ_A''(0)|^h]；SO 同理（(2)）。

## 核心结果（arXiv:2610.29947）

1. **全容许参数域收敛（Theorem 1.3）**：
   - USp：s > −3/2，Re(h) < s+3/2：
     lim F_N^{USp}(s,h)/N^{s(s+1)/2+2h} = 2^{s²/2}·√[G(1+s)Γ(1+s)/(G(1+2s)Γ(1+2s))]·E[(1+e(s+½)/2)^h]
   - SO：s > −1/2，Re(h) < s+1/2：
     lim F_N^{SO}(s,h)/N^{s(s−1)/2+2h} = 2^{s²/2}·√[G(1+s)Γ(1+2s)/(G(1+2s)Γ(1+s))]·E[(1+e(s−½)/2)^h]
   - N-指数 s(s±1)/2 与 Keating–Snaith 经典矩一致；**每引入一阶导数在指数上加 2**（快速核对用）。G 为 Barnes G-函数；前因子平方用 G(1+s)G(2+s)/G(2+2s) 消除表观奇点。
2. **Jacobi 参数化（Lemma 1.6，参数域直接读出）**：
   - F_N^{USp}(s,h) = E[|φ(0)|^s]·N^{2h}·E_N^{(a,b)}[(X_N^{(a,b)})^h]，**(a,b) = (s+1/2, +1/2)**
   - F_N^{SO}(s,h) 同理，**(a,b) = (s−1/2, −1/2)**
   - 容许域 = JUE 权重非负性 (a,b > −1) + 矩可积性 (Re(h) < a+1)，无需另行推导
   - X_N^{(a,b)} = 1 + (1/2N²)·Σ_{j=1}^N 1/x_j^{(N)} ≥ 1 a.s.（x_j 为 JUE(a,b) 特征值）：**二阶导统计量 = Jacobi 逆幂和的平移**
3. **Bessel 逆幂和（概率识别）**：e(a) = Σ_{i≥1} 1/B_i^a，{B_i^a} 为参数 a 的 Bessel 点过程点列（核 K_a^{Bes}(x,y) = [√x·J_{a+1}(√x)J_a(√y) − √y·J_{a+1}(√y)J_a(√x)]/(2(x−y))），a.s. 有限。硬边缩放 N²x_j → B_j ⟹ (1/2N²)Σ1/x_j → e(a)/2。
4. **σ-Painlevé III′ 表示（Theorem 1.5）**：
   - 方程：(tσ'')² + 4(σ'+1)²·(tσ'−σ) − (aσ' + (a+1)/2)² = 0（t>0, a>−1）
   - 解：σ(t;a) = −(i/2)·[C₁(t)]₁₂ + (1−4a²)/16 − t，[C₁]₁₂ 为唯一 RHP 解的 (1,2) 元
   - 整数 h：E[(1+e(a)/2)^h] = (−1)^h·(d^h/dz^h)·exp[∫₀^z σ(t;a)dt/t]|_{z=0}
   - 一般复 h：取 n = 0（Re h<0）或 min{m∈N: m > Re h}（Re h≥0），
     E[(1+e(a)/2)^h] = ((−1)^n/Γ(n−h))·∫₀^∞ z^{n−h−1}·(d^n/dz^n)·exp[∫₀^z σ(t;a)dt/t] dz
5. **证明流水线（五步，可复用骨架）**：
   a. 群上联合矩 → JUE(a,b) 的奇异逆幂统计的矩（Lemma 1.6）
   b. E[(X)^h] 经 Laplace 变换导数公式 ((−1)^n/Γ(n−h))∫z^{n−h−1}(d^n/dz^n)E[e^{−zX}]dz 处理复 h
   c. E[e^{−z·Σ1/x_j}] = det[∫₀¹ x^{i+j}·e^{−z/x}·x^a(1−x)^b dx]/Z_N^{a,b}：**Pollaczek–Jacobi 型权重**（e^{−z/x} 破坏 Szegő 条件）
   d. 有限 N：Pollaczek–Jacobi Hankel 行列式 → **σ-Painlevé V**（已知理论）；N→∞：精化 Riemann–Hilbert 分析（Deift–Zhou steepest descent + 小范数模型 RHP）给出小 x 渐近 + 有限 N 修正项的一致导数估计
   e. 核证明：缩放后的第一逆幂和依分布收敛到 Bessel 点过程对应量 ⟹ 极限系数的概率识别
6. 奇正交群 O⁻(2N) 情形可用几乎相同方法得到（作者注）。

## 可复用模式（跨域）

- **矩问题 → 点过程逆幂和**：复分析矩渐近的极限常数经常是可积点过程（Bessel/Airy/sine）幂和泛函的期望；显式写出 E[(1+c·e(a))^h] 型极限。
- **两层 Painlevé 塔**：端点叠加奇异因子（e^{−z/x} 破坏 Szegő 条件）⟹ 有限 N τ-函数是 σ-PV，N→∞ 极限落到 σ-PIII′；中间需要 RH 精化分析衔接。
- **容许域从系综参数读出**：参数 (s,h) 的容许域 = 权重非负性 (a,b>−1) + 幂可积性 (Re h < a+1)——先找系综参数化，域自动出现。
- **导数统计量的 N-指数校验**：群对称性使低阶导数退化时改用高阶导；每阶导数在 N-指数上加 2——用于快速核对结果。
- **对称类指纹**：USp ↔ (a,b)=(s+½,+½) ↔ e(s+½)；SO ↔ (s−½,−½) ↔ e(s−½)——a = s±½ 是 Katz–Sarnak 对称类的直接读出。

## 验证标准

- h=0 退化为 Keating–Snaith 经典矩（指数 s(s±1)/2、Barnes G 前因子逐项一致）。
- h∈N：τ-导数公式与小 N 精确群积分/Monte Carlo 对照。
- 参数边界 (a→−1⁺) 行为与 Selberg 型积分已知奇性一致。

## 适用场景

- L-函数矩渐近与 CFKS 型猜想（zeta/L-函数中心值及导数统计的 RMT 模型）
- β-系综/Jacobi/Laguerre 系综的逆幂和、间距泛函、Fredholm 行列式矩
- Painlevé τ-函数展开与可积概率（Hua–Pickrell 测度、Hankel 行列式渐近）

## 参考文献

- T. Assiotis, T. Bothner, J.P. Keating, N. Simm & F. Wei, arXiv:2610.29947 (2026)
- Assiotis, Gunes, Keating & Wei, Proc. Lond. Math. Soc. 132 (2026) e70136（受限域前作）；Gunes（USp 首个 Painlevé 表示）
- Keating & Snaith (2000)；Conrey–Farmer–Keating–Rubinstein–Snaith；Tracy–Widom（Bessel gap ↔ PIII）；Jimbo–Miwa–Ueno τ-函数；Fokas–Its–Kitaev（RH 正交多项式）；Deift–Zhou（非线性最速下降）
