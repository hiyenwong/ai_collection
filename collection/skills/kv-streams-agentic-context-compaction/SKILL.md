---
name: kv-streams-agentic-context-compaction
version: v1.0.0
last_updated: 2026-09-30
description: "KV-streams methodology — streaming the KV cache forward across compaction events instead of flushing it, for trainable constant-memory long-context agentic RL. Use when: (1) context compaction forces re-prefill and kills training throughput, (2) compaction loses long-range info the policy still needs, (3) agent RL traces overflow GPU memory. Keywords: KV cache streaming, context compaction, agentic RL, recurrent state, training throughput."
arxiv_id: "2609.35750"
authors: "Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda et al. (18 authors)"
tags: [kv-cache, compaction, agentic-rl, long-context, efficiency]
---

# KV-streams: Streaming KV Cache Across Compaction for Agentic RL

From arXiv:2609.35750 (2026-09-28).

## Problem

Long-horizon agentic LLM RL is memory-bound: full traces must fit in GPU memory, so **context compaction** (summarize/drop old tokens) is the standard fix. But every compaction event invalidates the KV cache → the model must **re-prefill** the compacted context from scratch, many times per trace. This destroys training throughput (prefill dominates wall-clock).

## Core Idea: Don't Flush the KV Cache — Stream It

**KV-streams**: on each compaction, instead of discarding the KV cache, **stream it forward** — carry the KV entries of retained tokens (plus a compacted summary of dropped ones) into the next segment's cache. The cache becomes a persistent object across compaction boundaries.

Three properties:

1. **Plug-and-play**: compatible with *any* compaction strategy (drop-based, summarization-based, hybrid). The change is in the training/serving plumbing, not the compaction policy itself.
2. **Throughput**: 2.6–5× wall-clock speedup in RL training across 3 compaction strategies, no evidence of performance degradation.
3. **Emergent recurrent state**: the streamed KV cache acts as a *recurrent hidden state*, carrying forward information that has long since disappeared from the visible context. Key finding: **RL alone (no auxiliary losses) suffices** for the model to learn to use this hidden channel — contrary to prior work that added explicit memory objectives.

## Implementation Pattern

```
segment_i: tokens t0..tk  → KV cache C_i
compaction at t=k: context c_i → c_{i+1} (any policy)
    naive: flush C_i, re-prefill c_{i+1}          # O(len(c_{i+1})) every step
    KV-streams: C_{i+1} = stream(C_i, c_{i+1})    # retain survivors' KV +
                                                 # compressed representation of dropped KV
segment_{i+1}: continue generation from C_{i+1}
```

- **Retention rule**: entries for tokens kept by the compaction policy are carried **as-is** (positional encoding re-based). Dropped tokens' contributions are folded into a small summary state.
- **Training**: works under standard policy-gradient RL (GRPO-style); no architecture change required. Backward through the stream uses cache checkpointing at segment boundaries.

## When to Use

- Agentic RL where traces exceed context/memory (tool-use, browsing, multi-turn tasks).
- Any pipeline that re-prefills after compaction (the throughput win alone justifies it).
- When you suspect the policy *needs* older context that compaction visibly deletes — the streamed cache preserves it implicitly, and RL will exploit it if useful.

## Key Results

| Setting | Result |
|---|---|
| Training throughput (3 compaction strategies) | 2.6–5× wall-clock speedup |
| Performance vs naive compaction | no evidence of degradation |
| Hidden-state emergence | RL training alone → cache used as recurrent state |

## Design Notes

- The "recurrent state" finding matters beyond efficiency: it implies **compaction need not be lossless** — the KV stream is a learnable memory the policy gradient can shape.
- Prefer streaming retention rules that keep KV entries *exact* for survivors; compressing survivors too hurt in ablations.
- Position re-basing across segments must be consistent, or the model conflates relative position with compaction boundaries.
