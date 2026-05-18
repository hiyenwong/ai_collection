---
name: astrocyte-neural-field-model
description: "Coupled astrocyte-neural field model for studying glial metabolic support in working memory stabilization. Integrates astrocyte resource diffusion with spatial neural field equations."
arxiv_source: "2604.10036"
version: v1.0.0
last_updated: 2026-04-20
---

# Astrocyte-Neural Field Coupled Model

Coupled astrocyte-neural field model for studying how glial metabolic support stabilizes persistent activity states in working memory. Integrates astrocyte resource diffusion dynamics with spatial neural field equations.

## Core Innovation

This methodology bridges the gap between neural circuit models and metabolic support systems by:
- **Coupled dynamics**: Neural field equations + astrocyte resource diffusion
- **Metabolic stabilization**: Astrocyte networks provide sustained neurotransmitter support
- **Spatial extended models**: Goes beyond point neuron models to spatial neural fields
- **Working memory mechanisms**: Persistent activity stabilized by glial support

## Technical Approach

### Neural Field Equations

The neural field component models spatially extended neural activity:

```
τ ∂u(x,t)/∂t = -u(x,t) + ∫ w(x,y)·f(u(y,t)) dy + I(x,t)
```

Where:
- `u(x,t)`: Neural activity at position x and time t
- `w(x,y)`: Spatial connectivity kernel
- `f(·)`: Firing rate function
- `I(x,t)`: External input

### Astrocyte Resource Diffusion

The astrocyte component models metabolic resource dynamics:

```
τ_a ∂a(x,t)/∂t = D_a·∇²a(x,t) - γ·a(x,t) + β·f(u(x,t))
```

Where:
- `a(x,t)`: Astrocyte resource concentration
- `D_a`: Diffusion coefficient
- `γ`: Resource consumption rate
- `β`: Resource production rate (activity-dependent)

### Coupling Mechanism

The two systems are coupled through:
- **Neural → Astrocyte**: Neural activity drives astrocyte resource production
- **Astrocyte → Neural**: Resource availability modulates neural gain and stability

## Implementation Guidelines

### Model Configuration

```python
class AstrocyteNeuralFieldModel:
    def __init__(self, spatial_dim=128, dt=0.1, tau_neural=10.0, tau_astro=50.0,
                 diffusion_coef=0.1, coupling_strength=0.5):
        self.spatial_dim = spatial_dim
        self.dt = dt
        self.tau_neural = tau_neural
        self.tau_astro = tau_astro
        self.diffusion_coef = diffusion_coef
        self.coupling_strength = coupling_strength
```

### Key Parameters

| Parameter | Range | Description |
|-----------|-------|-------------|
| `tau_neural` | 5-20 ms | Neural time constant |
| `tau_astro` | 20-100 ms | Astrocyte time constant |
| `diffusion_coef` | 0.01-1.0 | Resource diffusion rate |
| `coupling_strength` | 0.1-1.0 | Neural-astrocyte coupling |
| `spatial_dim` | 64-512 | Spatial grid resolution |

### Simulation Workflow

1. **Initialize** neural field and astrocyte resource distributions
2. **Apply stimulus** to create localized activity bump
3. **Evolve coupled dynamics** using numerical integration
4. **Analyze stability** of persistent activity states
5. **Perturb system** to test robustness of memory states

## Applications

- Working memory maintenance mechanisms
- Metabolic constraints on neural computation
- Spatial pattern formation in neural tissue
- Neurodegenerative disease modeling
- Brain-computer interface stability analysis

## Activation Keywords

- astrocyte neural field model
- astrocyte
- neural field
- working memory stabilization
- glial support
- metabolic resource diffusion
- persistent activity
- coupled neural-glia dynamics
