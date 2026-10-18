---
name: hindsight-privileged-rlvr
description: Use when RLVR needs token credit without group sampling.
---

# Hindsight-Privileged RLVR (HP-RLVR)

Source: arXiv:2610.20497 (Chen, Wu, Xu, Zhang, Zeng, Wang, Yang, et al. — "Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling", v2, 15 Oct 2026)

## Activation
- single rollout RLVR, GRPO all-same reward, group sampling cost, hindsight conditioning, JSD token weight, historical reward centering, G=1 training, token credit assignment, failed trajectory negative credit

## Problem
GRPO derives its baseline from group rewards; with G rollouts per prompt: (a) homogeneous outcomes (all-pass/all-fail) → zero advantage, wasted sampling (Pr(all-fail) = (1−p0)^n); (b) trajectory-level advantage broadcast to all tokens leaves credit coarse. HP-RLVR sets **G=1** and builds token credit from the trajectory's own realized future.

## Method (3 components)

1) **Historical reward centering (trajectory evaluation)** — Lemma (historical baseline invariance): any H_k-measurable baseline b_k ∈ [0,1] held fixed at differentiation gives E_k[(R−b_k)·g_θ] = ∇J_RLVR(θ) — an unbiased single-trajectory estimator. Choose b_k = mean reward of EARLIER completed trajectories C_k (current batch enters the history only AFTER advantages are built); s_i = R_i − b_k. Failures below baseline get negative credit; b_init ∈ [0,1] when history empty.

2) **Hindsight-conditioned scoring (local allocation)** — freeze the generating policy snapshot; for each eligible generated position j with causal history h_j, score two full-vocabulary distributions:
   - p_j = π_θold(·|h_j) — causal view
   - q_j = π_θold(·|h_j, F_j, O) — hindsight view: F_j = allowed future from the SAME trajectory, EXCLUDING the scored token y_j; O = textual verifier report rendered by a task adapter (e.g. "the solution passed 7 of 10 tests") — restates the report, no independent correctness judgment
   - Multi-turn agents: scoring turn t uses transitions from (action_{t+1}, observation_{t+2}) onward — excludes the immediate observation that would trivially reveal the current action. Hindsight is training-only privilege; never available at rollout generation or deployment.

3) **Token weight** — w_j = JSD(p_j, q_j)/log2 ∈ [0,1], JSD = ½KL(p‖m)+½KL(q‖m), m=(p+q)/2. Vanishes iff causal and hindsight views agree (token's information already in h_j); w_j=1 iff disjoint supports. **Bounded credit**: A_j = (R_i−b_k)·w_j with 0≤w_j≤1, so |A_j| ≤ |R_i−b_k| ≤ 1 — hyperparameter-free cap. A_j = 0 exactly when R_i = b_k or p_j = q_j.

Training objective: PPO-style clipped surrogate ℓ_j = min(r_jA_j, clip(r_j, 1−ε, 1+ε)A_j), r_j = π_θ(y_j|h_j)/π_θold(y_j|h_j), ε=0.2, one epoch; hindsight context/prompt/observations excluded from policy loss; advantages detached; trajectory-balanced reduction (per-trajectory row weights N_it/N_i sum to 1; effective trajectory weight must be uncorrelated with turn/token counts).

## Results (Qwen3-1.7B/4B/8B, LoRA r64 α128, 100 steps, 8×Ascend 910B)
- Speed at shared prompt/step budget vs GRPO(G=8): **1.21× faster (math), 1.46× (code), 2.30× (ALFWorld; saves 255.8 NPU-hours)** using 1/8 the rollouts per prompt.
- Math Avg@12 (AIME24/25+HMMT25): HP-RLVR ahead at all 3 sizes (+1.1 to +2.7 pts: 38.90/62.32/65.73 vs 37.80/60.09/63.07). GRPO ahead on LiveCodeBench Pass@1 (38.87 vs 40.65 @8B) and ALFWorld (62.45 vs 65.32).
- Training-signal availability: **43.2% (4B) / 49.0% (8B) of GRPO's gradient-norm records are ZERO in ALFWorld vs NONE for HP-RLVR** — the all-same-reward starvation is real and this eliminates it.
- Authors' caveat: frontier describes measured configs only; does not establish statistical superiority or isolate estimator effects across hardware/budgets; single training seed. Honest limitation — treat as "signal availability + cost" win, not accuracy win.

## When to Use
- Sparse terminal rewards with homogeneous outcomes (agent/ALFWorld-style tasks) — biggest win: no zero-gradient steps.
- Rollout-expensive settings (long/multi-turn trajectories, 50-turn envs): G=1 removes the ×G rollout cost; extra hindsight scoring = 2 forward passes over the same completed trajectory, O(T) stored weights + O(CV) divergence (C positions per group, V vocab) — far cheaper than G−1 extra rollouts.
- Keep GRPO when response-level exploration variance IS the learning driver (code tasks where GRPO won here).

## Implementation Pitfalls
- F_j must exclude the scored token y_j; hindsight context removed at deployment (training-only).
- JSD over the FULL vocabulary (no top-k approximation), computed in groups of ≤C positions to bound memory.
- Record generation-time log-probs during rollout for the ratio denominator; replay-check at first update and abort on mismatch (ratio-bias guard).
- Historical baseline must enter history only AFTER advantages are constructed (else biased).
- Multi-turn: retain h_j as observation-action history (e.g. 8-turn retained), score with 8192-token training context.

## Related skills
- Complements [[categorical-critics-llm-reinforcement-learning]] (critic-based credit). Competes with [[oppo-token-credit-assignment]] / [[delta-discriminative-token-credit-assignment]] (group-sampling token credit) and [[rc-opd-root-cause-repaired-distillation]] (repaired on-policy distillation). Different paper from [[prospective-hindsight-self-calibrating-rl]] (arXiv:2610.02740).