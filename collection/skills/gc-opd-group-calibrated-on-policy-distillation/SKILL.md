---
name: gc-opd-group-calibrated-on-policy-distillation
description: "Group-Calibrated On-Policy Distillation (GC-OPD) for long-context reasoning that combines verifier rewards with token-level teacher guidance. Use when training students on long-context evidence-aggregation tasks where global task constraints matter."
metadata:
  arxiv_id: "2608.19181"
  authors: "Various Authors"
  published: "2026-08-21"
  tags: [on-policy-distillation, long-context, verification, reward-calibration, reasoning]
license: Complete terms in LICENSE.txt
---

# GC-OPD: Group-Calibrated On-Policy Distillation

## Overview
Group-Calibrated On-Policy Distillation (GC-OPD) addresses the mismatch between token-level teacher support and trajectory-level verifier rewards in long-context reasoning tasks. In long-context evidence-aggregation tasks, token-level teacher guidance can favor locally plausible responses that omit distributed evidence or violate global constraints, while verifiers evaluate task completion at the response level.

## Problem Diagnosis
- **Teacher-verifier disagreement**: Trajectory-level OPD scores become progressively less aligned with verifier rewards as input length increases
- **Local vs Global optimization**: Token-level guidance optimizes local plausibility but may miss global task requirements
- **Evidence distribution**: Long contexts distribute evidence across the input, requiring global coordination

## Core Methodology

### Group Calibration
GC-OPD separately normalizes verifier rewards and trajectory-level OPD scores **within each rollout group** to create comparable scales:
```python
# Normalize within rollout group
normalized_verifier = (verifier_reward - group_mean_verifier) / group_std_verifier
normalized_opd = (opd_score - group_mean_opd) / group_std_opd
```

### Signed Disagreement Residual
The difference between normalized scores creates a **signed teacher-verifier disagreement residual**:
```python
disagreement_residual = normalized_verifier - normalized_opd
```

### Relative-Advantage-Based Credit Assignment (RACA)
RACA distributes the trajectory-level residual across tokens according to their relative OPD advantages:
```python
# Calculate relative advantages
relative_advantages = opd_token_scores - mean_opd_score

# Distribute residual proportionally to advantages
token_residuals = disagreement_residual * softmax(relative_advantages)

# Final token-level targets combine original OPD signal with residual
final_targets = original_opd_targets + token_residuals
```

## Implementation Workflow

### Step 1: Collect Rollout Groups
Generate multiple rollouts per prompt to form groups:
```python
rollout_groups = []
for prompt in prompts:
    group = [generate_rollout(prompt) for _ in range(num_rollouts_per_prompt)]
    rollout_groups.append(group)
```

### Step 2: Evaluate with Verifier and Teacher
For each rollout, compute both verifier reward and OPD score:
```python
for group in rollout_groups:
    for rollout in group:
        rollout.verifier_reward = verifier(rollout.response, prompt)
        rollout.opd_score = teacher_likelihood(rollout.tokens, prompt)
        rollout.token_opd_scores = token_level_teacher_scores(rollout.tokens, prompt)
```

### Step 3: Apply Group Calibration
Normalize scores within each group:
```python
for group in rollout_groups:
    verifier_rewards = [r.verifier_reward for r in group]
    opd_scores = [r.opd_score for r in group]
    
    group_mean_v, group_std_v = np.mean(verifier_rewards), np.std(verifier_rewards)
    group_mean_o, group_std_o = np.mean(opd_scores), np.std(opd_scores)
    
    for rollout in group:
        rollout.norm_verifier = (rollout.verifier_reward - group_mean_v) / (group_std_v + 1e-8)
        rollout.norm_opd = (rollout.opd_score - group_mean_o) / (group_std_o + 1e-8)
        rollout.disagreement_residual = rollout.norm_verifier - rollout.norm_opd
```

### Step 4: Apply RACA
Distribute residuals using relative advantages:
```python
for group in rollout_groups:
    for rollout in group:
        # Calculate relative advantages for each token
        mean_token_opd = np.mean(rollout.token_opd_scores)
        relative_advantages = rollout.token_opd_scores - mean_token_opd
        
        # Apply softmax to get distribution weights
        weights = softmax(relative_advantages)
        
        # Distribute residual
        token_residuals = rollout.disagreement_residual * weights
        
        # Create final targets
        rollout.final_targets = rollout.token_opd_scores + token_residuals
```

### Step 5: Train Student
Train the student model using the final targets:
```python
loss = mse_loss(student_predictions, final_targets)
loss.backward()
optimizer.step()
```

## Performance Results
- **Qwen3-4B**: Improved from 29.08 to 40.47 average across five benchmarks
- **Qwen3-8B**: Improved from 35.12 to 44.65 average across five benchmarks
- **Vanilla OPD baseline**: Reached 39.31 and 43.56 respectively

## Ablation Studies
- **Signed residual** is more effective than additional OPD-derived terms or direct verifier reward addition
- **RACA** improves over uniform token allocation
- **Group normalization** is crucial for proper calibration

## Best Practices

### Rollout Group Size
- Use **at least 4-8 rollouts per prompt** for stable group statistics
- Larger groups provide better normalization but increase computational cost

### Verifier Design
- Ensure verifiers capture **global task constraints** and **evidence completeness**
- Use **graded rewards** that reflect partial success rather than binary outcomes

### Teacher Selection
- Choose teachers that provide **dense token-level guidance**
- Ensure teacher quality is sufficient to provide meaningful OPD scores

### Hyperparameter Tuning
- **Learning rate**: Start with standard OPD learning rates and adjust based on stability
- **Temperature** for RACA softmax: Tune based on token advantage distribution

## Activation Keywords
- gc-opd
- group-calibrated distillation
- on-policy distillation
- long-context reasoning
- verifier reward calibration
- RACA

## References
- Original paper: https://arxiv.org/abs/2608.19181
- Related skills: on-policy-distillation-dlm-transformation, rl-closed-loop-eeg-tms