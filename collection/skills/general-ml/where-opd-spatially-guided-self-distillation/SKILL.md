---
name: where-opd-spatially-guided-self-distillation
description: MLLM细粒度感知提升时用。文本空间引导作为特权信息喂给教师，学生从图像+问题自蒸馏。Activation: on-policy distillation, privileged information, MLLM perception, synthetic scenes, spatial grounding, annotation-free post-training, synthetic-to-real transfer, teacher guidance
metadata:
  arxiv_id: "2610.02117"
  published: "2026-10-01"
  authors: "Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc, Nicolas Thome, Spyros Gidaris (Valeo)"
  source: "arXiv cs.CV, github.com/sirkosophia/Where-OPD"
  tags: [on-policy-distillation, multimodal-llm, privileged-information, perception, synthetic-data]
---

# Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs

## 核心机制

On-policy self-distillation：教师 = 自身的 frozen/EMA 版本，但接收**特权信息**；学生 on-policy 从普通输入复现教师行为。

Where-OPD 的特权形式：**文本空间引导**——标识 query 相关视觉元素及其空间坐标的文本描述（非图像裁剪）。

## 为什么用空间文本引导

- 图像裁剪特权只提升需要 zooming 的任务，且需人工标注 grounding 或外部教师模型
- 程序化生成合成场景 → 物体身份+坐标**自动免费获得** → 可扩展、免标注 post-training
- 教师用空间引导定位并整合多个相关区域证据；学生仅从图像+问题学出同等行为

## 训练配方

```
for each (procedural scene, question):
    guidance = "Relevant: {object identities + coordinates} for query"
    teacher_input = (image, question, guidance)   # frozen/EMA self
    student_input = (image, question)             # on-policy
    distill student toward teacher on-policy responses
```

## 结果

- 计数、文档、图表理解基准一致提升
- 仅用合成场景训练 → 迁移到真实感知基准：CVBench, V*, ZoomBench, BLINK, HR-Bench, MME-RealWorld 平均 **+3.23 pp**
- 证明空间特权信息经 OPD 诱导**更广感知能力**，synthetic-to-real 迁移超出训练分布

## 何时使用

- MLLM 细粒度感知短板（计数、小物体、文档/图表）
- 有程序化/仿真数据源可自动获得特权标注（身份/坐标/属性）
- 设计任何 privileged-information 蒸馏：优先考虑免标注可自动生成的特权形式，使教师能力成为学生输入的函数

## References

- arXiv: https://arxiv.org/abs/2610.02117
- Code: https://github.com/sirkosophia/Where-OPD
