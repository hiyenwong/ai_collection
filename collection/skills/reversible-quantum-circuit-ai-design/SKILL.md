---
name: reversible-quantum-circuit-ai-design
description: "AI自主设计高效量子电路的方法论：Claude在53小时内以纯文本规格+自动评估器闭环超越8个计算基元(模逆/point addition/Reed-Solomon解码等)的最优发表电路，部分改进超一个数量级(12x)。核心技术：可逆divsteps模逆=从迭代后数值对直接decode分支信息而非存储历史(省全部辅助qubit)；LLL格规约数学推导解码公式并用Lean形式化验证；Berlekamp-Massey替代扩展欧几里得(固定轮数固定步骤结构适配量子电路)；用403M次采样模拟测量最坏情况内存需求(665→19 qubits，1/10000失败率在容许内)；存储vs解码阈值扫描扩展Pareto前沿(12%更多qubit换17x更少门)。适用于量子算法资源优化、可逆计算设计、AI驱动科学发现闭环。Activation: quantum circuit synthesis AI, reversible modular inversion divsteps, branch information decoding uncompute, Berlekamp-Massey quantum decoder, DQI Reed-Solomon, qubit gate tradeoff Pareto, Lean verified quantum circuit, space time tradeoff uncompute"
version: 1.0.0
author: Andi Gu (Anthropic STEM Fellows), Alek Kemeny, Susanne Yelin (Harvard), Mikhail Lukin (Harvard/QuEra). arXiv:2610.22367
date: 2026-10-16
source: https://www.anthropic.com/research/designing-efficient-quantum-circuits
category: ai_collection
tags: [quantum-computing, circuit-synthesis, reversible-computing, ai-scientist, algorithm-design]
activation_keywords: [automated quantum circuit design, reversible divsteps modular inversion, branch history decoding without storage, Berlekamp-Massey vs extended Euclidean quantum, decoded quantum interferometry DQI decoder, worst case memory sampling 403 million, store versus decode threshold family, Pareto frontier qubits gates, AI closed loop evaluator score, Lean formal verification circuit, FeMoco Toffoli count reduction, AI design hardware co-optimization quantum]
---

# AI 自主设计高效量子电路

## 任务设置（AI 科学发现闭环的可复制模板）
- **输入**：8 个计算基元的纯文本规格（化学/优化/物理模拟/数论/数值计算），不给参考实现
- **验证器**：外部评估器程序——检查正确性 + 客观打分（qubit 数 × 门数 = 运行时代价）
- **闭环**：Claude 提案 → 评估器反馈+分数 → 改进，轮间**无人工输入**，53 小时跑完
- 适合 AI 的三条件：①设计可写成代码 ②正确性可机器高效验证（每个输入一个确定输出）③有清晰客观分数。**FeMoco 基准**：50 万亿 Toffoli（2017）→ 3.4 亿（社区 8 年）vs Claude 单次 53 小时推出椭圆曲线新设计

## 发现 1：可逆 divsteps 模逆（椭圆曲线 point addition 的最贵步骤）
- **难点**：divsteps（模逆的迭代法）每轮记录"选了哪个操作"（branch information）；量子电路必须可逆 → 传统做法要把全部分支历史存进额外 qubit，代价爆炸
- **Claude 的洞察**：分支信息或许**根本不用存**——从每轮迭代后的数值对本身就能"解码"出分支记录。数即记录，电路可倒着跑，零额外 qubit
- **怎么做到的**：先试猜测性解码规则（小案例通过、256-bit 全尺寸失败）→ 转向理论路线：证明 divsteps 迭代的新代数恒等式 → 从恒等式**推导出精确解码公式** → 大规模数值模拟检验 → **Lean 形式化证明**
- **空间-时间权衡族**：解码省 qubit 但费门；扫描"何时存 vs 何时解码"的阈值 → 产出新设计族：最小已知设计基础上 +12% qubits 换 **17× 更少门**，扩展 Pareto 前沿

## 发现 2：DQI 的 Reed-Solomon 解码器降 12×
- 背景：Decoded Quantum Interferometry 是最有希望的超多项式量子加速算法；最贵步骤 = 纠错解码器（从 syndrome 恢复错误位置）。此前最优用扩展欧几里得——但其步数和顺序依赖输入，量子电路必须对所有叠加输入跑同一固定门序列 → 只能按最坏情况拉长
- **方法层**：换 **Berlekamp–Massey**——每轮执行同类操作、固定轮数，天然适配固定门序列
- **架构层**：沿用"解码而非存储"思路重构临时值；少数例外值无法解码、必须保存——**最坏情况预留 665 qubits**
- **预算层**：Claude 写高速模拟器跑 **4.03 亿次采样解码**实测例外频率：几乎每次至多存 1 个值 → 只留 19 qubits，失败率 1/10000 在任务容许误差内
- 三层缺一不可：换方法 + 换架构 + 用统计实测替代最坏情况预留 → 门数相对 Google 之前构造降 **12×**

## 通用可迁移原则
1. **可逆计算的两大约束**：无 if-then（叠加态要求两分支操作都执行）+ 不可丢弃信息（scratch 必须 uncompute）→ 空间-时间强权衡
2. **"解码代替存储"**：若中间信息可从当前状态重构，就别存——uncompute 的成本从内存转嫁到少量解码门
3. **最坏情况预算 vs 统计实测**：模拟采样测真实分布，用可控失败率换数量级资源节省
4. **AI 协作的保守偏差及对策**：Claude 反复自我怀疑、偏好已知方法 → ①强制并行探索多个质性不同的方案 ②定期提示"想得更宽"。保守性也有价值（催生了 Lean 证明）
5. **下一步展望**：QEC 全栈组件（码/解码器/控制）目前各自独立设计——AI 可做**算法到硬件的联合优化**，产出面向特定问题的整台容错量子计算机

## 与相关 skill 的关系
- 与 [[human-ai-quantum-co-discovery]] 互补：那是人主导直觉+AI 扩展；本 skill 是 AI 主导闭环+人只写规格
- Berlekamp–Massey 选型逻辑可参考 [[mld-quantum-decoding]]（QEC 解码综述）

## 引用来源
Gu, A., Kemeny, A., et al. (2026). Designing more efficient quantum circuits with Claude. https://www.anthropic.com/research/designing-efficient-quantum-circuits (arXiv:2610.22367)
