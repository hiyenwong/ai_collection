---
name: bayesian-model-selection-bb-plot
description: Bayesian model selection using Bayes factors and BB (Bayes factor-Bayes factor) plot diagnostics for validating model comparison and estimating background distributions. Based on arXiv:2605.10333.
---

# Bayesian Model Selection & BB Plot Diagnostics

## Overview

This skill provides methods for:
1. **Computing Bayes factors** to compare competing models/hypotheses
2. **BB plot diagnostics** to validate Bayes factor calculations
3. **Estimating background distributions** of Bayes factors at low computational cost

Based on: *"BB plot: A Tool for Accurate Model Selection Using Bayes factors"* (arXiv:2605.10333)

---

## 1. Bayes Factor Fundamentals

### Definition

The **Bayes factor** $B_{12}$ between hypothesis $H_1$ and $H_2$ given data $d$ is the ratio of marginal likelihoods (evidence):

$$B_{12} = \frac{p(d|H_1)}{p(d|H_2)} = \frac{\int p(d|\theta_1, H_1)\,p(\theta_1|H_1)\,d\theta_1}{\int p(d|\theta_2, H_2)\,p(\theta_2|H_2)\,d\theta_2}$$

### Interpretation (Jeffreys' Scale)

| $\log_{10} B_{12}$ | Evidence for $H_1$ |
|---|---|
| < 0 | Supports $H_2$ |
| 0 – 0.5 | Not worth mentioning |
| 0.5 – 1 | Substantial |
| 1 – 2 | Strong |
| > 2 | Decisive |

### Posterior Odds

With prior odds $\frac{P(H_1)}{P(H_2)}$:

$$\frac{P(H_1|d)}{P(H_2|d)} = B_{12} \times \frac{P(H_1)}{P(H_2)}$$

---

## 2. The BB Relationship

### Core Insight

The BB plot exploits a fundamental relationship between the distribution of the Bayes factor under each hypothesis. Let:

- $p(B|H_1)$ = distribution of Bayes factor values when $H_1$ is true
- $p(B|H_2)$ = distribution of Bayes factor values when $H_2$ is true

The **BB relationship** states:

$$p(B|H_1) = B \cdot p(B|H_2)$$

or equivalently, in cumulative form:

$$P(B > B^* | H_1) = \int_{B^*}^{\infty} B \cdot p(B|H_2)\,dB$$

This means the tail probability under $H_1$ is determined entirely by the distribution under $H_2$, weighted by $B$.

### BB Plot Construction

1. **Generate** Bayes factor samples under $H_2$ (via simulation or analytical form)
2. **Compute** the expected tail probability under $H_1$: $P(B > B^* | H_1) = \mathbb{E}_{H_2}[B \cdot \mathbb{I}(B > B^*)]$
3. **Plot** $P(B > B^* | H_1)$ vs $P(B > B^* | H_2)$ on log-log axes
4. The diagonal line $y = x \cdot \bar{B}$ (or linear in appropriate coordinates) serves as the consistency check

### Diagnostic Interpretation

- **Points on the expected line**: Bayes factor calculations are self-consistent
- **Systematic deviations**: Indicates errors in evidence computation (e.g., insufficient sampler convergence, wrong priors, numerical integration errors)
- **Scatter pattern**: Reveals whether the Bayes factor has good discriminating power

---

## 3. When to Use BB Plots

Use this approach when:

- **Validating Bayes factor pipelines**: Before trusting model selection results, confirm the computation is accurate
- **Estimating false-alarm rates**: Get the background distribution of Bayes factors under the null without expensive simulations
- **Comparing model selection methods**: Cross-validate different evidence estimators (harmonic mean, thermodynamic integration, nested sampling)
- **Gravitational wave astronomy**: Model selection between competing waveform models, testing GR vs. alternatives, signal vs. noise classification
- **Any domain with expensive likelihoods**: Where you need reliable model comparison but can't afford massive simulation campaigns

---

## 4. Implementation Guide

### 4.1 Bayes Factor Computation (SciPy-based)

```python
import numpy as np
from scipy import integrate, stats
from scipy.special import logsumexp

def compute_evidence_numerical(data, likelihood_fn, prior_fn, param_bounds, n_grid=1000):
    """
    Compute marginal likelihood (evidence) via numerical integration.
    Suitable for low-dimensional problems (1-3 parameters).
    
    Parameters:
        data: observed data
        likelihood_fn: callable, returns p(data | theta)
        prior_fn: callable, returns p(theta)
        param_bounds: list of (min, max) tuples for each parameter
        n_grid: grid resolution per dimension
    
    Returns:
        evidence: float, p(data | H)
    """
    ndim = len(param_bounds)
    grids = [np.linspace(lo, hi, n_grid) for lo, hi in param_bounds]
    mesh = np.meshgrid(*grids, indexing='ij')
    
    # Evaluate log-likelihood + log-prior on grid
    log_weights = np.zeros([n_grid] * ndim)
    it = np.nditer(np.zeros([n_grid] * ndim), flags=['multi_index'])
    for _ in it:
        idx = it.multi_index
        theta = [grids[d][idx[d]] for d in range(ndim)]
        log_lik = np.log(likelihood_fn(data, theta) + 1e-300)
        log_pri = np.log(prior_fn(theta) + 1e-300)
        log_weights[idx] = log_lik + log_pri
    
    # Log-sum-exp for numerical stability
    log_evidence = logsumexp(log_weights.flatten())
    # Add volume element correction
    volumes = [hi - lo for lo, hi in param_bounds]
    log_volume = sum(np.log(v) for v in volumes)
    log_evidence += log_volume - ndim * np.log(n_grid)
    
    return np.exp(log_evidence)


def compute_bayes_factor(data, likelihood_h1, likelihood_h2, 
                         prior_h1, prior_h2, bounds_h1, bounds_h2, **kwargs):
    """
    Compute Bayes factor B_12 = p(data|H1) / p(data|H2).
    
    Returns:
        B12: Bayes factor (values > 1 favor H1)
        log_B12: log Bayes factor for numerical stability
    """
    evidence_h1 = compute_evidence_numerical(data, likelihood_h1, prior_h1, bounds_h1, **kwargs)
    evidence_h2 = compute_evidence_numerical(data, likelihood_h2, prior_h2, bounds_h2, **kwargs)
    
    B12 = evidence_h1 / evidence_h2
    return B12, np.log(B12)
```

### 4.2 Monte Carlo Evidence via Importance Sampling

```python
def compute_evidence_importance(data, likelihood_fn, prior_fn, 
                                proposal_fn, n_samples=100000):
    """
    Compute evidence via importance sampling.
    More scalable than grid integration for moderate dimensions.
    """
    # Sample from proposal distribution
    samples = proposal_fn(n_samples)
    
    # Compute importance weights: p(data|theta) * p(theta) / q(theta)
    log_weights = np.zeros(n_samples)
    for i, theta in enumerate(samples):
        log_lik = np.log(likelihood_fn(data, theta) + 1e-300)
        log_pri = np.log(prior_fn(theta) + 1e-300)
        log_prop = np.log(proposal_fn.pdf(theta) + 1e-300)
        log_weights[i] = log_lik + log_pri - log_prop
    
    # Log-space evidence estimation
    log_evidence = logsumexp(log_weights) - np.log(n_samples)
    return np.exp(log_evidence), log_evidence
```

### 4.3 BB Plot Implementation

```python
import matplotlib.pyplot as plt

def generate_bf_samples_under_h2(null_likelihood_fn, null_prior_fn, 
                                  alt_likelihood_fn, alt_prior_fn,
                                  data_generator_h2, n_simulations=1000, **kwargs):
    """
    Generate Bayes factor samples when H2 (null) is true.
    
    Parameters:
        null_likelihood_fn: p(data | theta, H2)
        null_prior_fn: p(theta | H2)
        alt_likelihood_fn: p(data | theta, H1)
        alt_prior_fn: p(theta | H1)
        data_generator_h2: callable that generates synthetic data under H2
        n_simulations: number of simulated datasets
    
    Returns:
        bf_samples: array of Bayes factor values B_12 computed under H2
    """
    bf_samples = []
    for i in range(n_simulations):
        synthetic_data = data_generator_h2()
        B12, _ = compute_bayes_factor(
            synthetic_data, alt_likelihood_fn, null_likelihood_fn,
            alt_prior_fn, null_prior_fn, **kwargs
        )
        bf_samples.append(B12)
    return np.array(bf_samples)


def compute_bb_relationship(bf_samples_h2, thresholds=None):
    """
    Compute the BB relationship: P(B > B* | H1) vs P(B > B* | H2).
    
    The key identity: P(B > B* | H1) = E_{H2}[B * I(B > B*)]
    
    Parameters:
        bf_samples_h2: Bayes factor samples generated under H2
        thresholds: array of B* thresholds (default: percentiles of samples)
    
    Returns:
        p_h2: P(B > B* | H2) for each threshold
        p_h1: P(B > B* | H1) for each threshold (computed via BB relationship)
        thresholds: the B* values used
    """
    if thresholds is None:
        thresholds = np.percentile(bf_samples_h2, np.linspace(0, 99.9, 200))
    
    p_h2 = []
    p_h1 = []
    
    for B_star in thresholds:
        # P(B > B* | H2): empirical tail under H2
        mask = bf_samples_h2 > B_star
        p_h2.append(np.mean(mask))
        
        # P(B > B* | H1) via BB relationship: E[B * I(B > B*)] under H2
        if np.any(mask):
            p_h1.append(np.mean(bf_samples_h2[mask]))
        else:
            p_h1.append(0.0)
    
    return np.array(p_h2), np.array(p_h1), thresholds


def plot_bb_diagnostic(bf_samples_h2, ax=None, title="BB Plot"):
    """
    Create a BB plot diagnostic.
    
    The expected relationship is p_h1 = B_mean * p_h2 in linear space,
    which appears as a straight line on log-log axes with slope ~1.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    p_h2, p_h1, thresholds = compute_bb_relationship(bf_samples_h2)
    
    # Filter out zeros for log plot
    valid = (p_h2 > 0) & (p_h1 > 0)
    
    ax.loglog(p_h2[valid], p_h1[valid], 'bo-', markersize=3, alpha=0.7,
              label='BB relationship')
    
    # Reference line: y = x (slope 1 in log-log)
    x_ref = np.array([1e-6, 1])
    ax.loglog(x_ref, x_ref, 'r--', alpha=0.5, label='p(H1) = p(H2)')
    
    # Reference line: y = mean(B) * x
    mean_b = np.mean(bf_samples_h2)
    ax.loglog(x_ref, mean_b * x_ref, 'g--', alpha=0.5, 
              label=f'p(H1) = {mean_b:.1f} × p(H2)')
    
    ax.set_xlabel('P(B > B* | H2)', fontsize=12)
    ax.set_ylabel('P(B > B* | H1)', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    return ax
```

### 4.4 Complete Workflow Example: Signal vs Noise

```python
# --- Example: Gravitational Wave Signal Detection ---
# H1: data contains a GW signal + noise
# H2: data contains noise only

np.random.seed(42)

# Simple model: H1 = signal (Gaussian with mean=mu) + noise, H2 = noise only
def gw_signal_model(mu=1.0, sigma_signal=0.3):
    """Signal + noise model: N(mu, sigma_signal^2 + sigma_noise^2)"""
    return lambda data, theta: stats.norm.pdf(data, loc=theta[0], 
                                                scale=np.sqrt(sigma_signal**2 + 0.1**2))

def noise_model():
    """Noise-only model: N(0, sigma_noise^2)"""
    return lambda data, theta: stats.norm.pdf(data, loc=0, scale=0.1)

# Priors
def signal_prior(theta):
    return stats.uniform.pdf(theta[0], loc=-3, scale=6)

def noise_prior(theta):
    return 1.0  # Improper but cancels in ratio

# Bounds
signal_bounds = [(-3, 3)]
noise_bounds = [(0, 0)]  # No free parameters

# Likelihood for full dataset (product over data points)
def make_dataset_likelihood(model_fn):
    def likelihood(data, theta):
        probs = model_fn(theta)
        return np.prod(probs(data) + 1e-300)
    return likelihood

# Generate synthetic data under H2 (noise only)
def generate_noise_data(n_points=20):
    return np.random.normal(0, 0.1, n_points)

# Generate a single Bayes factor
bf, log_bf = compute_bayes_factor(
    generate_noise_data(),
    make_dataset_likelihood(gw_signal_model()),
    make_dataset_likelihood(noise_model()),
    signal_prior, noise_prior,
    signal_bounds, noise_bounds,
    n_grid=200
)
print(f"Bayes factor B_12 = {bf:.4f} (log10 = {np.log10(bf):.3f})")

# Generate BB plot samples
print("Generating Bayes factor samples under H2 (this may take a moment)...")
bf_samples = []
n_sim = 100  # Use more in production
for i in range(n_sim):
    data = generate_noise_data()
    try:
        B12, _ = compute_bayes_factor(
            data,
            make_dataset_likelihood(gw_signal_model()),
            make_dataset_likelihood(noise_model()),
            signal_prior, noise_prior,
            signal_bounds, noise_bounds,
            n_grid=100
        )
        bf_samples.append(B12)
    except Exception:
        continue

bf_samples = np.array(bf_samples)
print(f"Generated {len(bf_samples)} Bayes factor samples")
print(f"Mean B_12 under H2: {np.mean(bf_samples):.4f}")
print(f"Median B_12 under H2: {np.median(bf_samples):.4f}")

# BB Plot
fig, ax = plt.subplots(figsize=(8, 6))
plot_bb_diagnostic(bf_samples, ax=ax, 
                   title="BB Plot: Signal vs Noise Model Selection")
plt.tight_layout()
plt.savefig("bb_plot_diagnostic.png", dpi=150)
print("BB plot saved to bb_plot_diagnostic.png")
```

---

## 5. Validating Bayes Factor Calculations

### Self-Consistency Check via BB Plot

1. **Simulate** many datasets under the null hypothesis $H_2$
2. **Compute** Bayes factors $B_{12}$ for each dataset
3. **Plot** the BB relationship: $P(B > B^* | H_1)$ vs $P(B > B^* | H_2)$
4. **Verify**: the curve should follow $P(B > B^* | H_1) \approx \bar{B} \cdot P(B > B^* | H_2)$

**If the curve deviates systematically from the expected line, the Bayes factor calculation has errors.** Common causes:
- Insufficient MCMC/nested sampling convergence
- Incorrect prior normalization
- Numerical precision issues in evidence estimation
- Likelihood implementation bugs

### Cross-Validation Strategy

Compare multiple evidence estimators on the same problem:
- Grid integration (low-dimensional, ground truth)
- Harmonic mean estimator (warn: often unstable)
- Thermodynamic integration
- Nested sampling (e.g., `dynesty`, `MultiNest`)
- Bridge sampling

The BB plot will reveal which estimator produces self-consistent results.

---

## 6. Estimating Background Distributions

One of the most powerful applications of the BB relationship is **estimating the background distribution of Bayes factors under $H_1$ from samples under $H_2$** (or vice versa).

### Analytical Estimation

When $p(B|H_2)$ can be derived analytically (e.g., in simple models), the BB relationship gives:

$$p(B|H_1) = B \cdot p(B|H_2)$$

This means you can compute the **entire false-positive distribution** without simulating under $H_1$.

### Low-Cost Monte Carlo

1. **Cheap direction**: Simulate under whichever hypothesis is computationally cheaper to sample from
2. **Weighted tail**: Use the BB relationship to derive the tail probabilities under the other hypothesis
3. **P-value estimation**: Compute frequentist p-values from the Bayes factor ranking

```python
def estimate_background_pvalue(observed_bf, bf_samples_h2):
    """
    Estimate the p-value for an observed Bayes factor using
    the BB relationship and samples under H2.
    """
    # P-value under H2: fraction of null BFs exceeding observed
    pvalue_h2 = np.mean(bf_samples_h2 >= observed_bf)
    
    # Corresponding tail under H1 via BB relationship
    mask = bf_samples_h2 >= observed_bf
    if np.any(mask):
        tail_h1 = np.mean(bf_samples_h2[mask])
    else:
        tail_h1 = 0.0
    
    return {
        'p_value_H2': pvalue_h2,
        'tail_probability_H1': tail_h1,
        'observed_BF': observed_bf
    }
```

---

## 7. Connection to Gravitational Wave Astronomy

The original paper demonstrates BB plots in GW contexts:

### Use Cases in GW Astronomy

| Application | H1 (Signal) | H2 (Null/Alt) |
|---|---|---|
| **Detection** | GW signal + noise | Noise only |
| **Waveform model selection** | Full GR waveform | Approximate/modified waveform |
| **Tests of GR** | Post-Newtonian + deviation params | Standard GR |
| **Binary classification** | Binary black hole | Binary neutron star |

### Why BB Plots Matter for GW

- **Expensive likelihoods**: GW parameter estimation takes hours per event; BB plots reduce the number of simulations needed for background estimation
- **Calibration**: BB plots validate that different evidence estimation methods (e.g., `bilby`'s nested sampling) give consistent results
- **Pipeline verification**: Before applying model selection to real GW events (e.g., GW150914), BB plots confirm the Bayes factor pipeline is working correctly

### Typical GW Workflow

```python
# Pseudocode for GW model selection with BB validation

# 1. Define waveform models
h1_waveform = lalimulation_IMRPhenomD  # Full GR model
h2_waveform = lalimulation_IMRPhenomPv2  # Alternative model

# 2. Compute Bayes factor on real data
B12_real = compute_bayes_factor_gw(real_strain_data, h1_waveform, h2_waveform)

# 3. Validate with BB plot
# Generate noise-only injections (cheap: no signal)
bf_null_samples = []
for injection_noise in noise_injections:
    B12 = compute_bayes_factor_gw(injection_noise, h1_waveform, h2_waveform)
    bf_null_samples.append(B12)

# 4. Plot BB diagnostic to validate
plot_bb_diagnostic(bf_null_samples)

# 5. Use BB relationship to estimate false alarm rate
# P(B > B12_real | H2) = tail probability under null
# P(B > B12_real | H1) = via BB relationship = E[B * I(B > B12_real)]
```

---

## 8. Quick Reference Checklist

- [ ] Define competing hypotheses $H_1$ and $H_2$ clearly
- [ ] Specify priors for parameters under each hypothesis
- [ ] Compute Bayes factor using appropriate evidence estimator
- [ ] Validate with BB plot: simulate under simpler hypothesis, check self-consistency
- [ ] If BB plot deviates from expected line → investigate evidence computation
- [ ] Use BB relationship to estimate background/false-alarm rates
- [ ] Report $\log_{10} B_{12}$ with uncertainty estimates
- [ ] For GW applications: validate against injection campaigns

---

## Dependencies

```
numpy
scipy
matplotlib
# Optional for GW applications:
# bilby
# dynesty
# lalsuite
```
