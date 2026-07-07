---
name: opd-evolver-on-policy-distillation-agent
description: "OPD-Evolver - On-policy distillation framework for cultivating holistic agent evolvers. Slow-fast co-evolution with four-level memory hierarchy: read, use, write, maintain experience. Outcome-calibrated memory attribution + privileged hindsight distillation. Use when: (1) building self-evolving agents, (2) memory management beyond storage, (3) agent experience learning. Activation: agent evolver, on-policy distillation, memory hierarchy, self-evolution, experience management."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.17628v1"
  published: "2026-06-16"
  authors: "Guibin Zhang, Xun Xu, Yanwei Yue et al."
  tags: [agent, memory, distillation, self-evolution, on-policy]
---

# OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation

Slow-fast co-evolution framework for cultivating agents that can **evolve through experience**, not just store it.

## Core Insight

**Memory ≠ Evolution**: Existing memory agents can store trajectories, retrieve reflections, or accumulate skills, but often lack holistic competence to:
- Select useful experience
- Act on it
- Write reusable knowledge
- Maintain growing repository

## Framework Architecture

### Fast Loop: Test-Time Evolution

Four-level memory hierarchy for rapid test-time evolution:

1. **READ** - Retrieve relevant experience
2. **USE** - Apply retrieved knowledge to current task
3. **WRITE** - Store new reusable knowledge
4. **MAINTAIN** - Update and prune memory repository

### Slow Loop: Policy Distillation

1. **Outcome-calibrated memory attribution** - Identify which memories contributed to success
2. **Privileged hindsight distillation** - Use ground-truth outcomes to train policy

```python
class OPDEvolver:
    def __init__(self):
        self.memory_hierarchy = FourLevelMemory()  # read/use/write/maintain
        self.policy_model = None
    
    def fast_loop(self, task):
        # Test-time evolution
        experience = self.memory_hierarchy.read(task)
        action = self.use(experience, task)
        outcome = execute(action)
        new_knowledge = self.write(outcome)
        self.memory_hierarchy.maintain(new_knowledge)
    
    def slow_loop(self):
        # Policy distillation
        attribution = outcome_calibrated_attribution()
        hindsight = privileged_information()
        self.policy_model = distill(attribution, hindsight)
```

## Outcome-Calibrated Memory Attribution

Identify which memories in the hierarchy contributed to successful outcomes:

- Use outcome verification to trace causal contribution
- Weight memory elements by their attribution scores
- Focus distillation on high-value experience

## Privileged Hindsight Distillation

During training, use ground-truth outcomes that weren't available at test time:

- Distill four abilities (read/use/write/maintain) into deployable policy
- Train with hindsight supervision from verified outcomes
- Enable policy to perform memory management autonomously

## When to Apply

- Building self-evolving agents beyond memory-augmented agents
- Memory management that goes beyond trajectory storage
- Agents that need to learn how to evolve through experience

## Performance Benchmarks

- Surpasses ReasoningBank by up to 11.5%
- Surpasses Skill0 by ~5.8%
- OPD-Evolver-9B challenges Qwen3.5-397B-A17B

## Pitfalls

- **Attribution complexity**: Outcome-calibrated attribution requires careful design
- **Hindsight leakage**: Ensure hindsight doesn't leak into test-time policy
- **Memory hierarchy tuning**: Four-level structure needs calibration

## Related Patterns

- See `admem-advanced-agent-memory` for agent memory architecture
- See `agent-memory-framework` for memory-augmented agents

---

arXiv: [2606.17628v1](https://arxiv.org/abs/2606.17628v1)