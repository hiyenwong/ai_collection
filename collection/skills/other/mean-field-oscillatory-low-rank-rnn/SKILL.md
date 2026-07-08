---
name: mean-field-oscillatory-low-rank-rnn
description: "Mean-field theory for rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation. Analyzes how low-rank structure and adaptation interact to produce complex oscillatory and chaotic behavior in recurrent neural networks."
trigger_words: ["mean field oscillatory", "low rank recurrent", "activity dependent adaptation", "oscillatory dynamics RNN", "rich oscillatory", "RNN mean field theory"]
category: "neuroscience"
---

## Overview

This paper (arXiv:2606.30366) develops mean-field theory for recurrent neural networks with both low-rank structure and activity-dependent adaptation. Shows how these two mechanisms interact to produce rich dynamical regimes including oscillations, chaos, and multistability.

## Core Theory

### Model Structure
```
dx/dt = -x + W_lowrank * φ(x) + W_full * φ(x) - g_adapt * a * φ(x)
da/dt = (-a + φ(x)) / τ_adapt
```
- **W_lowrank**: Low-rank structured connectivity (rank r << N)
- **W_full**: Random full-rank connectivity (chaotic driver)
- **g_adapt**: Adaptation strength controlling oscillation onset
- **τ_adapt**: Adaptation timescale

### Mean-Field Reduction
1. Project dynamics onto low-rank subspace
2. Use dynamical mean-field theory for random component
3. Derive closed equations for order parameters
4. Analyze fixed points, limit cycles, and chaotic regimes

## Key Regimes

1. **Fixed point regime**: Low adaptation, dominated by low-rank structure
2. **Oscillatory regime**: Moderate adaptation creates limit cycles
3. **Chaotic regime**: Strong random connectivity drives chaos
4. **Mixed regime**: Adaptation + chaos produces complex metastable dynamics

## Implementation

### Mean-Field Equations
```
m_dot = f(m, q, a)    # Order parameter dynamics
q_dot = g(m, q, a)    # Variance dynamics  
a_dot = (-a + h(m)) / τ_adapt  # Adaptation dynamics
```

### Bifurcation Analysis
- Vary g_adapt and σ_W (random connectivity strength)
- Track fixed point stability via Jacobian eigenvalues
- Identify Hopf bifurcations leading to oscillations
- Map chaos onset via largest Lyapunov exponent

## Pitfalls

- **Low-rank assumption**: Results depend on r << N; for higher rank, mean-field breaks down
- **Timescale separation**: Analysis assumes τ_adapt >> 1; fast adaptation needs different treatment
- **Activation function**: Results derived for specific φ(x); different nonlinearities change dynamics

## Applications

- Working memory: Oscillatory regimes support persistent activity
- Decision making: Multistability enables choice between alternatives
- Motor control: Oscillations drive rhythmic motor patterns

## Verification

1. Simulate full RNN and compare with mean-field predictions
2. Verify bifurcation diagram matches numerical continuation
3. Test different activation functions (ReLU, tanh, sigmoid)
4. Validate low-rank assumption by varying rank r

## Activation

mean field theory, oscillatory dynamics, low rank RNN, activity dependent adaptation, bifurcation analysis, RNN dynamics, working memory, neural oscillations
