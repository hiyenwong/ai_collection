---
name: unified-bellman-safe-rl
description: Single Bellman operator jointly optimizing task return and hard safety constraints, with two-timescale convergence; safe policy without a priori filters or average-case relaxation.
category: ai_collection
trigger: safe reinforcement learning, constrained MDP, Bellman operator, safety value function, two-timescale stochastic approximation, differential inclusion, safety-critical control, hard constraints at all times
---

# Unified Bellman Operator for Safety-Critical RL

Methodology from arXiv:2610.12420 (Rao et al., 2026-10-08, cs.LG): existing safe-RL paradigms
force a trade — a-priori safety filters give hard guarantees but need environment knowledge;
joint learners satisfy constraints only on average. This work unifies both objectives in a
**single joint value function** with one Bellman operator and proves convergence.

## The Joint Value Construction

- Define a joint value that scores a policy by **task return AND safety adherence simultaneously**,
  rather than a weighted sum that can trade one for the other.
- The joint Bellman operator's contraction/monotonicity structure is preserved so standard
  TD learning applies; the safety component acts as a *hard feasibility* term, not a Lagrangian
  penalty (no dual variable tuning, no constraint-violation-permitting optima).

## Two-Timescale Learning (why it converges)

TD learning with the joint operator is analyzed as **two-timescale stochastic approximation**:

- **Fast timescale**: estimates the safety value V_safe(π) of the *current learning policy* —
  safety estimation must track the moving policy faster than the policy-value estimates move.
- **Slow timescale**: estimates the joint value (task + safety) under the evolving safety estimate.

Convergence proof strategy (reusable):
1. Freeze the fast timescale → the coupled updates reduce to a limiting ODE/differential inclusion.
2. Formulate the limiting dynamics as an **occupation-averaged differential inclusion**
   (set-valued because the safety-term introduces kinks/discontinuities at constraint boundaries).
3. Show via Lyapunov/set-valued invariance arguments that trajectories converge to the set of
   *limiting optimal safety-constrained task value functions*.
4. Lift the ODE result to stochastic approximation with standard two-timescale theorems.

Practical reading: **estimate constraint-related quantities on a faster timescale than the main
value function** whenever the objective couples a feasibility critic with a performance critic.

## Empirical Anchors

- Continuous-control tasks with neural function approximation: stable convergence, **near-zero
  safety violations at test time** while maximizing task return.
- No a-priori model knowledge or external safety filter required at deployment; guarantees
  hold for the learned policy, not just on-average over episodes.

## Reusable Patterns

1. Hard constraints at all times ≠ Lagrangian/constrained-policy-optimization relaxation —
   encode feasibility into the value function's own structure via a joint operator.
2. Two-critic architectures need timescale separation: safety critic fast, task critic slow;
   mismatched rates show up as oscillation at the constraint boundary.
3. Differential-inclusion (not plain ODE) methods are the right tool when Bellman operators
   contain non-smooth feasibility terms — set-valued limits absorb the kinks.
4. Applicable template for other "performance + hard feasibility" decision problems:
   replace "safety" with any persistent constraint (energy budget, latency SLA, connectivity).
