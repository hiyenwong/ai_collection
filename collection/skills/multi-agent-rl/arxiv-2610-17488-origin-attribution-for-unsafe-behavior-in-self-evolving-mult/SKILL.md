---
name: arxiv-2610-17488-origin-attribution-for-unsafe-behavior-in-self-evolving-mult
description: 'Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Syste (arXiv: 2610.17488)'
metadata:
  {
    "arxiv_id": "2610.17488",
    "utility": 0.86,
    "title": "Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.17488"
  }
---

# Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems

**arXiv ID:** 2610.17488
**URL:** https://arxiv.org/abs/2610.17488
**Utility Score:** 0.86

## Abstract

As language-model-based coding agents evolve their programs and reuse code from one another, safety failures can acquire a history that extends beyond the agent in which they are detected. An unsafe change may originate in one agent, propagate through intermediate recipients, and survive subsequent revisions before an audit reveals it. Understanding this history is important for identifying the introducing change and distinguishing inherited behavior from independently occurring failures. We study origin attribution in self-evolving multi-agent coding systems: recovering the agent and program version that introduced an observed unsafe behavior into the target&#39;s code lineage, or determining that it arose locally. This task is challenging because rewriting obscures textual similarity, independent occurrences confound temporal ordering, and intermediate recipients can resemble the source. We propose a method that combines behavioral fingerprint matching with historical localization and recursive tracing. It compares candidate implementations beyond the unsafe outcome, retains evidence from multiple historical versions, and follows matching candidates upstream. On 158 queries across 85 controlled scenarios, the method achieves 96.8% exact attribution accuracy, compared with 77.2% for exhaustive fingerprint matching without recursion. Component ablations and evaluation on 34 additional queries using the same method and hyperparameters demonstrate the complementary roles of multiple representatives and recursive tracing. Further checks extend the evaluation to approval-boundary and resource-owner errors. Together, these results show how behavioral and historical evidence can recover the origins of unsafe behavior through code revision and cross-agent propagation.

## Key Topics

multi-agent, self-evolving, safety, vision

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.17488
