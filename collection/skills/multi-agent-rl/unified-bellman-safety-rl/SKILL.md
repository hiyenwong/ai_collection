---
name: unified-bellman-safety-rl
description: "Unified Bellman Operator for Safety-Critical RL: Unifies performance and safety into joint value function with two-timescale convergence. Near-zero safety violations at test time on continuous control tasks."
tags: [safe-rl, bellman-operator, safety-constraints, two-timescale, continuous-control, constrained-optimization]
source: "arXiv:2610.12420"
utility_score: 0.87
---

# A Unified Bellman Operator for Safety-Critical Reinforcement Learning

## Paper Metadata

- **arXiv ID**: 2610.12420
- **Title**: A Unified Bellman Operator for Safety-Critical Reinforcement Learning
- **Authors**: Nishanth Arun Rao, Royina Karegoudra Jayanth, Benjamin Eysenbach, Jaime Fernández Fisac
- **Published**: 2026-10-08
- **Categories**: cs.LG
- **Link**: https://arxiv.org/abs/2610.12420

## Abstract Summary

Reinforcement learning in safety-critical domains requires maximizing task performance while strictly adhering to safety constraints. Existing safe reinforcement learning paradigms typically force a trade-off: they either require a priori knowledge to provide strict safety guarantees (e.g., safety filters), or they enable joint learning but only satisfy safety constraints on average. This work proposes a novel Bellman operator that unifies performance and safety objectives into a joint value function. Temporal difference learning with the joint Bellman operator converges under a two-timescale stochastic approximation framework. On the fast timescale, the safety value of the learning joint policy is estimated, while the joint value is estimated on the slow timescale. Convergence is ensured by formulating the limiting dynamics as an occupation-averaged differential inclusion, and showing that it asymptotically converges to a set of limiting optimal safety-constrained task value functions. Once converged, the resulting optimal policy maximizes task return while maintaining safety at all times. Empirical evaluations on continuous control tasks with neural approximations demonstrate stable convergence with near-zero safety violations at test time.

## Key Contributions

1. **Unified Bellman operator**: Joint value function combining performance and safety objectives
2. **Two-timescale convergence**: Fast timescale for safety value, slow timescale for joint value
3. **Theoretical guarantees**: Convergence via occupation-averaged differential inclusion
4. **Strict safety**: Policy maximizes task return while maintaining safety at all times (not just on average)
5. **Empirical validation**: Near-zero safety violations on continuous control tasks with neural approximations

## Research Implications

- **No trade-off required**: Eliminates trade-off between a priori safety guarantees and joint learning
- **Strict safety guarantees**: Maintains safety at all times, not just in expectation
- **Convergence theory**: Provides rigorous convergence proof under two-timescale framework
- **Neural approximation**: Works with function approximation for high-dimensional problems
- **Practical deployment**: Near-zero violations make it suitable for real-world safety-critical applications

## Practical Applications

- Deploy RL in safety-critical domains (robotics, autonomous vehicles, healthcare)
- Train policies that guarantee safety constraints are never violated
- Balance task performance with strict safety requirements
- Apply to continuous control problems with neural network policies
- Build systems that learn safely without requiring perfect prior models

## Related Work

- Safe reinforcement learning
- Constrained Markov decision processes
- Safety filters and shield synthesis
- Constrained optimization in RL
- Two-timescale stochastic approximation
