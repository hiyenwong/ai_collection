---
name: darwin-family-evolutionary-merging
description: "Training-free evolutionary merging framework for LLMs using MRI-Trust Fusion and adaptive merge genome. Use when: merging LLMs without training, evolutionary model combination, gradient-free weight-space recombination, cross-architecture model breeding, diagnostic-guided model merging, training-free reasoning improvement. Activation: darwin family, evolutionary merging, MRI-Trust Fusion, model merging, gradient-free merging, cross-architecture breeding, training-free LLM, weight-space recombination."
---

# Darwin Family: Evolutionary Merging for LLMs

> Training-free evolutionary merging framework that achieves frontier-level reasoning performance (86.9% GPQA Diamond, #6/1252) through gradient-free weight-space recombination of existing model checkpoints.

## Metadata
- **Source**: arXiv:2605.14386
- **Authors**: Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Junghoon Shin, Minseo Kim
- **Published**: 2026-05-14

## Core Problem

Post-training LLMs is expensive. Can we improve reasoning performance by reorganizing latent capabilities already encoded in existing checkpoints, without any gradient-based training?

## Three Key Innovations

### 1. 14-Dimensional Adaptive Merge Genome
- Fine-grained component-level recombination (attention layers, FFN, embeddings)
- Block-level recombination (layer-group mixing)
- Search space captures architectural flexibility beyond simple linear interpolation

### 2. MRI-Trust Fusion
- **Layer-importance signals**: Diagnostic metrics identify which layers contribute most to reasoning
- **Learnable trust parameter**: Adaptively balances diagnostic signals with evolutionary search
- Avoids naive averaging that dilutes specialized capabilities

### 3. Architecture Mapper
- Enables cross-architecture breeding between heterogeneous model families
- Combines Transformer and Mamba-based components
- Handles structural mismatches through alignment mapping

## Implementation Guide

### Prerequisites
- Multiple LLM checkpoints (same or different architectures)
- Evaluation benchmark for fitness scoring
- Compute for inference-based evaluation (no gradients needed)

### Step-by-Step

1. **Genome Definition**
   ```python
   # 14-dimensional merge parameters
   genome = {
       'embed_ratio': 0.5,
       'attn_q_ratio': 0.3,
       'attn_kv_ratio': 0.7,
       'ffn_up_ratio': 0.4,
       'ffn_down_ratio': 0.6,
       # ... per-layer parameters
   }
   ```

2. **MRI-Trust Layer Analysis**
   ```python
   # Diagnostic analysis per layer
   layer_importance = compute_layer_importance(
       model, benchmark, metric='reasoning_accuracy'
   )
   trust_param = optimize_trust(layer_importance)
   ```

3. **Evolutionary Search**
   ```python
   # Population-based search over merge genomes
   for generation in range(n_gens):
       fitness = [evaluate(genome, benchmark) for genome in population]
       population = select_and_mutate(population, fitness)
   ```

4. **Cross-Architecture Mapping**
   ```python
   # Map between Transformer and Mamba components
   mapping = architecture_mapper(transformer_model, mamba_model)
   merged = apply_merge(mapping, best_genome)
   ```

## Applications
- Training-free LLM capability improvement
- Multi-model ensemble without inference overhead
- Cross-architecture knowledge transfer
- Resource-efficient reasoning model scaling (4B to 35B)
- Recursive multi-generation model evolution

## Pitfalls
- **Evaluation cost**: Fitness evaluation requires full benchmark runs — expensive for large populations
- **Architecture compatibility**: Cross-architecture merging requires careful component alignment
- **Overfitting to benchmark**: Evolutionary search may optimize for specific benchmark rather than general capability
- **Trust parameter tuning**: MRI-Trust requires domain-specific diagnostic metrics

## Related Skills
- near-policy-distillation
- sd-search-on-policy-hindsight-distillation
- hybrid-quantum-classical-framework