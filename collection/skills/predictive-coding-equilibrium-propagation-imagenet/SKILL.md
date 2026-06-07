---
name: predictive-coding-equilibrium-propagation-imagenet
description: Training Predictive Coding Networks on ImageNet using Equilibrium Propagation. Biologically plausible training framework for PCNs achieving near-backpropagation performance. Use when: (1) Training predictive coding networks at scale, (2) Implementing biologically plausible learning rules, (3) Scaling equilibrium propagation beyond small tasks, (4) Energy-based model training without backpropagation. Keywords: predictive coding network, PCN, equilibrium propagation, EP, energy-based model, ImageNet, biological learning, centered EP, equilibration scheme.
license: MIT
---

# Predictive Coding Network Training with Equilibrium Propagation at ImageNet Scale

## Overview

Predictive Coding Networks (PCNs) are energy-based models from computational neuroscience traditionally trained with specialized algorithms. Equilibrium Propagation (EP) is a physics-based training framework. This skill documents the first successful combination of both at ImageNet scale, achieving 13.23% top-5 error rate (close to backpropagation's 12.2%).

## Core Innovation

**Centered Equilibrium Propagation for PCNs**: Novel training method combining centered EP variant with specialized equilibration scheme for predictive coding networks.

**Key Results**:
- 10-layer convolutional PCN (VGG10) trained on full ImageNet
- 13.23% top-5 test error rate vs backpropagation baseline 12.2%
- First demonstration of both PCNs and EP at ImageNet scale

## Methodology

### Predictive Coding Network Architecture

PCNs are hierarchical energy-based models where:
- Each layer predicts the activity of the next layer
- Errors propagate backward through predictions
- Network minimizes a global energy function

**VGG10 PCN Structure**:
```
Input → Conv layers (10 total) → Output
       ↑ Predictions ↓ Errors
```

### Centered Equilibrium Propagation

Standard EP has bias issues. Centered EP removes systematic bias:

**Training phases**:
1. **Free phase**: Network relaxes to equilibrium given input
2. **Clamped phase**: Output nudged toward target, network re-equilibrates
3. **Gradient computation**: Difference between states

**Centering modification**:
- Subtract systematic bias from gradient estimate
- Use running averages to center the updates
- Enables unbiased gradient estimation

### Novel Equilibration Scheme

PCNs require different equilibration dynamics than Hopfield networks:

**Iterative relaxation**:
```
for iteration in equilibration_steps:
    for layer in reversed(layers):
        update_predictions()
        compute_errors()
        minimize_local_energy()
```

**Key parameters**:
- Equilibration steps: ~100-500 iterations
- Step size: Adaptive based on energy gradient
- Convergence criterion: Energy change threshold

### Training Procedure

**Step 1**: Initialize network with input image
```
x_input = image
Initialize all layers to predicted values
```

**Step 2**: Free phase equilibration
```
Relax network to equilibrium without output constraint
Monitor energy convergence
```

**Step 3**: Weakly clamped phase
```
nudge_output(epsilon)  # epsilon ~ 0.01-0.1
Re-equilibrate network
```

**Step 4**: Gradient computation (centered)
```
gradient = (clamped_state - free_state - centering_term) / epsilon
centering_term = running_average_state_difference
```

**Step 5**: Weight update
```
weights += learning_rate * gradient
Update running averages for centering
```

## Implementation Details

### Energy Function

Total energy for PCN:
```
E(x) = Σ_l ||e_l||² + Σ_l ||r_l - f(r_{l+1})||²
```

Where:
- `e_l`: Error at layer l
- `r_l`: Representation at layer l
- `f`: Prediction function (typically linear + activation)

### Computational Considerations

**Memory efficiency**:
- Store free and clamped states separately
- Use gradient checkpointing for deep networks
- Batch processing reduces memory overhead

**Speed optimization**:
- Parallelize layer updates where possible
- Use momentum in equilibration dynamics
- Early stopping when energy converges

### Hyperparameters

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| Equilibration steps | 100-500 | More for harder tasks |
| Nudge amplitude (ε) | 0.01-0.1 | Larger for faster convergence |
| Learning rate | 0.001-0.01 | Similar to backprop |
| Centering decay | 0.99 | Running average smoothing |
| Batch size | 32-128 | Standard ImageNet settings |

## Comparison to Backpropagation

**Advantages**:
- Biologically plausible (no weight transport)
- Local learning rules possible
- Natural uncertainty quantification

**Disadvantages**:
- Slower training (requires equilibration)
- More memory (store two states)
- Slightly lower final accuracy

**Performance gap**: ~1% absolute (13.23% vs 12.2%)

## Extensions

### Three-Factor Learning Rules

EP naturally implements three-factor Hebbian learning:
```
Δw_ij = η * (x_i^clamped - x_i^free) * (x_j^clamped - x_j^free) * neuromodulator
```

Where neuromodulator = output error signal.

### Hardware Implementation

**Neuromorphic systems**:
- Inference: Direct equilibrium dynamics
- Training: On-chip equilibration possible
- Energy: Potentially lower than backprop

**FPGA acceleration**:
- Parallel equilibration iterations
- Custom energy minimization circuits

## Pitfalls

1. **Insufficient equilibration**: Network not reaching true equilibrium leads to biased gradients
2. **Wrong nudge amplitude**: Too large distorts dynamics, too small requires more iterations
3. **Centering not applied**: Systematic bias accumulates without centering term
4. **Memory overflow**: Storing two full states doubles memory requirements

## Verification

Test equilibration convergence:
```python
def check_equilibrium(network, input_data, tolerance=1e-5):
    energy_prev = network.compute_energy()
    for _ in range(10):
        network.relax_one_step()
        energy_curr = network.compute_energy()
        if abs(energy_curr - energy_prev) < tolerance:
            return True  # Converged
        energy_prev = energy_curr
    return False  # Not converged
```

## Activation

**Trigger keywords**: predictive coding, equilibrium propagation, EP training, energy-based learning, biological backprop, centered EP, PCN training, ImageNet PCN

## References

See `references/architecture_details.md` for VGG10 PCN specification.
See `references/mathematical_derivation.md` for centered EP theory.

## Source

arXiv:2606.03584 - "Training a Predictive Coding Network on ImageNet using Equilibrium Propagation" (June 2026)
Authors: Tugdual Kerjan, Rasmus Høier, Benjamin Scellier