---
name: shortcut-trajectory-planning-offline-rl
description: Single-stage shortcut-model trajectory planner for efficient offline model-based RL. Replaces two-stage consistency-distillation with one-stage step-size-conditioned shortcut models + feasibility-aware critic for fast one/few-step generative planning. Use when building fast diffusion-based planners for offline RL (D4RL) without the training cost/instability of teacher-student distillation.
---

# Shortcut Trajectory Planning (STP) — from arXiv:2607.09336

Offline model-based RL framework that uses **shortcut models** as efficient trajectory generators,
avoiding the expensive two-stage teacher–student consistency-distillation pipeline common in
diffusion planners.

## When to use
- You want diffusion-quality trajectory planning but the iterative denoising (50+ steps) is too slow
  at inference.
- You want to avoid consistency-model distillation (two-stage, unstable, needs a teacher).
- Target domains: D4RL locomotion / navigation / manipulation / dexterous control.

## Core idea
- Train a **conditional shortcut trajectory model in a single stage**. The model is conditioned on a
  *step-size* parameter `s` so it can do **one-step (s large) or few-step (s small) inference** from
  the same weights — no separate distilled student.
- Generate K candidate plans (one/few-step), then **select** the best with a critic augmented by a
  **feasibility-aware correction** term that penalizes physically infeasible trajectories.

## Implementation steps
1. **Shortcut model**: parameterize the trajectory generator `G(z, s; θ)` where `s ∈ (0,1]` is the
   step-size. Train with a single-stage objective that maps noise → trajectory such that large `s`
   yields a coarse one-step guess and small `s` refines it. (Single-stage = no teacher needed.)
2. **Feasibility-aware critic**: standard Q/critic `Q(s, a)` plus a correction `c(τ)` that scores
   trajectory feasibility from the dynamics model (e.g. constraint violation, terminal-state
   reachability). Selection score = `Q + λ·c(τ)`.
3. **Planning**: sample `K` latent `z`, generate `τ_k = G(z_k, s)` at chosen `s` (1 or few steps),
   pick `argmax_k` selection score. Roll out in the environment / model.
4. Sweep `s` to trade latency vs plan quality.

## Key advantages over consistency distillation
- One training stage instead of two → simpler, cheaper, more stable.
- `s`-conditioning gives adjustable compute at inference with NO extra models.
- Feasibility correction prevents the shortcut from emitting infeasible plans that a raw diffusion
  sampler might.

## Pitfalls
- Shortcut models can under-perform full diffusion at very few steps on hard dynamics; calibrate `s`
  per task (few-step often best tradeoff).
- Feasibility correction must be cheap (use the learned dynamics model, not ground-truth sim rolls).
- Offline distribution shift: shortcut model may extrapolate; keep `K` modest and rely on the critic.
- Single-stage training needs careful noise scheduling; reuse the diffusion scheduler's sigma curve.

## Verification
- Report planning latency (steps) vs return on D4RL benchmarks vs a consistency-distilled baseline
  at matched compute.
- Ablate the feasibility correction: show it recovers infeasible-plan rejection.
