---
name: unbiased-recovery-policy-gradient
description: SafeExplorer - drop-in PPO modification for RL with a deterministic recovery policy that prevents silent bias in on-policy updates. Uses score-function estimator only at safe timesteps, never evaluates recovery-policy density, so it stays valid where importance sampling breaks. Use when training RL agents on real robots / safety-critical systems where falls/crashes are costly and a separate recovery controller is engaged inside the safe region.
---

# Unbiased Policy Gradient with Recovery Interventions (SafeExplorer, arXiv:2607.08925)

A drop-in fix for PPO when a **separate recovery policy** takes over whenever the agent leaves a
designer-specified safe region. Standard mixed-policy rollouts silently bias every on-policy update;
importance-sampling correction is ill-defined when the recovery policy is deterministic.

## When to use
- RL on physical robots / safety-critical sims where a fall/crash is very costly.
- You already (or plan to) hand control to a recovery policy inside a safe region.
- You want to minimize training-time failures, NOT trade them off against return (unlike CMDP).

## The problem
- Mixed rollout: agent acts, recovery policy intervenes near the safe-region boundary.
- On-policy estimators (PPO) assume a single policy generated the data → biased gradients.
- Importance sampling (IS) correction needs `π_recovery(a|s)` — undefined when recovery is
  **deterministic**, and unstable even when stochastic.

## The fix (core estimator)
- **Unbiased policy-gradient estimator**: use the score function `∇log π_agent(a|s)` ONLY at **safe
  timesteps** (where the agent, not recovery, acted). Never evaluate or divide by the recovery
  policy's density.
- This is valid even when recovery is deterministic — exactly where IS breaks — and empirically
  dominates IS when recovery is stochastic too.

## Two acceleration components (because recovery slows credit assignment near the boundary)
1. **Closed-form value for recovery-triggering states** when dynamics + recovery are deterministic:
   plug the known recovery outcome into the value target instead of bootstrapping through unknown
   transitions.
2. **Imitation loss**: copy recovery actions ONLY when recovery *succeeds* (not on failed recoveries,
   which would teach the agent bad behavior).

## Implementation steps
1. Define safe region `S ⊂ state space` (a subset the agent should stay within).
2. Keep a separate recovery policy `π_rec` (can be a simple controller / scripted).
3. During rollout: agent acts in `S`; when `s ∉ S`, `π_rec` takes over until back in `S`.
4. PPO modification: mask the policy-gradient term to safe timesteps only:
   `g = E[ 1[s_t ∈ S] · ∇log π_agent(a_t|s_t) · A_t ]` (advantage `A_t` from the value net).
5. Add closed-form value target for boundary states + success-gated imitation loss.
6. Train as usual; tune the safe-region size (too small → frequent recovery → slow; too large →
   unsafe).

## Results (paper, 3 envs × 5 seeds)
- Training-time falls reduced **233× / 48× / 26×** on HalfCheetah / Ant / Unitree Go1 vs PPO.
- Matches or exceeds PPO final reward.
- On Ant (unreliable recovery) it is the ONLY method reaching 80% of best final reward.

## Pitfalls
- Safe region must be cheap to evaluate each step; complex `S` adds overhead.
- If recovery frequently fails, the imitation loss gate is essential — without it you teach failure.
- The estimator assumes recovery transitions don't appear in the agent's gradient; if recovery is
  stochastic AND you want its gradients, this method explicitly drops them (by design).
- Doesn't replace a real safety filter; it's a training-time bias fix, not a runtime guarantee.

## Verification
- Compare training-time failure count, final reward, and sample efficiency vs PPO + naive IS.
- Confirm advantage estimates are unbiased on a toy MDP with known optimum.
