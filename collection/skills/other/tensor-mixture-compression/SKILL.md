---
name: tensor-mixture-compression
description: "Tensor Mixture (MixT) compression scheme for large language models — replaces targeted dense linear layers with natively executable mixtures of tensor operators. Works directly on generic linear projections across Transformer-based LLMs. Achieves 47.5% parameter reduction, 37.1% inference FLOPs reduction, 52.1% training FLOPs reduction, and 60.4% peak memory reduction on LLaMA2-7B while preserving MMLU accuracy up to a model-specific transition boundary. Use when: compressing LLMs, tensor-structured model optimization, LLM deployment on resource-constrained hardware, or analyzing LLM compression boundaries."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.25344"
  published: "2026-05-25"
  authors: Ying Lu, Peng-Fei Zhou, Qi-Xuan Fang, Pan Zhang, Shi-Ju Ran, Gang Su
  tags: [llm-compression, tensor-networks, mixture-of-operators, efficient-deployment, transformer-compression]
---

# Tensor Mixture (MixT) Compression for LLMs

## Core Concept

MixT replaces targeted dense linear layers in LLMs with **natively executable mixtures of tensor operators**. Unlike BPE/Unigram (greedy, locally optimal), MixT formulates compression as a tensor-structured optimization that considers the full vocabulary/model structure.

## Key Results (LLaMA2-7B at transition boundary)
- **Parameters**: 47.5% reduction
- **Inference FLOPs**: 37.1% reduction
- **Training FLOPs**: 52.1% reduction
- **Peak inference memory**: 60.4% reduction
- MMLU accuracy preserved until abrupt model-specific transition boundary

## Compression Regime

MixT identifies a **broad compressible regime** where MMLU accuracy is largely preserved, followed by an **abrupt transition** at model-specific boundaries. This transition coincides with coordinated shifts in:
1. Output entropy
2. Prediction entropy
3. Inter-layer geometry

## Application Pattern

1. **Target selection**: Identify dense linear layers for replacement
2. **Tensor operator mixture**: Replace with natively executable mixtures
3. **Recovery protocol**: Validate accuracy preservation
4. **Boundary detection**: Monitor output entropy, prediction entropy, inter-layer geometry for transition signals

## Applicable Models
- Transformer-based LLMs (validated on Qwen3-8B, LLaMA2-7B)
- Any architecture with dense linear mappings

## Activation Keywords
- tensor-mixture-compression
- MixT compression
- LLM tensor compression
- efficient LLM deployment
- transformer model compression
- tensor operator mixture
- LLM memory optimization
- 模型压缩
- 张量混合压缩

## Resources
- Paper: https://arxiv.org/abs/2605.25344
