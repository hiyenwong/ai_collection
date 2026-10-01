---
name: compositional-invariance-lebesgue
category: systems-engineering
description: Network safety verification via local if-and-only-if checks.
trigger_words: forward invariance, compositional safety, interconnected systems, assume-guarantee contracts, tangent cone, contingent cone, sleekness, networked control systems, DC microgrid safety, scalable safety verification, cyber-physical systems safety certificate
---

# Compositional Invariance via Tangential Lebesgue-Density

Source: Dekkaki, Belamfedel Alaoui, Reynaud, Maghenem, Iovine, Saoud, arXiv:2609.36539 (UM6P / Grenoble / Paris-Saclay).

## Core Result (Theorem 4.1) — 首个双向组合不变性定理

对连续时间互联系统 Σ = ⟨(Σᵢ), 𝓘⟩（N 个子系统，Cartesian 连接结构），**全局安全 ⟺ 局部安全**：

```
K = ∏ᵢ Kᵢ  对互联系统 Σ 是鲁棒前向不变集
⟺ 每个 Kᵢ 对子系统 Σᵢ 在耦合输入 Wᵢ² = ∏_{j∈N(i)} hⱼ(Kⱼ) 下是鲁棒前向不变集
⟺ 局部切锥包含： fᵢ(xᵢ, Wᵢ¹, Wᵢ²) ⊆ T_Kᵢ(xᵢ)  对所有边界点 xᵢ ∈ ∂Kᵢ
```

**意义**：此前所有 assume-guarantee / 组合安全框架（含 dissipativity 路线）只建立**充分方向**（局部⇒全局）。本文首次证明**充要**：全局不变性必然蕴含局部不变性——全局安全验证可以完全分解为独立局部子检查，**局部子检查通过 ⟹ 无需全局验证**。

## Key Innovation: Tangential Lebesgue-Density（切向 Lebesgue 稠密性）

等价性的技术核心。经典结果要求集合 **sleek**（Clarke 切锥 = contingent 锥，即 z ↦ T_K(z) 下半连续）才能保证：

```
∏ᵢ T_Kᵢ(xᵢ) = T_K(x)   （个体切锥之积 = 积集合的切锥）
```

Sleekness 太强。新条件：

**定义**：K 在 x ∈ ∂K 处切向 Lebesgue-稠密，若对所有 v ∈ T_K(x) 和 ε>0，可行时间集
```
S_K(x,v,ε) = { t>0 : ∃w, ‖w−v‖<ε, x+tw ∈ K }
```
满足 λ(S_K(x,v,ε) ∩ (0,r))/r → 1（当 r→0），即**近切向方向的有效时间占据零附近的几乎整个区间**。

**层级关系**：sleek ⟹ tangentially Lebesgue-dense；**逆命题为假**（反例：K = {y≥0} ∪ {x=0, y≤0} 的原点处稠密但不 sleek——T_K 非凸）。**凸集 ⟹ sleek ⟹ 稠密**（实用判据：区间/盒子约束自动满足）。

稠密性足以同步多个局部序列为单一全局序列，从而建立 ∏T_Kᵢ ⊆ T_K——反向包含平凡成立，二者合成等式。

## Verification Recipe（可复用流程）

1. **建模**：将每个子系统表示为 Σᵢ = (Xᵢ, Wᵢ¹, Wᵢ², Yᵢ, fᵢ, hᵢ)——区分外部扰动 w¹（环境/未建模）与内部耦合输入 w²（邻居输出，由连接结构内生决定）
2. **正则性**（Assumption 2.2）：fᵢ Lipschitz 集值映射、紧值、Xᵢ×Wᵢ¹×Wᵢ² ⊂ int dom(fᵢ)、hᵢ 连续——标准微分包含条件，互联后自动继承（Lemma 2.5）
3. **局部集**：Kᵢ 闭集且切向 Lebesgue-稠密（凸集/区间自动满足）
4. **局部检查**：对每个 i 和每个边界点 xᵢ ∈ ∂Kᵢ，验证 fᵢ(xᵢ, Wᵢ¹, Wᵢ²) ⊆ T_Kᵢ(xᵢ)，其中耦合集 Wᵢ² = ∏_{j∈N(i)} hⱼ(Kⱼ) 只依赖**直接邻居的安全集投影**
5. **结论**：所有局部检查通过 ⟺ 全局 K 不变，无需检查全局边界（其维度随 N 指数增长）

### 复杂度
- **区间型 Kᵢ（如电压带）**：每子系统 2 个标量不等式（上界处导数≤0，下界处导数≥0），总计 **2N 个标量检查，与网络拓扑无关**，复杂度 O(N)
- 对比集中式：条件需在 R^n（n=Σnᵢ）中不可数无穷边界点集上验证——无有限程序

## Case Study: 100-DGU 直流微电网
- 模型：Buck 变换器 + LC 滤波 + droop 一次控制，准稳态线路近似后每个 DGU 退化为**标量一阶系统**：
  ```
  Cᵢ V̇ᵢ = −(Vᵢ−V_nom)/Rᵢ_d + I_nom − I_L,i − Σ_{j}(Vᵢ−Vⱼ)/R_ij
  ```
- 安全带：Kᵢ = [47.2, 48.6] V（±1.5% 于 48V 标称）
- 拓扑：N=100，k-最近邻环（k=6，左右各3）——稠密耦合考验证书鲁棒性
- 负载电流 Wᵢ¹ = [0,12] A（共模慢阶跃 + 个体偏移 + 5% 噪声）
- 结果：**200 个标量不等式**完成全网安全证书；仿真确认 100 条电压轨迹全程滞留带内

## When to Use / When NOT
**适用**：
- 大规模网络化 CPS（微电网、多机编队、交通网）的安全证书，集中式验证维度爆炸
- 需要**必要条件**（诊断能力）：某局部检查失败 ⟹ 全局必不安全，可定位故障子系统（充分性-only 框架无此诊断）
- Cartesian 积安全集 + Lipschitz 动力学的标准设定

**限制**：
- 安全集必须是 Cartesian 积结构（非积耦合约束如 Σ|Vᵢ−Vⱼ|≤ε 不直接适用）
- 需要 Kᵢ 切向 Lebesgue-稠密（凸集免费；一般闭集需验证或反例排除）
- 耦合集 Wᵢ² = ∏hⱼ(Kⱼ) 可能保守（邻居取整个安全集而非实际轨迹范围）
