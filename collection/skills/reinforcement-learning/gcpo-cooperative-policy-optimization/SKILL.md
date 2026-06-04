---
name: gcpo-cooperative-policy-optimization
description: Group Cooperative Policy Optimization (GCPO) replaces GRPO's winner-takes-all competition with team cooperation. Rollouts are rewarded by contribution to team's valid solution coverage, measured as determinant volume over reward-weighted semantic embeddings. Solves exploration collapse in RLVR for LLM reasoning.
---

# GCPO: Group Cooperative Policy Optimization for Diverse LLM Reasoning

## Core Methodology

GCPO addresses exploration collapse in RLVR (Reinforcement Learning with Verifiable Rewards), where GRPO causes models to prematurely converge on narrow high-scoring patterns.

### Key Innovation: Team Cooperation over Competition

Instead of independent rollout scoring, GCPO implements team-level credit assignment:

1. **Coverage-based scoring**: A rollout is rewarded by how much it contributes to the team's valid solution coverage, not individual accuracy
2. **Determinant volume metric**: Coverage is described as determinant volume over reward-weighted semantic embeddings
   - Only correct AND non-redundant rollouts contribute to this volume
   - Redundant correct answers add no value
3. **Marginal contribution redistribution**: During advantage estimation, collective team reward is redistributed to each rollout according to its average marginal contribution

## Implementation Details

1. **Semantic embedding space**: Compute embeddings for each rollout's reasoning path
2. **Reward weighting**: Weight embeddings by correctness (verified rewards)
3. **Volume computation**: Calculate determinant volume of the coverage space
4. **Shapley-value-like redistribution**: Distribute team reward based on marginal contributions

## Advantages over GRPO
- Eliminates winner-takes-all dynamics that cause exploration collapse
- Naturally rewards diverse, correct reasoning paths
- No need for hand-tuned entropy regularization or diversity bonuses
- Incentivizes novel solutions that complement team coverage

## Applications
- LLM reasoning with verifiable rewards (RLVR)
- Mathematical reasoning tasks requiring multiple solution strategies
- Code generation with diverse valid implementations
- Any RLVR scenario where solution diversity is valuable

## Activation Keywords
gcpo, cooperative policy optimization, exploration collapse, RLVR, diverse reasoning, team credit assignment, winner-takes-all, determinant volume
