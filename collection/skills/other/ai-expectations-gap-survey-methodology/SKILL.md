---
name: ai-expectations-gap-survey-methodology
description: "AI预期差距的调查研究方法论：Anthropic员工(n=1334)vs美国成年人(n=10980, Morning Consult加权代表)双组调查设计——两组对AI当下能力判断几乎一致(任务难度排序相同)但对未来进度分歧巨大(2030年Nobel级发现:员工91% vs 公众39%)；核心发现'经验差异论'：分歧源不是不同的经济模型而是对AI能力的亲身体验不同——两组在'自己工作被自动化比例→失业率预测'上有相同梯度(+10%暴露→+0.4pt失业率)；方法要点=同题双组+把raw答案映射到经济模型参数(Substantial情景)、采用频率分层解释组间差异、以时间节省倍数感知测生产率预期。适用于技术预期调查设计、专家vs公众分歧归因、AI宏观经济情景校准。Activation: expectations gap survey, expert public divergence AI, own-job exposure unemployment gradient, survey to economic model mapping, time savings perception, adoption obstacles ranking, AI labor market forecast"
version: 1.0.0
author: Szymon Sacher, Tess Cotter, Charles I. Jones, Anton Korinek, Peter McCrory (Anthropic)
date: 2026-10-16
source: https://www.anthropic.com/research/ai-expectations-gap
category: ai_collection
tags: [economics, survey-methodology, ai-forecasting, labor-markets, expectations]
activation_keywords: [Anthropic staff versus US adults survey, Nobel level discovery by 2030 expectation, own work AI automation share 75 percent versus 28, unemployment forecast own-job exposure gradient, experience not theory drives divergence, Morning Consult representative weighting, survey mapped to economic scenarios, time savings doubling perception, adoption obstacles customer preference privacy, never capable AI task share, re-employment displaced worker months]
---

# AI 预期差距：调查研究方法论

## 调查设计（可复用模板）
- **双组同题**：Anthropic 员工（2026-08，n=1334，全公司各部分）vs 美国成年人（2026-08-11~23，Morning Consult，n=10,980，加权至全国代表）
- 未来问题对一半公众问 2027、一半问 2030（报告默认 2030）；9 月复测 n=7,613 验证稳健性
- **把 raw 答案映射到经济模型参数**：沿用 Economic Scenarios for Transformative AI 的程序（其余参数固定在 Substantial 情景）→ 产出模型隐含的 GDP 增长/失业率路径，可直接比较

## 核心发现：分歧源于"经验"而非"理论"
1. **当下能力判断几乎一致**：两组对 8 项任务的难度排序基本相同（写常规邮件→Nobel 级发现）
2. **未来进度分歧巨大**：2030 能做 Nobel 级发现——员工 91% vs 公众 39%（9 月复测升至 44%）；"AI 永远做不到某任务"——公众 19-40% 说 never vs 员工 ≤2%；自己工作的自动化比例预期 75% vs 28%；任务耗时减半以上——员工 85% vs 公众使用者 26% 说 ≤1/4 时间
3. **相同的经济学模型**：两组内部，预期自己工作被自动化越多 → 预测失业率越高（每 +10% 暴露 → +0.4pt 失业预测；≥80% 暴露者预测 12.2% 失业率，超 GFC 峰值）；**同等暴露水平下两组预测几乎一样** → 分歧不是理论不同，是体验不同
4. **使用频率分层解释**：工作中的常规 AI 使用者（约 1/5 受访者）预期介于公众与员工之间；但重度使用者仍远低于员工 96% 的"2030 前能做 7/8 任务"

## 方法细节与陷阱
- **采用障碍排序**：公众认为主要是人（客户偏好真人）与规则（隐私/可靠性/法规），不是技术——说明能力≠采用，扩散有摩擦；常规使用者把隐私安全排第一
- **自动化 vs 增强的自主性提问**：到 2030 员工多数预期"AI 独立完成或人只验收"；4/10 公众预期"人主导 + AI 辅助"——同一组能力问题折射 displacement vs augmentation 的直觉差异
- **"so-so technology"检验**（Acemoglu-Restrepo）：只问"能不能做"不够，还要问时间节省倍数——刚好替代不增产的技术 vs 1/4 时间完成的技术对 GDP 含义完全不同
- **招聘悖论**：员工预期 AI 能做 75% 的自己工作，但 95% 仍预期 12 个月内 headcount 增长（中位 +66%）——在 AI 前沿实验室，"自动化任务"≠"裁员"是两个独立预测
- **再就业悲观**：员工对被替代者跨职业再就业时长的预期（中位 12 个月）比公众（7-12 个月区间）略悲观

## 可迁移的框架
做任何"专家 vs 公众"技术预期分歧研究：
1. 同题双组 + 代表性加权 + 时间锚点随机化
2. 先测"当下判断"是否一致（分离信息差异与模型差异）
3. 用组内梯度（暴露→后果预测）检验两组是否共享同一因果模型
4. 把问卷答案映射到显式经济模型参数，产出可比情景
5. 用复测轮次检验热点问题的答案漂移

## 引用来源
Sacher, S., Cotter, T., Jones, C.I., Korinek, A., McCrory, P. (2026). The AI expectations gap. https://www.anthropic.com/research/ai-expectations-gap
姊妹摘要页：https://www.anthropic.com/research/expectations-for-the-future
