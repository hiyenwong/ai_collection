---
name: information-bottleneck-np-hardness
description: IB is NP-hard; 1/M^1.5 approx floor via clique inflation.
version: "1.0.0"
author: Hermes Agent (run5, 2026-10-18)
license: MIT
category: ai_collection
tags:
  - information-bottleneck
  - np-hardness
  - clique-reduction
  - motzkin-straus
  - entropic-turan
  - inapproximability
source: arXiv:2610.22272
source_title: The Information Bottleneck is NP-hard
authors: Roberto Bruno, Ugo Vaccaro (Univ. Salerno)
published: 2026-10-15
categories: cs.IT
trigger_words:
  - information bottleneck NP-hard
  - IB Lagrangian complexity
  - approximate information bottleneck
  - Blahut-Arimoto global optimum
  - entropic Turan
  - clique reduction information theory
---

# Information Bottleneck 是 NP-hard（CLIQUE 归约与不可近似性）

arXiv:2610.22272, Bruno & Vaccaro, cs.IT, 2026-10-15。数值验证 32/32 通过（2026-10-18，float64 全机器精度）。

## When to Use

- 你在用/评估 Information Bottleneck（IB）目标做表征学习、聚类、压缩或正则化，需要知道其计算复杂度边界与 Blahut–Arimoto 类算法的地位
- 你要为某个信息论/学习优化问题构造 NP-hardness 或不可近似性归约（本文的 clique-inflation + 熵 Turán cost 下界 + 线性/二次 gap 分离是可移植模板）
- 你在做互信息差（I(Y;T)−βI(X;T)）型泛函的极值分析，需要后验代价分解工具（g_W(P)=H(WP)−½H(P)、D(P‖π⊗π)=2g 恒等式）
- 触发词：IB global optimum, Blahut-Arimoto convergence, entropic Turan, Motzkin-Straus information theory, additive inapproximability

## 结论（何时引用）

- **IB(P_XY, R) = sup{I(Y;T) : I(X;T) ≤ R}** 与 **L_β(P_XY) = sup{I(Y;T) − βI(X;T)}**（任意固定有理 β∈(0,1)）的最优值计算均为 **NP-hard**（阈值判定形式，有理输入，bit 模型）。
- **不可近似性**：除非 P=NP，多项式时间不能在加性误差 1/(216|X|^{3/2})（Lagrangian）/ 1/(576|X|^{3/2})（Threshold）内近似最优值。常数可改进 4 倍（Remark 2, p=μ/(4m²)）。
- **实践警示**：Tishby 等的 Blahut–Arimoto 迭代只保证收敛到驻点——IB 后验空间非凸，全局最优多项式不可达。用 IB 做表征学习/正则化时应视其为启发式，除非分布有结构（已知可解情形见下）。
- β≥1 时 data processing ⇒ L_β=0（平凡）。常量加性误差的近似硬度是 open 问题。

## 核心方法论（可复用的证明机器）

### 1. Lagrangian 的后验代价分解

g_W(P) := H(WP) − ½H(P)。恒等式（Lemma 2）：

I(Y;T) − ½I(X;T) = g_W(P_X) − E_T[g_W(P_{X|T}(·|T))]

于是 **L_{1/2} = g_W(P_X) − inf_{encoders} E[g_W(后验)]**。任何「后验混合 = P_X」的分解（Prop 2：任意 {Q_t, P(t)}，ΣP(t)Q_t = P_X 可由信道 PT|X(t|x)=P(t)Q_t(x)/P_X(x) 实现）都给出下界；「所有分布的 cost ≥ c」给出上界 c。sup-over-encoders 变成了 mixture 分解问题。

### 2. 熵 Turán：D(P‖π⊗π) = 2g_G(P) + Motzkin–Straus

对图信道 W_G（X=定向边均匀, Y=端点二选一, π = W_G P）：

D(P‖π⊗π) = 2H(π) − H(P) = 2g_G(P)（精确恒等式，数值验证 err<2e-15）

Jensen：D ≥ −log Σ_{(u,v)∈A(G)} π(u)π(v)；**Motzkin–Straus 定理（定向形式）**：max_π Σ_{(u,v)∈A(G)} π(u)π(v) = 1 − 1/ω(G)。故

g_G(P) ≥ c_{ω(G)},  c_j := −½log₂(1 − 1/j) = log₂ j − ½log₂(j(j−1))

等号 iff P = U_C（最大团定向边均匀分布）。c_{m} − c_{m+1} ≥ 1/(2m² ln2)（Lemma 6）。对称分布情形即 Chao–Yu「When entropy meets Turán」(JLMS 2026)。

### 3. Clique-inflation gadget（NO 实例侧）

给定 (G,k)，m=k−1（只需 k≥4, N=|E|≥B=k(k−1)/2，否则平凡）：Ḡ 每条边 e={u,v} 加 m−2 新点使 C_e={u,v}∪S_e 成 m-clique，{E(C_e)} 划分 E(Ḡ)，M=|A(Ḡ)|=N·m(m−1)，ω(Ḡ)=max{ω(G),m}。
- **X** = A(Ḡ) 上均匀，**Y** = 边端点均匀 → 信道 W_{Ḡ}。
- **T0**：x ↦ 父边 e（x∈A(C_e)）。后验 = U_{C_e}，cost=c_m，值 Λ0 = g(P_X) − c_m。
- **NO（ω(G)<k）**：每个后验是 A(Ḡ) 上分布 ⇒ cost ≥ c_m（Lemma 5 应用于 Ḡ）⇒ T0 最优，L=Λ0，且 IB(P,R) ≤ R/2 + Λ0 ∀R。

### 4. Gap 注入：线性增益 vs 二次扰动（YES 实例侧）

G 含 k-clique K 时，T1 在 T0 上加一个符号 ⋆：x∈A(K) 时以 p=1/(12m²) 概率映射 ⋆（否则照旧）。
- 后验：⋆ → U_K（cost c_k，占比 λ=Bε/N）；e∈E(K) → V_e（U_{C_e} 微扰：A(e) 两点质量 μ(1−p)/(1−ε)，其余 μ/(1−ε)，归一化精确成立）；e∉E(K) → U_{C_e}。
- 参数：μ=1/(m(m−1)), ε=2μp=μ/(6m²), λ=Bε/N, Bμ=k/(2(k−2))≥1/2 (k≥4)。
- **增益** λ(c_m−c_k) ≥ λ/(2m²ln2)（线性 in ε）；**扰动损失** ≤ χ²/2ln2 ≤ ε²/(4ln2·μ(1−ε)²)（二次 in ε，Lemma 11 用 D≤χ²/2ln2 的 Sason–Verdú 界）。
- 净改善 Ψ − c_m < −3λ/(8m²) ⟹ **L(T1) > Λ0 + δ, δ = 1/(32Nm⁴) ≥ 1/(72M^{3/2})**（Lemma 13：δ=(1−1/m)/(32M·m²)，m² ≤ (3/2)√M）。

### 5. 有理化阈值 + 复杂度记账

Λ0 含对数（无理）→ 取有理 τ 近似 Λ0+δ/2 至 δ/12（Brent 高精度对数，Lemma 15 多项式时间）→ τ∈[Λ0+5δ/12, Λ0+7δ/12]，YES/NO 双侧各隔 5δ/12。近似算法误差 < 1/(216M^{3/2}) ≤ δ/3 即可判定 CLIQUE ⟹ 不可近似。归约本身多项式：|X|=M ≤ n⁴，P_XY 表每项 0 或 1/(2M)（O(log n) 位）。

### 6. IB-Threshold 的 R* 技巧

I(X;T1) = R* 有只依赖 (N,k) 的显式闭式（Lemma 14，五种对数的有理组合）。取 R̃≈R* 至 δ/4，R = max(R̃+δ/4, 0) ⟹ R* ≤ R ≤ R*+δ/2：YES 侧 T1 满足率约束且 I(Y;T1) > R/2+Λ0+3δ/4；NO 侧 IB ≤ R/2+Λ0 ≤ ϑ−δ/4。ϑ 取 gap 中点有理化。

### 7. β 推广：reveal-padding（Prop 3）

固定 β∈(0,1)∩Q，κ_β=2min{β,1−β}，ρ_β=β−κ_β/2，e_β=1−κ_β−ρ_β。新目标 Z：以 κ_β 概率揭示 Y、ρ_β 概率揭示 X、e_β 概率揭示 ⊥（J⊥(X,Y)）。链式法则给 I(Z;T) = κ_β I(Y;T) + ρ_β I(X;T)，且 β−ρ_β=κ_β/2 ⟹

L_β(P̃_XZ) = κ_β · L_{1/2}(P_XY)

同一 |X| ⟹ 同样的 1/(216|X|^{3/2}) 界除以 κ_β。无理 β：用多项式时间可计算的有理 b 逼近，误差 |β−b|log|X| 需 ≪ κ_b·γ（γ~|X|^{−3/2} ⟹ b 需 O(log|X|) 位精度，仍多项式）。

## 已知可解情形（ hardness 的边界外 ）

- 二元源过 BSC：Mrs. Gerber 引理（Wyner–Ziv 1973）；二元输入对称信道均匀输入（Chayat–Shamai, Sutskover–Shamai–Ziv）。
- 非二元 Hamming 信道均匀输入：整条曲线 = 显式标量函数的上凹包络（Benger–Asoodeh–Chen 2023）。
- 确定目标 Y=f(X)：IB(P,R)=min{R,H(Y)}；擦除信道：IB=(1−ε)R for R≤H(X)。
- 联合高斯：最优表征 = 典型相关方向的噪声线性投影（Chechik et al.）；联合平稳高斯过程：谱注水（Dikshtein–Weinberger–Shamai）。

## 数值验证要点（2026-10-18, 32/32 PASS）

float64 全部机器精度通过：c_j 恒等式 1e-16；D(P‖π⊗π)=2g 恒等式 200 抽样 1.7e-15；Motzkin–Straus 定向形式 5 图投影梯度搜索全部 ≤ 1−1/ω；Lemma 5 在 12 随机图×60 Dirichlet 抽样 min slack 9.6e-2 且 U_C_max 等号 1.7e-16；Petersen(NO)/K4(YES) 全管线：1500 合法随机编码器无一超过 Λ0；T0 机器值=Λ0 双实例 <1e-13；T1 增益 2.588e-4 > δ=6.430e-5（4.02×）；Ψ−c_m=−2.588e-4 < −3λ/(8m²)=−1.286e-4；Lemma 11 界 3.47e-6 ≤ 2.07e-5；R* 公式=I(X;T1) 双向 0 误差；Lemma 13 代数恒等式 1e-18；Prop 3 恒等式 300 抽样 0 误差。

## Pitfalls（验证调试教训，均已入档）

1. **验证脚本 I(Y;T) 必须含 H(Y) 项**：写成 −ΣP(t)H(Y|t)（漏 H(W P_X)）会整体下移 H(Y)，使绝对上界检查「全 PASS」——空洞通过。修复后原来「通过」的检查一度全 FAIL，暴露第二层 bug。**先跑 T0==Λ0 阳性对照再跑随机负检查**。
2. **dirichlet(ones(nX), size=nT) 生成的是后验不是信道**：行和=1 是 {P(X|T=t)} 的合法形式，作 P(T|X) 用则列不归一——这种「伪编码器」可以违反 Lemma 9 高达 +3.44 bits，让正确的公式看起来错。合法信道生成：`dirichlet(ones(nT), size=nX)`（每行 x 是 T 上分布）。
3. **pdftotext 分数/上标位移（第 4 类损坏）**：ε=2μp=μ/(6m²) 被拆成 "1/(6m)"；关键不等式链 −λ/(2m²)+λ/(8m²)=−3λ/(8m²) 中 3 的位置乱排。重构判据：从第一性原理重推（Lemma 6 精确界 + Lemma 11 χ² 界 + Bμ≥1/2），数值 4.02×/2.01× 比值自洽即确认。
4. **归约实例要卡边界**：K4 取 k=4 时 N=B=6 恰好饱和 (3.39) 的 N≥B，δ 与 1/(72M^{3/2}) 严格相等——是最严格的回归测试点。
5. **IB 实践者结论**：不要声称 Blahut-Arimoto 类算法找到 IB 最优；报告 IB 值时理论上限为多项式可达到精度的 |X|^{−3/2} 量级（对大字母表实际更松）。
