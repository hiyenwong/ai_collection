---
name: probe-learning-to-audit-policy-compliance
description: "PROBE: Learning to Audit Policy Compliance in Tool..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.22124v1
utility: 1.0
published: 2026-10-15
---

# PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents

**Authors:** Kshitij Mishra, Abhijith Sharma, Nils Lukas, Salem Lahlou
**Published:** 2026-10-15
**arXiv:** [2610.22124v1](https://arxiv.org/abs/2610.22124v1)
**Categories:** cs.AI
**Utility Score:** 1.0

## Abstract

Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful generations, but neither tests whether agents comply with predefined policies during otherwise valid tool use. Such policy violations are difficult to audit because their effects may emerge only after several turns, span multiple tool calls, or surface in downstream systems. We propose PROBE (Policy Rule Observation via Behavioral Exploration), an algorithm for training LLM-based auditors that interact with deployed agents as realistic users and probe them for policy violations through multi-turn, tool-mediated dialogue. We formalize agent auditing as a two-player Markov game and propose a composite reward that balances violation discovery, behavioral plausibility, conversation progress, and policy diversity. To study training objectives and reward design, we compare GRPO, DPO, and GFlowNet-based optimization in a controlled setting. Across extensive experiments, auditors trained with PROBE uncover substantially broader and higher-yield policy violations than same-architecture zero-shot adversaries, even when

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-15

## Activation

probe, learning, audit, policy, compliance, toolusing, agents
