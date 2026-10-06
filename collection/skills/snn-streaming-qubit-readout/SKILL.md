---
name: snn-streaming-qubit-readout
description: Use for real-time superconducting qubit readout with spiking neural networks on FPGA. Streaming SNN discriminators.
version: 1.0.0
created: 2026-10-03
author: Hermes Agent
category: neuroscience
metadata:
  arxiv_id: "2610.02129"
  published: "2026-10-01"
  authors: "Barry M. Dillon, Aqib Javed, Jim Harkin, Patryk Dabkowski, Benjamin Lienhard"
  tags: [spiking-neural-networks, qubit-readout, superconducting-qubits, fpga, hls4ml, streaming-inference, quantisation-aware-training]
---

# SNN Streaming Qubit Readout：脉冲神经网络的流式量子比特判别

## 核心问题与突破

**问题**：超导量子处理器的读出是最易错、最耗时的操作之一。频率复用读出使态指派成为**内生多变量**问题——测量迹线含串扰（crosstalk）、弛豫事件、瞬态非理想性，传统匹配滤波（MF）无法捕获。ANN 判别器虽能学非线性映射，但**必须等完整读出脉冲采集完才前向推理**——总延迟 = 脉冲时长 + 推理延迟。在反馈/QEC 循环中，决策必须快到能在编码信息改变前行动。

**突破**：SNN 判别器**按时间块（chunk）顺序处理读出信号**，在数据到达时持续更新分类得分与比特指派，而非等读出窗口结束。LIF 神经元的内部状态天然提供跨 chunk 的记忆。配合 QAT + hls4ml 综合，**每次 FPGA 推理更新在下一个读出块到达前完成**（31-52ns < 100ns chunk 时长）。

**性能**：在 5 比特 transmon 频率复用读出基准（Lienhard 数据集，32 个计算基态全标注）上：
- MF 基线 F_geom = 0.8960
- 最佳 ANN（10-step, 128 hidden, L5+C5）= 0.9100
- 最佳 SNN（10-step, 128 hidden, L5+C5）= **0.9084**——以显著更小的网络和流式更新逼近 ANN，且给出实时中间指派
- 64-dim SNN 的串扰矩阵最干净（最大非对角元 0.0130 vs ANN 0.0159）
- QAT 到 8-bit 定点仅损失 5×10⁻⁴ F_geom，12-bit 饱和

## 方法论详解

### 1. 数据与特征构造（可复用管线）

**基准数据集**（Lienhard et al.）：5-qubit transmon 处理器（4.3-5.2 GHz，T1 7-40µs），各耦合独立读出谐振腔（7-7.25 GHz），共享馈线频率复用传输测量。32 个计算基态全标注单-shot 测量，每次含 1µs 时间分辨 IQ 迹线（2ns 采样 → N=500 样本/通道）。

**分块特征**（关键设计）：ADC 在数据流入时把 1µs 流分成 T 个块（T∈{5,10}，即 200ns/100ns 每块），对每块取平均：

- **局部特征 L5(t)**：当前块的每比特 (I,Q) 均值 → 10 维向量
- **累积特征 C5(t)**：从 0 到当前的所有历史贡献之和 → 10 维向量

```
L5(t) = (1/M) Σ_{n∈S_t} [I_q(n), Q_q(n)]_q=1..5     (S_t = 当前块样本索引集)
C5(t) = (1/(tM)) Σ_{n=0}^{tM-1} [I_q(n), Q_q(n)]_q=1..5
```

**注意**（论文诚实披露）：C5 特征的增益不完全来自其信息内容——ANN 和 SNN 都能从纯 L5 内部重建累积特征。真正驱动因素是**更大的输入维度增加了参数量**，在严格延迟/资源约束下给了网络更多容量。

### 2. 网络架构与训练

**SNN**：一次一个时间步，LIF 隐层 + 膜积累读出：

```
Linear(R^d → h) → Dropout(0.02) → LIF(h) → Linear(h → 5)
h ∈ {32, 64, 128}, d ∈ {10 (L5), 20 (L5+C5)}
```

- LIF 动力学：`u_{t+1} = β·u_t + w·x_{t+1} − β·y_t·u_thresh + b`，spike `y_t = 1[u_t ≥ u_thresh]`
- **可学习 β**（初始化 0.75）、阈值 1.0、**减法 reset**（subtractive）
- 读出用**膜积累无衰减**（β_ro = 1.0）——每个时间步后输出 5 个 logits，固定零阈值出比特预测
- 训练：surrogate gradient（snnTorch），bitwise binary cross-entropy with logits（每比特独立 BCE），默认只在最后 chunk 施加损失
- AdamW，SNN lr=1.2×10⁻²（无 weight decay），batch 1024，ReduceLROnPlateau(factor 0.5, patience 10)，early stop 30 epochs（增益 <10⁻⁵），最多 250 epochs
- checkpoint 按验证集**几何均值指派保真度**选择

**ANN 基线**：展平全时间序列 `x_i ∈ R^{T×d}` → Linear(Td→128) → Dropout(0.02) → ReLU → Linear(128→5)。

**数据规模**：432k 训练 / 48k 验证 / 1.12M 测试迹线，32 态均衡。

### 3. 度量：几何均值指派保真度

对 5 比特 32 类问题，**F_geom = (∏_q F_qq)^{1/5}**，其中 F_qq 是 qubit q 的对角交叉保真度（正确指派率）。几何均值惩罚弱比特——本数据集 q2 是主导限制（F_22 ≈ 0.48-0.49，ML 方法无法大幅改善，增益主要来自其他比特）。

### 4. QAT 定点化（部署关键）

- 权重 + 神经元电位：ap_fixed<W,4>，W ∈ {8,10,12,16}（4 整数位）
- 读出膜态：ap_fixed<16,8>（16 位 8 整数位）
- **累加器例外**：ap_fixed<18,8> 且用**截断 + wrap**（非四舍五入/饱和）——给累加器加四舍五入和饱和会显著拖慢 FPGA 前向 pass（延迟原因）
- 全网络其他处用 rounding + saturation
- QAT 微调：AdamW lr 5×10⁻⁴，最多 100 epochs，early stop 20 epochs
- 结果：L5+C5 10-step 在 W=8 仅损 5×10⁻⁴，W=10 饱和

### 5. FPGA 综合（hls4ml + Vitis）

- 目标器件：**XCZU49DR**（Zynq UltraScale+，xczu49dr-ffvf1760-2-e）
- 全并行 I/O（io_parallel），latency-optimised dense 层，reuse factor 1
- 目标时钟 **8.0 ns**（125 MHz），时钟不确定性 18%
- **结果：所有配置 initiation interval = 1，每时间步延迟 31-52 ns**——低于最短 100ns 读出块，SNN 推理可在下一块到达前完成，实现采集期间连续更新
- 报告延迟**仅含 SNN 推理内核**——不含解调、平均、数据传输逻辑（论文明确披露）
- 资源：hidden 32→128 约线性放大 LUT/DSP；FF <1.3%；**8/10-bit 配置不用 DSP**（乘法用 LUT 实现），12/16-bit 逐渐映射到 DSP——精度选择改变算术到器件的映射方式

## Pitfalls

1. **流式 SNN 的准确率天花板略低于全迹 ANN**——这不是缺陷而是权衡：换得实时中间指派与早期分类可能。论文明确以"ANN 不显著更好"立论，勿夸大为 SNN 更准
2. **C5 特征增益主要是容量效应**——复现时若只用 L5 也应接近；不要把特征工程收益误读为信息论收益
3. **累加器必须截断+wrap**——QAT 中模拟此行为，否则综合后精度崩塌
4. **bitwise BCE 只在最后 chunk 施加**是默认配置；中间步损失可探索早期分类质量
5. **q2 类瓶颈不可用 ML 消除**——数据集内在限制（弛豫/串扰主导），先诊断哪个比特限制 F_geom 再调架构
6. **延迟报告口径**：hls4ml 综合估计不含 demod/传输——完整流水线预算需另计
7. **采样率适配**：2ns 采样太细，必须先分块平均（ADC 端完成）再进 SNN——块时长决定更新频率与信息粒度的权衡

## 与相关工作的关系

- **Lienhard et al.**（数据集来源）：全连接 ANN 多比特判别器，相比当代传统判别器减少 25% 指派误差、一个数量级串扰——但需完整迹线
- **reservoir computing 读出**：时间分辨但非流式可更新
- **HMM（HMM 弛豫检测）**：时间结构敏感但无 FPGA 低延迟路径
- **LHC SNN 应用谱系**（hls4ml 扩展）：触发过滤、径迹重建、量热器读出——本文把该谱系推进到量子控制 µs 时域
- hls4ml SNN 支持来自近期扩展（window-size logic），本文首次用于量子读出

## 实现路线图

1. 获取基准：Lienhard 5-qubit 频率复用数据集（32 态标注 IQ 迹线）
2. 特征管线：分块平均 → L5/C5 标准化（训练分割统计量）
3. snnTorch 训练：LIF 隐层 + 膜积累读出，bitwise BCE，验证集 F_geom 选 checkpoint
4. QAT：W∈{8,10,12,16} 扫描，累加器截断/wrap 模拟
5. hls4ml 综合：io_parallel，reuse=1，8ns 时钟，验证 II=1 且延迟 < chunk 时长
6. 流式评估：每 chunk 后的中间指派质量曲线（时间到准确率的权衡前沿）

## Applications

- 超导 QEC 循环的实时 syndrome 测量读出
- 反馈控制（如主动 reset）中读出-决策延迟压缩
- 频率复用多比特读出的串扰校正
- 更广的时间关键科学推理：LHC 触发、中微子事例、辐射检测的 SNN 谱系推广
- 神经形态 + 量子控制的交叉范式：µs 时域 FPGA 推理引擎

## Sources

- arXiv: 2610.02129 (submitted 1 Oct 2026)
- Dataset: Lienhard et al. 5-qubit multiplexed readout benchmark
- Tools: snnTorch (training), hls4ml + AMD Vitis HLS (synthesis), XCZU49DR
