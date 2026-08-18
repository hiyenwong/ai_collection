---
name: step-level-on-policy-distillation
description: "SOPD: Step-level supervision combining SFT and OPD."
---

# Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning

## Overview
Step-Level On-Policy Distillation (SOPD) combines the long-horizon correction of supervised fine-tuning (SFT) with the on-policy advantage of standard token-level OPD to provide step-level supervision over complete student-generated trajectories. At different limits of step length, SOPD reduces to SFT or approximates OPD.

## Key Advantages

### Compared to SFT
- Teacher responses are conditioned on student trajectories
- Aligns more closely with student-visited states
- Provides more relevant supervision

### Compared to OPD  
- Provides longer-horizon corrections rather than fragmented token-level guidance
- Unfolds complete and correct repair paths instead of partial corrections
- Better handles erroneous student trajectories

## Performance Results
- On ALFWorld, SOPD improves average success rate by 13.4 points over Vanilla OPD
- Substantially outperforms conventional SFT and OPD across both reasoning and agent tasks
- Competitive with or outperforms mean-baseline GRPO

## Implementation Guidelines

### When to Use
- Agent tasks requiring trajectory-level corrections
- Reasoning tasks with multi-step dependencies
- When standard OPD provides only fragmented corrections
- Need to balance on-policy advantages with long-horizon guidance

### Integration Steps
1. Define appropriate step length based on task complexity
2. Generate complete student trajectories
3. Condition teacher responses on student trajectories at step boundaries
4. Apply step-level supervision during training

## Applications
- Embodied AI agents (ALFWorld, WebArena)
- Complex reasoning tasks
- Multi-turn dialogue systems
- Code generation with execution feedback

## References
- arXiv:2608.16333
- ALFWorld benchmark results