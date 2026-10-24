---
name: fisher-geometric-multi-teacher-opd
description: Use when consolidating homologous specialist LLMs into one generalist. Multi-teacher on-policy distillation equals Fisher merging to second order; RGBM merge-then-gated-branch procedure.
category: ai_collection
metadata:
  arxiv_id: "2610.26525"
  published: "2026-10-19"
  authors: "Liu, Zhuang, Ma, Gu, Song, Weng, Ye (Meituan LongCat / ZJU / NJU / SJTU)"
  source: "arXiv cs.LG"
---

# Fisher-Geometric View of Multi-Teacher On-Policy Distillation (RGBM)

**论文**: "A Fisher-Geometric View of Multi-Teacher On-Policy Distillation" (arXiv:2610.26525, Meituan LongCat)

## 核心定理：合并 ≡ 蒸馏（不同逼近阶）

K 个同源 specialists {W_φd}（同一 base W_ref 上 RL 微调），多教师在线蒸馏目标

J_MOPD(θ) = Σ_d p_d · E_x~D_d [KL(π_θ ‖ π_φd)]

**Thm 1（二阶等价）**：共享盆地内二阶 Taylor 展开

J_MOPD(θ) = ½ Σ_d p_d (θ−W_φd)^T F_d (θ−W_φd) + O(‖·‖³)

即聚合 Fisher 距离；其无约束最优解 = **Fisher merge** θ*_Fisher = (Σ p_d F_d)^{-1} Σ p_d F_d W_φd（Matena & Raffel 2022 的经典合并法）。证明只用：在 θ=W_φd 处 KL 与梯度为零、Hessian = F_d。

**结论：合并不是蒸馏的启发式替代，而是蒸馏目标的二阶闭式阶段。从 Fisher merge 出发的梯度步只作用于三阶余项——merge before you distill。**

## 两个可计算化引理

**子空间投影（Eq.5）**：全参数 Fisher 逆不可行 → 限制到任务向量子空间 θ(α) = W_ref + T α（T 堆叠 task vectors τ_d = W_φd − W_ref），得 K×K 闭式解。Task Arithmetic 的系数即 Fisher 目标到任务子空间的度量投影。

**一阶隐式奖励同态（Prop 2，最实用）**：r_d(x,y) = log(π_φd(y|x)/π_ref(y|x))（RL 微调隐式优化的 log-prob ratio），则合并模型的 log-ratio

ℓ_α(x,y) = log(π_{θ(α)}/π_ref) ≈ Σ_d α_d r_d(x,y) = α^T r

推论：
1. 投影 Fisher 是奖励经验协方差 S_d ≈ Cov_π(r)——**只用前向 pass 可估，无需梯度**
2. **Label-free 线性盆地测试**：Err_lin(θ(α)) := 1 − R²(ℓ_α ~ α^T r)。超阈值 δ_tol=0.10 ⇒ 一阶叠加失效、checkpoint 已离开盆地——既是诊断也是写回上限

## RGBM：Residual-Governed Branch-and-Merge

**Phase 1（零训练 merge + 残差谱）**：
- 无标签提示上（域 d 出的 completions + base 与 K 个 specialist 前向）累积二阶矩 M_d = E[r r^T]（= Cov + 均值漂移外积，上界化 Fisher 残差；装配 <2 GPU·h）
- 域残差 L_d(α) = (α−e_d)^T M_d (α−e_d)
- **Minimax QP**：α* = argmin_α max_d L_d(α)——对未知域权重 p_d 取最坏情况 = 不牺牲任何域；K 维 QP 求解 <10ms；λ=1e-4 正则，α 不限 [0,1]
- **Domain Residual Spectrum**：L̄_d = L_d/E[r_d²]（按该域奖励能量归一化，跨域可比）——merge 后该域还剩多少能量份额没恢复

**Phase 2（谱门控 + 隔离分支 + 收缩写回）**：
- Gate：排序 + floor 0，在最大相邻 gap 中点切 ε（Eq.10）；L̄_d > ε 为 active，否则 passivated
- Passivated 域：Δ_d = 0，不写回（merge 已覆盖）
- Active 域：从 θ*_0 训练隔离分支（无梯度共享）得 Δ_d
- **唯一写回**：θ_RGBM = θ*_0 + Σ γ*_d Δ_d，其中 γ*_d = max{γ∈Γ: Err_lin(θ*_0+γΔ_d) ≤ δ_tol}，Γ={0.125,0.25,0.5,0.75}——收缩因子由线性测试封顶，写回不得破坏 Phase 1 叠加
- 整个流程 3 个固定常数（λ, Γ, δ_tol），**不用任何标注数据**

## 为什么不能从 merge 继续联合蒸馏

θ*_0（minimax 点）非 Fisher 驻点 → 各域梯度在共享权重上冲突拉离任务子空间；对低 L̄_d 域再花预算是"在缺口已闭合处花步骤"，三域总损失恶化而该域自己还在改善——**token 级 KL penalty 挡不住权重空间的碰撞**。所有 un-gated 写回（uniform 蒸馏 30.91 / TIES 30.96 / DARE 31.42 / γ=1.0 31.80）全部低于 merge 本身 32.52。

## 结果

- **Open-MOPD**（SmolLM3-3B，Math/Code/IF）：Phase 1 零训练 merge Macro **32.52** > 官方 600-step 蒸馏学生 30.93（144 GPU·h）> Task Arithmetic 31.31；谱 (0.128, 0.052, 0.015) → ε=0.090 只 Math active，γ*=0.125 → RGBM **33.03**（零联合训练步）
- **G-OPD**（Qwen3-4B）：同流程不变迁移，53.34 > SFT/OPD/TA；两域谱聚集 (0.094, 0.090) → 都 active，γ*=0.5 → **54.14 超最强训练基线 ExOPD**
- **系数是关键**：等权平均在 G-OPD 崩溃到 36.75（vs 53.34）——增益来自解出的 α 而非任务向量本身

## 实践清单

1. 有同源 specialists 要整合时：先做子空间 minimax merge（零训练），再考虑任何蒸馏
2. 用 Err_lin（1−R² 回归）作为 label-free 盆地有效性检查，任何写回前必测
3. 写回必须过 linearity gate + 收缩网格，宁小勿大（γ*=0.125 常见）
4. 从 merge 继续联合蒸馏是有害操作（共享权重梯度冲突）
5. 残差谱归一化（除以 E[r_d²]）才能跨域比较——能量大的域天然残差大

## 局限

- 共享盆地 + 同源 specialists 假设；异构模型（不同 base）不适用
- 一阶同态是近似；K 小（2-3 域）；谱反映"联合组合后剩余"非"该域已饱和"（passivated 域仍可单独改善，只是不能写回）
- 域残差用无标签提示估计，对分布偏移敏感

## 相关 skill

- [[training-free-on-policy-distillation]] — 无训练模型合并（本文为其提供理论基础）
- [[evo-generative-llm-merging]] / [[gffmerge-model-merging-gnns]] — 其他合并方法（本文证明其 Fisher 系数最优性）
- [[efficient-opd-distillation]] / [[opd-pre-rl-distillation]] — OPD 实践
