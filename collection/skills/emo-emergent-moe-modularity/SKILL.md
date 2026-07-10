---
name: emo-emergent-moe-modularity
description: "Expert guidance for designing modular Mixture-of-Experts (MoE) architectures using emergent document-level expert grouping. Based on EMO paper (arXiv:2605.06663). Use when designing sparse LLM architectures, MoE modularity, expert specialization, memory-efficient LLM deployment, or composable model architectures."
---

# EMO: Emergent Modularity in Mixture-of-Experts

Based on: *EMO: Pretraining Mixture of Experts for Emergent Modularity* (arXiv:2605.06663)
Authors: Ryan Wang, Akshita Bhagia, Sewon Min

## Problem

Standard MoE models degrade severely when restricting inference to a subset of experts per domain, preventing modular, memory-efficient deployment. Expert specialization occurs at low-level syntactic patterns rather than semantic domains.

## Key Innovation

EMO enables **emergent modularity** — independent use and composition of expert subsets — without human-defined priors:

1. **Document-level expert grouping**: Tokens within a document share an expert pool
2. **Cross-document diversity**: Different documents use different expert pools
3. **Shared pool constraint**: Simple document-boundary constraint enables coherent expert groupings during pretraining

## Architecture

Unlike per-layer expert ownership:
- Full model matches standard MoE performance
- 25% expert retention → only 1% drop
- 12.5% expert retention → only 3% drop

## Key Findings

1. **Semantic specialization**: EMO experts specialize at domain level (math, code, etc.)
2. **Standard MoE specialization**: Low-level syntactic patterns
3. **Modular deployment**: Subset of experts can be independently loaded
4. **Memory efficiency**: Composable architectures for constrained settings

## Implementation Patterns

### Pattern 1: Document-Bounded Expert Sharing
- For each document, restrict expert selection to a shared subset
- All tokens in document select from same expert pool
- Pool is shared across all tokens within document boundary

### Pattern 2: Modular Expert Deployment
- Load only domain-specific experts for inference
- Identify which experts specialize per domain
- Retains performance with fraction of parameters

## Activation Keywords

- emo moe
- emergent modularity
- mixture of experts modularity
- expert subset deployment
- composable MoE
- memory-efficient MoE
- modular LLM deployment

## Implementation Steps

1. **Pretraining Setup**
   - Pretrain 1B-active/14B-total on 1T tokens
   - Use document boundaries for expert pool restriction
   - Standard MoE as baseline comparison

2. **Expert Specialization Analysis**
   - Analyze which experts fire on which domains
   - Compare semantic vs syntactic specialization
   - Measure performance at various expert retention rates

3. **Modular Deployment**
   - Identify expert subsets per domain
   - Test independent loading and composition
   - Validate performance under memory constraints

## Pitfalls

1. **Too small expert pools** → performance degradation below 12.5% retention
2. **Random document boundaries** → disrupts expert clustering
3. **No comparison baseline** → always compare against standard MoE at same scale

## Related Skills

- moe-optimal-transport-routing
- routing-distraction-multimodal-moe
- unipool-shared-expert-moe

## References

- arXiv:2605.06663
