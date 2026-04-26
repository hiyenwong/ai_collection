---
name: probabilistic-prediction-neural-dynamics-via-autoregressive
description: "Probabilistic prediction of neural dynamics via autoregressive flow matching. Uses continuous normalizing flows to model neural population dynamics with uncertainty quantification. Activation: neural dynamics flow matching, autoregressive flow, neural dynamics prediction, probabilistic neural modeling, continuous normalizing flow"
---

# Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching

## Overview

This paper introduces an autoregressive flow matching framework for probabilistic prediction of neural dynamics. It combines continuous normalizing flows (CNFs) with autoregressive modeling to capture complex temporal dependencies in neural population activity while providing calibrated uncertainty estimates.

## Source Paper

- **Title:** Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- **arXiv: 2604.11178v1
- **Date:** 2026-04-13
- **Authors:** Nicole Rogalla, Yuzhen Qin, Mario Senden et al.
- **PDF: https://arxiv.org/pdf/2604.11178v1

## Core Concepts

### Flow Matching
- Direct training of continuous normalizing flows without likelihood evaluation
- Regression-based objective: learn vector field that transports noise to data
- More stable training than traditional CNFs (no ODE solver during training)
- Arbitrary sample generation after training

### Autoregressive Neural Dynamics
- Model conditional distribution p(x_t | x_{t-1}, ..., x_{t-k})
- Capture temporal dependencies in neural spiking/activity patterns
- Handle non-stationarity and state transitions
- Probabilistic forecasting with calibrated uncertainty

## Implementation

### Step 1: Flow Matching Objective

```python
import torch
import torch.nn.functional as F

def flow_matching_loss(model, x1, condition):
    t = torch.rand(x1.shape[0], 1)
    x0 = torch.randn_like(x1)
    xt = t * x1 + (1 - t) * x0
    vt = x1 - x0
    v_pred = model(xt, t, condition)
    return F.mse_loss(v_pred, vt)
```

### Step 2: Autoregressive Dynamics Model

```python
class NeuralDynamicsFlow(torch.nn.Module):
    def __init__(self, n_neurons, hidden_dim=256, context_window=10):
        super().__init__()
        self.n_neurons = n_neurons
        self.context_window = context_window
        self.context_encoder = torch.nn.Sequential(
            torch.nn.Linear(n_neurons * context_window, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim)
        )
        self.vector_field = torch.nn.Sequential(
            torch.nn.Linear(n_neurons + hidden_dim + 1, hidden_dim),
            torch.nn.SiLU(),
            torch.nn.Linear(hidden_dim, hidden_dim),
            torch.nn.SiLU(),
            torch.nn.Linear(hidden_dim, n_neurons)
        )

    def forward(self, xt, t, context):
        ctx_emb = self.context_encoder(context)
        combined = torch.cat([xt, ctx_emb, t], dim=-1)
        return self.vector_field(combined)

    @torch.no_grad()
    def sample_trajectory(self, initial_context, n_steps):
        x = torch.randn(1, self.n_neurons)
        trajectory = [x]
        for step in range(n_steps):
            dt = 0.1
            v = self(x, torch.tensor([[dt]]), initial_context)
            x = x + v * dt
            trajectory.append(x.clone())
            initial_context = torch.cat([initial_context[:, self.n_neurons:], x], dim=1)
        return torch.cat(trajectory, dim=0)
```

### Step 3: Training

```python
def train_neural_dynamics(model, neural_data, epochs=100, lr=1e-3):
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    for epoch in range(epochs):
        for i in range(model.context_window, len(neural_data)):
            context = neural_data[i-model.context_window:i].flatten().unsqueeze(0)
            target = neural_data[i].unsqueeze(0)
            optimizer.zero_grad()
            loss = flow_matching_loss(model, target, context)
            loss.backward()
            optimizer.step()
    return model
```

## Advantages

1. Uncertainty quantification: Calibrated confidence intervals on predictions
2. Arbitrary sampling: Generate diverse neural trajectories
3. No likelihood evaluation: Stable training via regression
4. Conditional generation: Control dynamics with external variables

## Related Skills

- neural-dynamics-autoregressive-flow-matching
- neural-population-dynamics
- neural-dynamics-universal-translator

## Activation Keywords

- neural dynamics flow matching, autoregressive flow, neural dynamics prediction, probabilistic neural modeling, continuous normalizing flow, vector field learning
