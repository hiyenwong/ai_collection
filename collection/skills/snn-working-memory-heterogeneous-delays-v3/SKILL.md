---
name: snn-working-memory-heterogeneous-delays-v3
description: Working memory in recurrent SNNs with heterogeneous synaptic delays. Uses delay distributions to stabilize persistent activity without fine-tuned connectivity. Trigger words: working memory, heterogeneous delays, recurrent SNN, persistent activity, synaptic delays.
---

# Working Memory in Recurrent SNNs with Heterogeneous Delays

## Paper Reference
- **arXiv**: [2604.14096v1](https://arxiv.org/abs/2604.14096)
- **Authors**: Laurent U Perrinet et al.
- **Published**: 2026-04-15
- **Citations**: 0

## Core Insight

Heterogeneous synaptic delays in recurrent SNNs naturally stabilize persistent activity for working memory, eliminating the need for precisely tuned connectivity weights. The diversity of delays acts as a built-in regularization mechanism.

## Key Mechanism

1. **Delay Distribution**: Use a distribution of synaptic delays (exponential/log-normal) across recurrent connections
2. **Temporal Smoothing**: Different delays create temporal averaging that smooths activity fluctuations
3. **Stability Without Fine-tuning**: Network maintains persistent activity across parameter ranges

## Implementation Pattern

```python
import numpy as np

class HeterogeneousDelaySNN:
    def __init__(self, n, delay_min=1, delay_max=20):
        self.W = np.random.randn(n, n) * 0.1
        self.W[np.random.random(self.W.shape) > 0.1] = 0
        self.delays = np.clip(np.round(np.random.lognormal(2, 1, self.W.shape)), delay_min, delay_max).astype(int)
        self.max_delay = int(self.delays.max())
        self.spike_history = np.zeros((n, self.max_delay + 1))
    
    def step(self, membrane, input_current=None):
        recurrent = np.zeros(len(membrane))
        for j in range(len(membrane)):
            for i in range(len(membrane)):
                d = self.delays[i, j]
                recurrent[i] += self.W[i, j] * self.spike_history[j, d]
        membrane *= 0.95
        membrane += recurrent + (input_current if input_current is not None else 0)
        spike = (membrane > 1.0).astype(float)
        membrane[spike > 0] = 0
        self.spike_history = np.roll(self.spike_history, 1, axis=1)
        self.spike_history[:, 0] = spike
        return membrane, spike
```

## Applications

- Working memory modeling in cognitive neuroscience
- Delay-dependent persistent activity in PFC
- Biologically plausible short-term memory systems
- Robust SNN architectures

## Related Skills

- [[snn-working-memory-heterogeneous-delays]]
- [[snn-learning-rules-dynamics]]
- [[brain-inspired-memory-ai-agents]]
