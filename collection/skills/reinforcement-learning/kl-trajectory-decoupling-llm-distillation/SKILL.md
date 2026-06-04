---
name: kl-trajectory-decoupling-llm-distillation
description: "KL-Trajectory Decoupling methodology — unified theoretical framework decomposing LLM distillation into two orthogonal choices: prefix distribution (what to condition on) and trajectory distribution (how to generate responses). Reveals that SFT, DAgger, Offline RL, and On-Policy Distillation (OPD) differ along these two axes. Use when: analyzing distillation methods, choosing between SFT/Dagger/OPD/Offline-RL, designing new distillation algorithms, understanding KL divergence in LLM fine-tuning, RL vs imitation learning trade-offs. Activation: KL trajectory decoupling, LLM distillation framework, SFT DAgger OPD comparison, prefix trajectory decomposition, distillation design space, on-policy off-policy distillation."
---

# KL-Trajectory Decoupling: A Unified Framework for LLM Distillation

## Overview

Knowledge distillation in LLMs has many paradigms (SFT, DAgger, Offline RL, On-Policy Distillation/OPD) that appear fundamentally different. This work reveals they are all special cases of **two orthogonal design choices**:

1. **Prefix Distribution**: What context/observations does the student condition on?
2. **Trajectory Distribution**: What response generation process produces the training targets?

## The Two-Axis Decomposition

### Axis 1: Prefix Distribution

| Method | Prefix Source |
|--------|--------------|
| SFT | Fixed dataset prompts (offline) |
| DAgger | Student-generated prefixes (interactive) |
| Offline RL | Fixed dataset states (offline) |
| OPD | Student-generated prefixes (on-policy) |

### Axis 2: Trajectory Distribution

| Method | Trajectory Source |
|--------|------------------|
| SFT | Expert/teacher demonstrations |
| DAgger | Expert/teacher demonstrations |
| Offline RL | Fixed dataset transitions |
| OPD | Student's own policy rollouts |

### Unified Matrix

| | Expert Trajectories | Student Trajectories | Fixed Dataset |
|--|---|---|---|
| **Fixed Prefix** | SFT | — | Offline RL |
| **Student Prefix** | DAgger | OPD | — |

## Key Theoretical Insights

### KL Coupling Problem

The prevailing paradigms implicitly **couple** prefix and trajectory choices:
- OPD: student prefixes + student trajectories (no gradient on prefix KL)
- SFT: fixed prefixes + expert trajectories (distribution shift)

This coupling creates blind spots:
- **SFT** ignores prefix KL divergence → distribution shift at inference
- **OPD** ignores trajectory KL → can't leverage teacher quality

### Decoupled Optimization

The framework proposes independently optimizing both axes:
```
min D_KL(π_student || π_teacher) = 
  D_KL(prefix_student || prefix_teacher) + 
  E[D_KL(trajectory_student || trajectory_teacher | prefix)]
```

This reveals that effective distillation requires:
1. Matching the prefix distribution (not just trajectories)
2. Selecting the right trajectory source for each prefix type

## Practical Implications

### When to Use Each Method

- **SFT**: Strong teacher, fixed task distribution, no distribution shift expected
- **DAgger**: Interactive setting, distribution shift is the main concern
- **Offline RL**: Rich fixed dataset, reward signal available
- **OPD**: No teacher trajectories, self-improvement via RL

### Hybrid Approaches

The decomposition suggests new hybrids:
- **SFT + OPD**: Expert trajectories on student prefixes (DAgger-like) combined with self-generated trajectories
- **Mixed prefixes**: Blend fixed and student-generated prefixes during training

## Implementation

### Unified Distillation Interface
```python
class DistillationConfig:
    prefix_source: str = "fixed"    # "fixed" | "student" | "mixed"
    trajectory_source: str = "expert"  # "expert" | "student" | "mixed"
    kl_prefix_weight: float = 0.0    # weight on prefix KL
    kl_trajectory_weight: float = 1.0  # weight on trajectory KL
    
    def get_method_name(self):
        if self.prefix_source == "fixed" and self.trajectory_source == "expert":
            return "SFT"
        elif self.prefix_source == "student" and self.trajectory_source == "expert":
            return "DAgger"
        elif self.prefix_source == "student" and self.trajectory_source == "student":
            return "OPD"
        elif self.prefix_source == "fixed" and self.trajectory_source == "student":
            return "Offline RL"
        else:
            return f"Hybrid({self.prefix_source}/{self.trajectory_source})"
```

### Decoupled Training Loop
```python
# Compute prefix KL separately
prefix_kl = compute_kl(student_prefix_dist, teacher_prefix_dist)

# Compute trajectory KL conditioned on prefix
trajectory_kl = compute_kl(
    student_traj_given_prefix, 
    teacher_traj_given_prefix
)

# Total loss = weighted sum
total_loss = kl_prefix_weight * prefix_kl + kl_trajectory_weight * trajectory_kl
```

## Applications

- Designing new distillation algorithms by exploring the 2D design space
- Diagnosing why certain distillation methods fail (missing axis coverage)
- Combining multiple distillation methods systematically
- Understanding the relationship between imitation learning and RL in LLMs

## Related

- [[tool-integrated-reasoning-recipe]] — SFT+RL pipeline for TIR
- [[d2evo-dual-difficulty-self-evolution]] — data-efficient RL
- [[learning-zone-energy-data-selection]] — RL post-training optimization
- [[sdar-self-distilled-agentic-rl]] — self-distilled agentic RL

## Paper

- arXiv: Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation
- Submitted: May 2026
