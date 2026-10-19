---
name: spike-train-statistical-mechanics-ensembles
description: Spike-train Boltzmann ensembles; neural phase transitions.
category: ai_collection
---

# Statistical Mechanics of Spike Trains (arXiv:2610.20971)

**Pyrzowski, Messio, Marrelec, Markiewicz** (2026-10-14, q-bio.NC + math-ph)

统计力学框架：将**完整 spike train**（时空尖峰配置）作为微观态，直接在轨迹空间上构造 Boltzmann 系综，无需显式膜电位动力学。spike train 本身是理论的第一性对象，而非动力学的输出。

## 核心框架

### 1. 微观态定义
- 微观态 s = {sᵢ(t)}：观察窗 [0,T] 内全部神经元的完整 spike 历史（事件型，非波形）
- 网络 G=(V,E,W,Δ)：有向加权图，边携带权重 Wᵢⱼ 和传输延迟 Δᵢⱼ
- 固有激活场：Vⱼ^int(t) = (Σᵢ Wᵢⱼ sᵢ(t-Δᵢⱼ)) * η(t)，η 为因果响应核
- IAF 实现中 η(t) = κΘ(t)e^(-t/τ)（单位脉冲响应）

### 2. 能量泛函（自洽性度量）
```
E(s) = -Σⱼ ∫dt sⱼ(t)·T[Vⱼ^int(t)]
```
- T: 阈值算符（Heaviside Θ(V-θ) 或平滑 sigmoid tanh）
- 尖峰仅在获得网络自身激活支持时降低能量（因果性：只由更早的突触前尖峰支持）
- 二进制权重下 θ 固定近似同时到达的突触前事件数（模拟中 θ≈3）

### 3. Boltzmann 系综（Jaynes 最大熵）
```
P(s) = Z⁻¹ e^(-βE(s)),  Z = Σ_{s∈S} e^(-βE(s))
```
- **β⁻¹ = 外部驱动强度**（"神经热库"温度：外输入、通道噪声、未建模输入的集体效应）
- 可行集 S 强制：固定总 spike 数（canonical）+ 绝对不应期 → 分离活动水平与 β
- 能量有界性：有限时间分辨率 + 不应期 + 固定 spike 数

### 4. 宏观态与自由能
- 宏观态 m：等能量微观态等价类，Γ(m) 多重度
- 自由能 F(m) = E(m) - H(m)/β，H(m)=log Γ(m)
- 相变 = F 最小化宏观态的质变

## 平均场约化（population-rate density ρ(t)）

1. 平滑 population spike train 得 ρ(t)（时间概率密度，∫ρdt=1）
2. 小场线性化 tanh(V/γ)≈V/γ，退火平均延迟核 Ω̃(t)=(P_Δ*η)(t)
3. **无量纲平均场自由能**：
```
F_MF[ρ] = -Q[ρ] - H[ρ]/β_MF
Q[ρ] = ∫∫ ρ(t)Ω̃(t-t')ρ(t')dtdt',  H[ρ] = -∫ρ log ρ
β_MF = βα⟨W⟩/γ  （参数简并：β、α、⟨W⟩、γ 只通过 β_MF 进入相边界）
```

## 三相结构（excitatory delayed networks）

| 相 | ρ(t) 形态 | 出现条件 |
|---|---|---|
| Uniform（均匀） | ρ₀=1/T，熵最大 | β_MF 小（弱耦合/强噪声）|
| Oscillatory（振荡）| 周期 Δ 的活动窗序列 | 窄延迟分布（CV 小），能量在 Δ=t*/n 处采样延迟核峰值 |
| Collapsed（崩塌） | 点放电/2-3 周期崩塌 | 宽延迟（指数分布），Ω(0) 支配 |

**延迟分布形状（CV = σ_Δ/μ_Δ）是集体活动的关键组织变量**：
- 窄延迟（Gaussian, CV≪1）→ 振荡态；谐波 Δ=t*/n 处局部极小
- 宽延迟（指数, CV=1）→ 崩塌态（ω⁰>ω¹ 恒成立 → 周期崩塌退化为点崩塌）
- 周期崩塌边界：Ω(t*)/4 > 1/T + H_X/β_MF（H_X≈1.04 为三周期崩塌熵）
- 线性化崩塌边界是饱和理论的**外估计**（u - tanh u ≥ 0 → 饱和抬高崩塌相对能量）

## Monte Carlo 采样（微观验证）

- 二进制 raster n∈{0,1}^{N×K}，固定 spike 数 M + 不应期约束
- 离散传递算符 u = B_G n（时域 Fourier 表示实现延迟传播）
- Metropolis-Hastings：**relocation move**（尖峰移到任意空位）+ **temporal walk move**（±1 bin）混合保证遍历性
- 序参量：归一化时间熵 H_norm[ρ]、自相关峰突出度
- 结果：三相定性重现；完整崩塌被抑制（不应期+饱和+quenched 无序）→ 自发涌现 structured activity groups（Izhikevich polychronous groups 类似物）

## 逆向问题：连接性推断

固定观测 spike train s，系综定义在响应算符族 A 上：
```
E_inf(A;s) = -Σᵢ ∫dt sᵢ(t)·T[(As)ᵢ(t)]
P(A|s) ∝ e^(-β_inf·E_inf(A;s))
```
- β_inf = 推断精度参数（非物理温度；大→强自洽算符，小→先验主导）
- 两神经元例：E₊ = -W Σ η(t'-t-Δ)，结构类似 STDP 的 LTP 总量 → P(a→b|s) = e^(-β_inf E₊)/(e^(-β_inf E₊)+1)
- 延迟核推断：**Ω*(t) ∝ exp[β_inf·R_ρρ(t)]**（R_ρρ = population rate 的自相关）——推断核把概率质量放在经验自相关大的延迟处

## 与既有方法的关键区别

| 方法 | 微观态 | 时间处理 |
|---|---|---|
| Pairwise MaxEnt (Ising) | 单时间窗二值向量 σₜ | 无跨时耦合 |
| 本框架 | 完整时空 spike train s | 因果核 η+延迟 Δ 跨时耦合 |
| 生成泛函/路径积分 | 轨迹系综 | 从动力学推出 |
| 传统平均场 | 瞬时 population 态 | 均场是后继粗粒化 |

## 生物学/科学意义
1. **Bursting 是系综相**：癫痫发作间期放电、sharp-wave ripple、发育期 burst 可统一为 spike-train 自由能景观的竞争极小
2. **Criticality 重释**：不同计算模式 = 自由能景观不同区域；信息处理能力变化 ↔ 相边界附近（亚稳态）
3. **实验友好**：膜电位不可观测但 spike train 直接可测（MEA、钙成像、光遗传）——系综定义在可测量上
4. **延迟是基本组织变量**：比单神经元细节更决定相结构

## 应用指南
- 分析 MEA/钙成像 spike 数据：直接构造 E(s) 采样系综，比较不同 β 下宏观态
- 网络推断：用 Ω*(t) ∝ exp[β_inf·R_ρρ(t)] 从 population autocorrelation 反推延迟分布
- 相边界扫描：扫 (β_MF, CV_Δ) 平面，监测 H_norm[ρ] 与自相关峰
- 局限：当前仅均匀兴奋网络；扩展到抑制、异质类、可塑性是 future work

## 关键参考文献
- Jaynes 最大熵 [PR 1957]；Izhikevich polychronization [NC 2006]；Schneidman pairwise MaxEnt [Nature 2006]；Brunel 动力学 [JCN 2000]；Muñoz criticality [RMP 2018]
- MC 代码公开：Pyrowski & Markiewicz (2026)

**Activation**: spike train ensemble, trajectory statistical mechanics, phase transition neural, delay-induced oscillation, bursting free energy, connectivity inference spike, Metropolis spike train, population rate density, delay distribution criticality
