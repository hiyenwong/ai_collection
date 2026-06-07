---
name: quantum-finance-portfolio
description: "量子计算在金融组合优化中的应用。涵盖 QUBO建模、量子退火、QRNG增强Monte Carlo、VaR/CVaR风险估计、QAOA Mixer选择、两步QAOA优化、混合量子优势审计、QRL动态组合优化、QAOA+ZNE误差缓解。触发词：量子金融、quantum portfolio、量子组合优化、quantum annealing finance、QRNG VaR、QAOA mixer、hybrid quantum audit、D-Wave hybrid、量子优势审计、quantum contribution measurement、QRL、QDDPG、QDQN、ZNE、zero noise extrapolation、carbon credit portfolio"
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

## Instructions for Agents

### Step 1: 问题分析
当用户请求量子金融任务时:
1. 确定问题类型 (聚类/优化/风险估计)
2. 评估量子适用性
3. 选择合适模式 (QUBO/QRNG/混合)

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

## Related Skills
- `stock-analysis`: 经典股票分析
- `arxiv-search`: 论文搜索
- `skill-extractor`: 从新论文提炼模式
- `qpinn-portfolio-optimization`: 量子PDE求解器（QPINN/Tensor Rank用于Merton组合优化）
- `qadqn-trading`: 量子注意力DQN交易策略（S&P 500 Sortino 1.28）