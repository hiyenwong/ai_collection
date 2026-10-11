---
name: safe-actions-obligation-guard
description: "Safe actions alone do not ensure safe agents. Identifies unfulfilled obligations as major safety risk (56.92% of trajectories). Introduces ObligationBench and ObligationGuard for obligation identification."
tags: [agent-safety, obligations, guard-models, benchmark, safety-critical-actions, unfulfilled-obligations]
source: "arXiv:2610.11773"
utility_score: 0.88
---

# Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models

## Paper Metadata

- **arXiv ID**: 2610.11773
- **Title**: Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models
- **Authors**: Youwei Feng, Yitong Zhang, Yuetong Liu, Jia Li, et al.
- **Published**: 2026-10-08
- **Categories**: cs.AI
- **Link**: https://arxiv.org/abs/2610.11773
- **Code**: https://github.com/THU-Agent/ObligationGuard

## Abstract Summary

Guard models are increasingly used to safeguard LLM-based agents, primarily by identifying actions that agents are forbidden to perform. However, identifying forbidden actions alone is insufficient to ensure agent safety. This work argues that agent safety also depends on identifying required yet unperformed safety-critical actions, called obligations. A preliminary study shows that 56.92% of GLM-5.3 trajectories contain unfulfilled obligations, compared with only 30.00% containing forbidden actions. This reveals unfulfilled obligations as a major and previously overlooked source of safety risk. The work introduces ObligationBench, the first benchmark for evaluating obligation identification capability, comprising 240 expert-validated trajectories. Evaluation of 14 representative models reveals substantial limitations: highest recall is only 48.97%. ObligationGuard achieves 57.52% recall and 21.67% exact-match rate, surpassing all evaluated models.

## Key Contributions

1. **Obligation identification**: Shifts focus from forbidden actions to required but unperformed safety-critical actions
2. **Empirical finding**: 56.92% of trajectories contain unfulfilled obligations vs. 30.00% with forbidden actions
3. **ObligationBench**: First benchmark for evaluating obligation identification (240 expert-validated trajectories)
4. **ObligationGuard**: Trained model achieving 57.52% recall (vs. 48.97% best baseline)
5. **Safety paradigm shift**: Demonstrates safe actions alone are insufficient for safe agents

## Research Implications

- **Safety redefinition**: Agent safety requires both avoiding forbidden actions AND fulfilling obligations
- **Benchmark gap**: No existing benchmark evaluated obligation identification before this work
- **Model limitations**: Even best models have low recall (48.97%) for obligation identification
- **Training approach**: Synthetic data (40,000 examples) can improve obligation identification
- **Community call**: Incorporates obligation identification into future guard model design and evaluation

## Practical Applications

- Build comprehensive guard models that check both forbidden actions and unfulfilled obligations
- Evaluate agent safety using ObligationBench
- Deploy ObligationGuard for real-time obligation monitoring
- Design agent systems with explicit obligation tracking
- Create safety protocols that verify required actions are performed

## Related Work

- Guard models and safety filters
- LLM agent safety
- Benchmark design for AI safety
- Safety-critical action identification
- Agent oversight and monitoring
