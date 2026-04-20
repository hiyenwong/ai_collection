---
name: self-sustained-neuron-population-modeling
description: Modeling self-sustained neural activity in recurrent networks without external stimulus. Balanced E/I mechanisms for autonomous persistent activity. Trigger words: self-sustained, autonomous activity, persistent activity, recurrent network, spontaneous activity, balanced network.
---

# Self-sustained Neuron Population Modeling

## Paper Reference
- **arXiv**: [2604.13719v1](https://arxiv.org/abs/2604.13719)
- **Authors**: İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy et al.
- **Published**: 2026-04-15
- **Citations**: 0

## Core Insight

Neural populations can maintain persistent structured activity without external input through carefully balanced recurrent connectivity, modeling spontaneous brain activity and intrinsic memory states.

## Key Mechanism

1. **Balanced E/I**: Excitation and inhibition dynamically balanced at population level
2. **Recurrent Structure**: Specific connectivity patterns sustain activity trajectories
3. **Attractor Dynamics**: Network settles into stable activity patterns
4. **Criticality**: Operates near critical point for sustained but not explosive activity

## Implementation Pattern

```python
import numpy as np

class SelfSustainedNetwork:
    def __init__(self, n_exc=800, n_inh=200, g=1.5):
        self.n = n_exc + n_inh
        self.n_exc = n_exc
        p_conn = 0.1
        self.W = np.zeros((self.n, self.n))
        exc_mask = np.zeros((self.n, self.n)); exc_mask[:n_exc, :] = 1
        self.W += np.random.randn(self.n, self.n) * p_conn * exc_mask / np.sqrt(n_exc * p_conn)
        inh_mask = np.zeros((self.n, self.n)); inh_mask[n_exc:, :] = 1
        self.W -= g * np.random.randn(self.n, self.n) * p_conn * inh_mask / np.sqrt(n_inh * p_conn)
        np.fill_diagonal(self.W, 0)
    
    def run(self, n_steps=5000, r0=None):
        r = r0 or np.random.rand(self.n) * 0.1
        history = [r.copy()]
        for _ in range(n_steps):
            r_new = -r + np.tanh(self.W @ r)
            r = np.maximum(r + 0.1 * r_new, 0)
            history.append(r.copy())
        return np.array(history)
```

## Applications

- Modeling spontaneous brain activity (default mode network)
- Intrinsic memory and thought processes
- Autonomous cognitive systems
- Resting-state fMRI dynamics

## Related Skills

- [[self-sustained-neural-population]]
- [[neural-population-dynamics]]
- [[attractor-metadynamics-neural]]

## Activation Keywords

- "self-sustained-neuron-population-modeling"
- "self sustained neuron population modeling"
- "use self sustained neuron population modeling"
- "self sustained neuron population modeling help"
- "self sustained neuron population modeling tool"

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

### Basic Self Sustained Neuron Population Modeling usage
```
User: "Help me with self sustained neuron population modeling"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed self sustained neuron population modeling assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
