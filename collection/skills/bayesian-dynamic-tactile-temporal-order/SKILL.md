---
name: bayesian-dynamic-tactile-temporal-order
description: "Bayesian dynamic framework for modeling temporal order effects in tactile perception. Dynamic Bayesian modeling of perceptual discrimination tasks with temporal bias, prior-weighted sequential processing. Activation: tactile perception, temporal order effect, Bayesian inference, perceptual discrimination, dynamic model, somatosensory, temporal bias, sequential processing."
---

# Bayesian Dynamic Framework for Temporal Order Effects in Tactile Perception

> Dynamic Bayesian model explaining temporal order effects in tactile discrimination tasks — showing how perceptual priors and sequential processing biases shape somatosensory perception over time.

## Metadata
- **Source**: arXiv:2604.19662
- **Authors**: Gastón Avetta, Jose Lobera, Juan José Zárate, Inés Samengo, Damián G. Hernández
- **Published**: 2026-04-21
- **Categories**: q-bio.NC, physics.bio-ph, stat.AP

## Core Methodology

### Key Innovation
A dynamic Bayesian framework that models how the temporal order of tactile stimuli affects perceptual discrimination. Unlike static Bayesian models, this framework incorporates temporal dynamics — the brain's prior evolves across trials, creating sequential biases that explain well-known psychophysical phenomena like contraction bias and order-dependent performance asymmetries.

### Technical Framework

1. **Temporal Order Effect (TOE)**: When two tactile stimuli are presented sequentially, their perceived magnitudes are biased by presentation order — the first stimulus is perceived differently than the second even when physically identical
2. **Dynamic Bayesian Model**: 
   - Prior distribution p(s) encodes expectations about stimulus magnitude
   - Likelihood p(x|s) encodes sensory noise in tactile encoding
   - Posterior evolves dynamically across trials with trial-to-trial updating
3. **Contraction Bias**: Both stimuli are biased toward the prior mean, but asymmetrically based on temporal position
4. **Sequential Processing**: The estimated first stimulus influences the prior for the second stimulus, creating a coupling between temporal order and perceptual accuracy

### Mathematical Foundation
- Bayes' theorem with temporal evolution: p(s_t|x_t) ∝ p(x_t|s_t) · p(s_t|s_{t-1})
- Contraction toward prior mean: ŝ = μ_prior + w·(x - μ_prior), where w depends on sensory noise
- Temporal coupling: prior for stimulus 2 = f(posterior of stimulus 1)
- Psychometric function with order-dependent parameters

## Implementation Guide

### Prerequisites
- Bayesian inference and probability theory
- Psychophysics experimental methods
- Understanding of somatosensory processing
- Statistical modeling (PyMC, Stan, or custom MCMC)

### Step-by-Step
1. Collect tactile discrimination data (two-alternative forced choice)
2. Fit individual psychometric functions for each temporal order condition
3. Estimate sensory noise σ_s from discrimination performance
4. Build dynamic Bayesian model with evolving prior
5. Compare model predictions to observed TOE patterns
6. Validate with cross-trial sequential analysis

### Code Example
```python
import numpy as np
from scipy.stats import norm

class TactileTOE_Bayesian:
    """Dynamic Bayesian model for temporal order effects in tactile perception."""
    
    def __init__(self, prior_mean=5.0, prior_std=2.0, sensory_noise=1.0):
        self.prior_mean = prior_mean
        self.prior_std = prior_std
        self.sensory_noise = sensory_noise
        self.trial_history = []
    
    def estimate_stimulus(self, sensory_reading, position='first'):
        """Bayesian estimate with position-dependent prior."""
        if position == 'first':
            prior_m, prior_s = self.prior_mean, self.prior_std
        else:
            # Second stimulus: prior influenced by first estimate
            prior_m, prior_s = self._updated_prior()
        
        # Posterior = precision-weighted average
        w = prior_s**2 / (prior_s**2 + self.sensory_noise**2)
        estimate = w * sensory_reading + (1 - w) * prior_m
        posterior_std = np.sqrt(1 / (1/prior_s**2 + 1/self.sensory_noise**2))
        
        return estimate, posterior_std
    
    def _updated_prior(self):
        """Prior for second stimulus evolves from first posterior."""
        if self.trial_history:
            last_est, last_unc = self.trial_history[-1]
            return last_est, last_unc * 1.5  # partial retention with decay
        return self.prior_mean, self.prior_std
    
    def discriminate(self, s1_reading, s2_reading):
        """Predict discrimination response."""
        est1, _ = self.estimate_stimulus(s1_reading, 'first')
        self.trial_history.append((est1, self.sensory_noise))
        est2, _ = self.estimate_stimulus(s2_reading, 'second')
        return 's2_larger' if est2 > est1 else 's1_larger'
```

## Applications
- Understanding temporal biases in somatosensory perception
- Designing haptic interfaces that account for perceptual temporal order effects
- Modeling sequential decision-making under sensory uncertainty
- Clinical assessment of tactile processing disorders

## Pitfalls
- Individual differences in prior strength require participant-specific fitting
- The model assumes stationary priors within a session; longer sessions may show drift
- Multi-finger or multi-site stimulation introduces spatial coupling not captured here
- The temporal dynamics of prior updating are still debated in the literature

## Related Skills
- computational-neuroscience-models
- brain-to-speech-prosody-feature-engineering
- eccentricity-confound-eeg-visual-attention-decoding
