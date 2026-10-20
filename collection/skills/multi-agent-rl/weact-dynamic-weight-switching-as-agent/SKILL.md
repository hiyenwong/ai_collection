---
name: weact-dynamic-weight-switching-as-agent
description: "WeAct: Dynamic Weight Switching as Agent Actions..."
tags: [cs.LG, cs.AI, cs.CL]
source: arxiv
arxiv_id: 2610.26847v1
utility: 0.87
published: 2026-10-19
---

# WeAct: Dynamic Weight Switching as Agent Actions

**Authors:** Rui Shi, Xunjian Yin, Jiacheng Sang, Zichuan Liu, Shuyan Zhou
**Published:** 2026-10-19
**arXiv:** [2610.26847v1](https://arxiv.org/abs/2610.26847v1)
**Categories:** cs.LG, cs.AI, cs.CL
**Utility Score:** 0.87

## Abstract

Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capability-specific LoRA adapters over a frozen backbone and adds adapter selection to the agent's action space. These internal actions use the model's native tool-calling interface for on-demand capability composition in a shared context. Across eight deep-research benchmarks, Qwen3-32B with WeAct improves average accuracy by 6.2% relative to full fine-tuning counterparts despite using less compute, and by 27.5% relative to the strongest static LoRA-merging method. WeAct also supports modular continual adaptation, by adding a new code computation adapter to expand the agent's capabilities and updating the existing writing adapter to improve report quality. Both updates leave the backbone and other adapters unchanged, supporting modular continual adaptation in agents.

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-19

## Activation

weact, dynamic, weight, switching, agent, actions
