---
name: prr-speculate-reuse-repair-sparse-attention
description: "Predict-Reuse-Repair (PRR) runtime for accelerating dynamic sparse attention in long-context LLM decoding. Speculates attention over predicted KV blocks while selection is in flight, then incrementally repairs missed blocks. Reduces per-token decoding latency up to 40%."
tags: [sparse-attention, long-context, LLM-inference, speculative-execution, dynamic-sparse-attention, KV-cache, FlashAttention]
source: "arXiv:2606.30389"
trigger: "long-context LLM, dynamic sparse attention, DSA, KV block selection, attention latency, speculate-reuse-repair, PRR"
---

# PRR: Predict-Reuse-Repair for Dynamic Sparse Attention

## Problem
Dynamic sparse attention (DSA) accelerates long-context LLM decoding by attending to only top-K KV blocks per query, but introduces a serialized selection-to-attention dependency that becomes the new latency bottleneck.

## Core Methodology

### Three-Phase Runtime
1. **Predict** — Lightweight EMA-based predictor forecasts likely KV blocks for the current query based on temporal locality in DSA selections across decoding steps
2. **Speculate** — Begin attention computation over predicted blocks while the true selection is still in flight (profiling-guided speculation budget keeps speculative work off critical path)
3. **Repair** — Once true selected set is known, use FlashAttention-based repair kernel that folds missed blocks into partial attention state using online-softmax statistics (incremental update, not recomputation)

### Key Design Decisions
- **EMA predictor**: Tracks moving average of selected block indices across layers/heads; exploits that DSA selections show strong temporal locality across decode steps
- **Speculation budget**: Profile-guided; ensures speculative compute doesn't exceed what would be saved, keeping it off the critical path
- **Online-softmax repair**: Leverages the running max/sum statistics from FlashAttention to incrementally merge missed blocks without re-attending to already-processed blocks

## Implementation Pattern
```
For each decode step:
  1. predictor.predict(next_block_indices)  # EMA-based
  2. flash_attention_speculate(predicted_blocks)  # overlap with selection
  3. true_blocks = block_selector(query, kv_cache)  # actual DSA selection
  4. missed = true_blocks - predicted_blocks
  5. if missed: repair_kernel(partial_attn_state, missed_blocks)  # incremental merge
```

## Results
- Up to 40% reduction in per-token decoding latency
- Preserves downstream task accuracy (no approximation beyond original DSA)
- Works across multiple DSA methods and long-context benchmarks
- Code: https://github.com/Tianyu9748/Incremental_FlashAttention

## Pitfalls
- Speculation only helps when temporal locality is strong; random access patterns yield no speedup
- Repair kernel must correctly handle online-softmax state merging; incorrect max-tracking causes silent accuracy loss
- Profiling-guided budget must be recalibrated for different hardware (A100 vs H100 have different compute/memory ratios)

## Activation
sparse attention, long-context decoding, DSA, KV block prediction, speculative attention, FlashAttention repair, LLM inference optimization, PRR
