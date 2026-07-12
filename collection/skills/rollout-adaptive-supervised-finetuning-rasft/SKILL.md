---
name: rollout-adaptive-supervised-finetuning-rasft
description: Rollout-Adaptive Supervised Fine-Tuning (RASFT) for reasoning tasks - policy-aware SFT that calibrates expert supervision based on problem-level solvability from verified rollouts.
authors:
  - Yongliang Miao
  - Fengyuan Liu
  - Wei Shi
date: 2026-06-05
arxiv: 2606.07006v1
tags:
  - reasoning
  - supervised-finetuning
  - policy-aware
  - adaptation
  - LLM
---

# Rollout-Adaptive Supervised Fine-Tuning (RASFT)

## Overview

Policy-aware supervised fine-tuning (SFT) that calibrates expert supervision based on verified on-policy rollouts. Avoids overfitting to single expert trajectories by incorporating correct self-generated reasoning when model already exhibits reliable behavior.

## Key Innovation

**Problem-Level Solvability Calibration:**
- Rigid expert imitation overfits to surface forms
- Suppresses model's own reasoning distribution
- RASFT adjusts guidance strength based on model performance on each problem

**Verified Rollouts:**
- Estimate solvability from on-policy rollouts with verification
- Strengthen expert guidance when model struggles
- Relax imitation when model already solves correctly

## Methodology

### Phase 1: Solvability Estimation

```
For each problem p in dataset:
    # Generate multiple rollouts with current policy
    rollouts = policy.generate_n_rollouts(p, n=K)
    
    # Verify correctness of each rollout
    verified_results = verify(rollouts)
    
    # Estimate solvability: fraction of correct rollouts
    solvability(p) = count_correct(verified_results) / K
```

### Phase 2: Adaptive Supervision

```
For each problem p:
    if solvability(p) is low:
        # Model struggles - strengthen expert guidance
        supervision_weight = high
        target_trajectory = expert_trajectory(p)
    elif solvability(p) is high:
        # Model reliable - relax rigid imitation
        supervision_weight = low
        # Incorporate correct self-generated trajectories
        target_trajectory = correct_self_trajectory(p)
    else:
        # Intermediate - balanced mixture
        target_trajectory = mix(expert, self_generated)
```

### Phase 3: Policy Drift Constraint

```python
# Clipped inverse ratio between frozen reference and current policy
reference_model = frozen_base_model
current_policy = trainable_model

drift_penalty = clip(
    inverse_ratio(
        log_prob(current_policy, trajectory),
        log_prob(reference_model, trajectory)
    ),
    min=drift_threshold
)

loss = SFT_loss + drift_penalty
```

## Reusable Patterns

### Pattern 1: Policy-Aware SFT
**Use when:** Standard SFT causes overfitting to expert trajectories
**Principle:** Calibrate supervision strength based on model's own verified performance
**Implementation:**
1. Generate rollouts with current policy
2. Verify correctness (execution check, ground truth, etc.)
3. Adjust supervision per-problem based on success rate

### Pattern 2: Self-Generated Trajectory Integration
**Use when:** Model exhibits partial competence
**Approach:**
- High solvability: Use model's own correct trajectories as targets
- Low solvability: Emphasize expert demonstration
- Mix for intermediate cases

### Pattern 3: Reference-Based Drift Constraint
**Use when:** Preventing excessive deviation from base model
**Method:**
1. Freeze base model as reference
2. Compute KL-like penalty between current and reference
3. Clip penalty to prevent over-constraint
4. Add to loss for stable adaptation

### Pattern 4: Verified Rollout Sampling
**Use when:** Need reliable solvability estimates
**Steps:**
1. Sample multiple rollouts per problem
2. Verify each with appropriate metric
3. Success rate → solvability score
4. Use for adaptive guidance

## Implementation Considerations

### Verification Methods
- **Mathematical reasoning**: Execute answer check
- **Code reasoning**: Run test cases
- **General reasoning**: Compare to ground truth or use validation model

### Solvability Thresholds
- Low threshold (e.g., < 0.3): Full expert guidance
- High threshold (e.g., > 0.7): Self-generated focus
- Intermediate: Balanced mixture

### Drift Constraint Parameters
- Clip minimum: Prevent excessive penalty
- Inverse ratio formulation: Penalize large deviations more
- Balance between adaptation and preservation

### Batch-Level Processing
- Process problems in batches for efficiency
- Cache solvability estimates between epochs
- Update rollouts periodically (not every step)

## Extensions

### Multi-Task Adaptation
- Task-specific solvability thresholds
- Per-task expert trajectory pools

### Curriculum Learning Integration
- Progress from low-solvability to high-solvability problems
- Adaptive curriculum based on rollout verification

### Reinforcement Learning Hybrid
- Combine RASFT with RL fine-tuning
- Use verified rollouts as RL reward signal

## Pitfalls

1. **Verification Cost**: Running verification for every rollout can be expensive
2. **Solvability Noise**: Low K (few rollouts) gives noisy estimates
3. **Self-Trajectory Quality**: Low-quality self trajectories degrade training
4. **Drift Over-Constraint**: Too tight clipping prevents necessary adaptation
5. **Batch Imbalance**: Solvability distribution may skew batch composition

## Results (Paper Findings)

- Better than standard SFT across mathematical and code reasoning
- Outperforms SFT variants and representative RL methods
- Tested on 6 mathematical reasoning + 2 code reasoning benchmarks
- Preserves useful reasoning priors via drift constraint

## Code Reference

GitHub: https://github.com/zjd1sq/RASFT

## Applications

- Mathematical reasoning fine-tuning
- Code generation adaptation
- Multi-step reasoning tasks
- Tasks with verifiable outputs
- Policy-aware training for any reasoning domain

## Activation Keywords

`RASFT`, `rollout-adaptive`, `policy-aware SFT`, `verified rollouts`, `solvability estimation`, `self-generated trajectories`, `expert guidance calibration`, `reasoning fine-tuning`, `policy drift constraint`, `adaptive supervision`