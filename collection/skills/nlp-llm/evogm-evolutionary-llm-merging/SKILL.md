---
name: evogm-evolutionary-llm-merging
description: "Evolutionary Generative Merging (EvoGM) framework for training-free LLM composition via learnable generative modeling and dual-generator architecture with cycle-consistent learning"
---

# EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization

**arXiv**: [2605.29295](https://arxiv.org/abs/2605.29295)
**Date**: 2026-05-28
**Conference**: ICML 2026
**Categories**: cs.NE (Neural and Evolutionary Computing)

## Background

Evolutionary model merging provides a powerful framework for automated, training-free composition of LLMs through parameter-space search. However, existing methods rely on stochastic, hand-crafted operators that overlook the underlying performance landscape of the coefficient space.

## Methodology

### Core Innovation

EvoGM transcends manual heuristics by employing **learnable generative modeling** to optimize merging coefficients, replacing stochastic search operators with adaptive sampling.

### Dual-Generator Architecture

1. **Cycle-consistent learning**: Two generators sample and refine merging candidates
2. **Winner-loser pairs**: Constructed from historical search trajectories
3. **Distribution capture**: Effectively captures high-performance parameter distributions
4. **Data efficiency**: Maximizes utility of search history

### Multi-Round Evolutionary Pipeline

- Elite merged models iteratively serve as new expert foundations
- Generative process seamlessly integrated into evolutionary loop
- Progressive refinement through learned coefficient distributions

## Key Findings

### Performance

- Significantly outperforms state-of-the-art baselines
- Robust performance on both seen and unseen tasks
- Training-free approach eliminates expensive fine-tuning

### Advantages over Prior Methods

1. **Learned operators** vs. hand-crafted stochastic search
2. **Adaptive coefficient sampling** vs. random perturbation
3. **Historical trajectory exploitation** vs. single-round search
4. **Multi-round refinement** vs. single-pass merging

## Applications

### Use Cases

1. **LLM ensemble creation**: Merge multiple specialized models
2. **Cross-domain adaptation**: Combine models with different capabilities
3. **Efficient deployment**: Training-free model composition
4. **Resource optimization**: Avoid expensive fine-tuning

### Trigger Keywords

`LLM merging`, `model composition`, `evolutionary optimization`, `training-free`, `generative modeling`, `coefficient optimization`, `ensemble models`, `ICML 2026`

## Pitfalls

1. **Generator initialization**: Poor initialization may lead to slow convergence
2. **Winner-loser imbalance**: Need sufficient search history for effective pairs
3. **Coefficient space complexity**: High-dimensional merging coefficients require careful modeling
4. **Computational overhead**: Multi-round evolution increases total computation time vs. single-pass methods

## References

- arXiv paper: https://arxiv.org/abs/2605.29295
- Code repository: Available via paper link
- Related: `darwin-family-evolutionary-merging` (alternative evolutionary merging approach)

## Technical Details

### Generator Learning Objective

Cycle-consistent learning ensures both generators produce high-quality merging candidates through mutual refinement:

- Generator G1: Samples from coefficient distribution
- Generator G2: Refines sampled candidates
- Consistency constraint: Winner-loser discrimination

### Evolutionary Loop Structure

```pseudo
Round 1: Initialize with base models → Search → Elite selection
Round 2: Elite → Generator training → Sample → Evaluate → Elite selection
Round N+: Progressive refinement with learned distributions
```

## Related Skills

- [[darwin-family-evolutionary-merging]] - Alternative evolutionary approach to LLM merging
- [[model-merging-patterns]] - General patterns for model composition