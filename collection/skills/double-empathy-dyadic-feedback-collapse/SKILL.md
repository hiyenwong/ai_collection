---
name: double-empathy-dyadic-feedback-collapse
description: "Use when modeling dyadic social interaction breakdown or channel-preference mismatch. 反馈环共情崩溃模型。"
category: neuroscience
metadata:
  arxiv_id: "2602.02562"
  published: "2026-01-30 (v2 2026-10-01, physics.soc-ph)"
  authors: "Enrique Calderoli, Tiago Figueiredo, Maria Cristina Varriale, Flávio Kapczinski"
  source: "UFRGS / ICEP / McMaster — arXiv q-bio.NC + physics.soc-ph cross-list"
  tags: [double-empathy-problem, dyadic-social-coupling, feedback-loop, empathy-collapse, jury-stability, loop-gain, separatrix, autism, channel-preference, computational-social-neuroscience, nonlinear-dynamics, falsifiable-predictions]
---

# Double Empathy 问题的反馈环数学模型：共情崩溃的动力学

**arXiv 2602.02562** (v2 2026-10-01) — Calderoli, Figueiredo, Varriale, Kapczinski。首个将 double empathy problem（跨神经类型沟通中断为双向现象，Milton 2012）形式化为**二元社会耦合动力系统**的机制模型：仅靠言语/非言语通道偏好差异即可复现临床上观察到的共情联结崩溃（empathy collapse）。

## 核心问题

传统解读把自闭症社交困难定位在个体内部（缺陷模型）；double empathy 框架主张误解是双向涌现的。但该框架迄今没有机制性数学模型——"沟通兼容性""交互成本""情感共鸣"如何相互作用无人建模。本文给出第一个可证伪的反馈环模型。

## 模型架构（三元函数组）

每个 agent（A = 自闭原型，NT = 神经典型原型）有三个函数，构成"感知缺口 → 防御性上升 → 共情输出下降"正反馈通路：

**1. 状态变量：防御性 D_i**（唯一真实动力学状态）
```
D_i[n+1] = D_i[n](1 − λ_i) + y_i(Δ_i[n+1]; ψ_i)
```
- λ_i ∈ [0,1]：防御性自然衰减（遗忘/情绪调节）
- Δ_i = EE_i − RE_i：共情缺口 = 期望共情 − 登记共情

**2. 感知函数 p_i（通道偏好核心）**
```
RE_i = c_{i,v}·X_{j,v} + c_{i,nv}·X_{j,nv}    (c_v + c_nv = 1)
```
- c_p,A = 0.75：自闭原型言语加权 3× 于非言语（文献支持：literal processing, prosody 差异）
- c_p,NT = 0.50：神经典型均衡感知
- 共情输出空间 [0,100]×[0,100] 二维（言语 × 非言语）

**3. 防御性增量函数 y_i（带饱和线性）**
```
y_i(Δ_i, D_i) = c_y,i·(Δ_i − θ_i)·(1 − D_i/D_sat,i)
```
- θ_i：缺口下限（对轻微拒绝的抑制能力）
- (1 − D/D_sat)：状态依赖增益，防无界增长并制造非平凡不动点

**4. 输出函数 z_i（防御性 → 共情输出）**
```
X_{i,v}  = X_max,i,v  − c_z,i,v·D_i
X_{i,nv} = X_max,i,nv − c_z,i,nv·D_i
ρ_i = c_z,i,v / c_z,i,nv   ← 输出不对称参数（关键新参数）
```
- ρ < 1：防御时言语通道保留（保护性）；ρ > 1：言语先衰减（脆弱性）

## 稳定性分析（Jury 条件 + 环增益）

Jacobian（对角 1−λ_i，非对角为跨 agent 耦合）：
```
L = y'_A·S_{A←NT} · y'_NT·S_{NT←A}      环增益乘积
det(J) = (1−λ_A)(1−λ_NT) − L
```
**崩溃判据（Jury 条件破坏）**：L > (1−λ_A)(1−λ_NT) 时局部失稳。

**中心发现——ρ_A 的双重脆弱性**：
```
L = 0.0072 × (ρ_A + 1) × (1−D_A/100)(1−D_NT/100)
```
1. **更早激活**：反馈环激活阈值 D_A > 6.67/(ρ_A+1) —— ρ=0.5 时需 D_A>4.45，ρ=2.0 时只需 D_A>2.22
2. **更强驱动**：耦合系数 J21 = 0.06×(ρ_A+1) 随 ρ 线性增长，ρ 从 1→2 时 J21 增 50%
3. 两者复合：高 ρ 个体既易触发又强驱动崩溃级联

## 相空间结构（数值结果）

120 组仿真（12 个 ρ_A × 10 个 D_A[0]，200 步）：
- **20/120 崩溃（16.7%），全部在 ρ_A ≥ 1.0**；ρ_A ≤ 0.9 时任何初始条件都稳定
- **双稳态 + separatrix**：低防御不动点（D*≈0，特征值 0.98 渐近稳定）与高防御不动点（D*≈80，饱和项平衡大缺口，局部稳定）之间由分水岭分隔；初始条件低于分水岭收敛到健康态，高于则被崩溃吸引子捕获
- **崩溃过程**：最大特征值瞬态超 1（代表性案例 ρ=1.5, D[0]=7 在第 8 步 λ_max=1.105）驱动防御性爆发增长；进入崩溃盆地后特征值回落 <1（第 51 步 0.997）——崩溃态本身稳定，系统不可逆
- **盆地大小 ≈ 反比于环增益**：L 翻倍 ≈ 稳定盆地减半；ρ=0.5 → +35.45% 稳定盆地，ρ=2.0 → −34.33%
- 崩溃轨迹形似 **Kindleberger 螺旋**（大萧条世界贸易崩溃）——跨域同构

## 可证伪预测（4 个实验设计）

模型完全可证伪，作者给出测量协议：
1. **c_p 测量**：因子设计视频（高/低言语 × 高/低非言语共情）+ 回归 RE_rated = c_p·X_v + (1−c_p)·X_nv + ε；预测自闭组平均 c_p 更高。若组间无差异或反向 → 核心假设证伪
2. **ρ 测量**：压力诱导（时间压力/认知负荷/社会评价威胁）下编码言语 vs 非言语共情衰减比 ρ = ΔX_v/X_v / ΔX_nv/X_nv；预测 ρ<1 个体跨初始条件稳定（与诊断无关的调节变量）
3. **D[0] 测量**：状态焦虑量表 + HRV/皮电复合指标，或假反馈操纵（"搭档评价你上一个回答没帮助"）
4. **纵向 dyad 设计三阶段**：参数估计 → 结构化交互任务（操纵 D[0]）→ 稳定/崩溃分类，检验崩溃率是否按预测模式分布

## 应用与延伸

- **诊断无关性**：机制是"表达方式 vs 感知权重"的生产-感知不匹配，神经类型只在群体倾向改变 profile 兼容性时相关——同样适用于跨文化、跨代际沟通断裂
- **干预靶点**：Falsification 4 预测"言语维持训练（降低 ρ）应减少后续崩溃"——可指导社交技能干预从非言语表达训练转向言语表达保持
- **未纳入维度**（作者明确的扩展方向）：交互成本、情感共鸣、动机、互惠 accommodadtion、认知疲劳——本模型只覆盖言语/非言语维度

## 实现要点（复现参数）

```python
λ = 0.02 (both), c_y = 0.10, EE = 96, θ = 1, D_sat = 100
c_p,A = 0.75, c_p,NT = 0.50, c_z,nv = 1.2 (both), ρ_A ∈ {0.5..2.0}
X_v = 100 − ρ·1.2·D,  X_nv = 100 − 1.2·D, cap(Δ−θ) at 98
200 steps; collapse ≡ D > 70; separatrix by binary search on D_A[0]
```
崩溃阈值表：ρ=1.0→5.98, 1.3→5.17, 1.5→4.74, 2.0→3.93（稳定盆地 −13.57%→−34.33%）

## 局限

- 单边参数变化（只扰动 A）——非完整双边交互成本测试；不稳定并非"源于自闭方"
- 参数理论驱动、未经实证校准；二维通道分类（言语/非言语）过于简化
- 未纳入已知的其他共情联结因果变量；原型化 profile 不代表个体异质性

## 相关技能

- [[social-exclusion-brain-dynamics]] — 社会排斥全局脑动力学（功能连接预测行为一致性）
- [[mtt-bench-social-dominance-mice]] — MLLM 预测小鼠社会优势
- [[harmonic-theory-behavior]] — 个体与集体行为谐波理论
- [[kinetic-energy-random-rnn-chaos]] — 随机 RNN 混沌的动能分析
