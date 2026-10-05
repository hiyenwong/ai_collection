---
name: tah2-adaptive-looped-transformer
version: v1.0.0
last_updated: 2026-09-30
description: "TaH2 methodology — per-token adaptive loop depth for test-time scaling, trained via lookahead depth supervision with online labels (does another iteration improve this token?). Use when: (1) looped transformers waste compute on easy tokens, (2) extending test-time scaling slope beyond fixed-depth looping, (3) deciding iteration depth per token at decode. Keywords: adaptive loop depth, test-time scaling, looped transformer, iteration decider, lookahead supervision."
arxiv_id: "2609.35748"
authors: "Yichen You, Tianyu Fu, Aosong Feng et al. (7 authors)"
tags: [looped-transformer, test-time-scaling, adaptive-compute, decoding, efficiency]
---

# TaH2: Token-Adaptive Depth for Looped Transformer Test-Time Scaling

From arXiv:2609.35748 (2026-09-28). Code: https://github.com/thu-nics/TaH

## Problem

Looped transformers reuse one block for extra latent computation — great for test-time scaling (accuracy per doubling of decode FLOPs). But:

1. Existing looped models have **steeper accuracy-compute slopes** than non-looped baselines, yet **underperform at matched compute** — fixed-depth looping spends iterations on *every* token.
2. Many tokens **don't benefit** from extra iterations at all.

## Core Idea: A Per-Token Iteration Decider, Trained with Online Labels

**TaH2** joint-post-trains (1) the looped backbone and (2) a lightweight **iteration decider** that chooses, per token, whether to run another loop pass.

**Lookahead depth supervision** generates the decider's labels *online* during training:
- For each token, run the extra iteration and check: **does the prediction improve?**
  - yes → label "iterate again" for this token
  - no → label "stop"
- These online labels are cheap (the extra pass is already computed during training) and directly target the test-time objective.

The decider focuses extra compute only where looping pays off — raising both the **slope** and the **peak** of test-time scaling.

## Implementation Sketch

```
for each token position i:
    h = backbone_block(h)                 # pass 1 (always)
    while decider(h_i) says "go" and d < D_max:
        h = backbone_block(h)            # extra pass for THIS token only
        # during training: label decider with lookahead ground truth
        #   label = 1[next_pass_improves_prediction_i]
```

- Decider: small head on the token's latent state → binary (or depth-budget) decision.
- Joint post-training of backbone + decider is essential: decider-only tuning drifts from backbone behavior.

## Key Results (AIME benchmarks)

| Metric | Result |
|---|---|
| Accuracy-compute slope | 2.74 vs 1.79 non-looped (+53%) |
| Peak accuracy @ matched compute | +3.4 pts over non-looped baseline |
| Gain vs baseline by max depth | +2.8 pts (depth 2) → +3.9 pts (depth 8), keeps growing |

Fixed-depth looped models plateau as depth budget grows; TaH2's advantage **widens** with depth — the decider converts a depth budget into a accuracy gain.

## When to Use

- Deploying looped transformers for inference-time scaling (math/code reasoning).
- Compute budgets where fixed-depth looping is wasteful (mixed-difficulty token streams).
- Any "how many refinement steps does this input need?" setting — the lookahead-supervision recipe (label = does-one-more-step-help) generalizes beyond transformers.
