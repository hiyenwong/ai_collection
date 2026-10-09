---
name: llm-robot-exposure-index
description: "用LLM构建职业机器人暴露度指数的方法论：O*NET 900职业19000任务中先用Claude按物理/认知/人际rubric筛出物理任务，再按机器人所需环境结构化程度分四级(E0不能做/E1专用环境/E2人类工作场所/E3非结构化环境)，要求Claude联网搜索真实机器人部署/销售/演示作证据，任务举例按时间加权多数决。发现机器人能做74%物理任务(34%工时)但仅0.3%任务有成本竞争力，50年回测验证暴露度→工资就业下降。Activation: robot exposure index, O*NET task analysis, LLM labor economics, automation prediction, job task rubric, robot capability assessment"
version: 1.0.0
author: Anthropic Economics team
date: 2026-09-30
source: https://www.anthropic.com/research/what-work-can-robots-do
category: ai_collection
tags: [labor-economics, robotics, exposure-index, onet, llm-annotation, automation]
activation_keywords: [robot exposure index, O*NET, LLM task annotation, automation risk, job exposure rubric, E0-E3 exposure tiers, robot cost competitiveness, LLM vs robot exposure, task-level analysis]
---

# LLM 机器人暴露度指数

## 方法论（用 LLM 做劳动经济测量的模板）

**Step 1 — 任务分类**：O*NET ~19,000 任务描述，用 Claude 按 rubric 评分物理/认知/人际成分，筛出物理任务（"Dig trenches"物理；"Teach dance students"物理+认知+人际；打字员算账不算）。得 7,594 个物理任务。

**Step 2 — 环境分级 rubric**（核心创新：以机器人所需的环境控制程度度量暴露度）：
- E0：机器人无法执行
- E1：专用机器人环境（工厂流水线）
- E2：结构化人类工作场所（物流仓库、医院）
- E3：非结构化环境（城市道路）

**Step 3 — 证据要求**：Claude 必须联网搜索与任务相关的真实机器人，评估能力与运行环境，直接引用来源。只算已演示的能力（部署/商业销售/演示），且机器人须做到与人类相近水平（计入可靠性、错误率、速度）。仅靠演示的评级剔除后结果稳健。

**Step 4 — 任务实例分解**：任务陈述太简略，让 Claude 生成"该任务今天怎么执行+各子活动频率"的详细实例，再对实例评分。
例："Dig trenches" = 25% 开阔地直线挖沟（E3，有挖掘机自主改装系统）+ 20% 埋线管附近小心手挖（E0，需精细灵巧性）→ 多数子活动不可自动 → 整体 E0。

**Step 5 — 聚合规则**：任务级 = 多数决（机器人在至少一半时间加权实例中能做的最不结构化环境）；按"做该任务的工人数量 × 花费时间比例"加权。

## 核心发现

- 机器人能做 74% 物理任务 = 34% 工时，但大多限于受控环境（E3 仅 2%）
- 与 LLM 暴露并集：~80% 工时暴露于机器人或 LLM；未暴露的是高度人际或物理技能工作
- 成本门槛：仅 0.3% 任务上机器人有成本竞争力；按历史降价速度要 40 年才到 10%
- 50 年回测：1977 年以来高暴露职业工资与就业后续下滑——"今天能做"是未来影响的有效预测器
- 每年机器人大约能新做之前不能做的物理工作的 ~2%

## 可复用模式

- **"能力盘点回测"**：不预测未来技术，枚举今天的能力+历史回测验证，比押注哪种未来技术会成功更可靠
- **环境结构化程度作为暴露度代理**：适用于任何"技术 X 能否做任务 Y"的评估——技术能做的环境越不结构化，近期自动化风险越高
- **LLM-as-annotator + 强制引用**：LLM 打分必须附带真实证据源（部署/销售记录），并对简化任务陈述先做实例分解——直接对粗粒度描述打分是主要误差来源
