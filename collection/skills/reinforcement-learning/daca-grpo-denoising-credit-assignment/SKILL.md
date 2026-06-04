---
name: daca-grpo-denoising-credit-assignment
description: Denoising-Aware Credit Assignment for GRPO in Diffusion Language Models. Introduces Denoising Progress Scores and Stratified Masking Likelihood to improve GRPO-style training for diffusion LLMs, achieving gains up to 5.6pp on math reasoning, 7.4pp on code generation, and 36.3pp on constraint satisfaction.
---

# DACA-GRPO: Denoising-Aware Credit Assignment for RL in Diffusion Language Models

## Core Methodology

DACA-GRPO addresses two fundamental weaknesses in RL for diffusion language models:
1. **Absence of temporal credit assignment** across the denoising trajectory
2. **Systematic bias** of mean-field likelihood estimates used for policy optimization

### Key Mechanisms

#### Denoising Progress Scores (DPS)
- Extracts per-token importance weights from intermediate predictions at no additional forward cost
- Tokens that contribute more to denoising progress receive higher importance weights
- Computed from the change in prediction confidence across denoising steps

#### Stratified Masking Likelihood (SML)
- Partitions token positions into strata so each token is predicted with most of the sequence as context
- Reduces the mean-field bias inherent in independent token likelihood estimation
- Each token sees a different masking pattern, providing better context coverage

## Implementation Notes

1. **Plug-and-play**: DACA-GRPO is a lightweight enhancement for any GRPO-style trainer
2. **No additional forward passes**: DPS extraction uses existing intermediate predictions
3. **Compatible with existing GRPO variants**: Works on top of GRPO, GSPO, REINFORCE++, etc.
4. **Stratified masking**: Implement token partitioning to reduce mean-field bias

## Performance Gains
- Mathematical reasoning: up to +5.6pp
- Code generation: up to +7.4pp  
- Constraint satisfaction: up to +36.3pp
- JSON schema adherence: up to +5.9pp

## Applications
- RL training for diffusion language models
- Improving GRPO-style policy optimization
- Diffusion-based code generation and reasoning
- Constrained generation with structural requirements

## Activation Keywords
daca-grpo, denoising credit assignment, diffusion language model, GRPO enhancement, stratified masking, denoising progress scores, diffusion LLM RL
