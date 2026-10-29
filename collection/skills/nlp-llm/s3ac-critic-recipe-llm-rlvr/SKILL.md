---
name: s3ac-critic-recipe-llm-rlvr
description: Use when long-CoT RLVR needs a trained value critic.
category: ai_collection
version: 1.0
author: hermes-dl-cron
license: MIT
trigger: RLVR critic training, long chain-of-thought actor-critic, value model pretraining, difficulty-aware prompt sampling, single rollout RL, GRPO alternative
arxiv: "2610.35518"
---

# S3AC — Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning

arXiv 2610.35518. Validated on dense 1.5B and MoE 35B/397B models.

## When to Use
Use when RLVR on long chain-of-thought reasoning needs token-level credit assignment, prompt-specific baselines, single-rollout training, or smarter prompt selection — i.e., whenever critic-free GRPO-family methods plateau or waste rollouts.

## Problem
RLVR for long CoT is dominated by critic-free methods because critic training is hard: (1) value pretraining data lacks coverage of long correct trajectories, (2) a newly initialized value head dominates early gradients and starves the backbone, (3) grouped rollouts waste compute on wrong-difficulty prompts.

## Setup
Token-level MDP: s_t = prompt + generated prefix; reward ±1 at the last token; γ=1.
Advantages via GAE: Â_t = Σ λ^l δ_{t+l}, δ_t = R_t + V(s_{t+1}) − V(s_t), V(s_T)=0.
Actor: CISPO surrogate J = Ê[sg(r̄_t·Â_t)·log π_θ(a_t|s_t)] with clipped importance weights treated as constants.
Critic: clipped squared-error value loss L = ½ Ê[max((V−R)², (V̄−R)²)] with V̄ clipped to V_old ± ε_v.

## Critic training recipe (core contribution)

1. **Coverage-oriented value pretraining**: pool trajectories from policies of DIFFERENT STRENGTHS (not just one initial policy) to cover diverse response lengths and outcomes. Two epochs, token-averaged MSE vs terminal returns; freeze attention layers; also freeze the MoE router.
2. **Value-head optimization**: initialize head weights with std = 1/(H+1) (H = hidden size); raise the critic gradient-clip threshold to 10 (vs the actor's 1) — for a linear head, ∇_w ℓ = e_t·h_t dominates early while the backbone sees ∇_h ℓ = e_t·w (tiny), so global clipping at 1 over-shrinks backbone updates.
3. **Online adaptation (two-timescale)**: critic LR = 5× actor LR; 2 critic epochs per rollout batch vs 1 actor epoch. Decouple GAE: critic regresses on MC returns (λ_critic=1); actor uses VAPO length-adaptive λ_actor = 1 − 1/(αT), α=1.5.

## DAPS — Difficulty-Aware Prompt Sampling
Pre-generation prompt selection (DAPO dynamic sampling discards only AFTER generation):
- Critt prior: p_c = clip((V(s_0)+1)/2, 0, 1) — success-probability estimate under ±1 reward; needs no offline difficulty calibration rollouts
- Blend with observed outcomes: p̂ = (S + n_c·p_c)/(N + n_c); counts decay as the policy evolves
- Acceptance: a = a_min + (1−a_min)·4p̂(1−p̂) — peaks at intermediate difficulty p̂=0.5, positive floor keeps ε-greedy exploration; phased in after an initial uniform-sampling period

## Results
- Intern-S2-397B group rollout (step 1200): GPQA-D 90.5 vs GRPO-X 88.9; 5-benchmark avg 87.3 vs 85.1
- Qwen2.5-Math-1.5B / R1-Distill-1.5B: beats GRPO-X on MATH500/AMC23/AIME25/Olympiad/Minerva
- At 35B: sustains SINGLE-ROLLOUT (K=1) training while critic-free baselines deteriorate — the critic supplies both token advantages and the prompt baseline
- Critic values track held-out MC returns; long failures (>20K tokens) get near-zero mean advantages on hard prompts vs below −1 on easy ones

## Reusable patterns
1. Multi-strength pretraining pools for value models — coverage beats raw scale (vs SAO's larger single-policy corpora; vs VC-PPO's fixed policy).
2. Head-vs-backbone gradient asymmetry fix — higher clip threshold for a freshly attached linear head plus small init; applies to any new head on a pretrained backbone.
3. Decoupled actor/critic GAE — MC targets for the critic, length-adaptive λ for the actor.
4. Critic reuse for data selection — initial-state value as a difficulty prior for prompt sampling.

## Related
GRPO-X, VC-PPO, SAO, FlashREINFORCE, REINFORCE++, CISPO, IcePoP token masking, MIS sequence-level masking, VAPO length-adaptive GAE
