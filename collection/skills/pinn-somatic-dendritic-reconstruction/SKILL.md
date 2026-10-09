---
name: pinn-somatic-dendritic-reconstruction
description: Soma voltage from dendritic-only recordings via HH PINN.
metadata:
  arxiv_id: "2609.25436"
  published: "2026-09-21"
  authors: "Abdeltif Oujbara, Benjamin Ambrosio, M. A. Aziz-Alaoui"
  tags: [pinn, hodgkin-huxley, two-compartment, dendritic-recording, inverse-problem, conductance-estimation]
---

# PINN Somatic Reconstruction from Dendritic Recordings

**Source**: arXiv:2609.25436 (2026-09-21) | Oujbara, Ambrosio, Aziz-Alaoui (Le Havre Normandie)

## 核心问题与贡献

从**仅树突记录**重建隐藏的胞体膜电位 Vs(t)——部分可观测逆问题。双室 Hodgkin-Huxley 模型（BLA 锥体神经元, Pinsky-Rinzel 型简化），弱耦合 gc=0.1 mS/cm² 下树突信号是胞体活动的强低通滤波衰减版。PINN 联合重建完整状态轨迹 + 估计 4 个胞体最大电导 ḡNa,s / ḡDR,s / ḡM,s / ḡCa,s。

**关键结论（sparse somatic anchoring 消融）**:

| Somatic supervision | RMSE(Vs) | Spike recovery | gNa/gDR error |
|---|---|---|---|
| 0% (dendrite-only) | 10–14 mV | ALL missed | 57% / 40% |
| 1% | 6.6–9.7 mV | ALL recovered | 0.08% / 0.94% |
| 5% | ~1.8–2.4 mV | full waveform | 0.06% / 0.08% |

**1% somatic samples 已足以选定 spiking branch**；5% 使 RMSE≈2 mV 且快速电导误差 <0.1%。

## 方法论细节

### 1. 双室模型（关键结构）
- 电荷守恒方程对 soma/dendrite 各一，轴向耦合项 (gc/p)(Vk − Vk')；ps+pd=1 归一化，γ = gc(1/ps+1/pd) = 4gc
- Soma 电流: INa, IDR, ICa, IM（6 gating vars）；Dendrite 额外: IH, ID, IC, IsAHP（11 gating vars）
- 双钙池: fast (f1=0.7, τ1=1ms) 驱动 IC；slow (f2=0.024, τ2=569ms) 驱动 IsAHP
- **Practical synchronization bound (Prop 3.1)**: |e(t)| ≤ |e(0)|e^(−(γ+gmin,d)t/Cm) + Btot/(γ+gmin,d)，mismatch 球半径 O(1/gc)。冻结门控电导项是耗散的（每电流 ΠX(x)≥0 ⇒ slope ≤ −ḡL,d），无需 γ>Lvolt 的经典条件

### 2. PINN 架构
- 输入: 归一化时间 tnorm∈[−1,1] + **Fourier features** (Nf=16, Bk=2πk) 对抗 spectral bias 尖峰 + 标准化注入电流 + protocol embedding er（单网络表示 4 种刺激）
- 8层 MLP × 256 units, SiLU；输出变换: V = Vc + Va·tanh(u/Va)（Vc=−20, Va=80 mV）; gating → sigmoid∈(0,1); [Ca] = rest + 0.01·softplus; **ḡj = softplus(ρj)** 保证正电导
- 自动微分计算 ODE 残差 r = dy/dt − f(y, I; θg)

### 3. 损失函数
```
L_total = λd·L_Vd(dendritic fidelity, dense) + λs·L_sparse_somatic(masked)
        + λphys·L_phys(Huber δ=25, per-component weights, warm-up ramp 10k steps)
        + λIC·L_IC(初始条件正则: Vd/gates/Ca/soma 先验)
λd=1, λs=1.5, λIC=0.2; Adam lr=1e-4, batch=2048, 30k steps
```
- Huber 惩罚避免 spike onset 的大残差主导；物理权重渐进激活避免 stiff residual 毁掉早期优化

### 4. 四种刺激协议（丰富训练信号）
constant step (Iamp=15) / ramp (20) / rectified sinusoidal (7) / pulse train (10)，窗口 [100,400]ms，dendrite-only 注入

## 核心洞见：可辨识性层级

- **快电导 (gNa, gDR)**: 每个尖峰的直接签名 → 强可辨识（<0.1% error, CV 0.03–0.8%）
- **慢电导 (gM, gCa)**: 小 2–3 个数量级 + 慢时间尺度（τp~几十ms, τu=569ms > 500ms 窗口）→ **practically unidentifiable**（14–18% error, CV 9.6–20%）
- 0% 失败模式不是随机失败: 收敛到**低兴奋性解**（gNa↓57%, gM→0.005, gCa↑572%）——参数与错误轨迹共适应，loss 在该方向近乎平坦
- 判别指标: RMSE/MAE 比值（1%时 3.5–4.1 = 误差集中在少数尖峰点；5%时 2.0–2.3）

## PINN vs UKF（同模型同数据对比）

| | PINN (global) | UKF (sequential) |
|---|---|---|
| RMSE(Vs) | 1.79–2.37 mV | 3.29–5.10 mV (PINN低1.4–2.8×) |
| offset | 无系统性偏移 | 峰间 −4~5 mV 系统性负偏 |
| spike shape | 宽度/复极正确 | 尖峰偏窄（早起、快复极、AHP 过冲）|
| gNa err | 0.06% | 34.67% |
| gM err | 17.8% | 129.75% |

**机制**: UKF 在两个 somatic anchor 之间只能靠弱信息树突观测+模型预测，参数作为常状态局部调整，Gaussian 近似被尖峰 upstroke 拉伸 → 有偏。PINN 全窗口同时施加方程，每个尖峰都约束同一组全局参数 → 无偏。**fixed-interval smoother 可部分恢复但未比较**。教训: 全局约束 vs 顺序同化是差异来源，非生物物理。

## 鲁棒性

- 噪声 σ=0–2 mV: RMSE 增幅 (0→0.9 mV) **小于噪声本身**——逆问题不放大噪声（非平凡性质）
- 8 seeds: RMSE 1.83±0.19 mV（CV 10%），gM/gCa 的 seed 间漂移沿 loss 平坦方向（gM 系统性≤truth, gCa 系统性≥truth——慢电流间部分补偿的签名）
- **轨迹本身每次都恢复得一样好**——主输出（隐藏胞体电压）不受慢电导辨识失败影响

## 实现指南

1. **数据配置**: 密集树突 Vd(t) + 已知 Istim,d(t) 必需；**至少 1% somatic samples**（~每 100 步 1 个点），推荐 5%
2. **必须使用 Fourier features** 否则 spectral bias 丢失尖峰
3. **物理权重 warm-up** 是训练成功关键（直接用满权重会被 stiff residual 破坏）
4. **只估计选定电导**（4 个），固定门控动力学——全参数 HH 估计是病态的（Daly et al. 可辨识性分析）
5. 扩展路径: N-compartment 树突树（data fidelity 只施加在被记录区室，物理残差全域）；网络级逆设计（找促进/抑制同步的刺激频率）

## Pitfalls

- ❌ 纯树突-only (0%) 在该损失形式下**失败**——这是损失形式的极限而非树突信息的绝对极限（更强约束/更丰富刺激协议可能突破）
- ❌ Emax ~35–54 mV 在 5% 时仍大——这是亚毫秒尖峰时序误差指标，不是漏检；用 MAE/RMSE 评价轨迹质量
- 慢电导辨识需要: 激发慢电流的协议 / 长于其时间常数的记录 / 额外慢观测量（如细胞内钙）

## 与相关 skill 的关系

- `pinn-neuronal-parameter-estimation` (arXiv:2603.08742): 单室 Morris-Lecar 版本；本 skill 扩展到**多室弱耦合 + 跨区室重建**
- `pinns-biomedical-modeling`: 一般 PINN 生物医学建模模式

## 扩展应用

- 实验场景: 只有 dendritic patch/成像数据时的胞体输出推断
- 疾病模型: 从可观测区室约束不可观测区室的生物物理
- 网络级: 癫痫/Parkinson 病理性节律的逆设计（找临界刺激频率）
