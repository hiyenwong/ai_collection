---
name: sae-brain-llm-topography
description: "Sparse Autoencoders (SAEs) bridge mechanistic interpretability with neural encoding models to map LLM features onto cortical semantic topography — decomposing GPT-2 XL and Llama-3.1-8B into 16K-32K interpretable features and showing semantic features dominate brain alignment (94% of peak encoding performance, r=0.285), validated across English/Chinese/French (arXiv: 2605.23035, CoNLL 2026)."
arxiv_id: "2605.23035"
published: "2026-05-21"
authors: "Dongxin Guo, Jikun Wu, Siu Ming Yiu"
tags: [sparse-autoencoder, brain-llm-alignment, mechanistic-interpretability, neural-encoding, semantic-topography, computational-neurolinguistics, fmri-encoding]
---

# SAEs Map Brain–LLM Alignment onto Cortical Semantic Topography

## Core Concept

Bridges **sparse autoencoders (SAEs)** from mechanistic interpretability with **neural encoding models** to explain why intermediate LLM layers best predict human brain responses to language. Decomposes GPT-2 XL and Llama-3.1-8B into 16K–32K interpretable features per layer and tests **cortical topography predictions** derived from three independent neuroscience programs.

## Key Contributions

1. **SAE Decomposition for Brain Encoding**: First work to apply SAEs to decompose LLM representations into interpretable features and evaluate their contribution to brain encoding performance.

2. **Semantic Feature Dominance**: Semantic features alone recover **94% of peak encoding performance** (r=0.285), substantially exceeding variance-matched baselines (p<0.001, d=1.31). Human-validated taxonomy achieves κ≥0.74.

3. **Cortical Topography Prediction**: Five a priori semantic subcategories (from three independent neuroscience programs) map onto distinct brain regions, confirmed by formal convergence test (Spearman ρ=0.72, p<0.001; hypergeometric p=0.007).

4. **Behavioral Validation**: SAE features predict human reading times beyond lexical controls (ΔlogLik=38.4, p<0.001). Prediction-error analysis provides preliminary evidence the brain encodes unexpected semantic content.

5. **Cross-Linguistic Generalization**: Results generalize across English, Chinese, and French.

## Methodology

### SAE Training
- **Models**: GPT-2 XL (1.5B), Llama-3.1-8B
- **Feature count**: 16K–32K interpretable features per layer
- **Sparsity**: Top-k activation with k=32 (GPT-2 XL), k=64 (Llama-3.1-8B)

### Feature Taxonomy
1. **Semantic features**: Categorical semantic information
2. **Syntax features**: Grammatical/syntactic structure
3. **Position features**: Token position encoding
4. **Other/Uninterpretable**: Non-interpretable dimensions

### Brain Encoding Evaluation
- **fMRI data**: Participants reading naturalistic text
- **Encoding model**: Ridge regression from SAE features to voxel responses
- **Evaluation**: Prediction accuracy (Pearson r) on held-out data

### Cortical Topography Test
- Five semantic subcategories derived a priori
- Predicted distinct regional specialization
- Convergence test across independent prediction maps

## Key Findings

| Finding | Evidence |
|---------|----------|
| Semantic features drive brain alignment | 94% of peak performance from semantic alone |
| Syntax features matter less | Variance-matched baselines significantly lower |
| Cortical topography confirmed | Spearman ρ=0.72 across five subcategories |
| Cross-linguistic robust | Same pattern in EN, ZH, FR |
| Reading time prediction | ΔlogLik=38.4 beyond lexical controls |

## Activation Keywords

- sparse-autoencoder-brain, brain-llm-alignment, sae-neural-encoding, cortical-semantic-topography, computational-neurolinguistics, llm-interpretability-fmri, semantic-feature-dominance, cross-linguistic-brain-encoding, sae-gpt2-fmri, sae-llama-fmri, mechanistic-interpretability-encoding, llm-brain-topography, semantic-subcategory-cortex
