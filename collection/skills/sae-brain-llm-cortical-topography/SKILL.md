---
name: sae-brain-llm-cortical-topography
description: Sparse Autoencoders (SAEs) bridge mechanistic interpretability with brain encoding models, decomposing LLMs into interpretable features that map onto cortical semantic topography. Use when analyzing brain-LLM alignment via SAE-discovered features, studying semantic feature organization in cortex, or evaluating how LLM internal representations correspond to neural responses across languages.
---

# Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography

Methodology from arXiv:2605.23035 (May 2026). Accepted at CoNLL 2026.

## Overview

This methodology bridges sparse autoencoders (SAEs) from mechanistic interpretability with neural encoding models. It decomposes intermediate layers of LLMs (GPT-2 XL, Llama-3.1-8B) into 16K-32K interpretable features per layer and maps them onto human brain responses via fMRI.

## Key Findings

1. **Semantic features dominate brain alignment**: Semantic features alone recover 94% of peak encoding performance (R²=0.94), substantially exceeding variance-matched baselines (R²=0.63-0.78).

2. **Cortical topography prediction**: Five semantic subcategories (derived a priori from three independent neuroscience programs) map onto distinct brain regions. Formal convergence test confirms alignment (Spearman ρ, p<0.05; hypergeometric p<0.05).

3. **Reading time prediction**: SAE features predict human reading times beyond lexical controls (ΔR², p<0.001).

4. **Cross-linguistic generalization**: Results generalize across English, Chinese, and French.

5. **Prediction-error encoding**: Exploratory analysis provides preliminary evidence that the brain encodes unexpected semantic content.

## Methodology

### Step 1: Train SAEs on LLM Activations
- Train sparse autoencoders on intermediate layer activations of GPT-2 XL and Llama-3.1-8B
- Use 16K-32K learned features per layer
- Apply L1 sparsity penalty during training

### Step 2: Classify Features into Semantic Taxonomy
- Develop a human-validated taxonomy of semantic features
- Classify SAE-discovered features into five semantic subcategories
- Validate classification via human raters

### Step 3: Neural Encoding with SAE Features
- Build encoding models using SAE features to predict fMRI responses
- Compare against variance-matched baselines (random features, PCA components)
- Test across multiple brain regions (IFG, PTL, etc.)

### Step 4: Cortical Topography Analysis
- Test a priori predictions about which brain regions encode which semantic subcategories
- Use convergence tests (Spearman correlation, hypergeometric test)
- Validate against known cortical semantic organization

### Step 5: Behavioral Validation
- Predict reading times from SAE features
- Control for lexical properties (word frequency, length, surprisal)
- Test for prediction-error encoding in brain responses

## Trigger Words
- sparse autoencoder, SAE, mechanistic interpretability, brain encoding
- brain-LLM alignment, cortical topography, semantic feature
- neural encoding model, LLM interpretability, semantic categories
- fMRI encoding, cross-linguistic brain alignment

## Related Skills
- sparse-autoencoder-mechanistic-interpretability
- brain-llm-alignment-training-data
- computational-lesions-multilingual-language-models-separate
