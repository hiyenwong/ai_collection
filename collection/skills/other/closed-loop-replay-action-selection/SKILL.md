---
name: closed-loop-replay-action-selection
description: "Use when modeling hippocampal replay/preplay/consolidation"
tags: [hippocampal-replay, preplay, memory-consolidation, ca3-criticality, navigation, spiking-network]
---

# 闭环重放优化动作选择 (Closed-Loop Replay Optimizes Action Selection)

**来源**: Masud Ehsani, Sen Cheng (2026) "Online Preplay and Offline Replay Optimize Action Selection in a Closed-Loop Navigation Model" - arXiv:2610.26424 [physics.bio-ph]。NEST 仿真，LIF 电导型突触。

## 核心论点

单一 CA3 类脉冲网络以**共同机制**（背景噪声 + E-I 平衡 + 临界雪崩）生成全部重放模式；模式多样性**仅由任务依赖的突触修饰**决定；每种模式对动作选择有不同功能：

| 重放模式 | 触发情境 | 功能 |
|---|---|---|
| 在线前瞻重放 (online preplay) | 目标导航中的停顿 | 发现捷径、路径优化 |
| 离线前瞻重放 (offline replay) | 目标任务后的静息 | 巩固最优位置-动作序列 |
| 扩散式重放 (diffusive) | 随机觅食后的静息 | 泛化状态-动作映射、均质化内部连接 |

## 模型架构（三层）

1. **输入层**: 在线=空间调谐输入; 离线=空间均匀的泊松噪声（E/I 均有）
2. **循环层（place cells, 2D 流形）**: 高斯距离依赖连接 P(d) ∝ exp(−d²/2σ²); 2% 稀疏长程连接（对齐 CA3 解剖）; 抑制严格局域; 8 个边界单元（parrot relay, 对指向墙的动作神经元施加静态抑制 w=−40, 不参与可塑性）
3. **动作环吸引子**: Mexican-hat（局部兴奋+更宽抑制），bump 位置=群体向量平均→移动方向

## 可塑性规则

- **多巴胺门控对称 STDP + 资格迹**: ẇ = c(n−b); ċ = −c/τc + C1·ΔSTDP; ṅ = −n/τn + (C2/τn)δ(t−tn)。仅当神经调质 n > 基线 b 时权重增长。
- **对称纯增强核**: Δc(Δt) = C1·e^(−|Δt|/τSTDP)，τSTDP = 71ms/ln2 ≈ 102ms（匹配 CA3–CA3 突触 142ms 半持续时间, Mishra 2016）。
- **在线**: 奖励门控。**离线**: 恒定紧张性 n₀ > b → 无监督对称 STDP。
- **E→I 突触可塑**（局域 E-I 平衡的负反馈）。**乘性突触归一化**: w_ij ← w_ij/Σ_k w_kj · w_target（保持输出总权重恒定，防失控）。

## 临界动力学（机制核心）

- 调至失稳边缘：**Bogdanov–Takens (BT) 分岔点附近的亚临界 Hopf 线**；权重标度 w ~ 1/√k；背景放电 ~0.1 Hz。
- **无标度雪崩**: 尺寸指数 τ=1.55, 时长指数 α=1.7, 形状坍缩 γ=1.23，满足标度关系 γ=(α−1)/(τ−1)✓；与麻醉大鼠皮层数据吻合（Fontenele 2019）；**不属于** directed percolation 普适类（1.5/2.0）。
- 学习窗口机制: 异步平衡态中抑制去相关（Renart 2010）→ 链上无增强；**群体爆发时抑制以短延迟跟随兴奋 → 短正滞后交叉协方差峰 → 链式增强窗口**。
- **Turing 分岔**（σE < σI, 宽度比 β≈0.75, 振幅比阈值 α≈1.19）: 漫游活动 bump。有效核 W_eff(r) = Ŵ_EE(r) − (w̃_EI/w̃_EE)·α·Ŵ_EI(r)。

## 三大结果

1. **Preplay 发现捷径**: 停顿时活动扫向未来位置，环吸引子 bump 移向即将到来动作的向量平均 → 选择指向目标的动作；重复重放+可塑性在 2D 流形中嵌入 **1D 线吸引子**（轨迹的连续嵌入）；更短路径 → 资格迹衰减更少 → 可塑性更强 → 新吸引子胜出；旧吸引子被新集群抑制+归一化降权。E→I 可塑性使抑制自动跟随新路径的兴奋（自动再平衡）。
2. **前向 > 反向偏置**: 对称核产生双向链，但先前活跃集群中更持久的抑制电流压制即时再激活 → 偏向前向重放。
3. **离线重放收益非单调**: 成功试验太少 → 重放无法激活相关序列（无效）；过多 → 在线学习已充分（饱和）；中间区收益最大。**无归一化 → 权重失控 → 漫游爆发 → 对动作神经元的伪输入 → 路径不稳定**。平衡态必需：超兴奋→伪关联；过抑制→重放仅限局域。
4. **扩散重放泛化**: 解码位置呈布朗运动（MSD ∝ t, D∈[3,10] m²/s）→ 降低权重核角度方差（连接均质化）→ 动作映射泛化到未访问起点（10 次独立实验）。或解释 REM 睡眠中头方向细胞Assembly 的快速扩散（Chaudhuri 2019）。

## 关键参数

place field σ=0.3m, 2.4×2.4m 场地, 每位置 ~50 个重叠 place field（Wilson & McNaughton 1993）, 长程连接概率 2%。

## 对 AI 系统的映射

- Preplay = model-based lookahead/规划（在压缩时间窗内重组过往轨迹 → 捷径）
- 离线重放 = 经验巩固（对应 LLM sleep-consolidation 类系统）
- 扩散重放 = 策略平滑/泛化（把离散经验插值为连续表征）
- 设计可重放网络四要素: **E-I 平衡 + 对称 STDP + 突触归一化 + BT/Hopf 边缘噪声驱动爆发**；临界态最大化对弱记忆痕迹的敏感度（长关联长度桥接远距离集群）

## 相关技能

- `dreaming-world-action-models` - 梦境推理（本文提供其生物机制基础：静息重放=记忆巩固）
- `sleep-like-consolidation-llm` - LLM 睡眠巩固
- `learning-sequence-timing-replay-speed-snn` - 序列时序与重放速度控制

## 参考文献

- Ehsani & Cheng 2026, arXiv:2610.26424
- Buzsáki 2015 (SWR); Stella et al. 2019 (diffusive replay); Pfeiffer & Foster 2013 (online replay); Chaudhuri et al. 2019 (REM 扩散); Mishra et al. 2016 (CA3–CA3 对称 STDP)