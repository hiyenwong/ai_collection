---
name: sd-search-on-policy-hindsight-distillation
description: SD-Search methodology for search-augmented reasoning. Derives step-level supervision from the policy itself through on-policy hindsight self-distillation, without external teacher or annotations.
category: ai_collection
---

# SD-Search: On-Policy Hindsight Self-Distillation

## Overview

SD-Search addresses the credit assignment problem in search-augmented reasoning agents. Under outcome-reward RL, every search decision shares the same trajectory-level reward, leaving individual queries without step-specific credit. SD-Search derives step-level supervision from the policy itself through on-policy hindsight self-distillation.

## Core Methodology

### 1. Dual-Role Architecture
- **Student**: Sees only context available at inference time
- **Teacher**: Additionally conditions on a compact hindsight block summarizing search queries and final outcomes of a group of rollouts
- **Same model**, different conditioning — no external teacher needed

### 2. Hindsight Self-Distillation
- Sample a group of rollouts from the same question
- Teacher knows how each rollout unfolded and which succeeded
- Teacher's query distribution implicitly marks valuable decisions
- Student trained to recover teacher behavior via token-level Jensen-Shannon divergence

### 3. Integration with GRPO
- Layers dense step-level signal on top of GRPO's coarse trajectory reward
- Signal produced by policy within standard RL training loop
- No external model inference, annotation pipeline, or additional training stage

### 4. Training Loop
```python
def sd_search_training_step(policy, questions):
    # Step 1: Sample rollout group
    rollouts = sample_group_rollouts(policy, question)
    
    # Step 2: Build hindsight block (queries + outcomes)
    hindsight_block = summarize_rollouts(rollouts)
    
    # Step 3: Teacher forward (with hindsight)
    teacher_logits = policy(context + hindsight_block)
    
    # Step 4: Student forward (without hindsight)
    student_logits = policy(context)
    
    # Step 5: Jensen-Shannon divergence at query positions
    loss = js_divergence(
        teacher_logits[query_positions],
        student_logits[query_positions]
    )
    
    # Step 6: Combine with GRPO trajectory reward
    total_loss = loss + grpo_loss
    
    return total_loss
```

## Advantages Over Alternatives

| Method | External Teacher | Annotations | Training Stages |
|--------|-----------------|-------------|-----------------|
| Process supervision | Required | Required | Multiple |
| SD-Search | None | None | Single |

## Key Design Principles

1. **Self-supervision**: Policy teaches itself via hindsight conditioning
2. **Token-level credit**: JS divergence provides fine-grained step-level signal
3. **No external dependency**: Everything happens within standard RL loop
4. **Group sampling**: Hindsight block summarizes multiple rollouts for contrast

## Activation

sd-search, on-policy distillation, hindsight self-distillation, search-augmented reasoning, step-level credit, process supervision alternative

## Reference

- arXiv: 2605.18299
- "SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning"
