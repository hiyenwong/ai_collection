---
name: neural-dynamics-autoregressive-flow-matching-v2
description: Autoregressive Flow Matching (AFM) for probabilistic prediction of neural dynamics. Combines flow matching with autoregressive modeling for neural time series. Trigger words: flow matching, neural dynamics prediction, autoregressive, probabilistic forecasting, neural time series.
---

# Neural Dynamics via Autoregressive Flow Matching

## Paper Reference
- **arXiv**: [2604.11178v1](https://arxiv.org/abs/2604.11178)
- **Authors**: Nicole Rogalla, Yuzhen Qin, Mario Senden et al.
- **Published**: 2026-04-13
- **Citations**: 0

## Core Insight

Autoregressive Flow Matching (AFM) combines flow matching with autoregressive temporal modeling to predict neural dynamics probabilistically, capturing both deterministic structure and stochastic variability of neural time series.

## Key Mechanism

1. **Flow Matching**: Learn a velocity field transporting noise to data distribution
2. **Autoregressive Conditioning**: Condition future predictions on past observations
3. **Probabilistic Output**: Generate distributions over future states, not point estimates
4. **Continuous-time Modeling**: Handle irregularly sampled neural recordings

## Implementation Pattern

```python
import torch
import torch.nn as nn

class AutoregressiveFlowMatcher(nn.Module):
    def __init__(self, input_dim, hidden=256, ctx_window=10):
        super().__init__()
        self.ctx_window = ctx_window
        self.input_dim = input_dim
        self.encoder = nn.Sequential(
            nn.Linear(input_dim * ctx_window, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU())
        self.velocity_net = nn.Sequential(
            nn.Linear(hidden + input_dim + 1, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, input_dim))
    
    def forward(self, context, x_current, t):
        ctx_enc = self.encoder(context.reshape(context.shape[0], -1))
        inp = torch.cat([ctx_enc, x_current, t.unsqueeze(-1)], dim=-1)
        return self.velocity_net(inp)
```

## Applications

- Neural trajectory prediction
- Brain state forecasting
- Generative modeling of neural recordings
- Irregularly sampled time series

## Related Skills

- [[neural-dynamics-universal-translator]]
- [[probabilistic-prediction-neural-dynamics]]
- [[generative-brain-dynamics-models]]

## Activation Keywords

- "neural-dynamics-autoregressive-flow-matching-v2"
- "neural dynamics autoregressive flow matching v2"
- "use neural dynamics autoregressive flow matching v2"
- "neural dynamics autoregressive flow matching v2 help"
- "neural dynamics autoregressive flow matching v2 tool"

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

### Basic Neural Dynamics Autoregressive Flow Matching V2 usage
```
User: "Help me with neural dynamics autoregressive flow matching v2"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed neural dynamics autoregressive flow matching v2 assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
