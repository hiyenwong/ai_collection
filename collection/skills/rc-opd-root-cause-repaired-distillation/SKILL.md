---
name: rc-opd-root-cause-repaired-distillation
description: "On-policy自蒸馏(OPSD)指导信号设计时用。RC-OPD：用学生自身推理的修复版本（定位最早实质错误→局部修正→锚定有效前缀）替代参考解做指导，解决reasoning mismatch与蒸馏陷阱。Activation: on-policy distillation, reasoning repair, privileged hindsight, root cause analysis, distillation trap, intermediate anchor, OPSD"
metadata:
  arxiv_id: "2610.03515"
  published: "2026-10-02"
  authors: "Chenglei Shen, Haoyang Yao, Weijie Yu, Song Jin, Xiao Zhang et al."
  source: "arXiv cs.CL"
  tags: [on-policy-distillation, reasoning, error-repair, privileged-information]
---

# RC-OPD: Root-Cause-Guided On-Policy Distillation

## 核心问题

OPSD 用参考解作为 privileged hindsight 监督学生自生成轨迹，存在两个缺陷：

1. **Reasoning mismatch**：参考解解释"如何正确解题"，但不解释"学生的推理为什么错"——学生借走正确结论，自身推理错误仍未解决
2. **蒸馏陷阱**：整条轨迹统一施加 hindsight，对已正确推理段的多余约束与对实质错误的修正相互竞争

## RC-OPD 方法

用**学生自身推理的修复版本**（而非参考解）提供指导：

1. **定位**：找出失败尝试中最早的实质性错误
2. **局部修正**：只修正该错误，得到修正后的中间结果
3. **锚定**：修正中间结果作为有效前缀的 anchor
4. **迭代**：diagnosis–repair–continuation 循环，学生从修复点继续，在固定 repair budget 内暴露更多错误

蒸馏双通道：
- **Root-cause-guided**：失败诊断 + 修正目标监督错误段
- **Anchor-guided**：有效前缀由通向修复中间结果的推理链支撑

## 结果

多数据集、多模型规模上显著增益，同时缓解 reasoning mismatch 与蒸馏陷阱。
