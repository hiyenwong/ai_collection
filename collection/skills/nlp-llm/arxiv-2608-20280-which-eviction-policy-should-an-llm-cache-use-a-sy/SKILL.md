---
name: arxiv-2608-20280-which-eviction-policy-should-an-llm-cache-use-a-sy
description: 'Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders (arXiv: 2608.20280)'
category: nlp-llm
version: "1.0"
date: 2026-08-22
---

# Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders

**Authors:** Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu
**arXiv:** 2608.20280
**Utility:** 1.00
**Published:** 2026-08-20T17:14:19Z
**Link:** http://arxiv.org/abs/2608.20280

## Abstract

Semantic caches reuse an LLM response when the incoming query embedding lies near a cached query, but proposed eviction policies have rarely been compared under one protocol. Using CLEVER, we evaluate FIFO, LRU, LFU, ARC, GDSF, a single-pass streaming adaptation of SISO, and a semantic-redundancy policy across three ordered, deduplicated query corpora, three cache capacities, and two encoders. No evaluated policy improves on LFU by more than 0.041 percentage points in any of the eighteen settings. Replacement is not irrelevant: FIFO and streaming SISO trail LFU by as much as 8.67 and 8.55 points, respectively, at tight capacity.
  We explain the missing upside with a conditional packing result. Under exact lookup and insert-on-miss, a newly inserted entry cannot have a resident neighbor within the hit radius, so a geometry-aware eviction rule receives little new redundancy signal. A separate audit exposes a larger problem with the evaluated operating point. At MiniLM's median nearest-neighbor threshold, only 2.1-3.9% of sampled LMSYS and QQP hits are judged answer-substitutable, reducing raw hit rates of 51-60% to quality-adjusted rates of 1.1-2.2%. The cross-encoder study further shows that thresholds do not transfer between embedding models. LFU is the strongest simple default in this protocol; deployment decisions should first establish answer validity and then test sub-point policy differences with exact search.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders". 
The paper presents novel ideas in nlp-llm that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20280
