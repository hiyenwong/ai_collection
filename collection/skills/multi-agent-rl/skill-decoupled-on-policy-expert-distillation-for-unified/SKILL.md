---
name: skill-decoupled-on-policy-expert-distillation-for-unified
description: "Skill-Decoupled On-Policy Expert Distillation for ..."
tags: [cs.CV, cs.AI]
source: arxiv
arxiv_id: 2610.22217v1
utility: 0.87
published: 2026-10-15
---

# Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models

**Authors:** Yuqi Xiong, Chunyi Peng, Zhipeng Xu, Qing Yang, Zhenghao Liu...
**Published:** 2026-10-15
**arXiv:** [2610.22217v1](https://arxiv.org/abs/2610.22217v1)
**Categories:** cs.CV, cs.AI
**Utility Score:** 0.87

## Abstract

Reinforcement learning (RL) can elicit specialized visual capabilities in vision-language models (VLMs), yet jointly optimizing heterogeneous objectives often introduces cross-capability gradient conflicts. Training experts independently mitigates this interference, but direct reward optimization may entangle specialized knowledge with reward-hacking biases. This paper proposes Skill-Decoupled On-Policy Expert Distillation (SCOPED), which trains capability-specific experts and extracts explicit skills through reward-guided reflection. During on-policy distillation, these skills guide expert supervision while remaining unavailable to the unified student, encouraging it to internalize procedural knowledge without explicit skills at inference time. Across eight multimodal benchmarks, SCOPED consistently outperforms the backbone and mixed-capability RL, demonstrating the effectiveness of skill-decoupled on-policy expert distillation for integrating independently acquired capabilities. Further analyses reveal interference during joint capability optimization and suggest that skill augmentation promotes more consistent expert trajectories, greater attention to task-relevant visual evidence, and better preservation of specialized expertise in the unified student. All code and data are available at https://github.com/NEUIR/SCOPED.

## Key Contributions

- Novel research in cs.CV, cs.AI
- Published 2026-10-15

## Activation

skilldecoupled, onpolicy, expert, distillation, unified, visionlanguage, models
