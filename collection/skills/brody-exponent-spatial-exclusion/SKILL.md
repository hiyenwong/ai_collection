---
name: brody-exponent-spatial-exclusion
description: "Calibrated measurement framework using the Brody exponent β as a quantitative measure of short-range exclusion in 2D spatial point processes. Originally from quantum chaos level-spacing statistics, now calibrated for spatial analysis with corrected CSR baseline, empirical β-r_excl calibration (Spearman ρ=0.988), and control protocols. Use for quantum chaos analysis, spatial statistics, prime number embeddings, and manufactured surface characterization."
metadata:
  arxiv_id: "2606.16393"
  published: "2026-06-15"
  authors: "Dawid Kucharski"
  tags: [quantum-chaos, spatial-statistics, brody-distribution, point-processes, prime-numbers]
---

# Brody Exponent Spatial Exclusion Framework

## Description

A calibrated measurement framework that repurposes the Brody distribution — originally from quantum chaos level-spacing statistics — as a quantitative measure of short-range exclusion in 2D spatial point processes. Includes corrected CSR baseline, empirical calibration against hard-core radius, and validated control protocols.

## Activation Keywords
- brody exponent, brody distribution
- spatial point process, level-spacing statistics
- quantum chaos spatial, short-range exclusion
- csr baseline correction, hard-core radius
- prime number embedding, wigner distribution
- 量子混沌, 空间点过程, 布罗迪指数

## Core Framework

### The Brody Distribution

Originally a phenomenological interpolation between Poisson (β=0) and Wigner (β=1) level-spacing statistics in quantum chaotic systems:

P(s) = C·β·s^(β-1) · exp(-C·s^β)

where C = [Γ(1+1/β)]^β normalizes the distribution.

### Key Results

1. **2D CSR Baseline Correction**: The 2D complete-spatial-randomness baseline is β = 0.96 ± 0.15, not the 1D Poisson reference (β=0). Using the 1D baseline in 2D analysis produces systematic bias.

2. **Empirical β-r_excl Calibration**: The Brody exponent β correlates with effective hard-core radius r_excl with Spearman ρ = 0.988, establishing β as a reliable proxy for exclusion strength.

3. **Density Independence**: Density-thinning experiments establish that β captures exclusion *strength* rather than point density, though absolute values are density-dependent.

### Measurement Protocol

```
1. Extract 2D point coordinates from data
2. Compute nearest-neighbor distances
3. Fit Brody distribution to distance histogram
4. Extract β parameter
5. Compare against calibrated CSR baseline (β ≈ 0.96 for 2D)
6. Interpret: β > 0.96 → exclusion present; β ≈ 0.96 → random; β < 0.96 → clustering
```

### Control Protocols

- **Sparse-integer control**: Distinguish genuine arithmetic signals from random patterns
- **Density-thinning**: Verify β measures exclusion strength not density
- **Binary-field baseline**: Low fill fraction requires distinct CSR baseline
- **Embedding null test**: Cantor-embedding shows some exclusion is embedding-created

### Decision Table

| β Range (2D) | Interpretation |
|---------------|----------------|
| β < 0.80 | Clustering behavior |
| 0.80 ≤ β < 0.96 | Near-random with slight clustering |
| 0.96 ± 0.15 | Complete Spatial Randomness (baseline) |
| 1.10 < β < 1.50 | Moderate exclusion |
| β > 1.50 | Strong exclusion |

## Usage Patterns

### Pattern 1: Quantum Chaos Analysis
Apply Brody distribution fitting to energy level spacings in quantum systems to characterize chaos-to-regularity transitions.

### Pattern 2: Spatial Statistics
Measure short-range exclusion in manufactured surfaces, biological point patterns, or geological distributions.

### Pattern 3: Number Theory
Analyze arithmetic sequences (e.g., prime number embeddings) for spatial exclusion patterns.

## Error Handling

### Baseline Selection
Always use the correct dimensionality-appropriate CSR baseline. Using 1D Poisson (β=0) for 2D data produces β values that are systematically inflated by ~0.96.

### Density Dependence
While β captures relative exclusion strength, absolute values depend on point density. Use density-thinning experiments to verify that observed β differences reflect genuine exclusion rather than sampling artifacts.

## References
- arXiv: 2606.16393 — "Calibrating the Brody exponent as a quantitative measure of short-range exclusion in 2D spatial point processes"
