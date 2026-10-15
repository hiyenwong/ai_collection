---
name: energy-information-neuropsychiatric-classification
description: Thermodynamic framework explaining weak neuroimaging biomarkers in psychiatry. Use when probing classification limits of brain disorders.
category: ai_collection
---

# Energy, Information, and the Limits of Neuropsychiatric Classification

**source**: arXiv:2610.14095 (Farbod Khodadadi, Hamidreza Jamalabadi (corresponding), et al., Marburg/Münster FOR2107 Consortium, v1 8 Oct 2026)
**papers**: Khodadadi-Jamalabadi et al., "Energy, Information, and the Limits of Neuropsychiatric Classification", 2026
**task**: 解释为什么精神疾病临床表现重但神经影像可分性弱；给出可分类性的热力学上界框架
**field**: computational psychiatry, neuroimaging biomarkers, statistical thermodynamics, energy landscapes

## Activation

- 研究 MDD/精神疾病的神经影像 biomarker 为何始终达不到个体水平诊断精度
- 建模"临床差异大 vs 影像重叠多"的矛盾（分类上限问题）
- 用 energy landscape / Hopfield 式状态占有率分析 fMRI 动力学
- 关键词: psychiatric biomarker limits, energy landscape fMRI, major depressive disorder classification, computational psychiatry, statistical energy, shared neural repertoire

## Summary

**Problem**: 数十年研究后，精神疾病的神经影像 biomarker 依然缺失——大型协调分析（MDD 4021 人）只找到弱且异质的相关，诊断性能在各种预处理/特征/模态/架构下都平庸。该平台期引出一个比分类器选择更根本的问题：**类条件分布本身到底有多少可分性？**

**Hypothesis（信息-能量约束假说）**: 基于统计热力学 + 神经编码代谢成本：精神疾病不创造新的脑状态 repertoire，而是对**共享活动景观产生能量受限的形变（deformation）**——输入重塑共享 repertoire、连接组限制传播方向、代谢限制形变的幅度/速度/稳定性。约束并非全局标量：认知控制与努力决策回路能耗最高，能量可得性下降使景观不均匀倾斜；外周/内感受信号进一步节点特异地调制能量状态（把可用 repertoire 与机体稳态耦合，而非纯中枢预算）。行为由被支持的轨迹产生，而神经影像只不完备地观察其分布。

**Framework（四环节链条）**: 物理资源约束 → 景观形变 → 分布分离 → 可达分类。每一环都做了实证检验：

1. **分布分离与分类上限**: 用 likelihood-ratio 排序得到最优 ROC——灵活解码器可逼近但不可恢复输入中不存在的类信息。达到的性能依赖样本/估计/算法；种群级上限依赖表征及其背后生物学。
2. **能量景观实证（人类数据）**: FOR2107 队列静息态 fMRI（1952 人：MDD 823 + HC 1129，Marburg/Münster 两中心），held-out 能量景观估计与非线性分类器在 13 项比较中一致（r=0.996）；SRPBS 900 人跨多诊断复现。统计能量≈物理势能/温度（在精确指定的三井平衡模型中验证）。
3. **合成数据**: 分类精度随分布分离度提升并逼近最优——分离度不足时任何算法都无济于事。
4. **三井模型（exactly specified physical model）**: 适度形变只重新分配状态占有率（occupancy redistribution），snapshot 分类的最优判别仍然弱——**直接演示"形变≠可分"**。
5. **诚实边界**: 文献地图发现目前**没有足够可比的人类证据来检验代谢约束环节**——该机制在人类中的实现仍属未检验状态；检验需要脑活动+身体生理+代谢的联合测量。

**Key results**:
- MDD vs HC 的能量景观形变存在且可复现（双中心、跨诊断队列一致）
- 但形变导致的分布重叠使最优分类上限本身很低——**不是分类器不够好，而是信息不在表征里**
- 统计能量与物理势能的比例关系（三井模型中 E_stat = U/T 形式的标度）
- 代谢约束是链条中最薄弱、最难检验的一环（作者明说 untested）

**Why it matters**: 把"精神疾病神经影像分类为何失败"从工程问题（换更好的分类器）提升为物理问题（表征的信息容量上界）。对 biomarker 研究的实践含义：与其继续在分类器上内卷，不如测量"分布分离度"这个上界本身；如果上界低，应当改变表征（时间维度、代谢联合测量）而非算法。

## Pattern: 上界优先的失败诊断法

可复用方法论——当某个预测任务持续达不到实用精度时：
1. 先估计**最优可达性能**（likelihood-ratio 上界、Oracle 分类器），而非先调算法
2. 若上界本身就低，问"类信息在当前表征中是否存在"，而非"算法是否够灵活"
3. 用机制模型（此处能量景观）解释上界为何低（形变共享景观 → 占有率重分配 → snapshot 重叠）
4. 明确指出框架中最未检验的环节（本文诚实标注代谢约束 untested），设计能区分机制与噪声的联合测量

## Pitfalls

- **Snapshot 局限**: 每人只有一张时间平均连接 snapshot；拟合分布描述的是组级 snapshot 重叠，不等于个体轨迹空间的可分性
- **能量≠可直接观测**: 统计能量是从占有率重构的推断量；"代谢约束"在人类上没有直接的测量证据（作者自己声明）
- **不要过度解读为"精神疾病不可分类"**: 结论是"在 fMRI 静息态连接表征下上限低"；动态表征、跨模态联合、或症状维度化可能突破
- **相关性 r=0.996 的一致性**是能量估计与分类器在 held-out 上的共识，不是因果证明
- 相关文献: dynamical-systems 账户（小几何/流变化 → 状态占有率/驻留/转移改变）是本框架的近亲，注意区分"形变共享景观"与"完全不同动力学"两种假说

## Related skills

- `heteroclinic-cognitive-state-modeling` — 认知状态的动力学/景观建模
- `griffiths-phase-brain-criticality` — 脑动力学临界区与个体变异
- `efficient-coding-criticality` — 能量/资源约束下的高效编码
- `eeg-hopfield-emotion-energy-landscapes` — 能量景观量化（EEG 情绪）
- `neuroscale-dynamical-changepoint-detection` 相关的动力学系统工作
