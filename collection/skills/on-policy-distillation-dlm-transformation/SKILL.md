---
name: on-policy-distillation-dlm-transformation
description: On-Policy Distillation (OPD) methodology for transforming autoregressive models into diffusion language models efficiently, eliminating train-inference mismatch.
authors:
  - Xingyu Su
  - Jacob Helwig
  - Shubham Parashar
date: 2026-06-04
arxiv: 2606.06712v1
tags:
  - LLM
  - distillation
  - diffusion
  - efficiency
  - model-transformation
---

# On-Policy Distillation for DLM Transformation

## Overview

On-Policy Distillation (OPD) enables efficient transformation of autoregressive language models (ARLMs) into diffusion language models (DLMs) by eliminating two critical distribution shifts:
1. Objective shift from next-token prediction to DLM objective
2. Train-inference mismatch in standard DLMs

## Key Innovation

**OPDLM Framework:**
- Student: ARLM with bidirectional attention (generates own trajectories)
- Teacher: Original frozen ARLM (provides target logits on student trajectories)
- Training: Direct on-policy manner, no random masking

**Results:** 15x to 7,000x fewer training tokens required

## Methodology

### Phase 1: Architecture Modification
1. Replace causal attention in ARLM with bidirectional attention
2. Freeze original ARLM as teacher
3. Initialize student with modified architecture

### Phase 2: On-Policy Training Loop
```
for each batch:
    # Student generates trajectory
    trajectory = student.generate_on_policy()
    
    # Teacher provides supervision
    target_logits = teacher.get_logits(trajectory)
    
    # Distillation loss
    loss = KL(student_logits, target_logits)
    
    # Backprop on student only
    student.backward(loss)
```

### Phase 3: Eliminating Train-Inference Mismatch
- Standard DLMs train on randomly masked sequences
- OPDLM trains on trajectories encountered at inference
- Confidence-based decoding alignment preserved

## Reusable Patterns

### Pattern 1: Self-OPD
**Use when:** Transforming pretrained models to new objectives
**Steps:**
1. Freeze original model as teacher
2. Modify student architecture for new objective
3. Generate trajectories with student
4. Distill teacher knowledge on student's own trajectories

### Pattern 2: Train-Inference Alignment
**Use when:** Objective mismatch causes performance degradation
**Principle:** Train directly on inference-time trajectories, not synthetic training data

### Pattern 3: Efficient Model Transformation
**Use when:** Pretraining from scratch is prohibitive
**Approach:** Treat transformation as post-training rather than retraining

## Implementation Considerations

### Memory Efficiency
- Teacher frozen (no optimizer state)
- Student generates trajectories (no storage of all sequences)
- On-policy training avoids caching random masks

### Computational Efficiency
- One forward pass per trajectory generation
- Teacher provides logits without gradients
- 15x-7000x token reduction vs. full DLM pretraining

### Quality Preservation
- Knowledge retention via distillation from original ARLM
- Bidirectional attention enables DLM-style reasoning
- No degradation from objective shift

## Extensions

### Multi-Objective Transformation
- Extend OPD to multiple downstream objectives
- Sequential transformation through OPD stages

### Domain-Specific Adaptation
- Apply OPD for domain transfer (e.g., code generation)
- Use domain-specific teacher supervision

### Hybrid Architectures
- Combine ARLM and DLM components via OPD bridges
- Mixed causal/bidirectional attention patterns

## Pitfalls

1. **Teacher-Student Architecture Mismatch**: Ensure student can generate valid trajectories for teacher evaluation
2. **Trajectory Quality**: Poor student trajectories lead to weak teacher supervision early on
3. **Convergence Speed**: On-policy training may be slower initially than off-policy alternatives
4. **Evaluation Metrics**: Standard ARLM metrics may not capture DLM benefits

## Related Methods

- Standard DLM training (random masking)
- Off-policy distillation (fixed datasets)
- Knowledge distillation (teacher-student on same architecture)
- Progressive training (growing model capacity)

## Code Reference

Paper implementation not released, but methodology follows:
- Teacher: Frozen ARLM (e.g., Llama, Mistral)
- Student: Bidirectional attention modification
- Training loop: Student-generated trajectories + teacher KL loss

## Applications

- ARLM to DLM transformation
- Efficient diffusion model training
- Model architecture modification without retraining
- Objective transfer in pretrained models

## Activation Keywords

`OPD`, `on-policy distillation`, `ARLM to DLM`, `diffusion language model`, `model transformation`, `train-inference mismatch`, `bidirectional attention`, `efficient pretraining alternative`