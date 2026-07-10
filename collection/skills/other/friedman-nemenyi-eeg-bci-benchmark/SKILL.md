---
name: friedman-nemenyi-eeg-bci-benchmark
description: Statistical benchmarking methodology for EEG motor-imagery BCI decoders using Friedman-Nemenyi tests. Proves no single decoding pipeline dominates across subjects — personalized model selection adds ~7% accuracy over best fixed choice. Use when evaluating BCI decoders, comparing multi-classifier performance, or designing subject-aware BCI systems.
activation: EEG BCI benchmark, motor imagery decoder comparison, Friedman-Nemenyi, per-subject optimality, BCI personalization, MOABB, CSP, covariance tangent-space
tags: [neuroscience, BCI, EEG, benchmarking, statistical-testing, motor-imagery, personalization]
version: 1.0.0
author: agent
arxiv_id: "2606.24394"
---

# Friedman-Nemenyi EEG Motor-Imagery BCI Benchmark

## Core Contribution

Rigorous statistical framework proving that **average rankings mask per-subject optimality** in EEG motor-imagery BCI decoding. The "best" pipeline on average is optimal for only 35% of participants — personalized model selection adds ~7 accuracy points.

## Key Findings

### Experimental Scale
- **1,056 decoding configurations** (feature extractor × scaler × classifier)
- **>340,000 subject-level model fits**
- **3 public datasets**: PhysionetMI (109 participants), Cho2017 (52), Zhou2016 (4)
- **2 frequency bands**: 8-15 Hz, 8-30 Hz
- Every model fit and tested within single session of single participant (easiest regime)

### Statistical Analysis
- **Friedman omnibus tests** for overall significance
- **Nemenyi critical-difference analysis** for pairwise comparisons
- **Wilcoxon signed-rank tests** with effect sizes
- Results on PhysionetMI (largest cohort): cov-tgsp and CSP families are strongest but **statistically indistinguishable** (Nemenyi p=0.27; Kendall's W=0.11)

### Central Result: Personalization Problem
- Single best pipeline optimal for only **35% of PhysionetMI participants**
- Nonlinear descriptors best for roughly **1/3 of participants**
- **Matching pipeline to participant adds ~7 accuracy points** over best fixed choice
- Ranking not artifact of dimensionality
- Classifier and scaler choices **secondary to feature representation**

## Methodology

### Multi-Classifier Comparison Statistics
```
1. Friedman test (non-parametric repeated measures ANOVA)
   → Tests if any classifier significantly differs from others
   
2. Nemenyi post-hoc test (critical difference diagram)
   → Pairwise comparisons with family-wise error correction
   → If p > 0.05: pipelines are statistically equivalent
   
3. Wilcoxon signed-rank + effect sizes
   → Individual pairwise comparisons with magnitude
```

### Feature Extractor Families
- **Covariance tangent-space projection (cov-tgsp)**: Riemannian geometry approach
- **Common Spatial Patterns (CSP)**: Classic spatial filtering
- **Nonlinear descriptors**: Capture complex feature interactions
- Ordering is **dataset-dependent** — no universal winner

### Framework
- **MOABB** (Mother of All BCI Benchmarks) for reproducible evaluation
- Within-subject, within-session cross-validation

## Practical Implications

1. **No universal BCI decoder exists** — even in easiest regime
2. **Personalized model selection is essential** — 7% accuracy gain is clinically significant
3. **Feature representation > classifier choice** — invest in feature engineering
4. **Average rankings are misleading** — always report per-subject distributions
5. **Nonlinear methods deserve attention** — optimal for ~33% of users

## Pitfalls

1. **Don't claim one pipeline is "best"** — statistically indistinguishable on large cohorts
2. **Don't ignore per-subject variance** — average accuracy hides individual differences
3. **Don't compare only on one dataset** — ordering is dataset-dependent
4. **Don't skip effect sizes** — statistical significance ≠ practical significance
5. **Don't ignore nonlinear methods** — they're optimal for 1/3 of users

## Related Skills

- `cross-subject-eeg-decoding` — complementary cross-subject generalization approaches
- `eeg-preprocessing-reliability` — preprocessing impacts on decoding reliability
- `ferroelectric-snn-eeg` — neuromorphic EEG BCI personalization
- `eeg-mftnet-multi-scale-temporal` — specific decoder architecture
- `bci-sift-feature-selection` — systematic feature tuning

## Source

Vasques, X., Barbaste, P., & Oullier, O. (2026). Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders. arXiv:2606.24394.
