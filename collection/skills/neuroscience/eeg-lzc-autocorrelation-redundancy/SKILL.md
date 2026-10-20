---
name: eeg-lzc-autocorrelation-redundancy
description: Use when interpreting EEG Lempel-Ziv complexity results.
category: ai_collection
metadata:
  arxiv_id: "2610.23231"
  published: "2026-10-16"
  authors: "Pedro Montoya, Ignacio Cifre, José Luis Rosselló Sanz, Dante R. Chialvo (UIB / IAIB / CONICET / HKBU)"
  source: "arXiv q-bio.NC, cond-mat.dis-nn"
---

# EEG Lempel-Ziv Complexity ≈ 一阶自相关的逆序代理

**论文**: "EEG Lempel-Ziv Complexity vis-à-vis Autocorrelation Function" (arXiv:2610.23231, Montoya, Cifre, Rosselló & Chialvo)

## 核心主张

归一化 Lempel-Ziv 复杂度（LZC）与 lag-1 自相关（AC1）存在**稳健的逆关系**：时间相关性越强 → LZC 越低。EEG 中 LZC 捕获的信息很大程度上是**时间冗余**——ACF 已经量化、且神经生理学解释更直接（振荡持续性、网络同步、时间整合、临界慢化）的部分。解释任何 EEG 复杂度结果前必须先审计：**AC1（及谱/SNR 等简单描述子）能否解释该变化？**

## 理论链（为何必然相关）

对称二态 Markov 链（转移矩阵含 ρ）的翻转概率 **q = (1 − AC1)/2**，熵率 **h(AC1) = H₂((1−AC1)/2)**（H₂ 二元熵函数）。Ziv 定理：平稳遍历源的归一化 LZ76 复杂度随长度→熵率；**有限长度 LZC 系统性高于该渐近线**（收敛极慢的有限尺寸效应）→ LZC 与 h 是单调映射+恒定偏移。任何提升时间可预测性的过程都增加模式重复 → 提高 LZ76 压缩率 → 降低 LZC。

## 定义

- **AC1**：归一化自相关 ρ(k)=R_xx(k)/R_xx(0) 在 lag-1 的值（EEG 采样率决定 lag 对应时长）
- **LZC**：信号二值化（阈值=median 或 mean）→ LZ76 左到右解析出不重复子串数 c(S) → 归一化 CLZ = c(S)/c_max，c_max(N)=N/log₂N；在窗口化段（1–10 s）上计算

## 三层合成验证

1. **Markov 链**（ρ=0.6–0.95，n=64 实现）：AC1=ρ 精确成立；1−LZC 与 AC1 同步单调；LZC vs H₂((1−AC1)/2) 单调且系统性高于对角线（有限尺寸偏置可视化）
2. **一维随机 Cantor 集**（长程相关；二分叉 b=2、保留概率 P；分维 D=log(2P)/log₂，Hurst H=(D−1)/2，自协方差 γ(k)=(σ²/2)[(k+1)²ᴴ−2k²ᴴ+(k−1)²ᴴ]）：单调、弱非线性 → 关系不限于自回归类模型
3. **Decimation 粗粒化**：递增窗均值替换逐步去相关；LZC→1 与 AC1→0 在相关长度 ξ 处同时到达（decimation 可反过来估计 ξ，Martiniani et al.）

## EEG 证据

- **ERP（情绪-注意任务，51 被试 n=1632 trial；α 带 8–13 Hz，median 阈值二值化）**：单被试内 AC1/LZC 散点 ~线性稳定，pre-stimulus 100 ms 与 ERP 峰值区间均成立；跨被试池化同样成立——LZC 与 AC1 在真实实验中平行涨落
- **静息态 eyes open/closed（53 导联，512 Hz；5 min 条件窗 + 75 s 滑窗）**：两条件形成分离点团——**睁眼=低 AC1/高 LZC，闭眼=高 AC1/低 LZC**；75 s 滑窗显示关系随时间动态保持

## 临界性语境（为何 AC1 有机制解释）

复杂系统逼近临界点/同步边缘时 **AC1 普适增加**（critical slowing down；鸟群、磁自旋、SNN 神经元群体同样成立），且伴随功能连接 CC 上升。因此 AC1（和 LZC）可追踪自发唤醒波动 ≈ 系统到临界点的距离（Galbardon et al. r-spectrum 证据）。

## 对文献的影响

麻醉/NREM 睡眠 LZC 下降、致幻剂 LZC 上升等经典"意识复杂度"结果，应重新表述为**时间相关性/到临界点距离的变化**——现象不假，但把解释从"信息处理丰富度/意识内容"拉回可检验的神经生理机制层。

## 实操规则（审计任何 EEG LZC 结果）

1. LZC 变化先用 AC1 回归/散点审计（同段、同窗、逐 epoch 与导联）
2. 用 eyes open/closed 做正控制——应复现 AC1↑/LZC↓ 的两团分离
3. 报告有限长度偏置：LZC 在熵率渐近线上方，对序列长度/二值化策略敏感
4. AC1 零成本、免符号化、机制解释直接——**LZC 的增量价值必须实证**（对 AC1 回归后的残差里还剩什么？高阶相关？非高斯结构？）
5. 谱成分、SNR、振荡幅度变化都能伪装成"LZC 变化"——控制后再谈意识/信息处理解释
6. 注意边界：LZC ≯ AC1 数学等价（高阶相关不由单系数代表）；LZC 仍是紧凑描述子，"额外信息"要单独证明而非默认

## 相关

- `permutation-entropy-artifact-robust-eeg` - 同类审计（序数熵 vs 伪迹鲁棒性）
- `eeg-microstate-cluster-illusion` - 微状态聚类显著性审计
- `eeg-speech-decoding-detection-floor-audit` - 解码声明检出地板审计
