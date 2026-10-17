---
name: probe-learning-audit-policy-compliance
description: "PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22124"
utility: 0.99
date: "2026-10-17"
---

# PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents

**arXiv:** [2610.22124](https://arxiv.org/abs/2610.22124)
**Authors:** Kshitij Mishra, Abhijith Sharma, Nils Lukas, Salem Lahlou
**Published:** 2026-10-15
**Categories:** cs.AI
**Utility Score:** 0.99

## Abstract

Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful generations, but neither tests whether agents comply with predefined policies during otherwise valid tool use. Such policy violations are difficult to audit because their effects may emerge only after several turns, span multiple tool calls, or surface in downstream systems. We propose PROBE (Policy Rule Observation via Behavioral Exploration), an algorithm for training LLM-based auditors that interact with deployed agents as realistic users and probe them for policy violations through multi-turn, tool-mediated dialogue. We formalize agent auditing as a two-player Markov game and propose a composite reward that balances violation discovery, behavioral plausibility, conversation progress, and policy diversity. To study training objectives and reward design, we compare GRPO, DPO, and GFlowNet-based optimization in a controlled setting. Across extensive experiments, auditors trained with PROBE uncover substantially broader and higher-yield policy violations than same-architecture zero-shot adversaries, even when the auditor is significantly smaller than the target agent. Our results show that multi-turn behavioral auditing is a distinct and necessary axis of agent evaluation, complementing capability and safety benchmarks. PROBE offers a scalable path toward automated policy auditing for real-world agentic systems and suggests a co-evolutionary loop in which auditors expose failures and agents improve from auditor feedback.

## Key Contributions

- Novel research in cs.AI
- High utility score (0.99) indicating significant research value

## Activation

probe, learning, audit, policy, compliance, toolusing, agents

## Notes

Added by arXiv cron job on 2026-10-17.
