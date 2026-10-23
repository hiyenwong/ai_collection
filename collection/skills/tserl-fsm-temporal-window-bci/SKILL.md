---
name: tserl-fsm-temporal-window-bci
description: TSE-RL for MI-BCI time-window optimization via FSM masks.
category: ai_collection
---

# TSE-RL: Temporal Structure Embedded RL for MI-BCI Window Optimization

**Paper**: arXiv:2610.16921 (Huan Luo, Na Lu et al., Xi'an Jiaotong Univ., cs.NE/cs.LG, 12 Oct 2026)
**Code**: https://github.com/LunaLab-XJTU/TSE-RL
**Methodology**: Constrained-MDP window selection with FSM action masking + Transformer history encoder, plug-and-play over 8 MI backbones

## When to Use

- 在线/流式 EEG（或任何连续生物信号）解码中需要自适应时间窗选择而非固定窗
- 需要将事件时间结构先验（Onset→Sustain→Offset）硬编码进 RL 动作空间以防生理不可靠决策序列
- 需要一个可插在任意预训练分类器 backbone 之上的窗口优化层

## 核心问题

在线 MI-BCI 用固定 1s 滑窗处理连续 EEG：窗可能只覆盖事件局部、含事件前基线、或被伪迹污染。现有窗口优化方法（CTWS/ACO/SSA）孤立评估每个窗口好坏，产生碎片化、生理不合理的窗口序列。TSE-RL 把窗口优化重构为受约束序列决策：**每个窗口不是 good/bad，而是 MI 事件的语义角色**。

## MDP 形式化

- **状态** sn = (Xn, Hn, ρn)：当前窗、最近 k=5 个历史窗、试次进度 ρn = (nΔ−L)/T ∈ [0,1]
- **动作** an ∈ {0=Discard, 1=Onset, 2=Sustain, 3=Offset}：保留时必须标记语义角色；Offset 或试次结束触发终分类
- **FSM 相位** φn ∈ {Planning, Execution, Recovery}（内部约束状态，非 MDP 状态）：
  - Planning：合法动作 {0, 1} — 搜索事件起始
  - Execution（ERD 期）：{0, 1, 2} — 可修正 Onset 边界或确认持续 ERD
  - Recovery（ERS 反弹期）：{0, 2, 3} — 可继续延伸或以 ERS 标记终止
- **奖励** R = rdisc + rcont + rterm：
  - rdisc = 2(pn(ytrue)−0.5) 保留时 / 0.2(0.5−pn) 丢弃时（即时窗质量反馈，来自冻结判别器）
  - rcont = 0.1·I{an>0 ∧ an=an−1} − 0.1·I{φ≠Planning ∧ an=0}（连续性塑形）
  - rterm = ±5·α(N)，α(N) = 1 + 0.1·max(0, N−3)（终分类结果，N=保留窗数）

## 三个机制

### 1. FSM 约束动作掩码（核心创新）

π(an | zn, φn) ∝ softmax(Π(zn)) ⊙ m_φn，非法动作概率在采样前直接置零后重归一化。**为什么硬约束优于奖励塑形**：软约束只能通过 policy gradient 间接影响策略，训练早期仍会探索非法轨迹；即使收敛后随机采样也不能完全排除非法序列。掩码剪枝策略搜索空间，且无效动作越多收益越大（Huang & Ontañón）。适用条件：事件有已知序结构（Planning/Execution/Recovery 对应准备电位、ERD、ERS）。

### 2. Transformer 历史编码器替代 RNN

历史窗特征 (fn−k,…,fn−1) → 1 层 4 头自注意力（dh=128）→ 时间均值池化 → 线性投影 hn ∈ R⁶⁴。避免 RNN 梯度路径随序列长度指数衰减/爆炸，并行计算，固定维度表示变长历史。

### 3. 即插即用 backbone 分解

任意 EEG 分类器 B(Xn) = D(F(Xn))：F=特征层（冻结），D=判别头（冻结，其 pn 供建模 rdisc/rterm）。策略输入 zn = [fn; hn; ρn]。8 种 backbone（EEGNet/TSLANet/EEGConformer/FBCNet/ATCNet/M-ShallowConvNet/mAtt/CSPNet）各自定义 F/D 切分点。

## 三阶段训练

1. **监督预训练**：F+D 作为标准分类器在满窗上训练（CE loss，lr 1e-3，300 epochs）
2. **策略学习**：F/D 冻结，仅 PPO 训练历史编码器 G + 策略网络 Π（lr 3e-4，clip 0.2，GAE λ=0.95，4×10⁴ 步）— 分离防止表征漂移干扰策略优化
3. **联合微调**：解冻 F 最后几层，小学习率（3e-5）继续 PPO（2×10⁴ 步）

## 实验结果（MOABB 四数据集：BNCI2014001/0002/15001 + OpenBMI）

- 窗：L=1.0s，步长 Δ=0.1s；连续拼接模拟在线流；因果决策，无跨试次统计泄漏
- **跨会话（被试内）**：BNCI2014001 上 8 backbone 中 7 个提升 2–3pp（EEGNet 70.15→72.34*，CSPNet 75.89→78.47*，TSLANet 唯一下降 68.04→66.65 — 因其窗口级置信度噪声大，奖励信号不可靠）；其余三数据集全部 8 个 backbone 提升
- **跨被试（LOSO）**：多数 backbone 显著提升（EEGNet 47.38→50.15*，CSPNet 51.93→53.96*）；中风数据集上 8 个全部提升
- **消融**（EEGNet）：RL 单独 +1pp，+掩码或+历史编码器再加 0.5–1pp，全开最高（BNCI2014001 within: 70.15→69.10→70.75→71.41→72.34）
- **神经生理对齐验证**：学得策略在 0.8–2.5s 集中 Onset/Sustain（与对侧 μ/β ERD 最强期一致），>2.5s 转向 Offset；真类置信度在持续去同步阶段 >0.7
- **计算开销**：单窗推理 1.72–16.67ms（远低于 0.1s 步长间隔）；最慢是 mAtt（特征分解不适合 GPU 并行）

## 关键设计教训

1. **语义动作优于二值动作**：retain/discard → Discard/Onset/Sustain/Offset 同时提升可解释性与性能
2. **奖励来源需要冻结判别器**：公共 MI 数据集只有试次级标签，窗级奖励由 D 的 pn 提供 — backbone 弱则奖励信号噪声大（TSLANet 教训）
3. **硬掩码（结构先验）+ 软奖励（连续性塑形）互补**：掩码保证合法序列，奖励决定合法序列中哪条更优
4. **保留窗聚合**：p̄(y) = Σ w(ai)·pi(y) / Σ w(ai)，权重 w(Onset)=1.0, w(Sustain)=1.5, w(Offset)=1.0（ERD 完全发展段权重最高）
5. **局限性（作者自述）**：非真实闭环 — 模拟在线复现了非平稳噪声/疲劳模式漂移但 BCI 输出未反馈给用户；闭环验证待做

## 可迁移模式

- 任何“先验事件结构 + 流式窗决策”任务：癫痫发作检测（pre-ictal→ictal→post-ictal）、睡眠分期、ERP 检测
- FSM 掩码可直接替代 safe-RL 中的惩罚项设计，当非法动作可枚举时
- 三阶段“监督→冻结表征学策略→解冻微调”是低样本效率 RL 的通用解法

## Activation

motor imagery BCI, time window optimization, FSM action masking, constrained MDP, PPO, ERD/ERS, EEG streaming, plug-and-play backbone, transformer history encoder, online decoding, MOABB, semantic action alignment, safe RL action masking
