---
name: graph-augmented-tree-search-agent-planning
description: GATS - eliminate LLM calls during agent planning by combining UCB1 tree search with a layered world model (exact symbolic match / learned statistics / LLM-for-unknown). Deterministic, zero-variance plans, 100% success on stress tests vs LATS/ReAct. Use when building LLM-agent planners that are too slow/costly/stochastic from in-loop LLM inference.
---

# GATS — Graph-Augmented Tree Search (from arXiv:2607.08894)

Planning framework that gets LLM-class planning success **without calling the LLM during
inference**. Combines systematic UCB1 tree search with a three-layer world model.

## When to use
- LLM-agent planning (LATS, ReAct) is too slow / expensive / non-deterministic in production.
- You need deterministic, reproducible plans (zero variance across runs).
- You have (or can build) an environment model or execution logs to learn from.

## Core architecture
Replace in-loop LLM next-action prediction with:
1. **UCB1 tree search** over the action space (systematic exploration, not sampling).
2. A **layered world model** that predicts outcomes WITHOUT an LLM call:
   - **L1 — Exact symbolic action matching**: known actions → deterministic lookup (fast path).
   - **L2 — Statistics learned from execution logs**: empirical success/transition distributions.
   - **L3 — LLM-based prediction**: used ONLY for genuinely unknown actions (cold start).
3. LLM is invoked at most during L3 (rare once L2 is populated); after warm-up, inference uses zero
   LLM calls.

## Implementation steps
1. Define the action space and a simulator / replayable execution log.
2. Build L1 as a deterministic rule/lookup table for actions with known effects.
3. Populate L2: mine execution logs → (state, action) → outcome frequency table; smooth with
   Laplace / Bayesian prior.
4. L3: route to an LLM only when L1+L2 have no confident prediction; cache the result back into L2.
5. Run UCB1 over the tree: `UCT = Q(a) + c·√(ln N_parent / N_a)`, expand using the world model, prune
   dead-ends (branching paths that L2/L3 mark as failing).
6. Return the highest-value path as the plan.

## Results (paper)
- 100% success vs LATS 92% / ReAct 64% on synthetic; 100% vs LATS 88.9% / ReAct 23.9% on 12-scenario
  stress test (coding, web nav, long-horizon).
- **Zero LLM calls per task during planning** (vs 37 for LATS); zero variance across runs.

## Pitfalls
- World-model quality dominates; bad L2 statistics → tree search optimizes the wrong thing. Validate
  L2 coverage before trusting plans.
- Cold-start (empty L2) degrades to L3 cost — seed L2 from any available logs first.
- UCB1 exploration constant `c` needs tuning; too high → wasted expansions, too low → premature
  convergence to a suboptimal deterministic plan.
- Environment non-stationarity: re-mine L2 periodically or plans rot.

## Verification
- Compare success rate, LLM-calls/task, and run-to-run variance vs LATS/ReAct on the same tasks.
- Report plan determinism (std dev across N runs = 0 target).
