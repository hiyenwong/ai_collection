---
name: parallel-multi-qpu-fragment-quantum-chemistry
description: Use when distributing quantum chemistry across multiple QPUs. FMO shot/fragment parallel.
category: ai_collection
metadata:
  arxiv_id: "2610.07702"
  published: "2026-10-06"
  authors: "Herrmann et al. (Quantum Brilliance + ORNL)"
  source: "arXiv quant-ph"
---

# 多QPU并行执行分片量子化学：FMO–QWFS 工作流实证（Parallel Multi-QPU FMO–QWFS）

**论文**: "Demonstration of Parallel Multi-QPU Execution for Fragment-Based Quantum Chemistry Using On-Premises Hardware" (arXiv:2610.07702, Quantum Brilliance + Oak Ridge National Laboratory, 2026-10)

## 核心发现

首个在**真实多 QPU 硬件**上演示分片量子化学并行化的实验。三台室温金刚石 NV 色心 Quoll 量子计算机（部署于 ORNL）并行执行 FMO2（Fragment Molecular Orbital）+ QWFS（Quantum Wave Function Sampler）计算 He₂–He₁₄ 团簇总能量。两种互补并行模式均提升采样吞吐量且不损失化学精度（1.4×10⁻³ a.u.）。

## 两种并行模式（核心方法论）

### 1. 同步 shot-parallel（采样级并行）
- 多 QPU 联合采样同一 QWFS 电路，SPAM 校正后合并为单一概率分布
- **负载均衡公式**：`N_i = N · R_i / Σ_j R_j`（按各设备实测平均采样率 R_i 分配 shots）
- 三 QPU 并行效率 **93.60%**（准线性扩展）；双 QPU 组合 96.7–97.7%
- **关键陷阱**：在一台设备上优化好的电路参数**不能**直接迁移到异构多机采样——三 QPU 时单一参数对 (M_i, D_i) 全局套用导致所有 dimer 片段不收敛（误差 >1 a.u.），且该现象在双 QPU 时不出现（异构噪声敏感度随 QPU 数增长）

### 2. 异步 fragment-parallel（任务级并行）
- 各 QPU 独立采样完整片段电路（使用本机优化参数），天然规避跨设备参数迁移问题
- 片段收敛（10⁻⁴ a.u.）即出队，剩余片段异步继续；先 monomer 队列后 dimer 队列
- 原始效率 75.01%（三 QPU）；**扣除不可中断作业的无效等待后 95.17%**——损失来自原型接口缺作业取消功能，非硬件或方法固有缺陷

## 异构噪声下的参数策略（Table II 实测）

| 策略 | 三QPU shot-parallel 结果 |
|------|------|
| 单机参数全局套用 (M_i,D_i) | dimer 全部不收敛，误差最高 >1 a.u. |
| **每机本地参数** (M₁–M₃, D₁–D₃) | 全部片段化学精度内（He₁₄ 误差 0.00126 a.u.）|
| **联合优化** Opt.(M,D)（直接在三QPU采样下优化）| 除 He₁₀ 略超阈值外全部化学精度 |

结论：NISQ 异构设备的电路参数补偿不跨设备迁移；设备专属参数或联合采样下优化可恢复精度。容错时代逻辑电路将消除此异构性问题。

## QWFS 采样方法要点

- 波函数系数 `c_i = s_i·√p_i`：量子电路只采样幅值 p_i（单一参数化电路重复测量），相位 s_i 由经典 NN 节点（tanh 激活，QRBM 式）给出
- 能量 `⟨H⟩ = Σ s_i s_j √(p_i p_j) H_ij / Σ s_i² p_i`，Hamiltonian 矩阵元用 Slater–Condon 规则经典计算
- 对比 VQE：无需多个 Pauli 基旋转电路，shot 需求只由"分辨基态概率"精度决定——对慢/噪声大的原型硬件友好

## 系统工程要点（本文的 systems 视角）

1. **FMO2 分解是 embarrassingly parallel**：`E_FMO2 = Σ_X E_X + Σ_{X>Y} (E_XY − E_X − E_Y)`，monomer/dimer 计算零通信独立执行
2. **效率指标双轨报告**：原始实测 + 理想化修正（区分软件缺陷 vs 硬件/方法极限）
3. **活动图诊断**（Fig.7）：逐处理器逐作业着色（成功/失败/相位完成后无效运行），定位效率损失根因
4. 硬件表征：SPAM 混淆矩阵逐机标定、SMSQ 门保真度 0.95–0.98、ACZ 门 0.79–0.96（Quoll-3 明显更差，解释其低采样率）

## 可复用模式

- **分布式量子采样负载均衡**：按实测设备吞吐率加权分配 shots（式 9），适用于任何 shot 级并行 NISQ 工作流
- **异构 NISQ 集群参数策略决策树**：同电路合并采样 → 需联合优化或设备专属参数；独立任务分配 → 本机参数即可
- **工作流级优势声明**：区分"采样吞吐量/wall-clock 效率提升"与"计算量子优势"——本文只主张前者（诚实边界）
- **双模式并行对照实验设计**：sampling-parallel（强同步约束、高效率上限）vs task-parallel（异步、鲁棒性优先），任何可分片量子工作流都应两者都测

## 局限

- 仅 3 台原型机、He 团簇（弱相互作用体系）、1–2 qubit 电路；缓解策略未验证扩展到更多 QPU
- shot-parallel 的参数策略在 fault-tolerant 逻辑电路下才有"可互换采样器"假设成立
- fragment-parallel 的负载不均衡（Quoll-1+3 组合修正后仍只有 86.22%）

**Activation**: multi-QPU, parallel quantum, FMO, fragment molecular orbital, QWFS, distributed quantum computing, shot parallelism, heterogeneous NISQ, load balancing, quantum chemistry workflow, HPC-QPU integration
