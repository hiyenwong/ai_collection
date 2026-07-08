---
name: direct-on-policy-distillation
description: "Weak-to-strong generalization methodology transferring RL-induced policy shifts as dense implicit reward signals from smaller to larger models, enabling cross-scale RL outcome reuse."
---

# Direct On-Policy Distillation (Direct-OPD)

## Description
A methodology for weak-to-strong generalization that transfers the RL-induced policy shift from a smaller teacher model to a stronger target model. Instead of distilling the teacher's final policy (which mixes useful RL gains with small-model limitations), Direct-OPD computes the log-ratio between post-RL and pre-RL teacher policies and uses this as a dense implicit reward for the student. Enables reusing RL outcomes across model scales without training explicit reward models or running sparse-reward RL on the target.

## Activation Keywords
- Direct-OPD
- direct on-policy distillation
- weak-to-strong generalization
- RL policy transfer
- implicit reward signal
- policy shift transfer
- cross-scale RL
- 弱到强泛化
- 策略迁移
- 隐式奖励

## Tools Used
- execute_code: Run RL training pipelines with distillation loss
- terminal: Execute training commands, monitor progress
- read: Load model checkpoints, compute log-ratios

## Core Methodology

### The Problem
- RLVR (RL with verifiable rewards) is expensive: target model must generate many rollouts during training
- Directly distilling post-RL weak teacher is insufficient: final policy mixes useful RL gains + small-model limitations
- As models scale, post-training itself becomes a bottleneck

### Direct-OPD Solution
1. Run RL on a smaller model (cheap rollouts)
2. Compute log-ratio: `log(π_post(x) / π_pre(x))` for each action
3. Treat this log-ratio as a dense implicit reward for the stronger student
4. Apply signal on the student's own on-policy states

### Mathematical Formulation
```
Implicit Reward: r_impl(x, a) = log(π_weak_post(a|x) / π_weak_pre(a|x))
Student Loss: L = E[(a ~ π_strong)] [r_impl(x, a)]
```

The checkpoint pair (pre-RL, post-RL) tells us which actions RL made more/less likely, and Direct-OPD applies that signal on the stronger student's states.

## Usage Patterns

### Pattern 1: Standard Direct-OPD Training
```
1. Train weak model with RLVR → get π_weak_post
2. Save pre-RL checkpoint π_weak_pre
3. For student model (stronger):
   a. Generate on-policy rollouts with π_strong
   b. Compute implicit rewards: r = log(π_weak_post/π_weak_pre)
   c. Update π_strong using implicit rewards
4. Repeat until convergence
```

### Pattern 2: Sequential Composition of Policy Shifts
```
Multiple weak teachers → sequential policy shifts:
1. Teacher 1 (small) → Student (medium)
2. Teacher 2 (medium, after step 1) → Student (large)
3. Each step transfers a different aspect of RL improvement
```

### Pattern 3: Cross-Scale RL Reuse
```
Instead of training RL on every model size:
1. Train RL once on smallest feasible model
2. Distill policy shift to medium model
3. Distill policy shift to large model
4. Distill policy shift to very-large model
```

## Instructions for Agents

### Step 1: Prepare Teacher Model
- Train smaller model with RLVR on target task
- Save BOTH pre-RL and post-RL checkpoints
- Ensure both checkpoints use same tokenizer/vocabulary

### Step 2: Compute Log-Ratio Rewards
```python
# For each state-action pair from teacher:
log_ratio = log(π_post(a|x)) - log(π_pre(a|x))
# This is the implicit reward
```

### Step 3: Train Student Model
```python
# Student training loop:
for batch in student_rollouts:
    implicit_reward = compute_log_ratio(batch, teacher_post, teacher_pre)
    loss = -implicit_reward * log(π_student(a|x))
    loss.backward()
    optimizer.step()
```

### Step 4: Validate Transfer
- Compare student performance vs:
  - Direct RL on student (baseline)
  - Standard distillation from post-RL teacher
  - Student without RL
- Measure sample efficiency improvement

## Error Handling

### Log-Ratio Explosion
If log-ratios become very large:
1. Clip log-ratios to reasonable range (e.g., [-5, 5])
2. Use KL-regularization to prevent student from diverging too far from reference
3. Reduce learning rate

### Vocabulary Mismatch
If teacher and student have different tokenizers:
1. Map tokens to common vocabulary space
2. Use embedding-space alignment before computing log-ratios
3. Consider using subword-level probabilities

### Over-Transfer
If student inherits teacher's limitations:
1. Reduce distillation strength (scale factor on implicit reward)
2. Mix implicit reward with ground-truth reward signal
3. Use multiple teachers with different strengths/weaknesses

## Performance Results (from arXiv:2607.05394)
- Qwen3-1.7B: 48.3% → 62.4% on AIME 2024 (4 hours, 8 A100 GPUs)
- Outperforms step-matched direct RL
- Enables sequential composition of multiple policy shifts
- RL outcomes reusable across model scales as implicit reward signals

## Related Skills
- `opcod-on-policy-co-distillation` — Mutual LLM improvement via co-distillation
- `efficient-opd-distillation` — Efficient on-policy distillation methodology
- `gaussian-grpo` — Gaussian Group Relative Policy Optimization
- `contrastive-on-policy-thinking` — CopT methodology for LLM reasoning

## Resources
- Paper: arXiv:2607.05394 — "Weak-to-Strong Generalization via Direct On-Policy Distillation"
- Project: https://bytedtsinghua-sia.github.io/Direct-OPD/
