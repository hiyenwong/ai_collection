---
name: sedima-hierarchical-insight-memory-evolutionary-search
description: Use for LLM evolutionary search agents needing cross-run memory. Three-level insight hierarchy.
category: ai_collection
---

# Sedima: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents

**Paper**: "Sedima: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents" (arXiv: 2610.02361, Abaskohi, Mostajabdaveh & Zhou, UBC / Huawei Technologies Canada, Oct 2026). Code on GitHub.

## What It Solves

LLM-driven evolutionary search systems (OpenEvolve, ShinkaEvolve, LLM4AD) are **memoryless**: each run starts from scratch, re-deriving the same improvements and re-exploring the same dead ends. Within a single run, quality also fluctuates as the agent proposes, forgets, and re-proposes locally useful edits.

Sedima is a **drop-in module** — it attaches via exactly two hooks (write after each evaluation, read before each mutation) and leaves all search operators (selection, population, mutation, evaluation) unmodified. It is single-agent (unlike multi-agent memory systems like PRISM/Reflexion-style persistent loops).

## Three-Level Memory Hierarchy

### Level 1: Raw traces (evidence layer)
After each evaluation, store: step index, parent and child fitness, fitness difference, event source, raw evaluation report. No interpretation. Purpose: keep retrieved recommendations linked to their originating evaluation events. Never pruned at write time.

### Level 2: Distilled insights (abstraction layer)
An LLM converts each trace into a compact natural-language insight linked back to its Level 1 evidence:
- **Problem-level insight** (on first evaluation of a problem): describes the main algorithmic/architectural bottleneck.
- **Change-level insight** (on each parent→child evaluation): modification type + observed performance effect, generated from parent fitness, child fitness, fitness delta, change summary, and evaluation report.
Distillation removes implementation-specific details while preserving reusable lessons (beneficial caching, pruning, vectorization, data-structure changes, redundant-computation reductions). Each insight is embedded for retrieval.

### Level 3: Semantic clusters (organization layer)
Insights grouped by embedding similarity: new insight joins nearest cluster if cosine ≥ τ_cluster (0.80), else starts a new cluster.
**Attention-weighted centroid** (the key non-parametric trick):
- Semantic centrality of member i: s_i = (1/(n−1)) Σ_{j≠i} cos(e_i, e_j)
- Attention weights: w_i = softmax(s_i / τ) with temperature τ = 0.10
- Representative: c = Σ w_i e_i (singleton → c = e_1)
- Low τ sharpens emphasis on prototypical insights; τ→∞ recovers mean pooling. Refreshed as members join; optional LLM summary captures the recurring optimization pattern (≤10 members).

## Retrieval (read-before-mutation)

1. Embed a query describing the current program and its observed issues.
2. Rank clusters by r_cluster = cos(e_q, c_k); keep top K_c = 3 clusters with r ≥ τ_ret (0.60).
3. Within each cluster, rank member insights by r_insight = cos(e_q, e_i); take top K_i = 3.
4. Keep cluster- and insight-level similarity scores SEPARATE (do not merge into one score).
5. Optionally attach up to 2 linked Level 1 traces per insight.
6. LLM synthesizes **3 concrete recommendations** (temp 0.2) from query + insight text + similarities + evidence, inserted into the diff or full-rewrite prompt.
7. **Fallback**: if no cluster passes threshold, use the original mutation prompt unchanged — no synthesis call.
8. Budget: retrieval capped at 2,500 tokens, constant as memory grows.

**Why it transfers**: retrieval is semantic, not genealogical — lessons carry across problems with similar failure modes even from different benchmark families.

## Results

- **20/20 model–harness–benchmark comparisons favor Sedima** (two-sided exact sign test, p = 1.9e-6; GPT-5.4, DeepSeek V4 Pro, Gemini 3 Pro, Qwen 3.7 Max, Qwen 3 Coder × OpenEvolve/ShinkaEvolve × AlgoTune/ALE-Bench LITE).
- +5.5% avg on AlgoTune (harmonic-mean speedup), +6.6% on ALE-Bench LITE at fixed 100-candidate budget.
- Largest gains for the weakest backbone (Qwen 3 Coder: +11.0%) — persistent guidance helps weak search most.
- **32.3% fewer iterations** on average to reach baseline-best (OpenEvolve, 5 backbones).
- **Transfer table** (memory provenance, eval problems fixed): cold 1.67/1113.7 → warm-same-benchmark 1.75/1187.8 (+4.8%/+6.7%) → warm-other-benchmark 1.70/1146.5 (+1.8%/+2.9%) — cross-family transfer is real but in-domain memory is stronger.
- **Random-retrieval control** ≈ no memory (1.62 vs 1.61): the gain comes from *relevant* retrieval, not prompt padding.
- Hyperparameters: cluster τ=0.80, retrieval τ=0.60, centroid τ=0.10, K_c=3, K_i=3; Qwen-Embedding-4B fixed across conditions; mutation temp 0.7, distillation/synthesis temp 0.2. Same backbone model does mutation AND memory ops (prevents stronger-model confound).

## Limitations (honest)

- Memory grows without bound — no consolidation/forgetting at scale.
- Inherits LLM bias/hallination: a wrong insight can amplify across runs.
- Step-reduction ≠ compute reduction (adds distillation + embedding + synthesis calls).
- Main tables are single-run (cost); per-step/ablation/transfer use 3 seeds.
- Not benchmarked against other memory-based evolutionary systems — establishes additive value over memoryless harnesses only.

## Reusable Patterns

1. **Two-hook memory interface**: any iterative optimizer can adopt persistent memory via (write-after-evaluate, read-before-propose) without touching its core loop.
2. **Evidence-linked distillation**: every abstract insight keeps a pointer to its raw trace — retrieved advice stays auditable.
3. **Problem-level vs change-level insights**: separate "what is the bottleneck" (once) from "what did this edit do" (every step).
4. **Attention-weighted centroids over similarity graphs**: non-parametric, no training — prototypical members dominate the cluster representative; temperature interpolates to mean pooling.
5. **Threshold-gated fallback**: retrieval that silently degrades to the original prompt when nothing clears threshold — keeps memory strictly additive.
6. **Separate provenance evaluation**: always report cold vs warm-same-domain vs warm-cross-domain to prove persistence AND transfer separately.

**Activation**: evolutionary search, LLM agent memory, insight distillation, cross-run transfer, semantic clustering, OpenEvolve, program synthesis, experience reuse, hypermutation guidance
