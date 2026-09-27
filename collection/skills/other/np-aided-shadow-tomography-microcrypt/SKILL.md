---
name: np-aided-shadow-tomography-microcrypt
description: NP-aided shadow tomography no-gos for Microcrypt PRS/PRU.
category: ai_collection
---

# NP-Aided Shadow Tomography: How Not to Build Microcrypt

Source: arXiv:2609.30253 "How Not to Build Microcrypt" (Gulati, Khurana, Tomer; UCSB/UIUC/NTT, 24 Sep 2026).

## When to use

- 设计/评估不依赖单向函数的量子密码候选（PRS、PRU、OWSG、PRI）时，先用本 skill 的 NP-辅助攻击 checklist 排除已被破解的架构。
- 需要 BQP^NP 学习算法（shadow tomography 降 NP）或 CMC 幺正判别攻击时。
- 分析"某 PRS/PRU 候选是否隐含经典单向函数"时。

## 核心结果（三条 no-go 定理）

1. **定理 1.1 / Thm 5.5 + Cor 5.9**: 任意 *computable* 纯态 OWSG 族（给定 key 可经典高效计算任意基矢幅度与相位）在 BQP^NP 下可逆 —— worst-case NP-hardness 被强制。
2. **定理 1.2 / Thm 5.10**: 若族还 *samplable*（可经典高效采样计算基分布），则**隐含经典单向函数**（抗量子求逆）。Hamiltonian Phase States（HPS, Bostanci et al. TQC 2025）与 Morimae–Xagawa IQP group-action OWSG 均落入此类 → 不在 Microcrypt 中。
3. **定理 1.3 / Thm 7.1 (CMC attack)**: 任意 CMC 幺正 U_k = C_{2,k} M_k C_{1,k}（C 为 Clifford，M 为 monomial：置换+相位）可被 BQP^NP 学习并从 Haar 区分 —— 覆盖 C₂PFC₁（首个被证 strong PRU）、CLRFC C₂S_R F S_L C₁、constant-time logical CMC、C₂PC₁。

## 攻击机器 1：NP-Aided Shadow Tomography（态）

**目标**: 给定 |ψ_k⟩^⊗s（key 未知），找 h 使 |ψ_h⟩ 与 |ψ_k⟩ 高保真。

**两阶段流水线**:
1. **幅度量级阶段**: 计算基测量得 X₁..X_s；NP oracle 搜索最大化似然 ∏p_h(X_i) 的 key h₀ → p_{h₀} ≈ p_k（Hellinger 意义下）。计算基丢弃相位，故还需阶段 2。
2. **相位干涉阶段（关键创新）**: 用阶段 1 求得的 h₀ **prepare 自参照** |ψ_{h₀}⁺⟩ = Σ|a_{h₀}(x)||x⟩（uncompute 相位），做 controlled-SWAP test：ancilla 变为 e^{iθ(x)}|0⟩ + e^{iθ(y)}|1⟩ / √2，其中 (x,y)~p×p。测 {±} 与 {±i} 基提取 cos/sin(θ(x)−θ(y))。**q=p 的选择使两支路幅度严格平衡**——对平坦态和尖峰态同样有效（均匀参照 |+⟩^⊗n 会被 S/D 压制，随机 2-design 会破坏可计算性，故自参照是唯一可行解）。
3. NP oracle 对最终样本再做一次最大似然 key 搜索 → 输出近似 key。

**忠实度桥（Thm 5.5）**: 1−|⟨φ|ψ⟩|² ≤ 100(t+g)²，t=H(R_{ψ,q},R_{φ,q})（测量分布 Hellinger），g=H(p,q)。证明链：第三边缘分布 ≈ (p+q)/2 → 边缘不增距 → r≈q → 自参照替换 → Hellinger=qsamples 欧氏距 → 保真下界。

**距离工具**: qsample |P⁺⟩=Σ√P(z)|z⟩; B(P,Q)=⟨P⁺|Q⁺⟩（Bhattacharyya）; H²=2−2B; TV≤H。三角不等式免费继承欧氏范数。

## 攻击机器 2：CMC 幺纯判别（Bell 位移测试）

**算法**:
1. 制备 Bell 态 |β_{a,c}⟩，作用 (U_k⊗U_k)，Bell 测量，记录位移 b = y₁⊕y₂。
2. monomial 核 M_k 满足位移 ∈ R_{π_k}(a) = {π_k(x)⊕π_k(x⊕a)}，|R| ≤ D/2（a≠0 时 x 与 x⊕a 成对给出相同位移）。Haar 下位移近似均匀 → 固定候选集以常数概率 miss。
3. **Clifford 层不影响**: (C⊗C)(I⊗P)|Φ⟩ = (I⊗CPC^T)|Φ⟩，CPC^T 仍是 Pauli → Bell 标签双射重排，给定候选 key 可经典反演修正。
4. **NP query（单次）**: 问是否存在 key h 与见证 x₁..x_m 使 π_h(x_i)⊕π_h(x_i⊕a_h)=b_i^(h) ∀i。真构造接受概率 1；Haar 下重复 m 次 + union bound over 指数多候选 key → 拒绝。
5. NP search-to-decision 归约 → 还能**学习**该幺正（非仅区分）。非自适应前向查询 + 一次 NP 查询即够。

## 可计算/可采样判定引理（组合闭包）

- **Lemma 8.3 (monomial 保持)**: 幺纯层 M|x⟩=ω(x)|π(x)⟩ 作用于 computable/samplable 态仍 computable/samplable（需 π 前向可高效计算；相位无需可算、π 无需可逆）。
- **Lemma 8.4 (乘积幅度)**: 前缀逐比特构造（prefix rotations）只需沿单条前缀路径求值，无需全局归一化因子。
- **Lemma 8.6 (2维混合)**: 单个 Kac step H_f P C 的 2×2 块条目可由有限编码 PRF 角度计算。
- 检查顺序: 基输入列（column）只需一个固定基输入可计算 → 反复 oracle 查询该输入 + Cor 8.1 即可攻击。

## 已破解清单（Table 1–3，勿再作候选）

**态构造**: PRF/binary-phase/Hamiltonian phase states；PRP subset/subset-phase states；prefix-rotation scalable；disjoint PFC blocks on Bell seed；reversible-cipher states；IQP group-action states（公共 H^⊗n 后）；其 pure OWSG 与 tensor repetition。

**幺正/等距**: Clifford PFC、phase-free PC、one-sided LRFC 及前两种 blocked 形式、PF(⊗V_j) local designs、P G H^⊗n F（含 somewhat PRU）、one Kac step H_fPC、AGKL PRI；带秘密输出 Clifford 的 C₂PFC₁、CLRFC、constant-time logical CMC、C₂PC₁。

## 幸存者清单（Table 4，攻击不适用 → 合法研究方向）

| 构造 | 难点 |
|---|---|
| Full PRSS walk | 单步分析难扩到多轮混合 |
| Long Kac walks | 多步混合后幅度不可高效求值 |
| Third blocked LRFC | monomial 层之间夹 Clifford |
| Ancilla-free glued LRFC | 粘合后 monomial 层被 Clifford 分隔 |
| Overlapping shallow/glued | 重叠块无全局 CMC 形式 |
| Phased-permutation Hamiltonians | monomial 求和的指数化 |
| Hidden-basis Hamiltonian dynamics | 秘密一般 PRU 基替代 Clifford 端点 |
| ABGL-style composition X^{k1}UX^{k3}UX^{k4} | 两 PF 被 (C₁X^{k3}C₂) 分隔 |

**设计准则**: 想在 Microcrypt 生存 → 避免任何固定基输入下幅度可计算（破坏 computability），或让中间层混合多到单列幅度无短描述；monomial 核 + Clifford 端点已死，需 Clifford-in-the-middle 或深层混合。

## 与相关工作关系

- Kretschmer: NP 攻击仅限 binary-phase PRS；本文推广到任意 computable 纯态族（允许高度非均匀幅度，无需 flatness）。
- Carrasco et al. (concurrent): 用 state certification 框架得 HPS→OWF，限均匀计算基概率；本文不要求 flat，且额外给出 NP-aided 幺正学习。
- 与 PP-oracle 可逆 OWSG（已知上界）相比，本文把所需经典能力降到 NP —— 关键在于把量子挑战转为带短经典见证的 NP 搜索。

## 排错
- 若幅度高度非均匀，勿用均匀参照 |+⟩^⊗n 干涉（信号被 S/D 压制）——必须先跑幅度阶段拿 h₀ 再自参照。
- 若候选架构在公开基变换（如 H^⊗n）后变成 phase state，即落入 computable samplable → 隐含 OWF（IQP group actions 即此）。
- Verifier 需 pointwise correctness（worst-case NP learner 的 key 不服从诚实分布）；附录 A 用 posterior sampling 放宽到平均正确性。
