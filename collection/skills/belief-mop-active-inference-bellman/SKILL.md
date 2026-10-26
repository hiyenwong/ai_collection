---
name: belief-mop-active-inference-bellman
description: 部分可观测内在动机控制时用。信念MOP与EFE的Bellman价值迭代。
metadata:
  arxiv_id: "2609.39342"
  published: "2026-09-30"
  authors: "Manolis Mylonas, Rubén Moreno-Bote (Universitat Pompeu Fabra)"
  source: "arXiv q-bio.NC, IWAI 2026 (7th International Workshop on Active Inference)"
  tags: [active-inference, maximum-occupancy-principle, pomdp, intrinsic-motivation, expected-free-energy, bellman-equation, value-iteration, empowerment, exploration]
---

# Belief-Based Maximum Occupancy Principle and Active Inference

## 核心贡献

把三类内在动机框架（MOP、Active Inference/EFE、Empowerment）统一到**部分可观测 POMDP 信念空间**下做正面对比，并给出两项关键算法改进：

1. **信念化 MOP**：把 Maximum Occupancy Principle（最大化未来状态-动作路径熵，无奖励、无偏好、无认知目标）从完全可观测扩展到 POMDP——智能体状态取充分统计量 (s, b)，信念 b 经贝叶斯传播（等价于 VFE 最小化/信念传播）。
2. **EFE 的 Bellman 化**：把 Sophisticated Inference 中随深度指数爆炸的树搜索重构为带折扣因子 γ 的 **Bellman 方程 + 价值迭代**——离线在整个信念-状态空间上求解，深度线性代价，γ 保证唯一不动点与**时间平稳策略**（无需每步重规划）。

## 数学框架

**POMDP 设置**：5×5 网格世界，两个隐藏食物源 h=(h1,h2)（位置 (1,1)/(5,5)，转移参数 λ/µ/ρ），内部能量 E∈[0,30]（Egain=15，E=0 即死亡终止），观测 ω 在食物位置完全告知、离开则完全无信息。信念 b(h) 因子化 b(h1)b(h2)，离散化网格步长 ∆=0.1，价值迭代时对网格间信念做线性插值。

**MOP 值函数**（β=0 退化形式）：

```
V*(s,b) = ln Σ_a exp[ βH(·,·|s,b,a) + γ Σ_{s',b'} P(s',b'|s,b,a) V*(s',b') ]
π*(a|s,b) = softmax Q*(s,b,a)
```

边界条件 V(s⁺, b)=0（E=0 终止态无未来路径熵）。

**EFE Bellman 形式**：

```
G(s,b,a) = E[ln P(s'|s,b,a) − ln P(s')] − E[ln q(ω'|s',h')] + γ E[G(s',b')]
           └── Risk（风险/实用）──┘  └── Ambiguity（歧义/认知）──┘
π(a|s,b) = softmax(−d·G(s,b,a))
```

先验偏好 P(s)：均匀分布 + E=0 低偏好（最少结构）。d→∞ 退化为硬最小化（确定性策略）。

**信念更新**：b′(h′) ∝ Σ_h q(ω′|x′,h′) p(h′|h,x) b(h)——与 VFE 最小化在网格世界**数学等价**（Appendix A.5），揭示 MOP 信念传播与 Active Inference 变分推断的内在联系。

## 关键结果

1. **行为分化**：MOP 广泛探索、频繁在两食物源间切换（可持续探索不收敛）；EFE 收敛到单一食物源附近（同时降 risk+ambiguity 的稳定吸引子）；Empowerment 有限视野（n=5）下局部探索。
2. **MOP 的能量自适应**：策略熵随内部能量 E 分档——高能（E>15）高熵广探索，低能（E≤15）策略收缩、直奔食物。**无需任何调参**。
3. **EFE 的 d-权衡曲线**：逆温度 d 是外部固定的单一旋钮，扫 d 得到一条 survival↔state-entropy 权衡迹（状态熵 2.7→0.7 nats，d=0.5→10）；**MOP 单点落在迹之外**——同等寿命下占据更广、同等占据下寿命更优，即 MOP 联合达成探索与生存，而 EFE 两者互斥交换。匹配策略熵的 d=0.8 下：MOP 食物源间切换 13.3 次/千步 vs EFE 3.8。
4. **生存机制的对偶**：MOP 中生存倾向**隐式涌现**——终止态（E=0 只能 stay）使未来路径熵塌缩为零而被强贬，等效于 Active Inference 显式编码的 homeostatic 先验。Kiefer 2025 的"约束熵最大化"统一视角得到实例化：两者主要是"保命约束显式（EFE）还是隐式（MOP）"的差别。

## 方法论价值（可复用模式）

1. **EFE 树搜索→价值迭代**：任何 Sophisticated Inference/expected free energy 实现都可 Bellman 化——信念离散化 + 线性插值 + γ 折扣，把指数代价降为线性，且得到 time-stationary 策略。适合所有小状态空间 POMDP 的认知建模。
2. **信念网格 + 插值的价值迭代模板**：(1/∆+1)^k 信念组合数下选 ∆=0.1 实用；验证网格粗细不扭曲值函数形状（只量化不平滑）。
3. **内在动机对照实验设计**：双隐藏源 + 能量变量 + 空间分离三要素构成最小可比 testbed——可分辨"聚焦单源 vs 分布注意"、"保守 vs 冒险"、"全局 vs 局部探索"。
4. **无参数自适应 vs 参数旋钮**：评估探索算法时，画 survival-occupancy 平面的单点/权衡迹对比图（Fig. 3e 模式），暴露"需要外部调参换取行为柔性"的框架缺陷。
5. **熵目标统一视角**：MOP（路径熵最大化）与 EFE（自由能最小化）可视为约束熵最大化的两种对偶形式——设计新内在动机目标时先检查它落在这个谱系的哪个位置。

## 实现要点

- 信念状态空间：25 位置 × 31 能量 × 11×11 信念网格 ≈ 94k 状态，价值迭代数分钟内收敛。
- Empowerment 基线用 Blahut-Arimoto 估信道容量（n=5 步动作-观测互信息）。
- 关键超参：γ（收敛保证）、∆（信念网格）、d（EFE 温度）；MOP 零超参（β=0）。
- 复现：环境参数表在 Appendix A.2（Emax=30, Egain=15, λ=0.8, µ=0.2, ρ=0.8）。

## 相关技能

- `free-energy-rl-investment` — 自由能-熵对偶的风险敏感决策
- `metacognition-as-reward` — 元认知内在奖励 RL
- `economy-of-minds-multi-agent-intelligence` — 多智能体内在动机
- `prism-probabilistic-intention-switching` — 概率递归意图切换

## 标签

#active-inference #intrinsic-motivation #pomdp #value-iteration #exploration
