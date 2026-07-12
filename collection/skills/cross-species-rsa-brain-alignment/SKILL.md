---
name: cross-species-rsa-brain-alignment
description: "Cross-Species RSA methodology for comparing brain-DNN alignment across human fMRI and macaque electrophysiology. Tests five learning rules (BP, FA, PC, STDP, untrained) across species showing conserved early visual alignment but divergent higher-area rankings. Use when: comparing species in brain encoding models, evaluating learning rule biological plausibility, cross-species validation of brain-DNN alignment, RSA with electrophysiology data. Triggered by: cross-species RSA, brain-DNN alignment macaque, learning rules comparison, V1 cross-species, macaque electrophysiology alignment, IT cross-species divergence, representational similarity analysis species."
category: ai_collection
tags: [brain-DNN-alignment, cross-species, RSA, macaque-electrophysiology, visual-cortex, learning-rules, representational-similarity-analysis]
---

# Cross-Species RSA: Conserved Early Visual Alignment but Divergent Higher-Area Rankings

**arXiv:** [2605.22401](https://arxiv.org/abs/2605.22401) (Submitted May 21, 2026)
**Author:** Nils Leutenegger
**Categories:** cs.LG, cs.NE, q-bio.NC

## Core Question

Does the relationship between learning rules and brain alignment generalize across species?

This paper extends the finding that **untrained CNNs match backpropagation at human V1** (arXiv:2604.16875) by testing the **same five learning rules** against **macaque electrophysiology** data.

## Methods

### Learning Rules Tested
1. **Backpropagation (BP)** — standard supervised learning
2. **Feedback Alignment (FA)** — random feedback weights
3. **Predictive Coding (PC)** — local error propagation
4. **STDP** — spike-timing-dependent plasticity
5. **Untrained random-weights baseline**

### Macaque Datasets
- **MajajHong2015**: V4/IT, 3,200 stimulus presentations, 88/168 neurons
- **FreemanZiemba2013**: V1/V2, 135 stimuli, 102/103 neurons

### Analysis
- **RSA (Representational Similarity Analysis)** with identical model weights from the prior human fMRI study
- Multi-seed variability (5 seeds)
- Noise ceilings and stimulus-control analysis

## Key Findings

### 1. Higher Absolute Alignment in Macaque
All models achieve **higher alignment** with macaque early visual cortex (ρ = 0.15–0.30 at V1/V2) than with human fMRI (ρ = 0.01–0.08), consistent with the higher signal-to-noise ratio of **electrophysiology** over fMRI BOLD.

### 2. STDP and PC Lead at V1/V2 (Cross-Species Conserved)
STDP produces the highest macaque V1/V2 alignment (ρ ~ 0.30), followed by PC (ρ ~ 0.28), consistent with their leading position among trained rules in human V1 — early visual alignment is **robust across species**.

### 3. IT Rankings Show No Cross-Species Correlation
At IT, learning rule rankings show **no detectable correlation** across species (Kendall's τ = 0.00, p = 1.00). However, this null result is limited by n = 5 (only detects τ = ±1.0) and is confounded by **stimulus set differences** between human and macaque experiments.

### 4. Model Capacity Dominates at IT
A **pretrained ResNet-50 (ImageNet)** achieves ρ = 0.25 at macaque IT, substantially above all custom CNN conditions (ρ = 0.07–0.14), suggesting IT alignment is **limited by model capacity and training data** rather than by the learning rule.

## Implications

### For Computational Neuroscience
- Early visual cortex (V1/V2) alignment with ANNs is **conserved across primate species** — validates human fMRI findings
- Higher visual areas (IT) show **species-dependent rankings**, driven by stimulus domain and model capacity rather than learning rule
- **Electrophysiology provides 2–4x higher signal-to-noise** for RSA compared to fMRI

### For Brain-Model Alignment Research
- Cross-species validation is essential — human fMRI findings may not transfer to electrophysiological benchmarks
- IT alignment requires **larger models and richer training data**, not better learning rules
- Multi-species benchmarks needed for robust evaluation of neural coding hypotheses

### Methodological Guidance
- Report **noise ceilings** and **multi-seed variability** in all RSA studies
- Control for **stimulus differences** when comparing across species
- Use **identical model weights** when comparing across datasets (this study does)

## Related Skills
- untrained-cnns-match-backpropagation-v1-rsa (predecessor human fMRI study)
- naturality-violation-score (category-theoretic brain-DNN alignment)
- brain-dnn-transformation-alignment

## Activation Keywords
- cross-species RSA
- brain-DNN alignment macaque
- learning rules comparison
- V1 cross-species conserved
- macaque electrophysiology alignment
- IT cross-species divergence
- representational similarity analysis species
- STDP macaque V1
- model capacity IT alignment
- pretrained ResNet vs learning rules
