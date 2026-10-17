---
name: calibrated-aif-information-gain-regret
description: 分析AIF信息增益探索何时优于置信集时用。校准novelty即奖励无关ℓ1置信集
metadata:
  arxiv_id: "2610.19046"
  published: "2026-10-13"
  authors: "Melih Kandemir, Mustafa Mert Çelikok (University of Southern Denmark)"
  source: "arXiv cs.LG, submitted 13 Oct 2026"
  tags: [active-inference, regret-theory, information-gain, exploration, bayes-ucbvi, confidence-sets, state-abstraction, adaptive-adversary, computational-neuroscience]
---

# What Information Buys in Active Inference — 校准信息增益的遗憾理论

## 核心贡献

首次把 Active Inference（AIF）与强化学习遗憾理论的 SOTA 方法 **Bayes-UCBVI** 放在完全平等的脚手架上对比，回答"自然界的 信息增益驱动探索 何时比 置信集驱动探索 更优"：

1. **统一脚手架**：两个 agent 作用于同一个 tabular MDP 的同一状态抽象 φ（|X| 个抽象态，|S| 个真实态），持有相同的 Dirichlet 后验，贪婪形式只在探索项不同——从而把"信息 vs 价值"作为探索货币的差异干净分离出来。
2. **负结果（固定奖励）**：AIF 的 novelty 按 N⁻¹ 衰减，但任何有效置信宽度必须 ≥ N⁻¹/² 的估计误差——阶数错配。用原始 novelty（或 softmax AIF）探索会把 agent 锁死在次优动作，导致**线性遗憾**。
3. **校准 AIF**：把 novelty 开平方并乘以值函数跨度（来自运输不等式：Dirichlet 后验下 B⊤f 的方差 ≤ ½·span(f)²·Novelty），得到与 Lu & Van Roy (2019) 贝叶斯宽度对应的频率主义有效宽度。遗憾 Õ(H^{3/2}·Γφ·√(XAT))，但比 Bayes-UCBVI 差一个分支数因子 Γφ ≤ X——固定奖励下校准后仍无优势。
4. **正结果（自适应目标）**：当对手从 agent 自身数据中选择奖励函数（"目标"）时，Bayes-UCBVI 的价值特异性分位数失效（Ω(K/ln K)），而校准 AIF（均匀先验）对**所有奖励函数同时乐观**——等价于奖励无关 ℓ1 置信集。代价 √S 因子，且任何 goal-memoryless agent 都无法避免（下界匹配）。
5. **学习抽象的失败模式**：AIF 对发射模型的好奇心使其偏好产生多样观测的坏动作（Ω(min{K,S}) 线性遗憾）；JEPA 式 decoder-free 潜在预测的自指目标会确认过粗抽象、永不被自身数据反驳（线性遗憾）；GOLF 用价值函数作为所有候选抽象的**公共目标**才获得 Õ(√T)。

## 数学框架

**设置**：有限视野分段式 tabular MDP M=(S,A,P*,R*,H)，agent 通过抽象 φ 观测。X=|φ(S)|≪S。

**统一价值备份**（所有 agent 共享）：
```
Q_k,h(x,a) = R̂_φ(x,a) + P̂_k,h(·|x,a)⊤V_k,h+1 + Ψ_k,h(x,a)
V_k,h(x) = max_a Q_k,h(x,a),  V_k,H+1 ≡ 0
```
探索项 Ψ 与动作规则是 agent 间唯一差异：
- Bayes-UCBVI：Ψ = 后验分位数间隙 Δ，贪婪动作
- softmax AIF：Ψ = β⁻¹(状态项+novelty)（novelty 被计两次），softmax 精度 β
- 校准 AIF：Ψ⁺（下式），贪婪动作，值钳制在 r₀(H−h+1)

**Novelty 定义**（对转移核 B 的信息增益）：
```
Novelty(x,a) := I[B; x_{τ+1} | x_τ=x, a_τ=a]
              = H[P̂_k,h(·|x,a)] − E_{B∼ρ_k(x,a)} H[B]
```
关键界：Novelty ≤ X/(n̄+1)（按 N⁻¹ 衰减），而有效宽度需 ~H·ν/√n（N⁻¹/²）。

**校准宽度**（核心公式，Eq. 5）：
```
Ψ⁺_k,h(x,a) := 2·span(V⁺_k,h+1)·√(ℓ_k,h·Novelty(x,a)) + 2√2·r₀H·√(ℓ_k,h/n̄_k,h)
ℓ_k,h 为对数因子, n̄ = n + n₀
```
第一项的"汇率" 2·span(V)·ℓ/Novelty ≥ 2·span(V)·ℓ·n̄/X，随 n̄^{1/2} 增长——**没有任何常数精度 β 能把 nats 换算成奖励，这个自适应汇率才能**。

**运输不等式**（Lemma 7）：对任意 Dirichlet 后验和有界 f，后验方差 Var(B⊤f) ≤ ½·span(f)²·Novelty。由 Pinsker 不等式：|E_B[f] − E_p̄[f]| ≤ span(f)·√(D_KL(B‖p̄)/2)。

**关键定理速查**（Table 1）：

| Agent | 遗憾界 | 结果 |
|---|---|---|
| 任意经 φ 行动的 agent | Ω(ε̄K + H√(XAT)) | Cor.1 下界 |
| Bayes-UCBVI on φ | O(ε_rep K) + Õ(H^{3/2}√(XAT)) | 最优 |
| softmax AIF / CaI | Ω(K) 线性 | Prop.1 |
| 贪婪 λ·Novelty^q, q∈(½,1] | Ω(K) | Thm.2(a) |
| 贪婪 λ·Novelty^q, q<½ | Ω(min{λK^{1−q}, K}) | Thm.2(b) |
| **校准 AIF（固定奖励）** | O(ε_rep K) + Õ(H^{3/2}Γφ√(XAT)) | Thm.3, 差 Γφ 因子 |
| Bayes-UCBVI（自适应目标） | Ω(K/√ln K) | Prop.7 锁死 |
| **校准 AIF 均匀先验（自适应目标）** | Õ(H^{3/2}√(XAT)) = O(S^{1/2}√K) | Thm.4(c) 达到下界 |
| 任意 goal-memoryless agent | Ω(√(S·K)) | Thm.4(b) 下界 |
| AIF 对发射好奇 | Ω(min{K,S}) | Prop.10 线性 |
| latent-predictive (JEPA式) | Ω(HK) | Prop.11 线性 |
| GOLF | Õ(√(H²XAT(ln|Φ|+XA))) | Thm.5 唯一安全 |

## 方法论要点

1. **判断信息增益是否是正确的探索货币**：奖励固定 → 用价值特异性宽度（UCBVI）；奖励/目标从 agent 数据自适应产生（homeostatic、autotelic、用户反馈驱动）→ 用校准信息增益（奖励无关 ℓ1 集合）。
2. **校准公式可移植**：任何用信息增益做探索的系统，把探索奖励乘 span(V)·√(ℓ·Novelty) 即可修复阶数错配。novelty 的平方 ≈ ℓ1 置信集半径的平方。
3. **精度 β 不是自由参数**：AIF 的 precision 理论中 β 应为该数据依赖汇率，常数 β 无法校准。
4. **表征学习目标必须是外生的**：自指目标（预测自己的标签，包括 JEPA 变体、对发射模型的好奇）在理论上有线性遗憾的不可反驳粗抽象；价值函数是候选抽象间唯一安全的公共目标（GOLF 模式）。
5. **抽象的表示代价**：经 φ 行动的一切 agent 至少付 Ω(ε̄K + H√(XAT))；ε_rep(φ)K 是抽象不准确度的线性代价。

## 与相关工作的关系

- **Control as Inference (CaI)**：忽略认识论不确定性 → 不探索（线性遗憾），除非外接 K-learning/VAPOR/EUBRL 项。
- **Lu & Van Roy 2019**：贝叶斯信息宽度 → 本文给出频率主义对应物（√novelty）。
- **Jaksch et al. 2010**：ℓ1 置信集（UCRL）——校准 novelty 是其半径的无奖励版本。
- **GOLF (Jin et al. 2021)**：低秩 MDP 中用价值做抽象选择的公共目标——学习抽象时的安全范式。
- **Friston/Da Costa 离散 AIF**：本文证明其标准形式（softmax、常数精度、发射好奇）在遗憾理论上有系统性失败模式；修复需要校准项+贪婪化+去发射。

## 应用场景

- **计算认知科学**：为"生物体为什么用信息增益探索"给出精确边界——只在其目标本身随经验适应（如体内平衡 set-point 漂移、autotelic 目标生成）时信息探索才有优势。
- **内在动机 RL 设计**：好奇心/novelty 奖励的正确尺度是 √novelty 而非 novelty；固定奖励环境应改用计数或后验分位数。
- **抽象/表征学习**：选抽象的价值目标 > 预测目标；JEPA 式自预测有理论上的粗抽象陷阱。
- **自适应评估协议下的 UCB**：任何"评估指标由历史数据决定"的场景（如在线推荐的目标漂移），价值特异性置信区间会失效，需要奖励无关集合。

## 陷阱

- novelty 被 AIF 状态项+参数增益**重复计数**——离散 AIF 公式的已知怪癖，本文修复时去掉了状态项。
- Table 1 中 q 的临界点在 1/2：q>½ 线性锁死，q<½ 只需 λ 随 K 调节；q=½ 是唯一安全指数。
- 均匀 Dirichlet 先验是"对所有目标同时乐观"的必要条件——非均匀先验会保留目标特定信息，破坏奖励无关性。
- 论文的 goal-memoryless 定义排除"把过去目标当数据"的 agent；这类 agent 可把 √S 代价降到 S^{1/4}（Thm. 4(a) vs (c)），但 AIF 的生成模型结构上做不到。

## arXiv 元数据

- **ID**: 2610.19046v1 [cs.LG] 13 Oct 2026
- **作者**: Melih Kandemir, Mustafa Mert Çelikok (University of Southern Denmark)
- **证明**: 全部在附录（Appendix B 列出各行条件；F.2 Theorem 2；F.7 运输引理；G 高斯族硬实例）
