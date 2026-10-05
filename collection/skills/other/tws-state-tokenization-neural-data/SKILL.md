---
name: tws-state-tokenization-neural-data
category: ai_collection
description: Use when building session-invariant neural data tokenizers.
trigger: 神经数据token化, 跨session解码, population manifold token, Grassmannian token, neuron-free tokenizer, cross-session decoding, neural foundation model generalization, IBL, Utah array transfer
---

# TWS: Tokenization with States — 行为事件边界的跨Session神经数据Token化

**来源**: arXiv:2610.03001 (2026-10-02, Sangyoon Bae & Jiook Cha, SNU)
**一句话**: 神经基础模型的token不该绑定neuron/session身份；以"行为事件之间的population流形状态"为token单元，跨session零适配解码，冻结后可跨物种迁移。

## 问题定义

细胞外电生理每个session记录的神经元集合完全不同（Neuropixels插入位置漂移、阻抗变化、spike sorting产出不同units），**neuron overlap across sessions ≈ 0**。POYO/POYO+/NDT2/CEBRA等神经基础模型为每个neuron/session学embedding → 每个新session都是OoD → 跨session解码坍塌到chance level。

**token化单元的两个必要条件**:
1. 同一个decoder在每个session都能用（session无关）
2. 携带行为意义（semantic）

## 核心洞察

**Population活动在行为事件处分regime切换，两个事件之间的population流形段（state）同时满足两条件**：
- 流形跨session/跨月/跨动物持续存在（Gallego 2020, Safaie 2023）——神经元更替不改变它
- 每个state有独立的行为含义（Elsayed 2016: movement onset后population进入与preparation正交的子空间）

类比NLP token化：per-neuron token = 闭词汇表（无法表示未见词）；单时间bin = 单字符（无语义）。state-level token = subword（BPE）——中间粒度的可复用语义词元。

## 方法（Algorithm 1 完整流程）

**Step 0 — 预处理**（仅用该session的*无标注*活动）:
- spike counts → `log(1+x)` → 按session内trials做per-neuron z-score

**Step 1 — Regime边界分割**（K=3 states）:
```
w1(t) = σ((b_stim − t)/γ)                    # pre-stimulus
w2(t) = σ((t − τ1)/γ) · σ((b_move − t)/γ)    # stim → move
w3(t) = σ((t − τ2)/γ)                        # post-move
τ1 = b_stim + Δ1,  τ2 = b_move + Δ2           # 2个可训练偏移量，全session共享
归一化: w̄k(t) = wk(t) / Σt' wk(t')
```
- 关键细节：population不在事件瞬间切regime，而是延迟后稳定 → 边界带**可训练offset**而非固定
- 转移区间 [b_stim, τ1)、[b_move, τ2) 不属于任何state
- γ = 温度参数（soft sigmoid gates）

**Step 2 — State加权的population摘要**:
```
x̄k = Σt w̄k(t) · x(t) ∈ R^Ns    # 每neuron在state k内的加权平均活动
```

**Step 3 — 流形承诺（Manifold commitment）**:
```
un = f_coord(pn) + f_act(x̄k,n)        # 共享编码器标量→R^256，全state/session共用
rk,j = LN(CrossAttn(qk,j, {un}))       # permutation-invariant聚合，无位置编码，kdim=2 queries per state
{ek,j} = GramSchmidt({rk,j})            # 正交基 ∈ Grassmannian Gr(2, 256)
```
- **置换不变性**：交换任意两个neuron（连同其坐标）→ token不变（softmax无位置编码 + 逐步neuron独立操作）
- Gram-Schmidt的几何（Grassmannian点）本身不关键——跳过它解码差异 < 0.01；关键是不变量

**Step 4 — Backbone + 解码**:
- 6 tokens (3 states × 2) ∈ R^256 → 4层kernel-3 CNN混token → mean pooling → Ridge/linear probe
- 自监督预训练：reconstruct masked state means + 相邻state子空间推正交

## Type A / Type B 变量分类（设计边界）

| 类型 | 定义 | 例子 | 无neuron身份表示能否保留 |
|------|------|------|------------------------|
| Type A | 低维共享子空间，任意大子集neurons都携带 | locomotion, movement, arousal, RT | ✅ 保留 |
| Type B | 解码方向随session变化 | choice, block | ❌ 不必保留（设计代价）|

## 关键实验结果

**IBL 53 held-out sessions（cross-session, leave-one-session-out, MCC）**:
| 方法 | Movement | RT R² | Choice | Block |
|------|----------|-------|--------|-------|
| TWS from scratch | **0.565** | **0.402** | 0.038 | 0.026 |
| TWS pretrained+finetuned | 0.553 | 0.398 | 0.040 | 0.031 |
| PerceiverIO (no embeddings) | 0.303 | 0.169 | 0.014 | 0.011 |
| POYO (pretrained含held-out) | 0.000 | 0.000 | −0.001 | −0.000 |
| CEBRA / NEDS (per-session) | 0.000 | 0.000 | — | — |
| PCA (aligned) | 0.349 | 0.226 | — | — |

**冻结迁移（mice训练 → 仅linear probe）**:
- Steinmetz 2019: choice 0.151, feedback 0.188, movement 0.581 — 全部超过在目标数据上训练的POYO
- Gallego Utah array (macaque): reach direction 0.232（event time本身只0.011）；NLB movement 0.392

**Tokenizer > Backbone**（2 tokenizer × 6 backbone 交叉）:
- backbone间差异 ≤5%；换掉TWS tokenizer → 解码减半
- session identity占embedding方差: PerceiverIO 31% vs TWS 19%（pretrained后）；movement: 1% vs 11%

**边界消融**（证明event边界的必要性）:
- jitter σ=5 bins → −7%；fixed/random/shuffled边界 → −62~70%
- **训练无法修复错误分割**：错误边界+40 epochs行为训练 < 正确边界的random init

**数据效率**: 仅5个带标签session的probe → RT解码比全部session训练的baseline好5x

**鲁棒性**: 只用1/4 units → 保留83% movement解码

## 使用场景与实现指南

1. **跨session/跨实验室/跨物种神经解码**：不要学neuron/session embedding；用事件分割+置换不变聚合
2. **神经基础模型token化设计**：任何"每个输入unit一个embedding"的设计在unit集合变化时都会坍塌
3. **实现骨架**: event times → soft gates(可训练offset) → state加权平均 → 共享标量编码器 → cross-attention(无位置编码) → Gram-Schmidt → 小CNN backbone → linear probe
4. **限制**: 需要任务记录的event times（自由行为需要数据驱动的regime发现）；regime内时间过程被平均掉；Type B变量不保证

## 相关技能
- `neurolens-jepa-chronic-recordings`（JEPA慢性记录表征，同一"记录不稳定 vs 可塑性"问题空间）
- `meta-learning-in-context-brain-decoding`（跨subject训练无关解码）
- `unibci-invasive-foundation-model`
