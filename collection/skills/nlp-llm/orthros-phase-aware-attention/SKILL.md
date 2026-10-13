---
name: orthros-phase-aware-attention
description: 'Orthros: Phase-aware heterogeneous attention for efficient Transformers with 21.9x prefilling speedup. Use when optimizing long-context Transformer inference with phase-aware decoupling.'
arxiv_id: '2610.13735'
utility: 0.87
authors: Yuhong Chou, Zehao Liu, Yuqi Pan, Qian Liu, Xianwei Chen
categories: [cs.LG, cs.AI]
tags: [transformer, attention, efficiency, long-context, inference-optimization]
---

# Orthros: Phase-Aware Heterogeneous Attention

## Key Innovation

Shifts efficiency paradigm from structural allocation to phase-aware decoupling. As a unified module, dynamically switches computation patterns across different phases of sequence processing: linear complexity prefilling + full attention decoding.

## Method

- Phase-aware decoupling: different attention patterns for prefill vs decode
- Linear complexity during prefilling phase
- Full attention during decoding phase
- Data-efficient Transformer-to-Orthros conversion

## Results

- 21.9x prefilling speedup over Transformers
- Near-perfect 128K needle-in-a-haystack results
- Transformer-level performance on real-world in-context recall
- Conversion surpasses original Transformer performance

## Practical Use

- Long-context LLM serving optimization
- Efficient prefilling for RAG and document processing
- Converting existing Transformers without retraining

## URL

https://arxiv.org/abs/2610.13735
