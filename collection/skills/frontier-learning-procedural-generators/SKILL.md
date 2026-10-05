---
name: frontier-learning-procedural-generators
version: v1.0.0
last_updated: 2026-09-30
description: "Frontier Learning methodology — open-ended RL post-training that generates informative problems online via procedural generators, using a regret signal to search the generator parameter space at the edge of the model's evolving capability. Use when: (1) fixed training pools go stale as the policy improves, (2) GRPO gets no signal from too-easy/too-hard problems, (3) designing curricula for reasoning RL. Keywords: open-ended learning, procedural generation, regret-driven curriculum, capability frontier, reasoning RL."
arxiv_id: "2609.35426"
authors: "Robin Faro, Shyam Sundhar Ramesh, Ilija Bogunovic, Aurelien Lucchi"
tags: [rl-post-training, curriculum, procedural-generation, grpo, reasoning]
---

# Frontier Learning: Training LLM Reasoners at the Edge of Capability

From arXiv:2609.35426 (2026-09-28).

## Problem: Fixed Pools Go Stale

RL post-training (GRPO) learns only when rollouts on a problem **mix successes and failures**. With a fixed problem pool:

- Problems near the model's ability get solved → gradient signal dies.
- The "useful band" of any fixed pool **shrinks as the model improves** — the pool stales quickly.
- Result: most of training computes zero-advantage rollouts.

## Core Idea: Generate Problems Online at the Frontier

**Frontier learning** replaces the fixed pool with **procedural generators** invoked *during* training:

1. Treat the generator's **task-specific parameters as a search space** (difficulty knobs, instance structure).
2. Use a **regret signal** to prioritize generator configurations at the **edge of the model's current capability** — where success probability is neither ~0 nor ~1.
3. Continually re-target as the policy evolves: today's frontier is tomorrow's warm-up.

This is open-ended post-training: the curriculum is not a schedule but a **feedback loop** keyed to measured difficulty.

## Implementation Pattern

```
loop:
    1. propose generator config θ ~ prioritized (by regret estimate over θ-space)
    2. instantiate problem batch x = G(θ)
    3. roll out policy π on x → per-problem success rate p̂
    4. GRPO update on x (signal exists only where 0 < p̂ < 1)
    5. update regret/difficulty model of θ-space:
       - p̂ ≈ 0 or 1 → deprioritize θ (off-frontier)
       - 0 < p̂ < 1  → boost θ and its neighborhood (frontier)
```

- The difficulty model can be a simple bandit/surrogate over generator params — no need for a learned simulator.
- Regret framing: prioritize θ where the *expected learning signal* (advantage variance) is highest.

## When to Use

- Reasoning RL where you can parameterize task generation (math templates, code specs, logic puzzles, synthetic agentic tasks).
- Fixed pools exhausted / plateaued mid-training (loss of GRPO signal is the symptom).
- Anytime a verifier exists for generated instances — the verifier closes the loop that makes procedural generation safe.

## Key Results

Across several reasoning tasks and model families: **consistent higher relative gains over fixed-pool baselines**. Effective post-training requires not just *selecting* useful problems but **continually generating them at the edge of capability**.

## Design Notes

- This is the RL analogue of "hard negative mining", lifted to problem synthesis.
- Works because GRPO's advantage is zero on uniformly-solved or uniformly-failed problems — frontier targeting maximizes non-zero advantage density.
- Practical requirement: a **verifiable** generated task. Without a verifier, frontier difficulty cannot be measured.
