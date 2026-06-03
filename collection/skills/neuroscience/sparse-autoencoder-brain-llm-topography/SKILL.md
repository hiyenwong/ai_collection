---
name: sparse-autoencoder-brain-llm-topography
description: "Sparse Autoencoders (SAEs) from mechanistic interpretability bridge LLM internal representations with cortical semantic topography in human brains. Decomposes LLMs (GPT-2 XL, Llama-3.1-8B) into 16K-32K interpretable features per layer; semantic features recover 94% of brain encoding performance. Five a priori semantic subcategories map onto distinct brain regions via formal convergence testing. Validated across English, Chinese, French. Accepted at CoNLL 2026. Activation: sparse autoencoder, brain-LLM alignment, cortical topography, SAE brain mapping, semantic encoding, computational neurolinguistics."
arxiv_id: "2605.23035"
published: "2026-05-21"
authors: "Dongxin Guo, Jikun Wu, Siu Ming Yiu"
tags: [brain-llm-alignment, sparse-autoencoders, cortical-topography, mechanistic-interpretability, neurolinguistics]
---

# Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography

> This paper bridges mechanistic interpretability (sparse autoencoders) with computational neurolinguistics by decomposing LLM internal representations into interpretable features and showing that semantic features alone recover 94% of neural encoding performance and map onto known cortical semantic topography.

**Source**: arXiv: [2605.23035](https://arxiv.org/abs/2605.23035) | Accepted at CoNLL 2026

## Core Methodology

### Key Innovation
The paper addresses a key gap in computational neurolinguistics: why intermediate layers of LLMs best predict human brain responses to language. It decomposes this question using sparse autoencoders (SAEs) to identify interpretable features within LLMs that align with brain activity.

### Technical Framework

1. **SAE Training on LLMs**: Train sparse autoencoders on GPT-2 XL and Llama-3.1-8B activations to extract 16K-32K interpretable features per layer
2. **Human-Validated Feature Taxonomy**: A structured taxonomy categorizes SAE-discovered features into semantic, syntactic, positional, and other types
3. **Encoding Model Framework**: Use SAE features as predictors in brain encoding models to predict fMRI responses to natural language stimuli
4. **Feature-Importance Analysis**: Quantify each feature category's unique contribution to brain prediction performance
5. **Cortical Topography Prediction**: Test whether five a priori semantic subcategories (derived from neuroscience) map onto distinct brain regions
6. **Cross-Lingual Validation**: Validate across English, Chinese, and French

### Key Results
- **94% recovery** of peak encoding performance using semantic features alone (ρ=.254 vs ρ=.270 baseline)
- **Substantially exceeds** variance-matched baselines (ρ=.238, ρ=.193)
- **Formal convergence test** confirms cortical topography alignment (Spearman ρ=1.0, hypergeometric p<.001)
- **Reading time prediction**: SAE features predict human reading times beyond lexical controls (ΔR²=.083, p<.01)
- **Prediction-error analysis**: Preliminary evidence that the brain encodes unexpected semantic content
- **Generalizes across** English, Chinese, and French

## Applications

- **Brain-LLM alignment analysis**: Use SAEs to map which types of LLM features drive neural prediction
- **Language model interpretability**: Understand what LLM layers encode in terms of brain-relevant features
- **Cross-lingual neuroscience**: Study how semantic representations organize across languages in the brain
- **Reading time modeling**: Build better models of human language processing using semantically-informed features

## Related Skills

- brain-llm-key-neurons-grammar
- fcn-llm-brain-network-understanding
- representation-steering
- mllm-brain-alignment-task-probing
