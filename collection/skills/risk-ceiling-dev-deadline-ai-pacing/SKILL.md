---
name: risk-ceiling-dev-deadline-ai-pacing
description: Use when analyzing AI pacing regulation feasibility under unknown safety yield.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.11093
source_title: Risk Ceilings and Development Deadlines - Pacing AI under Uncertain Safety Productivity
authors: Li Gan
published: 2026-10-08
categories: econ.GN, cs.CY
trigger_words:
  - ai regulation
  - pacing frontier ai
  - hazard ceiling
  - development deadline
  - safety research productivity
  - learn-then-replay
  - compute allocation rules
  - instrument choice regulation
---

# Risk Ceilings and Development Deadlines — AI Pacing Economics

## 核心问题
监管者能否同时承诺「每月灾难风险上限（ceiling）」与「开发延期上限（deadline）」？当安全研究的生产率未知时，两者相容要求排除弱研究——给出生产率下界（productivity bound）并量化承诺的客户服务成本。

## 模型骨架（可复用）

### 状态-步风险分解
```
lambda(t) = [ h(F) + k(F) * Fdot ] * exp(-S)
S_dot = sigma(F) * y(s),  y(s) = psi + (1-psi)(s/s0)^alpha   # 安全知识，+ln2 → 危害减半
Fdot = theta * (xK)^eps * e^(rho R)                          # 能力研发，R=研究用模型
K(t) = K0 * e^(Gt)                                            # 算力外生指数增长
```
- **状态危害 h(F)**：部署中模型随时间的风险；**步危害 k(F)**：每单位能力提升的风险。暂停只消除步危害。
- 知识以 log-hazard 减少计价：先学后用（learn-then-replay）之所以有效，是因为早期知识沿路径保护后续更强模型。

### 四个命题
- **P1 安全-暴露条件**：暂停的边际净收益 = m·A(t) − w(t)（知识增长 × 前方剩余危害 − 站立危害）。
- **P2 必要知识下界**：紧 ceiling 要求 takeoff 结束时知识存量达到 log-降幅 → 生产率 bound 的阈值。
- **P3 learn-then-replay 近最优**：先全算力安全、后全速重放。算力增长（6 月翻倍）使重放期研发占比极小。常数产出+纯状态风险下与必要 bound 仅差 3.3%；步风险各半或知识折损时扩大到 21–72%。
- **P5 固定配置规则定日期不定风险**：compute floors/pauses/R&D-lag 固定到达日期（与生产率无关），风险效应随生产率变号——quarter-yield 时 ceiling 反而**提高**灾难概率 20.1 点（慢速通过使暴露时间变长）。

### 工具选择类比（Weitzman prices-vs-quantities）
- Ceiling = 数量工具：锁定危害路径，让延期吸收不确定性。
- 配置规则 = 价格工具：锁定日期，让风险吸收不确定性。
- 每月 ceiling 对累积概率约束极松：`P <= 1 - e^{-cbar(T0+L)}` = 77.2% > 全速的 75%。要直接控概率应改用累积危害预算。

### 成本核算
保证由客户服务支付：学习期零服务；calibration 中 7.5 月学习 = 5 年服务价值的 4.1%；2 年口径损失 52%（早买的保证早付账）。服务预算须注意口径：5 年 1% 预算的绝对损失 = 2 年预算的 13.65 倍。

## 可复用模式
1. **监管承诺相容性测试**：输入 = ceiling 要求的 log-降幅、最快学习速率、lead 允许时间。先跑必要条件，再跑 replay 条件，两 bound 之间为开放区间。
2. **生产率证据的价值**：排除弱研究的证据把不可行的无条件承诺变成可行的条件承诺——测量「安全研究降低多少危害」本身就是监管基础设施。
3. 危害归一化技巧：构造 h,k 使全速路径保持固定累积概率（75%），再比较各规则的相对效应（区分「改技术」与「改危险」）。

## 校准来源
AI Futures Project (2026) worked example：18 月 takeoff、75% 灾难概率、安全案可降至 40%；算力 6 月翻倍、eps=0.5、终点递归改进 10x；全速份额 50% 研发 / 5% 安全 / 45% 客户。均为 judgment 而非估计。

## 局限（作者自列）
算力外生（实验室可投资扩产）、执行/度量理想化、deadline 非竞速内生、知识完全迁移假设、场景数值为判断值。命题 1–5 不依赖这些数值。

## 相关技能
- frontier-training-safety-cases — 安全 case 视角
- detecting-reducing-scheming-ai — 模型层面风险
