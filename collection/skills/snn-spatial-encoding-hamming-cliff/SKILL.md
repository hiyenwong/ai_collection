---
name: snn-spatial-encoding-hamming-cliff
description: SNN input encodings preserving semantic distance; hybrid coarse-fine codes.
category: ai_collection
---

# Beyond the Hamming Cliff: Compact Spatial Encodings in SNNs (arXiv:2610.22083)

**Davies, Aitsam, Stone, Di Nuovo, Han** (2026-10-15, cs.NE; Manchester Met Univ + Sheffield Hallam + Catania)

SpiNNaker 硬件上的系统性研究：SNN 空间编码的**码几何**如何决定监督 STDP 网络的稳态缩放、容差半径与假阳性行为。核心发现：消除 Hamming cliff 是必要但不充分的——Gray 编码消除 cliff 却几乎不保留全局距离结构。

## 问题背景

- **空间编码**：值以同时尖峰模式呈现（每 bit 一根突触），无积分窗延迟，决策延迟仅由网络深度决定——但分类依赖二进制码字几何
- **Hamming cliff**：标准二进制中 127(01111111) 与 128(10000000) 相差全部 8 bit；语义相邻 → 码空间最远
- 后果（Davies et al. 2025 已证）：训练码字间大 Hamming 距离产生 "don't care" 突触（权重对消）→ 需更强 homeostatic 缩放 → 假阳性激增
- Binary cliff 严重度 = 8（49.8% 相邻对耗费 >1 bit，几何分布尾部）；其余所有编码严重度 = 1

## 关键区分：局部平滑 vs 全局距离保持

| 编码 | 宽度(N=256) | 局部相邻=1bit | 全局单调性 ρₛ (Spearman) | 邻域质量 |
|---|---|---|---|---|
| Binary | 8 | ✗ (cliff) | 0.323 | 7+ 碎片段 |
| Gray | 8 | ✓ | **0.374**（vs d_cyc 0.392）| 7+ 碎片段，达 144 语义单位远 |
| Thermometer | 255 | ✓ | **1.000** (vs d_lin) | 单一连续区间 |
| Johnson | 128 | ✓ | **1.000** (vs d_cyc) | 单一连续区间（环形）|
| Hybrid lin B=4 | 65 | ✓ | 0.998 | ≤B 段 |
| Hybrid lin B=8 | 34 | ✓ | 0.990 | ≤B 段 |
| Hybrid cyc B=4 | 34 | ✓ | 0.996 | ≤B 段 |
| Hybrid cyc B=8 | 19 | ✓ | 0.980 | ≤B 段 |

**Gray 的陷阱**：反射构造使任意 v 与 2^W-1-v 恒差 1 bit → Hamming 球内值散布于 7 个不连续段、可达 144 单位远——与 Binary 无异。局部平滑足够局部聚类，不足以跨范围判别。

## 混合编码族（本文贡献）

**构造**：值 v 按 block size B 分解为块索引 b=⌊v/B⌋ + 块内偏移 r=v mod B：
- **粗场**：Thermometer（线性变体）或 Johnson 环（循环变体）编码 b —— 保距离但宽
- **细场**：log₂B-bit Gray 编码 r —— 紧凑但只保局部结构
- **关键创新——反射**：奇数块中偏移反射 r ↦ B-1-r，使相邻值（含块边界）恒差 1 bit
- 宽度公式：W_lin(B) = N/B - 1 + log₂B；W_cyc(B) = N/2 + log₂B（B<N/4 时与 Gray 逐位相同）

**极限情形**（B 为单参数插值）：B=1 → Thermometer/Johnson；B=N/2 → Gray。三种经典编码是同一连续统上的点。

**宽度-结构交换强非线性**：255→34 bit（×7.5）只损失 ρₛ 从 1.000→0.990；34→8 bit 再缩 4 倍几乎损失全部剩余结构（0.990→0.374）。

## 硬件机制（SpiNNaker 实测，131,072 次穷举分类）

### 1. 容差定律（核心定量结果）
双轨布线下失配 bit 使驱动损失 2w。增益 m 倍最小时接受半径：
```
h(m) = ⌊ W(1 - 1/m) / 2 ⌋
```
- 256 条件中 238 个接受集**精确匹配**预测（内容逐值一致）；18 个偏差 ≤1 bit 且总偏向更宽容
- 网络在码空间画 Hamming 球，**编码独自决定该球的语义含义**：Thermometer/Johnson → 连续区间；循环码在范围端环绕；Binary/Gray → 散射值集

### 2. 多模式缩放可预测（Eq.12）
双极表示 tᵢ∈{-1,+1}^W 下 Σ 训练得权重向量 Σᵢtᵢ，训练值 j 的驱动 = 内积：
```
⟨t_j, Σᵢtᵢ⟩ = W·n + Σ_{i≠j}(W - 2H_ij)
```
- 所需 homeostatic 因子 = nW / min_j(驱动)，**仅从训练码字两两 Hamming 距离即可预测**（40 条件最大偏差 0.03）
- Binary n=3 时需 4.03× 相干值（预测 4.00）；Thermometer/Johnson/hybrids 保持 ≤1.21×
- Gray 假阳性为零但因子升至 1.61× —— 弱全局结构先消耗稳态余量后产生错误

### 3. 检测邻域尺度不变律
结合容差定律与块结构：语义半径 r = B·h(m) ≈ N/2(1-1/m)（线性）或 N/4(1-1/m)（循环）——**块大小约去，检测邻域只依赖值域、增益与拓扑**，与码宽无关（Thermometer 255 bit 与 hybrid 34 bit 在 ×8 时同样接受到 111/112 单位远）。

### 4. 硬件输入容量限制（首次系统测量）
- **SpiNNaker**：sPyNNaker 默认 buffer 256 槽（1 空）→ 255 packets/神经元/timestep，**静默软件截断**（无报错，下游指标仍貌似合理）；扩大到 1024 槽解除。静态突触下边界模糊（drain-while-fill，385 后仍有 ~2/5 到达）
- **SpiNNaker2**：512 输入事件硬截断（513 输入产生精确 512 偏转），事件数而非电流或单源流量限制
- 空间码每决策花费 W packets：Thermometer@256 值 = 255 bit 逼近上限；hybrids 在 1024 值时 36-130 bit 内安全

## 1024 值扩展验证
Binary 严重退化：n=2 时接受 125 个未训练值（precision 0.016）——接受集是"共享 3 个高位 bit 的整块 896-1022"，纯码结构产物。Hybrids 保持相干（≤1.10×）且 16 条件中 13 个零假阳性，假阳性对齐块结构、聚集在训练簇 28 单位内。

## 实践准则
1. **按变量拓扑选码**：有界量用线性族（Thermometer→hybrid lin）；周期量（时刻/角度/相位）用循环族（Johnson→hybrid cyc）
2. 范围适配输入上限时用 Thermometer/Johnson（精确距离保持）
3. 超限时选**最小块尺寸**使其宽度适配上限——小块保持邻域更连续
4. 多特征拼接时注意：Hamming 距离是逐特征距离之和，容差半径作用于总和 → 一特征大偏差可被其他特征精确匹配抵消；需逐特征检测器或特征加权
5. 检查 SpiNNaker 默认 buffer：训练时 >255 bit 码会被静默截断

## 局限（作者自述）
- 合成值穷举协议（非下游任务）；单一架构/单输出神经元；慢于实时运行（未测宽码实时处理成本）
- 权重向量为独立训练后求和（线性理想化），非在片顺序 STDP 学习（后者不线性、权重上限会饱和 ≥6 值共享突触）
- hybrids 的接受集被 Gray 细场碎段化（≤B 段），假阳性不如 Thermometer 集中

## 与相关技能的边界
- vs `spike-nvpt-robust-visual-prompts`：本文是**输入编码层**（每 bit 一尖峰的码字几何），非 prompt/训练层
- vs `temporal-coding-thousand-brains-spiking`：本文纯空间（同时尖峰零积分窗），非 rank-order
- 代码与数据公开：github.com/sergiodavies/EncodedSpatialLearningCodeAndDataset

**Activation**: hamming cliff, spatial encoding SNN, Gray code neural, thermometer encoding, Johnson code, SpiNNaker, homeostatic scaling STDP, semantic distance code, dual-rail SNN, neuromorphic input encoding, false positive tolerance radius, coarse-fine hybrid code
