---
name: sdar-self-distilled-agentic-rl
description: >
  Self-Distilled Agentic Reinforcement Learning (SDAR) methodology.
  Stabilizes on-policy self-distillation (OPSD) for multi-turn LLM agents by
  treating distillation as a gated auxiliary while keeping RL as the primary backbone.
  Maps detached token-level signals into a sigmoid gate, strengthening distillation on
  positive-gap tokens and attenuating negative teacher rejections. Use when designing
  RL post-training for LLM agents, combining OPSD with GRPO/PPO, or addressing
  multi-turn distillation instability.
  Activation: self-distilled agentic RL, SDAR, on-policy self-distillation, OPSD,
  multi-turn RL agent, agent RL, gated distillation, GRPO agent, token-level RL
---

# Self-Distilled Agentic RL (SDAR)

## Core Idea

RL trajectory-level rewards give only coarse supervision for long-horizon agent tasks.
On-Policy Self-Distillation (OPSD) provides dense token-level guidance from a teacher
branch with privileged context, but naive RL+OPSD for multi-turn agents suffers from
compounding instability and asymmetric treatment of teacher rejections.

SDAR resolves this by treating OPSD as a **gated auxiliary objective** while keeping
RL as the primary optimization backbone.

## Key Mechanism

1. **Token-level signal detachment**: OPSD produces per-token advantage signals
2. **Sigmoid gating**: Maps detached signals through σ(·) to produce a gate g_t ∈ (0,1)
3. **Positive-gap strengthening**: When teacher signal > student signal, gate approaches 1,
   amplifying distillation loss
4. **Negative rejection attenuation**: When teacher rejects (negative gap), gate approaches 0,
   softly suppressing potentially noisy teacher guidance from imperfect skill retrieval

## Loss Function

```
L_total = L_RL + λ · g_t · L_distill
```

Where g_t = σ(α · Δ_t) with Δ_t being the teacher-student token-level gap.

## Advantages Over Naive RL+OPSD

- Avoids instability from naive loss addition (GRPO+OPSD diverges)
- Outperforms hybrid RL-OPSD baselines across model scales (Qwen2.5, Qwen3)
- +9.4% on ALFWorld, +7.0% on Search-QA, +10.2% on WebShop-Acc vs GRPO

## When to Use

- RL post-training for multi-turn LLM agents (ALFWorld, WebShop, Search-QA style tasks)
- Combining dense token-level distillation with trajectory-level RL rewards
- Mitigating instability in on-policy self-distillation for agentic tasks
- Skill-conditioned privileged guidance where teacher may reject imperfectly
