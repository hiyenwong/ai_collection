---
name: lpact-brain-lm-alignment-evaluation
description: "L-PACT framework for evaluating brain-language model alignment. Goes beyond prediction scores to assess predictive, relational, mechanism-stripping, and reliability-bounded evidence."
---

# L-PACT: Brain-Language Model Alignment Evaluation Framework

**Source:** arXiv:2605.14025 (May 15, 2026)
**Title:** Do Language Models Align with Brains? Prediction Scores Are Not Enough
**Categories:** q-bio.NC, cs.AI, cs.LG (likely)

## Problem Statement

Brain-language model comparisons often interpret neural prediction scores as evidence that model representations capture brain-relevant language computation. This paper challenges that assumption by asking whether prediction scores alone are sufficient to support claims of brain-model alignment.

## Key Innovation: L-PACT Framework

L-PACT is a **source-audited framework** that evaluates alignment across four evidence dimensions:

### 1. Predictive Evidence
- Standard brain-to-model prediction scores
- How well model features predict brain activity patterns
- Baseline evaluation using naturalistic language neural datasets

### 2. Relational Evidence
- Tests whether model-to-brain profiles reproduce brain-to-brain patterns
- Compares model representations against inter-subject brain similarity
- Goes beyond simple prediction to capture relational structure

### 3. Mechanism-Stripping Evidence
- Recomputes held-out scores after removing ("stripping") specific mechanisms
- Tests whether claimed alignment depends on specific model components
- Validates that alignment is not due to trivial or spurious correlations

### 4. Reliability-Bounded Evidence
- Normalizes evidence against brain-brain ceilings
- Accounts for measurement noise and reliability limits
- Provides upper bounds on achievable alignment

## Methodology

### Evaluation Pipeline:
```
[Neural Datasets] → [LM Representations] → [L-PACT Analysis]
                                                ↓
                              ┌─────────────────┼─────────────────┐
                              ↓                 ↓                 ↓
                       [Predictive]       [Relational]     [Mechanism-Stripping]
                              ↓                 ↓                 ↓
                       Score vs           Pattern           Ablation Study
                       Nuisance Baselines Reproduction     of Components
                              ↓                 ↓                 ↓
                         [Reliability-Bounded Normalization]
                              ↓
                       [Brain-Brain Ceiling Comparison]
```

### Key Comparisons:
- **Real model features** vs **nuisance baselines**
- **Severe controls** to test robustness
- **Brain-to-brain patterns** as ceiling for alignment
- **Mechanism ablation** to validate causal contribution

## Significance for NeuroAI

1. **Challenges prevailing assumptions** about brain-model alignment
2. **Provides rigorous framework** beyond simple prediction scores
3. **Source-audited** methodology ensures transparency
4. **Multi-dimensional evidence** prevents over-interpretation
5. **Establishes brain-brain ceiling** as normalization reference

## Applications

- Evaluating new language models for brain alignment
- Comparing different model architectures
- Validating claims in neuro-AI research
- Designing more brain-inspired language models
- Meta-analysis of brain-model alignment literature

## Implementation Guidance

### When to Use:
- Claiming brain-model alignment in research
- Comparing multiple models for neural prediction
- Validating that alignment is meaningful, not trivial
- Publishing neuro-AI alignment results

### L-PACT Evaluation Steps:
1. **Collect neural data** from naturalistic language tasks
2. **Extract model representations** at multiple layers
3. **Compute predictive scores** with proper baselines
4. **Test relational patterns** (model-brain vs brain-brain)
5. **Perform mechanism stripping** to validate contributions
6. **Normalize against reliability bounds**
7. **Report comprehensive evidence** across all dimensions

## Limitations & Open Questions

- Requires access to high-quality neural datasets
- Computationally intensive (multiple evaluation dimensions)
- Brain-brain ceiling estimation depends on dataset quality
- May need adaptation for different neural recording modalities

## Related Skills

- brain-dnn-transformation-alignment
- neural-encoding-evaluation-ground-truth
- decoding-encoding-alignment-critique
- naturality-violation-score
- lrm-game-learning-brain-alignment
- representation-steering

## Activation Keywords

- L-PACT
- brain model alignment
- brain-language alignment
- neural prediction evaluation
- mechanism stripping
- brain-brain ceiling
- alignment evaluation framework
- language model neuroscience
- brain alignment validation

## References

- arXiv: https://arxiv.org/abs/2605.14025
- PDF: https://arxiv.org/pdf/2605.14025.pdf
