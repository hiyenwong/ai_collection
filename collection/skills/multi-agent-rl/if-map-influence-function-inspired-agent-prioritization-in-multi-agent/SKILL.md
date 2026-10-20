---
name: if-map-influence-function-inspired-agent-prioritization-in-multi-agent
description: "IF-MAP: Influence-Function-Inspired Agent Prioriti..."
tags: [cs.AI, cs.MA]
source: arxiv
arxiv_id: 2610.24383v1
utility: 1.0
published: 2026-10-17
---

# IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems

**Authors:** Jie Mao, Pingchen Lu, Zikun Qu, Jiahang Sun, Xiangyi Wang...
**Published:** 2026-10-17
**arXiv:** [2610.24383v1](https://arxiv.org/abs/2610.24383v1)
**Categories:** cs.AI, cs.MA
**Utility Score:** 1.0

## Abstract

Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and Dee

## Key Contributions

- Novel research in cs.AI, cs.MA
- Published 2026-10-17

## Activation

ifmap, influencefunctioninspired, agent, prioritization, multiagent, systems
