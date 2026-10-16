---
name: neurolens-jepa-chronic-recordings
description: "慢性神经记录跨session表征学习时用。JEPA潜空间预测去噪电极漂移。"
metadata:
  arxiv_id: "2610.02864"
  published: "2026-10-02"
  authors: "Hanrui Lyu, Baiyuan Chen, Tianshu Tan, Matthew R. Whiteway, Maxwell D. Melin, Ji Xia, Linyang He, Bradly C. Stadie, Anne Churchland, Liam Paninski, Yizi Zhang"
  source: "arXiv q-bio.NC, cs.LG"
  tags: [neuroscience, jePA, self-supervised-learning, chronic-recordings, neural-population-drift, few-shot-bci, cross-attention, effective-rank, representation-plasticity, neuropixels, utah-array]
---

# NeuroLens: JEPA 自监督慢性神经记录表征学习

**arXiv 2610.02864** (2026-10-02) — Lyu, Chen, Tan et al. (Northwestern / Cambridge / JHU / Columbia / UCLA / Stanford)。JEPA (Joint-Embedding Predictive Architecture) 自监督框架从慢性（多天）神经记录学习去噪、语义可解码的潜在表征，核心解决"表征可塑性 vs 记录不稳定性"的混淆问题。

## 核心问题

慢性记录（Neuropixels 小鼠 3 个月 / Utah array 人类 ALS 患者 4-20 个月）中，电极漂移、信号退化、记录神经元集合变化会掩盖学习相关的真实神经变化。现有方法三类局限：
1. **流形对齐** (NoMAD, CEBRA) — 假设跨天共享动力学，限制过强
2. **测试时重校准** (CORP, DietCORP) — 需要任务特定伪标签
3. **监督 Transformer** (SPINT, POSSM, POYO) — 绑定预定义解码目标

重建式 SSL (causal NDT) 必须建模记录细节（漂移伪影），而 JEPA 在潜空间预测——只保留时间可预测结构，天然抑制瞬态记录噪声。

## 架构（三组件）

### 1. Day-Adaptive Cross-Attention Encoder
- 每个神经元 spike count 经 MLP `f_proj` → neuron token `u_{t,n}`
- **关键设计**：cross-attention 对 token 顺序不变（permutation-invariant），所以必须注入身份信息
- M 个 learned queries 聚合变长 token 序列 → 固定数 M 个 latent embeddings → 线性投影成 M 维向量 `z_t`
- **每个时间 bin 独立编码**（防时间泄漏），时序建模完全交给 AR predictor

### 2. Calibration-Based Neuron Identification（核心创新）
- 每天用少量 calibration trials 计算每个神经元的生理签名：firing-rate stats (5d) + autocorrelogram (20d) + population coupling (16d) → 41 维签名
- MLP `h_id` 将签名映射为 neuron embedding，与 region embedding 拼接、投影后加到 spike token 上
- **vs 固定 ID embedding (POYO/POSSM)**：签名身份可迁移到未见神经元，性能相当（附录 H 消融）
- **人类 Utah array 例外**：通道是混合信号非 spike-sorted 单元，签名会造成坍缩 → 改用 MLP encoder + hypernetwork 按天生成 FiLM 参数适配通道漂移

### 3. Causal Transformer AR Predictor
- 跨天共享参数，预测未来 latent：`ẑ_t = f_pred(P_θ(z_{1:t-1}))`
- 共享性强制稳定预测结构跨天一致

## 训练目标

```
L = L_pred + λ·L_sigreg
L_pred = MSE(ẑ_t, z_t)                      # 潜空间预测
L_sigreg = 特征函数匹配正则 (SIGReg)          # 防表征坍缩
```

**SIGReg** (Balestriero & LeCun 2025, LeJEPA)：随机投影 `a_j^T z` 的经验特征函数匹配各向同性高斯 `e^{-ξ²/2}`，K=17 个 Gaussian-weighted 梯形积分点 ξ∈[0,3]。无需 stop-gradient/非对称架构等启发式。

## 三种适配模式（预训练后）

| 模式 | 需要什么 | 更新什么 |
|------|---------|---------|
| **GF (gradient-free)** | 64 calibration trials 计算签名 | 无参数更新——只用预训练 h_id 推断新神经元身份，linear decoder 在冻结表征上训练 |
| **GB (gradient-based)** | calibration trials | 只更新 read-in 层（f_proj, h_id, f_fuse）+ decoder head；cross-attention、region embeddings、AR predictor 冻结 |
| **Full fine-tuning** | 足够新 session 数据 | 全模型（语音等难任务需要） |

## 关键结果

- **小鼠 IBL**（53 天 Neuropixels）：choice 解码比 causal NDT +6%，movement +2%；latent effective rank 更低但信息更浓（更紧凑）
- **人类 T12/T15**：sentence-embedding 解码 +38% vs causal NDT，phoneme 解码 +4-16%
- **泛化**：预训练 39 天 → 14 held-out 未来天，GF 模式（零梯度更新）choice 解码仍超 SPINT/POSSM/causal NDT
- **表征漂移分析**：raw spike RSA 相似度随天间隔增大而骤降；NeuroLens latents 保持稳定
- **Effective rank 稳定性**：causal NDT 的 rank 随记录神经元减少（159→更少）同步下降；NeuroLens 跨天保持稳定——分离任务相关变化与记录非平稳性

## 复用要点

1. **潜空间预测替代重建**：任何存在"观测噪声与信号解耦"需求的神经 SSL 任务，JEPA 目标优于 MAE/重建目标
2. **签名式身份编码**：跨 session/被试/电极迁移的标准做法——生理签名（FR+ACG+coupling）比 ID embedding 更通用
3. **GF few-shot 适配**：冻结 encoder + 签名重推断 = 无梯度 day-to-day 适配，BCI 校准的新范式
4. **有效秩作为非平稳性探针**：latent effective rank 跨天轨迹可区分"表征漂移"与"记录退化"
5. **通道 vs 单元**：spike-sorted 单元用签名+cross-attention；混合通道信号用 hypernetwork FiLM 按天条件化

## 数据与资源

- IBL chronic Neuropixels (Melin et al. 2024)：视觉决策任务，53 sessions/47h，16.7ms bins
- 人类数据：T12 (Willett et al. 2023) 23 天，T15 (Card et al. 2024) 45 天，ALS 语音
- 句子语义：all-MiniLM-L6-v2 384 维 embedding，top-5 retrieval 评估
- 基线：causal NDT, CEBRA, SPINT, POYO, POSSM（容量对齐，附录 K）

## 局限

- 未解耦"学习引起的变化"与"内在神经变化"（行为联合建模是未来方向）
- 未建模跨脑区交互/区域特定漂移
- 语音解码需要 full fine-tuning，GF/GB 不足

## 相关技能

- `eeg-fm-audit-systematic-evaluation` — EEG 基础模型系统评估
- `meta-learning-ict-brain-decoding` — 跨被试免训练解码
- `identity-trap-eeg-foundation-models` — 基础模型身份陷阱（与签名身份设计互补）
- `eeg-channel-adaptation-benchmark` — 通道适配方法基准
