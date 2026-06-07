---
name: bayesian-haptic-perception-dynamics
description: "Bayesian dynamical framework for modeling time-order effects in sequential haptic perception. Captures perceptual biases from prior expectations and temporal structure using drift-diffusion dynamics. Activation: haptic perception, Bayesian dynamics, time-order effects, sequential stimuli, perceptual bias."
---

# Bayesian Dynamical Framework for Haptic Perception

> Modeling time-order asymmetries and sequential biases in haptic discrimination using Bayesian drift-diffusion dynamics.

## Metadata
- **Source**: arXiv:2604.19662v1
- **Authors**: Gastón Avetta, Jose Lobera, Juan José Zárate, et al.
- **Published**: 2026-04-21
- **Category**: q-bio.NC (Neurons and Cognition)

## Core Methodology

### The Time-Order Effect Problem
Perceptual judgments of sequential stimuli show systematic biases:
- **Primacy Effect**: First stimulus dominates judgment
- **Recency Effect**: Last stimulus dominates judgment  
- **Contrast Effects**: Perceived differences depend on presentation order

This methodology models these effects using Bayesian drift-diffusion dynamics.

### Bayesian Dynamical Framework

1. **Prior Expectations**
   - Encode prior beliefs about stimulus statistics
   - Model as Gaussian or mixture distributions
   - Update dynamically based on sequential observations

2. **Sequential Evidence Accumulation**
   - Use drift-diffusion model (DDM) for each stimulus
   - Allow drift rate to depend on prior and previous stimulus
   - Incorporate time-varying decision boundaries

3. **Temporal Structure Modeling**
   - Inter-stimulus interval (ISI) affects integration
   - Memory decay between stimuli
   - Attentional modulation over time

4. **Decision Dynamics**
   - Bayesian posterior computation
   - Comparison operation with order-dependent weights
   - Response generation with motor execution noise

### Key Innovations

- **Dynamical Prior**: Prior beliefs evolve based on stimulus sequence
- **Order-Dependent Weights**: Different weights for first vs second stimulus
- **Temporal Integration Window**: Optimal time window for evidence accumulation

## Implementation Guide

### Prerequisites
- Bayesian inference libraries (PyMC, Stan)
- Drift-diffusion model toolboxes (HDDM, PyDDM)
- Signal processing tools
- Statistical analysis packages

### Step-by-Step

1. **Define Prior Distribution**
   - Set prior mean (e.g., 5.0 for neutral reference)
   - Set prior standard deviation (uncertainty)

2. **Model Evidence Accumulation**
   - Compute drift rate for first stimulus
   - Update posterior after first stimulus
   - Compute drift rate for second stimulus

3. **Compute Time-Order Asymmetry**
   - Compare forward vs backward sequences
   - Measure decision differences

4. **Fit to Behavioral Data**
   - Use Bayesian parameter estimation
   - MCMC sampling of model parameters

### Code Example

```python
import numpy as np
from scipy.stats import norm

class BayesianHapticPerception:
    """
    Bayesian dynamical model of sequential haptic perception.
    """
    
    def __init__(self, prior_mean=5.0, prior_std=2.0, 
                 drift_rate=0.1, diffusion_noise=1.0,
                 time_step=0.01, max_time=5.0):
        self.prior_mean = prior_mean
        self.prior_std = prior_std
        self.drift_rate = drift_rate
        self.diffusion_noise = diffusion_noise
        self.dt = time_step
        self.max_time = max_time
        
    def compute_posterior(self, stimulus, prior_mean, prior_std,
                         likelihood_std=1.0):
        """
        Compute posterior after observing a stimulus.
        
        Uses Bayesian updating with Gaussian conjugate prior.
        """
        # Bayesian update for Gaussian conjugate prior
        prior_precision = 1.0 / (prior_std ** 2)
        likelihood_precision = 1.0 / (likelihood_std ** 2)
        
        posterior_precision = prior_precision + likelihood_precision
        posterior_mean = (prior_precision * prior_mean + 
                         likelihood_precision * stimulus) / posterior_precision
        posterior_std = np.sqrt(1.0 / posterior_precision)
        
        return posterior_mean, posterior_std
    
    def drift_diffusion_trial(self, drift, boundary=1.0):
        """
        Simulate a single drift-diffusion process.
        
        Returns:
        --------
        decision_time : float
            Time to reach boundary
        choice : int
            1 for upper boundary, -1 for lower
        evidence_trace : array
            Accumulated evidence over time
        """
        evidence = 0.0
        evidence_trace = [evidence]
        time = 0.0
        
        while abs(evidence) < boundary and time < self.max_time:
            # Drift + diffusion step
            evidence += drift * self.dt + np.random.normal(0, 
                          np.sqrt(self.dt) * self.diffusion_noise)
            evidence_trace.append(evidence)
            time += self.dt
        
        choice = 1 if evidence >= boundary else -1
        return time, choice, np.array(evidence_trace)
    
    def sequential_discrimination(self, stimulus_1, stimulus_2, isi=1.0):
        """
        Model sequential haptic discrimination task.
        
        Parameters:
        -----------
        stimulus_1, stimulus_2 : float
            Intensities of two stimuli
        isi : float
            Inter-stimulus interval (seconds)
        
        Returns:
        --------
        decision : int
            1 if judged stimulus_2 > stimulus_1, -1 otherwise
        response_time : float
            Total decision time
        """
        # Step 1: Process first stimulus
        drift_1 = self.drift_rate * (stimulus_1 - self.prior_mean)
        dt_1, _, _ = self.drift_diffusion_trial(drift_1)
        
        # Update prior based on first stimulus
        post_mean, post_std = self.compute_posterior(
            stimulus_1, self.prior_mean, self.prior_std
        )
        
        # Memory decay during ISI
        decay_factor = np.exp(-isi / 2.0)  # Exponential decay
        effective_prior_mean = post_mean * decay_factor + \
                               self.prior_mean * (1 - decay_factor)
        effective_prior_std = np.sqrt(
            (post_std * decay_factor)**2 + 
            (self.prior_std * (1 - decay_factor))**2
        )
        
        # Step 2: Process second stimulus
        drift_2 = self.drift_rate * (stimulus_2 - effective_prior_mean)
        dt_2, decision, _ = self.drift_diffusion_trial(drift_2)
        
        total_time = dt_1 + isi + dt_2
        
        return decision, total_time
    
    def time_order_asymmetry(self, s_weak, s_strong, n_trials=1000):
        """
        Compute time-order asymmetry for a stimulus pair.
        
        Compares forward (weak->strong) vs backward (strong->weak) sequences.
        """
        # Forward order: weak then strong
        forward_choices = []
        for _ in range(n_trials):
            decision, _ = self.sequential_discrimination(s_weak, s_strong)
            forward_choices.append(decision)
        
        # Backward order: strong then weak
        backward_choices = []
        for _ in range(n_trials):
            decision, _ = self.sequential_discrimination(s_strong, s_weak)
            # Flip decision to match comparison direction
            backward_choices.append(-decision)
        
        # Asymmetry: difference in "strong > weak" judgments
        forward_rate = np.mean(np.array(forward_choices) == 1)
        backward_rate = np.mean(np.array(backward_choices) == 1)
        asymmetry = forward_rate - backward_rate
        
        return asymmetry, forward_rate, backward_rate

# Example usage
model = BayesianHapticPerception()
asymmetry, fw_rate, bw_rate = model.time_order_asymmetry(
    s_weak=3.0, s_strong=7.0, n_trials=500
)
print(f"Time-order asymmetry: {asymmetry:.3f}")
print(f"Forward (weak->strong): {fw_rate:.3f}")
print(f"Backward (strong->weak): {bw_rate:.3f}")
```

## Applications

### Cognitive Neuroscience
- **Somatosensory Processing**: Model S1/S2 cortex dynamics
- **Sequential Perception**: Study temporal order judgment tasks
- **Working Memory**: Understand short-term retention of tactile info

### Psychophysics
- **Haptic Illusions**: Explain and predict perceptual illusions
- **Cross-Modal Effects**: Extend to visual-auditory sequences
- **Clinical Assessment**: Detect perceptual deficits in patients

### Robotics and Haptics
- **Tactile Sensing**: Improve robot texture discrimination
- **Prosthetics**: Better encoding of tactile feedback
- **VR/AR**: Realistic haptic rendering

### Decision Making Research
- **Sequential Choice**: Model multi-alternative decisions
- **Context Effects**: Study how prior options affect current choice
- **Consumer Behavior**: Product comparison heuristics

## Pitfalls

### Model Limitations
- Assumes Gaussian distributions (may not match all stimuli)
- Linear drift rate may be oversimplified
- Single accumulator may miss parallel processing
- No explicit neural implementation

### Parameter Challenges
- Many free parameters require extensive fitting
- Parameter trade-offs (drift vs boundary vs non-decision time)
- Individual differences require subject-specific fits
- Limited generalization across stimulus types

### Validation Issues
- Difficult to measure internal evidence accumulation
- Response time data alone may not constrain model
- Alternative models may fit equally well
- Neural correlates of Bayesian updates unclear

## Related Skills
- drift-diffusion-model
- sequential-decision-making
- perceptual-decision-making
- bayesian-brain
- evidence-accumulation

## References
- Avetta, G., et al. (2026). "Modelling time-order effects in haptic perception with a Bayesian dynamical framework." arXiv:2604.19662v1
