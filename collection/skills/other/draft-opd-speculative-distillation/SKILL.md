---
name: draft-opd-speculative-distillation
description: On-Policy Distillation for Speculative Draft Models - training draft models for speculative decoding with replay from verification-exposed error positions
version: 1.0.0
author: Hermes Agent (from arXiv 2605.29343)
tags: [LLM, speculative-decoding, distillation, inference-optimization]
activation_keywords: [speculative decoding, draft model, EAGLE, DFlash, acceptance length, on-policy distillation]
---

# Draft-OPD: On-Policy Distillation for Speculative Draft Models

## Overview

Draft-OPD addresses the offline-to-inference mismatch in speculative decoding draft model training. Standard supervised fine-tuning (SFT) on target-generated trajectories plateaus because the draft model learns from fixed trajectories but is evaluated on blocks proposed under its own policy during inference.

## Core Methodology

### Problem Identification
- **SFT Plateau**: Draft model acceptance length stops improving on test data
- **Root Cause**: Offline-to-inference mismatch - SFT uses fixed target trajectories, but inference evaluates draft-induced states

### Solution: Draft-OPD
1. **Target-Assisted Rollout**: Use target model for stable continuations during training
2. **Error Position Replay**: Replay drafting from verification-exposed error positions
3. **Dual Feedback Learning**: Learn from both accepted and rejected proposals

## Implementation Steps

### Step 1: Setup Training Infrastructure
```python
# Core components needed:
# - Target model (LLM to accelerate)
# - Draft model (lightweight model for token proposals)
# - Verification module (parallel token acceptance check)
```

### Step 2: On-Policy Training Loop
```python
def draft_opd_training_step(draft_model, target_model, prompt):
    # Generate draft-induced states
    draft_tokens = draft_model.generate(prompt, max_length=32)
    
    # Get target verification
    accepted, rejected_positions = verify_with_target(target_model, draft_tokens)
    
    # Replay from error positions
    for error_pos in rejected_positions:
        draft_model.learn_from_target_feedback(
            state=prompt[:error_pos],
            target_action=target_model.predict(prompt[:error_pos])
        )
    
    return draft_model
```

### Step 3: Verification-Exposed Error Replay
- Collect sequences where draft proposals were rejected
- Use target model supervision at error positions
- Focus training on draft-induced errors that limit acceptance

## Key Results
- **5× lossless acceleration** for thinking models
- **23% improvement** over EAGLE-3
- **13% improvement** over DFlash

## When to Use
- Training draft models for speculative decoding (EAGLE, DFlash style)
- When SFT plateau is observed in draft model training
- For inference acceleration of reasoning/thinking models

## Pitfalls
- Cannot use pure on-policy rollout (draft model can't generate complete sequences)
- Avoid target-assisted-only training (eliminates on-policy signal)
- Need proper verification module to expose error positions

## References
- arXiv: 2605.29343v1
- Authors: Haodi Lei, Yafy Li, Haoran Zhang et al.
- Published: 2026-05-28