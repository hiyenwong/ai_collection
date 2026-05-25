---
name: sae-brain-llm-topography
description: "Sparse Autoencoders (SAEs) from mechanistic interpretability bridge brain-LLM alignment with cortical semantic topography prediction"
version: 1.0.0
author: arXiv 2605.23035 (Dongxin Guo, Jikun Wu, Siu Ming Yiu)
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [SAE, Brain-LLM-Alignment, Mechanistic-Interpretability, Neural-Encoding, Computational-Neurolinguistics, Sparse-Autoencoders, Cortical-Topography]
    related_skills: [sparse-autoencoder-brain-llm-topography, brain-llm-key-neurons-grammar, in-context-brain-decoding]
---

# Sparse Autoencoders Map Brain–LLM Alignment onto Cortical Semantic Topography

**Paper**: arXiv:2605.23035 (May 2026) — Accepted at **CoNLL 2026**  
**Authors**: Dongxin Guo, Jikun Wu, Siu Ming Yiu (The University of Hong Kong)  

## Summary

This paper bridges **sparse autoencoders (SAEs)** from mechanistic interpretability with **neural encoding models** to explain *why* intermediate layers of LLMs best predict human brain responses to language. By decomposing GPT-2 XL and Llama-3.1-8B into 16K–32K interpretable features per layer, the authors show that:

1. **Semantic features alone** recover 94% of peak brain encoding performance (r=0.285)
2. SAEs **recapitulate cortical semantic topography** — five a priori semantic subcategories map onto distinct brain regions
3. Results **generalize across English, Chinese, and French**

## Key Findings

### 1. Semantic Features Dominate Brain Alignment

- Human-validated taxonomy (Fleiss' κ ≥ 0.74) of SAE features across 6 categories
- **Semantic features alone**: r = 0.285 (94% of peak encoding performance)
- **Variance-matched baseline**: significantly lower (p < 0.001, Cohen's d = 1.31)
- SAE features predict human **reading times** beyond lexical controls (ΔlogLik = 38.4, p < 0.001)

### 2. Cortical Topography Prediction

Five semantic subcategories derived **a priori** from three independent neuroscience programs:

| Subcategory | Predicted Region | Neuroscience Source |
|------------|-----------------|-------------------|
| Social/Person | Dorsomedial PFC, TPJ, Precuneus | Theory of Mind network |
| Action/Event | Premotor, Posterior Parietal | Action observation network |
| Place/Spatial | Parahippocampal Place Area | Scene-selective cortex |
| Object/Entity | Lateral Occipital Complex | Object-selective cortex |
| Abstract/Emotion | Anterior Temporal Lobe, vmPFC | Semantic hub, emotion |

**Convergence test** (Spearman ρ = 0.72, p < 0.001; hypergeometric p = 0.007) confirms alignment at granularity inaccessible to prior methods.

### 3. Cross-Linguistic Generalization

Results replicate across **English, Chinese, and French**, suggesting language-universal semantic representations.

### 4. Semantic Prediction-Error Encoding

Exploratory analysis provides preliminary evidence that the brain additionally encodes **unexpected semantic content** — not just the predicted representation but deviations from it.

## Methodology

### Step 1: SAE Training

Train SAEs on LLM hidden states (GPT-2 XL, Llama-3.1-8B):
- **Dictionary size**: 16K–32K features per layer
- **Sparsity**: L1 + reconstruction loss
- **Layers**: Across all layers (not just final)

### Step 2: Feature Categorization

SAE features manually categorized into taxonomy:
1. **Semantic** (concrete concepts, abstract ideas, relations)
2. **Syntactic** (grammatical roles, POS tags)
3. **Positional** (token position, sequence position)
4. **Lexical** (word frequency, orthographic)
5. **Multi/Other** (multiple or uninterpretable)
6. **Function word** (articles, prepositions, etc.)

Human annotation with Fleiss' κ ≥ 0.74 inter-annotator agreement.

### Step 3: Brain Encoding Model

Use SAE feature activations as predictors for fMRI responses:
- **Ridge regression** encoding model
- Predict brain responses from SAE feature values
- Compare semantic-only model vs variance-matched baselines

### Step 4: Topography Mapping

For each brain voxel:
1. Find the SAE feature that best predicts it
2. Map feature subcategory to brain region
3. Test convergence with a priori neuroscience predictions

### Step 5: Behavioral Validation

Predict human **reading times** from SAE features:
- Beyond lexical frequency and length baselines
- ΔlogLik = 38.4 improvement over controls

## Practical Implications

- **For mechanistic interpretability**: SAEs provide a direct bridge to brain data
- **For cognitive neuroscience**: LLM features predict cortical organization at unprecedented granularity
- **For NLP**: Brain evidence for semantic primitives encoded in LLMs
- **For cross-linguistic research**: Universal semantic representations in LLMs

## Key Formulas

### SAE Architecture

```
f(x) = ReLU(W_enc · (x - b_dec) + b_enc)     # feature activation
x̂ = W_dec · f(x) + b_dec                       # reconstruction
L = ||x - x̂||² + λ · ||f(x)||₁                 # loss (reconstruction + sparsity)
```

### Encoding Model

```
brain_voxel(t) ≈ β · f_LLM(t) + ε              # ridge regression
```

## Implementation Notes

- Library: Use **SAELens** or **TransformerLens** for SAE training on LLMs
- fMRI data: Pereira et al. (2018) natural stories dataset or similar
- GPU requirements: 1–4 A100s for SAE training on 8B parameter models
- Cross-linguistic evaluation: Parallel stimuli in English, Chinese, French
- **Activation**: SAE brain alignment, sparse autoencoder encoding, LLM cortical topography, mechanistic interpretability brain, semantic encoding model, neural encoding SAE

## Pitfalls

- SAE feature interpretability is inherently noisy — human annotation essential
- Cross-subject alignment in fMRI adds noise; results are group-level
- Causal claims require follow-up experiments (activation patching)
- Semantic categories are coarse; finer-grained taxonomies may reveal more
- Single dataset (Pereira 2018); replication on diverse fMRI corpora needed
