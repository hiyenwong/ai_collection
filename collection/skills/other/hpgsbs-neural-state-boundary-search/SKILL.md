---
name: hpgsbs-neural-state-boundary-search
description: Interval-statistics reuse speeds GSBS neural-state search.
category: neuroscience
arxiv_id: "2610.25898"
tags: [neural-state-segmentation, GSBS, EEG, fMRI, algorithm-acceleration, prefix-sums, t-distance, greedy-search]
---

# HP-GSBS：可复用区间统计加速神经态边界搜索

> arXiv:2610.25898 — "HP-GSBS: Accelerating greedy state boundary search with reusable interval statistics" (Yanzhe Zhao, Yongzhang Ji, 2026-10-19, cs.CE/q-bio.NC)
> 代码: github.com/JustinZHAO-05/HP-GSBS (v0.2.0, MIT; NumPy/SciPy/Numba + PyTorch CUDA + Triton)

## 问题与结果

GSBS（Greedy State Boundary Search）在神经活动序列中找"相对稳定模式之间的转换边界"（状态分割），广泛用于 EEG/fMRI/高密度电生理。瓶颈：每个候选边界都触发**状态均值模板重构+全序列比对**，双边界搜索候选空间随区间长度二次膨胀，refinement 又重算未变区间。

HP-GSBS 把计算重组为**可复用统计**：区间分数表 O(1) 查找替代模板重构；2D 前缀和把 t-distance 的成对相关统计降为 O(K) 矩形查询。**结果：154–1730× 中位加速；168 次优化执行全部复现官方边界与状态数（最大 |ΔTD| = 1.88×10⁻¹¹）**。

## GSBS 目标函数（正确形式——主文公式有排版损坏）

pdftotext 提取的主文 Eq(1) 前因子 `√(T/(TP−1))` 是**上标丢失型损坏**（T²(P−1) 的 ² 被丢）。真实形式（本会话由补充材料 S1–S3 推导并数值确认，200 区间最大误差 1.11×10⁻¹⁶）：

```
F(a,b) = (B_b − B_a)ᵀ(A_b − A_a) / ( T · √(P−1) · ‖A_b − A_a‖₂ )
```

其中（X ∈ R^{T×P}，逐行中心化/标准化，样本 std P−1）：
- `c_t = H·x_t`（H = I − 11ᵀ/P 行中心化算子）；`z_t = √(P−1)·c_t/‖c_t‖`
- `A_b = Σ_{t<b} c_t`，`B_b = Σ_{t<b} z_t`（前缀和，O(T·P) 一次构建）
- **语义**：J(S) = Σ_{区间∈S} F = 全局**平均空间相关**——每个时间点与其所属状态模板的 Pearson 相关的均值（"GSBS maximizes the mean spatial correlation"）。
- **长度因子消去**：标准化状态均值 z(m_S)=√(P−1)·ΔA/‖ΔA‖ 使 r_t 不含区间长度 n。

分裂增益只需查表：`Δ₁(i) = F(a,i)+F(i,b)−F(a,b)`；`Δ₂(i,j) = F(a,i)+F(i,j)+F(j,b)−F(a,b)`。Q 表构建 O(T²P) 算术 / O(T²) 存储——之后**每个候选是 O(1) 查找**（vs 官方 O(TP) 模板重构）。

## t-distance 状态数选择（补充材料 S2–S6）

- 模式相关 `r_ij = U_iᵀU_j/(P−1)`（U 行标准化，对齐 numpy.cov 中心化）
- **W = {r_ij : j−i ≥ d, s(i)=s(j)}**（同状态对），**A = {r_ij : j−i≥d, s(j)=s(i)+1}**（相邻状态对），d=dmin 编码进对掩码
- 充分统计 (n, S=Σr, Q=Σr²)：µ=S/n，v=(Q−S²/n)/(n−1)，**TD = (µW−µA)/√(vW/nW+vA/nA)**（Welch 对比；无推断 p 值）
- **2D 前缀四角查询**：valid-pair 指示阵、掩码相关阵、平方阵各建 2D 零填充前缀 → 任意矩形和 O(1)；状态端点 O(T) 构造后每分区 **O(K) 查询**（vs O(T²) 扫描）。本会话验证：前缀 TD vs 直接扫描最大差 1.5×10⁻¹¹。
- 单 vs 双边界决策也用 t-distance；双插入允许最终 K = Kmax+1（索引保留）。

## 本会话完整复现（mini-GSBS，论文 Fig 2 合成示例）

T=80, P=16, 4 状态@边界 20/40/60, 噪声 σ=0.05, seed 19, Kmax=12：
- 贪心插入历史：K=2:[40] → K=3:[20,40] → **K=4:[20,40,60]**（与论文完全一致）
- TD 曲线：K=2:37.2 → K=3:67.3 → **K=4:339.4（峰值）** → K=5:104.2 →…
- **选择 K*=4 @ [20,40,60]** ✓ 全部三验证 PASS

## 工程加速模式（可迁移）

1. **区间统计复用**：目标可加分解为区间贡献时，预计算区间分数表把"重构+比对"降为查找——适用于一切贪心分裂/变点检测（PELT 思想的同胞）。
2. **流式候选削减**：按序评估合法候选只保留最大值，消去 O(L²) 双候选分数数组。
3. **窗口局部 refinement + 活动块缓存**：插入边界只影响局部——只重评估请求邻域，局部块分数乘 T/L_b 恢复全局归一化；分区未变时复用局部赢家。
4. **低内存模式**：特征矩替代成对时间矩阵——区间摘要 (L_S, u_S=ΣU_t, M_S=ΣU_tU_tᵀ, D1=Σ‖U_t‖², D2=Σ‖U_t‖⁴) 直接给出 within/cross 的 (n,S,Q)：`S_S=(‖u_S‖²−D1)/(2h)`, `Q_S=(‖M_S‖²_F−D2)/(2h²)`，h=P−1。5000×8 输入峰值 RSS 1598→190.6 MiB，运行 9.75→0.110s；系列达 50000×64 @ 469.5 MiB / 1.444s。
5. **数值一致性纪律**：FP64 默认、TF32 禁用、参考表达式复评、sentinel/首最大规则/非有限分数处理对齐参考实现——**加速不得改变科学输出**（边界历史逐位复现）。
6. **三后端共享顺序控制器**：CPU/Numba、PyTorch CUDA（批量 Gram+前缀）、Triton（融合差分/点积/范数）喂同一个串行搜索控制器——GPU 只做规则数值工作。

## 实证规模（供引用）

- 7 受控负载×2 实现：中位同输入加速 154–1730×；中心配置 T=512,P=32,Kmax=20：官方 64.7s vs CPU 0.142s / PyTorch 0.081s / Triton 0.099s。
- 4 个冻结 EEG（Brain Body & Behavior 数据集，5.12Hz，dmin=5, blocksize=50）：K*=126/120/173/131，三后端边界历史全同，|ΔTD|≤3.13×10⁻¹³。
- 机制消融（1336×64, Kmax=131）：物化 3.364s → 流式 1.803s → +窗口 1.601s → +缓存 1.429s。

## 使用

```python
from hpgsbs import GSBSConfig, GSBSResult, fit, fit_many
cfg = GSBSConfig(kmax=20, dmin=1, mode="throughput")
r = fit(x, cfg, backend="cpu-fast")          # 或 torch-cuda / triton
bounds, curve = r.get_bounds(r.nstates), r.tdists
r.save("results/recording.npz")               # 版本化持久化, 原子 CLI, 断点续跑
batch = fit_many(recordings, cfg, backend="torch-cuda", batch_size="auto")
```

## Activation

neural state segmentation, GSBS acceleration, state boundary search, EEG segmentation, fMRI state detection, t-distance state count, prefix sums interval statistics, greedy change point, streaming candidate reduction, low-memory pairwise statistics

## 相关技能

- `mts-slds-multi-timescale-switching`（切换 LDS 状态分割）
- `heteroclinic-cognitive-state-modeling`（认知状态序列动力学）
- `eeg-microstate-cluster-illusion`（微状态聚类的统计陷阱）
