---
name: cup-cap-topological-neural-network
description: TDL via cup/cap products. Lift node signals to triangles.
category: ai_collection
version: 1.0.0
author: agent
date: 2026-10-05
arxiv: 2610.03169
tags: [topological-deep-learning, simplicial-complex, cup-product, cap-product, higher-order-networks, brain-network, GNN]
activation: topological deep learning, simplicial complex neural network, cup product, cap product, Hodge Laplacian limitation, higher-order interactions, triangle message passing, brain network higher-order, simplicial signal processing, many-body interaction prediction
---

# Cup and Cap Topological Neural Network (CCNN)

Methodology from "Cup and Cap Topological Neural Network" (Niedostatek, Hernandez Caralt, Wang, Baccini, Giambagli, Lió, Bianconi — QMUL/Cambridge/Sapienza/FU Berlin), arXiv:2610.03169, 2026-10-02.

## 核心问题：Hodge-Laplacian TDL 的单层单维限制

现有 Topological Deep Learning（SCN、SCCN、SCCNN、及其它基于 boundary operator ∂ 与 Hodge Laplacian L_p = B_p B_p^T + B_{p+1}^T B_{p+1} 的架构）受制于代数拓扑基本恒等式 **∂² = 0**（边界的边界为零）：

- 边界算子 B_p 只能把 p-链映射到 (p−1)-链（降低一维），余切算子 B_p^T 只能升一维
- **任何单层内，信号无法跨越多于一个维度**——节点 (0-cochain) 信号无法在一个前向传播中"看到"三角形 (2-simplex) 的结构
- 现有架构让节点信号"看到"三角形需要堆叠多层（0→1→2），混合了深度与维度，高阶结构信息传播路径长且稀释

**研究问题**：只用节点特征（0-cochain）做节点级预测，同时利用数据中的多体相互作用（三角形等高阶单纯形）。典型场景：社会网络中三角形/clique 对观点动力学的强偏置（Iacopetti et al. 2019）；脑网络中 edge signals / 三角形团簇对节点动力学的调制（Faskowitz et al. 2020 的脑 edge signal 构造本质上就是 cup product，只是未被指出）。

## 数学方案：cup（升）与 cap（降）积

### Cup product — 跨维提升算子

p-cochain θ̂ ∈ C^p 与 q-cochain φ̂ ∈ C^q 的 cup product 是 (p+q)-cochain：

```
(θ̂ ⌣ φ̂) = Σ_{(i₀,…,i_{p+q})∈Q_{p+q}} θ[i₀,…,i_p] · φ[i_p,…,i_{p+q}] · ê[i₀,…,i_{p+q}]
```

关键性质：**共享一个界面顶点 i_p**——前一个单纯形的终点是后一个的起点，按字典序拼接。

三个最有用的特例：

1. **纯节点提升到边**（脑网络 edge signal 的代数本质）：
   `ξ̂ = θ̂ ⌣ 1̂_{N₁} ⌣ θ̂`，元素 `ξ[rs] = θ[r]·θ[s]`
   （1̂_{N₁} 是所有边上取 1 的 1-cochain）

2. **节点×边 → 边**：`ξ̂ = θ̂ ⌣ φ̂`，元素 `ξ[rs] = θ[r]·φ[rs]`

3. **边×边 → 三角形（跨两维提升）**：`ψ̂ = φ̂ ⌣ ξ̂`，元素 `ψ[rsp] = φ[rs]·ξ[sp]`
   特别地 `ψ̂ = ξ̂ ⌣ (B₁ᵀθ̂)` 可把 0-cochain 直接提升到 2-cochain（单层跨两维）

代数封闭性（Hatcher 2005）：cocycle ⌣ cocycle = cocycle；cocycle ⌣ coboundary = coboundary。cup product 保持上同调类的可分解结构。

### Cap product — 跨维降回算子

p-cochain θ̂ ∈ C^p 与 q-chain φ ∈ C_q（q ≥ p）的 cap product 是 (q−p)-chain：

```
θ̂ ⌢ φ = Σ_{(i₀,…,i_q)∈Q_q} θ[i₀,…,i_p] · φ[i₀,…,i_q] · e[i_p,…,i_q]
```

两个关键特例（α^{(q)} 是由 q 阶邻接张量 a^{(q)} 构造的 q-chain）：

1. **边降回节点**：`η = ξ̂ ⌢ α^{(1)}`，元素 `η[r] = Σ_s ξ[sr]·a^{(1)}_{sr}`
   **退化为图 Laplacian**：若 ξ̂ = B₁ᵀθ̂，则 `η[r] = Σ_s (θ[r]−θ[s])·a[sr] = (L₀θ)[r]`
   → cap product 是 L₀ 作用的严格推广；标准 GNN/SCN 传播是 CCNN 的一个特例

2. **三角形一步降回节点（跨两维）**：`η = ψ̂ ⌢ α^{(2)}`，元素 `η[r] = Σ_{m,s} ψ[msr]·a^{(2)}_{msr}`

## CCNN 架构

输入：0-cochain θ̂⁰ ∈ R^{N₀×n}（节点特征）。内部维护辅助 q-cochain χ̂_q^ℓ（由节点信号逐维 cup 出来）。输出：节点预测。

**主递推（0-cochain，Eq. 23 矩阵形式）**：

```
θ^{ℓ+1} = σ( θ^ℓ·D₁        # 自环/特征变换
            + L₀·θ^ℓ·W₂     # 标准 Laplacian 传播（cap 特例 1 的路径）
            + T(θ^ℓ, χ^ℓ)·W₃ )   # 三角形介导消息传递（cup 升 + cap 降）
```

其中三角形消息项（Eq. 24）：

```
T[r] = Σ_{s<m} a_{rsm} · f(χ_{[sm]}^ℓ) · ( θ[s] + θ[m] − 2·θ[r] )
```

- a_{rsm}：三角形邻接张量（r,s,m 构成 2-simplex 则为 1）
- f = tanh（若 σ=ReLU）或 f = x（若 σ=sigmoid）
- (θ[s]+θ[m]−2θ[r])：r 相对边 {s,m} 的"位置势"——节点向其所在三角形的对面边质心聚拢
- χ_{[sm]}：边 {s,m} 上的学习态，调制该边对 r 的影响力

**辅助 1-cochain 两个变体**（消融后保留）：

- **CCNN-η**（Eq. 25）：`χ^{ℓ+1} = σ( χ^ℓ·D₄ + |B₁ᵀθ^ℓ|·W₅ + D₆ )`
  用 coboundary 的绝对值——度信息（信号差幅度），与方向无关
- **CCNN-ω**（Eq. 26）：`χ^{ℓ+1} = σ( χ^ℓ·D₄ + (θ^ℓ ⌣ 1̂ ⌣ θ^ℓ)·W₅ + D₆ )`
  用纯 cup product——双线性耦合（信号乘积），保留 θ[s]θ[m] 的乘性交互

初始化：χ^{ℓ=0} = B₁ᵀθ⁰。为参数效率 D₁、D₄ 取对角阵，D₆ 是 bias；f(χ) 假设与单纯形定向无关（置换不变），只需按单一定向存储。

**信息流全景（单层）**：
```
节点 θ --cup--> 边/三角形态 χ (η: |B₁ᵀθ|, ω: θ⌣1⌣θ)
     χ --cup(B₁ᵀθ)--> 三角形耦合 (θ[s]+θ[m]−2θ[r])
          --cap α^{(2)}--> 一步回节点 T
θ^{ℓ+1} = σ(θD₁ + L₀θW₂ + T·W₃)
```

### 实现伪代码（M=2, PyTorch 风格）

```python
class CCNNLayer(nn.Module):
    def __init__(self, F_in, F_out):
        self.D1 = nn.Parameter(torch.diag(torch.rand(F_in, F_out)))  # 或 Linear 对角
        self.W2, self.W3, self.W5 = nn.Linear(F_in, F_out), nn.Linear(F_in, F_out), nn.Linear(F_in, F_out)
        self.D4, self.D6 = ..., ...
    def forward(self, theta, chi, B1, L0, A2):  # A2[a_rsm] sparse
        # A2: [num_tri, 3] 每行 (r, s, m) 三角形顶点
        # triangle message: f(chi[edge sm]) * (theta[s]+theta[m]-2*theta[r])
        msg = f(chi[edge_sm_index]) * (theta[s] + theta[m] - 2 * theta[r])
        T = scatter_sum(msg, index=r, dim_size=N0)   # per-triangle → per-node
        theta_next = relu(theta @ D1 + L0 @ theta @ W2.weight + T @ W3.weight)
        chi_next = relu(chi @ D4 + lift(theta, chi, B1) @ W5.weight + D6)
        return theta_next, chi_next

# CCNN-η lift: |B1ᵀθ| ; CCNN-ω lift: theta[r]*theta[s] per edge
# init: chi = B1ᵀ @ theta_input
```

## 基准结果（TopoBench, Clique Lifting, 5 seeds）

对比 SCN / SCCN / SCCNN（simplicial 基线）与 TopoBench 全域最优基线：

- **8/20 数据集胜过所有 simplicial 架构；13/20 处于全域最优基线 1σ 内**
- 节点级：Pubmed 89.74（超全域最优 89.62）；**Amazon 52.22——SCN/SCCN/SCCNN 全部 OOM，CCNN 正常运行**（三角形项稀疏化收益）；Empire/Minesweeper 上 clique-lifted 图基线占优（说明 cup/cap 并非处处赢）
- 图级：MUTAG 82.55±5.9（超最优 80.43）；NCI1 76.89（超 76.67）；**ZINC 0.55 显著强于所有 simplicial 基线（SCCNN 仅 0.36）**
- Election/Bachelor/Unempl 等 LOW/high-ORDER 数据集上 simplicial 基线反而更强——CCNN 优势集中在"三角形结构真实存在且承载信号"的数据

## 应用到脑网络（与 higher-order brain network 分析的直接接口）

1. **Edge signals 的代数统一**：Faskowitz 2020 构造脑 edge signals（ξ[rs]=θ[r]θ[s]）= cup product 特例 1。任何"从节点活动构造连接边信号"的操作都是 ⌣，可以套用本架构让边信号一步耦合进三角形
2. **三角形团簇 = 功能集成单元**：脑功能连接组的三角形丰富（clique 结构在皮层柱/模块内密集），T(θ,χ) 项精确实现"节点活动受其所在团簇对面边调制"——观点动力学/神经动力学中的 simplicial contagion 假设可直接实例化
3. **只需节点信号**：CCNN 输入仅需 0-cochain（如各 ROI 的 BOLD/峰值率），高阶结构从结构连接组（clique lifting）获得——适合"结构先验 + 节点动态"的脑状态预测任务
4. **与现有 higher-order 方法的互补**：hypergraph 类方法（超边=任意集合）用集合消息传递；CCNN 走代数拓扑路线（定向单纯形 + 界面顶点字典序），能表达超边方法无法表达的"界面共享"结构

## 设计规则（模式提炼）

- **Pattern A — 算子替代扩展**：不要在旧算子上加层，而是换代数积（cup/cap）突破其组合限制；∂²=0 是结构性限制，任何基于 B_p 的修补都逃不掉
- **Pattern B — 非线性乘性耦合**：CCNN-ω 的 θ[s]·θ[m] 是 ReLU GNN 框架外的乘性交互；线性化时退化为消息传递，但学习态 χ 提供逐边可学习的门控
- **Pattern C — 度量势差项**：(θ[s]+θ[m]−2θ[r]) 是 r 相对 {s,m} 中点的外推残差——把"节点受邻域拉扯"写成显式势能项，比纯加权求和更可解释（类似弹簧网络的离散曲率力）
- **Pattern D — 单层跨维往返**：lift（cup 到 2-cochain）+ lower（cap α²）组合让一层完成 node→triangle→node 信息往返；深度 L 不再承担"跨维"职责，只承担表达
- **Pattern E — 定向无关存储**：假设 f(χ) 置换不变，只需存一个定向的单纯形特征——实现上省一半内存，代数上以 χ 的置换等变设计为代价

## Pitfalls

- Clique lifting 在稠密图上三角形数 O(N³)——Amazon 上 simplicial 基线 OOM 的原因；CCNN 侥幸通过但三角形张量必须稀疏存储 + scatter 聚合
- Empire/Minesweeper 等"高维结构是 lifting 伪影"的数据集上，clique-lifted simplicial 架构（含 CCNN）劣于原生图模型——先用三角形密度/结构统计判断数据是否真的有高阶结构再选型
- cap product 退化为 L₀ 需要 ξ̂ = B₁ᵀθ̂（coboundary）；若 χ 是任意学习的 1-cochain，则 T 项不等于任何 Laplacian 作用——不能把 CCNN 简单理解为"加权图 Laplacian"
- 论文 f(χ) 的置换不变假设（不依赖定向）是实现简化而非数学必要；若放弃该假设需为每个定向存特征
- ZINCC 类长程任务上 1σ 内但未必最优——跨维提升是归纳偏置不是免费午餐

## 相关技能

- [[higher-order-brain-networks]] — 单纯复形/拓扑脑网络分析（TopoBench 生态）
- [[hypergraph-flow-matching-connectome-generation]] — 生成式超图连接组（生成侧 vs 本技能判别侧）
- [[brain-higher-order-structures]] — 持续同调视角的高阶脑结构
- [[topological-effective-connectivity-hodge]] — Hodge 分解有效连接（本技能正是其"Laplacian 依赖"的解药）

## 参考文献

- Niedostatek, M., Hernandez Caralt, F., Wang, R., Baccini, F., Giambagli, L., Lió, P., Bianconi, G. (2026). "Cup and Cap Topological Neural Network." arXiv:2610.03169
- Hatcher, A. (2005). *Algebraic Topology*. Cambridge University Press.（cup/cap 积定义）
- Nanda, V. (2021). "Computational Algebraic Topology" lecture notes.
- Faskowitz, J. et al. (2020). Edge-centric network analysis of brain connectomes.（脑 edge signals = cup product 特例）
- Iacopini, I. et al. (2019). Simplicial contagion in higher-order networks.（三角形偏置观点动力学）
- Telyatnikov, O. et al. (2025). TopoBench.（基准框架）
