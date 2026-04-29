---
name: modeling-self-sustained-neuron-population-without-external
description: "Methodology for modeling self-sustained neural activity in recurrent networks without external input. Based on Hodgkin-Huxley networks with STDP and intrinsic stochasticity. Use when: modeling autonomous neural activity, studying persistent activity mechanisms, simulating biophysical neural networks, investigating spontaneous activity patterns, or designing recurrent networks with plasticity."
---

# Modeling Self-Sustained Neural Activity Without External Stimulus

## Overview

Self-sustained neural activity without ongoing external input is a fundamental property of nervous systems. This skill provides methodology for building and analyzing biophysical recurrent networks that maintain autonomous activity after brief transient stimulation.

## Source Paper

- **Title**: Modeling of Self-sustained Neuron Population without External Stimulus
- **Authors**: İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak
- **arXiv**: 2604.13719v1
- **Published**: 2026-04-15
- **Categories**: cs.NE, q-bio.NC

## Core Mechanism

Self-sustained activity emerges from three factors:
1. **Recurrent connectivity** — 80% connection probability enables reverberating activity
2. **STDP** — Both excitatory and inhibitory STDP maintain weight distributions supporting sustained firing
3. **Intrinsic stochasticity** — Probabilistic vesicle release, synapse formation, receptor variability

## Network Parameters

```
Excitatory neurons: 160 (80%)
Inhibitory neurons: 40 (20%)
Connection probability: 80%
Neuron model: Hodgkin-Huxley
Initialization: 200ms stimulus to 30 excitatory neurons
Post-init: NO external input
```

## Key Results

| Metric | Value | Interpretation |
|--------|-------|---------------|
| Mean firing rate | 1.13 ± 1.34 Hz | Sparse irregular firing |
| Neurons < 1 Hz | 67% | Dominant sparse regime |
| Fano factor | 1-2 | Irregular spike timing |
| Simulation | 1800 s | Long-duration persistence |

## Implementation

```python
import numpy as np

class SelfSustainedNetwork:
    def __init__(self, n_exc=160, n_inh=40, p_conn=0.8):
        self.N = n_exc + n_inh
        self.W = np.random.binomial(1, p_conn, (self.N, self.N))
        np.fill_diagonal(self.W, 0)
        self.p_release = 0.5
        
    def initialize(self):
        """200ms brief stimulus, then no further input."""
        pass
        
    def apply_stdp(self, dt, A_plus=0.01, A_minus=-0.012, tau=20.0):
        if dt > 0:
            return A_plus * np.exp(-dt / tau)
        return A_minus * np.exp(dt / tau)
        
    def analyze(self, spike_trains, duration_ms):
        rates = [len(s) / (duration_ms / 1000) for s in spike_trains]
        return {
            'mean_rate': np.mean(rates),
            'sparse_fraction': sum(1 for r in rates if r < 1.0) / len(rates),
            'fano': np.var(rates) / np.mean(rates) if np.mean(rates) > 0 else 0
        }
```

## Critical Design Requirements

- STDP is essential (without it, activity dies or becomes epileptic)
- Stochasticity prevents synchronization
- 80/20 E/I ratio maintains stable dynamics
- Brief initialization only — then zero external drive

## Activation Keywords

- self-sustained activity, autonomous neural activity, persistent activity, Hodgkin-Huxley recurrent, spontaneous activity


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Modeling Self Sustained Neuron Population Without External

**Agent:** Modeling Self Sustained Neuron Population Without External 是关于...
