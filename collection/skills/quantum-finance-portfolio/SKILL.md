---
name: quantum-finance-portfolio
description: "量子计算在金融组合优化中的应用。涵盖 QUBO建模、量子退火、QRNG增强Monte Carlo、VaR/CVaR风险估计。触发词：量子金融、quantum portfolio、量子组合优化、quantum annealing finance、QRNG VaR"
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

## Tools Used
- `exec`: Run Python quantum computing scripts
- `web_search`: Search arxiv for latest quantum finance papers
- `web_fetch`: Fetch paper details from arxiv/Springer
- `sqlite3`: Query kg.db for related research

## Core Patterns (from 2025 research)

### Pattern 1: QUBO建模 (Graph-based Coalition - GCS-Q)

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
- arxiv 2509.07766: GCS-Q 图聚类
- arxiv 2502.02125: QRNG VaR/CVaR
- Springer 10.1186/s40854-025-00751-6: 量子金融综述

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

## Related Skills
- `stock-analysis`: 经典股票分析
- `arxiv-search`: 论文搜索
- `skill-extractor`: 从新论文提炼模式