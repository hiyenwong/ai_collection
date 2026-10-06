---
name: hierarchical-feature-memory-orientation-bias
description: 分析连续特征工作记忆的序列依赖时用。层级复合特征记忆痕迹理论。
metadata:
  arxiv_id: "2609.40204"
  published: "2026-09-30"
  authors: "Kira M. Düsterwald, Peter Vincent, Ana Kapros, Athena Akrami, Maneesh Sahani"
  source: "arXiv q-bio.NC (Gatsby Unit & Sainsbury Wellcome Centre, UCL)"
  tags: [computational-neuroscience, serial-dependence, working-memory, orientation-bias, hierarchical-processing, von-mises, efficient-coding, compound-features]
---

# Attraction to Hierarchical Feature Memory Explains Orientation Bias

## 核心论点

经典的"anti-cardinal bias"（观察者回忆朝向时系统性偏离水平/垂直轴）一直被归因于高效编码：环境常见的 cardinal 朝向分配更多神经资源、编码噪声更小。该论文推翻了这一标准解释——在**均匀编码精度**（各角度 fidelity 相同）下，一个基于**层级复合特征记忆痕迹**的最优推断模型即可完整复现 serial dependence 和 anti-cardinal bias 两种现象，无需任何编码不对称性。

**机制**：记忆痕迹不是孤立的单特征，而是跨皮层层级的**复合再激活**——一个 tilt 与其关于 cardinal 轴的**镜像反射**组成的复合特征。序列吸引效应由对前一次反应 Rn−1 **及其反射**的吸引主导，而非对前朝向本身。

## 关键实验发现（86 名线上被试）

1. **反射吸引**：当 Rn−1 与 Rn 在 vertical 同侧（congruent）时显著正圆相关（吸引）；异侧（incongruent）时显著**负**圆相关——即被吸引向 Rn−1 的**镜像反射**（均 p<0.001，置换检验）。
2. **层级签名——空间特异性分层**：前刺激呈现在对侧半视野时，orientation-specific（低层）吸引减弱，而复合特征（反射）吸引**跨视野中线保持**——符合高层表征空间抽象度更高的性质。
3. **响应主导**：GAM 分析显示序列效应由前次**报告的反应** Rn−1 而非前次刺激 Sn−1 驱动（Rn−1 之后 Sn−1 无额外方差解释）。
4. **EEG 解码再分析**（Wolff et al. 2020 数据）：orientation-evoked potentials 同时相似于相同朝向与反射朝向——工作记忆在神经层面编码复合 tilt/reflection 特征的初步证据。

## 定量模型

响应 Rn 为混合信念分布的均值（circular mean）：

- **当前样本信念**：p(Sn|Xn) = VM(Xn, κX)，内部估计 Xn ~ VM(Sn, κS)（von Mises，κ 为浓度参数）
- **复合记忆痕迹**：Rn−1 与 Rn−2 的 von Mises 混合分量，每个分量在 θ 与其反射 −θ（关于最近 cardinal 轴）处各放一个分量
- **编码精度先验均匀**——刻意不含 cardinal 资源倾斜

仅拟合 serial dependence 数据确定 κ 参数后，同一模型**零额外调参**复现了完整 anti-cardinal 响应偏差。结论：anti-cardinal bias = 吸引 Rn−1 与吸引其反射的平均 anti-cardinal 优势。

## 方法论价值（可复用模式）

1. **特征-反射分解**：分析角度/对称特征的工作记忆数据时，用 congruent/incongruent 圆相关分离"特征吸引"与"复合反射吸引"两种成分——后者是层级再激活的行为学指纹。
2. **跨半视野测试**：半视野操作（对侧 vs 同侧呈现）是区分低层（空间特异）与高层（空间抽象）记忆影响的实验设计模板。
3. **均匀编码对照建模**：先用"编码不对称"假说造对照模型，再证明均匀精度+复合记忆即可解释偏差——把"编码约束解释"与"推断结构解释"做因果分离。
4. **EEG ERP 相似度泛化**：用 Mahalanobis 距离/ERP 相似度在"相同朝向 vs 反射朝向"两条参考轴上扫描，检验工作记忆表征的复合性。

## 与标准理论的关系

- **支持**：serial dependence 的吸引性（Fischer & Whitney 2014）、anti-cardinal bias 的存在（Wei & Stocker 2015 的数据本身）。
- **修正**：Wei & Stocker 效率编码框架中"偏差⇐编码噪声各向异性"的因果方向——偏差可由推断层复合记忆痕迹产生，与编码资源无关。
- **提示**：Perceptual bias 研究需在模型空间中区分"编码端"（sensory fidelity）与"推断端"（memory prior 结构）两类解释源。

## 实现要点

- von Mises 混合响应模型可直接用 `scipy.stats.vonmises` 实现；circular correlation 用 Fisher 变换或置换检验。
- 复合特征定义：对朝向 θ∈[0°,180°)，反射算子为关于 0°/90° 轴的镜像，映射到圆上最近 cardinal 轴的反射角。
- 复现数据集：Noel et al. 2021 (PLoS Biol)、Wei & Stocker 2015 (Nat Neurosci)、Wolff et al. 2020 (PLoS Biol, 含 EEG) 均公开。

## 相关技能

- `harmonic-spectroscopy-animal-decisions` — 决策的谐波谱学（同为特征空间分析）
- `context-modulated-emrnn-memory` — 上下文调制的工作/情景记忆
- `functional-ensembles-deep-spiking-networks` — 复合特征在群体表征中的实现

## 标签

#computational-neuroscience #working-memory #serial-dependence #hierarchical-processing
