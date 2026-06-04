---
name: free-energy-principle-moe-routing
description: "Free Energy Principle-based MoE routing using LIF membrane dynamics. Solves domain transition failures in sparse MoE with three mechanisms: temporal memory (beta), precision-weighted gating (Pi), and anticipatory routing. 124x improvement at transitions. Activation: free energy principle, MoE routing, domain transition, predictive routing, LIF gating, Friston, mixture of experts."
---

# Free Energy Principle for Mixture-of-Experts Routing

> Recovers the Free Energy Principle in MoE routing using LIF membrane dynamics. Three lightweight mechanisms solve domain transition failures: temporal memory (beta), precision-weighted gating (Pi), and anticipatory routing. Achieves 124x improvement in correct expert assignment at domain boundaries.

## Metadata
- **Source**: arXiv:2605.00604
- **Authors**: Man Yung Wong (Russell)
- **Published**: 2026-05-01
- **Code**: https://github.com/russellwmy/affinity-is-not-enough

## Core Problem

Standard **affinity-based MoE routing** catastrophically fails at domain transitions:
- At the transition point, standard routing assigns only **0.006 ± 0.001** probability to the correct expert
- Stateless predictors cannot detect approaching transitions (pre-transition tokens are distributionally identical to within-domain tokens)
- This is a structural limitation of current MoE architectures

## Core Methodology

### Three Lightweight Gate Modifications

#### 1. Temporal Memory (β) — Per-Expert LIF Membrane Potential
- Each expert maintains a **LIF membrane potential** that accumulates routing context across tokens
- Inspired by biological neuron membrane dynamics: integrates incoming signals, leaks over time, fires when threshold reached
- Provides **temporal context** that pure affinity lacks
- Allows the gate to "remember" which experts have been useful recently

```python
# LIF dynamics for routing memory
tau = 2.0  # membrane time constant
beta_new = beta_old * exp(-1/tau) + routing_signal
# When beta crosses threshold, expert becomes active
```

#### 2. Precision-Weighted Gating (Π) — Per-Expert Inverse Variance
- Tracks **inverse variance of recent prediction error** for each expert
- Yields 31× contrast between reliable and unreliable experts
- Experts with low prediction variance (high precision) get higher routing weight
- Implements the precision-weighted prediction error from Free Energy Principle

#### 3. Anticipatory Routing — Next-State Predictor
- Predicts the **next hidden state** conditioned on β-accumulated context
- Cannot work alone (gives +0.000 improvement) — needs β memory
- Enables the gate to **pre-position** experts before domain transitions
- Places 0.86 probability on the correct expert BEFORE the domain appears in input

### Free Energy Principle Connection

The routing mechanism maps directly to Friston's Free Energy Principle:
- **Prediction**: The gate predicts which expert will be needed
- **Prediction Error**: Routing adjusts based on expert performance (prediction error)
- **Precision Weighting**: More reliable experts get higher weight (precision)
- **Active Inference**: The gate actively seeks to minimize free energy (surprise) by routing correctly

### Super-Additive Interaction

The key discovery is the **super-additive β × Ant interaction**:

| Configuration | Improvement over Standard | Oracle Gap Closed |
|---------------|--------------------------|-------------------|
| Anticipation alone | +0.000 | 0% |
| β alone | +0.295 | ~40% |
| β + Ant combined | +0.741 | 75% |
| **Sum of individual** | 0.295 | — |
| **Super-additive bonus** | **+0.446** | — |

This is structural: anticipation needs temporal context (β) to be useful, and β needs anticipation to fully close the gap.

## Implementation Guide

### Prerequisites
- Mixture-of-Experts architecture (e.g., in PyTorch)
- Understanding of LIF neuron dynamics
- Free Energy Principle basics

### Beta-MoE Gate Implementation

```python
import torch
import torch.nn as nn
import math

class LIFMembrane(nn.Module):
    """LIF membrane potential for routing temporal memory."""
    def __init__(self, num_experts, tau=2.0):
        super().__init__()
        self.num_experts = num_experts
        self.tau = tau
        self.register_buffer('beta', torch.zeros(num_experts))
    
    def forward(self, routing_signal):
        # LIF dynamics: leak + integrate
        leak = math.exp(-1.0 / self.tau)
        self.beta = self.beta * leak + routing_signal
        return self.beta

class PrecisionWeightedGate(nn.Module):
    """Precision-weighted MoE gating."""
    def __init__(self, dim, num_experts):
        super().__init__()
        self.gate = nn.Linear(dim, num_experts)
        self.lif = LIFMembrane(num_experts)
        self.register_buffer('error_var', torch.ones(num_experts))
    
    def update_precision(self, expert_errors):
        """Update inverse variance (precision) from prediction errors."""
        ema = 0.9
        self.error_var = ema * self.error_var + (1 - ema) * expert_errors.pow(2)
    
    def forward(self, x):
        # Affinity scores
        logits = self.gate(x)
        
        # Temporal memory (LIF integration)
        beta = self.lif(logits.softmax(-1))
        
        # Precision weighting
        precision = 1.0 / (self.error_var + 1e-8)
        weighted = logits + torch.log(precision)
        
        # Combined routing
        routing_probs = (weighted + beta).softmax(-1)
        return routing_probs

class AnticipatoryRouter(nn.Module):
    """Next-state predictor for anticipatory routing."""
    def __init__(self, dim, hidden_dim, num_experts):
        super().__init__()
        self.predictor = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_experts)
        )
    
    def forward(self, accumulated_state):
        """Predict next routing distribution from accumulated context."""
        return self.predictor(accumulated_state).softmax(-1)
```

### Combined β-MoE Architecture

```python
class BetaMoE(nn.Module):
    """Full Beta-MoE with all three mechanisms."""
    def __init__(self, dim, num_experts, hidden_dim=64):
        super().__init__()
        self.gate = PrecisionWeightedGate(dim, num_experts)
        self.anticipator = AnticipatoryRouter(dim, hidden_dim, num_experts)
        self.experts = nn.ModuleList([ExpertMLP(dim) for _ in range(num_experts)])
        self.accumulated_state = None
    
    def forward(self, x):
        # Update accumulated state
        if self.accumulated_state is None:
            self.accumulated_state = x.detach()
        else:
            self.accumulated_state = 0.9 * self.accumulated_state + 0.1 * x.detach()
        
        # Anticipatory prediction
        anticipatory = self.anticipator(self.accumulated_state)
        
        # Standard + precision + memory routing
        routing = self.gate(x)
        combined = routing + anticipatory  # Super-additive combination
        
        # Route to experts
        top_k = 2
        probs, indices = combined.topk(top_k, dim=-1)
        output = sum(p * e(x) for p, e, idx in zip(probs, self.experts, indices))
        
        # Update precision based on expert output quality
        return output
```

## Results

### Domain Transition Handling
| Method | Transition Probability | Improvement |
|--------|----------------------|-------------|
| Standard MoE | 0.006 ± 0.001 | baseline |
| β-MoE | 0.748 ± 0.002 | **124×** |

### Character-level MoE Language Model
| Method | Transition BPC | Pre-transition Accuracy |
|--------|---------------|------------------------|
| Standard MoE | 6.56 ± 0.01 | 0.42 ± 0.12 |
| β-MoE | 4.01 ± 0.15 | — |
| β + Ant | — | **0.86 ± 0.02** |

## Applications
- Mixture-of-Experts LLMs with domain transitions
- Multi-task learning with dynamic expert switching
- Continual learning with catastrophic forgetting prevention
- Any MoE system that processes sequential data with distribution shifts

## Key Insights
1. **Stateless routing is fundamentally limited**: cannot detect approaching domain transitions
2. **LIF dynamics provide natural temporal memory**: membrane potential accumulates routing context
3. **Free Energy Principle provides theoretical grounding**: precision-weighted prediction errors are optimal
4. **Super-additive interactions matter**: combining mechanisms yields more than sum of parts
5. **Anticipation needs memory**: without β, anticipatory routing is useless

## Pitfalls
- β alone is insufficient — must combine with anticipation for full benefit
- Precision tracking needs careful EMA smoothing to avoid overfitting to noise
- LIF time constant τ must be tuned per task (too fast = no memory, too slow = outdated)
- Reference implementation is ~200 lines per mechanism — keep it lightweight
- The super-additive effect only emerges when all three mechanisms interact properly

## Related Skills
- moe-optimal-transport-routing
- free-energy-moe-routing
- emotion-evolved-moe-modularity
- unipool-shared-expert-moe
- routing-distraction-multimodal-moe
- adaptive-distributionally-robust-control
