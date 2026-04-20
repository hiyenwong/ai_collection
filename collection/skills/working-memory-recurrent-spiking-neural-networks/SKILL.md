---
name: working-memory-recurrent-spiking-neural-networks
category: neuroscience
description: Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Achieves precise temporal pattern storage and recall through delay-based coding.
trigger: working memory snn, heterogeneous delays, recurrent spiking memory, temporal pattern storage, delay-based coding
---

# Working Memory in Recurrent SNN with Heterogeneous Delays

## Paper
- **Title**: Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Author**: Laurent U Perrinet
- **Date**: April 15, 2026
- **arXiv**: 2604.14096v1

## Overview
Working memory -- the ability to store and recall precise temporal patterns of neural activity -- is implemented in recurrent SNNs using heterogeneous synaptic delays as a computational resource rather than a nuisance.

## Core Mechanism
- **Heterogeneous synaptic delays** serve as memory traces
- Different delay values create **temporal basis functions** for pattern storage
- **Recurrent connectivity** maintains activity through delayed feedback
- No need for persistent firing -- memory encoded in **delay structure**

## Key Findings
1. Heterogeneous delays enable **precise temporal pattern** storage
2. Memory capacity scales with **delay diversity** not just neuron count
3. **Energy efficient** compared to persistent activity models
4. Biologically realistic -- cortical synapses have naturally heterogeneous delays

## Architecture
```
Input → [Spike encoding] → Recurrent layer with heterogeneous delays → Output
                                ↓
                      Delay distribution: τ ∈ [τ_min, τ_max]
                      Each connection has unique delay τ_ij
```

### Delay-Based Memory Encoding
```python
class DelayedRecurrentSNN:
    def __init__(self, n_neurons, delay_range=(1, 20)):
        self.delays = np.random.randint(*delay_range, (n_neurons, n_neurons))
        self.spike_buffers = [deque(maxlen=max_delay) for ...]
        
    def step(self, spikes):
        # Apply heterogeneous delays
        delayed_spikes = self.apply_delays(spikes)
        # Recurrent computation with delayed inputs
        membrane = self.weights @ delayed_spikes + self.input_weights @ spikes
        output = self.fire(membrane)
        return output
```

## Applications
- Temporal pattern recognition
- Sequence learning
- Working memory tasks
- Neuromorphic computing

## Related Skills
- snn-working-memory-heterogeneous-delays-v3
- learning-neuron-dynamics-deep-snn


## Latest Research Updates

### arXiv:2604.14096v1 (2026-04-15)
**Title:** Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
**Authors:** Laurent U Perrinet
**Link:** https://arxiv.org/abs/2604.14096v1

### arXiv:2604.15997v1 (2026-04-17)
**Title:** Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks
**Authors:** Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi
**Link:** https://arxiv.org/abs/2604.15997v1

## Activation Keywords

- "working-memory-recurrent-spiking-neural-networks"
- "working memory recurrent spiking neural networks"
- "use working memory recurrent spiking neural networks"
- "working memory recurrent spiking neural networks help"
- "working memory recurrent spiking neural networks tool"

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

### Basic Working Memory Recurrent Spiking Neural Networks usage
```
User: "Help me with working memory recurrent spiking neural networks"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed working memory recurrent spiking neural networks assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
