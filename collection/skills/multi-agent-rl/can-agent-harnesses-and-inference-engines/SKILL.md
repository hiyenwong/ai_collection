---
name: can-agent-harnesses-and-inference-engines
description: "Can Agent Harnesses and Inference Engines Hear Eac..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.06597v1
utility: 0.95
published: 2026-10-05
---

# Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving

**Authors:** Jiaqi Zhao, Haodong Chen, Jitai Hao, Wei Zhao, Jinghao Pang...
**Published:** 2026-10-05
**arXiv:** [2610.06597v1](https://arxiv.org/abs/2610.06597v1)
**Categories:** cs.AI
**Utility Score:** 0.95

## Abstract

LLM agents increasingly execute complex workflows involving multi-turn reasoning, tool use, and parallel agents. Efficient serving requires decisions that span two layers with complementary information: the agent harness understands workflow dependencies, context lifecycles, and execution objectives, whereas the inference engine observes request queues, KV-cache state, resource pressure, and execution capabilities. Existing interfaces do not systematically connect these views, limiting workflow-aware execution. HEAR, a bidirectional Harness--Engine Pairing protocol for agentic LLM serving. HEAR standardizes how the harness communicates workflow intent and execution requirements and how the engine returns runtime state, capabilities, and outcomes. By separating protocol semantics from optimization policies, HEAR supports diverse coordination strategies without changing workflow or model semantics. We instantiate HEAR for online cache-aware runtime coordination and workload-aware execution-mode selection for agent roles. Across four conversational and research-agent benchmarks under memory-constrained, concurrent serving, HEAR achieves a $1.61\times$ batch speedup and reduces median time-to-first-token by $2.23\times$ on SCBench. Mooncake shows that workflow intent and live engine state provide complementary benefits across load regimes. On BrowseComp-Plus and DeepResearchBench, workload-specific configurations yield $1.23\times$ and $2.45\times$ end-to-end speedups, respective

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-05

## Activation

agent, harnesses, inference, engines, hear, each, other, hear, protocol, agentic
