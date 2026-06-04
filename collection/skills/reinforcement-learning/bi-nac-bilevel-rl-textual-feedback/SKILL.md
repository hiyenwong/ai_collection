---
name: bi-nac-bilevel-rl-textual-feedback
description: Bilevel Natural Language Actor-Critic (Bi-NAC) methodology — joint training of a critic to generate reward-improving textual feedback and an actor to exploit it, formulated as a Stackelberg bilevel program for RL with learnable textual feedback.
---

# Bi-NAC: Bilevel Natural Language Actor-Critic

**Paper**: RL with Learnable Textual Feedback: A Bilevel Approach
**arXiv**: 2605.24547
**Authors**: Utsav Singh, Sidhaarth Sredharan, Souradip Chakraborty, Amrit Singh Bedi
**Submitted**: 23 May 2026

## Core Idea

Reinforcement learning with verifiable rewards can improve LLM reasoning, but learning is sample-inefficient when terminal rewards are sparse. Existing methods treat textual feedback from a critic as fixed or auxiliary, missing a key property: **feedback should not merely be correct, but should improve the policy (actor model) when provided in context**.

This work formalizes the coupling between feedback generation and policy learning as a **Stackelberg bilevel program**, and derives **Bilevel Natural Language Actor-Critic (Bi-NAC)**.

## Key Contributions

1. **Identifies the learnable textual feedback problem**: Feedback should be optimized to improve the policy, not just to be correct.
2. **Bilevel formulation**: The actor's learning depends on the quality of feedback, while the feedback's usefulness depends on the actor's ability to exploit it.
3. **Bi-NAC algorithm**: Jointly trains a critic (upper-level) to generate reward-improving feedback and an actor (lower-level) that exploits it.
4. **Strong empirical results**: 2B model beats 3B GRPO on MATH-500 (46.6% vs 41.4%); 6B model beats 7B GRPO on GPQA (49.3% vs 43.6%).

## Method Details

### Bilevel Formulation (Stackelberg Game)

**Upper-level (Critic)**: Generate feedback `f` that maximizes the actor's expected reward.

**Lower-level (Actor)**: Learn policy that maximizes reward given feedback.

### Bi-NAC Algorithm

1. **Actor update**: Standard policy gradient with augmented reward (scalar reward + textual feedback utility)
2. **Critic update**: Optimize feedback generation to maximize downstream actor performance
3. **Alternating optimization**: Iterate between actor and critic updates

### Architecture
- **Actor**: LLM-based reasoning model (e.g., 2B, 6B parameters)
- **Critic**: LLM-based feedback generator producing natural language critiques
- **Feedback mechanism**: Critic output prepended to actor's context as textual guidance

## Key Formulas

### Policy Gradient with Feedback
∇J(θ_actor) = E[ ∇log π_θ(a|s,f) · (R(s,a) + λ · U(f,a)) ]

### Critic Feedback Optimization
∇J(θ_critic) = E[ ∇_f R(s,a) · ∇_θ_critic f ]

## Implementation Considerations

- Use separate LoRA adapters for actor and critic on a base LLM
- Feedback utility function U(f,a) measures how much feedback improves output
- Alternating update: 1 critic step per K actor steps
- Temperature scaling for feedback diversity during critic training

## Activation Keywords

- bilevel RL, textual feedback RL, learnable feedback, natural language actor-critic, Bi-NAC, RL with feedback, Stackelberg RL, feedback-guided RL, critic-generated feedback, LLM reasoning RL

## Related Work

- **GRPO**: Single-level policy optimization without learnable feedback
- **RL with verifiable rewards**: Sparse terminal rewards, no intermediate signal
- **RLHF**: Human feedback as reward model, not learnable textual feedback
