---
name: actionrag-evidence-refining-graph-diffusion-for-long-term-me
description: "ActionRAG: Evidence-Refining Graph Diffusion for Long-Term..."
category: multi-agent-rl
tags: [cs.AI, cs.CL]
source: arxiv
paper_id: 2610.32752v1
utility: 0.85
---

# ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

**arXiv ID:** 2610.32752v1
**URL:** http://arxiv.org/abs/2610.32752v1
**Published:** 2026-10-23T14:59:37Z
**Categories:** cs.AI, cs.CL
**Utility Score:** 0.85

## Abstract

LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evide

## Key Contributions

- Paper from arXiv in categories: cs.AI, cs.CL
- High utility score (0.85) indicates relevance to AI/ML research
- Published: 2026-10-23T14:59:37Z

## Related Skills

This paper relates to the `multi-agent-rl` category based on keyword analysis.
