---
name: quantum-finance-portfolio
description: "量子计算在金融组合优化中的应用。涵盖 QUBO建模、量子退火、QRNG增强Monte Carlo、VaR/CVaR风险估计、QAOA Mixer选择、两步QAOA优化、混合量子优势审计、QRL动态组合优化、QAOA+ZNE误差缓解、qReduMIS递归量子-经典组合优化。触发词：量子金融、quantum portfolio、量子组合优化、quantum annealing finance、QRNG VaR、QAOA mixer、hybrid quantum audit、D-Wave hybrid、量子优势审计、quantum contribution measurement、QRL、QDDPG、QDQN、ZNE、zero noise extrapolation、carbon credit portfolio、qReduMIS、frozen nodes、Quantinuum"
---

# Quantum Finance Portfolio

量子计算在金融组合优化和风险管理中的应用技能。

## Activation Keywords
- 量子金融
- quantum finance
- quantum portfolio optimization
- 量子组合优化
- quantum annealing finance
- QUBO portfolio
- QRNG Monte Carlo
- 量子风险估计
- quantum VaR CVaR
- QAOA mixer selection
- 两步QAOA
- hybrid quantum audit
- D-Wave hybrid
- quantum advantage audit
- quantum contribution measurement
- 混合量子审计
- 量子优势审计
- `exec`: Run Python quantum computing scripts
- `web_search`: Search arxiv for latest quantum finance papers
- `web_fetch`: Fetch paper details from arxiv/Springer
- `sqlite3`: Query kg.db for related research

## Core Patterns (from 2025-2026 research)

### Pattern 0: 无惩罚QUBO管线 (Penalty-Free QUBO)
**Source**: arXiv:2605.17628 (Lozano)

**核心发现**：标准QUBO组合优化中的基数惩罚项产生密集全1矩阵（rank-one term proportional to all-ones matrix），使逻辑交互图完全连通，导致D-Wave Pegasus/Zephyr上链断裂率达83-92%。

**解决方案**：
1. 完全丢弃惩罚项：仅从期望收益和风险缩放协方差构建QUBO目标
2. 在硬件上采样
3. 将基数约束作为经典后处理步骤强制执行

**效果**：链断裂率从71-92%降至≤0.04%。在N=49股票和N=48投注组合上验证，QPU返回的可行组合能量低于贪婪启发式。

### Pattern 0b: 热启动量子组合优化 (Hot-Start QPO)
**Source**: arXiv:2510.11153 (Schlütter et al.)

当目标函数光滑凸时（如均值方差组合优化）：
1. 先用经典凸优化求解连续松弛解 x*
2. 在 x* 的 ε-邻域内构造紧凑希尔伯特空间
3. 在缩减空间上运行 QAOA 或量子退火
4. 量子比特数从 log2(N^k) 降至 log2(|S_ε|)

优势：在 D-Wave Advantage 上超越现有量子方法
适用：整数约束组合优化、NISQ 设备

### Pattern 0c: qReduMIS — Quantum-Informed Portfolio Selection (2026-07-01, arXiv:2607.01037)

**核心发现**: 不用量子直接求解全问题，而是将QAOA作为"Oracle"识别frozen nodes（在>90%高质量解中出现的变量），再用经典归约递归缩小问题规模。

**工作流程**:
1. 将资产相关性矩阵构建为图（高相关资产间有边 = 分散化约束）
2. 在图上运行QAOA (p=2)，测量节点包含概率
3. 识别frozen nodes: p_in > 0.9 → frozen IN; p_in < 0.1 → frozen OUT
4. 经典归约：移除frozen nodes及其邻居，应用支配/团归约
5. 递归直到经典求解

**硬件验证结果** (Quantinuum Helios 98-qubit trapped-ion):
| 指数 | 资产数 | QAOA成功率 | qReduMIS成功率 | 近似比 |
|------|--------|-----------|---------------|-------|
| DJIA | 30 | ~0.80 | ~0.95 | ≥0.96 |
| S&P 100 | 100 | ~0.15 | ~0.40 | ≥0.96 |
| Nikkei 225 | 225 | ~0.05 | ~0.95 | ≥0.96 |

**关键结果**: 时间-解决方案缩放指数比独立QAOA小3.2倍。

**设计原则**: QAOA as Oracle, Not Solver — 用量子采样识别结构上"容易"的变量，经典方法处理剩余"困难"部分。这是当前NISQ时代组合优化的务实路径。

See `references/qredumis-quantum-portfolio.md` for full pipeline code and QUBO formulation.

### Pattern 1: 量子金融五层计算栈 (Finance Stack Analysis)
**Source**: arXiv:2604.08180 (Gong et al., 134页综述)

评估量子金融应用必须覆盖五个层次：
| 层次 | 量子原语 | 优势条件 |
|------|----------|---------|
| 组合优化 | QAOA, 量子退火 | 约束搜索主导时 |
| 衍生品定价 | 振幅估计 | 重复期望计算是瓶颈 |
| 尾部风险 | 量子Monte Carlo | 罕见事件需要大量采样 |
| 量子ML | 变分量子电路 | 任务依赖，无通用优势 |
| 后量子安全 | N/A（防御领域） | **立即行动** — 必须在FTQC攻击前迁移 |

核心结论：最强近期优势在混合工作流而非纯量子方案

### Pattern 2: 专家分析评估框架 (Expert Evaluation)
**Source**: arXiv:2507.20532 (Innan et al., QCE 2025)

VQE/QAOA优化的组合常违反金融标准（充分分散、合理风险暴露）。
必须引入金融专业人士评估经济合理性和市场可行性。
**关键发现**：算法性能与金融适用性之间存在显著差距。

### Pattern 3: QUBO建模 (Graph-based Coalition - GCS-Q)

将组合优化问题转化为 QUBO (Quadratic Unconstrained Binary Optimization):

```
问题: 资产聚类 (signed correlation graphs)
转换: min/max ΣᵢΣⱼ Qᵢⱼ xᵢxⱼ  where x ∈ {0,1}ⁿ

关键步骤:
1. 构建关联矩阵 W (signed, weighted)
2. 映射到 QUBO 矩阵 Q
3. 量子退火求解
4. 解码聚类结果
```

优势: 无需预设聚类数，直接处理 signed correlations

### Pattern 2: QRNG增强Monte Carlo

量子随机数生成器提升 Monte Carlo 精度:

```
应用: VaR/CVaR 估计
方法: QRNG → 路径采样 → 风险指标

步骤:
1. 使用光子/QPU生成真随机数
2. 生成更多独立路径样本
3. 计算 VaR (Value at Risk) 和 CVaR
4. 对比经典 RNG 结果
```

优势: 更低估计偏差，更好的精度

### Pattern 3: 混合量子-经典框架
结合经典预筛选和量子优化的混合方法，降低量子电路深度需求。

### Pattern 4: QAOA Mixer选择（2026-05-16新增）
**核心发现**：XY混合器在传统X混合器之上，对约束型投资组合优化问题有15%更好的近似比。
- XY Mixer适用于多约束（long/short/neutral）组合优化
- X Mixer适用于简单权重分配问题
- Mixer选择应基于问题约束类型：有约束→XY，无约束→X
### Pattern 5: 两步QAOA优化（2026-05-16新增）

**核心思想**：先经典筛选 promising 资产子集，再量子优化权重分配。

- **Step 1 - 经典预筛选**：使用传统方法（如均值-方差、风险平价）缩小资产范围
- **Step 2 - 量子优化**：对候选子集应用QAOA进行权重分配
- **优势**：降低电路深度、减少qubit需求、更适合NISQ设备
- **适用场景**：大规模投资组合（>50资产）、qubit有限的量子硬件

### Pattern 6: 囚禁离子硬件感知分解（2026-05-16新增，arXiv: 2602.23976）

**核心思想**：将大规模组合优化问题分解以适配囚禁离子量子处理器的硬件限制。

- **分解管道**：经典预筛选（按夏普比率/流动性过滤）→ 子问题分区（匹配qubit数量）→ 量子优化（每个子问题在离子阱QPU上求解）→ 经典聚合（全局约束执行）
- **囚禁离子优势**：全对全连接（无需SWAP开销）、高保真门（>99.9%单比特/>99%双比特）、原生Mølmer-Sørensen门（高效处理组合QUBO项）
- **基数约束处理**：两种方法——(1) 惩罚方法 ρ(Σz_i - k)² (2) 约束保持XY混合器
- **适用场景**：100+资产的大规模组合优化、带基数约束的现实投资组合

**⚠️ 关键发现 (2026-05)**: 当前 D-Wave 混合方案中经典后处理占主导，QPU 贡献主要在解空间探索（帮助跳出局部最优）。混合系统的"量子优势"常被高估——必须通过审计量化真实量子贡献。

### Pattern 6: 混合量子优势审计 (Hybrid Quantum Audit)

审计混合量子-经典优化系统中量子 vs 经典的贡献分配。基于 Lozano et al. 2026 对 D-Wave 混合组合优化的审计研究。

**核心方法论**:
1. **分解混合管道**: 隔离 QPU 采样 vs 经典后处理组件
2. **运行对照实验**: 完整混合求解器 vs 禁用 QPU 的经典变体 (相同预/后处理)
3. **定义量化指标**:
   - **量子改进率**: QPU 改善经典结果的实例百分比
   - **解空间探索指数**: QPU 引入的解多样性度量
   - **经典后处理放大系数**: 经典优化对 QPU 原始解的改进程度
   - **混合协同分数**: 量子+经典 > 量子 alone + 经典 alone?
4. **统计协议**: ≥30 次迭代、bootstrap 置信区间、Cohen's d 效应量
5. **报告生成**: 量子优势热力图、贡献分解 (量子%/经典%/协同%)

**关键发现**: 当前混合系统中量子贡献主要在帮助逃逸局部最优，经典组件处理大部分解精细化工作。审计前不要假设混合系统一定有量子优势。

### Pattern 7: QNN期权定价 (QNN Option Pricing on NISQ, 2026-05-23新增)
**Source**: arXiv:2604.19832 (Zając & Pracht)

**核心发现**：首个在真实NISQ硬件上实现量子神经网络(QNN)期权定价的跨平台研究，使用2-qubit QNN架构近似Black-Scholes-Merton定价函数。

**硬件评估**：四大量子处理器对比
- IBM Fez (超导)
- IQM Garnet (超导)
- IonQ Forte (离子阱)
- Rigetti Ankaa-3 (超导)

**关键结论**：
- 不同硬件平台表现出显著的性能差异
- 尽管NISQ限制，各平台均能实现一致的定价近似
- 证明QNN方法用于衍生品定价的可行性
- 可扩展到更复杂模型：局部波动率、随机波动率(Heston)、利率框架

**工作流**：
1. BSM参数编码 → 量子态制备 (资产价格、行权价、到期时间映射到量子比特旋转)
2. 参数化量子电路作为QNN
3. 经典-量子混合训练循环 (经典优化器更新电路参数，量子硬件评估期望值)
4. 损失函数：QNN输出与真实BSM价格的MSE
5. 跨平台基准测试对比定价精度、电路保真度、噪声鲁棒性

**陷阱**：
- **相干时间**：限制电路深度
- **门误差**：深层电路噪声累积
- **编码挑战**：金融参数跨度大，量子态需归一化输入
- **测量精度**：有限shots影响定价精度
- **校准漂移**：硬件性能日复一日变化

See `references/qnn-option-pricing.md` for detailed cross-platform benchmark results.

### Pattern 8: QRL for Dynamic Portfolio Optimization (arXiv:2601.18811)

Quantum Reinforcement Learning using VQC as function approximators for sequential portfolio allocation.

```
核心架构: VQC替代经典神经网络作为策略/价值函数近似器
- QDDPG: 连续动作空间 (portfolio weights), actor-critic架构
- QDQN: 离散动作空间, VQC作为Q函数近似器
- 优势: 比经典深度RL使用更少参数但性能相当
- NISQ约束: 电路深度受限, 测量shot噪声, barren plateau风险
```

### Pattern 9: QAOA+ZNE on Real Hardware (arXiv:2602.09047)

QAOA combined with Zero Noise Extrapolation for multi-objective portfolio optimization on IBM Quantum hardware.

```
工作流程:
1. 多目标QUBO编码 (碳封存+生物多样性+社会影响, 88变量)
2. QAOA电路: [U_C(γ)·U_M(β)]^p
3. ZNE: 门折叠放大噪声 → 多噪声水平 → Richardson外推至λ=0
4. 经典优化循环更新QAOA参数

关键发现: ZNE对NISQ硬件至关重要，QAOA+ZNE超越经典贪心基线
```

## 2026年QAOA最新进展
| 方法 | 优势 | 适用场景 |
|------|------|----------|
| XY Mixer | 15%更好近似比 | 约束型组合优化 |
| 两步QAOA | 降低电路深度 | NISQ设备 |
| 经典预筛选 | 减少qubit需求 | 大规模组合 |
| 离子阱分解 | 全连接无SWAP | 100+资产带基数约束 |
| **NISQ表达力-相干性权衡** | 硬件基准评估 | 所有量子金融部署决策 |

## ⚠️ 2026-06-27 新增关键约束：NISQ 表达力-相干性权衡

部署密集金融优化问题时，存在根本性权衡——WS-QAOA 数学表达力强但遭遇灾难性退相干（dense CVaR 问题在 heavy hex 拓扑上导致指数级 SWAP 门开销），HE-VQNN 硬件相干性好但无法捕获密集尾部风险关联。

```
决策树:
  IF 问题关联密度 > 硬件连接密度:
    → 选择 HE-VQNN (牺牲表达力保相干性)
  IF 问题关联密度 ≤ 硬件连接密度:
    → 选择 WS-QAOA (保留表达力)
  IF 资产规模 > 可用量子比特:
    → 经典预筛选 + 量子优化 (两步法)

混合代理矩阵方法:
  经典预计算 CVaR 代理矩阵 → 仅量子优化离散决策 x ∈ {0,1}^n
  绕过辅助量子比特瓶颈 (无需 ζ + S×K 辅助寄存器)
```

**经典优化器选择**: NISQ 硬件上用 SPSA（每步仅 2 次电路评估，噪声鲁棒），模拟环境用 Nelder-Mead（快速精确但对 shot noise 敏感）。

**⚠️ 关键结论**: 当前 NISQ 硬件在 all-to-all 连接性缺失的情况下，迫使量子金融优化在"算法不可表达性"和"硬件退相干"之间做不可行选择。这不是算法改进能解决的——需要硬件拓扑升级。

See `references/quantum-nisq-resilience-benchmark.md` for detailed transpilation metrics, SWAP tax analysis, and the full decision framework.
实际应用中的混合架构:

```
架构:
  量子预处理 (QPU) → 中间结果 → 经典后处理 (CPU)

应用:
- 量子: 问题编码、采样、优化
- 经典: 数据预处理、结果解析、验证

适用场景:
- NISQ时代硬件限制
- 渐进式量子优势验证
```

### Pattern 4: CCD-QAOA for Constrained Portfolio Optimization (arXiv:2605.06858)

Standard QAOA with transverse-field mixers fail to enforce hard constraints (budget, cardinality) requiring soft penalties that distort the energy landscape. **CCD-QAOA** (Constrained Counterdiabatic QAOA) solves this:

```
核心创新:
- XY mixer: H_XY = ½∑_{i<j}(X_i X_j + Y_i Y_j) 保持汉明权重
  → 天然执行预算约束 (∑x_i = K)，无需惩罚项
- Counterdiabatic driving: 从嵌套对易子生成近似绝热规范势
  A_μ ≈ ∑ c_k [H_prob, [H_prob, ... [H_prob, H_XY]...]]
  → 加速收敛，添加通向绝热的捷径

CCD-QAOA拟设:
  |ψ(θ)⟩ = ∏_{l=1}^p e^{-iβ_l H_CD} e^{-iγ_l H_prob} e^{-iα_l H_XY} |ψ₀⟩

基准测试:
  在固定深度p下，CCD-QAOA一致优于:
  - 标准 XY-mixer QAOA
  - Grover-mixer QAOA
  - 惩罚型 QAOA
```

适用场景: 带预算/基数/行业约束的组合优化；直接指数化(ESG约束)；任何需要硬约束保持的量子组合优化问题。

### Pattern 5: Quantum Reservoir Computing for Financial Time Series (arXiv:2505.13933)

QRC uses quantum dynamics as a rich feature extractor for temporal prediction tasks:

```
核心架构:
- 储层: 全连通横向场 Ising 哈密顿量
  H = -∑ J_{ij} σ_i^z σ_j^z - ∑ h_i σ_i^x
- 输入量子比特: 接收时间序列数据
- 记忆量子比特: 保持时间上下文
- 读出层: 经典线性回归 (仅训练读出层)

工作流程:
  1. 时间序列预处理 (归一化、滑窗)
  2. Wrapper前向选择特征 → 减少所需量子比特
  3. 编码到量子储层 (输入比特)
  4. 量子动力学演化 (记忆比特保留时序信息)
  5. 测量量子态
  6. 训练经典读出层
  7. 多误差指标 + MCS程序验证

可解释性:
  - Shapley值量化特征重要性
  - 前向选择识别最优量子比特子集

结果: 在已实现波动率预测上持续超越 ARIMA、GARCH、经典ML
发表: Physical Review Research 8, 023028 (2026)
```

适用场景: 波动率预测、股票价格预测、金融时间序列分析、任何时序预测任务。NISQ硬件可行（特征选择减少量子比特需求）。

### Pattern 10: FPQC-SAC — Quantum Representation Filtering for Financial RL (2026-06-13, arXiv:2606.10448)

**问题**：金融市场是典型的低信噪比(SNR)环境，不稳定 off-policy 最大熵方法(如SAC)。噪声状态表示产生不可靠的Q值估计，bootstrapping放大误差，形成"金融熵陷阱"(Financial Entropy Trap)。

**FPQC-SAC 解决方案**：在 actor 和 critic 网络**之前**放置紧凑有界 Parameterized Quantum Circuit (PQC)，在**表示层**约束特征传播，而非过滤原始输入或正则化 bootstrapping 后的Q值。

```
核心架构:
  原始状态 s → PQC(θ) → 过滤表示 φ(s) → Actor/Critic网络 → Q值/策略

关键机制:
- PQC 作为有界特征变换器：限制极端市场波动对 Bellman 目标估计的影响
- 可训练量子纠缠：保持灵活的跨资产交互
- 表示级过滤：比输入过滤或Q值正则化更有效

实证结果 (真实投资组合管理任务):
- 66.89% 相对收益提升 (vs 标准 SAC)
- 27% 超越最佳连续控制 DRL 基线
- 显著提升样本外稳定性
- 代码开源: https://github.com/ZeyuLIU-UST/FPQC-SAC-main

与 Pattern 8 (QRL) 的区别:
- QRL (Pattern 8): VQC 替代经典神经网络作为策略/价值函数近似器
- FPQC-SAC (Pattern 10): PQC 放在网络**之前**作为表示层过滤器，经典网络仍作为函数近似器
- FPQC-SAC 更轻量、更容易集成到现有 RL 管线
```

适用场景: 低SNR金融环境下的RL（投资组合管理、算法交易）；需要稳定 off-policy 最大熵方法的场景；现有 RL 方法在极端市场波动下失效的情况。

### Pattern 11: Quantum Rare Event Discovery (2026-06-13, arXiv:2606.06316)

**问题**：金融崩盘、级联失败等罕见事件（极低概率）触发巨大损失。经典和量子方法都需要巨大的采样开销来收集足够的稀有事件样本，且稀有事件事先未知，无法用标准技术标记放大。

**量子稀有事件发现算法**:
```
核心创新:
- 无需事先学习哪些事件是稀有的
- 实现与稀有性阈值的最优量子缩放
- 对重尾系统（尾部有非零总质量）实现二次加速
- 对平稳随机过程实现稳健多项式加速（指数由熵率结构决定）

数学框架:
- 量子缩放: O(1/√ε) vs 经典 O(1/ε) (ε = 稀有性阈值)
- 重尾系统: 二次加速 ∝ 1/√P(event < threshold)
- 平稳过程: 多项式加速 ∝ exp(-h·T) (h = 熵率)

应用领域:
- 金融崩盘预测和尾部风险估计
- 基础设施级联失败分析
- AI系统关键错误检测
```

适用场景: 金融尾部风险估计、极端事件建模、压力测试、任何需要发现/采样未知稀有事件的场景。是对 Pattern 1 尾部风险层的具体算法实现。

### Pattern 10: FPQC-SAC — Quantum Representation Filtering for Financial RL (2026-06-13, arXiv:2606.10448)

**问题**：金融市场是典型的低信噪比(SNR)环境，使 off-policy 最大熵方法(如SAC)不稳定。噪声状态表示产生不可靠的Q值估计，bootstrapping放大这些误差，形成"金融熵陷阱"(Financial Entropy Trap)。

**FPQC-SAC 解决方案**：在 actor 和 critic 网络之前放置紧凑有界的 Parameterized Quantum Circuit (PQC)，在**表示层**约束特征传播，而非过滤原始输入或正则化 bootstrapping 后的Q值。

```
核心架构:
  原始状态 s → PQC(θ) → 过滤表示 φ(s) → Actor/Critic网络 → Q值/策略

关键机制:
- PQC作为有界特征变换器：限制极端市场波动对Bellman目标估计的影响
- 可训练量子纠缠：保持灵活的跨资产交互
- 表示层过滤：比输入过滤或Q值正则化更有效

实证结果 (真实投资组合管理任务):
- 66.89%相对收益提升 (vs 标准SAC)
- 27%超越最佳连续控制DRL基线
- 显著提升样本外稳定性
- 代码开源: https://github.com/ZeyuLIU-UST/FPQC-SAC-main

与 Pattern 8 (QRL) 的区别:
- QRL (Pattern 8): VQC替代经典神经网络作为策略/价值函数近似器
- FPQC-SAC (Pattern 10): PQC放在网络**之前**作为表示层过滤器，经典网络仍作为函数近似器
- FPQC-SAC更轻量、更容易集成到现有RL管线
```

**适用场景**: 低SNR金融环境下的RL（投资组合管理、算法交易）；需要稳定 off-policy 最大熵方法的场景；现有 RL 方法在极端市场波动下失效的情况。

### Pattern 11: Quantum Rare Event Discovery (2026-06-13, arXiv:2606.06316)

**问题**：金融崩盘、基础设施级联失败、AI系统关键错误等由极小概率事件触发的事件。现有经典和量子方法需要大量采样开销收集足够数据样本，且稀有事件事先未知，无法用标准技术标记放大。

**量子算法**：无需事先学习哪些事件是稀有的，直接实现最优量子缩放。

```
核心创新:
- 无需预先识别稀有事件
- 实现与稀有性阈值的最优量子缩放
- 重尾系统(尾部有非零总质量)中实现二次加速
- 平稳随机过程中实现稳健多项式加速(指数由熵率结构决定)

应用场景:
- 金融崩盘预测和尾部风险估计
- 基础设施级联故障分析
- AI系统关键错误检测
```

**与 Pattern 1 的关系**：这是 Pattern 1 (五层栈)中"尾部风险"层的具体算法实现。Pattern 1 说"量子Monte Carlo在罕见事件需要大量采样时有优势"，Pattern 11 给出了具体的算法框架和复杂度分析。

## Instructions for Agents

### Step 1: 问题分析
当用户请求量子金融任务时:
1. 确定问题类型 (聚类/优化/风险估计/RL/稀有事件)
2. 评估量子适用性
3. 选择合适模式 (QUBO/QRNG/混合/FPQC-SAC/稀有事件发现)

### Step 2: QUBO建模 (如适用)
1. 定义优化目标函数
2. 构建二次项矩阵 Q
3. 添加约束 (转换为惩罚项)
4. 评估问题规模 (qubit需求)

### Step 3: 算法选择
- **小规模 (n<100)**: 量子退火器 (D-Wave) 或 QAOA
- **中等规模**: 混合 VQE + 经典优化
- **大规模**: QRNG增强 Monte Carlo

### Step 4: 结果验证
1. 与经典算法对比
2. 检查量子优势 (精度/速度)
3. 评估实用性

## Error Handling

### 问题规模超出量子硬件能力
```
If N > available qubits:
  1. 使用混合方法
  2. 问题分解为子问题
  3. 递归量子求解
```

### 量子结果不稳定
```
If quantum results vary significantly:
  1. 增加采样次数
  2. 使用错误缓解技术
  3. 多次运行取平均
```

See `references/quantum-nisq-resilience-benchmark.md` for the expressibility-coherence trade-off analysis (arXiv:2606.07727).

### Pattern 11: NISQ Expressibility-Coherence Trade-off (2026-06-27, arXiv:2606.07727)

**核心发现**: 在 NISQ 设备上部署密集金融优化问题时，存在根本性权衡——WS-QAOA 数学表达力强但遭遇灾难性退相干（dense CVaR 问题在 heavy hex 拓扑上导致指数级 SWAP 门开销），HE-VQNN 硬件相干性好但无法捕获密集尾部风险关联。

```
决策树:
  IF 问题关联密度 > 硬件连接密度:
    → 选择 HE-VQNN (牺牲表达力保相干性)
  IF 问题关联密度 ≤ 硬件连接密度:
    → 选择 WS-QAOA (保留表达力)
  IF 资产规模 > 可用量子比特:
    → 经典预筛选 + 量子优化 (两步法)

混合代理矩阵方法:
  经典预计算 CVaR 代理矩阵 → 仅量子优化离散决策 x ∈ {0,1}^n
  绕过辅助量子比特瓶颈 (无需 ζ + S×K 辅助寄存器)
```

**经典优化器选择**: NISQ 硬件上用 SPSA（每步仅 2 次电路评估，噪声鲁棒），模拟环境用 Nelder-Mead（快速精确但对 shot noise 敏感）。

**⚠️ 关键结论**: 当前 NISQ 硬件在 all-to-all 连接性缺失的情况下，迫使量子金融优化在"算法不可表达性"和"硬件退相干"之间做不可行选择。这不是算法改进能解决的——需要硬件拓扑升级。

See `references/quantum-nisq-resilience-benchmark.md` for detailed transpilation metrics and SWAP tax analysis.

## References

最新研究论文存储在 kg.db:

```bash
sqlite3 kg.db "SELECT name, properties FROM kg_entities WHERE entity_type='paper' AND category='quantum-finance'"
```

关键论文:
- arXiv:2602.09047 — Optimizing Carbon Credit Portfolios with QAOA+ZNE on IBM Quantum Hardware (ZNE误差缓解, 88变量多目标优化)
- arXiv:2601.18811 — Quantum Reinforcement Learning for Dynamic Portfolio Optimization (QDDPG/QDQN, VQC替代经典神经网络)
- arXiv:2605.17628 — Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization (无惩罚QUBO，链断裂率71-92%→0.04%)
- arXiv:2604.08180 — Quantum Computing for Financial Transformation (134页综述，五层计算栈)
- arXiv:2510.11153 — Hot-Starting Quantum Portfolio Optimization (紧凑希尔伯特空间)
- arXiv:2509.17876 — Quantum Portfolio Optimization: An Extensive Benchmark (250实例基准)
- arXiv:2509.02647 — ℏ_E: an action constant for quantum economics (经济作用常数)
- arXiv:2508.21031 — Quantum Economic Advantage Online Calculator (MIT)
- arXiv:2507.20532 — Quantum Portfolio Optimization with Expert Analysis Evaluation (QCE 2025)
- arXiv:2505.08917 — When Recall Fails, Discord Remembers (量子博弈论, Kuhn定理)
- arXiv:2502.02125 — QRNG VaR/CVaR
- arXiv:2507.03963 — Quantum Stochastic Walks for Portfolio Optimization (QSW稳态分布优化器, Sharpe+15%, turnover-90%)

## Quantum Stochastic Walk (QSW) Optimization Pattern

A **third paradigm** beyond QAOA circuits and VQE eigenvalue approaches. QSW doesn't use variational circuits at all — instead it embeds assets in a weighted covariance graph and derives portfolio weights from the stationary distribution of a Lindblad-driven quantum-classical walk.

**Key parameters**: α (return sensitivity), λ (risk aversion), ω (quantum-classical balance, empirically sweet spot ∈ [0.2, 0.4])

**Results on S&P 500 top-100** (2016-2024): 15% Sharpe improvement, 90% turnover reduction vs classical mean-variance. Naturally respects UCITS 5/10/40 rules.

**Implementation**: Solve Liouvillian superoperator for null space → extract diagonal of stationary density matrix as weights.

See `quantum-stochastic-walk-portfolio` skill for full methodology.

## Related Skills
- `quantum-finance-computation-stack` — Unified five-layer finance stack framework synthesizing portfolio optimization, derivative pricing, tail-risk, QML, and PQC (arXiv:2604.08180, 2510.11153, 2507.20532, 2505.08917)
- `quantum-stochastic-walk-portfolio` — QSW portfolio optimization methodology
- arXiv:2604.25644 — Efficient Complex-Valued State Preparation on Bucket Brigade QRAM (BBQRAM + segment tree, O(log²(MN)) amplitude encoding)
- arXiv:2602.23976 — Large-scale portfolio optimization on trapped-ion quantum computer (硬件感知分解)

## Example Usage

### Example 1: 资产聚类
```
User: "用量子方法聚类这50支股票的相关性矩阵"

Agent:
1. 分析相关性矩阵 (signed correlations)
2. 构建 QUBO 问题
3. 推荐量子退火求解
4. 对比 SPONGE/k-Medoids 结果
```

### Example 2: VaR估计
使用QRNG增强Monte Carlo进行风险价值估计。

### Example 3: QAOA Mixer选择
```python
# 根据问题约束选择Mixer
if has_constraints(portfolio_constraints):
    mixer = "XY"  # 约束型问题用XY混合器
else:
    mixer = "X"   # 简单问题用X混合器
    
# 验证：在同一实例上对比不同Mixer
for mixer_type in ["X", "XY"]:
    result = run_qaoa(problem, mixer=mixer_type)
    print(f"{mixer_type}: approximation_ratio = {result.ratio}")
```

### Example 4: 两步QAOA优化
```python
# Step 1: 经典预筛选
candidates = classical_screening(assets, top_k=20)

# Step 2: 量子优化权重分配
weights = qaoa_optimize(candidates, constraints)

# 对比纯量子方法
qubit_savings = len(assets) - len(candidates)
print(f"Qubit savings: {qubit_savings}")
```
User: "用量子随机数估计投资组合的VaR"

Agent:
1. 设置 Monte Carlo 参数
2. 解释 QRNG 优势
3. 提供实现框架
4. 对比经典 RNG 结果
```

## Resources
- **kg.db**: 本地知识图谱存储量子金融论文
- **kg_tool**: CLI查询工具
- **weekly_topics.py**: 今日主题获取
- **references/qnn-option-pricing.md**: QNN期权定价跨平台基准测试结果 (IBM Fez, IonQ Forte, Rigetti Ankaa-3, IQM Garnet)
- **references/arxiv-retry-patterns.md**: arXiv API 429/超时时的重试和缓存回退模式
- **references/arxiv-api-escalation-2026-05-23.md**: arXiv API 完全失效的升级报告 + 浏览器替代方案
- **references/quantum-nisq-resilience-benchmark.md**: NISQ 表达力-相干性权衡分析 (arXiv:2606.07727) — SWAP tax量化、HE-VQNN vs WS-QAOA硬件对比、SPSA优化器选择

## QRL Portfolio Optimization (Added 2026-06-20)

### Pattern: Variational Quantum Circuit as RL Policy Network
Based on arXiv:2601.18811 (VQC-Based RL for Dynamic Portfolio Optimization) and related papers.

**Approach**: Replace classical neural network policy with a Variational Quantum Circuit:
1. Encode market state s_t → quantum state |ψ(s_t)⟩ via amplitude/angle encoding
2. Apply VQC(θ), measure to get action probabilities
3. Update θ using parameter-shift rule + classical optimizer (Adam/COBYLA)
4. Use classical RL training loop (PPO, A3C, Q-learning variants)

**Key techniques from recent papers**:
- **Hot-starting** (arXiv:2510.11153): Initialize VQC from classical solution to avoid barren plateaus
- **Sector rotation** (arXiv:2506.20930): Hybrid QRL with PPO backbone for sector rotation trading
- **Dynamic clustering** (arXiv:2512.21819): Q-A3C2 with time-series dynamic clustering for ETF selection
- **QRAM state prep** (arXiv:2604.25644): O(log²(MN)) complex-valued state preparation for efficient data loading

**Barren plateau mitigation**:
- Problem-inspired ansatz over hardware-efficient
- Layer-wise training with gradual depth increase
- Hot-start from classical policy weights

**See also**: `qrl-dynamic-portfolio` skill for full methodology.

## Related Skills
- `qrl-dynamic-portfolio` — Full QRL portfolio methodology (arXiv:2601.18811)
- `stock-analysis`: 经典股票分析
- `arxiv-search`: 论文搜索
- `skill-extractor`: 从新论文提炼模式
- `qpinn-portfolio-optimization`: 量子PDE求解器（QPINN/Tensor Rank用于Merton组合优化）
- `qadqn-trading`: 量子注意力DQN交易策略（S&P 500 Sortino 1.28）