---
name: cmos-analog-neuron-noise-reliability
version: 1.0.0
description: Use when analog spiking neurons face noise. Jitter and TUR.
category: ai_collection
tags: [neuromorphic-hardware, analog-spiking-neuron, jitter, stochastic-thermodynamics, thermodynamic-uncertainty-relation, spike-timing-reliability, excitability]
source_paper: "arXiv:2610.06720"
source_authors: "Léopold Van Brandt, Alon Ascoli, Michele Bonnin, Grégoire Brandsteert, Denis Flandre, Jean-Charles Delvenne (UCLouvain/PoliTo)"
source_date: "2026-10-05"
---

# CMOS 模拟脉冲神经元的噪声-可靠性权衡

**论文**: Interplay between Excitability and Noise in Analog Spiking Neurons (arXiv:2610.06720, 2026-10-05)
**作者**: Van Brandt, Ascoli, Bonnin, Brandsteert, Flandre, Delvenne — UCLouvain / Politecnico di Torino（ERC-Synergy SWIMS）

## TL;DR

在工业级瞬态噪声 SPICE（NOISETRAN，65nm foundry compact models）下复现 Mainen-Sejnowski (1995) 经典神经科学实验于 **CMOS 模拟脉冲神经元**（简化 Morris-Lecar，V_DD=200mV，4-fJ/spike 架构）：恒定阈上激励 → 振荡 regime，ISI jitter 随周期**线性累积**（相位噪声随机游走）；时变激励（frozen 滤波高斯噪声，DC 分量阈下）→ 兴奋性 regime，每个脉冲由**受控状态转移**触发，jitter 大幅降低。可靠性-耗散权衡由**随机热力学不确定关系 (TUR)** 定量刻画：振荡/rate-coding regime 在物理上受 TUR 下界约束，而兴奋性 regime 天然规避之。

## 电路与仿真设置

- **电路**: ULP CMOS 模拟神经元（Sourikopoulos 2017, 4-fJ/spike, 65nm），简化 Morris-Lecar 电路——两个反相器实现 Na⁺/K⁺ 通道电导，输入 i_ex，输出 v_GK；代表 AdEx LIF 等现代神经形态核
- **噪声源**: 晶体管热噪声，**状态依赖**（非外加白噪声）——通过工业 SPICE 瞬态噪声框架注入真实器件噪声（对比既往理论工作"外加固定强度白高斯噪声"的缺陷）
- **实验 A（振荡 regime）**: 恒定 i_ex = 7.5 pA（阈上）→ 自持振荡，25 次 trial
- **实验 B（兴奋性 regime）**: frozen 滤波白高斯噪声，DC=5pA（阈下）+σ=20pA，τ=5µs（复刻 Mainen-Sejnowski 刺激协议，滤波核 h(t)=t·exp(−t/τ)/τ²）

## 核心发现

### 1. 两个 regime 的 jitter 行为

| Regime | 激励 | 脉冲机制 | Jitter 演化 |
|--------|------|----------|------------|
| 振荡 (rate-coding) | 恒定阈上电流 | 自持极限环（限周期）| **线性累积** σ_jitter ∝ t（相位噪声逐周期累加）|
| 兴奋性 (temporal-coding) | 时变阈下+涨落 | 受控状态转移（resting→spike 由输入涨落触发）| **受抑**，trial 间 spike time 紧对齐 |

- 兴奋性 regime 中少数 spike（如第 4、15 个）仍高变异——归因于**内在噪声主导的类双稳态随机状态转移**（与亚阈值 SRAM 位翻转机制同源，见 Van Brandt 2023/2025）

### 2. 热力学不确定关系 (TUR) 刻画权衡

- TUR（适用于一般过阻尼耗散随机动力系统）：精度 × 耗散 ≥ 界，即降低 jitter（提高定时精度）需以增大耗散/熵产为代价
- **振荡 regime 落入 TUR 约束**：恒流驱动下精度-耗散权衡由热力学强制——rate coding 的可靠性上限是物理性的
- **兴奋性 regime 规避 TUR**：时变输入下脉冲不再是自由振荡相位的读出，而是输入调度的状态转移事件——**temporal coding 借输入涨落获得噪声免疫**，为神经形态 event-based 计算的噪声鲁棒性提供热力学层面的正面证据

## 方法论（可复用）

### 1. 瞬态噪声 SPICE 协议（区别于外加噪声建模）
- 用 NOISETRAN 类瞬态噪声分析（foundry compact model 兼容）而非微分方程外加白噪声——保留器件噪声的**状态依赖性**
- frozen-noise 协议：同一噪声实现注入所有 trial → 直接量化 intrinsic jitter；跨 trial spike raster 对齐度即可靠性指标
- jitter 累积曲线（σ vs spike index）：线性 → 振荡 regime；饱和/受抑 → 兴奋性 regime

### 2. 判据移植：什么任务该用哪个 regime
- 需要长程规则脉冲列（振荡器/中央模式发生器）→ 接受线性 jitter 或提高耗散
- 需要 precise spike-time 信息编码 → 用时变/事件驱动激励进入兴奋性 regime
- 神经形态芯片核选型：AdEx/LIF 类核在 temporal coding 下有噪声优势——不牺牲功耗

### 3. TUR 作为硬件预算工具
- 给定可接受 jitter，TUR 给出最小耗散下界 → 反推供电/偏置预算
- 评估 memristive/CMOS 混合神经元时：先问"哪个 regime、TUR 是否适用"，再谈精度

## 应用方向

1. **神经形态芯片设计**: temporal-coding 架构（Loihi类）在器件噪声下有物理层优势；rate-coding 块需注入刷新/锁相代价
2. **脉冲编码选型**: 对噪声敏感的下游任务（SNN 推理、temporal 感知编码）优先事件驱动激励
3. **可靠性-能耗联合优化**: TUR 把"可靠性预算"翻译成"能耗预算"——芯片级 EDP 优化新维度
4. **生物一致性验证**: CMOS 神经元复现 Bryant-Segundo 1976 / Mainen-Sejnowski 1995 神经科学实验——silicon neuron 可靠性基准测试协议

## 局限

- 仿真仅限单神经元、两类激励；网络级 jitter 传播未涉及
- TUR 论证限于过阻尼框架；Morris-Lecar 电路的完整随机热力学模型留作未来工作
- 未与 memristive neuron（Ascoli 2025 neuristor）在同一协议下对比

## 关键引用

- Mainen & Sejnowski 1995 (Science) — 时变刺激下 spike timing 可靠性原型实验
- Bryant & Segundo 1976 — 白噪声分析始祖
- Sourikopoulos et al. 2017 — 4-fJ/spike 65nm CMOS 神经元架构
- Sepulchre 2022 "Spiking control systems" — 兴奋性/控制视角
- 联系本库: [[snn-temporal-vulnerability-census]], [[analog-interaction-systems-ais]], [[spike-timing-neuronal-assemblies]], [[heterogeneity-sr-liquid-computing]]

## Activation

cmos analog neuron, spike timing jitter, excitability regime, thermodynamic uncertainty relation, neuromorphic noise, mainen sejnowski, transient noise simulation, rate vs temporal coding
