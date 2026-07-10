---
name: defermem-evidence-distillation
description: "DeferMem methodology from arXiv:2605.22411 (May 2026). Long-term memory QA framework using query-time evidence distillation via RL (DistillPO): high-recall candidate retrieval + query-conditioned evidence rewriting with decomposed-and-gated reward. Use when: long-term memory QA, RAG with long conversations, RL-based evidence distillation, memory systems for LLM agents."
---

# DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

**Paper:** arXiv:2605.22411 (May 2026)

## Overview

DeferMem is a long-term memory framework for LLM-based agents that addresses a fundamental tension in memory-augmented QA: retrieving too much context drowns the model in noise and token budgets, while retrieving too little misses critical evidence. DeferMem decouples memory into two distinct phases:

1. **High-recall candidate retrieval** — cast a wide net across raw history using a lightweight structural index
2. **Query-conditioned evidence distillation** — an RL-trained *memory distiller* selects and rewrites the noisy candidates into concise, faithful, self-contained evidence that directly answers the query

The key insight is that *raw retrieval can be coarse and high-recall* (cheap, broad) while the burden of precision is shifted to a *trainable distillation step* that produces clean evidence for the downstream LLM. This mirrors "deferred" computation — hence the name DeferMem.

## Segment-Link Structure

The raw conversation history is organized into a lightweight **segment-link** structure:

- The conversation is divided into **segments** — contiguous blocks of dialogue turns (typically 2–8 turns each).
- **Links** are bidirectional edges between segments, weighted by semantic or temporal adjacency (e.g., discourse continuity, topic shift detection, timestamp proximity).
- The segment-link graph is built **offline** during conversation ingestion and updated incrementally as new history arrives.
- At query time, **spreading activation** starting from the last few segments traverses the link graph to retrieve a broad candidate set (typically 50–200 segments) — intentionally sacrificing precision for high recall.
- This structure is lightweight compared to full vector-database indexes: segments are plain text with metadata, links are sparse edges, and no dense embeddings are stored persistently.

## Dual-Phase Workflow

### Phase 1: Candidate Retrieval (High-Recall, Zero-Learning)
1. Identify the most recent N segments as seed nodes in the segment-link graph.
2. Run spreading activation with decaying relevance scores across link hops (1–3 hops, configurable).
3. Collect all activated segments as the raw candidate pool (targeting recall >95% on held-out queries).
4. No learned ranking or dense retrieval — just structural graph traversal.

### Phase 2: Evidence Distillation (RL-Trained, Query-Conditioned)
1. The raw candidates + the user query are fed into the **memory distiller** (a lightweight transformer, e.g., 7B–8B parameters).
2. The distiller produces structured output: a selected subset of messages + optionally rewritten evidence text.
3. The evidence is appended to the context window of the downstream LLM for final answer generation.
4. The distillation is done at **query time** — the distiller runs once per query, not during ingestion.

## DistillPO Algorithm

DistillPO (Distillation Policy Optimization) is the RL algorithm used to train the memory distiller. It formulates post-retrieval evidence distillation as a structured RL problem.

### Structured Action Space

Each action consists of two components:

- **Message Selection (`a_sel`):** A binary mask over retrieved candidates, choosing which raw messages to keep (filtering out noise, redundancy, and irrelevant context).
- **Evidence Rewriting (`a_rw`):** An optional rewrite step that condenses, paraphrases, or reformulates the selected messages into self-contained evidence that directly answers the query. The distiller can choose to pass through verbatim (no rewrite) when the selected messages are already suitable.

The combined action is `a = (a_sel, a_rw)`, allowing the distiller to both *filter* and *reshape* retrieved content.

### Decomposed-and-Gated Reward Pipeline

The reward signal is decomposed into three components, each assessing a distinct quality dimension:

| Reward Component | Symbol | Assesses |
|---|---|---|
| **Faithfulness** | `R_faith` | Whether the distilled evidence is factually consistent with the source segments (using an NLI-based verifier) |
| **Answerability** | `R_ans` | Whether the distilled evidence, when given to the downstream LLM (frozen decoder), enables a correct answer to the query |
| **Conciseness** | `R_conc` | Token efficiency — penalizes unnecessarily long evidence relative to a budget |

The gated combination is: 

```
R = g_faith * R_faith + g_ans * R_ans + g_conc * R_conc
```

Where `g_* ∈ {0, 1}` are gating signals. The gates are computed heuristically: `g_faith = 1` always; `g_ans = 1` if `R_faith` exceeds a threshold (no point rewarding answerability if evidence is unfaithful); `g_conc = 1` only when both previous gates are active and the evidence length exceeds the budget. This **deferred gating** ensures that reward components only activate when prerequisite quality dimensions are satisfied, preventing the distiller from gaming the system (e.g., producing concise-but-wrong evidence).

### Advantage Assignment & Training

- Trajectories are collected by running the distiller on training queries paired with ground-truth answers.
- The reward model (frozen downstream LLM + NLI verifier) scores each distillation output.
- **Advantage** is computed per action step using a learned value baseline (a small MLP over distiller hidden states), following a REINFORCE-with-baseline setup.
- The policy gradient objective maximizes the expected advantage:

  ```
  ∇J(θ) = E[ A(s, a) · ∇θ log π_θ(a|s) ]
  ```

- Ties are broken behaviorally: when no candidate is clearly superior, the distiller learns to prefer conciseness via the gated reward structure.

## Key Results

Reported on long-context QA benchmarks (e.g., LongBench, NarrativeQA, and an internal multi-session conversation dataset):

| Metric | DeferMem | Best Baseline | Δ |
|---|---|---|---|
| **QA Accuracy (F1)** | **73.4%** | 68.1% (Full-Context) | +5.3 pp |
| **QA Accuracy (EM)** | **61.2%** | 55.8% (RAG-50) | +5.4 pp |
| **Evidence Token Budget** | **~1,200 tokens** | ~8,000 tokens (Full-Context) | **6.7× reduction** |
| **End-to-End Latency** | **1.2×** | 1.0× (no memory) | only 20% overhead |
| **Distillation False Positives** | **↓ 62%** | — | vs. Frozen RAG |

Key findings:
- DeferMem matches or exceeds the accuracy of *full-context* approaches while using ~15% of the tokens.
- The segment-link retrieval achieves 96% recall on evidence-containing segments across held-out queries.
- DistillPO-trained distiller significantly outperforms supervised-finetuning (SFT) baselines for evidence distillation, especially on the faithfulness and conciseness axes.
- The decomposed reward structure is critical: ablating any single component degrades accuracy by 2–6 pp.
- The gating mechanism prevents reward hacking: without gating, the distiller learns to produce miniaturized-but-wrong evidence that exploits conciseness rewards.

## When to Use DeferMem / DistillPO

- **Long-term memory QA:** Systems where an agent accumulates conversation history over extended sessions (days/weeks) and needs to answer queries grounded in that history.
- **RAG with long conversations:** Standard RAG breaks down with hundreds of conversation turns due to embedding drift and token limits; DeferMem's segment-link structure handles it more naturally.
- **Evidence distillation as a learned skill:** When you want to train a model to condense retrieved context specifically for downstream task performance, rather than using generic summarization.
- **RL for retrieval/reranking pipelines:** DistillPO's decomposed reward and gating approach is transferable to other RL-for-retrieval settings (multi-hop QA, tool-use memory, etc.).

## Activation Keywords

DeferMem, DistillPO, evidence distillation, query-time distillation, long-term memory QA, memory system, segment-link graph, spreading activation, reinforcement learning for retrieval, decomposed reward, gated reward, post-retrieval distillation, RL for RAG, evidence selection, evidence rewriting, conversational memory, multi-session QA, high-recall retrieval, query-conditioned distillation, REINFORCE with baseline, faithful evidence generation, memory distiller, structured action space, NLI-based faithfulness verification, deferred computation, learning to distill retrieval.
