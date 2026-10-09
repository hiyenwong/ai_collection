---
name: causal-pieces-snn-expressivity
description: Use when analysing SNN expressivity or choosing SNN weight init. Causal pieces theory.
category: ai_collection
metadata:
  arxiv_id: "2504.14015"
  published: "2025-04-18"
  revised: "2026-09-29 (v2)"
  authors: "Dominik Dold, Philipp Christian Petersen (University of Vienna)"
  source: "arXiv cs.NE, q-bio.NC"
---

# Causal Pieces: Analysing and Improving SNNs Piece by Piece

**论文**: "Causal pieces: analysing and improving spiking neural networks piece by piece" (arXiv:2504.14015v2, Dold & Petersen, Univ. Vienna)

## 核心思想

SNN 表达力分析的 "linear pieces"（ReLU ANN）类比：**causal pieces** 把前馈单脉冲编码 SNN 的输入×参数空间划分为不同区域，每个区域内**同一子网络（causal subnetwork）引发输出脉冲**。区域内输出脉冲时间对输入和参数局部 Lipschitz 连续；跨区域边界可产生脉冲时间不连续或脉冲消失。这是首个不要求正权重、不回避脉冲时间不连续性的 SNN 表达力框架。

## 关键概念链

1. **Causal set** C_i：神经元 i 的所有在输出脉冲前发放的突触前神经元索引（可从观测脉冲时间+连接组直接计算，Algorithm in A.6.9）
2. **Causal subnetwork** P_I：递归定义的引发输出层的神经元/连接子集（按层存 causal set 列表）
3. **Causal piece** P[P_I]：使 causal subnetwork 保持不变的 (t₀, W) 联合空间区域；固定权重时退化为输入空间分区

## 理论结果

**Theorem 1（近似误差下界）**：对 g∈C³[a,b] 且 exp(g/τs) 非仿射，任意 p 个 causal pieces 的 nLIF 网络满足
‖Φ−g‖_{L∞} > c·ζ^{-2}·p^{-1/2}
即 piece 数是 SNN 近似能力的度量，且对任意不连续行为有效。经 transference principle [Göltz] 推广到多脉冲。

**Theorem 2（Sparre Andersen 计数）**：对称连续分布权重、大方差极限下
η_q ≥ (2^N−1) / (√(2N)·π·(N−3/2)²)
对所有此类分布成立——随机游走 Sparre Andersen 定理的直接推论。

## 反直觉初始化洞见（最实用）

- **非零均值权重分布才能最大化 piece 数**。文献中普遍借用 ANN 的零均值初始化（正态/均匀）恰恰是次优的
- 蒙特卡洛估计 p_k^q（k 个随机游走步后超过阈值的概率）→ piece 数上界 Σ_k C(N,k)·p_k^q
- 非零均值+大方差 → 更多 pieces（方差大可部分弥补均值选错）
- 进化算法优化分布参数（Gaussian: α₀=1.69, α₁=0.79, α₂=1.13, α₃=0.49 缩放律 N^{...}）

## 实验规律（可直接复用）

- **初始化时训练样本落入的 piece 数与最终测试精度强相关**（log-linear r=0.70 before / r=0.92 after training, τs=0.5；τs=0.1 时 r=0.85）；Fashion-MNIST r=0.83-0.89、EuroSAT r=0.80-0.87
- **差初始化难恢复**：多数网络训练后 piece 数反而下降；恢复者靠训练中大幅增加 piece 数（与 Thm 1 一致）
- 小时间常数 τs 更糟：晚到脉冲更难被整合，训练中创造新 piece 更难
- 样本在 pieces 间切换的重组活动：低 piece 数网络最终熄灭，高 piece 数网络持续重组
- **深 vs 宽**：piece 数随深度增长为 logistic 饱和（γ₀/(γ₁+e^{−γ₂N})，中位相对误差 2e-3~9e-2）而非 ReLU 的指数；深网络训练后 piece 增、浅网络减
- **正权重 SNN（仿生，皮层80%兴奋性）**：只要每神经元输入权和>阈值即全局 Lipschitz（可正则化强制）→ 覆盖数泛化上界；lognormal/均匀正初始化 + 线性读出（可负权重）在 Yin-Yang/MNIST/EuroSAT 达到全连接 ANN 水平

## 实践检查清单（SNN 初始化设计）

1. 计算训练集上每层 causal pieces（只需 connectome + spike times，复杂度 ∝ 参数数×样本数，可按层并行）
2. 权重从**非零均值**分布采样（正：lognormal；带符号：偏移 Gaussian/uniform）
3. 方差宁大勿小（Thm 2 下界保护）
4. 若初始 piece 数低（如 <100 for 3-class toy）：直接换种子/分布，别指望训练救回
5. 需要泛化界时考虑正权重 SNN+和>阈正则（全局 Lipschitz→covering number）
6. 深度增加 piece 数比宽度有效但会饱和——前几层增益最大

## 局限

- 理论限于前馈、单脉冲、nLIF（大 τm）；仿真支持标准 LIF（τm=2τs）外推
- 未覆盖：多脉冲动力学、surrogate gradient 训练、循环网络
- piece 数是近似能力度量非泛化度量；训练/验证 piece 数对比是提出的泛化研究方向
- 与离散时间 piece 分解 [Maass] 本质不同：那些区域对应常量输出、数量不随深度增长

## 相关 skill

- [[mdtf-temporal-fusion-local-snn]] — 单脉冲 TTFS 局部学习架构（本文理论的对象类型）
- [[snn-universal-approximation]] — SNN 通用逼近定理
- [[spikelite-snn-forecasting]] / [[surrogate-gradient-snn-training]] — 训练方法侧
