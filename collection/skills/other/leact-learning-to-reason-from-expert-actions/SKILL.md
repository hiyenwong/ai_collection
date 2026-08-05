---
name: leact-learning-to-reason-from-expert-actions
description: "LeAct framework for recovering chain-of-thought reasoning from expert systems that only produce actions without explicit reasoning traces, treating CoT as a latent variable optimized via action probability scoring."
---

# LeAct: Learning to Reason from Expert Actions

## Overview
LeAct (Learning to reason from Actions) is a framework for recovering chain-of-thought (CoT) reasoning from expert systems that only produce actions without explicit reasoning traces. This approach treats CoT as a latent variable and optimizes it by sampling candidate CoTs for each expert action, retaining those that improve the student model's probability of recovering the action.

## Key Contributions
- **Latent CoT Recovery**: Treats reasoning as a latent variable to be optimized from expert actions alone
- **Expert System Distillation**: Enables distillation from silent expert systems (game engines, planners, theorem provers)
- **Action-Guided Reasoning**: Uses the expert action as supervision signal for CoT quality
- **Scalable Performance**: Achieves 5× closer to solver than expert-iteration baselines at large scale
- **Cross-Domain Generalization**: Works across imperfect-information games and robotics benchmarks

## Methodology
1. **Expert Action Collection**: Gather near-optimal actions from expert systems across diverse domains
2. **CoT Sampling**: Student model samples multiple candidate reasoning traces for each expert action
3. **Action Probability Scoring**: Evaluate each CoT by measuring how much it improves the student's probability of producing the expert action
4. **Retain High-Scoring CoTs**: Keep CoTs that measurably improve action recovery probability
5. **Iterative Refinement**: Use retained CoTs to train the student model for better reasoning generation

## Applications
- **Game AI**: Extract strategic reasoning from game solvers in imperfect-information games like poker
- **Robotics**: Recover planning logic from optimal control policies in simulated environments  
- **Theorem Proving**: Distill proof strategies from automated theorem provers
- **Classical Planning**: Extract planning heuristics from optimal planners
- **Foundation Model Training**: Create new sources of reasoning data beyond human annotations or LLM distillation

## Implementation Guidelines
- Use temperature-controlled sampling for diverse CoT candidates
- Implement action probability scoring with proper normalization
- Apply filtering thresholds to retain only significantly improved CoTs
- Consider domain-specific constraints when sampling reasoning traces
- Validate generalization by testing on held-out expert actions

## Evaluation Metrics
- **Action Recovery Accuracy**: Probability of student reproducing expert actions
- **Reasoning Quality**: Human evaluation or automated metrics for CoT plausibility
- **Generalization Gap**: Performance difference between training and test expert actions
- **Computational Efficiency**: Cost of CoT sampling vs. quality improvement

## Activation Triggers
Use LeAct when:
- You have access to expert systems that produce optimal actions but no reasoning traces
- You need to distill reasoning capabilities into foundation models
- Traditional CoT collection (human annotation, LLM distillation) is insufficient
- Working with domains where expert actions are available but explanations are not
- Building agentic systems that need to learn from optimal behavior demonstrations

## References
- Yang, Z., Shi, C., Ghugare, R., Eysenbach, B., Narasimhan, K., & Jin, C. (2026). LeAct: Learning to Reason from Expert Actions. arXiv:2607.21856.