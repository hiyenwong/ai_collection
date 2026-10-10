---
name: mean-expectile-wasserstein-dro-portfolio
description: Use for expectile Wasserstein DRO portfolio optimization.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.11917
source_title: Multi-period Mean-Expectile Portfolio Optimization under Wasserstein Ambiguity
authors: Rupendra Yadav, Aparna Mehra
published: 2026-10-08
categories: q-fin.CP, math.OC
trigger_words:
  - expectile
  - wasserstein ambiguity
  - distributionally robust portfolio
  - elicitable risk measure
  - mean-expectile model
  - ground metric choice
  - price of robustness
---

# Mean-Expectile Wasserstein DRO Portfolio

## 核心问题
Expectile 是唯一同时满足 coherent（次可加、正齐次、单调、现金不变）与 elicitable（可回测）的 law-invariant 风险度量，但缺 CVaR 的 Rockafellar–Uryasev 表示，导致 Wasserstein DRO 无法直接套对偶。本文给出 envelope theorem 填补此缺口。

## 方法论（可复用模式）

### 1. Worst-case Expectile 包络定理
任何 ambiguity set 上的最坏 expectile 是标量不动点的唯一根：
```
Psi(q) = sup_F [ E_F[L] + kappa_tau * E_F[(L-q)+] ] - q
sup_F e_tau(L) = q* = min{ q : Psi(q) <= 0 }
```
其中 `kappa_tau = (2tau-1)/(1-tau)`。Psi 连续严格递减 → 唯一根，可用二分或 Lemma 5 端点结果免二分。该论证适用于任何有单调不动点表示的风险度量。

### 2. 两段仿射被积函数 → Wasserstein 对偶
被积函数 `h_t(xi) = -xi^T x + kappa*(-xi^T x - q)+ = max{-k1 xi^T x + c1 q, -k2 xi^T x + c2 q}`，斜率差 `Delta = kappa_tau`（对比 CVaR 的外生 `1/(1-alpha)`）。标准 Wasserstein 对偶给出 4 个参数化 LP，O(N) 约束（N=样本数）。

### 3. 四个结构性质（选型/诊断用）
- **P1 内生阻尼鲁棒性价格**: `dq*/drho = (1+kappa)||x||* / (1 + kappa*m/N)`，m 为超出 q* 的样本数 → 鲁棒性价格随半径自动衰减（CVaR 固定 ||x||*/(1-alpha)）。
- **P2 决策依赖退化阈值**: `rho_crit(x) = (max_i L_i - L_bar) / ((1+kappa)||x||*)`。超过它尾部失活，q* 闭式 = `(1+kappa) rho ||x||* - mu^T x`。半径选太大 → 模型退化为只惩罚最大持仓范数。
- **P3 零半径精确恢复名义模型**（校验实现正确性的单元测试基准）。
- **P4 度规几何决定分散/集中**: l_inf ground metric（对偶 l_1）→ simplex 上 ||x||_1≡1 → 惩罚常数 → 退化为最大化样本均值（集中）；l_1 ground metric（对偶 l_inf）→ max-weight 集中度惩罚 → 促分散；l_2 → ridge 型 → SOCP。**选 ground metric = 选隐式正则化**。

### 4. 多期可分性
采用 Chen et al. (2013) 可分条件风险映射保持时间一致性；expectile 单调 → 满足分解条件，多期问题化为逐期 LP。

## 实验基准
FTSE 90 成分股，250 日窗，21 日再平衡，3341 个样本外交易日（13.3 年）。tau=alpha=0.95，lambda∈{0.10,0.15,0.20}，rho∈{0.001,0.005,0.010}。expectile 在全部 9 个参数格 Sharpe 胜过完全匹配的 CVaR；rho∈{0.005,0.010} 时统计显著。半径校准用 stationary bootstrap（Politis-Romano）处理波动率聚集。

## 使用要点与坑
- 实现时先跑 P3 零半径恢复测试再上数据。
- 半径别超 rho_crit：超过后尾部成分失活，等于在做范数惩罚而非风险控制。
- l_inf 度规（沿用 Wang et al. 2026 CVaR 框架的习惯）会隐性鼓励集中——长期组合要改 l_1。
- expectile 级别与超出频率有 Bellini-Di Bernardino 对应，回测时用 elicitability 的 scoring function。

## 相关技能
- distributional-portfolio-optimization — DPO 统一框架
- hmm-rl-regime-portfolio-allocation — regime 切换型配置（可作对照）
- robust-regret-control — DRO regret 视角
