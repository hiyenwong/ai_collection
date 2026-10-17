---
name: beyond-downstream-qa-rethinking-how
description: "Beyond Downstream QA: Rethinking How We Evaluate Agent Memory"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22209"
utility: 0.99
date: "2026-10-17"
---

# Beyond Downstream QA: Rethinking How We Evaluate Agent Memory

**arXiv:** [2610.22209](https://arxiv.org/abs/2610.22209)
**Authors:** Sebastian-Antonio Toma, Jean de Kernier, Mike Ply, Oliviu Matei
**Published:** 2026-10-15
**Categories:** cs.CL, cs.AI, cs.LG
**Utility Score:** 0.99

## Abstract

Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives where incorrect responses blame correct memory for retrieval failures. We introduce FEB-30, a benchmark of 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion: documents are generated from known fact trajectories, yielding deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts (documents, emails, conversations), enabling direct inspection of the memory store after each ingestion step. Applying FEB-30 to a representative memory system, we demonstrate that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition reveals that the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time, a failure entirely invisible to extrinsic evaluation, and that failure modes differ systematically by category and difficulty. We release the benchmark, document generation pipeline, and scoring framework to support reproducible evaluation of agent memory systems.

## Key Contributions

- Novel research in cs.CL, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

beyond, downstream, rethinking, evaluate, agent, memory

## Notes

Added by arXiv cron job on 2026-10-17.
