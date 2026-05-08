---
name: hebbian-learning-benchmark-memory
description: >
  Benchmarking of seven local Hebbian learning rules for associative memory storage,
  prototype extraction, and weight information capacity in recurrent neural networks
  with winner-take-all dynamics. Compares additive Hebb, covariance learning, and
  Bayesian-Hebbian rules across non-modular and modular architectures.
  Use when: benchmarking Hebbian learning rules, associative memory design, prototype
  extraction, synaptic plasticity comparison, content-addressable memory, winner-take-all
  networks, binary pattern storage, memory capacity analysis.
  Activation: hebbian learning, associative memory, prototype extraction, memory capacity,
  winner-take-all, WTA dynamics, covariance learning, Bayesian-Hebbian, binary patterns,
  sparse coding, plasticity benchmark, 赫布学习, 联想记忆, 原型提取, 记忆容量
---

# Hebbian Learning Rules Benchmark for Associative Memory

Based on: Lansner et al. (2026), arXiv:2605.01074

## Problem

Many Hebbian learning rules exist for associative memory, but systematic comparison
ac architectures and tasks is limited. Key question: **which rule provides the best
trade-off between storage capacity, prototype extraction, and robustness to correlations?**

## Benchmark Setup

### Network Architecture
- **Non-modular**: Single recurrent network with winner-take-all (WTA) dynamics
- **Modular**: Multiple WTA modules with inter-module connections
- **Patterns**: Moderately sparse binary patterns

### Seven Hebbian Rules Tested

| Rule | Description | Capacity | Robustness |
|------|-------------|----------|------------|
| Additive Hebb | Δw = pre × post | **Worst** | Low |
| Covariance | Δw = (pre - μ_pre)(post - μ_post) | Moderate | **High** |
| Bayesian-Hebbian | Probabilistic update based on posterior | **Highest** | High |
| *(4 others)* | Various normalized/covariance variants | Varies | Varies |

### Key Findings

1. **Additive Hebb rule** has the worst capacity across all conditions
2. **Covariance learning** is robust but offers only moderate capacity
3. **Bayesian-Hebbian rules** consistently show the highest capacity in almost all tested conditions
4. **Modular architectures** generally outperform non-modular for both storage and prototype extraction
5. **Correlation sensitivity** varies significantly across rules — Bayesian rules are most robust

## When to Use Which Rule

| Task | Recommended Rule |
|------|-----------------|
| Maximum storage capacity | Bayesian-Hebbian |
| Robustness to noise/correlations | Covariance learning |
| Simple implementation | Additive Hebb (but expect low capacity) |
| Prototype extraction | Bayesian-Hebbian in modular WTA |
| Few-shot learning | Bayesian-Hebbian |

## Implementation Guidance

### WTA Network with Hebbian Learning

```python
import numpy as np

class WTAAssociativeMemory:
    def __init__(self, n_neurons, sparsity=0.1, rule='bayesian'):
        self.n = n_neurons
        self.sparsity = sparsity
        self.W = np.zeros((n_neurons, n_neurons))
        self.rule = rule
    
    def learn(self, patterns):
        """Apply Hebbian learning rule to patterns."""
        for x in patterns:
            if self.rule == 'additive':
                self.W += np.outer(x, x)
            elif self.rule == 'covariance':
                mu = self.sparsity
                self.W += np.outer(x - mu, x - mu)
            elif self.rule == 'bayesian':
                # Bayesian update with prior
                prior = 1.0 / self.n
                posterior = x / (x + (1-x) * (prior / (1-prior)))
                self.W += np.outer(posterior, x)
    
    def recall(self, cue):
        """Retrieve pattern using WTA dynamics."""
        state = cue.copy()
        for _ in range(10):  # iterations
            activation = self.W @ state
            # WTA: keep only top-k active
            k = int(self.sparsity * self.n)
            state = np.zeros_like(state)
            indices = np.argsort(activation)[-k:]
            state[indices] = 1
        return state
```

### Capacity Measurement

```python
def measure_capacity(network, n_patterns, n_trials=50):
    """Measure how many patterns can be stored and recalled."""
    success = 0
    for _ in range(n_trials):
        patterns = generate_sparse_patterns(n_patterns, network.n, network.sparsity)
        network.learn(patterns)
        for p in patterns:
            # Corrupt 20% of bits
            cue = corrupt(p, noise=0.2)
            recalled = network.recall(cue)
            if np.array_equal(recalled, p):
                success += 1
    return success / (n_trials * n_patterns)
```

### Prototype Extraction

When training set contains distorted instances of underlying prototypes:

```python
def prototype_extraction(network, distorted_patterns, n_prototypes):
    """Network should converge to generating prototype from distorted instances."""
    network.learn(distorted_patterns)
    # Query with new distorted instance
    probe = distort(prototype, noise=0.3)
    result = network.recall(probe)
    # Should match the original prototype, not any training instance
    return result
```

## Pitfalls

- **Additive Hebb saturates quickly**: weights grow unbounded without normalization
- **Correlated patterns**: severely reduce capacity for simple Hebb rules
- **Prototype vs. memorization**: network may memorize specific instances rather than extracting prototypes
- **Modular vs. non-modular**: modular WTA has higher capacity but requires careful inter-module weight design
- **Sparsity matters**: optimal sparsity depends on rule — Bayesian-Hebbian works well at moderate sparsity (~0.1)

## References

- Lansner et al. (2026). "Benchmarking local Hebbian learning rules for memory
  storage and prototype extraction." arXiv:2605.01074 [cs.NE].
- Willshaw et al. (1969). A simple model of short-term memory.
- Tsodyks & Feigel'man (1988). Enhanced storage capacity in neural networks.
