---
name: dre-dynamic-rollout-editing
description: "Dynamic Rollout Editing (DRE) for reducing overthinking in RL-trained reasoning models. Training-time intervention that preserves verified prefixes and edits unnecessary continuation. Use when: (1) GRPO/RLVR training shows overthinking, (2) credit assignment fails for successful trajectories, (3) models continue reasoning after correct answer emergence. Activation: overthinking, GRPO, rollout editing, credit assignment, RL post-training."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.17890v1"
  published: "2026-06-16"
  authors: "Zihao Wei, Wenjie Shi, Liang Pang et al."
  tags: [reasoning, rl, overthinking, grpo, credit-assignment]
---

# Dynamic Rollout Editing (DRE)

Training-time intervention for reducing overthinking in RL-trained reasoning models.

## Core Concept

**Overthinking**: Models continue generating unnecessary reasoning after a correct answer has emerged.

**Root cause**: GRPO assigns sequence-level credit — cannot distinguish solution-reaching prefix from unnecessary continuation. Both receive positive update signal.

**Key observation**: In early GRPO rollouts, successful trajectories exhibit slightly higher overthinking than unsuccessful trajectories. This creates undesirable feedback loop.

## DRE Intervention

For successful trajectories that continue thinking after answer emergence:

1. **Preserve** the accepted verified prefix
2. **Edit** the remaining thinking (truncate or simplify)
3. **Prefer** the edited trajectory within the same RL group

This weakens preference signal for unnecessary thinking without penalizing reasoning needed to reach the answer.

## Implementation Pattern

```python
# Conceptual DRE workflow
def dynamic_rollout_editing(trajectory, answer_emergence_point):
    """
    Args:
        trajectory: Full reasoning chain
        answer_emergence_point: Index where correct answer first appears
    
    Returns:
        edited_trajectory: Prefix + simplified continuation
    """
    verified_prefix = trajectory[:answer_emergence_point]
    edited_continuation = truncate_or_simplify(trajectory[answer_emergence_point:])
    return verified_prefix + edited_continuation
```

## Training Integration

Within GRPO training loop:
1. Sample rollouts at onset of training
2. Identify answer emergence points via verification
3. For successful trajectories with overthinking: apply DRE
4. Include edited trajectory in preference comparison
5. Continue standard GRPO update

## When to Apply

- Early GRPO training shows imbalance between successful/unsuccessful trajectories
- Sequence-level credit assignment cannot distinguish prefix from continuation
- Models trained with RLVR produce excessive reasoning chains

## Pitfalls

- **Premature truncation**: Ensure answer is verified before editing
- **Over-correction**: Don't penalize reasoning needed to reach answer
- **Implementation complexity**: Requires trajectory-level modification during RL

## Related Patterns

- See `suco-sufficiency-guided-continuous-adaptive-reasoning` for sufficiency-based stopping
- See `opd-evolver-on-policy-distillation-agent` for agent memory evolution

---

arXiv: [2606.17890v1](https://arxiv.org/abs/2606.17890v1)