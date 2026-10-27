---
name: two-clocks-rlvr-batch-scaling
description: "Use when scaling RLVR rollout batches. Two clocks: progress vs failure."
category: reinforcement-learning
---

# Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in RLVR

Source: arXiv:2610.18853 (Li, Quan, Qiu, Zhang, Tao — CMU & U Toronto, Oct 2026). Theory + controlled GRPO experiments (Qwen2.5-Math-1.5B, 16x batch range) showing square-root LR scaling splits RLVR into two clocks that tick in different units. Code: github.com/WinstonLiyt/two-clocks-rlvr

Use when: choosing RLVR rollout batch size, transferring learning rates across batches, diagnosing why a large-batch run needs more samples or collapses "on schedule", or designing batch-ramp schedules.

## Problem
RLVR generation cost motivates larger rollout batches B_r with square-root LR scaling (eta = kappa*sqrt(b), b = B_r/mu responses per optimizer step, mu steps per rollout). The rule is said to preserve progress per sample, but in multi-step training larger batches (a) need MORE samples to reach an accuracy target and (b) still collapse after ~the same number of consumed samples.

## Two-clock model (local quadratic approximation)
Progress clock — the rule preserves first-order drift per sample, but longer steps lose more to curvature:
- Progress per consumed response: r(b) = r0 - C_curv*b, C_curv = kappa^2 * (gHg)/(2*sigma^2)
- Samples to target: N_tau(B_r) = N_tau_min * (1 + B_r/B*); critical batch B* = mu*( 2*sigma*||g||^2 / (kappa * gHg) - B_noise ), B_noise = tr(H Sigma)/(gHg)
- B* DECREASES as the LR scale kappa grows (1/kappa term) — unlike McCandlish's gradient-noise critical batch (LR-independent); B* can lie far below the gradient noise scale.

Failure clock (drift-threshold hypothesis): a run fails when accumulated drift ||sum_j d_theta_j|| reaches threshold D over a stretch of slowly-changing mean-gradient direction:
- Failure law: N_fail = C * sqrt(b)/eta with C = D*sigma/||g||. Under the sqrt rule N_fail = C/kappa — INDEPENDENT of batch: failure keeps time in CONSUMED SAMPLES, not optimizer steps. (Noise-driven failure would give N_fail ~ b/eta^2.)

Where the clip acts: within a rollout, log-ratio spread grows ~factor B_rL/B_rS faster for large batches, so the ratio clip cuts more of their tokens and limits drift added per rollout — but it cannot remove the curvature-driven progress gap (gap persists even at mu=1 where the clip cannot act).

## Predictions (all confirmed)
- P1 Progress slows beyond B*: sample-cost exponent rose 0.15 -> 0.44 across LR regimes 1e-6 -> 1e-5; implied B* fell ~9k -> 2k responses. 512 -> 1536 costs little; beyond, increasingly step-limited.
- P2 Failure keeps time in samples: across 21 unclipped runs (32x batch, 6x LR), fit N_fail ~ b^beta * eta^-gamma gives beta - gamma/2 ~= 0 (CIs contain 0; rules out batch-blind -1/2) and gamma = 0.64-0.72 (rules out random-walk gamma=2). The 4096 batch fails in 7-10 rollouts (56-80 steps) vs 512 in 81 rollouts (648 steps) — both after 30-50k responses. 14/18 failing runs within factor 1.5 of the law.
- P3 Clip buys stability, not speed: with the clip, the 8192 batch never fails in budget; pushed to 2x rate it lasts 4x longer (small batch only 2x). ~0.5% of large-batch tokens carry >half the gradient norm. Widening the clip = transient speed, later decay/collapse. Clip-delayed failure means the failure law is a CONSERVATIVE estimate for clipped runs.

## Practical recipe (the payoff)
1. Below B*: use the largest efficient batch (in their setup 1536 — matched 512's sample efficiency, best final accuracy, never failed).
2. Above B*: ramp — start at small batch (B_r < B*), switch to large batch before the predicted failure point, reset optimizer state, repeat a one-rollout LR warm-up. Ramps (512 -> 4096/8192 at 24.6k samples) track the best fixed batch while generating 3/4 of samples at the large batch; switch window 25k-74k samples is forgiving.
3. Failure criterion: accuracy < half of best-so-far, or first sustained gradient-norm excursion (>4x early median, with >=3 of next 8 rollouts above it).
4. Monitor consumed samples, not steps: budgets and failure are set by responses generated.

## Robustness
Held on DeepScaleR-Preview, Qwen2.5-1.5B-Instruct, Qwen2.5-Math-7B (7B: batches fail 6x apart in rollouts but 1.3x in samples). Gradient-norm clipping on/off does not change failure timing.

## Reuse pattern
For any on-policy RL pipeline where generation dominates cost (RLVR, agentic rollouts): estimate B* from short pilot runs by fitting N_tau(B_r) = N_tau_min(1+B_r/B*); train below B* until progress stalls or drift nears the failure law, then switch; keep ratio clipping as cheap insurance that disproportionately protects large batches. Treat "more samples to same accuracy" and "same-sample collapse" as two separate budgets.

Related: McCandlish gradient noise scale (different: LR-dependent B* here), momentum-in-RLVR, EliteReplay, COPC (asynchronous staleness), GRPO clipping analyses.
