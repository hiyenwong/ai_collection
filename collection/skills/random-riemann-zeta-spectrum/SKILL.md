---
name: random-riemann-zeta-spectrum
description: |
  Methodology for analyzing the integral means spectrum of the random Riemann zeta
  function and its connection to Gaussian multiplicative chaos (GMC). Applies to
  analytic number theory, probability theory, Liouville quantum gravity, and
  complex analysis. Triggers: Riemann zeta function, integral means spectrum,
  Gaussian multiplicative chaos, Kraetzer conjecture, random analytic function,
  analytic number theory, probability, Liouville quantum gravity, 黎曼zeta函数
---

# Random Riemann Zeta Function Analysis

## Core Framework

### Random Zeta Function

The randomized zeta function zeta_rand(sigma + ih) represents the asymptotic
statistical behavior of random vertical shifts of the actual zeta function
in the critical strip (1/2 < sigma <= 1, h in R).

### Integral Means Spectrum

For an analytic function f, the integral means spectrum measures:
```
beta(t) = sup{ beta : integral of |f'(re^(i*theta))|^t = O((1-r)^(-beta)) }
```

### Kraetzer Conjecture

The universal integral means spectrum for univalent functions in the disc
has a specific quadratic form, conjectured 30 years ago.

## Key Results from arXiv:2603.26507

1. **Main Result**: The complex integral means spectrum of the primitive of
   zeta_rand is almost surely of the Kraetzer form

2. **GMC Connection**: Same Kraetzer form holds for holomorphic multiplicative
   chaos on the unit disc (related to Liouville quantum gravity on unit circle)

3. **Non-injectivity**: Neither the primitive of zeta_rand nor holomorphic GMC
   are injective functions

4. **Alternative Derivation**: Uses convergence of zeta on critical line to
   holomorphic GMC distribution (Duplantier-Webb)

## When to Use

- Analyzing statistical properties of zeta function on critical line
- Computing integral means spectra for random analytic functions
- Connecting number theory to Liouville quantum gravity
- Studying Gaussian multiplicative chaos applications
- Analyzing conformal mapping properties
