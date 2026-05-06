---
name: online-generalised-predictive-coding
version: v1.0.0
last_updated: 2026-05-05
description: "Online Dynamic Expectation Maximisation (ODEM) — biologically-inspired online inference, learning, and uncertainty estimation for dynamic environments. Extends generalised filtering with temporal scale separation for triple estimation (states, parameters, precisions). Based on arXiv:2605.02675 (Bazargani et al., 2026)."
category: ai_collection
---

# Online Generalised Predictive Coding (ODEM)

## Description
ODEM extends generalised filtering for online data assimilation through a separation of temporal scales. It enables joint inference of latent states, learning of unknown model parameters, and estimation of uncertainty (state and observation noise) in an integrated framework — known as "triple estimation." Framed from a neuro-mimetic predictive coding perspective, ODEM offers a biologically inspired solution to online inference in dynamic environments.

**Paper:** Bazargani, M.H.Z., Urbas, S., Razi, A. et al. "Online Generalised Predictive Coding." arXiv:2605.02675 (2026). Categories: stat.ML, cs.LG, q-bio.NC

## Activation Keywords
- online dem
- odem
- generalised predictive coding
- generalised filtering
- dynamic expectation maximisation
- triple estimation
- variational kalman-bucy
- online inference dynamic
- 在线广义预测编码
- 动态期望最大化
- predictive coding online

## Core Methodology

### Key Innovation
**Temporal scale separation:** Slow updating of parameters and precisions contextualizes fast Bayesian belief updating about dynamic hidden states.

### Triple Estimation Framework
ODEM simultaneously estimates three quantities:
1. **Latent states** (fast timescale) — Bayesian belief updating about hidden states
2. **Model parameters** (slow timescale) — Learning unknown system parameters
3. **Precisions/noise** (slow timescale) — Estimating state and observation noise

### Workflow

#### Step 1: Define Generative Model
- Specify the nonlinear dynamical system: dx/dt = f(x, θ) + noise
- Specify observation model: y = g(x, φ) + noise
- θ, φ are unknown parameters to be learned

#### Step 2: Variational Formulation
- Set up variational free energy (negative log model evidence)
- Use generalised coordinates of motion (states + derivatives)
- Define recognition density q over states, parameters, precisions

#### Step 3: Temporal Scale Separation
- **Fast loop:** Update beliefs about hidden states at observation frequency
- **Slow loop:** Update parameters and precisions at lower frequency
- This prevents parameter drift during rapid state fluctuations

#### Step 4: Online Variational Updates
- Process data sequentially (no batch processing needed)
- At each observation:
  1. Prediction step: propagate state beliefs through dynamics
  2. Update step: correct beliefs based on prediction error
  3. Slow update: adjust parameters and precisions

#### Step 5: Precision Estimation
- Estimate state noise precision (process noise)
- Estimate observation noise precision (measurement noise)
- These adapt online based on prediction error statistics

#### Step 6: Validation
- Test on nonlinear/chaotic generative models
- Verify latent state tracking even when model form differs from true dynamics
- Compare with offline DEM and standard Kalman filtering

## Implementation Notes

### Variational Free Energy
```python
# Pseudocode for ODEM variational update
def odem_update(state_belief, params, precisions, observation, dt):
    """One step of Online DEM."""
    # Fast: update state beliefs
    prediction = forward_model(state_belief, params)
    prediction_error = observation - observation_model(prediction)
    
    # Kalman-like gain based on precisions
    gain = compute_gain(precisions, prediction, state_belief)
    state_belief = prediction + gain @ prediction_error
    
    # Slow: update parameters (lower learning rate)
    param_gradient = compute_param_gradient(state_belief, params, prediction_error)
    params += slow_learning_rate * param_gradient
    
    # Slow: update precisions
    precision_gradient = compute_precision_gradient(prediction_error, precisions)
    precisions += precision_learning_rate * precision_gradient
    
    return state_belief, params, precisions
```

### Neuro-Mimetic Interpretation
- **Prediction errors** → cortical prediction error signals
- **State updates** → cortical prediction neurons
- **Parameter updates** → synaptic plasticity (slow)
- **Precision updates** → neuromodulatory gain control

### Advantages Over Existing Methods
1. **Online:** No need for full data batch; processes data sequentially
2. **Triple estimation:** States, parameters, and noise estimated together
3. **Biologically plausible:** Maps to predictive coding in cortex
4. **Robust to model mismatch:** Works even when generative model differs from true dynamics
5. **Handles chaos:** Validated on chaotic systems

### Applications
- Real-time neural data analysis (EEG, fMRI, calcium imaging)
- Online system identification for dynamical systems
- Adaptive control with uncertainty quantification
- Neuroimaging analysis with Dynamic Causal Modeling (DCM)
- Brain-computer interfaces requiring online adaptation

## Resources
- **Paper:** https://arxiv.org/abs/2605.02675
- **PDF:** https://arxiv.org/pdf/2605.02675
- **Related:** Dynamic Causal Modeling (DCM), predictive coding, variational inference

## Related Skills
- neurobridge-koopman-brain-dynamics (Koopman dynamics for brain states)
- brain-dit-fmri-foundation-model (fMRI foundation models)
- neural-dynamics-universal-translator (neural dynamics alignment)
- autoregressive-flow-matching-neural-dynamics (neural dynamics prediction)
