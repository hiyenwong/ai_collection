---
name: doob-barrier-noise-consolidation
description: "Doob barrier-conditioned diffusion methodology for continual learning on analog neuromorphic hardware. Turns intrinsic device noise into consolidation resource using h-transform. Activation: continual learning, noise consolidation, Doob h-transform, barrier diffusion, neuromorphic hardware, BrainScaleS, analog noise"
tags: [continual-learning, noise-consolidation, doob-h-transform, neuromorphic, brainscales]
---

## Core Methodology

### Doob h-Transform for Synaptic Consolidation
- Cast per-synapse consolidation as **Doob h-transform**
- Condition weight dynamics on never crossing memory-critical barrier
- Conditioned diffusion gains extra drift: `σ² d/dw log h`
- Restoring force amplified by noise variance itself
- Diverges at barrier, preventing catastrophic forgetting

### Key Innovation
**Turning noise into resource**: Intrinsic analog device noise (normally accuracy tax) becomes consolidation dividend that digital accelerators must spend energy to generate.

### Mathematical Formulation
```
Weight dynamics: dw = -s(w-μ)dt + σdW + σ²∇log(h)dt

Where:
- -s(w-μ): anchored drift (from OUA, MESU, EWC)
- σdW: intrinsic noise term
- σ²∇log(h): Doob barrier-conditioning drift (NOVEL)
- h: harmonic function encoding barrier constraint
```

### Falsifiable Prediction
Increasing intrinsic noise **non-monotonically** improves sequential-task retention:
- **Inverted-U curve**: retention peaks at interior noise optimum
- Anchored-drift methods (OU/EWC/MESU) produce monotonic curves
- Pre-registered go/no-go gate: passes on Split-MNIST

## Implementation on BrainScaleS-2

### Hardware Characteristics
- Analog neuromorphic silicon
- Intrinsic noise: additive, trial-to-trial independent
- Tunable via on-chip averaging
- Real hardware-in-the-loop training

### Experimental Results
**Split-MNIST (8 seeds)**:
- Barrier-conditioning lifts retention **10.9 points** at interior optimum
- Paired Wilcoxon p=0.004 (statistically significant)
- Matched OU/EWC/MESU anchors are monotone (no inverted-U)

**BrainScaleS-2 silicon (single seed)**:
- Retains prior task **15.6 points better** than matched control
- Matched average accuracy (stability-plasticity shift, not net-accuracy win)
- Energy modeled (not measured directly)

### Ablation Studies
- Removing conditioning removes effect
- Optimum tracks barrier position
- Inverted-U survives second task stream
- Robust to noise realization in forward pass

## Applications

### Continual Learning on Neuromorphic Hardware
- Sequential task learning without catastrophic forgetting
- Energy-efficient memory consolidation
- Stability-plasticity balance via noise tuning
- Hardware-native continual learning

### Analog Neural Networks
- Leveraging device noise as computational resource
- Barrier-based weight protection
- Noise-aware training algorithms
- In-memory consolidation

### Brain-Inspired Learning
- Synaptic consolidation mechanisms
- Noise-dependent memory formation
- Biologically plausible continual learning
- Energy-efficient adaptation

## Implementation Guide

### Step 1: Define Barrier Function
```python
import numpy as np

def harmonic_function(w, consolidated_value, barrier_width):
    """
    Harmonic function h(w) encoding barrier constraint
    h -> 0 as w approaches barrier
    """
    distance = np.abs(w - consolidated_value)
    # h diverges at barrier, preventing crossing
    h = np.exp(-distance**2 / (2 * barrier_width**2))
    return h
```

### Step 2: Compute Doob Drift
```python
def doob_drift(w, consolidated_value, barrier_width, noise_variance):
    """
    Doob barrier-conditioning drift: σ² d/dw log h
    """
    h = harmonic_function(w, consolidated_value, barrier_width)
    # Gradient of log h
    grad_log_h = -(w - consolidated_value) / (barrier_width**2)
    # Doob drift term
    drift = noise_variance * grad_log_h
    return drift
```

### Step 3: Synaptic Update Rule
```python
def synaptic_update(w, consolidated_value, barrier_width, noise_variance, 
                   learning_rate, gradient):
    """
    Complete synaptic update with Doob barrier-conditioning
    """
    # Anchored drift (from EWC/OUA/MESU)
    anchored_drift = -learning_rate * (w - consolidated_value)
    
    # Doob barrier drift
    doob_term = doob_drift(w, consolidated_value, barrier_width, noise_variance)
    
    # Intrinsic noise
    noise = np.sqrt(noise_variance) * np.random.randn()
    
    # Gradient descent on task loss
    task_gradient = -learning_rate * gradient
    
    # Total update
    dw = anchored_drift + doob_term + noise + task_gradient
    w_new = w + dw
    
    return w_new
```

### Step 4: Tune Noise Level
```python
def find_optimal_noise(task_sequence, noise_range=np.logspace(-2, 1, 20)):
    """
    Find noise level that maximizes retention (inverted-U)
    """
    retention_scores = []
    
    for noise_var in noise_range:
        retention = train_and_evaluate(task_sequence, noise_var)
        retention_scores.append(retention)
    
    # Find peak of inverted-U
    optimal_idx = np.argmax(retention_scores)
    optimal_noise = noise_range[optimal_idx]
    
    return optimal_noise, retention_scores
```

### Step 5: Deploy on BrainScaleS-2
```python
# Configure hardware noise parameters
hw_config = {
    'noise_variance': optimal_noise,
    'barrier_width': task_dependent_width,
    'consolidation_enabled': True
}

# Run hardware-in-the-loop training
for task in task_sequence:
    train_on_hardware(task, hw_config)
    consolidate_weights(hw_config)
```

## Pitfalls

### Barrier Width Selection
**Problem**: Too narrow → weights stuck; too wide → no protection
**Solution**: Scale barrier_width with task similarity; use validation set to tune

### Noise Calibration
**Problem**: Hardware noise differs from simulation
**Solution**: Measure intrinsic noise on real silicon; calibrate simulation to match

### Anchored Drift Interference
**Problem**: Anchored drift (-s(w-μ)) can dominate Doob drift
**Solution**: Balance learning rates; use ablation to verify Doob contribution

### Stability-Plasticity Trade-off
**Problem**: High retention may reduce plasticity for new tasks
**Solution**: Monitor both retention and new-task accuracy; tune barrier dynamically

## Verification

### Inverted-U Test
- Vary noise across log-spaced values
- Plot retention vs noise
- Confirm non-monotonic (inverted-U) curve
- Statistical test: paired Wilcoxon at optimum vs monotone baselines

### Ablation Studies
- Remove Doob conditioning → effect should disappear
- Vary barrier position → optimum should track
- Test on multiple task streams → inverted-U should persist

### Hardware Validation
- Measure intrinsic noise on BrainScaleS-2
- Run rule with hardware noise in training loop
- Compare retention to matched control
- Verify stability-plasticity shift

## References

- Paper: arXiv:2607.06924
- Author: Gunner Levi Howe
- Hardware: BrainScaleS-2 neuromorphic silicon
- Date: July 8, 2026
- Pages: 14 pages, 9 figures
- Code: Available (proof-of-concept training run included)
