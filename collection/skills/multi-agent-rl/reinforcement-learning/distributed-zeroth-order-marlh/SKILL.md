---
name: distributed-zeroth-order-marlh
description: "Distributed zeroth-order policy gradient for networked multi-agent reinforcement learning from human feedback (RLHF). Addresses scalability of preference-based RL to multi-agent systems without centralized training. Activation: distributed multi-agent RLHF, zeroth-order policy gradient, networked MARL, human feedback multi-agent, decentralized preference RL, spatial-temporal truncated trajectory."
---

# Distributed Zeroth-Order Policy Gradient for Networked MARL with Human Feedback

**Paper:** "Distributed Zeroth-Order Policy Gradient for Networked Multi-agent Reinforcement Learning from Human Feedback"
**arXiv:** [2605.15697](https://arxiv.org/abs/2605.15697)
**Authors:** Pengcheng Dai, He Wang, Dongming Wang, Jian Qin, Wenwu Yu
**Date:** 2026-05-15

## Core Problem

Existing preference-feedback RL approaches are primarily single-agent and centralized, limiting scalability to large-scale networked multi-agent systems.

## Key Innovation

### Spatiotemporally Truncated Trajectory Pairs

Human feedback is provided on trajectory pairs aggregated over each agent's **κ-hop neighborhood**:
- **H-horizon** truncated trajectories
- **κ-hop** spatial neighborhood aggregation
- No explicit reward signals needed
- No centralized control required

### Distributed Zeroth-Order Policy Gradient Algorithm

```
For each agent i:
  1. Observe κ-hop neighborhood states and actions
  2. Sample perturbed policy θ_i + ε_i (ε_i ~ N(0, σ²I))
  3. Human provides preference: π_i(current) vs π_i(perturbed)
  4. Estimate local gradient: g_i ≈ (preference_score / σ) · ε_i
  5. Update: θ_i ← θ_i + α · g_i
  6. Communicate only with κ-hop neighbors
```

### Theoretical Guarantees

- Converges to **ε-stationary point** with **polynomial sample complexity**
- Fully distributed — no global reward or centralized coordination
- Each agent's feedback depends only on local κ-hop neighborhood

## Key Parameters

| Parameter | Role |
|-----------|------|
| H | Trajectory horizon for preference comparison |
| κ | Neighborhood hop distance (controls communication scope) |
| σ | Perturbation standard deviation |
| α | Learning rate |

## Algorithm Design Patterns

- **Zeroth-order gradient estimation**: Uses function value differences instead of explicit gradients
- **Localized communication**: Each agent only communicates within κ-hop neighborhood
- **Preference-only supervision**: No reward function needed, only pairwise preferences
- **Networked structure**: Exploits underlying network topology with localized state dependencies

## Applications

- Multi-robot coordination with human guidance
- Networked control systems with preference feedback
- Scalable MARL where explicit reward design is infeasible
- Decentralized optimization with human-in-the-loop

## Implementation Considerations

- Perturbation must be zero-mean for unbiased gradient estimates
- Neighborhood size κ controls tradeoff between accuracy and communication cost
- Human preference model must be consistent (can be noisy but not adversarial)

## Related Work

- [[sdar-self-distilled-agentic-rl]] - Self-distilled agentic RL (dense supervision paradigm)
- [[ohp-rl-human-preference-guidance]] - Online human preference for single-agent manipulation
- [[rlhf-from-human-feedback]] - Centralized RLHF
- [[multi-agent-rl-patterns]] - Multi-agent reinforcement learning patterns
