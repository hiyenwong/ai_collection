---
name: kronlstm-kronecker-delta-rule
description: Use when designing linear attention or associative memory update rules, or analyzing memory interference. Kronecker Delta Rule (KronLSTM) - single-direction memory revision with provably bounded norm.
category: ai_collection
metadata:
  arxiv_id: "2610.26834"
  published: "2026-10-19"
  authors: "Hartl, Zolyomi, List, Klambauer, Bock, Hochreiter (NX-AI / JKU)"
  source: "arXiv cs.LG"
  code: "github.com/NX-AI/KronLSTM"
---

# KronLSTM: Kronecker Delta Rule for Long Context Linear Attention

**论文**: "Kronecker Delta Rule for Long Context Linear Attention" (arXiv:2610.26834, NX-AI / JKU xLSTM 团队)

## 核心思想

线性注意力把上下文压缩为关联矩阵记忆 S ∈ R^{d_v×d_k}。三种写入规则的本质差异是"如何修正已存关联"：

| 规则 | 更新 | 修正方向 | 干扰控制 |
|---|---|---|---|
| Hebbian (mLSTM) | S←S+v k^T | 无修正只叠加 | 无，记忆无限增长需 forget gate 压制 |
| Delta (DeltaNet) | S←S−β(Sk−v) k^T | 残差方向（依赖记忆内容） | 仅 key 重叠 |
| **Kronecker Delta** | S←S−β(v^T S k−c) v k^T | 输入对自身的方向 | **value 重叠 × key 重叠 双重门控** |

Kronecker Delta Rule 不修整个向量残差 S k−v，而是把**标量关联** v^T S k 朝目标 c 修正，修正方向固定为 v k^T（只由当前输入决定，不读记忆内容）——最小侵入式记忆修订，长上下文下干扰远小于 delta rule。

## 数学结构

**向量化形式（命名由来）**：令 a_t = k_t ⊗ v_t = vec(v_t k_t^T)（Kronecker 积特征），s = vec(S)，则

s_{t+1} = (I − β_t a_t a_t^T) s_t + β_t c_t a_t

即 Kronecker 特征 a 上的 Widrow–Hoff Delta Rule——一次对 ½(v^T S k − c)² 的梯度下降。

**关键性质**：
1. **误差修正**：重呈现同一对时误差乘 (1−β‖a‖²) 收缩 iff 0<β<2/‖a‖²；Newton step β=1/‖a‖²=1/(‖k‖²‖v‖²) 一步达标；c=0 删除关联
2. **干扰公式（最实用）**：Δ(v_i^T S k_i) = −β(v_t^T S k_t − c_t)·(v_i^T v_t)(k_t^T k_i)——value 或 key 任一正交即保护已存关联；DeltaNet 只由 key 重叠控制、mLSTM 全部受影响
3. **容量**：每个三元组 (k,v,c) 施加一条线性约束 → 可精确存 d_k·d_v 个标量关联（DeltaNet 只有 d_k 个向量关联）；单 key 可挂多个相互正交 value（读出为它们的和）
4. **chunkwise 并行**：转移因子 (I−β a a^T) 是与 c 无关的广义 Householder → DeltaNet 的 WY 表示/分块并行训练直接迁移（a 替换 k，target 只进驱动项）
5. **状态跟踪**：β‖a‖² ∈ (1,2) 时转移因子出现负特征值——DeltaNet 系状态跟踪能力的来源在 Kronecker 版同样保留

## 稳定性定理

- **Thm 1（无偏均值与稳态）**：E[s_{t+1}] = (I−βĀ)E[s_t]+β b̄ 精确递推，唯一不动点是最小二乘记忆 S^LS = argmin E[(v^T S k−c)²]；迭代构成时间齐次 Markov 链，存在唯一平稳分布 π_β，任意初始化几何收敛，平稳均值恰为 S^LS（隐式正则化的目标）
- **Thm 2（范数界）**：非扩张 regime（κ=β max‖a‖² ≤ 1）下 E‖S_t‖_F² ≤ (1+q^{t/2})²·E[c²]/λ_min(Ā) ≤ 4E[c²]/λ_min(Ā)，瞬态因子从 4 几何衰减到 1；且 S^LS 被目标能量夹逼：残差能量只会让它更小
- **实践含义**：ℓ2 归一化 k,v + sigmoid β ⇒ β‖k‖²‖v‖² = β < 1 自动非扩张——**不需要 mLSTM 的 normalizer/stabilizer 状态**，省去大数量级比值归一化的数值困难（mLSTM 高学习率压力测试梯度尖峰失稳，KronLSTM 稳定）

## KronLSTM 架构

- **三门解耦**：forget F_t=diag(f_t) 右乘作用在 key 维（逐 key 方向独立衰减 S F_t）；erase β_t=σ(w_β^T x)；write c_t=σ(w_c^T x)，用 c̃=c/β 解耦——β 单独控制擦除多少、c 单独控制写入多少
- **遗忘门参数化**（Mamba/GDN-2 式）：f = σ(−s_f)^α，α=exp(a_log) 每 head 一个学得的 log 尺度指数 → 基线保留时序跨数量级差异，head 内逐方向变化全由输入决定，无需高 pre-activation
- **完整更新**：S_{t+1} = S_t F_t − β_t(v_t^T S_t F_t k_t) v_t k_t^T + c_t v_t k_t^T
- **块结构**：Q/K/V 线性投影+短因果 depthwise conv+SiLU+ℓ2 归一化；读出 h = W_out·RMSNorm(o_t ⊙ S_t q_t)；携带的唯一状态是各 head 的 S_t，可作 Transformer 块中注意力层的 drop-in 替换

## 实验结果（1.5B / 100B tokens / FineWeb-Edu / 8k ctx）

- 语言建模：线性模型 Avg-6 59.72（六任务中五项最佳，超最强对手 KDA +1.6pt），LAMBADA ppl 11.72；hybrid（5:1 linear:SWA-2048）59.56 仍居首
- 2k 真实召回套件（SWDE/SQuAD/FDA/TQA/NQ/DROP）：线性 30.31、hybrid 37.40 均最佳
- RULER NIAH：GDN 系在 16k 外推时崩溃（S2 跌至 17.8），KronLSTM 相对稳健；hybrid 16k 全部任务最佳；MQ 领先随长度增长（4k→16k 从 +2.4 到 +4.1pt）——与干扰分析一致：干扰随上下文增长，最小侵入修订的优势随之放大
- 32k 扩展（75B 处分支+25B ProLong 长文档混合）：ppl 改善约 4 点，KronLSTM 五项召回任务保持领先

## 局限

- S1（高频重复噪声句 NIAH）明显弱于 GDN：重复 key 的残差累积；对真实文本影响小
- 干扰保护是重叠门控而非消除；DeltaNet 稳态范数界常数更小，KronLSTM 的优势在更长的初始记忆保留而非更紧的界
- 忘记门为 1 时（κ≤1 分析）外推仍会衰减——长上下文仍需 length extension 训练

## 实践指南

1. 设计线性注意力记忆更新时，优先"修正标量关联 + 输入定方向"而非向量残差方向
2. 并行训练：直接复用 DeltaNet chunkwise WY 形式，特征换 a_t = k_t⊗v_t
3. 稳定性零成本配方：ℓ2 归一化 k,v + sigmoid β → 自动非扩张，免归一化器
4. 需要状态跟踪能力时允许 β‖a‖² ∈ (1,2)
5. 高频重复 key 场景（缓存、模板文本）注意残差累积，靠 forget gate 清理

## 相关 skill

- [[deltanet-pc-test-time-memory]] — DeltaNet 固定点测试时记忆（同族前作）
- [[mamba3-underdamped-oscillatory-dynamics]] / [[lighthouse-attention]] — 其他线性/长上下文架构
- [[memory-attention-lookup-values]] — 关联记忆容量设计
