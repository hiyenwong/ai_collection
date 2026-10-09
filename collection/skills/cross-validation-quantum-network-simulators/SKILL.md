---
name: cross-validation-quantum-network-simulators
description: Cross-validation methodology for open-source quantum network simulators (QuISP vs SeQUeNCe).
category: ai_collection
trigger: quantum network simulator, QuISP, SeQUeNCe, cross-validation, discrete event simulation, entanglement distribution benchmark
---

# Cross-Validation of Open-Source Quantum Network Simulators

**Paper**: arXiv:2610.09322 — Chung, Hajdušek et al. (Argonne + Keio, Q-NEXT / JST Moonshot), 7 Oct 2026
**Task domain**: 量子网络系统工程 — simulator reliability, reproducibility, benchmark methodology

## 核心贡献

两个主流开源量子网络模拟器（QuISP 与 SeQUeNCe）的首次系统交叉验证。通过 4 个解析可解的基准任务，定位了两者在网络时序与保真度上的定量/定性差异根源，并给出了可复用的交叉验证方法论。

### 差异根源三分类（诊断框架）

两个模拟器结果不一致时的三种解释（任何 simulator 对比研究的诊断起点）：
1. **(a) 真实设计差异** — 值得研究的对象（这是设计决策本身）
2. **(b) 有效的不同简化** — 物理或协议层级的合法建模选择（如握手次数、节点内部处理时间模型）→ 需要量化其影响
3. **(c) bug** — 直接修复（本研究实际导致两个模拟器的大量修复）

### 关键实证发现

| 维度 | 发现 |
|------|------|
| 时序 | SeQUeNCe 慢于 QuISP，比值恒定 ≈ **4.16–4.33**（随 memory 数仅微变） |
| 根源 | SeQUeNCe 每 Bell pair 做三次握手（three-way handshake）vs QuISP 只做一次两次握手（two-way handshake once） |
| 非对称链路 | **定性分歧**：SeQUeNCe 连接建立时间与 BSA 位置无关；QuISP 在 BSA 居中最优，BSA 偏移时恶化 → 首代量子网络部署规划中 BSA 位置的选型判据 |
| 保真度 | 相同误差参数下两模拟器**一致**（错误模型实现均正确） |
| 时间相关误差 | 均匀离散化：SeQUeNCe 用连续时间 Pauli 信道解析模型 p=exp(−t/τ)；QuISP 用时间不变态转移矩阵离散指数化 |
| 净化实验 | ΔF_pur 与初始保真度无关（等待时间分布独立于初始保真度）；有限 τ 下 QuISP 保真度更高（链路生成快 → 空闲时间短） |
| 吞吐量 | 完美记忆下吞吐差恒定；有限 τ 下 SeQUeNCe 慢通信模型双重叠加（生成慢 + 空闲久 → 成功概率降）→ 线性依赖初始保真度 |

### 可复用的交叉验证协议

1. **选解析可解任务**：link-level 纠缠生成（MIM 架构）、非对称 MIM、两链路 swapping、BBPSSW 净化 — 每个都有闭式方程（论文给出 Eq. 5, 11, 17, 19）
2. **先推导理论模型再跑模拟**：闭式预测线叠在仿真散点上（论文 Fig. 7-9 模式）
3. **归一化相对差指标**：ΔF_swap = (F^Q − F^S)/F^S，消除绝对量级，聚焦相对分歧
4. **扫描参数网格**：gate error p_g × measurement error p_m × coherence time τ（18ms / 55ms / ∞）三维扫描定位分歧区间
5. **差异溯源到机制**：每个定量分歧必须归因到具体协议/建模差异（如握手次数），不能停留在"结果不同"

## 可复用模式（skill 提取物）

- **Simulator 三分类诊断**（真实差异 / 合法简化 / bug）适用于任何模拟器对比（经典网络、ML 系统、数字孪生）
- **"恒定比值 → 机制差异"启发式**：两个模拟器性能比恒定（4.16–4.33 不随参数变）→ 差异来自协议级常数因子而非物理模型错误
- **保真度一致 + 时序不一致** 的组合意味着错误模型正确但通信模型不同 — 分别验证误差模型与协议时序是正交的
- **解析可解任务集**是 simulator cross-validation 的锚点：先把闭式解写成代码，再对比模拟输出

## 工程要点

- QuISP：面向大规模网络/网际网（100 networks × 100 nodes 最小资源），RuleSet 驱动（Condition/Action clauses），QRSA 路由软件架构
- SeQUeNCe：面向高定制量子光子网络精度模拟
- 两者均聚焦第一代（1G）量子中继网络（纠缠分发 + swapping，无 QEC）
- 光子 BSM 成功概率上限 1/2（线性光学）→ 链路级纠缠生成本质概率性
- 记忆量子比特上的 BSM 无此上限 → 可确定性

## 相关工作

- NetSquid, QuantumSavory, QuNetSim, QuNet, ReQuSim, Q2NS — 其他量子网络模拟器（同类验证目标）
- 本 skill 与 [[repeater-swapping-scheduling-decoherence]]（2610.07991）互补：后者是中继调度设计，本 skill 是模拟器层验证基础设施

**Activation**: quantum network simulator, QuISP, SeQUeNCe, cross-validation, entanglement distribution benchmark, simulator reliability, discrete event simulation
