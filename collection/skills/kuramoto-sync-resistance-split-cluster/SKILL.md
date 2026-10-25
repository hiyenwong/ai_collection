---
name: kuramoto-sync-resistance-split-cluster
description: Kuramoto sync resistance bounds via split-cluster templates.
category: ai_collection
---

# Beyond 11/16: Dense Kuramoto Networks that Resist Synchrony

**Paper**: arXiv:2610.21271 (Kevin P. O' Keffee, Starling Research Institute, nlin.AO/math.CO/math.DS, 15 Oct 2026)
**Methodology**: Lower-bound construction for the critical connectivity of Kuramoto synchronization via split-cluster templates + interval-arithmetic certification

## 核心问题

同质 Kuramoto 网络中，同步成为唯一稳定状态所需的最小连通度 μc（最小度/(n−1)）。此前界为 11/16 ≤ μc < 3/4。本文将下界提升到

μ0 = (4 + 2q*)/(7 + q*) = 0.6929077063…

其中 q* = 0.6505691669… 是 8 次不可约多项式

9q⁸ + 72q⁷ + 288q⁶ + 448q⁵ + 470q⁴ + 88q³ − 208q² − 128q − 15 = 0

在 (0,1) 内的唯一根。μc 被确定严格大于 11/16。

## 模板（Template）形式化 — 聚类级搜索框架

聚类模板为三元组 (x, φ, P)：簇大小 xa（Σxa=1）、簇相位 φa、簇间链接密度 Pab ∈ [0,1]。三个条件：

1. **相位锁定**: Fa ≡ Σb Pab·xb·sin(φa−φb) = 0（每个簇受到的拉力平衡）
2. **抗分裂**: ca ≡ Σb Pab·xb·cos(φa−φb) > 0（簇内成员被拉回）
3. **簇模式稳定**: L(y) = Σa<b xa·xb·Pab·cos(φa−φb)·(ya−yb)² > 0 对所有非全局旋转 y

关键结构事实：固定 (x, φ) 后，三条件与度 da 都对 P **线性** → 最稠密严格模板搜索是凸问题（SDP，内层）；外层移动 (x, φ)。任何稳定不动点按相位分组都给出满足非严格条件的模板 → **模板搜索无损失**。

## S7 分裂态构造（核心创新）

起点是 μ=3/4 的四簇 splay 态 C4（四簇各占 1/4，相位差 π/2，相邻簇全连、相对簇不连）。C4 线性退化：cos(π/2)=0 使 L≡0（razor's edge，非线性项不稳定）。

S7 对 C4 做三步微扰：

1. **分裂**：3 个相邻簇各裂为两半（±h，中间簇按 ±w·h 拉得更宽），第 4 簇 W 保持完整作为锚
2. **倾斜**：分裂打破 cos(π/2)=0 简并 — 相邻半簇对变得略近（正耦合）或略远（负耦合）
3. **疏化**：倾斜最大的 4 对"交叉"半簇链接（每对相邻分裂簇间最近对+最远对）密度降至 q≈0.65，对称地恢复拉力平衡

平衡固定 a = 1/(7+q)。两个中性偶极模式条件给出封闭方程组：

- w² = (q² + 6q + 1)/(q + 1)²
- 4(1 − q²)·w = 2q²w² + (3q − 1)(q + 1)

消去 w 即得 8 次多项式，w* = 1.3982781340…。连通度 μ = 1 − a(3 − q) = (4+2q)/(7+q)，在 q* 处取最大 μ0。

**稳定机制**（关键理论点）：分裂对簇模式形式的贡献在一阶相消，稳定性由二阶形式决定，q 进入其中；三簇模式中两个偶极在 q* 处恰好中性（提 q 提升连通度但软化它们），第三个由锚簇 W 保证。

## 证明机器（可复用的认证管线）

1. **Krawczyk 检验**：区间版牛顿法，若区间算子将相位小盒映射进自身 → 盒内恰有一个真解（固定点存在性）
2. **区间 Cholesky**：对称矩阵区间 Cholesky 分解成功且主元为正 → 区间内所有矩阵正定（稳定性）
3. **循环群 blow-up（Lemma 2）**：每簇排成环 Zg，簇间用固定"shift 集合"Sab 连接 → 每个振子看到相同模式（簇相位是精确不动点），Jacobian 按 Fourier 模分块；随机 shift 的 Fourier 系数小（Hoeffding）+ Gershgorin → 非均匀模稳定
4. **摄动论证**（Theorem 1）：q = q* − t 备退 t>0 使中性偶极以 O(t) 严格稳定，h→0 时度收敛到 μ0；先固定 t 再取小 h

认证成员：t=10⁻⁵, h=10⁻⁶ 给 μ* = 0.6929050246…（距 μ0 < 3×10⁻⁶）；最弱簇模式距中性仅 6.23×10⁻¹⁹ → 有理数据分母 D≈3.06×10⁴²，blow-up 网络规模 ≥ 9×10⁸⁴。

## 脆弱性与数值搜索教训（最重要的可迁移教训）

1. **带稳定裕度 ε 的优化器会系统性错过脆弱态**：Canale 态代价线性（11/16−μ ≈ 2.8ε），S7 态代价 ~ε^{1/3}（陡峭）— 最优解可能在裕度→0 的极限处，任何有限裕度搜索返回错误答案
2. **贴近退化点时标准优化器停滞或返回伪点**：S7 与 C4 只差 10⁻³ 量级相位偏移，CMA-ES 150 次重启 + 1850 个局部最优全部错过
3. **发现策略**：先对已知态（C4、Canale）做簇分裂/合并扰动，再在退化点附近**重新标度问题**（h⁻² 尺度提取极限模型），而不是直接全局搜索
4. **AI 代理协同发现**：论文states大部分工作由 LLM agents完成（Claude Fable 5.1/Opus 5.5、GPT-6、Grok 4.7）— 搜索、验证代码、证明推导、互审；一个独立 agent 拿到问题+Canale 论文也**没找到** S7，说明脆弱态发现需要正确的 ansatz 空间设计而非单纯搜索算力

## 与神经科学的关联

Kuramoto/相位振子网络是脑振荡同步（θ-γ coupling、皮层节律）的标准简化模型。本方法论给出：
- 脑网络同步-抗同步权衡的精确构造工具（什么拓扑能维持去同步的稳定簇态）
- 数值搜索脑动力学多稳态时的脆弱态警告：加了裕度/正则化的搜索可能错过生理上真实存在的高维精细态

## Activation

Kuramoto model, synchronization threshold, critical connectivity, cluster state, splay state, split cluster, template method, interval arithmetic, Krawczyk, action masking, oscillator network sync resistance, fragile metastable states, numerical search pitfalls, razor's edge degeneracy
