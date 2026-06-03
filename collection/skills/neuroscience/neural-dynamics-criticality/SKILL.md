---
name: neural-dynamics-criticality
description: "Framework for analyzing critical dynamics in neural systems. Covers neuronal avalanches, power-law distributions, self-organized criticality (SOC), and their implications for brain function. Activation: criticality, avalanches, power-law, SOC, neural criticality."
---

# Neural Dynamics and Criticality Analysis

## Overview

Neural criticality refers to the hypothesis that the brain operates near a critical point, balancing between order and disorder. This framework provides methods to analyze critical dynamics in neural systems, including neuronal avalanches, power-law distributions, and self-organized criticality.

## Key Concepts

### Neuronal Avalanches

Neuronal avalanches are cascades of activity that propagate through neural networks, characterized by:
- **Spatial extent**: Number of electrodes/neurons activated
- **Duration**: Time span of the cascade
- **Size distribution**: Often follows power-law: P(s) ~ s^(-α)

### Power-Law Analysis

Critical systems exhibit power-law distributions:
```
P(x) = C * x^(-α)
```

Where α (alpha) is the power-law exponent. For neuronal avalanches: α ≈ 1.5 (theoretical) or α ≈ 2.0 (experimental)

### Self-Organized Criticality (SOC)

SOC is a property of dynamical systems that naturally evolve to a critical state without external tuning.

## Methodology

### Avalanche Detection

```python
import numpy as np

def detect_avalanches(spike_times, bin_size=0.001, threshold=0):
    """Detect neuronal avalanches from spike data."""
    max_time = np.max(spike_times)
    bins = np.arange(0, max_time + bin_size, bin_size)
    spike_counts, _ = np.histogram(spike_times, bins=bins)
    
    avalanches = []
    in_avalanche = False
    current_avalanche = []
    
    for count in spike_counts:
        if count > threshold:
            if not in_avalanche:
                in_avalanche = True
                current_avalanche = []
            current_avalanche.append(count)
        else:
            if in_avalanche:
                avalanches.append(current_avalanche)
                in_avalanche = False
    
    sizes = [sum(a) for a in avalanches]
    durations = [len(a) for a in avalanches]
    
    return sizes, durations
```

### Power-Law Fitting

```python
def fit_power_law(data, xmin=None):
    """Fit power-law distribution using maximum likelihood."""
    if xmin is None:
        xmin = min(data)
    
    filtered_data = data[data >= xmin]
    n = len(filtered_data)
    alpha = 1 + n / np.sum(np.log(filtered_data / xmin))
    
    return alpha, xmin
```

### Criticality Assessment

```python
def analyze_criticality(spike_times, sampling_rate=1000):
    """Complete criticality analysis pipeline."""
    sizes, durations = detect_avalanches(spike_times, bin_size=1.0/sampling_rate)
    alpha_size, _ = fit_power_law(np.array(sizes))
    sigma = 1 - 1/np.mean(sizes) if np.mean(sizes) > 1 else 0
    
    is_critical = 1.3 < alpha_size < 1.7 and 0.9 < sigma < 1.1
    
    return {
        'alpha_size': alpha_size,
        'branching_ratio': sigma,
        'is_critical': is_critical,
        'num_avalanches': len(sizes)
    }
```

## References

- Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23(35), 11167-11177.
- Munoz, M. A. (2018). Colloquium: Criticality and dynamical scaling in living systems. *Reviews of Modern Physics*, 90(3), 031001.

## Activation Keywords

- criticality
- neural criticality
- neuronal avalanches
- power-law
- self-organized criticality
- SOC
- branching ratio


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`
