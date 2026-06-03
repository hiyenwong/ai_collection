---
name: weibull-change-point-detection
description: "Copula-based Markov chain methodology for offline change-point estimation in financial time series with Weibull marginals. Handles nonlinear serial dependence in nonnegative financial data (volumes, durations, volatility). Use when analyzing regime changes in financial data, detecting structural breaks in trading volumes or volatility, modeling time series with copula-based dependence, or working with Weibull-distributed financial quantities."
metadata:
  arxiv_id: "2605.29541"
  published: "2026-05-29"
  tags: [statistics, finance, change-point, weibull, copula, markov, time-series]
---

# Weibull Change-Point Detection

## Core Methodology

Offline change-point estimation for time series with nonlinear serial dependence using copula-based Markov chain models with Weibull marginals. Suitable for nonnegative financial data: trading volumes, order durations, volatility measurements, inter-trade times.

### Mathematical Framework

**Weibull Marginals**: Financial quantities X ~ Weibull(k, λ) where k is shape parameter (controls tail behavior) and λ is scale parameter. More flexible than exponential for modeling heavy-tailed financial data.

**Copula-Based Markov**: Joint distribution F(x_t, x_{t-1}) = C(F(x_t), F(x_{t-1}); θ) where C is copula function capturing nonlinear dependence structure, F is Weibull CDF, θ is dependence parameter. Separates marginal distribution from dependence structure.

**Change-Point Detection**: Find τ where the copula parameter θ changes: θ_t = θ_1 for t ≤ τ, θ_t = θ_2 for t > τ. Use likelihood ratio test or Bayesian information criterion.

### Key Patterns

**Pattern 1: Volume Regime Detection**
- Model daily trading volumes with Weibull marginals
- Use Gaussian or Clayton copula for serial dependence
- Detect shifts in volume dynamics (e.g., before/after major events)

**Pattern 2: Volatility Break Detection**
- Model realized volatility with Weibull distribution
- Detect structural breaks in volatility clustering
- Useful for regime-switching model validation

**Pattern 3: Duration Analysis**
- Model inter-trade durations or order arrival times
- Detect changes in market microstructure
- Useful for HFT analysis and liquidity monitoring

### Implementation Steps

1. **Fit Weibull marginals** to data using MLE
2. **Select copula family** (Gaussian, Clayton, Gumbel) based on AIC/BIC
3. **Estimate copula parameter** θ via canonical maximum likelihood
4. **Apply change-point test**: maximize log-likelihood ratio over candidate breakpoints
5. **Validate** with bootstrap or permutation tests

### Error Handling

- **Small sample sizes**: Weibull MLE may be unstable; use Bayesian estimation with informative priors
- **Multiple change-points**: Apply binary segmentation or wild binary segmentation
- **Nonstationary marginals**: Use rolling window estimation for time-varying Weibull parameters

### Related Skills
- `deep-portfolio-optimization-framework` - portfolio optimization
- `quantum-off-policy-evaluation-pricing` - insurance pricing
- `quantum-finance` - quantum computing in finance
