---
name: latent-on-policy-self-distillation
description: "LOPD: learnable privileged context for agentic AI evolution."
metadata:
  arxiv_id: "2608.13040"
  published: "2026-08-13"
  authors: "Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao et al."
  tags: [agentic, reinforcement-learning, distillation, self-evolution]
license: Complete terms in LICENSE.txt
---

# Latent On-Policy Self-Distillation (LOPD)

## Overview

Latent On-Policy Self-Distillation (LOPD) addresses the central problem in self-evolving AI: enabling agents to learn from experience and internalize it into their policy. Unlike existing on-policy self-distillation (OPSD) methods that rely heavily on designer-specified privileged artifacts (answers, feedback, skills, or trajectories), LOPD makes the teacher's privileged context itself learnable end-to-end from experience.

## Key Components

### 1. Continuous Latent Tokens
- Retrieves relevant experiences and composes them into continuous latent tokens
- These tokens condition a self-teacher model
- The latent context is learned end-to-end from experience

### 2. Dense Token-Level Supervision
- Student generates trajectories from task and interaction history
- Receives dense token-level supervision at every visited prefix
- Enables fine-grained learning signal throughout the trajectory

### 3. Privileged-Margin Objective
- Introduced to stabilize and regulate the learning of latent context
- Helps prevent overfitting and ensures robust learning

## Implementation Workflow

### Step 1: Experience Retrieval and Composition
1. Collect agent trajectories and experiences from interactions
2. Implement experience retrieval mechanism to find relevant past experiences
3. Compose retrieved experiences into continuous latent tokens using an encoder

### Step 2: Self-Teacher Conditioning
1. Use the continuous latent tokens to condition the self-teacher model
2. The teacher generates privileged supervision signals based on the latent context
3. Ensure the teacher architecture can effectively utilize the latent conditioning

### Step 3: Student Training with Dense Supervision
1. Generate new trajectories using the student policy
2. Apply dense token-level supervision at every prefix position
3. Compute loss between student predictions and teacher supervision

### Step 4: Privileged-Margin Optimization
1. Implement the privileged-margin objective to regularize latent context learning
2. Balance between learning informative latent representations and preventing overfitting
3. Monitor training stability and adjust margin parameters as needed

## Performance Characteristics

- **Strong performance**: Outperforms RLVR and representative OPSD methods including OPSD, SDPO, and Skill-SD across both agentic tool use and code generation
- **High learning efficiency**: Surpasses GRPO and Skill-SD with less than 30% of their rollout budget
- **Scalability**: Enables end-to-end learnability required for continual self-improvement

## Use Cases

- **Agentic tool use**: Building agents that can learn to use tools more effectively through self-distillation
- **Code generation**: Improving code generation capabilities by learning from past successful generations
- **Self-evolving AI systems**: Creating AI systems that can continually improve without human intervention
- **Experience-based policy internalization**: Transforming external experiences into internal policy improvements

## Activation Keywords

- latent on-policy self-distillation
- LOPD
- self-evolving agents
- learnable privileged context
- continuous latent tokens
- dense token-level supervision
- agentic AI evolution

## References

- **Paper**: [Latent On-Policy Self-Distillation](https://arxiv.org/abs/2608.13040v1)
- **Related Skills**: 
  - `on-policy-distillation-dlm-transformation`
  - `efficient-agentic-reasoning-sr2am`
  - `self-policy-distillation-spd`