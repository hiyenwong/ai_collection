---
name: lighthouse-attention
description: "Long Context Pre-Training with Lighthouse Attention — NousResearch 提出的对称选择式分层注意力算法。面向超长上下文预训练，通过对称 Q/K/V 金字塔池化、无参数打分 top-K 选择、选择与注意力解耦、两阶段训练，实现 O(N·d) 复杂度。触发词：lighthouse attention, long context pretraining, hierarchical attention, symmetric pooling, sparse attention, FlashAttention wrapper"
---

# Lighthouse Attention — Long Context Pre-Training

> NousResearch (2026.05) 提出的面向超长上下文预训练的分层注意力机制，通过对称 Q/K/V 金字塔池化 + 无参数 top-K 选择 + 标准 FlashAttention，实现 1.4–1.7× 端到端加速，最终模型可完全恢复为 dense SDPA。

## Metadata
- **Source**: arXiv:2605.06554v1 [cs.CL]
- **Authors**: Bowen Peng, Subho Ghosh, Jeffrey Quesnelle (NousResearch)
- **Published**: 2026-05-07
- **Code**: https://github.com/ighoshsubho/lighthouse-attention

## Core Methodology

### 四阶段 Pipeline

Lighthouse 用四阶段流水线替换标准 attention 层，**不修改注意力核本身**：

```
输入 X → Q,K,V 投影 → 金字塔池化 → 打分 & top-K → 密集 gather → FlashAttention → scatter-back → 输出 O
                                                        ↑
                                               选择逻辑在注意力核外
```

#### 阶段 1: 金字塔构建 (Pyramid Construction)
- 对 Q, K, V **对称**做 L 层平均池化，池化因子 p
- 第 ℓ 层：Q_i^(ℓ), K_i^(ℓ), V_i^(ℓ) 是 p^ℓ 个连续 token 的均值
- Level 0 = 原始全分辨率；每层向下一层总结 p 个连续项
- 总条目数 ≤ N·p/(p-1)，Θ(N) 时间和内存

**关键差异**: NSA/HISA/InfLLM-V2 只池化 KV 侧；Lighthouse 对称池化 Q/K/V 三者

#### 阶段 2: 打分与选择 (Scoring & Selection)
- **打分函数** (无参数): s_QK = ||Q||₂, s_KQ = ||K||₂ (ℓ₂ 范数)
- 粗层通过 max-pool 从 level 0 继承，不重新计算
- top-K 选择所有层中最高的 k 个条目
- 最粗层始终全部保留，剩余预算用于更细层
- **不**使用 straight-through estimator 或 Gumbel softmax

#### 阶段 3: 密集子序列注意力
- 将选中的三元组 gather 为长度 S 的连续子序列
- S = N/p^(L-1) + (L-1)·p·k
- 标准 FlashAttention 计算: Õ = Attn(Q̃, K̃, Ṽ; M̃)
- 因果掩码从金字塔坐标推导，为标准 S×S 因果掩码

#### 阶段 4: Scatter-back 重建
- 每个 level ℓ 的选中条目写回偏移范围 R(ℓ,i) = [i·p^ℓ + p^ℓ - 1, i·p^ℓ + 2p^ℓ - 2]
- 偏移 p^ℓ - 1 保持因果性
- 跨层贡献求和，每位置扇入 ≤ L

### 两阶段训练

**Stage 1**: 用 Lighthouse 预训练大部分时间 (如 10k steps)  
**Stage 2**: 恢复 checkpoint，用标准 dense SDPA 继续训练 (如 6k steps)  
- 优化器状态和数据加载器保持连续
- Stage 2 结束时 loss 匹配或优于 pure dense baseline

### 梯度流

```
∇L → scatter → FlashAttention → gather → W_Q,W_K,W_V
                     ↑
              top-K 不带梯度，scorer 不训练
```

投影矩阵学习"被选中时有用"的值，而非"擅长打分的分数"。

## Complexity Analysis

| 阶段 | 原语 | 复杂度 |
|------|------|--------|
| Q,K,V 投影 | GEMM | Θ(N·d_model·d) |
| 金字塔池化 | view+mean | Θ(N·d) |
| 打分 (范数, max-pool) | norm+max | Θ(N·d) |
| Top-K 选择 | chunked bitonic | Θ(N·log k) |
| Gather | torch.gather | Θ(S·d) |
| 密集子序列注意力 | FlashAttention | Θ(S²·d) |
| Scatter-back | custom atomic | Θ(N·d) |

S = Θ(k·log N) 当 L = log_p(N/k) 时  
**总复杂度**: Θ(N·d)（有界 k 下）

## Kernel Design

### Chunked-Bitonic Top-K
- 分数流分区为 N_chunk=2048 大小的块
- 每块维护 in-register top-m 缓冲 (m=128)
- 通过寄存器内双调合并更新
- 分块作为独立 CTA 分发
- **分层 top-K**：保证序列每个区域都有贡献，避免选择坍塌

### 选择-注意力解耦
- 选择产生密集连续子序列 → 标准 FlashAttention
- 训练和推理使用同一核
- 禁用选择即可完全恢复 dense baseline
- 支持标准 ring attention 进行上下文并行

## Experimental Results

### 530M Llama-3, 98K context, C4 dataset
| 配置 | 最终 Loss | Tok/s/GPU | B200-Hrs |
|------|-----------|-----------|----------|
| SDPA Baseline | 0.7237 | 45.6k | 303.2 |
| LH(k=6144)+SDPA | 0.6980 | 75.0k | 228.0 |
| LH(k=1536)+SDPA | 0.6825 | 93.9k | 203.9 |

### 加速比
- 98K: 1.4–1.7× 端到端加速
- 512K: 前向 21×，前向+反向 17.3×
- 1M token: 32×Blackwell GPU, CP=8

## 设计选择 rationale

1. **对称 Q/K/V 池化** (vs. 非对称): 将 dense kernel 从 O(NSd) 降到 O(S²d)；pooled Q 和 pooled K 在同一表示空间
2. **无参数打分** (vs. 可学习 scorer): 更便宜；是更保守的基准 — 任何正向结果都是下界
3. **选择-注意力解耦** (vs. 融合核): 同一核用于训练和推理；正确性可通过禁用选择来验证
4. **top-K 不可微** (vs. STE): 避免 scorer 坍塌、scorer-注意力不对齐等优化病态

## 局限

- 对称池化假设所有查询在同一前向传播中 — **不适用于自回归解码**
- 依赖 dense-SDPA resumption 获得推理就绪模型
- 内部注意力是 Θ(S²d) — 次二次但非严格线性

## 未来方向

- 用非对称稀疏目标替换 SDPA resumption → 原生可服务 checkpoint
- 每层/每头自适应 k
- 多尺度金字塔扩展到 vision/audio/video
- 服务集成：连续批处理、推测解码、KV-cache 管理

## Applications
- LLM 长上下文预训练加速 (128K–1M+ tokens)
- 多模态长序列理解
- 多步推理 agent 的训练效率提升

## Related Skills
- spiking-quantum-encoding
- quantum-ml-patterns
- speculative-decoding-optimization
- memory-efficient-looped-transformer
