---
name: prior-elicitation-connectivity
description: >
  Bayesian prior elicitation methodology for single-subject functional connectivity
  network inference from resting-state fMRI. Introduces novel Bayesian priors on
  correlation matrices with a dedicated elicitation framework that translates
  expert beliefs about expected correlation levels and variability into interpretable
  hyperparameters. Provides distributional (not point) estimates of connectivity
  weights with uncertainty quantification and credible sets. Use when performing
  Bayesian functional connectivity analysis, single-subject rs-fMRI inference,
  prior elicitation for correlation matrices, uncertainty-aware brain network
  estimation, or distributional connectivity weights. Triggers: Bayesian FC,
  prior elicitation, single-subject connectivity, correlation matrix prior,
  distributional connectivity weights, credible sets brain network.
  arXiv: 2605.02587 (Jiang et al., 2026).
---

# Bayesian Prior Elicitation for Single-Subject FC Networks

Provides distributional connectivity weights via posterior distributions, enabling
uncertainty quantification, robust point estimates, and significance testing based
on credible sets — applicable to single-subject rs-fMRI data.

## Problem Statement

Most existing FC methods estimate constant weights. This approach provides:
- Distributional weights defined by posterior distributions
- Regularized estimates through expert-informed priors
- Uncertainty evaluation for each connection
- Post-inference analyses including significance testing

## Core Framework

### Bayesian Model

```
Y ~ N(0, Σ)          # Gaussian likelihood on fMRI time series
Σ ~ Prior(θ)          # Prior on covariance/correlation matrix
P(Σ|Y) ∝ P(Y|Σ)·P(Σ) # Posterior distribution
```

### Novel Priors on Correlation Matrices

The key innovation: priors that translate expert beliefs into interpretable hyperparameters:
- **Expected correlation level**: Mean correlation strength between brain regions
- **Correlation variability**: Expected heterogeneity in connection strengths
- These map to concrete hyperparameters in the prior distribution

### Prior Elicitation Procedure

1. **Specify expected mean correlation**: e.g., "most connections are weak (ρ ≈ 0.2)"
2. **Specify expected variability**: e.g., "some connections are much stronger"
3. **Map to hyperparameters**: Use the elicitation framework to translate beliefs
   into prior distribution parameters
4. **Validate prior**: Check that the prior generates correlation matrices consistent
   with domain knowledge

### Posterior Inference

```python
# Conceptual workflow
import numpy as np
from scipy.stats import wishart

def bayesian_fc_posterior(fMRI_data, prior_params, n_samples=10000):
    """
    Estimate posterior distribution of FC matrix.
    
    Args:
        fMRI_data: T x N matrix (timepoints x regions)
        prior_params: hyperparameters from elicitation
        n_samples: number of posterior samples
    """
    T, N = fMRI_data.shape
    S = fMRI_data.T @ fMRI_data / T  # Sample covariance
    
    # With conjugate prior (e.g., inverse-Wishart),
    # posterior is analytically tractable
    posterior_df = prior_params['df'] + T
    posterior_scale = prior_params['scale'] + T * S
    
    # Sample from posterior
    samples = wishart.rvs(posterior_df, posterior_scale, size=n_samples)
    
    # Convert to correlation matrices
    corr_samples = []
    for s in samples:
        d = np.sqrt(np.diag(s))
        corr = s / np.outer(d, d)
        corr_samples.append(corr)
    
    return np.array(corr_samples)
```

### Significance Testing via Credible Sets

```python
def significant_connections(posterior_samples, alpha=0.05):
    """Identify significant connections using posterior credible intervals."""
    n_regions = posterior_samples.shape[1]
    significant = np.zeros((n_regions, n_regions), dtype=bool)
    
    for i in range(n_regions):
        for j in range(i+1, n_regions):
            vals = posterior_samples[:, i, j]
            ci_lower = np.percentile(vals, alpha/2 * 100)
            ci_upper = np.percentile(vals, (1 - alpha/2) * 100)
            # Significant if credible interval excludes zero
            significant[i, j] = significant[j, i] = (ci_lower > 0 or ci_upper < 0)
    
    return significant
```

## Advantages Over Existing Methods

| Aspect | Standard FC | Bayesian FC (this work) |
|--------|------------|------------------------|
| Estimate type | Point estimate | Full posterior distribution |
| Uncertainty | None | Quantified per connection |
| Prior knowledge | Not used | Expert-informed priors |
| Significance | Arbitrary threshold | Credible interval based |
| Single-subject | Limited methods | Specifically designed for |

## Key Contributions

1. **Novel Bayesian priors** on correlation matrices with interpretable hyperparameters
2. **Prior elicitation framework** translating expert beliefs into statistical parameters
3. **Computational advantages** when combined with Gaussian likelihood
4. **Distributional weights** enabling uncertainty quantification
5. **Significance procedure** based on posterior credible sets
6. **Rare applicability to single-subject** rs-fMRI (only 2nd known Bayesian FC model)

## Activation Keywords

- Bayesian functional connectivity, prior elicitation correlation, single-subject FC,
  distributional connectivity weights, credible sets brain network, Bayesian rs-fMRI,
  correlation matrix prior, uncertainty-aware connectivity, expert-informed priors,
  posterior FC estimation
