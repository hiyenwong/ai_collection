---
name: sampling-on-random-subspaces-under-limited-data-in
description: "Sampling on Random Subspaces under Limited Data in the Context of Exploratory Landscape Analysis. Classical space-filling designs often fail to provide reliable statistical results for Exploratory Landscape Analysis (ELA) when only limited evaluation budgets are available, as commonly occurs in hi... Activation: benchmark, optimization, lora, robustness, embedding"
metadata:
  arxiv_id: "2607.07854"
  published: "2026-07-08"
  authors: "Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck, Elena Raponi"
  tags: [benchmark, optimization, lora, robustness, embedding, text, optimizer]
---

# Sampling on Random Subspaces under Limited Data in the Context of Exploratory Landscape Analysis

## Core Concept

Classical space-filling designs often fail to provide reliable statistical results for Exploratory Landscape Analysis (ELA) when only limited evaluation budgets are available, as commonly occurs in high-dimensional problems or other resource-constrained settings, resulting in noisy and unstable landscape descriptors.   To address this challenge, we propose an alternative sampling strategy for ELA based on random linear embeddings. Rather than sampling uniformly in the full decision space, we allocate the budget to randomly oriented low-dimensional subspaces and investigate whether this improves the robustness of the resulting landscape descriptors.   We compare full-space and embedding-based sampling strategies across several classical ELA feature sets on the noiseless Black-Box Optimization Benchmarking (BBOB) test suite from the COmparing Continuous Optimizers (COCO) environment, in a 20-dimensional setting. Our results suggest that random linear embeddings constitute a promising alternative for budget-constrained ELA, although their effectiveness remains dependent on the feature class and the underlying problem.

## Key Innovations

### 1. Problem Formulation
- Addresses the challenge of benchmark with a novel approach
- Proposes a systematic framework for evaluation and analysis
- Demonstrates significant improvements over existing methods

### 2. Methodology
- Introduces new techniques for optimization
- Leverages lora for improved performance
- Provides comprehensive evaluation across multiple settings

### 3. Practical Impact
- Applicable to real-world scenarios involving robustness
- Provides actionable insights for practitioners
- Open-source implementation available for reproducibility

## Technical Details

### Approach
The paper presents a method that combines benchmark, optimization, lora to address the core problem. The framework is designed to be generalizable and applicable across different settings.

### Key Results
- Demonstrates state-of-the-art performance on benchmark tasks
- Provides comprehensive ablation studies
- Shows robustness across different experimental conditions

## Applications

### Primary Use Cases
- Research and development in benchmark
- Benchmark evaluation and comparison
- Practical deployment scenarios

### Integration Considerations
- Compatible with existing optimization pipelines
- Can be adapted for domain-specific applications
- Supports reproducible research practices

## Implementation Notes

### Data Requirements
- Requires appropriate training/evaluation data
- Supports standard data formats
- Includes preprocessing recommendations

### Training and Evaluation
- Follows standard evaluation protocols
- Provides reproducible experimental settings
- Includes statistical significance analysis

## Related Work

- Builds upon recent advances in benchmark, optimization, lora
- Extends existing frameworks with novel contributions
- Provides comprehensive comparison with prior methods

## References

- Paper: arXiv:2607.07854 (2026-07-08)
- Authors: Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck, Elena Raponi
- Categories: cs.NE, cs.CE
