---
name: low-rank-rnn-learning-dynamics
description: "Framework for analyzing learning dynamics in low-rank RNNs via overlap space decomposition. Distinguishes loss-visible overlaps (determine activity/output/loss) from loss-invisible overlaps (encode training history). Enables understanding of why functionally equivalent networks learn differently. Activation: low-rank RNN learning, RNN overlap space, loss-visible invisible, RNN gradient descent dynamics, RNN learning theory, Ger Barak RNN."
---

# Low-Rank RNN Learning Dynamics

> Extends the low-rank RNN framework from activity analysis to learning dynamics by deriving gradient-descent ODEs in reduced overlap space, revealing invisible structure that encodes training history.

## Metadata
- **Source**: arXiv:2605.04115
- **Authors**: Yoav Ger, Omri Barak
- **Published**: 2026-05-05
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation

Low-rank RNNs have been well-studied for their **activity dynamics** — how connectivity maps to function. However, the **learning process** (how synaptic changes reshape representations) remained theoretically opaque. This work derives a closed-form, low-dimensional system of ODEs that governs gradient-descent learning directly in the **overlap space**, providing analytical tractability for understanding RNN learning.

### Overlap Space Decomposition

The central theoretical contribution is the decomposition of overlaps into two classes:

#### Loss-Visible Overlaps
- Fully determine network activity, output, and loss
- Define the functional mapping of the network
- What traditional low-rank analysis focuses on

#### Loss-Invisible Overlaps
- Do NOT affect current network function
- Are REQUIRED to describe the learning process
- Act as **memory variables** encoding training history
- Explain why **functionally equivalent networks learn differently**

### Mathematical Framework

1. **Low-Rank Connectivity**: Express RNN weights as `W = m n^T` where `m, n` are low-rank factors
2. **Overlap Definition**: `q = n^T x` where `x` is the network state (overlap between readout vector and state)
3. **Gradient Flow in Overlap Space**: Derive ODEs for `dq/dt` under gradient descent
   - Exact for **linear RNNs**
   - Asymptotically exact for **nonlinear RNNs** in the large-N Gaussian limit
4. **Decomposition**: Split `q` into visible (`q_v`) and invisible (`q_i`) components:
   - `q_v` → determines loss, evolves under gradient
   - `q_i` → invisible to loss, but evolves via coupling with `q_v`

### Two Key Phenomena

#### 1. Learning Exposes Connectivity Differences
- Two networks with identical input-output behavior (same loss-visible overlaps)
- May have different loss-invisible overlaps (different internal connectivity)
- Under learning, these differences become visible — the networks diverge
- **Implication**: Functional equivalence ≠ learning equivalence

#### 2. Loss-Invisible Overlaps as Memory
- Invisible overlaps encode training history
- They persist after training and affect future learning trajectories
- Characterized conditions for when this memory effect occurs
- **Implication**: Training history leaves persistent traces in network structure

## Implementation Guide

### Prerequisites
- Understanding of low-rank RNN framework
- Familiarity with gradient descent dynamics
- Knowledge of statistical physics / mean-field theory for large-N limits

### Analytical Steps

1. **Define Low-Rank Parameterization**:
   ```
   W = sum_{r=1}^R m_r n_r^T  (rank R << N)
   ```

2. **Define Overlap Variables**:
   ```
   q_r = n_r^T h  (projection of hidden state onto readout vectors)
   ```

3. **Derive Gradient Flow**:
   ```
   dW/dt = -eta * dL/dW
   => dm_r/dt = ... (depends on visible overlaps)
   => dn_r/dt = ... (depends on visible + invisible overlaps)
   ```

4. **Separate Visible/Invisible Components**:
   ```
   q_visible  = components that affect loss
   q_invisible = orthogonal complement (zero gradient w.r.t. loss)
   ```

5. **Analyze Coupled Dynamics**:
   ```
   dq_visible/dt  = f_visible(q_visible)          (direct gradient)
   dq_invisible/dt = f_invisible(q_visible, q_invisible)  (coupled evolution)
   ```

### Code Example

```python
import numpy as np
from scipy.integrate import solve_ivp

def low_rank_rnn_learning_dynamics(t, state, N, R, activation='tanh'):
    """
    Gradient descent dynamics in overlap space for low-rank RNN.
    
    Args:
        state: [q_visible, q_invisible] concatenated
        N: network size
        R: rank of connectivity
        activation: nonlinearity
    """
    q_v = state[:R]      # loss-visible overlaps
    q_i = state[R:]      # loss-invisible overlaps
    
    # Compute derivatives (simplified linear case)
    dq_v = -learning_rate * (W_visible @ q_v - target)
    dq_i = coupling_matrix @ q_v + A_invisible @ q_i
    
    return np.concatenate([dq_v, dq_i])

# Solve for learning trajectory
sol = solve_ivp(
    low_rank_rnn_learning_dynamics,
    t_span=[0, 100],
    y0=np.concatenate([q_v_init, q_i_init]),
    args=(N=1000, R=2)
)
```

## Applications

- **Understanding RNN training dynamics**: Why some initializations converge faster
- **Network pruning analysis**: What structure is preserved/lost during fine-tuning
- **Transfer learning**: How pre-training history affects downstream adaptation
- **Biological learning predictions**: Testable hypotheses about synaptic plasticity
- **Functionally equivalent networks**: Understanding why "same function, different weights" matters for learning
- **Continual learning**: Invisible overlaps as implicit memory of past tasks

## Pitfalls

- **Large-N approximation**: Results are asymptotically exact only in the infinite-width limit
- **Linear vs. Nonlinear**: Closed-form exact only for linear RNNs; nonlinear requires Gaussian approximation
- **Loss landscape**: Assumes smooth, differentiable loss — not applicable to discrete/quantized settings
- **Rank assumption**: Framework requires low-rank structure; full-rank networks don't benefit from dimensionality reduction

## Related Skills

- nonlinear-rnn-fixed-connectivity-solution
- cavity-method-rnn-analysis
- rnn-task-degradation-analysis
- spiking-mode-neural-networks
- attractor-metadynamics-neural
