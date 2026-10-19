---
name: thought-blocks-non-autoregressive-latent-communication-for-multi-agent-systems-v
description: 'Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation (arXiv: 2610.23056v1). Utility: 0.85. Categories: cs.MA'
metadata:
  {
    "arxiv_id": "2610.23056v1",
    "utility": 0.85,
    "title": "Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation",
    "authors": "Zhenhan Guan, Xiaolong Liu, Hengwei Ye, Zheng Tian",
    "url": "https://arxiv.org/abs/2610.23056v1",
    "categories": "cs.MA"
  }
---

# Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation

**arXiv ID:** 2610.23056v1
**Authors:** Zhenhan Guan, Xiaolong Liu, Hengwei Ye, Zheng Tian
**URL:** https://arxiv.org/abs/2610.23056v1
**Utility Score:** 0.85
**Categories:** cs.MA

## Abstract

LLM-based multi-agent systems typically communicate through text, incurring repeated generation and re-encoding costs. Although latent communication removes explicit verbalization, constructing latent messages may still require autoregressive latent trajectories. We therefore distinguish message representation from message construction and ask whether agents can directly construct useful continuation states without executing the trajectories that normally produce them. We formulate this problem as trajectory-to-state compilation and introduce Thought Blocks, fixed-size blocks of latent key--value (KV) continuation memory constructed in one shot. Thought Blocks achieve a 2.5 times average latency speedup over autoregressive latent communication. Compared with text-based multi-agent communication, Thought Blocks reduce text tokens by 45.7% and autoregressive steps by 84.8%, achieving an 8.6 times average latency speedup. These results demonstrate that trajectory-to-state compilation enables efficient inter-agent latent communication without sequential latent rollouts at inference.

## Key Concepts

- This paper addresses important questions in: cs.MA
- Published: 2026-10-16

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows and research tracking.

## References

- arXiv: https://arxiv.org/abs/2610.23056v1
