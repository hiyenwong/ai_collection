---
name: router-drift-control-moe-rl
description: "Use when RL-training MoE LLMs. Filter router-drift data."
category: reinforcement-learning
---

# Router Drift Control (RDC): Mitigating Off-Policy Degradation in MoE RL

Source: arXiv:2610.21682 (Liangyao Jin, Zhixin Wang, Liming Liu, et al. — PKU, Shanghai Innovation Institute, Infrawaves; Oct 2026, v2). Response-level filtering of high router-drift samples for Mixture-of-Experts LLM reinforcement learning. Qwen3-30B-A3B on DAPO-Math-17K (GRPO + DAPO Clip-Higher): in asynchronous training, RDC+TIS improves average peak accuracy on AIME24/25 by +5.5 pts over TIS and +4.5 pts over R3 routing replay.

Use when: RL post-training (GRPO/PPO-style) a sparse MoE LLM where rollout generation and policy optimization run on separate engines — asynchronous training, sequential mini-batch updates, or FP8-vs-BF16 engine mismatch — and routing decisions drift between rollout and training.

## Problem: router drift

Three off-policy sources: (1) training-inference mismatch (different precision/kernels/parallelism → different token probabilities under identical weights); (2) mini-batch sequential updates (later mini-batches increasingly stale); (3) asynchronous rollout-training overlap (policy lag). In MoE, tiny policy differences flip top-k expert choices: the same token is routed to DIFFERENT experts during rollout vs training. Routing determines gradient support — an expert not selected receives no direct gradient through that layer — so routing mismatch silently redirects which parameters learn from each token.

Why existing fixes fall short:
- Probability-space corrections (TIS, CISPO, GSPO, GMPO, CTPO, SIS, TRM) reweight/mask via token likelihood ratios — they see distribution shift but NOT computation-path changes.
- Routing replay (R2/R3, Ma et al. 2025) reuses rollout-time expert selections in the training forward pass. This enforces routing consistency but INTRODUCES GRADIENT BIAS: it omits contributions from experts that the CURRENT training router selects but the rollout router did not — biased gradient attribution relative to native routing.

## Method (RDC)

1. **Expert-usage distribution** per layer l, per response y, per engine a ∈ {µ=rollout, π=training}: u_l^a(e|y) = (1/TK) Σₜ 1[e ∈ R_l^a(t)] — the fraction of the response's T·K expert selections assigned to expert e.
2. **Layer distance**: d_l(y) = ½‖u_l^µ(·|y) − u_l^π(·|y)‖₁ (total variation between the two usage histograms).
3. **Response-level drift score**: D_route(y) = (1/L) Σ_l d_l(y) ∈ [0,1] — aggregate expert-usage shift across the response.
4. **Selective filtering**: rank responses by D_route WITHIN LENGTH BUCKETS (scores are not comparable across very different lengths) and filter the top ⌈q·|B_b|⌉ per bucket; filtering ratio q = 0.08 default.
5. **Objective**: L_RDC(θ) = (1/N_B) Σ_y m_B(y)·ℓ_θ(y; R^π(y)) — retained responses use their NATIVE training routes (no replay, no gradient bias); m_B is the keep-mask. Recompute routing scores and the mask before EVERY mini-batch update with the current policy.
6. **Composition**: RDC (routing space) + TIS (probability space) are complementary and stack — the paper's best async setting is GRPO+TIS+RDC.

Training routes R^π come from teacher-forcing the sampled response under the current policy — collectible during the training forward pass, so drift statistics cost only E-dimensional histogram bookkeeping per layer.

## Results

- Setup: Qwen3-30B-A3B, DAPO-Math-17K, GRPO baseline with DAPO Clip-Higher (ε_low=0.2, ε_high=0.27); eval AIME24, AIME25, MATH-500; q=0.08.
- Gains GROW with policy staleness: RDC helps most in asynchronous training where drift is largest, and remains effective in synchronous settings.
- Async: GRPO+TIS+RDC beats GRPO+TIS by +5.5 and GRPO+R3 by +4.5 average peak on AIME24/25, with stable training dynamics.

## Implementation notes

- Only changes WHICH responses join each update — orthogonal to loss shaping, importance ratios, and replay strategies; safe to combine with any of them.
- Filter ratio q: 0.08 default; too large discards learning signal, too small misses drift.
- Recompute per mini-batch: drift is measured against the CURRENT training policy, so stale masks defeat the mechanism.
- Length-bucketed ranking prevents long/short response bias in the score.
- R3 vs RDC trade-off: use RDC when unbiased native gradient attribution matters (staleness-dominated regimes); R3's replay suits routing-instability-dominated regimes but pays the omission bias.

## Relation

- Related skills: [[venusrl-disaggregated-agentic-rl-system]] (async RL systems), [[carm-cancellation-aware-response-masking]] (sequence-level response masking for off-policy filtering), [[copc-coupled-off-policy-correction]] (stale trajectory correction), [[two-clocks-rlvr-batch-scaling]] (off-policy batch effects in RLVR), [[routing-distraction-multimodal-moe]] (multimodal MoE routing analysis — different problem).

## Activation keywords

MoE RL, router drift, routing mismatch, expert routing disagreement, off-policy LLM RL, asynchronous RL, stale rollouts, GRPO MoE, R3 routing replay, sequence-level filtering, RLVR post-training
