---
name: eom-gittins-index-futures-delivery
description: Use when pricing futures delivery options via Gittins index.
category: ai_collection
metadata:
  arxiv_id: "2610.21196"
  published: "2026-10-15"
  authors: "Erhan Bayraktar (University of Michigan)"
  source: "arXiv q-fin.MF"
---

# 期货 End-of-Month 交割期权定价：Gittins Index 方法（EOM-Gittins）

**论文**: "The end-of-month option in futures contracts and the Gittins index of holding the underlying" (arXiv:2610.21196, Erhan Bayraktar, q-fin.MF, 2026-10-15, 28pp, JEL: G13/C61, 代码: github.com/ebayr/eom-gittins)

## 核心思想

期货空头在 end-of-month 窗口内可自主选择交割时点（交割价固定）。把"继续持有标的并收集便利收益"建模为一个**可退休项目**，其 Gittins index 完全刻画最优交割决策。期货价格 = 使项目价值等于现货价格的退休回报——这是一个把定价问题转译为**指数刻画**的通用模式。

## 方法论结构

### 1. 通用指数刻画（Bank–El Karoui 表示定理）
- 对任意 semimartingale 标的，最优交割由 universal index 决定：`ν(t) = sup_{τ≥t} E[∫_t^τ e^{-r(u-t)} δ_u du + e^{-r(τ-t)} R_τ]` 形式（δ=便利收益流，R=退休回报）
- 关键转换：**交割时机问题 ⇒ 停止问题 ⇒ retiming/martingale 表示**，无需具体模型即可给出价格上下界与立即交割准则

### 2. Dinkelbach 迭代求解
- 把 Gittins index 的 sup-inf 问题化为序列标准最优停时问题
- 显式压缩界保证收敛：每步解一个标准 optimal stopping（可复用任意停时求解器：PDE/binomial/Longstaff-Schwartz）
- **可复用模式**：任何 `index = inf{γ : sup_τ E[...- γ·w(τ)] ≤ 0}` 形式的量（Gittins/Sharpe-ratio 型/最大漂移抽取率）都能用 Dinkelbach 线性化成序列停时

### 3. 模型应用
- **GBM 情形**：刻画期货价=现货价的具体条件；临近到期得到 square-root 边界渐近 `b(t) ~ c√(T-t)`
- **Gibson–Schwartz（随机便利收益）**：价格对收益的单调性；存在临界收益水平 δ*，低于 δ* 时期货价=现货价（立即交割区）

## 可迁移技能模式

1. **期权定价 → 资源索引转译**：任何带内嵌择时权的合约（交割期权/转换期权/Abandonment）都可转译为持有标的的 Gittins index 问题——先找"每单位时间现金流 + 退休回报"结构
2. **Dinkelbach 分解**：含参数 sup/inf 的非凹问题 → 序列凸标量问题；每步复用现成停时求解器，收敛率有显式界
3. **无模型优先**：Bank–El Karoui 先给模型无关的刻画与界，再进具体模型——避免过拟合特定动力学假设
4. **代码**：github.com/ebayr/eom-gittins 数值复现价格迭代与交割区域

## 何时使用
- 定价期货/远期中的交割时机期权（EOM option、Treasury 交割期权、百慕大式交割权）
- 商品便利收益建模与最优库存释放时机
- 任何可写成"持有收益流 vs 退休回报"的 stopping/retirement 问题（实物期权、可退役资产、专利放弃）

## 陷阱
- Gittins index 刻画要求 discounting 结构可分离；路径依赖折现需先做 retiming 变换
- 立即交割准则依赖 δ 的符号约定（持有收益为正 → 延迟；存储成本为负 → 交割）
- Gibson–Schwartz 的临界收益 δ* 无闭式，需数值求根 + 单调性验证
