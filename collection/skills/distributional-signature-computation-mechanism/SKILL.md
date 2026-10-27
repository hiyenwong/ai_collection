---
name: distributional-signature-computation-mechanism
description: Use when inferring mechanisms from runtime distributions.
category: ai_collection
metadata:
  arxiv_id: "2610.23607"
  published: "2026-10-16"
  authors: "Céline van Valkenhoef, Catherine Schuman, Nikolaus Kriegeskorte, Philip Walther (Univ. Vienna / UT Knoxville / Columbia)"
  source: "arXiv q-bio.NC"
---

# Distributional Signatures of Computation：从计算时间分布推断计算机制

**论文**: "Distributional signatures of computation: inferring mechanisms from computation time distributions" (arXiv:2610.23607, van Valkenhoef, Schuman, Kriegeskorte & Walther)

## 核心思想

有限物理计算系统（生物/经典/神经形态/量子）的内部算法与架构常不可直接观测。计算时间（如反应时 RT）不只是"围绕均值的噪声"——**其完整分布是随机计算动力学的可观测签名（distributional signature）**，可用于反向推断计算机制。

**因果链**：计算机制 → 随机动力学 → 计算时间分布；**经验推断** = 逆因果链，从观测分布推断机制。计算时间被当作 observable 而非 resource，与复杂性理论互补：复杂性刻画抽象模型的渐近资源，本框架刻画有限物理实现的计算组织（computational organisation）。

## 为什么均值/基准测试不够

- 均值 RT 分析把分布压缩成单一数字，丢弃了机制线索；跨被试聚合还会扭曲分布形状
- 基准曲线（linear/√N 等）需要**任意缩放因子**对齐 → 解释强依赖缩放假设；同 scaling 的不同机制不可区分
- 模型时间步与人类秒之间无内在可比性，斜率差异不可直接解读

## 机制 → 分布形状识别表（可复用目录）

| 机制 | 分布（跨规模） | 固定规模剖面 |
|------|--------------|------------|
| 确定性执行（与规模无关） | 常数带 | δ 峰 |
| 顺序遍历（解位置在确定路径上随机） | 均匀 | 均匀 |
| 干涉动力学（类波构造/破坏） | 带状 | 周期峰 |
| 累积过程（证据逐步积分） | 分级密度 | 指数 → gamma → ex-Gaussian（累积度越高越宽、正偏越强） |

累积类内部再分层：**无引导随机采样**（重复访问低后验位置→更长累积→更宽更偏）比**后验引导采样**更宽；**驻留式局部累积**（无空间记忆）产生中等 gamma 形剖面。

## 方法流水线

1. **可扩展任务设计**：输入规模跨 ~3 个数量级（示例：视觉搜索 400→320,000 像素）；设基线条件（目标异色→常数时间搜索）扣除渲染/运动成本
2. **基准测试**：计算时间 vs 规模拟合 constant/log/linear/poly/exp → 只约束总体效率阶数
3. **特征分布（characteristic distribution）**：每条 RT 除以其输入规模（divisive normalization），在 ~线性 scaling 假设下把全部规模的观测聚合 → 高统计力的剖面形状估计
4. **模型比较（时间单位不可比时的双统计量）**：
   - **KS 形状分析**：逐被试在 log 尺度上一维有界优化拉伸因子 s∈[10⁻³,10⁵]，最小化两样本 KS 距离（KS 原生支持不等样本量，无需重采样）；成对差 + 两侧配对 t 检验
   - **LOO 边际对数似然**：对模型 RT/位置拟合 Gamma 族 → 逐被试 MAP 拉伸（log s 上弱正态先验）→ 用其余被试的 MAP 拟合 LOO 经验贝叶斯先验 → Gauss-Hermite 积分（log 空间）得逐被试 mLLH → 成对差对被试 bootstrap（10⁴ 次）求 95% 区间

## 演示结果（人类视觉搜索）

任务：49 像素 emoticon 目标藏于随机黑白背景；94 名被试（1 人 1398 trial 特大型数据集）。人类特征分布 = 短 RT 高密度 + 重尾。三模型均值 scaling 均 ~线性（benchmarking 不可区分），但分布形状分层：

- **rDDM**（随机采样、全局后验不用）最差：分布下界随规模上移、最宽
- **gDDM**（采样最大后验位置）居中：捕获部分偏度
- **MNM**（浅层脉冲网络：90×90 中央凹密度视场、7×7 目标匹配滤波器、explore→confirm→verify 驻留式局部累积、无空间记忆、RISP 基底）最贴人类
- KS 与 LOO mLLH 排序一致：rDDM < gDDM < MNM
- **结论**：人类视觉搜索 ≈ 有限记忆、驻留式、图像可计算（image-computable）的证据累积，而非全局后验引导采样

## 三种推断模式

1. **结构推断**：内部组织不可观测的系统（大模型、生物认知、黑盒硬件）从行为分布推断机制
2. **时间推断**：学习 = 计算机制的演化 → 追踪分布签名随训练/适应的漂移，跨学习系统比较
3. **跨基底比较**：经典/模拟/神经形态/量子/生物系统在机制层面对齐；同一机制在不同物理实现中的签名差异本身是研究对象

## 注意事项

- 剖面形状**不唯一识别机制**（不同机制可产生相似剖面）；有限数据必须有代表性；多机制混合 → 剖面模糊
- 时间单位不可直接换算——必须用拉伸因子 + 不确定度积分处理
- 特征分布归一化假设 ~线性 scaling：先验证 scaling 阶数再归一化

## 实践检查清单

1. 收集跨规模、足量重复测量（随机性来自系统本身而非测量噪声）
2. 先基准测试定 scaling 阶数，再做分布分析
3. RT÷规模归一化聚合出特征分布，对照识别表定位机制类别
4. 候选机制模型用 KS+拉伸 与 LOO mLLH 双统计比较（两者应给出一致排序才算稳健）
5. 对"混合机制"剖面先做分解检验再下结论
6. 报告缩放因子的不确定度（bootstrap），勿只报点估计

## 相关

- `harmonic-spectroscopy-animal-decisions` - 决策谱测量（"分布即签名"思想的行为学变体）
- `backtest-live-parity-defects` - 同类"均值之外看分布"的审计哲学
