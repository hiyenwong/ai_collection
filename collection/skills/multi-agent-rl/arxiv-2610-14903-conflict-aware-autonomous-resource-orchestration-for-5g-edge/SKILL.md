---
name: arxiv-2610-14903-conflict-aware-autonomous-resource-orchestration-for-5g-edge
description: 'Conflict-Aware Autonomous Resource Orchestration for 5G Edge Slicing Using Multi (arXiv: 2610.14903)'
metadata:
  {
    "arxiv_id": "2610.14903",
    "utility": 0.96,
    "title": "Conflict-Aware Autonomous Resource Orchestration for 5G Edge Slicing Using Multi-Agent Systems and LLMs",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.14903"
  }
---

# Conflict-Aware Autonomous Resource Orchestration for 5G Edge Slicing Using Multi-Agent Systems and LLMs

**arXiv ID:** 2610.14903
**URL:** https://arxiv.org/abs/2610.14903
**Utility Score:** 0.96

## Abstract

5G edge network slicing must reconcile two coupled requirements: understanding high-level operator intent and reallocating scarce computing and bandwidth resources under dynamic contention. Centralized optimization can face computational and responsiveness challenges under rapidly changing edge contention, and Multi-Agent System (MAS)-based auctions can support resource arbitration but still depend on operator-defined economic parameters and priorities. Embedding a Large Language Model (LLM) directly in a recurring control loop, by contrast, may introduce non-negligible inference latency and non-deterministic behavior. This paper proposes a two-timescale architecture that addresses this gap: an LLM-based Strategist translates natural-language network intents into economic policy parameters (budget, income, and bidding-aggressiveness) at the macro scale, while a deterministic, Vickrey-inspired second-price mechanism run by SPADE-based slice agents resolves recurring resource contention at the operational scale, with the resulting allocations enforced by patching Kubernetes CPU limits and Calico CNI bandwidth annotations directly on User Plane Function pods. We evaluate the architecture end-to-end on a real Kubernetes/Open5GS edge cluster across two complementary scenarios, each repeated 30 times: a Smart-City scenario, in which natural-language public-safety intents propagate into measurable changes in slice bids and bandwidth allocations within a few auction rounds, and a Hierarchical-slicing scenario, in which the mechanism provides priority-dependent resource and QoE differentiation, adapts to abrupt demand changes, and preserves configured minimum guarantees while maintaining near-complete allocation of the shared bandwidth pool.

## Key Topics

multi-agent, orchestration, ppo, autonomous

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.14903
