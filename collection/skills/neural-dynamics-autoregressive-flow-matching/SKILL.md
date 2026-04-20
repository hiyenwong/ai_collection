---
name: neural-dynamics-autoregressive-flow-matching
description: Autoregressive Flow Matching (AFM) framework for probabilistic prediction of neural dynamics with uncertainty quantification
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neural-dynamics, flow-matching, probabilistic-prediction, generative-modeling]
    source_paper: "Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching (arXiv:2604.11178)"
    authors: "Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar, Marcel van Gerven"
    published: "2026-04-13"
    category: "neuroscience"
---

# Neural Dynamics Autoregressive Flow Matching

## Overview
This paper introduces a generative forecasting framework for neural dynamics using autoregressive flow matching (AFM). It enables probabilistic prediction of brain activity trajectories with principled uncertainty quantification, addressing the challenge of predicting complex neural time series.

## Key Concepts

### Autoregressive Flow Matching
- Combines flow matching with autoregressive modeling
- Generates future neural states conditioned on past observations
- Captures temporal dependencies in neural dynamics

### Probabilistic Forecasting
```
Past Neural Activity --> AFM Model (Flow) --> Future Predictions
                              |
                        Uncertainty Quantification
```

## Implementation Pattern

```python
import torch
import torch.nn as nn

class NeuralDynamicsAFM:
    """Autoregressive Flow Matching for neural dynamics prediction."""
    
    def __init__(self, input_dim, hidden_dim=256, num_flows=4):
        self.input_dim = input_dim
        self.flows = nn.ModuleList([
            CouplingLayer(input_dim, hidden_dim) 
            for _ in range(num_flows)
        ])
        self.temporal_encoder = TemporalEncoder(input_dim, hidden_dim)
    
    def forward_flow(self, x, t):
        """Apply flow matching transformation."""
        z = x
        for flow in self.flows:
            z = flow(z, t)
        return z
    
    def predict_trajectory(self, past_activity, horizon=10):
        """Generate probabilistic future predictions."""
        context = self.temporal_encoder(past_activity)
        
        trajectories = []
        for _ in range(100):  # Monte Carlo samples
            z = torch.randn(self.input_dim)
            trajectory = [z]
            
            for step_t in range(horizon):
                dz = self.forward_flow(z, step_t)
                z = z + dz
                trajectory.append(z)
            
            trajectories.append(torch.stack(trajectory))
        
        trajectories = torch.stack(trajectories)
        mean = trajectories.mean(dim=0)
        std = trajectories.std(dim=0)
        
        return mean, std
    
    def flow_matching_loss(self, x_0, x_1, t):
        """Flow matching objective."""
        u_t = x_1 - x_0  # Target velocity
        v_t = self.velocity_network(x_t, t)  # Predicted velocity
        return ((v_t - u_t) ** 2).mean()
```

## Applications
- Brain activity prediction
- Neural state forecasting
- Clinical outcome prediction
- BCI trajectory planning

## References
- Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- Authors: Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar, Marcel van Gerven
- arXiv: 2604.11178 (2026-04-13)

## Activation
- neural dynamics prediction
- autoregressive flow matching
- probabilistic forecasting
- brain activity prediction
- flow matching
- 神经动力学预测
- 自回归流匹配

## Activation Keywords

- "neural-dynamics-autoregressive-flow-matching"
- "neural dynamics autoregressive flow matching"
- "use neural dynamics autoregressive flow matching"
- "neural dynamics autoregressive flow matching help"
- "neural dynamics autoregressive flow matching tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Neural Dynamics Autoregressive Flow Matching usage
```
User: "Help me with neural dynamics autoregressive flow matching"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed neural dynamics autoregressive flow matching assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
