---
name: clipping-bottleneck-nsr
description: Near-boundary Stochastic Rescue (NSR) for stabilizing RLVR/GRPO training via stochastic recovery of clipped signals
---

# Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary Signals

**arXiv: 2605.22703** | Submitted 21 May 2026

## Core Concept

Reinforcement Learning with Verifiable Rewards (RLVR) training for LLMs (e.g., GRPO) suffers from instability due to **hard clipping** — the rigid rule that discards tokens whose probability ratio falls outside the [1-ε, 1+ε] clipping range. This paper identifies that **informative signals often lie just beyond the clipping boundary**, and discarding them creates a training bottleneck.

## Key Methodology: Near-boundary Stochastic Rescue (NSR)

NSR is a minimal, plug-and-play modification to GRPO-style objectives:

1. **Detection**: Tokens whose probability ratio is slightly out of bounds (beyond but near the clipping threshold) are identified.
2. **Stochastic Recovery**: Instead of hard-clipping these tokens, NSR stochastically retains a fraction of them via a Bernoulli sampling process at the boundary.
3. **Implicit Effect**: In expectation, NSR induces a smooth gradient decay near the boundary rather than a hard cutoff.

### Key Insight

NSR can be interpreted as inducing implicit gradient decay in expectation, but empirical ablations show that the **stochastic, boundary-local rescue mechanism** is consistently more effective than deterministic gradient decay.

## Implementation Points

- Plug-and-play: requires only modifying the clipping logic in GRPO-style objectives
- Works across model sizes (7B to 30B) and architectures (dense and MoE)
- Validated against strong baselines: DAPO, GSPO
- No additional training overhead beyond the stochastic sampling step

## Application Scenarios

- LLM post-training with RLVR/GRPO
- Any clipped policy gradient method where signal-to-noise ratio near boundaries is important
- Stabilizing long-chain reasoning training

## Activation Keywords
- NSR, near-boundary stochastic rescue
- GRPO clipping bottleneck
- RLVR stabilization
- hard clipping vs stochastic recovery