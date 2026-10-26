---
name: chaotic-griffiths-phase-neuron-map-networks
category: ai_collection
description: Use when modeling disorder-induced criticality in neurons.
trigger: 混沌Griffiths相, 淬火无序, 参数异质性, 扩展临界性, 神经元映射网络, Chialvo map, cluster size power law, Lyapunov subextensive scaling, chaotic Griffiths phase, quenched disorder, extended criticality
---

# 混沌Griffiths相：淬火参数无序驱动的神经元网络扩展临界性

**来源**: arXiv:2610.03344 (2026-10-02, Juan Velez-Rojas & M. G. Cosenza)
**一句话**: 拓扑无序不是Griffiths相的必要条件——仅靠**局部神经元参数的淬火无序**即可在全局耦合映射网络中产生混沌Griffiths相；与small-world拓扑无序叠加时临界区间进一步扩展并完全抑制相干态。

## 问题定义

- 传统临界性图像：需要精细调节到孤立临界点 → 生物系统难以维持
- Griffiths相（GP）：淬火无序系统中rare regions保持局部有序 → 在**扩展参数区间**呈现反常弛豫与类临界行为，无需fine-tuning
- **先前共识**: 神经元网络中的GP主要来自结构异质性（模块化、层级、小世界拓扑）
- **本文问题**: 局部动力学异质性（兴奋性/阈值/发放参数的多样性，建模为局部参数淬火无序）单独能否产生混沌Griffiths相？

## 模型

**Chialvo 2D map-based neuron**（局部动力学）:
```
x_{t+1} = f(x,y) = x²exp(y − x) + k     # 激活电位（电压状态）
y_{t+1} = g(x,y) = a·y − b·x + c        # 恢复变量（离子通道失活样）
```
固定 a=0.89, b=0.18, c=0.28（混沌发放）；k = 外部刺激参数 → **异质性载体**

**全局耦合网络**:
```
x_{t+1}(i) = (1−ε)·f(x_t(i), y_t(i), k(i)) + ε·h_t
h_t = (1/N) Σ_j f(x_t(j), y_t(j), k(j))     # 平均场
y_{t+1}(i) = g(x_t(i), y_t(i))
```
淬火无序: k(i) ~ U[0.026, 0.03]，与拓扑无关（全局耦合 = 无拓扑无序的对照隔离）

**异质性幅度控制**:
```
k(i) = (k1+k2)/2 + A·[ξ(i) − 1/2]·(k2−k1)     # ξ ~ U[0,1]
```
A=0 → 完全同质；A=1 → 最大异质。

**Small-world扩展**（Watts-Strogatz, rewiring r=0.04, n̄=40）:
```
x_{t+1}(i) = (1−ε)f(...) + (ε/n(i)) Σ_j A_ij·f(...)
```

## 检测方法论（可复用的判据管线）

**1. 瞬时cluster识别（single-linkage）**:
- 每步按激活状态排序 x(1) ≤ … ≤ x(N)
- 相邻链接判据: x(j+1) − x(j) ≤ δ_N → maximal consecutive sequence = cluster
- **阈值δ_N标定协议**: 找admissible区间——使代表性**去同步**轨迹 p_t < 0.10（≥95%时间）且**相干**轨迹 p_t > 0.90（≥95%时间）；取区间上界。GP轨迹本身不参与标定。δ随N缩小（例: δ_1000=2.2e−5, δ_16000=1.41e−6）

**2. 三相判据**:
| 相 | p_t | σ(p) = p_t的渐近标准差 |
|----|-----|------------------------|
| D 去同步 | p̄→0 | < σ_min |
| **G 混沌Griffiths相** | 在[0,1]大幅涨落 | **> σ_min = 0.12** |
| S 相干 | p̄=1 | = 0 |

**3. 类临界性签名**:
- cluster尺寸分布幂律 P(s) ~ s^(−α)，α随ε单调变化（MLE估计，s∈[10,1000]）
- 正Lyapunov指数数目反常标度 N+ ~ N^β，β≈0（规则CML为线性extensive；Shinoda-Kaneko判据）

## 核心结果

**1. 参数无序单独充分**（全局耦合，N=200~16000）:
- ε扫描: D (ε=0.028) → **G (ε=0.14, 间歇性cluster形成/瓦解)** → S (ε=0.7)
- A=0（同质）: **无混沌GP**；A→1: ε区间单调加宽
- 幂律 α ≈ 2.2 量级，ε ∈ [0.146, 0.411]
- N+ 反常标度在纯参数无序下同样出现 → 拓扑无序非必要

**2. 与拓扑无序的协同**（small-world, N=10000）:
- 混沌GP扩展到 ε ∈ [0.4, 1.0]，**相干态被完全抑制**
- 幂律 α ∈ [2.15, 2.30]

**3. 机理图像**: 间歇性相干-去同步过程类似globally coupled maps中的chaotic itinerancy，但存在于**扩展参数区域**而非孤立参数点。

## 生物学意义

真实神经元在兴奋性、发放阈值等动力学属性上本质多样 → 内在动力学异质性是**独立于脑结构连接**的扩展临界性机制。这为"大脑为何不需要fine-tuning到临界点"提供了第二解释路径：结构异质性与动力学异质性**互补**地维持扩展临界区间（关联动态范围、信息处理能力、健康指标）。

## 实现指南（复现脚本骨架）

```python
# 1. Chialvo map + quenched k
k = np.random.uniform(0.026, 0.03, N)          # or A-scaled Eq.(11)
def step(x, y, eps):
    h = np.mean(x**2 * np.exp(y - x) + k)
    x_new = (1-eps) * (x**2 * np.exp(y - x) + k) + eps * h
    y_new = 0.89*y - 0.18*x + 0.28
    return x_new, y_new
# 2. 丢弃 5e4 transients；每步排序 + single-linkage(δ_N) 求 p_t
# 3. σ(p) over T=长序列 → >0.12 判 G；P(s) 幂律拟合；N+ 随 N 标度
```

## 与既有技能的关系
- `griffiths-phase-brain-criticality`：结构网络模块化诱导的GP（此技能补充**动力学**无序机制，二者互补）
- `neutral-theory-neural-dynamics`：无标度雪崩的中性漂移解释（替代临界性假设的另一路径）
- `chaos-programming-neural-circuits`、`sequential-chaotic-oscillations-ei-networks`
