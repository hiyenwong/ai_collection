---
name: neuroplastic-plasticity-optimizer
description: "NeuroPlastic - A plasticity-modulated optimizer for biologically inspired learning dynamics. Incorporates synaptic plasticity mechanisms like Hebbian learning, homeostatic plasticity, and metaplasticity into gradient-based optimization for enhanced learning stability and biological plausibility."
tags: ["neuroscience", "optimizer", "plasticity", "hebbian-learning", "biologically-inspired", "deep-learning"]
---

# NeuroPlastic: Plasticity-Modulated Optimizer

A biologically-inspired optimizer that integrates synaptic plasticity mechanisms into gradient-based learning, combining the computational efficiency of backpropagation with the stability and adaptability of biological neural networks.

## Overview

NeuroPlastic modifies traditional gradient-based optimization by incorporating three key biological plasticity mechanisms:

1. **Hebbian Learning**: "Neurons that fire together, wire together"
2. **Homeostatic Plasticity**: Maintaining stable activity levels
3. **Metaplasticity**: The plasticity of plasticity itself

## Key Concepts

### Hebbian Component
Strengthens weights when pre- and post-synaptic neurons are correlated:
```
Δw_hebb ∝ pre_activation × post_activation
```

### Homeostatic Regulation
Prevents runaway excitation/inhibition:
```
Δw_homeo ∝ target_activity - actual_activity
```

### Metaplasticity Modulation
Adapts learning rates based on weight history:
```
η_eff = η × f(weight_history)
```

## When to Use

- Training deep networks with biological constraints
- Scenarios requiring stable learning dynamics
- Continual learning (avoiding catastrophic forgetting)
- Neuromorphic computing applications
- Research on biologically-plausible learning

## Core Algorithm

```python
class NeuroPlastic(Optimizer):
    """
    Plasticity-modulated optimizer combining gradient descent
    with biological synaptic plasticity mechanisms.
    """
    
    def __init__(self, params, lr=1e-3, 
                 hebb_strength=0.1,
                 homeo_rate=0.01,
                 metaplastic_tau=1000):
        """
        Args:
            lr: Base learning rate
            hebb_strength: Strength of Hebbian component (0-1)
            homeo_rate: Rate of homeostatic adjustment
            metaplastic_tau: Time constant for metaplasticity
        """
        defaults = dict(
            lr=lr, 
            hebb_strength=hebb_strength,
            homeo_rate=homeo_rate,
            metaplastic_tau=metaplastic_tau
        )
        super().__init__(params, defaults)
        
        # State tracking
        self.state = {}
        self.step_count = 0
        
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        
        self.step_count += 1
        
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                
                grad = p.grad.data
                state = self.state[p]
                
                # Initialize state
                if len(state) == 0:
                    state['momentum'] = torch.zeros_like(p.data)
                    state['hebb_trace'] = torch.zeros_like(p.data)
                    state['activity'] = torch.zeros(p.data.size(0))
                    state['weight_history'] = torch.zeros_like(p.data)
                    state['step'] = 0
                
                momentum = state['momentum']
                hebb_trace = state['hebb_trace']
                activity = state['activity']
                weight_history = state['weight_history']
                
                # Get hyperparameters
                lr = group['lr']
                hebb_strength = group['hebb_strength']
                homeo_rate = group['homeo_rate']
                tau = group['metaplastic_tau']
                
                # Compute activations (for Hebbian)
                pre_act = torch.sigmoid(p.data.mean(dim=1, keepdim=True))
                post_act = torch.sigmoid(grad.mean(dim=0, keepdim=True))
                
                # Hebbian update: pre × post
                hebb_update = torch.mm(pre_act, post_act)
                hebb_trace.mul_(0.9).add_(hebb_update, alpha=0.1)
                
                # Homeostatic regulation
                target_activity = 0.1  # 10% average activity
                current_activity = torch.sigmoid(p.data).mean(dim=1)
                activity.mul_(0.99).add_(current_activity, alpha=0.01)
                homeo_factor = target_activity - activity
                
                # Metaplasticity: learning rate depends on weight magnitude
                weight_age = state['step'] / tau
                metaplastic_factor = torch.exp(-weight_age)
                
                # Combined update
                # Base gradient + Hebbian + Homeostatic
                effective_lr = lr * metaplastic_factor
                
                # Momentum update
                momentum.mul_(0.9).add_(grad + 
                    hebb_strength * hebb_trace + 
                    homeo_rate * homeo_factor.unsqueeze(1))
                
                # Parameter update
                p.data.add_(momentum, alpha=-effective_lr)
                
                # Update history
                weight_history.mul_(0.99).add_(p.data, alpha=0.01)
                state['step'] += 1
        
        return loss
```

## Implementation Details

### Hebbian Learning Component

```python
def compute_hebbian_update(pre_synaptic, post_synaptic, method="covariance"):
    """
    Compute Hebbian weight update.
    
    Methods:
        - "classic": Simple correlation
        - "covariance": Covariance-based (Sejnowski)
        - "oja": Oja's rule (normalized)
        - "bcm": BCM theory (sliding threshold)
    """
    if method == "classic":
        # Classic Hebb: Δw ∝ x × y
        return torch.outer(pre_synaptic, post_synaptic)
    
    elif method == "covariance":
        # Covariance: Δw ∝ (x - x̄)(y - ȳ)
        pre_mean = pre_synaptic.mean()
        post_mean = post_synaptic.mean()
        return torch.outer(pre_synaptic - pre_mean, 
                          post_synaptic - post_mean)
    
    elif method == "oja":
        # Oja's rule: Δw ∝ x × y - α × w × y²
        correlation = torch.outer(pre_synaptic, post_synaptic)
        normalization = 0.001 * torch.outer(
            (pre_synaptic ** 2).sum() * torch.ones_like(pre_synaptic),
            post_synaptic ** 2
        )
        return correlation - normalization
    
    elif method == "bcm":
        # BCM: Δw ∝ x × y × (y - θ_M)
        theta_m = post_synaptic.mean() ** 2
        return torch.outer(pre_synaptic, 
                          post_synaptic * (post_synaptic - theta_m))
```

### Homeostatic Plasticity

```python
class HomeostaticRegulator:
    """
    Maintains neural activity within target range.
    """
    
    def __init__(self, target_activity=0.1, 
                 time_constant=100):
        self.target = target_activity
        self.tau = time_constant
        self.activity_history = []
        
    def update(self, current_activity):
        """
        Compute homeostatic scaling factor.
        """
        self.activity_history.append(current_activity)
        if len(self.activity_history) > self.tau:
            self.activity_history.pop(0)
        
        # Moving average activity
        avg_activity = sum(self.activity_history) / len(self.activity_history)
        
        # Scaling factor (increase if below target, decrease if above)
        if avg_activity < self.target * 0.5:
            return 1.1  # Increase excitability
        elif avg_activity > self.target * 2:
            return 0.9  # Decrease excitability
        return 1.0
    
    def synaptic_scaling(self, weights, current_rates):
        """
        Scale synaptic weights to maintain firing rates.
        """
        target_rates = torch.full_like(current_rates, self.target)
        scaling_factors = target_rates / (current_rates + 1e-8)
        
        # Apply multiplicative scaling
        return weights * scaling_factors.unsqueeze(1)
```

### Metaplasticity

```python
class MetaplasticModulator:
    """
    Modulates learning based on synaptic history.
    Implements cascade model of metaplasticity.
    """
    
    def __init__(self, n_states=3, 
                 transition_rates=None):
        """
        Args:
            n_states: Number of metaplastic states
            transition_rates: Probability of state transitions
        """
        self.n_states = n_states
        self.rates = transition_rates or [0.1] * (n_states - 1)
        self.states = None
        
    def initialize(self, weight_shape):
        """Initialize all synapses to state 0."""
        self.states = torch.zeros(weight_shape, dtype=torch.long)
        
    def get_effective_lr(self, base_lr):
        """
        Get learning rate for each synapse based on state.
        Later states have lower learning rates (more stable).
        """
        # Exponentially decreasing learning rates
        factors = torch.tensor([
            base_lr * (0.5 ** s) 
            for s in range(self.n_states)
        ])
        return factors[self.states]
    
    def update_states(self, weight_changes):
        """
        Update metaplastic states based on activity.
        """
        # Probability of transitioning to next state
        for s in range(self.n_states - 1):
            mask = (self.states == s) & \
                   (torch.rand_like(weight_changes) < self.rates[s])
            self.states[mask] = s + 1
```

## Complete NeuroPlastic Optimizer

```python
import torch
from torch.optim import Optimizer

class NeuroPlastic(Optimizer):
    """
    Complete NeuroPlastic optimizer with all three mechanisms.
    """
    
    def __init__(self, params, lr=0.001, 
                 betas=(0.9, 0.999),
                 eps=1e-8,
                 weight_decay=0,
                 hebb_strength=0.05,
                 hebb_method="covariance",
                 homeo_target=0.1,
                 homeo_rate=0.001,
                 metaplastic=False,
                 metaplastic_tau=1000):
        """
        Args:
            lr: Learning rate
            betas: Coefficients for running averages
            eps: Term added for numerical stability
            weight_decay: L2 penalty
            hebb_strength: Weight of Hebbian component
            hebb_method: Hebbian update rule
            homeo_target: Target firing rate
            homeo_rate: Strength of homeostatic regulation
            metaplastic: Enable metaplasticity
            metaplastic_tau: Time constant for plasticity
        """
        defaults = dict(
            lr=lr, betas=betas, eps=eps,
            weight_decay=weight_decay,
            hebb_strength=hebb_strength,
            hebb_method=hebb_method,
            homeo_target=homeo_target,
            homeo_rate=homeo_rate,
            metaplastic=metaplastic,
            metaplastic_tau=metaplastic_tau
        )
        super().__init__(params, defaults)
        
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                
                grad = p.grad.data
                state = self.state[p]
                
                # Initialize state
                if len(state) == 0:
                    state['step'] = 0
                    state['exp_avg'] = torch.zeros_like(p.data)
                    state['exp_avg_sq'] = torch.zeros_like(p.data)
                    if group['metaplastic']:
                        state['plasticity_state'] = torch.zeros_like(p.data)
                
                exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                beta1, beta2 = group['betas']
                
                state['step'] += 1
                
                # Weight decay
                if group['weight_decay'] != 0:
                    grad = grad.add(p.data, alpha=group['weight_decay'])
                
                # Hebbian component
                hebb_update = self._compute_hebbian(p, group)
                grad = grad + group['hebb_strength'] * hebb_update
                
                # Homeostatic component
                homeo_update = self._compute_homeostatic(p, group)
                grad = grad + group['homeo_rate'] * homeo_update
                
                # Adam update with metaplasticity
                exp_avg.mul_(beta1).add_(grad, alpha=1-beta1)
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1-beta2)
                
                bias_correction1 = 1 - beta1 ** state['step']
                bias_correction2 = 1 - beta2 ** state['step']
                
                step_size = group['lr'] / bias_correction1
                
                # Metaplastic modulation
                if group['metaplastic']:
                    age = state['step'] / group['metaplastic_tau']
                    metaplastic_factor = torch.exp(-age)
                    step_size = step_size * metaplastic_factor
                
                denom = (exp_avg_sq.sqrt() / bias_correction2.sqrt()).add_(group['eps'])
                
                p.data.addcdiv_(exp_avg, denom, value=-step_size)
        
        return loss
    
    def _compute_hebbian(self, p, group):
        """Compute Hebbian update."""
        # Simplified: use current weights as proxy for activations
        pre = torch.sigmoid(p.data.mean(dim=1, keepdim=True))
        post = torch.sigmoid(p.data.mean(dim=0, keepdim=True))
        return torch.mm(pre, post)
    
    def _compute_homeostatic(self, p, group):
        """Compute homeostatic update."""
        current_activity = torch.sigmoid(p.data).mean(dim=1)
        target = torch.full_like(current_activity, group['homeo_target'])
        deviation = target - current_activity
        return deviation.unsqueeze(1).expand_as(p.data)
```

## Usage Examples

### Basic Training

```python
import torch
import torch.nn as nn

# Define model
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# Use NeuroPlastic optimizer
optimizer = NeuroPlastic(
    model.parameters(),
    lr=1e-3,
    hebb_strength=0.05,
    homeo_rate=0.001,
    metaplastic=True
)

# Training loop
for epoch in range(100):
    for batch in dataloader:
        x, y = batch
        
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
```

### Continual Learning

```python
# NeuroPlastic helps prevent catastrophic forgetting

# Task 1
train_task1(model, optimizer, task1_data)

# Task 2 (same optimizer continues)
train_task2(model, optimizer, task2_data)
# Hebbian traces preserve Task 1 knowledge
# Homeostatic regulation maintains stability
```

## Advantages

1. **Biological Plausibility**: Local learning rules
2. **Stability**: Homeostatic regulation prevents runaway weights
3. **Continual Learning**: Hebbian traces preserve old knowledge
4. **Adaptive**: Metaplasticity adjusts to learning history
5. **Compatible**: Works with existing PyTorch infrastructure

## References

- Paper: "NeuroPlastic: A Plasticity-Modulated Optimizer for Biologically Inspired Learning Dynamics"
- Authors: Douglas Jiang, Yuechen Wang, Jiayi Wang
- arXiv: 2604.26297
- Category: cs.LG
- Published: 2026-04-29

## Related Skills

- `decolle-snn-learning`: Local learning in SNNs
- `synaptic-plasticity`: Synaptic plasticity mechanisms
- `brain-inspired-snn-pattern-analysis`: SNN pattern analysis
