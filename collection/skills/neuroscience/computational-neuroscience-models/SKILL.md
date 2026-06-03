---
name: computational-neuroscience-models
description: "Foundational neuron and network models in computational neuroscience. Covers Hodgkin-Huxley, FitzHugh-Nagumo, Izhikevich, and integrate-and-fire models. Activation: neuron model, Hodgkin-Huxley, FitzHugh-Nagumo, Izhikevich, integrate-and-fire."
---

# Computational Neuroscience: Canonical Models

## Overview

Computational neuroscience uses mathematical models to understand neural function. This skill covers canonical models from detailed biophysical to simplified phenomenological models.

## Key Concepts

### Model Hierarchy

From detailed to abstract:
1. **Hodgkin-Huxley**: Ion channel dynamics
2. **FitzHugh-Nagumo**: Phase plane reduction
3. **Izhikevich**: Two-dimensional simplification
4. **Integrate-and-fire**: Threshold models

## Methodology

### Hodgkin-Huxley Model

```python
import numpy as np
from scipy.integrate import odeint

class HodgkinHuxley:
    """Hodgkin-Huxley neuron model."""
    
    def __init__(self, C_m=1.0, g_Na=120.0, g_K=36.0, g_L=0.3,
                 E_Na=50.0, E_K=-77.0, E_L=-54.4):
        self.C_m = C_m
        self.g_Na = g_Na
        self.g_K = g_K
        self.g_L = g_L
        self.E_Na = E_Na
        self.E_K = E_K
        self.E_L = E_L
    
    def alpha_n(self, V):
        return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))
    
    def beta_n(self, V):
        return 0.125 * np.exp(-(V + 65) / 80)
    
    def alpha_m(self, V):
        return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))
    
    def beta_m(self, V):
        return 4.0 * np.exp(-(V + 65) / 18)
    
    def alpha_h(self, V):
        return 0.07 * np.exp(-(V + 65) / 20)
    
    def beta_h(self, V):
        return 1.0 / (1 + np.exp(-(V + 35) / 10))
    
    def derivatives(self, state, t, I_ext):
        V, n, m, h = state
        dn = self.alpha_n(V) * (1 - n) - self.beta_n(V) * n
        dm = self.alpha_m(V) * (1 - m) - self.beta_m(V) * m
        dh = self.alpha_h(V) * (1 - h) - self.beta_h(V) * h
        
        I_Na = self.g_Na * m**3 * h * (V - self.E_Na)
        I_K = self.g_K * n**4 * (V - self.E_K)
        I_L = self.g_L * (V - self.E_L)
        
        dV = (I_ext - I_Na - I_K - I_L) / self.C_m
        return [dV, dn, dm, dh]
```

### Izhikevich Model

```python
class Izhikevich:
    """Izhikevich neuron model."""
    
    PRESETS = {
        'regular_spiking': {'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8},
        'fast_spiking': {'a': 0.1, 'b': 0.2, 'c': -65, 'd': 2},
    }
    
    def __init__(self, a=0.02, b=0.2, c=-65, d=8, v_thresh=30):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.v_thresh = v_thresh
    
    @classmethod
    def from_preset(cls, preset_name):
        params = cls.PRESETS[preset_name]
        return cls(**params)
    
    def simulate(self, I_ext, t_span, dt=0.25, v_init=-65):
        t = np.arange(t_span[0], t_span[1], dt)
        n_steps = len(t)
        v = np.zeros(n_steps)
        u = np.zeros(n_steps)
        v[0] = v_init
        u[0] = self.b * v_init
        spikes = []
        
        for i in range(n_steps - 1):
            dv = (0.04 * v[i]**2 + 5 * v[i] + 140 - u[i] + I_ext) * dt
            du = (self.a * (self.b * v[i] - u[i])) * dt
            v[i+1] = v[i] + dv
            u[i+1] = u[i] + du
            
            if v[i+1] >= self.v_thresh:
                spikes.append(t[i+1])
                v[i+1] = self.c
                u[i+1] = u[i+1] + self.d
        
        return t, v, u, np.array(spikes)
```

### Leaky Integrate-and-Fire

```python
class LeakyIntegrateFire:
    """Leaky Integrate-and-Fire neuron."""
    
    def __init__(self, tau_m=20.0, v_rest=-70.0, v_thresh=-55.0,
                 v_reset=-70.0, R=10.0):
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.R = R
    
    def simulate(self, I_ext, t_span, dt=0.1):
        t = np.arange(t_span[0], t_span[1], dt)
        n_steps = len(t)
        v = np.zeros(n_steps)
        v[0] = self.v_rest
        spikes = []
        
        for i in range(n_steps - 1):
            dv = (-(v[i] - self.v_rest) + self.R * I_ext / 1000) * dt / self.tau_m
            v[i+1] = v[i] + dv
            
            if v[i+1] >= self.v_thresh:
                spikes.append(t[i+1])
                v[i+1] = self.v_reset
        
        return t, v, np.array(spikes)
```

## Model Selection Guide

| Model | Complexity | Speed | Use Case |
|-------|-----------|-------|----------|
| Hodgkin-Huxley | High | Slow | Biophysical accuracy |
| Izhikevich | Low | Fast | Large networks |
| LIF | Very Low | Very Fast | Abstract analysis |

## References

- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current. *The Journal of Physiology*, 117(4), 500-544.
- Izhikevich, E. M. (2007). *Dynamical Systems in Neuroscience*. MIT Press.
- Dayan, P., & Abbott, L. F. (2001). *Theoretical Neuroscience*. MIT Press.

## Activation Keywords

- neuron model
- Hodgkin-Huxley
- FitzHugh-Nagumo
- Izhikevich
- integrate-and-fire


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

**User:** 请解释 Computational Neuroscience Models

**Agent:** Computational Neuroscience Models 是关于...
