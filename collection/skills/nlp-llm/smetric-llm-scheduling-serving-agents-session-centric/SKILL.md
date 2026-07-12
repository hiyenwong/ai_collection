---
name: smetric-llm-scheduling-serving-agents-session-centric
description: "Balanced session-centric LLM scheduling for agent serving workloads. Routes first request in each session for load balance and follow-ups cache-aware. 10-16% TPS improvement. Leverages intra-session locality and 80%+ KV-reuse in agent traces. Activation: LLM scheduling, agent serving, session-centric scheduling, inference infrastructure, tokens-per-second."
metadata:
  arxiv_id: "2607.08565"
  published: "2026-07-09"
  authors: "Jiahao Wang, Kaizhan Lin, Kaixi Zhang, Jinbo Han, Xingda Wei"
  tags: [llm-scheduling, agent-serving, session-centric-scheduling, inference-infrastructure, tokens-per-second]
---

# SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling

## Overview

LLM scheduling is critical to serving, yet existing designs are optimized for human-issued requests, not agent-issued ones. Agent serving shifts the workload: agents act on complete responses (making TPS the primary goal) and requests share much of their KV-cache (80%+ reuse in production traces). SMetric addresses the tension between KV-reuse and load balance with balanced session-centric scheduling.

## Key Innovations

### Agent Serving Characteristics
- Agents act on complete responses — TPS is primary, per-token latency is relaxed
- KV-reuse exceeds 80% of request tokens in agent traces (vs 54-62% in chat)
- Existing schedulers over-prioritize routing to cached instances, capping TPS

### Balanced Session-Centric Scheduling
- Routes each session's first request purely for load balance
- Follow-up requests routed cache-aware (preserving local KV-reuse)
- Session turn information derived from user inputs alone — scheduler stays clean and stateless
- Balances a small fraction of requests (first in each session) to balance the cluster

### Two Key Insights
1. Load balance need not sacrifice all KV-reuse (thanks to global-tier KV store)
2. Intra-session locality means balancing first requests suffices for cluster balance

## Methodology

1. **Session Detection**: Identify session boundaries from request patterns
2. **First-Request Routing**: Route first request in session for load balance
3. **Follow-Up Routing**: Route subsequent requests cache-aware
4. **Stateless Design**: Use session turn info from user inputs, no global state

## Implications

- Agent serving requires fundamentally different scheduling than human serving
- Session-centric scheduling is a simple yet powerful abstraction
- Stateless design avoids the complexity of global session tracking
- 10-16% TPS improvement demonstrates real-world impact

## Pitfalls

- Session detection from user inputs may not be perfectly accurate
- Global-tier KV store availability affects performance gains
- Workload characteristics may vary across different agent applications
- First-request routing may increase cold-start latency for new sessions

## Activation Keywords

LLM scheduling, agent serving, session-centric scheduling, inference infrastructure, TPS optimization, KV-cache reuse, load balancing, SMetric, BAILIAN trace

## Paper Reference

arXiv:2607.08565 - "SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling" (Jul 2026)
