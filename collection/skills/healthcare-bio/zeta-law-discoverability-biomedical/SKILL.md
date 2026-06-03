---
name: zeta-law-discoverability-biomedical
description: >
  Research skill for the paper "How Much Data is Enough? The Zeta Law of Discoverability
  in Biomedical Data" (arXiv:2604.17581) by Paul M. Thompson. Covers the Zeta Law framework
  derived from Riemann zeta function properties that characterizes how discovery probability
  scales with sample size in biomedical data. Applicable to sample size estimation, power
  analysis, discoverability modeling, brain connectomics, data collection planning, zeta
  function applications, and resource allocation in neuroimaging studies.
activation_triggers:
  - sample size
  - power analysis
  - discoverability
  - brain connectomics
  - data collection
  - zeta function
  - resource allocation
  - diminishing returns
  - neuroimaging
  - connectome
  - UK Biobank
  - ABCD Study
  - optimal stopping
  - power-law decay
---

# How Much Data is Enough? The Zeta Law of Discoverability in Biomedical Data

**Paper:** arXiv:2604.17581 (2026)
**Author:** Paul M. Thompson
**Categories:** cs.LG, cs.AI, q-bio.NC
**Published:** 2026-04-19

---

## Summary

This paper introduces the **Zeta Law of Discoverability**, a mathematical framework that predicts how the probability of discovering new scientific findings scales with sample size in biomedical data. Derived from Riemann zeta function properties and calibrated on large-scale brain connectomics datasets (UK Biobank, ABCD Study), the law establishes that discoverability follows a power-law decay with sample size, enabling derivation of optimal stopping criteria for data collection and practical resource allocation guidelines for neuroimaging studies.

---

## Core Methodology: Zeta Law Derivation

### Foundational Insight
The Zeta Law is derived from properties of the **Riemann zeta function** ζ(s), which connects number-theoretic structure to the statistical mechanics of discovery in high-dimensional biomedical data. The key idea is that the rate at which new findings (e.g., brain connectivity associations) emerge as a function of sample size follows regularities analogous to the convergence behavior of ζ(s).

### Derivation Steps
1. **Model each potential discovery as a latent variable** with an unknown effect size drawn from a prior distribution.
2. **Map the cumulative discovery probability** to the partial sums of ζ(s), where the index over real numbers corresponds to ranking potential discoveries by their detectability.
3. **Apply analytic continuation and residue calculus** to derive closed-form expressions for discovery probability as a function of sample size N.
4. **The resulting power-law decay** arises naturally from the pole structure of ζ(s) at s = 1, which governs the asymptotic rate of new discoveries.

### Calibration Datasets
- **UK Biobank:** ~40,000+ participants with structural and functional MRI connectomics data.
- **ABCD Study (Adolescent Brain Cognitive Development):** ~12,000+ participants with longitudinal neuroimaging.
- These datasets provide empirical validation of the theoretical power-law scaling across different populations and imaging modalities.

---

## Key Findings on Discoverability Scaling

### Power-Law Decay of Discoverability
- The marginal probability of discovering a **new** scientific finding at sample size N decays as a **power law** in N: P(new discovery | N) ∝ N^(-α), where α > 0 is determined by the underlying effect size distribution.
- The cumulative number of discoveries D(N) follows **D(N) ∝ N^(1-α)** for α < 1, exhibiting diminishing returns: each additional sample yields fewer new discoveries.
- The parameter α is empirically estimable from pilot data or existing datasets and reflects the "richness" of the discovery landscape.

### Empirical Observations
- In brain connectomics, the majority of discoverable associations are found within the first few thousand samples.
- Beyond ~10,000–20,000 samples, the discovery rate slows dramatically, suggesting diminishing returns for further data collection in standard connectomics analyses.
- The power-law exponent α varies by modality (structural vs. functional connectivity) and by the strictness of statistical thresholds.

### Diminishing Returns Threshold
- The paper identifies a **knee point** in the D(N) curve beyond which the cost per new discovery increases sharply.
- This knee point can be computed analytically from the estimated α and the cost structure of data collection.

---

## Mathematical Framework

### Discovery Probability Model

The core model expresses the expected number of discoveries at sample size N as:

```
D(N) = C · N^(1-α) + D₀
```

where:
- **C** is a scaling constant related to the total pool of discoverable effects
- **α** is the power-law exponent (0 < α < 1 in typical biomedical settings)
- **D₀** is the baseline number of trivially discoverable effects
- The marginal discovery rate is: dD/dN = C·(1-α)·N^(-α)

### Connection to Riemann Zeta Function

The cumulative discovery probability integrates over effect sizes indexed by their detectability rank k:

```
P(discovery by sample size N) = Σ_k [1 - exp(-λ_k · N)]
```

where λ_k ∝ k^(-s) follows a ζ-distribution. The sum is approximated by:

```
D(N) ≈ C_total · [1 - ζ(s)⁻¹ · ζ(s, N)]
```

linking discovery rate directly to the Hurwitz zeta function ζ(s, N) and its asymptotics.

### Optimal Stopping Criterion

Given a cost model where:
- **c(N)** = cost of collecting N total samples
- **v(D)** = value of D discoveries

The optimal sample size N* satisfies:

```
dD/dN |_{N*} = c'(N*) / v'(D(N*))
```

For linear cost c(N) = c₀·N and linear value v(D) = v₀·D, this reduces to:

```
N* = [C·(1-α)·v₀ / c₀]^(1/α)
```

This provides a **closed-form optimal stopping rule** parameterized by the empirically estimated α.

### Confidence Intervals on Discovery Count

The framework also provides uncertainty quantification: the variance in the number of discoveries scales with N, enabling construction of confidence bands around the D(N) curve for study planning.

---

## Practical Guidelines for Neuroimaging Resource Allocation

### 1. Estimating the Power-Law Exponent α
- Use a **pilot dataset** (N ≥ 500) to estimate the discovery curve D(N) via subsampling.
- Fit the power-law model D(N) = C·N^(1-α) + D₀ using maximum likelihood or Bayesian methods.
- Report α alongside traditional power analyses as a complement.

### 2. Determining Adequate Sample Size
- For structural connectomics: α ≈ 0.5–0.7, suggesting N ≈ 5,000–15,000 captures most discoverable effects.
- For functional connectomics: α ≈ 0.6–0.8, with diminishing returns setting in at N ≈ 3,000–10,000.
- These ranges depend on the number of connections tested and multiple comparison correction stringency.

### 3. Resource Allocation Across Studies
- When funding multiple studies, allocate samples to maximize total discoveries: prioritize smaller studies up to their knee points before increasing any single study beyond its optimal N*.
- Use the Zeta Law to compare the marginal value of adding samples to an existing dataset vs. starting a new collection.

### 4. Multi-Site Study Planning
- The framework accounts for site heterogeneity: increased variance from multi-site data effectively increases α, shifting the optimal N* upward.
- Budget for 10–30% more samples than single-site estimates to account for inter-site variability.

### 5. When to Stop Collecting Data
- Monitor the empirical discovery curve in real time as data accumulates.
- Stop when the observed marginal discovery rate falls below the cost-adjusted threshold derived from the optimal stopping criterion.
- This is especially relevant for consortium studies where data collection is ongoing and iterative decisions are needed.

### 6. Generalization Beyond Connectomics
- While calibrated on brain connectomics, the Zeta Law framework is theoretically applicable to any biomedical domain where:
  - Discoveries correspond to detecting effects in high-dimensional data
  - Effect sizes follow a heavy-tailed prior distribution
  - Statistical power increases monotonically with sample size
- Potential applications: genomics (GWAS hit discovery), proteomics, clinical trial enrichment.

---

## Key Equations Reference

| Quantity | Formula | Description |
|----------|---------|-------------|
| Cumulative discoveries | D(N) = C·N^(1-α) + D₀ | Total findings at sample size N |
| Marginal discovery rate | dD/dN = C·(1-α)·N^(-α) | Rate of new findings per sample |
| Optimal sample size | N* = [C·(1-α)·v₀/c₀]^(1/α) | Cost-optimal stopping point |
| Zeta-weighted discovery sum | Σ_k [1 - exp(-λ_k·N)] | Full model over effect rank k |
| Power-law exponent α | Estimated from pilot data | Controls diminishing returns rate |

---

## Limitations and Considerations

1. **Effect size distribution assumption:** The framework assumes effect sizes follow a distribution consistent with ζ-function indexing. Deviations (e.g., sharply bimodal distributions) may affect accuracy.
2. **Dependence on statistical threshold:** The estimated α depends on the multiple comparison correction method used; more stringent corrections effectively steepen the discovery curve.
3. **Population homogeneity:** Results are calibrated on specific cohorts (UK Biobank, ABCD); generalization to clinical or differently structured populations requires recalibration.
4. **Non-stationary effects:** Longitudinal changes in measurement technology or phenotype definitions can shift the discovery landscape over time.

---

## Related Concepts

- **Statistical power analysis** — traditional approach to sample size determination for single hypotheses
- **Multiple comparisons and false discovery rate** — govern the threshold for "discovery" in the Zeta Law framework
- **Scaling laws in AI** — analogous power-law scaling observed in deep learning (Kaplan et al., 2020)
- **Brain connectomics** — the primary application domain; structural and functional connectivity networks
- **Riemann zeta function and number theory** — mathematical foundation of the framework
- **Resource allocation in clinical trials** — practical application area for optimal stopping
- **UK Biobank neuroimaging** — one of the largest brain imaging datasets, key calibration resource

---

## Citation

```bibtex
@article{thompson2026zeta,
  title={How Much Data is Enough? The Zeta Law of Discoverability in Biomedical Data},
  author={Thompson, Paul M.},
  journal={arXiv preprint arXiv:2604.17581},
  year={2026},
  categories={cs.LG, cs.AI, q-bio.NC}
}
```
