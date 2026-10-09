---
name: ctempo-comb-tensor-network-path-integrals
description: CTEMPO/CCTEMPO numerically exact non-Markovian quantum network simulation via comb tensor networks.
category: ai_collection
trigger: non-Markovian, TEMPO, process tensor, path integral, tensor network, open quantum system, strong system-bath coupling, FMO complex, superradiance
---

# CTEMPO/CCTEMPO: Comb Tensor Network Path Integrals for Non-Markovian Quantum Networks

**Paper**: arXiv:2610.10259 — Quentin W. Richter, Moritz Cygorek (TU Dortmund), 7 Oct 2026
**Task domain**: 量子物理/数值方法 — numerically exact open quantum system simulation

## 核心贡献

提出 CTEMPO（causal TEMPO）与 CCTEMPO（comb-CTEMPO）：在强系统-环境耦合 + 强结构化环境（多峰谱密度）下，将路径积分张量网络的键维数压缩到个位数/低两位数，比 TEMPO 和 PT-MPO 快 1–2 个数量级，首次让非马尔可夫量子网络的数值精确模拟成为"turnkey"方案。

### 方法核心：三种收缩顺序的对比

| 方法 | 收缩顺序 | 键维数 χ | 特点 |
|------|----------|---------|------|
| TEMPO | 逐列（含系统传播子） | 大 | 系统演化历史进 MPO，中间键维数大 |
| PT-MPO | 逐行（仅影响张量，因果序） | 数百–数千 | 可预计算复用，但强耦合下 χ 爆炸 |
| **CTEMPO** | 逐行（因果序）+ **每步立刻收缩第 l 个系统传播子** | **个位数–低两位数** | 缩短 MPO、压缩边缘贴近短时记忆节点 |

**关键洞察**：短时记忆节点对大键维数贡献最大。CTEMPO 每步消掉一腿（系统传播子），把 SVD 压缩最有效的位置移到最难压缩的短时记忆节点附近。

### 算法要点

1. **路径积分表示**：ρ̄_αn = Σ M_αl,αl−1 × Π b^(i−j)（Feynman-Vernon 影响泛函的 Gaussian 性）
2. **Zip-up 收缩**：每次 MPO-张量收缩后 SVD 压缩，截断 σ_i < ε·σ_0
3. **Comb 拓扑（CCTEMPO）**：多体密度矩阵的 MPO 作为骨干（backbone），每个 site 的 CTEMPO MPO 作为梳齿（teeth）
4. **交替传播**：骨干半步 MPO-MPO 乘法 → 各梳齿 CTEMPO 更新 → 骨干再半步。瓶颈是骨干更新，梳齿腿使 MPO-MPO 时间线性增长 χ（χ 小 → 可行）

### 基准结果

- **Spin-boson 模型**（Ohmic, T=0K）：α=0.1/1.0 下 CTEMPO 比 TEMPO/PT-MPO 快 10–100×；χ 在定位相变（α∼1）处出现峰值 → 时间关联在相变附近增长（类比空间关联）
- **FMO 复合物**（7-site, 62-峰谱密度, T=77K）：此前 PT-MPO 不可行的问题，CCTEMPO 3–17 小时收敛至 DAMPF 参考解 1% 内。关键：模拟完整两能级 site 网络（非单激发流形多能级系统）
- **量子点超辐射**（N=20, super-Ohmic 声子浴, 全连接坍缩算符 L=Σσ−）：发现**新中间标度区** — 局域 super-Ohmic 声子使峰值强度比 I*₄K/I* 对大 N 趋于常数（vs 局域 Lindblad 去相的 →1 预测）；τ_d ∼ ln N/(Nγ) 在 γ⁻¹=5ps 时小于声子记忆时间 3ps → 发射快于去相

### 可复用模式

1. **"收缩顺序决定可压缩性"**：同样的张量网络，改变收缩顺序（列→行→行+传播子）可将 χ 从千级降到个位数 — 适用于任何路径积分/影响泛函计算
2. **"把系统传播子尽早收缩进网络"**：消除已知腿 → MPO 更短 → 压缩更有效。通用张量网络技巧
3. **Comb 骨架+梳齿拓扑**：将单点非马尔可夫解法（齿）挂到多体 MPO（骨干）上，代价线性于 χ — 任何"局部环境+全局演化"问题的模板
4. **SVD 截断阈值 ε 作为精度-成本旋钮**：σ_i < ε·σ_0；压缩误差图（ε vs runtime/χ）是标准收敛性证据
5. **相变附近的键维数峰值**作为关联长度增长指标 — 可反过来用作相变探测器
6. **内存截断**（memory truncation）实现传播时间线性标度 — 长时间模拟必备

### 局限

- 环境必须是 spin-boson 型（Gaussian 环境）；非高斯环境需扩展
- Comb 拓扑最适合准一维系统；高维需 belief propagation（不引入环、代价线性于 χ）
- 无需微调，但需选 ∆t 和 ε 两个收敛参数

## 相关工作

- TEMPO (Strathearn et al.) — 逐列收缩原始方法
- PT-MPO / process tensor (Jørgensen & Pollock) — 因果序收缩 + 可复用
- DAMPF — 阻尼谐振子拟合浴关联函数（FMO 参考方法）
- 本 skill 与 [[parallel-scan-neural-quantum-states]] 互补：后者是 NQS 压缩，本 skill 是路径积分张量网络压缩；均以 χ（键维数）为核心资源度量

**Activation**: non-Markovian simulation, TEMPO, process tensor, path integral tensor network, open quantum system, strong coupling, FMO complex, superradiance scaling, bond dimension compression
