---
name: mts-slds-multi-timescale-switching
description: Use when inferring regime-specific neural timescales from population recordings. MTS-SLDS method.
version: 1.0.0
created: 2026-10-03
author: Hermes Agent
category: neuroscience
metadata:
  arxiv_id: "2610.01786"
  published: "2026-10-01"
  authors: "Lulu Gong, Yongxu Zhang, Shreya Saxena"
  tags: [neural-timescales, switching-linear-dynamical-systems, laplace-em, moment-initialization, poisson-observations]
---

# MTS-SLDS: Multi-Timescale Switching Linear Dynamical Systems

## 核心问题与突破

**问题**：神经群体活动包含多时间尺度（快/慢波动共存），且随行为状态切换。传统自相关（ACF）拟合无法扩展到高维群体记录，在动力学随行为变化时不可靠。标准 SLDS 虽能建模高维群体潜在动力学，但**不能保证恢复时间尺度谱**——两个特征值不同的转移矩阵可产生相似似然，因为似然对观测预测最敏感，对背后的衰减率只是间接敏感。轨迹重构好 ≠ 时间尺度恢复好（两者可以完全解离：相似 held-out R²=0.82 下，时间尺度误差 11% vs 44%，regime 准确率 0.95 vs 0.54）。

**突破**：MTS-SLDS 两阶段框架：
1. **多滞后矩初始化**（Multi-lag moment initialization）——用多个观测滞后上的矩关系直接约束衰减率
2. **regime-conditioned Laplace EM（RC-L-EM）**——推断期间为每个候选 regime 维护独立的高斯状态近似，防止不确定 regime 指派混合跨 regime 的动力学统计量

拟合后从每个 regime 的转移矩阵特征值直接读出时间尺度：`τ = -Δt/log|λ|`。

## 方法论详解

### 1. 模型设定

SLDS 潜在状态模型（连续潜态 x_t ∈ R^H + 离散 regime z_t ∈ {1..K}）：

```
z_t | z_{t-1}=i ~ Cat(P_{i,:})
x_t | x_{t-1}, z_t=k, u_t ~ N(A_k x_{t-1} + b_k, Q_k)
```

两种发射模型：
- **Gaussian 观测**：`y_t | x_t, z_t=k ~ N(C_k x_t + d_k, R_k)`（连续信号）
- **Poisson 观测**：`y^n_t | x_t, z_t=k ~ Poisson(exp(c^n⊤_k x_t + d^n_k))`（脉冲计数，条件独立，exp 链接）

每个 regime 通过 A_k 的特征值 λ_{k,j} 表征。衰减模态（0<|λ|<1）：
- 弛豫时间尺度 **τ_{k,j} = -Δt / log|λ_{k,j}|**
- 振荡频率 **f_{k,j} = |arg(λ_{k,j})| / 2πΔt**

正实特征值=非振荡衰减；复共轭对=阻尼振荡。**注意区分**：这些时间尺度是 regime 固定下的潜态动力学，不同于 P 控制的 regime 驻留时间。

### 2. 多滞后矩初始化（关键创新 1）

对固定 regime k 的稳定平稳参考过程，观测矩满足：

```
M_{ℓ,k} = C_k A^ℓ_k Σ_k C_k⊤    (ℓ > 0)
```

- Gaussian 观测：M_{ℓ,k} = Γ_{y,k}(ℓ)（直接用滞后协方差）
- **Poisson 观测的元素级矩转换**（Buesing et al. 2012 谱学习关系）：

```
[M_{ℓ,k}]_{nm} = log(1 + [Γ_{y,k}(ℓ)]_{nm} / (μ_{n,k} μ_{m,k}))
```

其中 μ_{n,k} 是参考过程下的均值 firing rate。这个 log 转换把 Poisson 观测协方差转回线性潜态矩。

**实践流程**：
1. 从合并的 trial 内正滞后矩构造低维投影
2. 对标准化的滑窗自相关描述子做 **K-means** 得到临时 regime 标签
3. 估计 regime 特定观测均值，只用完全落在同一 regime 内的滞后区间重算矩
4. 选定滞后上投影矩矩阵之间的**正则化回归**求初始转移算子
5. 映射到与发射参数兼容的潜坐标

这些平稳恒等式只是初始化动机，对实际切换数据不必精确成立——产物仅作 RC-L-EM 的起点。

### 3. Regime-Conditioned Laplace EM（关键创新 2）

**标准变分 Laplace EM 的问题**：因子化后验 q_x(x)q_z(z) 中 q_x 是所有 regime 共享的单一高斯轨迹近似。A_k 更新用的是**同一组状态矩**，仅以 regime k 的 responsibility 加权——指派不确定时每个 A_k 都在被部分属于其他 regime 的矩拟合。

**RC-L-EM 的解法**：通过切换滤波/平滑（GPFA-sPCF 谱系，Song & Shanechi 2023）为每个候选 regime 和相邻 regime 对维护**独立的高斯状态近似**：

前向滤波：`q_f(x_t, z_t=k) = γ_t^f(k) N(x_t; m_t^(k), V_t^(k))`——每个 regime 携带自己的状态估计。
- 对每个目标 regime：匹配入射状态分量的前两阶矩 → 经 A_k 传播 → 并入 y_t
- Gaussian 观测用高斯测量更新；Poisson 观测对每个 k 做**局部 Laplace 近似**
- 预测证据 L_t(k) ≈ p(y_t|z_t=k, y_{1:t-1}) 与 Markov 预测合并更新 regime 权重

后向平滑给出 γ_t^s(k) 和相邻 regime 概率 ξ_t(i,k)，以及条件高斯对 q_t^{ik}(x_{t-1}, x_t)。

**M 步中 A_k 更新的矩差异**（这是核心公式）：

```
RC:  M_{t,k} = Σ_i ξ_t(i,k) E_{q_t^ik}[x_t x_{t-1}⊤]   ← 期望本身以 regime 对为条件
MF:  M_{t,k} = γ_t^s(k) E_{q_x}[x_t x_{t-1}⊤]           ← 只有标量权重依赖 k
```

期望回归公式两者相同，差别只在供给的矩。M 步：期望回归更新线性动力学；期望转移计数更新 P；regime 条件状态矩决定发射更新。Poisson 期望对数似然用高斯指数矩解析表达，数值优化。

### 4. 判别式实验设计（可复用模式）

- 合成数据：128 通道 Gaussian/Poisson 观测 ← 10 维潜态，5ms bins，30 训练 + 20 held-out trials × 4s
- 平稳实验 K=1：时间尺度 {20, 100} ms，每个 5 个模态
- 切换实验 K=2：谱 {10,40,100} vs {20,80,300} ms（3/3/4 模态），对称 Markov 自转移 0.9975（期望驻留 2s）
- **MAPE 度量**：先匹配推断 regime/模态到 ground truth 再算误差
- 对比基线：标准 SLDS（ssm 库变分 Laplace EM）、双指数 ACF 拟合、aABC（Poisson）

**关键结果**：
- 切换 Poisson 实验：轨迹重构相当（R²=0.82）但 MTS-SLDS regime 准确率 0.95 vs 0.54，时间尺度误差 11% vs 44%
- Gaussian SNR 0.5-5 两种方法都 ~6% 误差；Poisson 0.05-0.5 counts/bin 时 MTS-SLDS 误差低 1.7-3.3 倍
- 消融：RC-L-EM 贡献大部分 regime 信息恢复；多滞后初始化补齐剩余时间尺度误差差距

### 5. 神经数据应用（验证模式）

**V4 固视（16 通道猕猴，2ms bins，K=1 Poisson）**：
- H∈{2..10} 五折 CV + 多种子 → 预测饱和于 H=8
- held-out log-likelihood 每试验 +52.4±6.9
- 模型模拟的池化自相关比 SLDS 更贴近实测（MTS 0.045 vs SLDS 0.086 偏差）
- 三个可复现时间尺度：**26.4 / 49.5 / 120.2 ms**（SLDS: 23.5/36.1/110.9；ACF-exp: 3.0/55.4；aABC 两分量: 28.3/108.1）
- 教训：ACF 池化把两个较快潜态带压缩成一个"有效衰减"，标量投影掩盖部分模态贡献

**S2 触达/到达（20ms bins，K=2 Poisson，H=6）**：
- 推断 regime 与运动 onset 对齐
- 运动关联 regime 的中位时间尺度：主动到达 188ms vs 被动扰动 99ms——与行为学衰减时间 168/86ms 对应
- SLDS 两试次类型给出几乎相同的 117/108ms（无法区分）
- sPCF-EM 基线也无清晰区分——支持方法特异性
- 附加检验：打乱数据拟合未见相同结构（阴性对照）

## Pitfalls

1. **不要把轨迹重构质量当作时间尺度恢复的证据**——两者可解离，必须直接对 ground truth 谱评估（合成数据）或与独立行为测量对照（真实数据）
2. **Poisson 矩转换需要均值**——μ_{n,k} 估计误差会传播到初始化；只用完整落在同 regime 的滞后区间
3. **多滞后初始化假设 regime 内近似平稳**——短 regime 驻留、弱观测模态、密集衰减率、有限记录时长都会限制可恢复性
4. **有效时间尺度 ≠ 内禀时间尺度**——拟合的 A 可能吸收来自未观测区域或行为变量的持续驱动（Chaudhuri 2015 谱系的问题在此保留）
5. **RC-L-EM 仍是近似 EM**——矩匹配 + 局部 Laplace 不保证单调 ELBO 增或全局最优/无偏
6. **H 和 K 选择**：用 held-out 预测似然选 H；K 的选择在切换场景需先验理由（本文运动任务用 K=2 对应预运动/运动两态）
7. **数值细节**：从 λ 提取 τ 时若 |λ|→1 则 τ 发散——限定分析频带（本文 S2 用 20-300ms 频带规避 bin 尺寸与试次窗口限制）

## 与相关方法的关系

- **vs aABC**：aABC 是汇总统计匹配，处理有限样本偏差且量化不确定性，但作用于群体求和计数（标量投影）。MTS-SLDS 保留全部空间信息
- **vs 谱学习（Buesing 2012）**：继承 Poisson 矩转换思想，但推广到切换系统 + EM 精炼
- **vs sPCF-EM（Song & Shanechi）**：RC-L-EM 的切换滤波谱系来源，但 sPCF 不显式测试谱恢复
- **vs Zoltowski/Linderman ssm 变分 Laplace EM**：因子化 q_x 是标准实现；RC 版本保留 regime 条件矩——这是恢复 regime 特定谱的关键差别

## 实现路线图

1. 数据准备：trial 化 spike counts，选 bin 宽（注意 τ 可分辨下限 ~bin 尺寸）
2. 滑窗 ACF 描述子 + K-means → 临时 regime 分割
3. 每 regime 内估计 μ，Poisson log 矩转换，多滞后正则化回归 → A_k 初始化
4. RC-L-EM 循环：前向切换滤波（每 regime 独立高斯）→ 后向平滑 → 矩条件化 M 步 → 重复
5. 特征值分解 A_k → τ 谱 + 振荡频率
6. 验证：held-out 似然、模拟 ACF 对比、打乱对照、（如有）与行为时间尺度相关

## Applications

- 皮层层级时间尺度组织（Murray 2014 谱系）的 regime 感知版本
- 行为状态（注意/固视/运动）切换下的时间尺度重组研究
- 跨皮层区域时间尺度比较（V4 vs S2 模式）
- BCI 潜态动力学表征：regime 感知的 timescale 提取可改进状态估计器设计
- 神经质（neural latents）竞赛数据的动力学结构分析工具

## Sources

- arXiv: 2610.01786 (submitted 1 Oct 2026)
- Data: V4 fixation (Gieselmann & Thiele 2023, Engel 2016); S2 reaching (Dandi 000127, Lawlor 2018, Miller 2022)
- Builds on: Buesing et al. 2012 (spectral learning); Zoltowski et al. 2020 (ssm); Song & Shanechi 2023 (sPCF); Zeraati 2022 (aABC)
