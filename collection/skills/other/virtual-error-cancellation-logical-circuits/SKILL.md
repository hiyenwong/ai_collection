---
name: virtual-error-cancellation-logical-circuits
description: Use when mitigating logical errors via syndrome reweighting with dual decoders.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.12400
source_title: Measure Now Mitigate Later - Virtual Error Cancellation for Logical Quantum Circuits
authors: Oles Shtanko, Saswata Roy, Shashwat Kumar, Zlatko Minev (Google Quantum AI)
published: 2026-10-08
categories: quant-ph
trigger_words:
  - logical error mitigation
  - virtual error cancellation
  - syndrome records
  - dual decoder
  - coarse-grained sectors
  - sampling overhead
  - homological gap
  - postselection bias
---

# Virtual Error Cancellation (VEC) for Logical Quantum Circuits

## 核心问题
早期容错量子计算受限于不可纠正的残余逻辑错误。标准逻辑误差缓解（logical PEC）需要先验噪声表征、修改电路、巨大采样开销三者中的至少两者。VEC 三样全免：只用已存的 syndrome 记录 + 纯经典后处理，适用于**通用**电路（此前 syndrome 重加权协议限于 Clifford）。

## 方法论（可复用模式）

### 1. 线性重加权估计器与精确条件
```
<O>_vec = (1/N) * sum_i w(s_i) * m_i
无偏条件: E_s[w(s)] = 1                    (trace preservation)
          E_s[w(s) * p_alpha(s)] = 0        (error cancellation, alpha = X,Y,Z logical)
```
因 p_alpha(s) >= 0，w 必须在易错 syndrome 上取负——负权重是数学必然不是技巧。

### 2. 最优 syndrome-resolved 滤波器
```
w*(s) = 1 - pbar^T Sigma^-1 (p(s) - pbar)
C*(w) = E[w^2] = 1 + pbar^T Sigma^-1 pbar   (最小采样开销乘子)
```
逐 syndrome 精确后验 #P-hard → 需要粗粒化。

### 3. 粗粒化下界：K >= M+1 扇区
消除 M 个逻辑 Pauli 通道需 M+1 个线性约束 → 至少 M+1 个扇区；质心须构成包围 pbar 的非退化 M-simplex。

### 4. 双解码器扇区划分（核心创新）
- 实时解码器（MWPM/union-find，微秒级）与离线高复杂度解码器（MPS/最大似然，BSV 收缩 χ=2^d）对每个 shot 的逻辑修正之积 ∈ Pauli group：
  - 一致 → consensus sector S_I（份额 1−O(p_L)）
  - 不一致 → directional disagreement sectors S_Q（4^n−1 个）
- 差分对比矩阵 V = (p_Q1−p_I, …) 在阈值下严格对角占优 → Lévy–Desplanques 可逆 → 闭式权重 `w_I = (1+1^T V^-1 p_I)/q_I > 1`，`w_Q = -(V^-1 p_I)_Q / q_Q < 0`。
- 直觉：用「两个解码器吵架」的 syndrome 空间作误差信号，放大一致 shot、负权重抵消争议 shot 的误差——保留全部数据（对照 postselection 丢弃争议 shot 且留 consensus 误差底线不消）。

### 5. 采样开销谱标度定理（选码/解码器指南）
```
C_S* - 1 = O( p^((d+1)/2 - Delta W_min) )
```
- **Gapped (ΔW=1)**：解耦 X/Z 解码、repetition code、独立 bit-flip → C*−1 = O(p^{(d−1)/2})（差）
- **Gapless (ΔW=0)**：Y 故障联合解码、gauge/subsystem code、hook 错误 → C*−1 = O(p_L)（最优，η→1）
- 基准：标准 logical PEC η≈4，单解码器 syndrome-aware PEC η=2，VEC 大距离极限 η→1。

### 6. Syndrome 噪声学习（免标定电路）
- 对无标签 syndrome 记录做傅里叶保真度 F_hat(χ) = mean[(−1)^{χ·s}]，attenuation 坐标 b_χ = −ln F。
- **Jensen 偏差修正收缩估计器**：b_hat = −ln F_hat − 0.5·(1−F_hat²)/(T·F_hat²)（−ln 严格凸 → 二阶偏差）。
- 规范简并 + 样本复杂度 → 用对称群 G_sym（格点对称/时间平移/去极化各向同性）做参数绑定 θ = C·θ_tied，正交列 C^T C = diag(|orbit|)。

## 实验结果
Rotated surface code d=7（49 数据量子比特），Stim + PyMatching（实时）+ BSV-MPS（离线，χ=128）。d=7, p=0.05：对角转移 P_I,I≈1.00, P_X,X≈P_Z,Z≈0.86, P_Y,Y≈0.78；最优权重 w_I≈1.01, w_X=w_Z≈−0.42, w_Y≈−4e−2。残余误差随样本数下降，比解码后逻辑错误率抑制 **>3 个数量级**，比离线 postselection 好 >2 个数量级。对噪声误表征稳健（尺度不变性：全局乘性 miscalibration 不改变最优权重）。

## 使用要点
1. VEC 与 postselection 的本质区别：postselection 有系统偏差（丢掉 consensus 误差底线），VEC 无偏但方差增大 C(w)。
2. gapless regime 才是 VEC 甜点；解耦 CSS 解码的 gapped 码开销标度差一个 p 因子。
3. 扇区概率 share O(p_L) → 争议 shot 稀少，负权重的方差代价有限。
4. 时间漂移：粗粒化（4 扇区 vs 全 syndrome）降低对漂移与后验估计波动的敏感度。

## 相关技能
- real-time-qec-system-stack — 实时 QEC 系统栈（VEC 是其后处理延伸）
- sparse-mamba-qec-decoder — 解码器工程
- mp-decoder-fpga-qec — FPGA 解码器实现
