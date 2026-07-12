---
name: fabrivia-lightweight-vision-language-action-multi-task-manipulation
description: "FabriVLA: lightweight VLA model combining InternVL3.5 VLM backbone with flow-matching action head. Gated self-attention across action tokens, shallow VLM layer fusion. 90.0% success on Meta-World MT50. 1B-scale VLM without billion-parameter backbone. Activation: vision-language-action, lightweight model, multi-task manipulation, flow-matching, robot learning."
metadata:
  arxiv_id: "2607.08575"
  published: "2026-07-09"
  authors: "Shiyuan Yang, Borong Zhang, Jizheng Zhang, Zhijia Tao, Junfei Guo"
  tags: [vision-language-action, lightweight-model, multi-task-manipulation, flow-matching, robot-learning]
---

# FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation

## Overview

FabriVLA is a lightweight Vision-Language-Action model that demonstrates a compact VLA built on a 1B-scale VLM can achieve strong performance without relying on multi-billion-parameter VLA backbones. It combines an InternVL3.5 vision-language backbone with a flow-matching action head, trained via single-stage joint optimization.

## Key Innovations

### Compact Architecture
- InternVL3.5 vision-language backbone (1B scale)
- Flow-matching action head with gated self-attention across action tokens
- Shallow VLM layer fusion for enriched spatial context
- No reliance on multi-billion-parameter backbones

### Single-Stage Joint Optimization
- Trained from pretrained VLM and randomly initialized action head
- Joint optimization in a single stage
- Avoids complex multi-stage training pipelines

### Meta-World MT50 Performance
- 90.0% tier-average success rate across 50 diverse manipulation tasks
- Demonstrates that compact VLA models can match larger architectures
- Strong performance across diverse task types

## Methodology

1. **Backbone Selection**: InternVL3.5 as VLM backbone (1B scale)
2. **Action Head Design**: Flow-matching head with gated self-attention
3. **Fusion Strategy**: Shallow VLM layer fusion for spatial context
4. **Training**: Single-stage joint optimization from pretrained VLM + random action head
5. **Evaluation**: Meta-World MT50 benchmark (50 tasks)

## Implications

- Lightweight VLA models are viable alternatives to large-scale VLA architectures
- 1B-scale VLMs provide sufficient vision-language understanding for manipulation
- Flow-matching action heads with gated attention are effective for action generation
- Single-stage training simplifies VLA deployment

## Pitfalls

- Meta-World MT50 is simulation-only — real-world performance not demonstrated
- 1B-scale VLM may struggle with complex language instructions
- Single-stage training may not be optimal for all task domains
- Flow-matching may be slower than direct action prediction at inference

## Activation Keywords

vision-language-action, FabriVLA, lightweight VLA, multi-task manipulation, flow-matching, InternVL3.5, robot learning, Meta-World MT50, compact model

## Paper Reference

arXiv:2607.08575 - "FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation" (Jul 2026)
