---
name: quantum-hamming-polynomial-bound
description: "任意(非纯)量子码强化Hamming界：Krawtchouk多项式+二项期望方法。"
version: 1.0.0
author: V. Grishin & A.L. Zabokritskiy (arXiv:2610.30088); skill by 工程狮5号
date: 2026-10-23
source: https://arxiv.org/abs/2610.30088
category: ai_collection
tags: [quantum-codes, quantum-hamming-bound, polynomial-method, krawtchouk, weight-enumerators, coding-theory, lp-bound]
license: MIT
related_skills: quantum-codes-lee-metric, covariant-quantum-codes, ultra-high-rate-quantum-codes, spacetime-requirements-quantum
---

# 量子码的多项式方法：强化量子 Hamming 界对任意 exact 码全参数成立

## When to Use

- 给定 (n, K, d, p) 证明/估计**任意 exact 量子码**（允许退化 impure、非加性 non-additive）的维数上界。
- 纯码（pure code）论证失效时：纯度假设是量子 Hamming 界历史障碍，本文给出 purity-free 的完整处理。
- 经典 Delsarte/LP 界向量子侧的移植与对偶化。
- 任何可化归为「格点非负测试多项式 + 二项期望」的计数/矩不等式问题。

## 核心技术（可移植）

1. **Exact code 设定**：K 维子空间 C ⊆ (C^p)^⊗n（p 为任意整数 ≥2，不必素数幂），距离 ≥d ⟺ 对所有 |supp E| < d 有 PEP = (Tr(PE)/K)·P。量子 Singleton 界 K ≤ p^{n−2(d−1)} 对任意子空间已知成立；Hamming 界此前只在纯码/低距离成立。
2. **量子重量枚举子（purity-free 的关键）**：
   - A_i = (1/K²) Σ_{wt(E)=i} |Tr(PE)|²,  B_i = (1/K) Σ Tr(PEPE†)
   - 恒等式：A_0 = 1, Σ_i A_i = p^n/K；B_i = (n/K) Σ_x A_x P_i^{(n,Q)}(x)（Q = p²）
   - **检测 ⟹ i < d 时 B_i = A_i**。故 ν(x) = K·A_x/p^n 是概率测度且 E_ν[P_i^{(n,Q)}(X)] = A_i（i < d）。这一步对任意 exact 子空间成立，无需纯度。
3. **Krawtchouk 多项式**：生成函数 Σ_j P_j^{(L,Q)}(x) z^j = (1+(Q−1)z)^{L−x}(1−z)^x；在二项测度 μ_L = Bin(L, (Q−1)/Q) = Bin(n, 1−p^{−2}) 下正交，v_j = C(L,j)(Q−1)^j。**P_0 = 1 的系数 = μ-期望**，即展开 f = Σ c_i P_i 时 c_0 = E_μn[f]。
4. **系数判据（Lemma 2.3）**：设 f = Σ_{i=0}^{D} c_i P_i^{(n,Q)}，D < d，f 在格点 {0..n} 非负，f(0) > 0。若 c_0·f(i) ≥ f(0)·c_i 对 1 ≤ i ≤ D，则 **K·f(0) ≤ p^n·c_0**。
   - 一行证明：avg := E_ν[f] = Σ c_i A_i > 0（因 ν(0) = K/p^n > 0）；格点非负 + 判据 + A_i ≥ 0 ⟹ avg ≥ (K/p^n)Σ f(i)A_i ≥ (K f(0)/(p^n c_0))·avg，约去 avg。
5. **多项式定理（Theorem 2.2, p ≥ 3）**：每个次数 ≤ D（2 ≤ D < d）、f(0) > 0、格点非负的实多项式 f 都满足
   **K·f(0) ≤ p^n·E_μn[f(X)]**，X ~ Bin(n, 1−p^{−2})。
   纯码时 f 可任选（B_i = A_i 直接控制）；非纯码只有 f(0) 单点可控——本文用「固定 f(0)、极小化 E_μ[f]」的极小多项式处理全部 f。
6. **Yu–Lai–Oh 舍入族（Theorem 2.1）**：d = 2t+1+σ，D = d−1 = 2m+r，m = t−e，r = 2e+σ，N = n−r。取 h(x) = Π_{j=1}^m (x−a_j)(x−a_j−1)，a_j = ⌊ξ_j⌋，ξ_j 为 P_m^{(N−1,Q)} 的根；g(x) = C(n−x, r)·h(x)（二项因子制造终端零块，成对因子保格点非负）。舍入分母 S = g(0)/c_0 = Q^r·h(0)/E_μN[h(X)]。结论：
   **K·S ≤ p^n 对所有 p ≥ 2, t ≥ 1, 0 ≤ e ≤ t, σ ∈ {0,1} 成立**——e=0 含 Zhang–Chen 一般码 Hamming 界，e=t 退化为 Singleton 端点（S = Q^D）。
7. **证明架构（分情形流水线，方法学上最可复用）**：
   - p ≥ 3：固定原点值、极小化二项期望；极小多项式零点结构 = 终端块 + 相邻整对；根区域（次数 ≤ 长度的显式分数）内零点全部超过次数
   - 根区域外：切换到重量枚举子的**不变窗口秩界**（对码维数本身做 rank bound，而非对多项式）
   - p = 3, 4：精确有限证书（finite certificate）覆盖有界余项
   - p = 2：对舍入多项式直接验证系数不等式

## 可复用模式（跨域）

- **纯度无关化**：枚举子恒等式对任意 exact 子空间成立；非纯码的障碍只在对偶系数的符号——用「极小期望多项式」替代「纯度下 f 可任选」的论证。
- **插值界族**：构造以两个经典界为端点的单参数族（e: Hamming → Singleton），在正交多项式根处成对舍入 (x−a)(x−a−1) 保持格点非负性——舍入比未舍入族严格更强。
- **格点非负 + 二项期望**：通用配方 K·f(0) ≤ p^n·E[f(Bin(n, 1−p^{−2}))]，把码维数界化为离散正交多项式的矩问题；测试多项式次数只需 < d。
- **对偶 Krawtchouk involution**：f ↔ F(x) = Σ_j f(j)P_j(x)，F(i) = Q^n·c_i——与 Li–Xing LP 界互为对偶视角；判据 (16) ⟺ F 的系数非负且 F 在正集合外 ≤ 0。
- **分 regime 流水线**：一个参数空间（此处 deg/n 比值）内用极小化结构，界外切换到秩/维数论证，余项用有限计算证书封口。

## 验证标准

- 小参数 (n, d, p) 穷举或 ILP 搜索码空间，对照界值是否紧。
- 端点退化检验：e = 0 退化为已知一般码 Hamming 界；e = t 退化为 Singleton 界。
- 纯码情形与 Yu–Lai–Oh 原结果逐点一致。

## 适用场景

- 量子码维数/码率界：qubit、qudit、degenerate/non-additive 码
- 经典 Delsarte–LP 界的对偶化与向新码类（量子、子空间码）移植
- Krawtchouk/Hahn 等离散正交多项式支撑的矩不等式与计数问题

## 参考文献

- V. Grishin & A.L. Zabokritskiy, "The strengthened quantum Hamming bound of Yu, Lai, and Oh", arXiv:2610.30088 (2026)
- Yu, Lai & Oh（插值族原始提出者）; Zhang & Chen（一般码 e=0 情形）; Li & Xing（量子码 LP 界，Lemma 2.3 的对偶特例）; Rains（量子重量枚举子恒等式）
