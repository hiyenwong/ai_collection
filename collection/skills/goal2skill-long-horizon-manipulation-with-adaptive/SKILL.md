---
name: goal2skill-long-horizon-manipulation-with-adaptive
description: 'Research paper: Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection'
metadata:
  source: arXiv
  arxiv_id: 2604.13942
  published: 2026-04-15
  utility_score: 0.91
  keywords: agentic, memory, long-horizon, reasoning, planning, reflection
---

# Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection

**arXiv ID:** 2604.13942  
**Published:** 2026-04-15  
**Utility Score:** 0.91  
**URL:** http://arxiv.org/abs/2604.13942

## Authors
Zhen Liu, Xinyu Ning, Zhe Hu

## Categories
cs.RO

## Abstract
Recent vision-language-action (VLA) systems have demonstrated strong capabilities in embodied manipulation. However, most existing VLA policies rely on limited observation windows and end-to-end action prediction, which makes them brittle in long-horizon, memory-dependent tasks with partial observability, occlusions, and multi-stage dependencies. Such tasks require not only precise visuomotor control, but also persistent memory, adaptive task decomposition, and explicit recovery from execution failures. To address these limitations, we propose a dual-system framework for long-horizon embodied manipulation.   Our framework explicitly separates high-level semantic reasoning from low-level motor execution. A high-level planner, implemented as a VLM-based agentic module, maintains structured task memory and performs goal decomposition, outcome verification, and error-driven correction. A low-level executor, instantiated as a VLA-based visuomotor controller, carries out each sub-task through diffusion-based action generation conditioned on geometry-preserving filtered observations. Together, the two systems form a closed loop between planning and execution, enabling memory-aware reasoning, adaptive replanning, and robust online recovery. Experiments on representative RMBench tasks show that the proposed framework substantially outperforms representative baselines, achieving a 32.4% average success rate compared with 9.8% for the strongest baseline. Ablation studies further confirm the importance of structured memory and closed-loop recovery for long-horizon manipulation.

## Matched Keywords
agentic, memory, long-horizon, reasoning, planning, reflection

## Relevance to AI Agents
This paper is highly relevant to AI agent systems research with focus on:
- agentic, memory, long-horizon, reasoning, planning

## Quick Reference
```bash
# View paper
open http://arxiv.org/abs/2604.13942

# Download PDF
open http://arxiv.org/pdf/2604.13942.pdf
```

---
*Auto-generated from arXiv on 2026-04-17*
