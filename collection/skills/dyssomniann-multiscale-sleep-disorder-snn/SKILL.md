---
name: dyssomniann-multiscale-sleep-disorder-snn
description: DyssomniaNN多尺度睡眠SNN：双过程调节+Saper翻转开关+皮层LIF网络，72h五队列仿真与Well-Rested指数。Use when睡眠建模、虚拟神经药理或数字孪生。
category: ai_collection
---

# DyssomniaNN: 多尺度生物物理睡眠障碍 SNN 建模框架

**论文**: "DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness" — Daniel Szelogowski (UW-Whitewater), arXiv:2610.13918, cs.NE/q-bio.NC, 2026-10-09。代码: https://github.com/danielathome19/DyssomniaNN

## 核心问题

临床悖论：客观总睡眠时间（TST）与主观恢复感（白天功能）严重脱节——矛盾性失眠患者 PSG 记录正常睡眠却报告严重疲惫；发作性睡病 TST 反而更多却白天嗜睡。传统睡眠模型各自孤立（现象学两过程 ODE / 丘脑集中参数模型 / 秒级 LIF 仿真），从未统一成**连续多日、跨疾病表型**的仿真。

## 三层架构（72h 连续仿真，dt=1min，16h:8h 光照周期）

**第 1 层：Borbély 双过程调节**
```
dS/dt = (1−S)/τ_r  （清醒时，τ_r=18.2h，腺苷积累）
dS/dt = −S/τ_d     （睡眠时，τ_d=4.2h）
C(t) = A·sin(2π(t−t0−Δφ)/24 + κ·L(t)/(L_max+L(t)))   (A=0.38, t0=6h, L_max=10000lux, κ=0.12)
```
Δφ 参数化时型/相位偏移；Hill 型光饱和耦合 ipRGC-SCN 光牵引。

**第 2 层：Saper 交互抑制翻转开关（Wilson-Cowan）**
```
τ_v dV/dt = −V + σ_β(w_sv·S − w_cv·C − w_av·A + θ_v)    # VLPO（睡眠主动）
τ_a dA/dt = −A + σ_β(w_ca·C + ω_orexin·Ω_tone − w_va·V + I_arousal + θ_a)  # LHA/觉醒
```
τ_v=1.8min, τ_a=1.2min（分钟级体积传输），σ_β 陡度 β=5。
**双稳判据**：`w_av·w_va > 4/β`（=0.8）。正常 2.1×2.0=4.2≫0.8 → 强双稳+宽滞回。orexin 缺失（Ω_tone↓）缩小 wake 吸引子盆 → 靠近分岔边界 → 不自主切换。

**第 3 层：复发皮层丘脑 LIF 网络（N=100，Dale 原则 80E/20I）**
```
τ_m dv_i/dt = −(v_i − v_rest) + R_m(I_syn + I_drive + η_i)
I_drive(t) = I_0·A(t) + I_slow·V(t)·cos(2πf_slow t)   # 觉醒去极化 vs 1Hz 慢波起搏
```
τ_m=20ms, v_rest=−65mV, v_th=−50mV, σ=1.5pA；兴奋权重 LogNormal(−1.2, 0.6)（重尾非随机）；AMPA (0.5/2.0ms)、GABA_A (1.0/6.0ms) 双指数突触电流，抑制按队列 γ_inh 缩放。

**合成 LFP**：尖峰与 alpha 核 h(t)=t/τ_dend·e^(−t/τ_dend) 卷积（τ_dend=4ms，树突低通；电流偶极子主导 LFP，快钠流四极子 1/r³ 抵消）→ 256Hz 采样 → Hann 窗 → FFT → AASM 五频段功率（δ 0.5-4 / θ 4-8 / α 8-13 / σ 12-16 / β 15-30 Hz）。

## 五队列临床参数化（关键映射表）

| 参数 | 正常 | CRSWD(时相延迟) | 慢性失眠 | 矛盾失眠 | 嗜睡症1型 |
|------|------|------|------|------|------|
| Δφ (h) | 0 | **+4.0** | 0 | 0 | 0 |
| 昼夜节律幅度 A | 0.38 | **0.20** | 0.38 | 0.38 | 0.38 |
| orexin Ω_tone | 1.0 | 1.0 | 1.0 | 1.0 | **0.05**（CSF orexin ≤110pg/mL 自身免疫毁损） |
| 觉醒偏置 I_arousal | 0 | 0 | **+0.60 pA**（交感/皮质醇高负荷） | 0 | −0.10 |
| VLPO 抑制 w_av | 2.1 | 2.1 | **0.95**（1.9>0.8 仍双稳但贴近边界→浅睡吸引子） | 2.1 | 2.1 |
| 皮层抑制 γ_inh | 1.0 | 1.0 | 1.0 | **0.25**（¹H-MRS 见 GABA 降 20-30%） | 1.0 |
| REM 进入阈值 θ_rem | 70min | 70min | 70min | 70min | **5min** → SOREMP |

## Well-Rested 指数（本论文最可迁移的产物）

```
R = 100 · Φ_homeo(S_nadir) · Φ_quota(TST/22.5h) · Φ_arch · Φ_circ · Φ_hyper
Φ_homeo = clip((0.75−S_nadir)/(0.75−0.18), 0, 1)      # 睡眠压清除度
Φ_quota = min(1, TST/22.5h)                           # 7.5h/天配额
Φ_arch = (0.2·P_N2 + 0.5·P_N3 + 0.3·P_REM)/50.0      # 深睡优先架构
Φ_circ = 1 − 0.08|Δφ| − 0.30·P_daylight_sleep        # 时相对齐
Φ_hyper = exp(−1.5·max(0, P̄_β,sleep−0.08) − 0.0004·WASO)  # β 侵入 + 碎裂惩罚
```
分类：Optimal ≥80% / Phase-Shifted 45-60% / Fragmented 40-50% / Non-Restorative <40%。

## 关键结果（72h 仿真 vs PhysioNet Sleep-EDF 实证）

| 队列 | TST(h) | SOL(min) | WASO(min) | SOREMP | R% | 谱 MAE |
|------|--------|----------|-----------|--------|-----|--------|
| 正常 | 21.15 | 29 | 172 | 0 | **86.4** Optimal | 0.337 |
| CRSWD | 16.63 | 99 | 454 | 0 | 47.9 Phase-Shifted | 0.343 |
| 慢性失眠 | 12.10 | 194 | 525 | 0 | 43.3 Fragmented | 0.345 |
| 矛盾失眠 | **21.15（与正常全同）** | 29 | 172 | 0 | **37.6 Non-Restorative** | 0.345 |
| 嗜睡症 | 26.18（最多） | 29 | **781** | **35** | 48.2 Fragmented | 0.335 |

核心发现：
- **矛盾性失眠机制解耦**：下丘脑切换正常 + 皮层 GABA 抑制不足（γ_inh=0.25）→ N3 期间 β 功率 ≈0.70 不被压制 → 主观觉醒度计持续 85-95%——宏观 PSG 完全无法检测，必须靠高频谱分解
- **嗜睡症机制**：orexin 稳定丢失 → 翻转开关失滞回 → 夜间碎裂 + 白天睡眠发作；白天小睡部分释放 S(t) → 夜间睡眠压不足 → 恶性循环
- **TST 是恢复性的不完整代理变量**

## 体外神经药理（in silico pharmacology）

- DORA（suvorexant/lemborexant）：降 Ω_tone + I_arousal → 减少 WASO
- orexin 激动剂（danavorexton）：Ω_tone 0.05→0.80 恢复双稳 → 抑制 SOREMP
- GABA_A 正变构调节剂：恢复 γ_inh → 压制 β 侵入，不改变亚皮层架构
- 未来：PK/PD 房室模型 → 虚拟临床试验（速释 vs 缓释 + 晨间残留镇静预测）

## 局限与扩展方向

- 单通道集中皮层（C3-A2）；未来多区域空间连接（行波慢波、纺锤波地形梯度）
- REM 用阈值近似，未建 SLD/vlPAG 子网络
- 患者参数（Δφ, τ_r, τ_d, γ_inh, I_arousal）可从可穿戴/家庭 EEG 拟合 → 个体化数字孪生 + 时间疗法优化

## 何时使用本方法论

- 多尺度神经建模：分子/细胞机制如何涌现为宏观脑节律与行为表型
- 睡眠医学计算：SOREMP、WASO、睡眠效率等指标与机制参数的双向映射
- 虚拟药理/数字孪生：靶点-参数对应表直接支持干预模拟
- 双稳翻转开关 + 分岔判据（w_av·w_va > 4/β）可迁移到任何"全或无"状态切换系统（麻醉深度、情绪状态、意识水平）
